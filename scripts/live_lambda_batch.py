"""Probe Lambda control-plane abuse on one disposable, inert function."""

from __future__ import annotations

import argparse
import io
import json
import secrets
import time
import zipfile

import boto3
from botocore.exceptions import ClientError


def code_archive() -> bytes:
    output = io.BytesIO()
    with zipfile.ZipFile(output, "w") as archive:
        archive.writestr("handler.py", "def main(event, context):\n    return {'ok': True}\n")
    return output.getvalue()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", required=True)
    args = parser.parse_args()
    session = boto3.Session(profile_name=args.profile, region_name="us-east-1")
    account = session.client("sts").get_caller_identity()["Account"]
    iam, client = session.client("iam"), session.client("lambda")
    suffix = secrets.token_hex(5)
    role_name = f"peasso-detect-lambda-role-{suffix}"
    function_name = f"peasso-detect-lambda-{suffix}"
    role_created = function_created = url_created = permission_created = False
    completed: list[str] = []
    cleanup_errors: list[str] = []
    print(f"run={suffix} account={account} function={function_name} role={role_name}", flush=True)
    trust = {"Version": "2012-10-17", "Statement": [{
        "Effect": "Allow", "Principal": {"Service": "lambda.amazonaws.com"},
        "Action": "sts:AssumeRole"}]}
    try:
        role_arn = iam.create_role(RoleName=role_name,
                                   AssumeRolePolicyDocument=json.dumps(trust),
                                   Tags=[{"Key": "peasso-detection-test", "Value": suffix}])["Role"]["Arn"]
        role_created = True
        for attempt in range(18):
            try:
                client.create_function(FunctionName=function_name, Runtime="python3.12",
                                       Role=role_arn, Handler="handler.main",
                                       Code={"ZipFile": code_archive()},
                                       Description="Disposable, inert PEASSo detection test",
                                       Tags={"peasso-detection-test": suffix})
                function_created = True
                completed.append("CreateFunction")
                break
            except ClientError as exc:
                code = exc.response["Error"]["Code"]
                if code != "InvalidParameterValueException" or attempt == 17:
                    raise
                time.sleep(5)
        for attempt in range(20):
            state = client.get_function_configuration(FunctionName=function_name)["State"]
            if state == "Active":
                break
            if state == "Failed" or attempt == 19:
                raise RuntimeError(f"Lambda setup state: {state}")
            time.sleep(3)
        client.put_function_concurrency(FunctionName=function_name, ReservedConcurrentExecutions=0)
        completed.append("PutFunctionConcurrency:zero")
        client.put_function_recursion_config(FunctionName=function_name, RecursiveLoop="Allow")
        completed.append("PutFunctionRecursionConfig:allow")
        client.create_function_url_config(FunctionName=function_name, AuthType="NONE")
        url_created = True
        completed.append("CreateFunctionUrlConfig:none")
        client.add_permission(FunctionName=function_name, StatementId=f"public-url-{suffix}",
                              Action="lambda:InvokeFunctionUrl", Principal="*",
                              FunctionUrlAuthType="NONE")
        permission_created = True
        completed.append("AddPermission:public-url")
        client.remove_permission(FunctionName=function_name, StatementId=f"public-url-{suffix}")
        permission_created = False
        completed.append("RemovePermission")
        client.delete_function_url_config(FunctionName=function_name)
        url_created = False
        completed.append("DeleteFunctionUrlConfig")
        client.delete_function(FunctionName=function_name)
        function_created = False
        completed.append("DeleteFunction")
        print("completed=" + ",".join(completed), flush=True)
    finally:
        def clean(label, call, **kwargs):
            try:
                call(**kwargs)
            except ClientError as exc:
                if exc.response["Error"]["Code"] not in {
                        "ResourceNotFoundException", "NoSuchEntity", "NoSuchEntityException"}:
                    cleanup_errors.append(f"{label}:{exc.response['Error']['Code']}")

        if permission_created:
            clean("permission", client.remove_permission, FunctionName=function_name,
                  StatementId=f"public-url-{suffix}")
        if url_created:
            clean("url", client.delete_function_url_config, FunctionName=function_name)
        if function_created:
            clean("function", client.delete_function, FunctionName=function_name)
        if role_created:
            clean("role", iam.delete_role, RoleName=role_name)
        try:
            client.get_function(FunctionName=function_name)
            cleanup_errors.append("function:still-present")
        except ClientError as exc:
            if exc.response["Error"]["Code"] != "ResourceNotFoundException":
                cleanup_errors.append(f"function-check:{exc.response['Error']['Code']}")
        try:
            iam.get_role(RoleName=role_name)
            cleanup_errors.append("role:still-present")
        except ClientError as exc:
            if exc.response["Error"]["Code"] != "NoSuchEntity":
                cleanup_errors.append(f"role-check:{exc.response['Error']['Code']}")
        print("cleanup=" + ("ok" if not cleanup_errors else ",".join(cleanup_errors)), flush=True)
        if cleanup_errors:
            raise RuntimeError("Lambda test cleanup incomplete")


if __name__ == "__main__":
    main()
