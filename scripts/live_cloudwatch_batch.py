"""Exercise CloudWatch alarm and dashboard changes on disposable resources."""

from __future__ import annotations

import argparse
import json
import secrets

import boto3
from botocore.exceptions import ClientError


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", required=True)
    args = parser.parse_args()
    session = boto3.Session(profile_name=args.profile, region_name="us-east-1")
    account = session.client("sts").get_caller_identity()["Account"]
    client = session.client("cloudwatch")
    suffix = secrets.token_hex(5)
    alarm = f"peasso-detect-alarm-{suffix}"
    dashboard = f"peasso-detect-dashboard-{suffix}"
    alarm_created = dashboard_created = False
    completed: list[str] = []
    cleanup_errors: list[str] = []
    print(f"run={suffix} account={account} alarm={alarm} dashboard={dashboard}", flush=True)
    try:
        metric_alarm = dict(AlarmName=alarm, AlarmDescription="Disposable PEASSo detection test",
                            MetricName="NoSuchMetric", Namespace="PeassoDetectionTest",
                            Statistic="Sum", Period=300, EvaluationPeriods=1,
                            Threshold=1, ComparisonOperator="GreaterThanThreshold",
                            TreatMissingData="notBreaching")
        client.put_metric_alarm(**metric_alarm, ActionsEnabled=True)
        alarm_created = True
        completed.append("PutMetricAlarm")
        client.disable_alarm_actions(AlarmNames=[alarm])
        completed.append("DisableAlarmActions")
        client.put_metric_alarm(**metric_alarm, ActionsEnabled=False)
        completed.append("PutMetricAlarm:actions-disabled")
        client.set_alarm_state(AlarmName=alarm, StateValue="OK", StateReason="Disposable detection test")
        completed.append("SetAlarmState:OK")
        client.enable_alarm_actions(AlarmNames=[alarm])
        completed.append("EnableAlarmActions")
        client.put_dashboard(DashboardName=dashboard,
                             DashboardBody=json.dumps({"widgets": [{"type": "text", "x": 0, "y": 0,
                                 "width": 6, "height": 3,
                                 "properties": {"markdown": "Disposable PEASSo detection test"}}]}))
        dashboard_created = True
        completed.append("PutDashboard")
        client.delete_dashboards(DashboardNames=[dashboard])
        dashboard_created = False
        completed.append("DeleteDashboards")
        client.delete_alarms(AlarmNames=[alarm])
        alarm_created = False
        completed.append("DeleteAlarms")
        print("completed=" + ",".join(completed), flush=True)
    finally:
        if dashboard_created:
            try:
                client.delete_dashboards(DashboardNames=[dashboard])
            except ClientError as exc:
                cleanup_errors.append(f"dashboard:{exc.response['Error']['Code']}")
        if alarm_created:
            try:
                client.delete_alarms(AlarmNames=[alarm])
            except ClientError as exc:
                cleanup_errors.append(f"alarm:{exc.response['Error']['Code']}")
        if client.describe_alarms(AlarmNames=[alarm]).get("MetricAlarms"):
            cleanup_errors.append("alarm:still-present")
        if any(item["DashboardName"] == dashboard for item in
               client.list_dashboards(DashboardNamePrefix=dashboard).get("DashboardEntries", [])):
            cleanup_errors.append("dashboard:still-present")
        print("cleanup=" + ("ok" if not cleanup_errors else ",".join(cleanup_errors)), flush=True)
        if cleanup_errors:
            raise RuntimeError("CloudWatch test cleanup incomplete")


if __name__ == "__main__":
    main()
