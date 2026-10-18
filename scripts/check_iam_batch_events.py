"""Check disposable IAM probe events against the local rule pack without saving logs."""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import boto3


NAMES = ("AttachUserPolicy", "PutUserPolicy", "CreateLoginProfile", "UpdateLoginProfile", "UpdateAccessKey")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", required=True)
    parser.add_argument("--run", required=True, help="Hex suffix printed by live_iam_batch.py")
    parser.add_argument("--wait-seconds", type=int, default=0)
    args = parser.parse_args()
    sys.path.insert(0, "/Users/carlospolop/git/Blue-CloudPEASS")
    from peaso.attack_detection.rules import detect_aws_events, load_rules

    actor = f"peasso-detect-actor-{args.run}"
    rules = load_rules(Path(__file__).resolve().parents[1] / "rules", product="aws")
    client = boto3.Session(profile_name=args.profile, region_name="us-east-1").client("cloudtrail")
    deadline = time.monotonic() + args.wait_seconds
    while True:
        found = {}
        for name in NAMES:
            pages = client.get_paginator("lookup_events").paginate(
                LookupAttributes=[{"AttributeKey": "EventName", "AttributeValue": name}],
                PaginationConfig={"MaxItems": 500, "PageSize": 50},
            )
            for page in pages:
                for row in page["Events"]:
                    record = json.loads(row["CloudTrailEvent"])
                    if (record.get("userIdentity") or {}).get("userName") != actor:
                        continue
                    detections = detect_aws_events([record], rules)
                    found[name] = {
                        "event_id": record.get("eventID"),
                        "error": record.get("errorCode"),
                        "detected": [item.technique_id for item in detections],
                    }
        print(json.dumps(found, sort_keys=True), flush=True)
        if len(found) == len(NAMES) or time.monotonic() >= deadline:
            break
        time.sleep(30)


if __name__ == "__main__":
    main()
