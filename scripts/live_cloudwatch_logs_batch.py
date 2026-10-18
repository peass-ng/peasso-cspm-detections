"""Probe CloudWatch Logs retention and evidence deletion on disposable logs."""

from __future__ import annotations

import argparse
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
    client = session.client("logs")
    suffix = secrets.token_hex(5)
    group = f"/peasso/detection-test/{suffix}"
    stream = "synthetic-events"
    filter_name = f"peasso-detect-filter-{suffix}"
    group_created = stream_created = filter_created = False
    completed: list[str] = []
    cleanup_errors: list[str] = []
    print(f"run={suffix} account={account} group={group} stream={stream}", flush=True)
    try:
        client.create_log_group(logGroupName=group, tags={"peasso-detection-test": suffix})
        group_created = True
        completed.append("CreateLogGroup")
        client.create_log_stream(logGroupName=group, logStreamName=stream)
        stream_created = True
        completed.append("CreateLogStream")
        client.put_log_events(logGroupName=group, logStreamName=stream,
                              logEvents=[{"timestamp": int(time.time() * 1000),
                                          "message": '{"level":"ERROR","test":"disposable"}'}])
        completed.append("PutLogEvents:synthetic")
        client.put_metric_filter(logGroupName=group, filterName=filter_name,
                                 filterPattern='{ $.level = "ERROR" }',
                                 metricTransformations=[{"metricName": "SyntheticErrors",
                                                         "metricNamespace": "PeassoDetectionTest",
                                                         "metricValue": "1"}])
        filter_created = True
        completed.append("PutMetricFilter")
        client.put_retention_policy(logGroupName=group, retentionInDays=1)
        completed.append("PutRetentionPolicy:one-day")
        client.delete_retention_policy(logGroupName=group)
        completed.append("DeleteRetentionPolicy")
        client.delete_metric_filter(logGroupName=group, filterName=filter_name)
        filter_created = False
        completed.append("DeleteMetricFilter")
        client.delete_log_stream(logGroupName=group, logStreamName=stream)
        stream_created = False
        completed.append("DeleteLogStream")
        client.delete_log_group(logGroupName=group)
        group_created = False
        completed.append("DeleteLogGroup")
        print("completed=" + ",".join(completed), flush=True)
    finally:
        def clean(label, call, **kwargs):
            try:
                call(**kwargs)
            except ClientError as exc:
                if exc.response["Error"]["Code"] != "ResourceNotFoundException":
                    cleanup_errors.append(f"{label}:{exc.response['Error']['Code']}")
        if filter_created:
            clean("filter", client.delete_metric_filter, logGroupName=group,
                  filterName=filter_name)
        if stream_created:
            clean("stream", client.delete_log_stream, logGroupName=group,
                  logStreamName=stream)
        if group_created:
            clean("group", client.delete_log_group, logGroupName=group)
        if client.describe_log_groups(logGroupNamePrefix=group).get("logGroups"):
            cleanup_errors.append("group:still-present")
        print("cleanup=" + ("ok" if not cleanup_errors else ",".join(cleanup_errors)), flush=True)
        if cleanup_errors:
            raise RuntimeError("CloudWatch Logs test cleanup incomplete")


if __name__ == "__main__":
    main()
