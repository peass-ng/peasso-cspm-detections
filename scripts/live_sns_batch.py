"""Run six SNS topic abuse probes with disposable topic, queue and IAM user."""

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
    sns, sqs, iam = session.client("sns"), session.client("sqs"), session.client("iam")
    suffix = secrets.token_hex(5)
    topic_name = f"peasso-detect-sns-{suffix}"
    queue_name = f"peasso-detect-sns-queue-{suffix}"
    user = f"peasso-detect-sns-user-{suffix}"
    label = f"account-{suffix}"
    topic_arn = None
    queue_url = None
    subscription_arn = None
    user_created = False
    completed = []
    cleanup_errors = []
    print(f"run={suffix} topic={topic_name} queue={queue_name} user={user}", flush=True)
    try:
        user_arn = iam.create_user(UserName=user, Tags=[{"Key": "peasso-detection-test", "Value": suffix}])["User"]["Arn"]
        user_created = True
        topic_arn = sns.create_topic(Name=topic_name)["TopicArn"]
        queue_url = sqs.create_queue(QueueName=queue_name)["QueueUrl"]
        queue_arn = f"arn:aws:sqs:us-east-1:{account}:{queue_name}"
        delivery_policy = {"Version": "2012-10-17", "Statement": [{
            "Effect": "Allow", "Principal": {"Service": "sns.amazonaws.com"},
            "Action": "sqs:SendMessage", "Resource": queue_arn,
            "Condition": {"ArnEquals": {"aws:SourceArn": topic_arn}}}]}
        sqs.set_queue_attributes(QueueUrl=queue_url, Attributes={"Policy": json.dumps(delivery_policy)})
        sns.add_permission(TopicArn=topic_arn, Label=label,
                           AWSAccountId=[account], ActionName=["Subscribe"])
        completed.append("AddPermission:account-principal")
        sns.remove_permission(TopicArn=topic_arn, Label=label)
        completed.append("RemovePermission:account-principal")
        topic_policy = json.loads(sns.get_topic_attributes(TopicArn=topic_arn)["Attributes"]["Policy"])
        topic_policy.setdefault("Statement", []).append({
            "Sid": "DisposableControlledUser", "Effect": "Allow",
            "Principal": {"AWS": user_arn}, "Action": "sns:Subscribe", "Resource": topic_arn})
        for attempt in range(12):
            try:
                sns.set_topic_attributes(TopicArn=topic_arn, AttributeName="Policy",
                                         AttributeValue=json.dumps(topic_policy))
                break
            except ClientError as exc:
                if exc.response["Error"]["Code"] not in {"InvalidParameter", "InvalidParameterValue"} or attempt == 11:
                    raise
                time.sleep(5)
        completed.append("SetTopicAttributes:controlled-user-policy")
        subscription_arn = sns.subscribe(TopicArn=topic_arn, Protocol="sqs", Endpoint=queue_arn,
                                         ReturnSubscriptionArn=True)["SubscriptionArn"]
        completed.append("Subscribe:controlled-queue")
        sns.publish(TopicArn=topic_arn, Message="disposable peasso detection test")
        delivered = False
        for _ in range(5):
            if sqs.receive_message(QueueUrl=queue_url, WaitTimeSeconds=2).get("Messages"):
                delivered = True
                break
        print("synthetic_delivery=" + ("observed" if delivered else "not_observed"), flush=True)
        sns.unsubscribe(SubscriptionArn=subscription_arn)
        subscription_arn = None
        completed.append("Unsubscribe")
        sns.delete_topic(TopicArn=topic_arn)
        topic_arn = None
        completed.append("DeleteTopic")
        print("completed=" + ",".join(completed), flush=True)
    finally:
        def clean(label, call, **kwargs):
            try:
                call(**kwargs)
            except ClientError as exc:
                if exc.response["Error"]["Code"] not in {"NotFound", "NotFoundException", "NoSuchEntity",
                        "AWS.SimpleQueueService.NonExistentQueue"}:
                    cleanup_errors.append(f"{label}:{exc.response['Error']['Code']}")

        if subscription_arn and subscription_arn != "pending confirmation":
            clean("subscription", sns.unsubscribe, SubscriptionArn=subscription_arn)
        if topic_arn:
            clean("topic", sns.delete_topic, TopicArn=topic_arn)
        if queue_url:
            clean("queue", sqs.delete_queue, QueueUrl=queue_url)
        if user_created:
            clean("user", iam.delete_user, UserName=user)
        print("cleanup=" + ("ok" if not cleanup_errors else ",".join(cleanup_errors)), flush=True)
        if cleanup_errors:
            raise RuntimeError("SNS test cleanup incomplete")


if __name__ == "__main__":
    main()
