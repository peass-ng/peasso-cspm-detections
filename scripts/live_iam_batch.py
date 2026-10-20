"""Run five disposable IAM audit probes; print no keys or passwords.

Usage: python3 scripts/live_iam_batch.py --profile AWS_LAB_PROFILE
All resources are uniquely prefixed and removed in a finally block.
"""

from __future__ import annotations

import argparse
import json
import secrets
import time

import boto3
from botocore.exceptions import ClientError


ADMIN = "arn:aws:iam::aws:policy/AdministratorAccess"
POLICY = json.dumps({"Version": "2012-10-17", "Statement": [
    {"Effect": "Allow", "Action": "*", "Resource": "*"}
]})


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", required=True)
    args = parser.parse_args()
    session = boto3.Session(profile_name=args.profile)
    iam = session.client("iam")
    suffix = secrets.token_hex(5)
    actor = f"peasso-detect-actor-{suffix}"
    target = f"peasso-detect-target-{suffix}"
    key = None
    target_key = None
    completed: list[str] = []
    cleanup_errors: list[str] = []
    print(f"run={suffix} actor={actor} target={target}", flush=True)
    try:
        iam.create_user(UserName=actor, Tags=[{"Key": "peasso-detection-test", "Value": suffix}])
        iam.create_user(UserName=target, Tags=[{"Key": "peasso-detection-test", "Value": suffix}])
        # Bootstrap permission is required to issue the five calls as this IAM user.
        iam.put_user_policy(UserName=actor, PolicyName="test-bootstrap", PolicyDocument=POLICY)
        key = iam.create_access_key(UserName=actor)["AccessKey"]
        target_key = iam.create_access_key(UserName=target)["AccessKey"]
        iam.update_access_key(UserName=target, AccessKeyId=target_key["AccessKeyId"], Status="Inactive")
        actor_session = boto3.Session(
            aws_access_key_id=key["AccessKeyId"],
            aws_secret_access_key=key["SecretAccessKey"],
            region_name="us-east-1",
        )
        actor_iam = actor_session.client("iam")
        # Eventual consistency of the bootstrap IAM policy.
        for attempt in range(12):
            try:
                actor_session.client("sts").get_caller_identity()
                actor_iam.attach_user_policy(UserName=actor, PolicyArn=ADMIN)
                completed.append("AttachUserPolicy:self-admin")
                break
            except ClientError as exc:
                if exc.response["Error"]["Code"] not in {"AccessDenied", "NoSuchEntity", "InvalidClientTokenId"} or attempt == 11:
                    raise
                time.sleep(5)
        actor_iam.put_user_policy(UserName=actor, PolicyName="test-self-admin", PolicyDocument=POLICY)
        completed.append("PutUserPolicy:self-admin")
        actor_iam.create_login_profile(UserName=target, Password=secrets.token_urlsafe(28) + "Aa1!", PasswordResetRequired=False)
        completed.append("CreateLoginProfile:other-user")
        actor_iam.update_login_profile(UserName=target, Password=secrets.token_urlsafe(28) + "Aa1!", PasswordResetRequired=False)
        completed.append("UpdateLoginProfile:other-user")
        actor_iam.update_access_key(UserName=target, AccessKeyId=target_key["AccessKeyId"], Status="Active")
        completed.append("UpdateAccessKey:other-user-active")
        print("completed=" + ",".join(completed), flush=True)
    finally:
        def clean(label: str, call, **kwargs) -> None:
            try:
                call(**kwargs)
            except ClientError as exc:
                if exc.response["Error"]["Code"] != "NoSuchEntity":
                    cleanup_errors.append(f"{label}:{exc.response['Error']['Code']}")

        clean("target-profile", iam.delete_login_profile, UserName=target)
        if target_key:
            clean("target-key", iam.delete_access_key, UserName=target, AccessKeyId=target_key["AccessKeyId"])
        clean("target-user", iam.delete_user, UserName=target)
        clean("actor-admin", iam.detach_user_policy, UserName=actor, PolicyArn=ADMIN)
        clean("actor-test-policy", iam.delete_user_policy, UserName=actor, PolicyName="test-self-admin")
        clean("actor-bootstrap", iam.delete_user_policy, UserName=actor, PolicyName="test-bootstrap")
        if key:
            clean("actor-key", iam.delete_access_key, UserName=actor, AccessKeyId=key["AccessKeyId"])
        clean("actor-user", iam.delete_user, UserName=actor)
        print("cleanup=" + ("ok" if not cleanup_errors else ",".join(cleanup_errors)), flush=True)
        if cleanup_errors:
            raise RuntimeError("IAM cleanup incomplete")


if __name__ == "__main__":
    main()
