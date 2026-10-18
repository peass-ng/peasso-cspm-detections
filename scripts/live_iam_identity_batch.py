"""Run five disposable IAM identity and credential probes, then delete resources."""

from __future__ import annotations

import argparse
import secrets
from datetime import datetime, timedelta, timezone

import boto3
from botocore.exceptions import ClientError
from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.x509.oid import NameOID


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", required=True)
    args = parser.parse_args()
    iam = boto3.Session(profile_name=args.profile).client("iam")
    suffix = secrets.token_hex(5)
    user = f"peasso-identity-{suffix}"
    oidc_url = f"https://id.example.com/peasso-{suffix}"
    provider_arn = None
    certificate_id = None
    completed = []
    cleanup_errors = []
    print(f"run={suffix} user={user}", flush=True)
    try:
        iam.create_user(UserName=user, Tags=[{"Key": "peasso-detection-test", "Value": suffix}])
        key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        subject = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "peasso-disposable-test")])
        now = datetime.now(timezone.utc)
        cert = (x509.CertificateBuilder().subject_name(subject).issuer_name(subject)
                .public_key(key.public_key()).serial_number(x509.random_serial_number())
                .not_valid_before(now - timedelta(minutes=1))
                .not_valid_after(now + timedelta(days=1))
                .sign(key, hashes.SHA256()))
        pem = cert.public_bytes(Encoding.PEM).decode()
        certificate_id = iam.upload_signing_certificate(UserName=user, CertificateBody=pem)["Certificate"]["CertificateId"]
        completed.append("UploadSigningCertificate:other-user")
        iam.update_user(UserName=user, NewPath="/peasso-test/")
        completed.append("UpdateUser:path-change")
        provider_arn = iam.create_open_id_connect_provider(
            Url=oidc_url, ClientIDList=["sts.amazonaws.com"], ThumbprintList=["a" * 40]
        )["OpenIDConnectProviderArn"]
        completed.append("CreateOpenIDConnectProvider")
        iam.add_client_id_to_open_id_connect_provider(
            OpenIDConnectProviderArn=provider_arn, ClientID=f"peasso-{suffix}")
        completed.append("AddClientIDToOpenIDConnectProvider")
        iam.update_open_id_connect_provider_thumbprint(
            OpenIDConnectProviderArn=provider_arn, ThumbprintList=["b" * 40])
        completed.append("UpdateOpenIDConnectProviderThumbprint")
        print("completed=" + ",".join(completed), flush=True)
    finally:
        def clean(label, call, **kwargs):
            try:
                call(**kwargs)
            except ClientError as exc:
                if exc.response["Error"]["Code"] != "NoSuchEntity":
                    cleanup_errors.append(f"{label}:{exc.response['Error']['Code']}")

        if provider_arn:
            clean("oidc", iam.delete_open_id_connect_provider, OpenIDConnectProviderArn=provider_arn)
        if certificate_id:
            clean("certificate", iam.delete_signing_certificate,
                  UserName=user, CertificateId=certificate_id)
        clean("user", iam.delete_user, UserName=user)
        print("cleanup=" + ("ok" if not cleanup_errors else ",".join(cleanup_errors)), flush=True)
        if cleanup_errors:
            raise RuntimeError("IAM identity cleanup incomplete")


if __name__ == "__main__":
    main()
