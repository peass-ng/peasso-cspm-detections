"""Run five disposable CloudTrail tampering probes in us-east-1 and clean up."""

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
    cloudtrail = session.client("cloudtrail")
    s3 = session.client("s3")
    suffix = secrets.token_hex(5)
    trail = f"peasso-detect-trail-{suffix}"
    bucket = f"peasso-detect-trail-{account}-{suffix}"
    arn = f"arn:aws:cloudtrail:us-east-1:{account}:trail/{trail}"
    bucket_created = False
    trail_created = False
    completed = []
    cleanup_errors = []
    print(f"run={suffix} trail={trail} bucket={bucket}", flush=True)
    try:
        s3.create_bucket(Bucket=bucket)
        bucket_created = True
        policy = {"Version": "2012-10-17", "Statement": [
            {"Sid": "CloudTrailAcl", "Effect": "Allow", "Principal": {"Service": "cloudtrail.amazonaws.com"},
             "Action": "s3:GetBucketAcl", "Resource": f"arn:aws:s3:::{bucket}",
             "Condition": {"StringEquals": {"aws:SourceArn": arn}}},
            {"Sid": "CloudTrailWrite", "Effect": "Allow", "Principal": {"Service": "cloudtrail.amazonaws.com"},
             "Action": "s3:PutObject", "Resource": f"arn:aws:s3:::{bucket}/AWSLogs/{account}/*",
             "Condition": {"StringEquals": {"aws:SourceArn": arn, "s3:x-amz-acl": "bucket-owner-full-control"}}},
        ]}
        s3.put_bucket_policy(Bucket=bucket, Policy=json.dumps(policy))
        cloudtrail.create_trail(Name=trail, S3BucketName=bucket,
                                IsMultiRegionTrail=True, IncludeGlobalServiceEvents=True,
                                EnableLogFileValidation=True)
        trail_created = True
        cloudtrail.start_logging(Name=trail)
        cloudtrail.update_trail(Name=trail, EnableLogFileValidation=False)
        completed.append("UpdateTrail:validation-off")
        cloudtrail.update_trail(Name=trail, IsMultiRegionTrail=False, IncludeGlobalServiceEvents=False)
        completed.append("UpdateTrail:region-and-global-off")
        cloudtrail.put_event_selectors(TrailName=trail, EventSelectors=[
            {"ReadWriteType": "ReadOnly", "IncludeManagementEvents": True, "DataResources": []}])
        completed.append("PutEventSelectors:read-only-management")
        cloudtrail.stop_logging(Name=trail)
        completed.append("StopLogging")
        cloudtrail.delete_trail(Name=trail)
        trail_created = False
        completed.append("DeleteTrail")
        print("completed=" + ",".join(completed), flush=True)
    finally:
        if trail_created:
            try:
                cloudtrail.stop_logging(Name=trail)
            except ClientError as exc:
                if exc.response["Error"]["Code"] != "TrailNotFoundException":
                    cleanup_errors.append("stop:" + exc.response["Error"]["Code"])
            try:
                cloudtrail.delete_trail(Name=trail)
            except ClientError as exc:
                if exc.response["Error"]["Code"] != "TrailNotFoundException":
                    cleanup_errors.append("trail:" + exc.response["Error"]["Code"])
        if bucket_created:
            for attempt in range(10):
                try:
                    for page in s3.get_paginator("list_objects_v2").paginate(Bucket=bucket):
                        objects = [{"Key": obj["Key"]} for obj in page.get("Contents", [])]
                        if objects:
                            s3.delete_objects(Bucket=bucket, Delete={"Objects": objects})
                    s3.delete_bucket(Bucket=bucket)
                    break
                except ClientError as exc:
                    if exc.response["Error"]["Code"] != "BucketNotEmpty" or attempt == 9:
                        cleanup_errors.append("bucket:" + exc.response["Error"]["Code"])
                        break
                    time.sleep(3)
        print("cleanup=" + ("ok" if not cleanup_errors else ",".join(cleanup_errors)), flush=True)
        if cleanup_errors:
            raise RuntimeError("CloudTrail test cleanup incomplete")


if __name__ == "__main__":
    main()
