"""Run six disposable SQS queue abuse probes with one synthetic message."""

from __future__ import annotations

import argparse
import json
import secrets
import time

import boto3
from botocore.exceptions import ClientError


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", required=True)
    args = parser.parse_args()
    session = boto3.Session(profile_name=args.profile, region_name="us-east-1")
    account = session.client("sts").get_caller_identity()["Account"]
    sqs = session.client("sqs")
    iam = session.client("iam")
    suffix = secrets.token_hex(5)
    queue = f"peasso-detect-sqs-{suffix}"
    user = f"peasso-detect-sqs-user-{suffix}"
    label = f"account-{suffix}"
    queue_url = None
    user_created = False
    completed = []
    cleanup_errors = []
    print(f"run={suffix} queue={queue} user={user}", flush=True)
    try:
        user_arn = iam.create_user(UserName=user, Tags=[{"Key": "peasso-detection-test", "Value": suffix}])["User"]["Arn"]
        user_created = True
        queue_url = sqs.create_queue(QueueName=queue)["QueueUrl"]
        queue_arn = f"arn:aws:sqs:us-east-1:{account}:{queue}"
        sqs.add_permission(QueueUrl=queue_url, Label=label,
                           AWSAccountIds=[account], Actions=["ReceiveMessage"])
        completed.append("AddPermission:account-principal")
        sqs.remove_permission(QueueUrl=queue_url, Label=label)
        completed.append("RemovePermission:account-principal")
        policy = {"Version": "2012-10-17", "Statement": [{
            "Sid": "DisposableControlledUser", "Effect": "Allow",
            "Principal": {"AWS": user_arn}, "Action": "sqs:ReceiveMessage",
            "Resource": queue_arn}]}
        for attempt in range(12):
            try:
                sqs.set_queue_attributes(QueueUrl=queue_url, Attributes={"Policy": json.dumps(policy)})
                break
            except ClientError as exc:
                if exc.response["Error"]["Code"] != "InvalidAttributeValue" or attempt == 11:
                    raise
                time.sleep(5)
        completed.append("SetQueueAttributes:controlled-user-policy")
        sqs.set_queue_attributes(QueueUrl=queue_url, Attributes={"MessageRetentionPeriod": "60"})
        completed.append("SetQueueAttributes:retention-60")
        sqs.send_message(QueueUrl=queue_url, MessageBody="disposable peasso detection test")
        sqs.purge_queue(QueueUrl=queue_url)
        completed.append("PurgeQueue")
        sqs.delete_queue(QueueUrl=queue_url)
        queue_url = None
        completed.append("DeleteQueue")
        print("completed=" + ",".join(completed), flush=True)
    finally:
        if queue_url:
            try:
                sqs.delete_queue(QueueUrl=queue_url)
            except ClientError as exc:
                if exc.response["Error"]["Code"] != "AWS.SimpleQueueService.NonExistentQueue":
                    cleanup_errors.append("queue:" + exc.response["Error"]["Code"])
        if user_created:
            try:
                iam.delete_user(UserName=user)
            except ClientError as exc:
                if exc.response["Error"]["Code"] != "NoSuchEntity":
                    cleanup_errors.append("user:" + exc.response["Error"]["Code"])
        print("cleanup=" + ("ok" if not cleanup_errors else ",".join(cleanup_errors)), flush=True)
        if cleanup_errors:
            raise RuntimeError("SQS test cleanup incomplete")


if __name__ == "__main__":
    main()
