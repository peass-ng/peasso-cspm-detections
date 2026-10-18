"""Probe EC2 metadata downgrades and public ingress on disposable resources."""

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
    ec2 = session.client("ec2")
    ami = session.client("ssm").get_parameter(
        Name="/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64"
    )["Parameter"]["Value"]
    vpc = next(x["VpcId"] for x in ec2.describe_vpcs()["Vpcs"] if x["IsDefault"])
    subnet = next(x["SubnetId"] for x in ec2.describe_subnets(
        Filters=[{"Name": "vpc-id", "Values": [vpc]}])["Subnets"] if x.get("DefaultForAz"))
    suffix = secrets.token_hex(5)
    group_name = f"peasso-detect-ec2-{suffix}"
    group_id = instance_id = None
    completed: list[str] = []
    cleanup_errors: list[str] = []
    print(f"run={suffix} account={account} group={group_name} subnet={subnet}", flush=True)
    try:
        group_id = ec2.create_security_group(GroupName=group_name,
                                             Description="Disposable PEASSo detection test",
                                             VpcId=vpc)["GroupId"]
        completed.append("CreateSecurityGroup")
        result = ec2.run_instances(
            ImageId=ami, MinCount=1, MaxCount=1, InstanceType="t3.micro",
            NetworkInterfaces=[{"DeviceIndex": 0, "SubnetId": subnet,
                                "Groups": [group_id], "AssociatePublicIpAddress": False,
                                "DeleteOnTermination": True}],
            MetadataOptions={"HttpEndpoint": "enabled", "HttpTokens": "required",
                             "HttpPutResponseHopLimit": 1},
            TagSpecifications=[{"ResourceType": resource_type, "Tags": [
                {"Key": "Name", "Value": f"peasso-detect-ec2-{suffix}"},
                {"Key": "peasso-detection-test", "Value": suffix}]}
                for resource_type in ("instance", "volume")],
        )
        instance_id = result["Instances"][0]["InstanceId"]
        completed.append("RunInstances")
        print(f"instance={instance_id}", flush=True)
        ec2.get_waiter("instance_running").wait(InstanceIds=[instance_id],
                                                  WaiterConfig={"Delay": 5, "MaxAttempts": 36})
        ec2.authorize_security_group_ingress(GroupId=group_id, IpPermissions=[{
            "IpProtocol": "tcp", "FromPort": 22, "ToPort": 22,
            "IpRanges": [{"CidrIp": "0.0.0.0/0", "Description": "Disposable detection test"}]}])
        completed.append("AuthorizeSecurityGroupIngress:public-ssh")
        ec2.revoke_security_group_ingress(GroupId=group_id, IpPermissions=[{
            "IpProtocol": "tcp", "FromPort": 22, "ToPort": 22,
            "IpRanges": [{"CidrIp": "0.0.0.0/0"}]}])
        completed.append("RevokeSecurityGroupIngress")

        def wait_metadata():
            for attempt in range(24):
                details = ec2.describe_instances(InstanceIds=[instance_id])["Reservations"][0]["Instances"][0]
                if details["MetadataOptions"]["State"] == "applied":
                    return details
                if attempt == 23:
                    raise RuntimeError("EC2 metadata options did not apply")
                time.sleep(5)

        ec2.modify_instance_metadata_options(InstanceId=instance_id, HttpTokens="optional")
        completed.append("ModifyInstanceMetadataOptions:optional")
        wait_metadata()
        ec2.modify_instance_metadata_options(InstanceId=instance_id,
                                             HttpEndpoint="enabled", HttpPutResponseHopLimit=2)
        completed.append("ModifyInstanceMetadataOptions:hop-2")
        wait_metadata()
        ec2.modify_instance_metadata_options(InstanceId=instance_id, HttpTokens="required",
                                             HttpEndpoint="enabled", HttpPutResponseHopLimit=1)
        completed.append("ModifyInstanceMetadataOptions:restore")
        wait_metadata()
        ec2.terminate_instances(InstanceIds=[instance_id])
        completed.append("TerminateInstances")
        print("completed=" + ",".join(completed), flush=True)
    finally:
        if not instance_id:
            found = ec2.describe_instances(Filters=[
                {"Name": "tag:peasso-detection-test", "Values": [suffix]},
                {"Name": "instance-state-name", "Values": ["pending", "running", "stopping", "stopped"]},
            ])["Reservations"]
            if found:
                instance_id = found[0]["Instances"][0]["InstanceId"]
        if instance_id:
            try:
                state = ec2.describe_instances(InstanceIds=[instance_id])["Reservations"][0]["Instances"][0]["State"]["Name"]
                if state not in {"shutting-down", "terminated"}:
                    ec2.terminate_instances(InstanceIds=[instance_id])
                ec2.get_waiter("instance_terminated").wait(InstanceIds=[instance_id],
                                                            WaiterConfig={"Delay": 5, "MaxAttempts": 60})
            except ClientError as exc:
                if exc.response["Error"]["Code"] != "InvalidInstanceID.NotFound":
                    cleanup_errors.append(f"instance:{exc.response['Error']['Code']}")
            except Exception as exc:
                cleanup_errors.append(f"instance:{type(exc).__name__}")
        for attempt in range(18):
            volumes = ec2.describe_volumes(Filters=[
                {"Name": "tag:peasso-detection-test", "Values": [suffix]}])["Volumes"]
            if not volumes:
                break
            if attempt == 17:
                cleanup_errors.extend(f"volume:still-present:{volume['VolumeId']}" for volume in volumes)
            else:
                time.sleep(5)
        if group_id:
            for attempt in range(18):
                try:
                    ec2.delete_security_group(GroupId=group_id)
                    break
                except ClientError as exc:
                    if exc.response["Error"]["Code"] == "InvalidGroup.NotFound":
                        break
                    if exc.response["Error"]["Code"] != "DependencyViolation" or attempt == 17:
                        cleanup_errors.append(f"group:{exc.response['Error']['Code']}")
                        break
                    time.sleep(5)
            try:
                ec2.describe_security_groups(GroupIds=[group_id])
                cleanup_errors.append("group:still-present")
            except ClientError as exc:
                if exc.response["Error"]["Code"] != "InvalidGroup.NotFound":
                    cleanup_errors.append(f"group-check:{exc.response['Error']['Code']}")
        print("cleanup=" + ("ok" if not cleanup_errors else ",".join(cleanup_errors)), flush=True)
        if cleanup_errors:
            raise RuntimeError("EC2 test cleanup incomplete")


if __name__ == "__main__":
    main()
