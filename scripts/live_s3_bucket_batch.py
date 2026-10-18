"""Probe five S3 bucket abuse surfaces on an empty disposable bucket."""

from __future__ import annotations

import argparse
import json
import secrets

import boto3
from botocore.exceptions import ClientError


BLOCK_ALL = {"BlockPublicAcls": True, "IgnorePublicAcls": True,
             "BlockPublicPolicy": True, "RestrictPublicBuckets": True}
ALLOW_ALL = {key: False for key in BLOCK_ALL}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", required=True)
    args = parser.parse_args()
    session = boto3.Session(profile_name=args.profile, region_name="us-east-1")
    s3 = session.client("s3")
    account = session.client("sts").get_caller_identity()["Account"]
    suffix = secrets.token_hex(5)
    bucket = f"peasso-detect-s3-{account}-{suffix}"
    created = False
    completed = []
    cleanup_errors = []
    print(f"run={suffix} bucket={bucket}", flush=True)
    try:
        s3.create_bucket(Bucket=bucket)
        created = True
        s3.put_public_access_block(Bucket=bucket, PublicAccessBlockConfiguration=ALLOW_ALL)
        completed.append("PutPublicAccessBlock:all-off")
        policy = {"Version": "2012-10-17", "Statement": [{
            "Sid": "DisposablePublicRead", "Effect": "Allow", "Principal": "*",
            "Action": "s3:GetObject", "Resource": f"arn:aws:s3:::{bucket}/*",
        }]}
        s3.put_bucket_policy(Bucket=bucket, Policy=json.dumps(policy))
        completed.append("PutBucketPolicy:public-read")
        s3.put_bucket_ownership_controls(Bucket=bucket, OwnershipControls={"Rules": [{
            "ObjectOwnership": "BucketOwnerPreferred"}]})
        s3.put_bucket_acl(Bucket=bucket, ACL="public-read")
        completed.append("PutBucketAcl:public-read")
        s3.put_bucket_website(Bucket=bucket, WebsiteConfiguration={
            "RedirectAllRequestsTo": {"HostName": "example.com", "Protocol": "https"}})
        completed.append("PutBucketWebsite:redirect")
        s3.put_bucket_cors(Bucket=bucket, CORSConfiguration={"CORSRules": [{
            "AllowedMethods": ["GET"], "AllowedOrigins": ["*"], "AllowedHeaders": ["*"],
            "MaxAgeSeconds": 3600}]})
        completed.append("PutBucketCors:wildcard-origin")
        print("completed=" + ",".join(completed), flush=True)
    finally:
        if created:
            def clean(label, call, **kwargs):
                try:
                    call(**kwargs)
                except ClientError as exc:
                    if exc.response["Error"]["Code"] not in {
                            "NoSuchBucket", "NoSuchBucketPolicy", "NoSuchWebsiteConfiguration",
                            "NoSuchCORSConfiguration", "NoSuchOwnershipControls"}:
                        cleanup_errors.append(f"{label}:{exc.response['Error']['Code']}")

            # Revoke access before trying to delete the bucket.
            clean("public-block", s3.put_public_access_block,
                  Bucket=bucket, PublicAccessBlockConfiguration=BLOCK_ALL)
            clean("policy", s3.delete_bucket_policy, Bucket=bucket)
            clean("acl", s3.put_bucket_acl, Bucket=bucket, ACL="private")
            clean("website", s3.delete_bucket_website, Bucket=bucket)
            clean("cors", s3.delete_bucket_cors, Bucket=bucket)
            clean("bucket", s3.delete_bucket, Bucket=bucket)
        print("cleanup=" + ("ok" if not cleanup_errors else ",".join(cleanup_errors)), flush=True)
        if cleanup_errors:
            raise RuntimeError("S3 test cleanup incomplete")


if __name__ == "__main__":
    main()
