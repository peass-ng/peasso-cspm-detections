"""Exercise disposable GuardDuty detector and suppression-filter changes."""

from __future__ import annotations

import argparse
import secrets

import boto3
from botocore.exceptions import ClientError


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", required=True)
    args = parser.parse_args()
    session = boto3.Session(profile_name=args.profile, region_name="us-east-1")
    account = session.client("sts").get_caller_identity()["Account"]
    client = session.client("guardduty")
    if client.list_detectors()["DetectorIds"]:
        raise RuntimeError("GuardDuty detector already exists in this Region; refusing to alter it")
    suffix = secrets.token_hex(5)
    name = f"peasso-detection-test-{suffix}"
    detector = None
    filter_created = False
    completed: list[str] = []
    cleanup_errors: list[str] = []
    print(f"run={suffix} account={account} filter={name}", flush=True)
    criteria = {"Criterion": {"type": {"Eq": ["UnauthorizedAccess:IAMUser/ConsoleLoginSuccess.B"]}}}
    try:
        detector = client.create_detector(Enable=True, Tags={"peasso-detection-test": suffix})["DetectorId"]
        completed.append("CreateDetector")
        client.create_filter(DetectorId=detector, Name=name, Action="ARCHIVE", Rank=1,
                             FindingCriteria=criteria)
        filter_created = True
        completed.append("CreateFilter:ARCHIVE")
        client.update_filter(DetectorId=detector, FilterName=name, Action="NOOP", Rank=1)
        completed.append("UpdateFilter:NOOP")
        client.update_filter(DetectorId=detector, FilterName=name, Action="ARCHIVE", Rank=1)
        completed.append("UpdateFilter:ARCHIVE")
        client.update_detector(DetectorId=detector, Enable=False)
        completed.append("UpdateDetector:disable")
        client.update_detector(DetectorId=detector, Enable=True)
        completed.append("UpdateDetector:enable")
        client.delete_filter(DetectorId=detector, FilterName=name)
        filter_created = False
        completed.append("DeleteFilter")
        client.delete_detector(DetectorId=detector)
        detector = None
        completed.append("DeleteDetector")
        print("completed=" + ",".join(completed), flush=True)
    finally:
        if detector is not None:
            if filter_created:
                try:
                    client.delete_filter(DetectorId=detector, FilterName=name)
                except ClientError as exc:
                    if exc.response["Error"]["Code"] != "BadRequestException":
                        cleanup_errors.append(f"filter:{exc.response['Error']['Code']}")
            try:
                client.delete_detector(DetectorId=detector)
            except ClientError as exc:
                cleanup_errors.append(f"detector:{exc.response['Error']['Code']}")
        remaining = client.list_detectors()["DetectorIds"]
        if remaining:
            cleanup_errors.append("detectors:still-present:" + ",".join(remaining))
        print("cleanup=" + ("ok" if not cleanup_errors else ",".join(cleanup_errors)), flush=True)
        if cleanup_errors:
            raise RuntimeError("GuardDuty test cleanup incomplete")


if __name__ == "__main__":
    main()
