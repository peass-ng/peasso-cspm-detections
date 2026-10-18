"""Five further disposable IAM techniques, with cleanup in finally."""

from __future__ import annotations

import argparse
import json
import secrets
import time

import boto3
from botocore.exceptions import ClientError
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


ADMIN = "arn:aws:iam::aws:policy/AdministratorAccess"
ADMIN_DOC = json.dumps({"Version": "2012-10-17", "Statement": [
    {"Effect": "Allow", "Action": "*", "Resource": "*"}]})
LIMITED_DOC = json.dumps({"Version": "2012-10-17", "Statement": [
    {"Effect": "Allow", "Action": "s3:ListAllMyBuckets", "Resource": "*"}]})


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", required=True)
    args = parser.parse_args()
    iam = boto3.Session(profile_name=args.profile).client("iam")
    suffix = secrets.token_hex(5)
    actor, target, group, role, policy = (f"peasso-b2-{kind}-{suffix}"
                                          for kind in ("actor", "target", "group", "role", "policy"))
    key = None
    ssh_key_id = None
    policy_arn = None
    version_id = None
    completed = []
    cleanup_errors = []
    print(f"run={suffix} actor={actor} target={target}", flush=True)
    try:
        iam.create_user(UserName=actor)
        iam.create_user(UserName=target)
        iam.put_user_policy(UserName=actor, PolicyName="test-bootstrap", PolicyDocument=ADMIN_DOC)
        key = iam.create_access_key(UserName=actor)["AccessKey"]
        iam.create_group(GroupName=group)
        iam.attach_group_policy(GroupName=group, PolicyArn=ADMIN)
        policy_arn = iam.create_policy(PolicyName=policy, PolicyDocument=LIMITED_DOC)["Policy"]["Arn"]
        iam.attach_user_policy(UserName=actor, PolicyArn=policy_arn)
        trust = {"Version": "2012-10-17", "Statement": [
            {"Effect": "Allow", "Principal": {"Service": "ec2.amazonaws.com"}, "Action": "sts:AssumeRole"}]}
        iam.create_role(RoleName=role, AssumeRolePolicyDocument=json.dumps(trust))
        actor_session = boto3.Session(aws_access_key_id=key["AccessKeyId"],
                                      aws_secret_access_key=key["SecretAccessKey"],
                                      region_name="us-east-1")
        actor_iam = actor_session.client("iam")
        for attempt in range(12):
            try:
                actor_iam.create_policy_version(PolicyArn=policy_arn, PolicyDocument=ADMIN_DOC, SetAsDefault=True)
                completed.append("CreatePolicyVersion:admin-default")
                break
            except ClientError as exc:
                if exc.response["Error"]["Code"] not in {"InvalidClientTokenId", "AccessDenied", "NoSuchEntity"} or attempt == 11:
                    raise
                time.sleep(5)
        actor_iam.set_default_policy_version(PolicyArn=policy_arn, VersionId="v1")
        actor_iam.set_default_policy_version(PolicyArn=policy_arn, VersionId="v2")
        completed.append("SetDefaultPolicyVersion:admin")
        actor_iam.add_user_to_group(GroupName=group, UserName=actor)
        completed.append("AddUserToGroup:admin-group")
        wildcard = {"Version": "2012-10-17", "Statement": [
            {"Effect": "Allow", "Principal": {"AWS": "*"}, "Action": "sts:AssumeRole"}]}
        actor_iam.update_assume_role_policy(RoleName=role, PolicyDocument=json.dumps(wildcard))
        completed.append("UpdateAssumeRolePolicy:wildcard")
        public_key = rsa.generate_private_key(public_exponent=65537, key_size=2048).public_key().public_bytes(
            serialization.Encoding.OpenSSH, serialization.PublicFormat.OpenSSH).decode()
        ssh_key_id = actor_iam.upload_ssh_public_key(UserName=target, SSHPublicKeyBody=public_key)["SSHPublicKey"]["SSHPublicKeyId"]
        completed.append("UploadSSHPublicKey:other-user")
        print("completed=" + ",".join(completed), flush=True)
    finally:
        def clean(label, call, **kwargs):
            try:
                call(**kwargs)
            except ClientError as exc:
                if exc.response["Error"]["Code"] != "NoSuchEntity":
                    cleanup_errors.append(f"{label}:{exc.response['Error']['Code']}")

        if ssh_key_id:
            clean("ssh-key", iam.delete_ssh_public_key, UserName=target, SSHPublicKeyId=ssh_key_id)
        clean("target", iam.delete_user, UserName=target)
        clean("group-membership", iam.remove_user_from_group, GroupName=group, UserName=actor)
        clean("group-policy", iam.detach_group_policy, GroupName=group, PolicyArn=ADMIN)
        clean("group", iam.delete_group, GroupName=group)
        clean("role", iam.delete_role, RoleName=role)
        if policy_arn:
            clean("policy-detach", iam.detach_user_policy, UserName=actor, PolicyArn=policy_arn)
            clean("policy-default", iam.set_default_policy_version, PolicyArn=policy_arn, VersionId="v1")
            clean("policy-v2", iam.delete_policy_version, PolicyArn=policy_arn, VersionId="v2")
            clean("policy", iam.delete_policy, PolicyArn=policy_arn)
        clean("bootstrap", iam.delete_user_policy, UserName=actor, PolicyName="test-bootstrap")
        if key:
            clean("actor-key", iam.delete_access_key, UserName=actor, AccessKeyId=key["AccessKeyId"])
        clean("actor", iam.delete_user, UserName=actor)
        print("cleanup=" + ("ok" if not cleanup_errors else ",".join(cleanup_errors)), flush=True)
        if cleanup_errors:
            raise RuntimeError("IAM cleanup incomplete")


if __name__ == "__main__":
    main()
