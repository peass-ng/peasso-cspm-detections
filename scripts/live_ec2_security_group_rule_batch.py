"""Probe in-place SSH/RDP ingress edits on an unattached disposable group."""

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
    ec2 = session.client("ec2")
    vpc = next(x["VpcId"] for x in ec2.describe_vpcs()["Vpcs"] if x["IsDefault"])
    suffix = secrets.token_hex(5)
    group_name = f"peasso-detect-sg-edit-{suffix}"
    group_id = None
    completed: list[str] = []
    cleanup_errors: list[str] = []
    print(f"run={suffix} account={account} group={group_name}", flush=True)
    try:
        group_id = ec2.create_security_group(GroupName=group_name,
                                             Description="Disposable PEASSo rule edit test",
                                             VpcId=vpc)["GroupId"]
        ec2.create_tags(Resources=[group_id], Tags=[{"Key": "peasso-detection-test", "Value": suffix}])
        completed.append("CreateSecurityGroup")
        result = ec2.authorize_security_group_ingress(GroupId=group_id, IpPermissions=[{
            "IpProtocol": "tcp", "FromPort": port, "ToPort": port,
            "IpRanges": [{"CidrIp": "192.0.2.0/32", "Description": "Disposable baseline"}]}
            for port in (22, 3389)])
        ids = {item["FromPort"]: item["SecurityGroupRuleId"] for item in result["SecurityGroupRules"]}
        assert set(ids) == {22, 3389}
        completed.append("AuthorizeSecurityGroupIngress:restricted-baseline")

        def edit(port: int, cidr: str) -> None:
            ec2.modify_security_group_rules(GroupId=group_id, SecurityGroupRules=[{
                "SecurityGroupRuleId": ids[port],
                "SecurityGroupRule": {"IpProtocol": "tcp", "FromPort": port,
                                      "ToPort": port, "CidrIpv4": cidr,
                                      "Description": "Disposable PEASSo rule edit test"}}])

        for port in (22, 3389):
            edit(port, "0.0.0.0/0")
            completed.append(f"ModifySecurityGroupRules:public-{port}")
            edit(port, "192.0.2.0/32")
            completed.append(f"ModifySecurityGroupRules:restore-{port}")
        ec2.revoke_security_group_ingress(GroupId=group_id, SecurityGroupRuleIds=list(ids.values()))
        completed.append("RevokeSecurityGroupIngress")
        ec2.delete_security_group(GroupId=group_id)
        group_id = None
        completed.append("DeleteSecurityGroup")
        print("completed=" + ",".join(completed), flush=True)
    finally:
        if group_id:
            try:
                ec2.delete_security_group(GroupId=group_id)
            except ClientError as exc:
                if exc.response["Error"]["Code"] != "InvalidGroup.NotFound":
                    cleanup_errors.append(f"group:{exc.response['Error']['Code']}")
        remaining = ec2.describe_security_groups(Filters=[
            {"Name": "group-name", "Values": [group_name]},
            {"Name": "vpc-id", "Values": [vpc]}])["SecurityGroups"]
        if remaining:
            cleanup_errors.append("group:still-present")
        print("cleanup=" + ("ok" if not cleanup_errors else ",".join(cleanup_errors)), flush=True)
        if cleanup_errors:
            raise RuntimeError("EC2 security group rule test cleanup incomplete")


if __name__ == "__main__":
    main()
