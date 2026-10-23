# AWS attack-page action review queue

Pinned HackTricks Cloud source: `47c375ae496ae89f81936f47ab1cb84885c88373`. This lists **all** attack-page
Markdown files in the five AWS attack categories, including pages that already
have a rule reference. It is an index for further semantic review, not a count
of attacks, tested techniques, or missing detectors. IAM actions can have a
different CloudTrail event name, no standalone event, or an existing broader rule.
An exact event-name match also does not prove detection of the described route.
H3 headings can be setup or background, and attack routes may appear outside H3.

- Pages: **578**; direct YAML reference: **269**; no direct reference: **309**.
- H3 headings: **1713**; exact action-name mentions: **619**;
  mentions without an exact YAML event name: **669**; headings without
  a backticked `service:Action`: **889**.

The [work plan](WORK_PLAN.md) contains the full no-reference census and
live-test receipts. The [high-heading review](AWS_COVERAGE_REVIEW.md) lists
pages with at least three H3 headings and no direct YAML reference.

## Page index

| Source page | Direct YAML ref | H3 | Exact action name | No exact name | Manual H3 |
| --- | :---: | ---: | ---: | ---: | ---: |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sso-and-identitystore-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sso-and-identitystore-privesc/README.md) | no | 15 | 3 | 17 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-firewall-manager-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-firewall-manager-post-exploitation/README.md) | no | 5 | 0 | 10 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sso-and-identitystore-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sso-and-identitystore-post-exploitation/README.md) | no | 5 | 0 | 6 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-elemental-inference-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-elemental-inference-post-exploitation/README.md) | no | 5 | 0 | 5 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-security-agent-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-security-agent-post-exploitation/README.md) | no | 5 | 0 | 5 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-snowball-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-snowball-post-exploitation/README.md) | no | 5 | 1 | 5 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codestar-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codestar-privesc/README.md) | no | 3 | 0 | 5 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-macie-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-macie-post-exploitation/README.md) | no | 5 | 0 | 4 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-timestream-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-timestream-post-exploitation/README.md) | no | 6 | 2 | 4 | 1 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codeconnections-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codeconnections-privesc/README.md) | no | 2 | 0 | 4 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudfront-data-access-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudfront-data-access-post-exploitation/README.md) | no | 2 | 0 | 4 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-data-exchange-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-data-exchange-post-exploitation/README.md) | no | 2 | 0 | 4 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ebs-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ebs-privesc/README.md) | no | 2 | 0 | 4 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/route53-createhostedzone-route53-changeresourcerecordsets-acm-pca-issuecertificate-acm-pca-getcer/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/route53-createhostedzone-route53-changeresourcerecordsets-acm-pca-issuecertificate-acm-pca-getcer/README.md) | no | 1 | 1 | 4 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-drs-mgn-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-drs-mgn-post-exploitation/README.md) | no | 2 | 0 | 3 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-mainframe-modernization-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-mainframe-modernization-post-exploitation/README.md) | no | 3 | 0 | 3 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-pinpoint-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-pinpoint-post-exploitation/README.md) | no | 3 | 0 | 3 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-rtb-fabric-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-rtb-fabric-post-exploitation/README.md) | no | 3 | 0 | 3 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-datapipeline-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-datapipeline-privesc/README.md) | no | 1 | 1 | 3 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-pca-connector-ad-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-pca-connector-ad-privesc/README.md) | no | 3 | 0 | 3 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-workspaces-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-workspaces-privesc/README.md) | no | 1 | 0 | 3 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-end-user-messaging-social-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-end-user-messaging-social-post-exploitation/README.md) | no | 3 | 0 | 2 | 1 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-mediapackage-v2-policy-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-mediapackage-v2-policy-persistence/README.md) | no | 2 | 0 | 2 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-memorydb-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-memorydb-persistence/README.md) | no | 2 | 2 | 2 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-security-incident-response-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-security-incident-response-persistence/README.md) | no | 2 | 0 | 2 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-acm-pca-scep-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-acm-pca-scep-post-exploitation/README.md) | no | 2 | 0 | 2 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-codeguru-profiler-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-codeguru-profiler-post-exploitation/README.md) | no | 2 | 0 | 2 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-dms-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-dms-post-exploitation/README.md) | no | 2 | 0 | 2 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ecs-data-access-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ecs-data-access-post-exploitation/README.md) | no | 2 | 0 | 2 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-elb-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-elb-post-exploitation/README.md) | no | 2 | 0 | 2 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-fsx-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-fsx-post-exploitation/README.md) | no | 1 | 0 | 2 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-healthimaging-data-access-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-healthimaging-data-access-post-exploitation/README.md) | no | 2 | 0 | 2 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-kendra-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-kendra-post-exploitation/README.md) | no | 2 | 1 | 2 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-memorydb-data-access-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-memorydb-data-access-post-exploitation/README.md) | no | 2 | 0 | 2 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-network-security-manager-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-network-security-manager-post-exploitation/README.md) | no | 3 | 1 | 2 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-opensearch-cross-account-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-opensearch-cross-account-post-exploitation/README.md) | no | 1 | 0 | 2 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-pcs-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-pcs-post-exploitation/README.md) | no | 2 | 2 | 2 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-q-in-connect-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-q-in-connect-post-exploitation/README.md) | no | 1 | 0 | 2 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-resource-tag-inventory-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-resource-tag-inventory-post-exploitation/README.md) | no | 2 | 0 | 2 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-route53-resolver-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-route53-resolver-post-exploitation/README.md) | no | 2 | 0 | 2 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-storage-gateway-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-storage-gateway-post-exploitation/README.md) | no | 1 | 0 | 2 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-wickr-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-wickr-post-exploitation/README.md) | no | 3 | 1 | 2 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-workspaces-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-workspaces-post-exploitation/README.md) | no | 2 | 0 | 2 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-chatbot-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-chatbot-privesc/README.md) | no | 1 | 0 | 2 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-gamelift/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-gamelift/README.md) | no | 2 | 1 | 2 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-security-lake-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-security-lake-post-exploitation/README.md) | no | 4 | 0 | 1 | 3 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-workmail-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-workmail-post-exploitation/README.md) | no | 3 | 0 | 1 | 2 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-partner-central-account-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-partner-central-account-post-exploitation/README.md) | no | 2 | 0 | 1 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-workdocs-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-workdocs-post-exploitation/README.md) | no | 4 | 2 | 1 | 1 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-directory-services-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-directory-services-privesc/README.md) | no | 2 | 0 | 1 | 1 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-workdocs-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-workdocs-privesc/README.md) | no | 4 | 2 | 1 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-account-management-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-account-management-post-exploitation/README.md) | no | 1 | 0 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-agent-registry-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-agent-registry-post-exploitation/README.md) | no | 1 | 0 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-app-mesh-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-app-mesh-post-exploitation/README.md) | no | 1 | 0 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-application-discovery-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-application-discovery-post-exploitation/README.md) | no | 2 | 1 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-aurora-dsql-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-aurora-dsql-post-exploitation/README.md) | no | 1 | 0 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-batch-data-disclosure-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-batch-data-disclosure-post-exploitation/README.md) | no | 1 | 0 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudtrail-data-access-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudtrail-data-access-post-exploitation/README.md) | no | 1 | 0 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-connect-health-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-connect-health-post-exploitation/README.md) | no | 1 | 0 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-dlm-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-dlm-post-exploitation/README.md) | no | 1 | 1 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-emr-serverless-configuration-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-emr-serverless-configuration-post-exploitation/README.md) | no | 1 | 0 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-free-tier-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-free-tier-post-exploitation/README.md) | no | 1 | 0 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-medialive-video-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-medialive-video-post-exploitation/README.md) | no | 1 | 0 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-memorydb-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-memorydb-post-exploitation/README.md) | no | 2 | 1 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-msk-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-msk-post-exploitation/README.md) | no | 1 | 0 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-odb-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-odb-post-exploitation/README.md) | no | 1 | 0 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-refactor-spaces-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-refactor-spaces-post-exploitation/README.md) | no | 2 | 2 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-route53-global-resolver-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-route53-global-resolver-post-exploitation/README.md) | no | 1 | 0 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-simpledb-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-simpledb-post-exploitation/README.md) | no | 1 | 0 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-storage-gateway-chap-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-storage-gateway-chap-post-exploitation/README.md) | no | 1 | 0 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-uxc-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-uxc-post-exploitation/README.md) | no | 1 | 0 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cloudcontrol-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cloudcontrol-privesc/README.md) | no | 1 | 1 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-msk-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-msk-privesc/README.md) | no | 1 | 0 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-proton-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-proton-privesc/README.md) | no | 2 | 2 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-quicksight-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-quicksight-privesc/README.md) | no | 2 | 1 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-supply-chain-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-supply-chain-post-exploitation/README.md) | no | 9 | 0 | 0 | 9 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-s3-unauthenticated-enum/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-s3-unauthenticated-enum/README.md) | no | 9 | 0 | 0 | 9 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-security-hub-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-security-hub-post-exploitation/README.md) | no | 6 | 0 | 0 | 6 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-security-incident-response-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-security-incident-response-post-exploitation/README.md) | no | 6 | 0 | 0 | 6 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-shield-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-shield-post-exploitation/README.md) | no | 6 | 0 | 0 | 6 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-accounts-unauthenticated-enum/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-accounts-unauthenticated-enum/README.md) | no | 6 | 0 | 0 | 6 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-eks-unauthenticated-enum/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-eks-unauthenticated-enum/README.md) | no | 6 | 0 | 0 | 6 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-invoicing-and-billing-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-invoicing-and-billing-persistence/README.md) | no | 5 | 0 | 0 | 5 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-audit-manager-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-audit-manager-post-exploitation/README.md) | no | 5 | 0 | 0 | 5 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-codebuild-post-exploitation/aws-codebuild-untrusted-pr-webhook-bypass.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-codebuild-post-exploitation/aws-codebuild-untrusted-pr-webhook-bypass.md) | no | 5 | 0 | 0 | 5 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-gamelift-streams-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-gamelift-streams-post-exploitation/README.md) | no | 5 | 0 | 0 | 5 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-invoicing-and-billing-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-invoicing-and-billing-post-exploitation/README.md) | no | 5 | 0 | 0 | 5 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-cognito-user-pool-unauthenticated-access/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-cognito-user-pool-unauthenticated-access/README.md) | no | 5 | 0 | 0 | 5 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-devops-agent-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-devops-agent-post-exploitation/README.md) | no | 4 | 0 | 0 | 4 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-managed-blockchain-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-managed-blockchain-post-exploitation/README.md) | no | 4 | 0 | 0 | 4 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-partner-central-channel-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-partner-central-channel-post-exploitation/README.md) | no | 4 | 0 | 0 | 4 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-payment-cryptography-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-payment-cryptography-post-exploitation/README.md) | no | 4 | 0 | 0 | 4 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-api-gateway-unauthenticated-enum/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-api-gateway-unauthenticated-enum/README.md) | no | 4 | 0 | 0 | 4 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-cognito-unauthenticated-enum/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-cognito-unauthenticated-enum/README.md) | no | 4 | 0 | 0 | 4 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-iam-and-sts-unauthenticated-enum/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-iam-and-sts-unauthenticated-enum/README.md) | no | 4 | 0 | 0 | 4 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-identity-center-and-sso-unauthenticated-enum/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-identity-center-and-sso-unauthenticated-enum/README.md) | no | 4 | 0 | 0 | 4 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-quicksight-unauthenticated-enum/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-quicksight-unauthenticated-enum/README.md) | no | 4 | 0 | 0 | 4 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-security-hub-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-security-hub-persistence/README.md) | no | 3 | 0 | 0 | 3 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-bedrock-data-access-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-bedrock-data-access-post-exploitation/README.md) | no | 3 | 0 | 0 | 3 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-partner-central-benefits-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-partner-central-benefits-post-exploitation/README.md) | no | 3 | 0 | 0 | 3 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-q-business-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-q-business-post-exploitation/README.md) | no | 3 | 0 | 0 | 3 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-systems-manager-incident-manager-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-systems-manager-incident-manager-post-exploitation/README.md) | no | 3 | 0 | 0 | 3 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/README.md) | no | 3 | 0 | 0 | 3 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-cloudsearch-unauthenticated-enum/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-cloudsearch-unauthenticated-enum/README.md) | no | 3 | 0 | 0 | 3 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-ivs-unauthenticated-access/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-ivs-unauthenticated-access/README.md) | no | 3 | 0 | 0 | 3 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-mq-unauthenticated-enum/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-mq-unauthenticated-enum/README.md) | no | 3 | 0 | 0 | 3 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-neptune-unauthenticated-enum/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-neptune-unauthenticated-enum/README.md) | no | 3 | 0 | 0 | 3 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-subdomain-takeover/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-subdomain-takeover/README.md) | no | 3 | 0 | 0 | 3 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-api-gateway-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-api-gateway-persistence/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-clean-rooms-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-clean-rooms-persistence/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-compute-optimizer-automation-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-compute-optimizer-automation-persistence/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-connect-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-connect-persistence/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-inspector-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-inspector-persistence/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-lightsail-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-lightsail-persistence/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-mediaconnect-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-mediaconnect-persistence/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-step-functions-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-step-functions-persistence/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-appfabric-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-appfabric-post-exploitation/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-bedrock-data-automation-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-bedrock-data-automation-post-exploitation/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-billing-conductor-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-billing-conductor-post-exploitation/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-codebuild-post-exploitation/aws-codebuild-token-leakage.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-codebuild-post-exploitation/aws-codebuild-token-leakage.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-compute-optimizer-automation-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-compute-optimizer-automation-post-exploitation/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-control-tower-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-control-tower-post-exploitation/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-evs-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-evs-post-exploitation/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ground-station-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ground-station-post-exploitation/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-post-exploitation/aws-warm-lambda-persistence.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-post-exploitation/aws-warm-lambda-persistence.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-network-flow-monitor-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-network-flow-monitor-post-exploitation/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-partner-central-revenue-measurement-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-partner-central-revenue-measurement-post-exploitation/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-partner-central-selling-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-partner-central-selling-post-exploitation/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-pricing-calculator-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-pricing-calculator-post-exploitation/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-pricing-plan-manager-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-pricing-plan-manager-post-exploitation/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ssm-gui-connect-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ssm-gui-connect-post-exploitation/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-systems-manager-for-sap-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-systems-manager-for-sap-post-exploitation/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-textract-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-textract-post-exploitation/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-trusted-advisor-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-trusted-advisor-post-exploitation/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-appsync-unauthenticated-enum/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-appsync-unauthenticated-enum/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-connect-participant-unauthenticated-enum/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-connect-participant-unauthenticated-enum/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-datasync-agent-unauthenticated-access/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-datasync-agent-unauthenticated-access/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-device-farm-unauthenticated/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-device-farm-unauthenticated/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-ec2-unauthenticated-enum/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-ec2-unauthenticated-enum/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-invoicing-and-billing-unauthenticated-access/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-invoicing-and-billing-unauthenticated-access/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-kinesis-video-unauthenticated-enum/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-kinesis-video-unauthenticated-enum/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-lex-v2-unauthenticated-enum/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-lex-v2-unauthenticated-enum/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-marketplace-unauthenticated-access/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-marketplace-unauthenticated-access/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-memorydb-unauthenticated-access/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-memorydb-unauthenticated-access/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-msk-unauthenticated-enum/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-msk-unauthenticated-enum/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-rds-unauthenticated-enum/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-rds-unauthenticated-enum/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-timestream-influxdb-unauthenticated-enum/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-timestream-influxdb-unauthenticated-enum/README.md) | no | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/README.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-elemental-inference-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-elemental-inference-persistence/README.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-rds-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-rds-persistence/README.md) | no | 2 | 1 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-sqs-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-sqs-persistence/README.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-user-notifications-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-user-notifications-persistence/README.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-bedrock-agentcore-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-bedrock-agentcore-post-exploitation/README.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudtrail-csv-injection-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudtrail-csv-injection-post-exploitation/README.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cognito-directory-secret-disclosure-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cognito-directory-secret-disclosure-post-exploitation/README.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-connect-campaigns-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-connect-campaigns-post-exploitation/README.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-documentdb-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-documentdb-post-exploitation/README.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/aws-ebs-snapshot-dump.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/aws-ebs-snapshot-dump.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-elastic-beanstalk-secret-disclosure-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-elastic-beanstalk-secret-disclosure-post-exploitation/README.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ivs-chat-room-token-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ivs-chat-room-token-post-exploitation/README.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-post-exploitation/aws-lambda-privileged-event-consumer-injection.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-post-exploitation/aws-lambda-privileged-event-consumer-injection.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-post-exploitation/aws-lambda-vpc-egress-bypass.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-post-exploitation/aws-lambda-vpc-egress-bypass.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-route53-arc-routing-control-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-route53-arc-routing-control-post-exploitation/README.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-signin-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-signin-post-exploitation/README.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-user-notifications-suppression-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-user-notifications-suppression-post-exploitation/README.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-workspaces-appstream-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-workspaces-appstream-post-exploitation/README.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-workspaces-thin-client-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-workspaces-thin-client-post-exploitation/README.md) | no | 2 | 1 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-fis-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-fis-privesc/README.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-iot-sitewise-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-iot-sitewise-privesc/README.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-lake-formation-grants-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-lake-formation-grants-privesc/README.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-macie-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-macie-privesc/README.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-migration-hub-orchestrator-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-migration-hub-orchestrator-privesc/README.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-appconfig-unauthenticated-access/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-appconfig-unauthenticated-access/README.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-codebuild-unauthenticated-access/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-codebuild-unauthenticated-access/README.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-dynamodb-unauthenticated-access/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-dynamodb-unauthenticated-access/README.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-ecr-unauthenticated-enum/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-ecr-unauthenticated-enum/README.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-elastic-beanstalk-unauthenticated-enum/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-elastic-beanstalk-unauthenticated-enum/README.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-elb-unauthenticated-access/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-elb-unauthenticated-access/README.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-gamelift-streams-unauthenticated-access/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-gamelift-streams-unauthenticated-access/README.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-lambda-unauthenticated-access/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-lambda-unauthenticated-access/README.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-location-service-unauthenticated-enum/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-location-service-unauthenticated-enum/README.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-managed-blockchain-unauthenticated-enum/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-managed-blockchain-unauthenticated-enum/README.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-media-unauthenticated-enum/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-media-unauthenticated-enum/README.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-redshift-unauthenticated-enum/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-redshift-unauthenticated-enum/README.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-sagemaker-unauthenticated-enum/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-sagemaker-unauthenticated-enum/README.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-security-incident-response-unauthenticated-access/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-security-incident-response-unauthenticated-access/README.md) | no | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-cross-account-attacks/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-cross-account-attacks/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-cross-account-attacks/cross-service-confused-deputy-attacks.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-cross-account-attacks/cross-service-confused-deputy-attacks.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-cross-account-attacks/detection-and-hardening.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-cross-account-attacks/detection-and-hardening.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-cross-account-attacks/historical-cross-account-vulnerabilities.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-cross-account-attacks/historical-cross-account-vulnerabilities.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-cross-account-attacks/iam-trust-and-federation-attacks.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-cross-account-attacks/iam-trust-and-federation-attacks.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-cross-account-attacks/organizations-and-central-account-pivots.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-cross-account-attacks/organizations-and-central-account-pivots.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-cross-account-attacks/resource-policy-and-shared-resource-attacks.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-cross-account-attacks/resource-policy-and-shared-resource-attacks.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-account-management-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-account-management-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-acm-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-acm-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-agent-registry-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-agent-registry-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-amplify-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-amplify-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-appintegrations-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-appintegrations-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-athena-result-redirection-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-athena-result-redirection-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-bedrock-data-automation-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-bedrock-data-automation-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-cloudformation-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-cloudformation-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-cloudtrail-trail-redirection-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-cloudtrail-trail-redirection-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-cloudwatch-omni-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-cloudwatch-omni-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-codeguru-profiler-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-codeguru-profiler-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-connect-campaigns-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-connect-campaigns-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-datasync-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-datasync-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-device-farm-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-device-farm-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-devops-agent-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-devops-agent-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-direct-connect-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-direct-connect-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-directory-service-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-directory-service-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-dynamodb-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-dynamodb-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-ec2-replace-root-volume-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-ec2-replace-root-volume-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-end-user-messaging-social-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-end-user-messaging-social-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-entity-resolution-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-entity-resolution-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-firewall-manager-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-firewall-manager-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-fraud-detector-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-fraud-detector-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-gamelift-streams-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-gamelift-streams-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-global-accelerator-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-global-accelerator-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-ground-station-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-ground-station-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-healthlake-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-healthlake-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-identity-center-user-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-identity-center-user-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-iot-sitewise-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-iot-sitewise-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-iot-twinmaker-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-iot-twinmaker-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-keyspaces-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-keyspaces-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-lambda-persistence/aws-abusing-lambda-extensions.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-lambda-persistence/aws-abusing-lambda-extensions.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-lambda-persistence/aws-lambda-alias-version-policy-backdoor.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-lambda-persistence/aws-lambda-alias-version-policy-backdoor.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-lambda-persistence/aws-lambda-async-self-loop-persistence.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-lambda-persistence/aws-lambda-async-self-loop-persistence.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-lambda-persistence/aws-lambda-exec-wrapper-persistence.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-lambda-persistence/aws-lambda-exec-wrapper-persistence.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-lex-v2-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-lex-v2-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-mainframe-modernization-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-mainframe-modernization-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-managed-blockchain-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-managed-blockchain-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-managed-prometheus-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-managed-prometheus-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-marketplace-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-marketplace-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-medialive-output-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-medialive-output-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-mq-broker-admin-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-mq-broker-admin-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-msk-policy-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-msk-policy-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-network-manager-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-network-manager-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-network-security-manager-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-network-security-manager-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-odb-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-odb-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-opensearch-access-policy-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-opensearch-access-policy-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-partner-central-selling-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-partner-central-selling-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-payment-cryptography-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-payment-cryptography-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-q-business-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-q-business-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-q-in-connect-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-q-in-connect-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-ram-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-ram-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-refactor-spaces-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-refactor-spaces-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-route53-arc-readiness-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-route53-arc-readiness-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-s3-vectors-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-s3-vectors-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-security-agent-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-security-agent-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-supply-chain-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-supply-chain-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-systems-manager-incident-manager-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-systems-manager-incident-manager-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-timestream-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-timestream-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-workspaces-web-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-workspaces-web-persistence/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloud-control-handler-role-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloud-control-handler-role-post-exploitation/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-databrew-stored-job-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-databrew-stored-job-post-exploitation/README.md) | no | 1 | 1 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-datasync-delegated-copy-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-datasync-delegated-copy-post-exploitation/README.md) | no | 2 | 2 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/aws-malicious-vpc-mirror.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/aws-malicious-vpc-mirror.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-interconnect-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-interconnect-post-exploitation/README.md) | no | 1 | 1 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-post-exploitation/aws-lambda-runtime-pinning-abuse.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-post-exploitation/aws-lambda-runtime-pinning-abuse.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-route53-domains-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-route53-domains-post-exploitation/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-snow-device-management-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-snow-device-management-post-exploitation/README.md) | no | 1 | 1 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-account-management-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-account-management-privesc/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-aurora-dsql-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-aurora-dsql-privesc/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-braket-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-braket-privesc/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cloud-control-handler-role-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cloud-control-handler-role-privesc/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cloudformation-privesc/iam-passrole-cloudformation-createstack-and-cloudformation-describestacks.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cloudformation-privesc/iam-passrole-cloudformation-createstack-and-cloudformation-describestacks.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cloudwatch-omni-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cloudwatch-omni-privesc/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codepipeline-job-credentials-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codepipeline-job-credentials-privesc/README.md) | no | 1 | 1 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codestar-privesc/codestar-createproject-codestar-associateteammember.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codestar-privesc/codestar-createproject-codestar-associateteammember.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codestar-privesc/iam-passrole-codestar-createproject.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codestar-privesc/iam-passrole-codestar-createproject.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cognito-user-pools-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cognito-user-pools-privesc/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-connect-cases-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-connect-cases-privesc/README.md) | no | 1 | 2 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-connect-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-connect-privesc/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-control-tower-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-control-tower-privesc/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-customer-profiles-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-customer-profiles-privesc/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-device-farm-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-device-farm-privesc/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-documentdb-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-documentdb-privesc/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecs-privesc/aws-ecscape-privesc.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecs-privesc/aws-ecscape-privesc.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-entity-resolution-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-entity-resolution-privesc/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-gamelift-streams-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-gamelift-streams-privesc/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-healthomics-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-healthomics-privesc/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-invoicing-and-billing-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-invoicing-and-billing-privesc/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ivs-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ivs-privesc/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-lex-v2-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-lex-v2-privesc/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-mainframe-modernization-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-mainframe-modernization-privesc/README.md) | no | 1 | 1 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-managed-blockchain-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-managed-blockchain-privesc/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-memorydb-user-reset-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-memorydb-user-reset-privesc/README.md) | no | 1 | 1 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-migration-hub-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-migration-hub-privesc/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ml-dataaccess-passrole-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ml-dataaccess-passrole-privesc/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-odb-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-odb-privesc/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-organizations-prinvesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-organizations-prinvesc/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-payment-cryptography-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-payment-cryptography-privesc/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-q-business-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-q-business-privesc/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-resilience-hub-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-resilience-hub-privesc/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-route53-domains-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-route53-domains-privesc/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-s3-credential-brokers-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-s3-credential-brokers-privesc/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-supply-chain-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-supply-chain-privesc/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-timestream-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-timestream-privesc/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-wickr-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-wickr-privesc/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-workspaces-appstream-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-workspaces-appstream-privesc/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-cloudfront-unauthenticated-enum/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-cloudfront-unauthenticated-enum/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-documentdb-enum/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-documentdb-enum/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-ecs-unauthenticated-enum/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-ecs-unauthenticated-enum/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-edge-origin-bypass/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-edge-origin-bypass/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-elasticsearch-unauthenticated-enum/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-elasticsearch-unauthenticated-enum/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-global-accelerator-unauthenticated-enum/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-global-accelerator-unauthenticated-enum/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-iot-unauthenticated-enum/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-iot-unauthenticated-enum/README.md) | no | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/README.md) | yes | 45 | 12 | 28 | 20 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecs-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecs-privesc/README.md) | yes | 16 | 1 | 25 | 5 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sagemaker-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sagemaker-privesc/README.md) | yes | 15 | 2 | 25 | 3 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-lambda-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-lambda-privesc/README.md) | yes | 15 | 6 | 22 | 3 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-api-gateway-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-api-gateway-post-exploitation/README.md) | yes | 17 | 0 | 18 | 4 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-inspector-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-inspector-post-exploitation/README.md) | yes | 8 | 5 | 15 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ssm-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ssm-privesc/README.md) | yes | 13 | 7 | 13 | 3 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ec2-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ec2-privesc/README.md) | yes | 11 | 8 | 12 | 3 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-eventbridge-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-eventbridge-post-exploitation/README.md) | yes | 10 | 1 | 11 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecr-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecr-privesc/README.md) | yes | 9 | 12 | 11 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cloudformation-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cloudformation-privesc/README.md) | yes | 14 | 12 | 10 | 4 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-apigateway-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-apigateway-privesc/README.md) | yes | 6 | 0 | 10 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-emr-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-emr-privesc/README.md) | yes | 6 | 3 | 10 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-s3-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-s3-post-exploitation/README.md) | yes | 17 | 8 | 9 | 7 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ses-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ses-post-exploitation/README.md) | yes | 12 | 0 | 9 | 4 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codebuild-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codebuild-privesc/README.md) | yes | 11 | 12 | 8 | 2 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-rds-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-rds-privesc/README.md) | yes | 8 | 4 | 8 | 2 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudwatch-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudwatch-post-exploitation/README.md) | yes | 14 | 19 | 8 | 1 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cloudfront-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cloudfront-privesc/README.md) | yes | 3 | 3 | 8 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-elastic-beanstalk-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-elastic-beanstalk-privesc/README.md) | yes | 5 | 11 | 8 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sagemaker-configuration-access-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sagemaker-configuration-access-post-exploitation/README.md) | yes | 4 | 0 | 7 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-vpn-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-vpn-post-exploitation/README.md) | yes | 6 | 1 | 7 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-amplify-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-amplify-privesc/README.md) | yes | 7 | 9 | 7 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-post-exploitation/README.md) | yes | 21 | 1 | 6 | 14 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-rds-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-rds-post-exploitation/README.md) | yes | 20 | 18 | 6 | 6 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-eks-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-eks-privesc/README.md) | yes | 8 | 7 | 6 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-iam-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-iam-post-exploitation/README.md) | yes | 14 | 4 | 5 | 8 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudfront-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudfront-post-exploitation/README.md) | yes | 6 | 2 | 5 | 4 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-marketplace-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-marketplace-post-exploitation/README.md) | yes | 8 | 1 | 5 | 2 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-iam-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-iam-privesc/README.md) | yes | 21 | 29 | 5 | 2 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-cloudwatch-log-forwarding-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-cloudwatch-log-forwarding-persistence/README.md) | yes | 4 | 2 | 5 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-elastic-beanstalk-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-elastic-beanstalk-post-exploitation/README.md) | yes | 6 | 6 | 5 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-function-access-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-function-access-post-exploitation/README.md) | yes | 4 | 0 | 5 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codepipeline-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codepipeline-privesc/README.md) | yes | 11 | 12 | 5 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-dynamodb-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-dynamodb-post-exploitation/README.md) | yes | 25 | 25 | 4 | 5 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cognito-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cognito-privesc/README.md) | yes | 22 | 24 | 4 | 4 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ecr-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ecr-post-exploitation/README.md) | yes | 8 | 6 | 4 | 3 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-bedrock-agentcore-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-bedrock-agentcore-privesc/README.md) | yes | 6 | 4 | 4 | 2 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-mwaa-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-mwaa-privesc/README.md) | yes | 4 | 2 | 4 | 1 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-stepfunctions-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-stepfunctions-privesc/README.md) | yes | 4 | 4 | 4 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-route53-dns-takeover-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-route53-dns-takeover-post-exploitation/README.md) | yes | 2 | 2 | 4 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ssm-parameter-and-command-access-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ssm-parameter-and-command-access-post-exploitation/README.md) | yes | 5 | 6 | 4 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sagemaker-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sagemaker-post-exploitation/README.md) | yes | 10 | 1 | 3 | 7 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-mwaa-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-mwaa-post-exploitation/README.md) | yes | 7 | 1 | 3 | 5 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sts-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sts-privesc/README.md) | yes | 8 | 3 | 3 | 2 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-efs-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-efs-post-exploitation/README.md) | yes | 9 | 5 | 3 | 1 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-s3-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-s3-privesc/README.md) | yes | 5 | 5 | 3 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-appstream-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-appstream-post-exploitation/README.md) | yes | 3 | 1 | 3 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-neptune-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-neptune-post-exploitation/README.md) | yes | 3 | 0 | 3 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-bedrock-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-bedrock-privesc/README.md) | yes | 3 | 3 | 3 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-emr-serverless-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-emr-serverless-privesc/README.md) | yes | 4 | 4 | 3 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/eventbridgescheduler-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/eventbridgescheduler-privesc/README.md) | yes | 1 | 0 | 3 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-bedrock-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-bedrock-post-exploitation/README.md) | yes | 7 | 2 | 2 | 4 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-guardduty-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-guardduty-post-exploitation/README.md) | yes | 8 | 2 | 2 | 4 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-redshift-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-redshift-privesc/README.md) | yes | 8 | 5 | 2 | 4 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lakeformation-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lakeformation-post-exploitation/README.md) | yes | 8 | 3 | 2 | 3 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-post-exploitation/aws-lambda-event-source-mapping-hijack.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-post-exploitation/aws-lambda-event-source-mapping-hijack.md) | yes | 5 | 0 | 2 | 3 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-organizations-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-organizations-post-exploitation/README.md) | yes | 5 | 0 | 2 | 3 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-transfer-family-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-transfer-family-post-exploitation/README.md) | yes | 6 | 2 | 2 | 3 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-artifact-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-artifact-post-exploitation/README.md) | yes | 3 | 0 | 2 | 2 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-stepfunctions-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-stepfunctions-post-exploitation/README.md) | yes | 13 | 13 | 2 | 2 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-waf-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-waf-post-exploitation/README.md) | yes | 10 | 18 | 2 | 2 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudwatch-omni-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudwatch-omni-post-exploitation/README.md) | yes | 4 | 1 | 2 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-elasticache-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-elasticache-post-exploitation/README.md) | yes | 3 | 0 | 2 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-license-manager-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-license-manager-post-exploitation/README.md) | yes | 4 | 1 | 2 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-redshift-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-redshift-post-exploitation/README.md) | yes | 5 | 2 | 2 | 1 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-appsync-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-appsync-privesc/README.md) | yes | 3 | 3 | 2 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-direct-connect-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-direct-connect-post-exploitation/README.md) | yes | 3 | 1 | 2 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-service-catalog-appregistry-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-service-catalog-appregistry-post-exploitation/README.md) | yes | 2 | 0 | 2 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-appstream-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-appstream-privesc/README.md) | yes | 8 | 7 | 2 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-athena-spark-role-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-athena-spark-role-privesc/README.md) | yes | 3 | 1 | 2 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-budgets-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-budgets-privesc/README.md) | yes | 1 | 1 | 2 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-datasync-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-datasync-privesc/README.md) | yes | 2 | 5 | 2 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-iot-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-iot-privesc/README.md) | yes | 3 | 4 | 2 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ecs-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ecs-post-exploitation/README.md) | yes | 10 | 1 | 1 | 8 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-sagemaker-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-sagemaker-persistence/README.md) | yes | 8 | 0 | 1 | 7 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-chime-sdk-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-chime-sdk-post-exploitation/README.md) | yes | 9 | 2 | 1 | 7 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-iot-core-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-iot-core-post-exploitation/README.md) | yes | 10 | 3 | 1 | 7 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-appflow-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-appflow-post-exploitation/README.md) | yes | 7 | 0 | 1 | 6 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-connect-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-connect-post-exploitation/README.md) | yes | 7 | 0 | 1 | 6 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-managed-prometheus-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-managed-prometheus-post-exploitation/README.md) | yes | 6 | 0 | 1 | 5 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudtrail-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudtrail-post-exploitation/README.md) | yes | 5 | 0 | 1 | 4 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-keyspaces-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-keyspaces-post-exploitation/README.md) | yes | 6 | 1 | 1 | 4 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-backup-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-backup-post-exploitation/README.md) | yes | 4 | 2 | 1 | 2 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sns-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sns-post-exploitation/README.md) | yes | 10 | 8 | 1 | 2 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-config-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-config-privesc/README.md) | yes | 3 | 1 | 1 | 2 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sqs-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sqs-post-exploitation/README.md) | yes | 10 | 11 | 1 | 1 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-apprunner-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-apprunner-privesc/README.md) | yes | 4 | 3 | 1 | 1 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-batch-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-batch-privesc/README.md) | yes | 3 | 3 | 1 | 1 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-managed-grafana-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-managed-grafana-privesc/README.md) | yes | 4 | 2 | 1 | 1 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-data-firehose-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-data-firehose-persistence/README.md) | yes | 1 | 0 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-managed-grafana-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-managed-grafana-persistence/README.md) | yes | 2 | 1 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-redshift-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-redshift-persistence/README.md) | yes | 4 | 3 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-amplify-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-amplify-post-exploitation/README.md) | yes | 2 | 1 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-athena-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-athena-post-exploitation/README.md) | yes | 3 | 3 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudformation-trigger-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudformation-trigger-post-exploitation/README.md) | yes | 2 | 1 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudwatch-log-data-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudwatch-log-data-post-exploitation/README.md) | yes | 4 | 5 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-codeartifact-auth-token-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-codeartifact-auth-token-post-exploitation/README.md) | yes | 1 | 1 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-gamelift-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-gamelift-post-exploitation/README.md) | yes | 3 | 2 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-managed-grafana-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-managed-grafana-post-exploitation/README.md) | yes | 1 | 1 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-resource-explorer-inventory-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-resource-explorer-inventory-post-exploitation/README.md) | yes | 1 | 0 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-appconfig-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-appconfig-privesc/README.md) | yes | 1 | 1 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-athena-stored-query-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-athena-stored-query-privesc/README.md) | yes | 2 | 1 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-dlm-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-dlm-privesc/README.md) | yes | 1 | 1 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-eventbridge-pipes-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-eventbridge-pipes-privesc/README.md) | yes | 1 | 1 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-iot-core-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-iot-core-privesc/README.md) | yes | 1 | 1 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-kms-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-kms-privesc/README.md) | yes | 4 | 7 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-mq-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-mq-privesc/README.md) | yes | 4 | 8 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-region-switch-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-region-switch-privesc/README.md) | yes | 2 | 2 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-secrets-manager-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-secrets-manager-privesc/README.md) | yes | 2 | 3 | 1 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-kms-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-kms-post-exploitation/README.md) | yes | 13 | 1 | 0 | 12 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-lambda-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-lambda-persistence/README.md) | yes | 10 | 1 | 0 | 9 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-customer-profiles-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-customer-profiles-post-exploitation/README.md) | yes | 8 | 0 | 0 | 8 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-secrets-manager-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-secrets-manager-post-exploitation/README.md) | yes | 9 | 1 | 0 | 8 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-clean-rooms-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-clean-rooms-post-exploitation/README.md) | yes | 7 | 0 | 0 | 7 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/aws-ebs-multi-attach-data-theft.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/aws-ebs-multi-attach-data-theft.md) | yes | 7 | 0 | 0 | 7 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-eks-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-eks-post-exploitation/README.md) | yes | 8 | 1 | 0 | 7 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sqs-post-exploitation/aws-sqs-dlq-redrive-exfiltration.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sqs-post-exploitation/aws-sqs-dlq-redrive-exfiltration.md) | yes | 7 | 0 | 0 | 7 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-workspaces-web-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-workspaces-web-post-exploitation/README.md) | yes | 7 | 0 | 0 | 7 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-ec2-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-ec2-persistence/README.md) | yes | 6 | 0 | 0 | 6 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-device-farm-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-device-farm-post-exploitation/README.md) | yes | 6 | 0 | 0 | 6 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/aws-ami-store-s3-exfiltration.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/aws-ami-store-s3-exfiltration.md) | yes | 6 | 0 | 0 | 6 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/aws-ec2-instance-connect-endpoint-backdoor.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/aws-ec2-instance-connect-endpoint-backdoor.md) | yes | 6 | 0 | 0 | 6 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/aws-managed-prefix-list-backdoor.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/aws-managed-prefix-list-backdoor.md) | yes | 6 | 0 | 0 | 6 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-iam-post-exploitation/aws-resource-policy-principal-validation.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-iam-post-exploitation/aws-resource-policy-principal-validation.md) | yes | 6 | 0 | 0 | 6 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-migration-hub-strategy-recommendations-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-migration-hub-strategy-recommendations-post-exploitation/README.md) | yes | 6 | 0 | 0 | 6 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-iam-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-iam-persistence/README.md) | yes | 7 | 2 | 0 | 5 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-secrets-manager-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-secrets-manager-persistence/README.md) | yes | 5 | 0 | 0 | 5 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-appsync-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-appsync-post-exploitation/README.md) | yes | 6 | 2 | 0 | 5 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-codeconnections-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-codeconnections-post-exploitation/README.md) | yes | 5 | 0 | 0 | 5 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/aws-vpc-flow-logs-cross-account-exfiltration.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/aws-vpc-flow-logs-cross-account-exfiltration.md) | yes | 5 | 0 | 0 | 5 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-glue-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-glue-post-exploitation/README.md) | yes | 5 | 0 | 0 | 5 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-iot-sitewise-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-iot-sitewise-post-exploitation/README.md) | yes | 5 | 0 | 0 | 5 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-kinesis-video-streams-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-kinesis-video-streams-post-exploitation/README.md) | yes | 5 | 0 | 0 | 5 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lex-v2-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lex-v2-post-exploitation/README.md) | yes | 5 | 0 | 0 | 5 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-cloudwatch-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-cloudwatch-persistence/README.md) | yes | 4 | 0 | 0 | 4 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-customer-profiles-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-customer-profiles-persistence/README.md) | yes | 4 | 0 | 0 | 4 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-eks-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-eks-persistence/README.md) | yes | 4 | 0 | 0 | 4 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-guardduty-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-guardduty-persistence/README.md) | yes | 4 | 0 | 0 | 4 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-lambda-persistence/aws-lambda-layers-persistence.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-lambda-persistence/aws-lambda-layers-persistence.md) | yes | 4 | 0 | 0 | 4 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-waf-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-waf-persistence/README.md) | yes | 4 | 0 | 0 | 4 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-codebuild-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-codebuild-post-exploitation/README.md) | yes | 8 | 4 | 0 | 4 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cost-explorer-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cost-explorer-post-exploitation/README.md) | yes | 4 | 0 | 0 | 4 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-datazone-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-datazone-post-exploitation/README.md) | yes | 4 | 0 | 0 | 4 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/aws-eip-hijack-impersonation.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/aws-eip-hijack-impersonation.md) | yes | 4 | 0 | 0 | 4 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/aws-vpc-endpoint-egress-bypass.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/aws-vpc-endpoint-egress-bypass.md) | yes | 4 | 0 | 0 | 4 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-emr-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-emr-post-exploitation/README.md) | yes | 4 | 0 | 0 | 4 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-entity-resolution-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-entity-resolution-post-exploitation/README.md) | yes | 4 | 0 | 0 | 4 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-healthlake-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-healthlake-post-exploitation/README.md) | yes | 4 | 0 | 0 | 4 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-iot-twinmaker-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-iot-twinmaker-post-exploitation/README.md) | yes | 4 | 0 | 0 | 4 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-iot-wireless-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-iot-wireless-post-exploitation/README.md) | yes | 4 | 0 | 0 | 4 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ivs-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ivs-post-exploitation/README.md) | yes | 4 | 0 | 0 | 4 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-kinesis-data-streams-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-kinesis-data-streams-post-exploitation/README.md) | yes | 4 | 0 | 0 | 4 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-post-exploitation/aws-lambda-loggingconfig-redirection.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-post-exploitation/aws-lambda-loggingconfig-redirection.md) | yes | 4 | 0 | 0 | 4 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-managed-flink-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-managed-flink-post-exploitation/README.md) | yes | 4 | 0 | 0 | 4 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-mediaconnect-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-mediaconnect-post-exploitation/README.md) | yes | 4 | 0 | 0 | 4 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sns-post-exploitation/aws-sns-fifo-replay-exfil.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sns-post-exploitation/aws-sns-fifo-replay-exfil.md) | yes | 4 | 0 | 0 | 4 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sns-post-exploitation/aws-sns-firehose-exfil.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sns-post-exploitation/aws-sns-firehose-exfil.md) | yes | 4 | 0 | 0 | 4 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-appflow-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-appflow-persistence/README.md) | yes | 3 | 0 | 0 | 3 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-elastic-beanstalk-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-elastic-beanstalk-persistence/README.md) | yes | 3 | 0 | 0 | 3 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-ivs-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-ivs-persistence/README.md) | yes | 3 | 0 | 0 | 3 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-kinesis-video-streams-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-kinesis-video-streams-persistence/README.md) | yes | 3 | 0 | 0 | 3 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-verified-permissions-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-verified-permissions-persistence/README.md) | yes | 3 | 0 | 0 | 3 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-b2bi-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-b2bi-post-exploitation/README.md) | yes | 3 | 0 | 0 | 3 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudformation-registry-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudformation-registry-post-exploitation/README.md) | yes | 3 | 0 | 0 | 3 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cognito-user-pools-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cognito-user-pools-post-exploitation/README.md) | yes | 3 | 0 | 0 | 3 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-connect-cases-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-connect-cases-post-exploitation/README.md) | yes | 3 | 0 | 0 | 3 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-data-firehose-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-data-firehose-post-exploitation/README.md) | yes | 3 | 0 | 0 | 3 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-detective-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-detective-post-exploitation/README.md) | yes | 3 | 0 | 0 | 3 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-healthomics-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-healthomics-post-exploitation/README.md) | yes | 3 | 0 | 0 | 3 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-post-exploitation/aws-lambda-efs-mount-injection.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-post-exploitation/aws-lambda-efs-mount-injection.md) | yes | 3 | 0 | 0 | 3 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lightsail-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lightsail-post-exploitation/README.md) | yes | 11 | 8 | 0 | 3 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-resilience-hub-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-resilience-hub-post-exploitation/README.md) | yes | 3 | 0 | 0 | 3 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-route53-profiles-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-route53-profiles-post-exploitation/README.md) | yes | 3 | 0 | 0 | 3 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sagemaker-post-exploitation/feature-store-poisoning.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sagemaker-post-exploitation/feature-store-poisoning.md) | yes | 3 | 0 | 0 | 3 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sns-post-exploitation/aws-sns-data-protection-bypass.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sns-post-exploitation/aws-sns-data-protection-bypass.md) | yes | 3 | 0 | 0 | 3 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-verified-permissions-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-verified-permissions-post-exploitation/README.md) | yes | 3 | 0 | 0 | 3 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codedeploy-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codedeploy-privesc/README.md) | yes | 3 | 0 | 0 | 3 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ec2-image-builder-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ec2-image-builder-privesc/README.md) | yes | 3 | 0 | 0 | 3 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-service-catalog-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-service-catalog-privesc/README.md) | yes | 3 | 0 | 0 | 3 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-chime-sdk-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-chime-sdk-persistence/README.md) | yes | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-cloudtrail-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-cloudtrail-persistence/README.md) | yes | 3 | 1 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-datazone-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-datazone-persistence/README.md) | yes | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-ecr-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-ecr-persistence/README.md) | yes | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-ecs-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-ecs-persistence/README.md) | yes | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-efs-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-efs-persistence/README.md) | yes | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-healthomics-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-healthomics-persistence/README.md) | yes | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-kinesis-data-streams-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-kinesis-data-streams-persistence/README.md) | yes | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-kms-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-kms-persistence/README.md) | yes | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-managed-flink-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-managed-flink-persistence/README.md) | yes | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-sns-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-sns-persistence/README.md) | yes | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-sqs-persistence/aws-sqs-orgid-policy-backdoor.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-sqs-persistence/aws-sqs-orgid-policy-backdoor.md) | yes | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-ssm-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-ssm-persistence/README.md) | yes | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-sts-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-sts-persistence/README.md) | yes | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-appconfig-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-appconfig-post-exploitation/README.md) | yes | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-config-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-config-post-exploitation/README.md) | yes | 5 | 3 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-global-accelerator-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-global-accelerator-post-exploitation/README.md) | yes | 5 | 3 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-s3-tables-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-s3-tables-post-exploitation/README.md) | yes | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-s3-vectors-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-s3-vectors-post-exploitation/README.md) | yes | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sts-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sts-post-exploitation/README.md) | yes | 3 | 1 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-dynamodb-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-dynamodb-privesc/README.md) | yes | 3 | 2 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-sns-unauthenticated-enum/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-sns-unauthenticated-enum/README.md) | yes | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-sqs-unauthenticated-enum/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-unauthenticated-enum-access/aws-sqs-unauthenticated-enum/README.md) | yes | 2 | 0 | 0 | 2 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-s3-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-s3-persistence/README.md) | yes | 2 | 2 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-athena-query-disclosure-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-athena-query-disclosure-post-exploitation/README.md) | yes | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudformation-data-disclosure-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudformation-data-disclosure-post-exploitation/README.md) | yes | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-codeartifact-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-codeartifact-post-exploitation/README.md) | yes | 2 | 1 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/aws-eni-secondary-ip-hijack.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/aws-eni-secondary-ip-hijack.md) | yes | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-eventbridge-scheduler-post-exploitation.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-eventbridge-scheduler-post-exploitation.md) | yes | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-fraud-detector-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-fraud-detector-post-exploitation/README.md) | yes | 4 | 3 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-greengrass-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-greengrass-post-exploitation/README.md) | yes | 4 | 5 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-post-exploitation/aws-lambda-function-url-public-exposure.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-post-exploitation/aws-lambda-function-url-public-exposure.md) | yes | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-launch-wizard-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-launch-wizard-post-exploitation/README.md) | yes | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-network-manager-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-network-manager-post-exploitation/README.md) | yes | 5 | 5 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-resource-explorer-setup-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-resource-explorer-setup-post-exploitation/README.md) | yes | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sqs-post-exploitation/aws-sqs-sns-injection.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sqs-post-exploitation/aws-sqs-sns-injection.md) | yes | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codeartifact-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codeartifact-privesc/README.md) | yes | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codecommit-pipeline-source-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codecommit-pipeline-source-privesc/README.md) | yes | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-mediapackage-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-mediapackage-privesc/README.md) | yes | 5 | 4 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sns-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sns-privesc/README.md) | yes | 4 | 3 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-synthetics-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-synthetics-privesc/README.md) | yes | 2 | 1 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-transfer-family-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-transfer-family-privesc/README.md) | yes | 1 | 0 | 0 | 1 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-appconfig-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-appconfig-persistence/README.md) | yes | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-appstream-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-appstream-persistence/README.md) | yes | 2 | 2 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-appsync-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-appsync-persistence/README.md) | yes | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-b2bi-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-b2bi-persistence/README.md) | yes | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-codeartifact-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-codeartifact-persistence/README.md) | yes | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-cognito-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-cognito-persistence/README.md) | yes | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-config-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-config-persistence/README.md) | yes | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-elasticache-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-elasticache-persistence/README.md) | yes | 2 | 4 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-eventbridge-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-eventbridge-persistence/README.md) | yes | 2 | 2 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-glue-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-glue-persistence/README.md) | yes | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-iot-wireless-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-iot-wireless-persistence/README.md) | yes | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-location-service-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-location-service-persistence/README.md) | yes | 1 | 1 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-resource-explorer-default-view-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-resource-explorer-default-view-persistence/README.md) | yes | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-route53-profiles-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-route53-profiles-persistence/README.md) | yes | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-s3-files-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-s3-files-persistence/README.md) | yes | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-s3-tables-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-s3-tables-persistence/README.md) | yes | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-sqs-persistence/aws-sqs-dlq-backdoor-persistence.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-sqs-persistence/aws-sqs-dlq-backdoor-persistence.md) | yes | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-persistence/aws-support-authorization-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-support-authorization-persistence/README.md) | yes | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloud-map-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloud-map-post-exploitation/README.md) | yes | 2 | 2 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-codecommit-source-access-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-codecommit-source-access-post-exploitation/README.md) | yes | 2 | 4 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-codepipeline-data-access-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-codepipeline-data-access-post-exploitation/README.md) | yes | 3 | 4 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cognito-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cognito-post-exploitation/README.md) | yes | 4 | 7 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-eventbridge-pipe-configuration-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-eventbridge-pipe-configuration-post-exploitation/README.md) | yes | 1 | 1 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-mediapackage-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-mediapackage-post-exploitation/README.md) | yes | 4 | 4 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-mq-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-mq-post-exploitation/README.md) | yes | 2 | 2 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-network-firewall-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-network-firewall-post-exploitation/README.md) | yes | 3 | 3 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-s3-files-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-s3-files-post-exploitation/README.md) | yes | 1 | 1 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sns-subscriber-disclosure-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sns-subscriber-disclosure-post-exploitation/README.md) | yes | 1 | 2 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-vpc-lattice-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-vpc-lattice-post-exploitation/README.md) | yes | 3 | 3 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-datazone-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-datazone-privesc/README.md) | yes | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-deadline-cloud-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-deadline-cloud-privesc/README.md) | yes | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-efs-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-efs-privesc/README.md) | yes | 1 | 2 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-elasticache-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-elasticache-privesc/README.md) | yes | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-eventbridge-pipe-stored-role-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-eventbridge-pipe-stored-role-privesc/README.md) | yes | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-eventbridge-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-eventbridge-privesc/README.md) | yes | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-glue-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-glue-privesc/README.md) | yes | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-iot-twinmaker-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-iot-twinmaker-privesc/README.md) | yes | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-kinesis-data-streams-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-kinesis-data-streams-privesc/README.md) | yes | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-lightsail-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-lightsail-privesc/README.md) | yes | 12 | 12 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-managed-flink-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-managed-flink-privesc/README.md) | yes | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-opensearch-serverless-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-opensearch-serverless-privesc/README.md) | yes | 1 | 1 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-resource-explorer-view-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-resource-explorer-view-privesc/README.md) | yes | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-s3-files-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-s3-files-privesc/README.md) | yes | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-s3-tables-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-s3-tables-privesc/README.md) | yes | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-s3-vectors-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-s3-vectors-privesc/README.md) | yes | 0 | 0 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sqs-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sqs-privesc/README.md) | yes | 2 | 2 | 0 | 0 |
| [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-verified-permissions-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-verified-permissions-privesc/README.md) | yes | 0 | 0 | 0 | 0 |

## Action names without an exact YAML event name

Each item needs manual review of the source paragraph, existing rule
semantics, CloudTrail shape, service availability and live test evidence.

### src/pentesting-cloud/aws-security/aws-persistence/aws-cloudwatch-log-forwarding-persistence/README.md

- [`observabilityadmin:CreateS3TableIntegration`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-cloudwatch-log-forwarding-persistence/README.md#L15)
- [`logs:AssociateSourceToS3TableIntegration`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-cloudwatch-log-forwarding-persistence/README.md#L15)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-cloudwatch-log-forwarding-persistence/README.md#L15)
- [`logs:PutAccountPolicy`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-cloudwatch-log-forwarding-persistence/README.md#L171)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-cloudwatch-log-forwarding-persistence/README.md#L203)

### src/pentesting-cloud/aws-security/aws-persistence/aws-data-firehose-persistence/README.md

- [`firehose:UpdateDestination`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-data-firehose-persistence/README.md#L13)

### src/pentesting-cloud/aws-security/aws-persistence/aws-managed-grafana-persistence/README.md

- [`grafana:UpdatePermissions`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-managed-grafana-persistence/README.md#L19)

### src/pentesting-cloud/aws-security/aws-persistence/aws-mediapackage-v2-policy-persistence/README.md

- [`mediapackagev2:PutChannelPolicy`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-mediapackage-v2-policy-persistence/README.md#L13)
- [`mediapackagev2:PutOriginEndpointPolicy`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-mediapackage-v2-policy-persistence/README.md#L35)

### src/pentesting-cloud/aws-security/aws-persistence/aws-memorydb-persistence/README.md

- [`memorydb:CreateACL`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-memorydb-persistence/README.md#L17)
- [`memorydb:UpdateACL`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-memorydb-persistence/README.md#L17)

### src/pentesting-cloud/aws-security/aws-persistence/aws-redshift-persistence/README.md

- [`redshift:AuthorizeEndpointAccess`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-redshift-persistence/README.md#L108)

### src/pentesting-cloud/aws-security/aws-persistence/aws-sagemaker-persistence/README.md

- [`sagemaker:UpdateNotebookInstanceLifecycleConfig`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-sagemaker-persistence/README.md#L74)

### src/pentesting-cloud/aws-security/aws-persistence/aws-security-incident-response-persistence/README.md

- [`security-ir:UpdateMembership`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-security-incident-response-persistence/README.md#L15)
- [`security-ir:UpdateCase`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-security-incident-response-persistence/README.md#L76)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-account-management-post-exploitation/README.md

- [`account:EnableRegion`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-account-management-post-exploitation/README.md#L17)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-acm-pca-scep-post-exploitation/README.md

- [`pca-connector-scep:CreateChallenge`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-acm-pca-scep-post-exploitation/README.md#L17)
- [`acm:ExportCertificate`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-acm-pca-scep-post-exploitation/README.md#L58)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-agent-registry-post-exploitation/README.md

- [`agent-registry:UpdateRegistryRecordStatus`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-agent-registry-post-exploitation/README.md#L15)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-amplify-post-exploitation/README.md

- [`amplify:GetArtifactUrl`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-amplify-post-exploitation/README.md#L70)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-api-gateway-post-exploitation/README.md

- [`apigateway:POST`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-api-gateway-post-exploitation/README.md#L15)
- [`apigateway:GET`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-api-gateway-post-exploitation/README.md#L51)
- [`apigateway:PATCH`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-api-gateway-post-exploitation/README.md#L91)
- [`apigateway:PATCH`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-api-gateway-post-exploitation/README.md#L118)
- [`apigateway:PATCH`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-api-gateway-post-exploitation/README.md#L192)
- [`apigateway:POST`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-api-gateway-post-exploitation/README.md#L192)
- [`apigateway:PUT`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-api-gateway-post-exploitation/README.md#L224)
- [`apigateway:POST`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-api-gateway-post-exploitation/README.md#L224)
- [`apigateway:UpdatePortal`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-api-gateway-post-exploitation/README.md#L262)
- [`apigateway:PublishPortal`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-api-gateway-post-exploitation/README.md#L262)
- [`apigateway:PATCH`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-api-gateway-post-exploitation/README.md#L334)
- [`apigateway:PATCH`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-api-gateway-post-exploitation/README.md#L367)
- [`apigateway:PATCH`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-api-gateway-post-exploitation/README.md#L397)
- [`apigateway:POST`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-api-gateway-post-exploitation/README.md#L397)
- [`apigateway:PATCH`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-api-gateway-post-exploitation/README.md#L435)
- [`apigateway:GET`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-api-gateway-post-exploitation/README.md#L489)
- [`apigateway:UpdateRestApiPolicy`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-api-gateway-post-exploitation/README.md#L513)
- [`apigateway:PATCH`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-api-gateway-post-exploitation/README.md#L513)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-app-mesh-post-exploitation/README.md

- [`appmesh:UpdateRoute`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-app-mesh-post-exploitation/README.md#L20)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-appflow-post-exploitation/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-appflow-post-exploitation/README.md#L214)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-application-discovery-post-exploitation/README.md

- [`discovery:ListConfigurations`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-application-discovery-post-exploitation/README.md#L17)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-appstream-post-exploitation/README.md

- [`appstream:UpdateImagePermissions`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-appstream-post-exploitation/README.md#L15)
- [`appstream:CreateExportImageTask`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-appstream-post-exploitation/README.md#L60)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-appstream-post-exploitation/README.md#L60)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-artifact-post-exploitation/README.md

- [`artifact:GetTermForReport`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-artifact-post-exploitation/README.md#L43)
- [`artifact:GetReport`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-artifact-post-exploitation/README.md#L43)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-athena-post-exploitation/README.md

- [`athena:StartQueryExecution`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-athena-post-exploitation/README.md#L33)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-aurora-dsql-post-exploitation/README.md

- [`dsql:DbConnect`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-aurora-dsql-post-exploitation/README.md#L17)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-backup-post-exploitation/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-backup-post-exploitation/README.md#L17)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-batch-data-disclosure-post-exploitation/README.md

- [`batch:DescribeJobDefinitions`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-batch-data-disclosure-post-exploitation/README.md#L17)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-bedrock-post-exploitation/README.md

- [`bedrock:DeleteModelInvocationLoggingConfiguration`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-bedrock-post-exploitation/README.md#L374)
- [`bedrock:PutModelInvocationLoggingConfiguration`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-bedrock-post-exploitation/README.md#L374)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-chime-sdk-post-exploitation/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-chime-sdk-post-exploitation/README.md#L328)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudformation-trigger-post-exploitation/README.md

- [`cloudformation:ExecuteChangeSet`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudformation-trigger-post-exploitation/README.md#L7)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudfront-data-access-post-exploitation/README.md

- [`cloudfront:ListDistributions`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudfront-data-access-post-exploitation/README.md#L17)
- [`cloudfront:GetDistribution`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudfront-data-access-post-exploitation/README.md#L17)
- [`cloudfront:GetDistributionConfig`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudfront-data-access-post-exploitation/README.md#L17)
- [`cloudfront:GetFunction`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudfront-data-access-post-exploitation/README.md#L55)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudfront-post-exploitation/README.md

- [`cloudfront:GetDistributionConfig`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudfront-post-exploitation/README.md#L193)
- [`cloudfront:CreateFunction`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudfront-post-exploitation/README.md#L259)
- [`cloudfront:DescribeFunction`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudfront-post-exploitation/README.md#L259)
- [`cloudfront:PublishFunction`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudfront-post-exploitation/README.md#L259)
- [`cloudfront:GetDistributionConfig`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudfront-post-exploitation/README.md#L259)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudtrail-data-access-post-exploitation/README.md

- [`cloudtrail:LookupEvents`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudtrail-data-access-post-exploitation/README.md#L17)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudtrail-post-exploitation/README.md

- [`cloudtrail-data:PutAuditEvents`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudtrail-post-exploitation/README.md#L118)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudwatch-log-data-post-exploitation/README.md

- [`rum:GetAppMonitorData`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudwatch-log-data-post-exploitation/README.md#L77)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudwatch-omni-post-exploitation/README.md

- [`cloudwatch:CreateOneTimeDeepLinkCode`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudwatch-omni-post-exploitation/README.md#L17)
- [`cloudwatch:UpdateAlert`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudwatch-omni-post-exploitation/README.md#L193)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudwatch-post-exploitation/README.md

- [`oam:CreateLink`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudwatch-post-exploitation/README.md#L63)
- [`cloudwatch:EnableAlarmActions`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudwatch-post-exploitation/README.md#L221)
- [`cloudwatch:PutManagedInsightRules`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudwatch-post-exploitation/README.md#L350)
- [`cloudwatch:PutMetricStream`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudwatch-post-exploitation/README.md#L398)
- [`cloudwatch:PutMetricData`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudwatch-post-exploitation/README.md#L398)
- [`observabilityadmin:UpdateTelemetryPipeline`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudwatch-post-exploitation/README.md#L457)
- [`oam:UpdateLink`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudwatch-post-exploitation/README.md#L524)
- [`oam:DeleteLink`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudwatch-post-exploitation/README.md#L524)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-codeartifact-auth-token-post-exploitation/README.md

- [`sts:GetServiceBearerToken`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-codeartifact-auth-token-post-exploitation/README.md#L17)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-codeguru-profiler-post-exploitation/README.md

- [`codeguru-profiler:GetProfile`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-codeguru-profiler-post-exploitation/README.md#L15)
- [`codeguru-profiler:PostAgentProfile`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-codeguru-profiler-post-exploitation/README.md#L65)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-connect-health-post-exploitation/README.md

- [`health-agent:GetPatientInsightsJob`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-connect-health-post-exploitation/README.md#L19)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-connect-post-exploitation/README.md

- [`connect:CreateParticipant`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-connect-post-exploitation/README.md#L15)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-data-exchange-post-exploitation/README.md

- [`dataexchange:CreateDataGrant`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-data-exchange-post-exploitation/README.md#L17)
- [`dataexchange:PublishToDataGrant`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-data-exchange-post-exploitation/README.md#L17)
- [`dataexchange:CreateJob`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-data-exchange-post-exploitation/README.md#L77)
- [`dataexchange:StartJob`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-data-exchange-post-exploitation/README.md#L77)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-direct-connect-post-exploitation/README.md

- [`directconnect:CreateDirectConnectGatewayAssociationProposal`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-direct-connect-post-exploitation/README.md#L49)
- [`directconnect:AssociateMacSecKey`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-direct-connect-post-exploitation/README.md#L85)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-dlm-post-exploitation/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-dlm-post-exploitation/README.md#L15)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-dms-post-exploitation/README.md

- [`dms:ModifyEndpoint`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-dms-post-exploitation/README.md#L17)
- [`dms:StartReplicationTask`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-dms-post-exploitation/README.md#L65)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-drs-mgn-post-exploitation/README.md

- [`drs:StartRecovery`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-drs-mgn-post-exploitation/README.md#L17)
- [`drs:UpdateLaunchConfiguration`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-drs-mgn-post-exploitation/README.md#L17)
- [`mgn:StartExport`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-drs-mgn-post-exploitation/README.md#L48)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-dynamodb-post-exploitation/README.md

- [`dynamodb:PartiQLSelect`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-dynamodb-post-exploitation/README.md#L222)
- [`dynamodb:DescribeStream`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-dynamodb-post-exploitation/README.md#L275)
- [`dynamodb:CreateTableReplica`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-dynamodb-post-exploitation/README.md#L598)
- [`dynamodb:RestoreTableFromAwsBackup`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-dynamodb-post-exploitation/README.md#L742)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/README.md

- [`ec2:DescribeInstances`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/README.md#L411)
- [`ec2:RunInstances`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/README.md#L411)
- [`ec2:CreateSecurityGroup`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/README.md#L411)
- [`ec2:CreateTrafficMirrorTarget`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/README.md#L411)
- [`ec2:CreateTrafficMirrorSession`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/README.md#L411)
- [`ec2:CreateTrafficMirrorFilter`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/README.md#L411)
- [`ec2:CreateTrafficMirrorFilterRule`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/README.md#L411)
- [`ec2:EnableAddressTransfer`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/README.md#L465)
- [`ec2:EnableAllowedImagesSettings`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/README.md#L870)
- [`ec2:ReplaceImageCriteriaInAllowedImagesSettings`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/README.md#L870)
- [`ec2:DisableImageBlockPublicAccess`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/README.md#L913)
- [`ec2:EnableSnapshotBlockPublicAccess`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/README.md#L913)
- [`ec2:ModifyEbsDefaultKmsKeyId`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/README.md#L1446)
- [`ec2:LockSnapshot`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/README.md#L1489)
- [`ec2:CreateDhcpOptions`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/README.md#L1530)
- [`ebs:ListSnapshotBlocks`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/README.md#L1572)
- [`ebs:GetSnapshotBlock`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/README.md#L1572)
- [`ec2:DescribeSnapshots`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/README.md#L1572)
- [`ec2:CreateSnapshot`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/README.md#L1616)
- [`autoscaling:SetDesiredCapacity`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/README.md#L1718)
- [`ec2-instance-connect:SendSerialConsoleSSHPublicKey`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/README.md#L1750)
- [`ec2:EnableSerialConsoleAccess`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/README.md#L1790)
- [`ec2:DescribeLaunchTemplateVersions`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/README.md#L1822)
- [`ec2:DescribeLaunchTemplates`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/README.md#L1822)
- [`ec2:ModifyInstanceMetadataDefaults`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/README.md#L1922)
- [`ec2:ModifyImageAttribute`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/README.md#L1977)
- [`ec2:ModifySnapshotAttribute`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/README.md#L1977)
- [`ec2:GetPasswordData`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/README.md#L2010)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ecr-post-exploitation/README.md

- [`ecr:PutSigningConfiguration`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ecr-post-exploitation/README.md#L271)
- [`ecr:DeleteSigningConfiguration`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ecr-post-exploitation/README.md#L271)
- [`ecr:PutAccountSetting`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ecr-post-exploitation/README.md#L314)
- [`ecr:PutRegistryScanningConfiguration`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ecr-post-exploitation/README.md#L334)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ecs-data-access-post-exploitation/README.md

- [`ecs:DescribeTaskDefinition`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ecs-data-access-post-exploitation/README.md#L17)
- [`ecs:DescribeTasks`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ecs-data-access-post-exploitation/README.md#L48)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ecs-post-exploitation/README.md

- [`ecs:ExecuteCommand`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ecs-post-exploitation/README.md#L70)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-efs-post-exploitation/README.md

- [`elasticfilesystem:CreateReplicationConfiguration`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-efs-post-exploitation/README.md#L17)
- [`elasticfilesystem:UpdateFileSystem`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-efs-post-exploitation/README.md#L131)
- [`elasticfilesystem:ClientMount`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-efs-post-exploitation/README.md#L161)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-elastic-beanstalk-post-exploitation/README.md

- [`elasticbeanstalk:AddTags`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-elastic-beanstalk-post-exploitation/README.md#L41)
- [`elasticbeanstalk:RemoveTags`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-elastic-beanstalk-post-exploitation/README.md#L41)
- [`elasticbeanstalk:DescribeEnvironmentResources`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-elastic-beanstalk-post-exploitation/README.md#L152)
- [`elasticloadbalancing:ModifyLoadBalancerAttributes`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-elastic-beanstalk-post-exploitation/README.md#L152)
- [`s3:ListBucket`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-elastic-beanstalk-post-exploitation/README.md#L152)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-elasticache-post-exploitation/README.md

- [`elasticache:CopySnapshot`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-elasticache-post-exploitation/README.md#L61)
- [`elasticache:ExportServerlessCacheSnapshot`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-elasticache-post-exploitation/README.md#L104)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-elb-post-exploitation/README.md

- [`elasticloadbalancing:ModifyListener`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-elb-post-exploitation/README.md#L17)
- [`elasticloadbalancing:ModifyRule`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-elb-post-exploitation/README.md#L47)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-elemental-inference-post-exploitation/README.md

- [`elemental-inference:GetMetadata`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-elemental-inference-post-exploitation/README.md#L15)
- [`elemental-inference:ExportDictionaryEntries`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-elemental-inference-post-exploitation/README.md#L48)
- [`elemental-inference:UpdateDictionary`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-elemental-inference-post-exploitation/README.md#L88)
- [`elemental-inference:PutMedia`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-elemental-inference-post-exploitation/README.md#L126)
- [`elemental-inference:UpdateFeed`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-elemental-inference-post-exploitation/README.md#L160)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-emr-serverless-configuration-post-exploitation/README.md

- [`emr-serverless:GetApplication`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-emr-serverless-configuration-post-exploitation/README.md#L17)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-end-user-messaging-social-post-exploitation/README.md

- [`social-messaging:GetWhatsAppMessageMedia`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-end-user-messaging-social-post-exploitation/README.md#L15)
- [`social-messaging:SendWhatsAppMessage`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-end-user-messaging-social-post-exploitation/README.md#L50)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-eventbridge-post-exploitation/README.md

- [`events:CreateSubscriber`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-eventbridge-post-exploitation/README.md#L25)
- [`events:PutTargets`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-eventbridge-post-exploitation/README.md#L76)
- [`events:CreateConnection`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-eventbridge-post-exploitation/README.md#L107)
- [`events:CreateApiDestination`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-eventbridge-post-exploitation/README.md#L107)
- [`events:RemoveTargets`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-eventbridge-post-exploitation/README.md#L150)
- [`events:UpdateSubscriber`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-eventbridge-post-exploitation/README.md#L177)
- [`events:PutRule`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-eventbridge-post-exploitation/README.md#L235)
- [`events:UpdateSubscriber`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-eventbridge-post-exploitation/README.md#L269)
- [`events:UpdateEventBus`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-eventbridge-post-exploitation/README.md#L309)
- [`events:UpdateConnection`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-eventbridge-post-exploitation/README.md#L340)
- [`events:DeauthorizeConnection`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-eventbridge-post-exploitation/README.md#L340)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-firewall-manager-post-exploitation/README.md

- [`fms:PutNotificationChannel`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-firewall-manager-post-exploitation/README.md#L154)
- [`fms:DeleteNotificationChannel`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-firewall-manager-post-exploitation/README.md#L154)
- [`fms:BatchAssociateResource`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-firewall-manager-post-exploitation/README.md#L187)
- [`fms:BatchDisassociateResource`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-firewall-manager-post-exploitation/README.md#L187)
- [`fms:PutResourceSet`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-firewall-manager-post-exploitation/README.md#L187)
- [`fms:DeleteResourceSet`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-firewall-manager-post-exploitation/README.md#L187)
- [`fms:PutAppsList`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-firewall-manager-post-exploitation/README.md#L215)
- [`fms:DeleteAppsList`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-firewall-manager-post-exploitation/README.md#L215)
- [`fms:PutProtocolsList`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-firewall-manager-post-exploitation/README.md#L238)
- [`fms:DeleteProtocolsList`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-firewall-manager-post-exploitation/README.md#L238)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-free-tier-post-exploitation/README.md

- [`freetier:UpgradeAccountPlan`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-free-tier-post-exploitation/README.md#L15)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-fsx-post-exploitation/README.md

- [`fsx:CreateFileSystemFromBackup`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-fsx-post-exploitation/README.md#L17)
- [`fsx:CreateVolumeFromBackup`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-fsx-post-exploitation/README.md#L17)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-gamelift-post-exploitation/README.md

- [`gamelift:GetComputeAccess`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-gamelift-post-exploitation/README.md#L17)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-guardduty-post-exploitation/README.md

- [`guardduty:UpdateCustomDetectionRuleAssociation`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-guardduty-post-exploitation/README.md#L335)
- [`guardduty:DeletePublishingDestination`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-guardduty-post-exploitation/README.md#L420)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-healthimaging-data-access-post-exploitation/README.md

- [`medical-imaging:GetImageSetMetadata`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-healthimaging-data-access-post-exploitation/README.md#L17)
- [`medical-imaging:GetImageFrame`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-healthimaging-data-access-post-exploitation/README.md#L32)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-iam-post-exploitation/README.md

- [`iam:GetRequestAuthorizationDetails`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-iam-post-exploitation/README.md#L268)
- [`iam:ListOpenIDConnectProviders`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-iam-post-exploitation/README.md#L580)
- [`iam:AssociateDelegationRequest`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-iam-post-exploitation/README.md#L645)
- [`iam:AcceptDelegationRequest`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-iam-post-exploitation/README.md#L645)
- [`iam:SendDelegationToken`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-iam-post-exploitation/README.md#L645)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-inspector-post-exploitation/README.md

- [`inspector2:CreateFindingsReport`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-inspector-post-exploitation/README.md#L20)
- [`inspector2:CreateSbomExport`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-inspector-post-exploitation/README.md#L20)
- [`inspector2:CancelFindingsReport`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-inspector-post-exploitation/README.md#L121)
- [`inspector2:CancelSbomExport`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-inspector-post-exploitation/README.md#L121)
- [`inspector2:DeleteFilter`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-inspector-post-exploitation/README.md#L150)
- [`inspector2:DisableDelegatedAdminAccount`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-inspector-post-exploitation/README.md#L182)
- [`inspector2:EnableDelegatedAdminAccount`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-inspector-post-exploitation/README.md#L182)
- [`organizations:EnableAWSServiceAccess`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-inspector-post-exploitation/README.md#L182)
- [`iam:CreateServiceLinkedRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-inspector-post-exploitation/README.md#L182)
- [`inspector2:AssociateMember`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-inspector-post-exploitation/README.md#L220)
- [`inspector2:DisassociateMember`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-inspector-post-exploitation/README.md#L220)
- [`inspector2:Disable`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-inspector-post-exploitation/README.md#L252)
- [`inspector2:Enable`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-inspector-post-exploitation/README.md#L252)
- [`iam:CreateServiceLinkedRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-inspector-post-exploitation/README.md#L252)
- [`inspector2:UpdateOrganizationConfiguration`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-inspector-post-exploitation/README.md#L284)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-iot-core-post-exploitation/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-iot-core-post-exploitation/README.md#L212)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-kendra-post-exploitation/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-kendra-post-exploitation/README.md#L17)
- [`kendra:PutPrincipalMapping`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-kendra-post-exploitation/README.md#L46)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-keyspaces-post-exploitation/README.md

- [`cassandra:Modify`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-keyspaces-post-exploitation/README.md#L123)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lakeformation-post-exploitation/README.md

- [`lakeformation:PutDataLakeSettings`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lakeformation-post-exploitation/README.md#L24)
- [`lakeformation:UpdateLFTagExpression`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lakeformation-post-exploitation/README.md#L208)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-function-access-post-exploitation/README.md

- [`lambda:ListFunctions`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-function-access-post-exploitation/README.md#L17)
- [`lambda:ListVersionsByFunction`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-function-access-post-exploitation/README.md#L17)
- [`lambda:GetFunction`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-function-access-post-exploitation/README.md#L134)
- [`lambda:GetFunctionConfiguration`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-function-access-post-exploitation/README.md#L162)
- [`lambda:GetLayerVersion`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-function-access-post-exploitation/README.md#L188)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-post-exploitation/README.md

- [`lambda:CreateMicrovmAuthToken`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-post-exploitation/README.md#L39)
- [`lambda:GetDurableExecutionHistory`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-post-exploitation/README.md#L77)
- [`lambda:UpdateNetworkConnector`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-post-exploitation/README.md#L212)
- [`lambda:PutFunctionConcurrency`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-post-exploitation/README.md#L462)
- [`lambda:AddLayerVersionPermission`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-post-exploitation/README.md#L651)
- [`lambda:PutProvisionedConcurrencyConfig`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-post-exploitation/README.md#L699)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-post-exploitation/aws-lambda-event-source-mapping-hijack.md

- [`lambda:CreateEventSourceMapping`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-post-exploitation/aws-lambda-event-source-mapping-hijack.md#L15)
- [`lambda:UpdateEventSourceMapping`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-post-exploitation/aws-lambda-event-source-mapping-hijack.md#L68)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-license-manager-post-exploitation/README.md

- [`license-manager:CheckoutBorrowLicense`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-license-manager-post-exploitation/README.md#L15)
- [`license-manager:UpdateLicenseConfiguration`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-license-manager-post-exploitation/README.md#L110)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-macie-post-exploitation/README.md

- [`macie2:CreateInvitations`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-macie-post-exploitation/README.md#L15)
- [`macie2:GetSensitiveDataOccurrences`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-macie-post-exploitation/README.md#L46)
- [`macie2:PutClassificationExportConfiguration`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-macie-post-exploitation/README.md#L78)
- [`macie2:CreateFindingsFilter`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-macie-post-exploitation/README.md#L108)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-mainframe-modernization-post-exploitation/README.md

- [`m2:GetSignedBluinsightsUrl`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-mainframe-modernization-post-exploitation/README.md#L15)
- [`m2:CreateDataSetExportTask`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-mainframe-modernization-post-exploitation/README.md#L46)
- [`m2:CreateDataSetImportTask`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-mainframe-modernization-post-exploitation/README.md#L84)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-managed-grafana-post-exploitation/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-managed-grafana-post-exploitation/README.md#L7)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-managed-prometheus-post-exploitation/README.md

- [`aps:RemoteWrite`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-managed-prometheus-post-exploitation/README.md#L79)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-marketplace-post-exploitation/README.md

- [`aws-marketplace:GetBuyerDashboard`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-marketplace-post-exploitation/README.md#L78)
- [`aws-marketplace:PutDeploymentParameter`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-marketplace-post-exploitation/README.md#L165)
- [`aws-marketplace:BatchMeterUsage`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-marketplace-post-exploitation/README.md#L205)
- [`aws-marketplace:MeterUsage`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-marketplace-post-exploitation/README.md#L237)
- [`aws-marketplace:StartChangeSet`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-marketplace-post-exploitation/README.md#L267)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-medialive-video-post-exploitation/README.md

- [`medialive:DescribeThumbnails`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-medialive-video-post-exploitation/README.md#L17)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-memorydb-data-access-post-exploitation/README.md

- [`memorydb:Connect`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-memorydb-data-access-post-exploitation/README.md#L19)
- [`memorydb:CopySnapshot`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-memorydb-data-access-post-exploitation/README.md#L72)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-memorydb-post-exploitation/README.md

- [`memorydb:UpdateCluster`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-memorydb-post-exploitation/README.md#L17)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-msk-post-exploitation/README.md

- [`kafka:UpdateSecurity`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-msk-post-exploitation/README.md#L9)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-mwaa-post-exploitation/README.md

- [`airflow:CreateWebLoginToken`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-mwaa-post-exploitation/README.md#L19)
- [`airflow:CreateCliToken`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-mwaa-post-exploitation/README.md#L19)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-mwaa-post-exploitation/README.md#L23)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-neptune-post-exploitation/README.md

- [`neptune-db:ReadDataViaQuery`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-neptune-post-exploitation/README.md#L19)
- [`neptune-db:GetStreamRecords`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-neptune-post-exploitation/README.md#L54)
- [`neptune-graph:ReadDataViaQuery`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-neptune-post-exploitation/README.md#L84)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-network-security-manager-post-exploitation/README.md

- [`network-security-manager:UpdateRule`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-network-security-manager-post-exploitation/README.md#L15)
- [`network-security-manager:DeleteAdminAccount`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-network-security-manager-post-exploitation/README.md#L81)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-odb-post-exploitation/README.md

- [`odb:CreateAutonomousDatabaseWallet`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-odb-post-exploitation/README.md#L15)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-opensearch-cross-account-post-exploitation/README.md

- [`es:CreateOutboundConnection`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-opensearch-cross-account-post-exploitation/README.md#L17)
- [`es:AuthorizeVpcEndpointAccess`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-opensearch-cross-account-post-exploitation/README.md#L17)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-organizations-post-exploitation/README.md

- [`organizations:DisableAWSServiceAccess`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-organizations-post-exploitation/README.md#L50)
- [`organizations:CloseAccount`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-organizations-post-exploitation/README.md#L96)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-partner-central-account-post-exploitation/README.md

- [`partnercentral:GetVerification`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-partner-central-account-post-exploitation/README.md#L17)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-pcs-post-exploitation/README.md

- [`pcs:GetCluster`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-pcs-post-exploitation/README.md#L15)
- [`pcs:GetCluster`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-pcs-post-exploitation/README.md#L52)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-pinpoint-post-exploitation/README.md

- [`sms-voice:SendTextMessage`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-pinpoint-post-exploitation/README.md#L17)
- [`mobiletargeting:SendMessages`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-pinpoint-post-exploitation/README.md#L32)
- [`mobiletargeting:CreateCampaign`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-pinpoint-post-exploitation/README.md#L38)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-q-in-connect-post-exploitation/README.md

- [`wisdom:ListMessages`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-q-in-connect-post-exploitation/README.md#L15)
- [`wisdom:ListSpans`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-q-in-connect-post-exploitation/README.md#L15)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-rds-post-exploitation/README.md

- [`rds:DescribeDBProxies`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-rds-post-exploitation/README.md#L15)
- [`rds:CreateDBSnapshot`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-rds-post-exploitation/README.md#L311)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-rds-post-exploitation/README.md#L393)
- [`rds:CreateDBSnapshot`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-rds-post-exploitation/README.md#L427)
- [`rds:CreateDBClusterSnapshot`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-rds-post-exploitation/README.md#L462)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-rds-post-exploitation/README.md#L493)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-redshift-post-exploitation/README.md

- [`redshift:AuthorizeSnapshotAccess`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-redshift-post-exploitation/README.md#L97)
- [`redshift:AuthorizeDataShare`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-redshift-post-exploitation/README.md#L129)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-refactor-spaces-post-exploitation/README.md

- [`refactor-spaces:UpdateRoute`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-refactor-spaces-post-exploitation/README.md#L74)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-resource-explorer-inventory-post-exploitation/README.md

- [`resource-explorer-2:GetView`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-resource-explorer-inventory-post-exploitation/README.md#L17)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-resource-tag-inventory-post-exploitation/README.md

- [`tag:GetResources`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-resource-tag-inventory-post-exploitation/README.md#L17)
- [`tag:StartReportCreation`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-resource-tag-inventory-post-exploitation/README.md#L68)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-route53-dns-takeover-post-exploitation/README.md

- [`route53:CreateHostedZone`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-route53-dns-takeover-post-exploitation/README.md#L111)
- [`acm-pca:IssueCertificate`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-route53-dns-takeover-post-exploitation/README.md#L111)
- [`acm-pca:GetCertificate`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-route53-dns-takeover-post-exploitation/README.md#L111)
- [`ec2:DescribeVpcs`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-route53-dns-takeover-post-exploitation/README.md#L111)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-route53-global-resolver-post-exploitation/README.md

- [`route53globalresolver:GetAccessToken`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-route53-global-resolver-post-exploitation/README.md#L17)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-route53-resolver-post-exploitation/README.md

- [`route53resolver:UpdateResolverRule`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-route53-resolver-post-exploitation/README.md#L17)
- [`route53resolver:CreateResolverRule`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-route53-resolver-post-exploitation/README.md#L30)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-rtb-fabric-post-exploitation/README.md

- [`rtbfabric:UpdateResponderGateway`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-rtb-fabric-post-exploitation/README.md#L15)
- [`rtbfabric:CreateOutboundExternalLink`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-rtb-fabric-post-exploitation/README.md#L63)
- [`rtbfabric:UpdateLinkModuleFlow`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-rtb-fabric-post-exploitation/README.md#L94)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-s3-post-exploitation/README.md

- [`s3:RestoreObject`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-s3-post-exploitation/README.md#L117)
- [`s3:CreateJob`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-s3-post-exploitation/README.md#L664)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-s3-post-exploitation/README.md#L664)
- [`s3:GetBucketAcl`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-s3-post-exploitation/README.md#L789)
- [`s3:GetObjectAcl`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-s3-post-exploitation/README.md#L835)
- [`s3:GetObjectVersionAcl`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-s3-post-exploitation/README.md#L879)
- [`s3:PutObjectVersionAcl`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-s3-post-exploitation/README.md#L879)
- [`s3:PutBucketCORS`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-s3-post-exploitation/README.md#L903)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-s3-post-exploitation/README.md#L942)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sagemaker-configuration-access-post-exploitation/README.md

- [`sagemaker:DescribeAppImageConfig`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sagemaker-configuration-access-post-exploitation/README.md#L17)
- [`sagemaker:ListAppImageConfigs`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sagemaker-configuration-access-post-exploitation/README.md#L17)
- [`sagemaker:DescribeModel`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sagemaker-configuration-access-post-exploitation/README.md#L39)
- [`sagemaker:DescribeTrainingJob`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sagemaker-configuration-access-post-exploitation/README.md#L56)
- [`sagemaker:CreatePresignedMlflowTrackingServerUrl`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sagemaker-configuration-access-post-exploitation/README.md#L121)
- [`sagemaker-mlflow:AccessUI`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sagemaker-configuration-access-post-exploitation/README.md#L121)
- [`sagemaker-mlflow:SearchExperiments`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sagemaker-configuration-access-post-exploitation/README.md#L121)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sagemaker-post-exploitation/README.md

- [`sagemaker:RetryPipelineExecution`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sagemaker-post-exploitation/README.md#L463)
- [`datazone:CreateUserProfile`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sagemaker-post-exploitation/README.md#L490)
- [`iam:GetUser`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sagemaker-post-exploitation/README.md#L490)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-security-agent-post-exploitation/README.md

- [`securityagent:StartPentestJob`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-security-agent-post-exploitation/README.md#L13)
- [`securityagent:ListActorMessages`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-security-agent-post-exploitation/README.md#L42)
- [`securityagent:GetArtifact`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-security-agent-post-exploitation/README.md#L76)
- [`securityagent:StartCodeRemediation`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-security-agent-post-exploitation/README.md#L117)
- [`securityagent:UpdateFinding`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-security-agent-post-exploitation/README.md#L150)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-security-lake-post-exploitation/README.md

- [`securitylake:CreateSubscriber`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-security-lake-post-exploitation/README.md#L50)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-service-catalog-appregistry-post-exploitation/README.md

- [`servicecatalog:GetAttributeGroup`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-service-catalog-appregistry-post-exploitation/README.md#L25)
- [`servicecatalog:UpdateAttributeGroup`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-service-catalog-appregistry-post-exploitation/README.md#L59)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ses-post-exploitation/README.md

- [`ses:SendEmail`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ses-post-exploitation/README.md#L126)
- [`ses:SendRawEmail`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ses-post-exploitation/README.md#L150)
- [`ses:SendTemplatedEmail`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ses-post-exploitation/README.md#L173)
- [`ses:SendBulkTemplatedEmail`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ses-post-exploitation/README.md#L196)
- [`ses:SendBulkEmail`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ses-post-exploitation/README.md#L219)
- [`ses:SendBounce`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ses-post-exploitation/README.md#L240)
- [`ses:SendCustomVerificationEmail`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ses-post-exploitation/README.md#L263)
- [`ses:PutIdentityPolicy`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ses-post-exploitation/README.md#L289)
- [`sesv2:PutEmailIdentityPolicy`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ses-post-exploitation/README.md#L289)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-simpledb-post-exploitation/README.md

- [`sdb:StartDomainExport`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-simpledb-post-exploitation/README.md#L15)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-snowball-post-exploitation/README.md

- [`snowball:GetJobManifest`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-snowball-post-exploitation/README.md#L15)
- [`snowball:UpdateLongTermPricing`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-snowball-post-exploitation/README.md#L49)
- [`snowball:CancelJob`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-snowball-post-exploitation/README.md#L82)
- [`snowball:CreateJob`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-snowball-post-exploitation/README.md#L122)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-snowball-post-exploitation/README.md#L122)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sns-post-exploitation/README.md

- [`sns:SetSMSAttributes`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sns-post-exploitation/README.md#L56)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sqs-post-exploitation/README.md

- [`sqs:UntagQueue`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sqs-post-exploitation/README.md#L74)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ssm-parameter-and-command-access-post-exploitation/README.md

- [`ssm:DescribeParameters`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ssm-parameter-and-command-access-post-exploitation/README.md#L36)
- [`ssm:ListCommands`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ssm-parameter-and-command-access-post-exploitation/README.md#L93)
- [`ssm:ListCommandInvocations`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ssm-parameter-and-command-access-post-exploitation/README.md#L116)
- [`ssm:ListCommands`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ssm-parameter-and-command-access-post-exploitation/README.md#L116)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sso-and-identitystore-post-exploitation/README.md

- [`sso:DeletePermissionSet`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sso-and-identitystore-post-exploitation/README.md#L22)
- [`sso:DeleteAccountAssignment`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sso-and-identitystore-post-exploitation/README.md#L52)
- [`sso:PutPermissionsBoundaryToPermissionSet`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sso-and-identitystore-post-exploitation/README.md#L87)
- [`sso:ProvisionPermissionSet`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sso-and-identitystore-post-exploitation/README.md#L87)
- [`sso:GetRoleCredentials`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sso-and-identitystore-post-exploitation/README.md#L130)
- [`sso-admin:CreateTrustedTokenIssuer`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sso-and-identitystore-post-exploitation/README.md#L168)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-stepfunctions-post-exploitation/README.md

- [`states:RevealSecrets`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-stepfunctions-post-exploitation/README.md#L28)
- [`lambda:UpdateFunctionCode`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-stepfunctions-post-exploitation/README.md#L244)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-storage-gateway-chap-post-exploitation/README.md

- [`storagegateway:DescribeChapCredentials`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-storage-gateway-chap-post-exploitation/README.md#L17)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-storage-gateway-post-exploitation/README.md

- [`storagegateway:CreateNFSFileShare`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-storage-gateway-post-exploitation/README.md#L17)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-storage-gateway-post-exploitation/README.md#L17)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-timestream-post-exploitation/README.md

- [`timestream:Unload`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-timestream-post-exploitation/README.md#L105)
- [`timestream:WriteRecords`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-timestream-post-exploitation/README.md#L136)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-timestream-post-exploitation/README.md#L179)
- [`timestream:ExecuteScheduledQuery`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-timestream-post-exploitation/README.md#L304)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-transfer-family-post-exploitation/README.md

- [`transfer:TestIdentityProvider`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-transfer-family-post-exploitation/README.md#L81)
- [`transfer:UpdateServer`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-transfer-family-post-exploitation/README.md#L133)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-uxc-post-exploitation/README.md

- [`uxc:UpdateAccountCustomizations`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-uxc-post-exploitation/README.md#L15)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-vpn-post-exploitation/README.md

- [`ec2:ModifyVpnConnection`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-vpn-post-exploitation/README.md#L72)
- [`ec2:ModifyVpnTunnelOptions`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-vpn-post-exploitation/README.md#L72)
- [`ec2:AuthorizeClientVpnIngress`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-vpn-post-exploitation/README.md#L135)
- [`ec2:AssociateClientVpnTargetNetwork`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-vpn-post-exploitation/README.md#L179)
- [`ec2:CreateClientVpnRoute`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-vpn-post-exploitation/README.md#L179)
- [`ec2:ApplySecurityGroupsToClientVpnTargetNetwork`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-vpn-post-exploitation/README.md#L243)
- [`ec2:ModifyClientVpnEndpoint`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-vpn-post-exploitation/README.md#L298)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-waf-post-exploitation/README.md

- [`wafv2:DeleteRuleGroup`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-waf-post-exploitation/README.md#L194)
- [`iam:CreateServiceLinkedRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-waf-post-exploitation/README.md#L458)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-wickr-post-exploitation/README.md

- [`wickr:GetOidcInfo`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-wickr-post-exploitation/README.md#L17)
- [`wickr:GetOpentdfConfig`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-wickr-post-exploitation/README.md#L52)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-workdocs-post-exploitation/README.md

- [`workdocs:AddResourcePermissions`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-workdocs-post-exploitation/README.md#L44)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-workmail-post-exploitation/README.md

- [`workmailmessageflow:GetRawMessageContent`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-workmail-post-exploitation/README.md#L75)

### src/pentesting-cloud/aws-security/aws-post-exploitation/aws-workspaces-post-exploitation/README.md

- [`workspaces:UpdateWorkspaceImagePermission`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-workspaces-post-exploitation/README.md#L17)
- [`workspaces:ModifySamlProperties`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-workspaces-post-exploitation/README.md#L46)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-amplify-privesc/README.md

- [`amplifybackend:CreateToken`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-amplify-privesc/README.md#L13)
- [`amplifybackend:GetToken`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-amplify-privesc/README.md#L56)
- [`amplify:GetJob`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-amplify-privesc/README.md#L80)
- [`amplify:GetArtifactUrl`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-amplify-privesc/README.md#L121)
- [`amplify:StartJob`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-amplify-privesc/README.md#L125)
- [`amplify:StartJob`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-amplify-privesc/README.md#L175)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-amplify-privesc/README.md#L210)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-apigateway-privesc/README.md

- [`apigateway:POST`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-apigateway-privesc/README.md#L18)
- [`apigateway:GET`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-apigateway-privesc/README.md#L41)
- [`apigateway:UpdateRestApiPolicy`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-apigateway-privesc/README.md#L45)
- [`apigateway:PATCH`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-apigateway-privesc/README.md#L45)
- [`apigateway:PUT`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-apigateway-privesc/README.md#L49)
- [`apigateway:POST`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-apigateway-privesc/README.md#L49)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-apigateway-privesc/README.md#L49)
- [`apigateway:PATCH`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-apigateway-privesc/README.md#L88)
- [`apigateway:POST`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-apigateway-privesc/README.md#L88)
- [`apigateway:PATCH`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-apigateway-privesc/README.md#L138)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-appconfig-privesc/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-appconfig-privesc/README.md#L17)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-apprunner-privesc/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-apprunner-privesc/README.md#L43)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-appstream-privesc/README.md

- [`appstream:CreateImageBuilder`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-appstream-privesc/README.md#L312)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-appstream-privesc/README.md#L312)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-appsync-privesc/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-appsync-privesc/README.md#L13)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-appsync-privesc/README.md#L91)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-athena-spark-role-privesc/README.md

- [`athena:StartCalculationExecution`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-athena-spark-role-privesc/README.md#L51)
- [`athena:CreatePresignedNotebookUrl`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-athena-spark-role-privesc/README.md#L129)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-athena-stored-query-privesc/README.md

- [`athena:UpdateNotebook`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-athena-stored-query-privesc/README.md#L23)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-batch-privesc/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-batch-privesc/README.md#L13)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-bedrock-agentcore-privesc/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-bedrock-agentcore-privesc/README.md#L49)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-bedrock-agentcore-privesc/README.md#L100)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-bedrock-agentcore-privesc/README.md#L135)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-bedrock-agentcore-privesc/README.md#L167)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-bedrock-privesc/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-bedrock-privesc/README.md#L137)
- [`lambda:UpdateFunctionCode`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-bedrock-privesc/README.md#L170)
- [`bedrock:InvokeAgent`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-bedrock-privesc/README.md#L170)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-budgets-privesc/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-budgets-privesc/README.md#L24)
- [`budgets:ExecuteBudgetAction`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-budgets-privesc/README.md#L24)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-chatbot-privesc/README.md

- [`chatbot:CreateSlackChannelConfiguration`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-chatbot-privesc/README.md#L18)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-chatbot-privesc/README.md#L18)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cloudcontrol-privesc/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cloudcontrol-privesc/README.md#L17)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cloudformation-privesc/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cloudformation-privesc/README.md#L18)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cloudformation-privesc/README.md#L52)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cloudformation-privesc/README.md#L101)
- [`cloudformation:ExecuteChangeSet`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cloudformation-privesc/README.md#L101)
- [`cloudformation:ExecuteChangeSet`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cloudformation-privesc/README.md#L149)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cloudformation-privesc/README.md#L171)
- [`s3:PutObject`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cloudformation-privesc/README.md#L206)
- [`ssm:PutParameter`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cloudformation-privesc/README.md#L251)
- [`cloudformation:RegisterType`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cloudformation-privesc/README.md#L304)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cloudformation-privesc/README.md#L304)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cloudfront-privesc/README.md

- [`cloudfront:GetDistributionConfig`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cloudfront-privesc/README.md#L13)
- [`cloudfront:CreateFunction`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cloudfront-privesc/README.md#L17)
- [`cloudfront:DescribeFunction`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cloudfront-privesc/README.md#L17)
- [`cloudfront:PublishFunction`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cloudfront-privesc/README.md#L17)
- [`cloudfront:GetDistributionConfig`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cloudfront-privesc/README.md#L17)
- [`lambda:CreateFunction`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cloudfront-privesc/README.md#L21)
- [`lambda:PublishVersion`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cloudfront-privesc/README.md#L21)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cloudfront-privesc/README.md#L21)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codebuild-privesc/README.md

- [`codebuild:StartBuildBatch`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codebuild-privesc/README.md#L21)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codebuild-privesc/README.md#L308)
- [`codebuild:CreateProject`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codebuild-privesc/README.md#L308)
- [`codebuild:StartBuildBatch`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codebuild-privesc/README.md#L308)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codebuild-privesc/README.md#L450)
- [`codebuild:StartBuildBatch`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codebuild-privesc/README.md#L450)
- [`codebuild:StartBuildBatch`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codebuild-privesc/README.md#L502)
- [`s3:PutObject`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codebuild-privesc/README.md#L623)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codeconnections-privesc/README.md

- [`codeconnections:CreateSyncConfiguration`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codeconnections-privesc/README.md#L13)
- [`codeconnections:UpdateSyncConfiguration`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codeconnections-privesc/README.md#L13)
- [`codeconnections:PassRepository`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codeconnections-privesc/README.md#L13)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codeconnections-privesc/README.md#L13)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codepipeline-privesc/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codepipeline-privesc/README.md#L21)
- [`codebuild:CreateProject`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codepipeline-privesc/README.md#L21)
- [`codepipeline:UpdatePipeline`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codepipeline-privesc/README.md#L50)
- [`s3:PutObject`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codepipeline-privesc/README.md#L204)
- [`codepipeline:PutJobSuccessResult`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codepipeline-privesc/README.md#L280)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codestar-privesc/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codestar-privesc/README.md#L25)
- [`codestar:CreateProject`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codestar-privesc/README.md#L25)
- [`codestar:CreateProject`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codestar-privesc/README.md#L46)
- [`codestar:AssociateTeamMember`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codestar-privesc/README.md#L46)
- [`codestar:CreateProjectFromTemplate`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codestar-privesc/README.md#L91)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cognito-privesc/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cognito-privesc/README.md#L36)
- [`cognito-identity:GetOpenIdTokenForDeveloperIdentity`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cognito-privesc/README.md#L127)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cognito-privesc/README.md#L240)
- [`cognito-idp:AdminRespondToAuthChallenge`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-cognito-privesc/README.md#L343)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-config-privesc/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-config-privesc/README.md#L102)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-datapipeline-privesc/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-datapipeline-privesc/README.md#L24)
- [`datapipeline:PutPipelineDefinition`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-datapipeline-privesc/README.md#L24)
- [`datapipeline:ActivatePipeline`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-datapipeline-privesc/README.md#L24)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-datasync-privesc/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-datasync-privesc/README.md#L18)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-datasync-privesc/README.md#L98)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-directory-services-privesc/README.md

- [`ds:ResetUserPassword`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-directory-services-privesc/README.md#L21)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-dlm-privesc/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-dlm-privesc/README.md#L22)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ebs-privesc/README.md

- [`ebs:ListSnapshotBlocks`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ebs-privesc/README.md#L13)
- [`ebs:GetSnapshotBlock`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ebs-privesc/README.md#L13)
- [`ec2:DescribeSnapshots`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ebs-privesc/README.md#L13)
- [`ec2:CreateSnapshot`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ebs-privesc/README.md#L17)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ec2-privesc/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ec2-privesc/README.md#L13)
- [`ec2:RunInstances`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ec2-privesc/README.md#L13)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ec2-privesc/README.md#L98)
- [`iam:AddRoleToInstanceProfile`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ec2-privesc/README.md#L98)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ec2-privesc/README.md#L135)
- [`ec2:AssociateIamInstanceProfile`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ec2-privesc/README.md#L135)
- [`ec2:DisassociateIamInstanceProfile`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ec2-privesc/README.md#L135)
- [`ec2:ReplaceIamInstanceProfileAssociation`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ec2-privesc/README.md#L135)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ec2-privesc/README.md#L170)
- [`autoscaling:CreateLaunchConfiguration`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ec2-privesc/README.md#L307)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ec2-privesc/README.md#L307)
- [`autoscaling:CreateAutoScalingGroup`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ec2-privesc/README.md#L307)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecr-privesc/README.md

- [`ecr:BatchCheckLayerAvailability`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecr-privesc/README.md#L42)
- [`ecr:CompleteLayerUpload`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecr-privesc/README.md#L42)
- [`ecr:InitiateLayerUpload`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecr-privesc/README.md#L42)
- [`ecr:UploadLayerPart`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecr-privesc/README.md#L42)
- [`sts:GetServiceBearerToken`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecr-privesc/README.md#L85)
- [`ecr-public:BatchCheckLayerAvailability`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecr-privesc/README.md#L85)
- [`ecr-public:CompleteLayerUpload`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecr-privesc/README.md#L85)
- [`ecr-public:InitiateLayerUpload`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecr-privesc/README.md#L85)
- [`ecr-public:UploadLayerPart`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecr-privesc/README.md#L85)
- [`ecr:CreatePullThroughCacheRule`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecr-privesc/README.md#L249)
- [`ecr:PutAccountSetting`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecr-privesc/README.md#L387)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecs-privesc/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecs-privesc/README.md#L15)
- [`ecs:RegisterTaskDefinition`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecs-privesc/README.md#L15)
- [`ecs:RunTask`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecs-privesc/README.md#L15)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecs-privesc/README.md#L103)
- [`ecs:RunTask`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecs-privesc/README.md#L103)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecs-privesc/README.md#L178)
- [`ecs:RegisterTaskDefinition`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecs-privesc/README.md#L178)
- [`ecs:StartTask`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecs-privesc/README.md#L178)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecs-privesc/README.md#L215)
- [`ecs:RegisterTaskDefinition`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecs-privesc/README.md#L215)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecs-privesc/README.md#L336)
- [`ecs:RunTask`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecs-privesc/README.md#L336)
- [`ecs:RegisterTaskDefinition`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecs-privesc/README.md#L364)
- [`ecs:ExecuteCommand`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecs-privesc/README.md#L430)
- [`ecs:DescribeTasks`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecs-privesc/README.md#L430)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecs-privesc/README.md#L523)
- [`ec2:RunInstances`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecs-privesc/README.md#L523)
- [`ecs:RegisterContainerInstance`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecs-privesc/README.md#L547)
- [`ecs:DeregisterContainerInstance`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecs-privesc/README.md#L547)
- [`ecs:StartTask`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecs-privesc/README.md#L547)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecs-privesc/README.md#L547)
- [`ecs:RegisterTaskDefinition`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecs-privesc/README.md#L613)
- [`ecs:CreateTaskSet`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecs-privesc/README.md#L613)
- [`ecs:UpdateServicePrimaryTaskSet`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecs-privesc/README.md#L613)
- [`ecs:DescribeTaskSets`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ecs-privesc/README.md#L613)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-eks-privesc/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-eks-privesc/README.md#L144)
- [`iam:GetRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-eks-privesc/README.md#L144)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-eks-privesc/README.md#L182)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-eks-privesc/README.md#L224)
- [`eks:CreateNodegroup`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-eks-privesc/README.md#L224)
- [`eks:CreateFargateProfile`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-eks-privesc/README.md#L224)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-elastic-beanstalk-privesc/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-elastic-beanstalk-privesc/README.md#L91)
- [`cloudformation:DescribeStackResources`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-elastic-beanstalk-privesc/README.md#L148)
- [`cloudformation:DescribeStackResource`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-elastic-beanstalk-privesc/README.md#L148)
- [`autoscaling:DescribeAutoScalingGroups`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-elastic-beanstalk-privesc/README.md#L148)
- [`autoscaling:SuspendProcesses`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-elastic-beanstalk-privesc/README.md#L148)
- [`elasticbeanstalk:DescribeEnvironmentResources`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-elastic-beanstalk-privesc/README.md#L271)
- [`elasticloadbalancing:ModifyLoadBalancerAttributes`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-elastic-beanstalk-privesc/README.md#L271)
- [`s3:ListBucket`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-elastic-beanstalk-privesc/README.md#L271)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-emr-privesc/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-emr-privesc/README.md#L15)
- [`s3:PutObject`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-emr-privesc/README.md#L117)
- [`elasticmapreduce:CreateEditor`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-emr-privesc/README.md#L167)
- [`iam:ListRoles`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-emr-privesc/README.md#L167)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-emr-privesc/README.md#L167)
- [`elasticmapreduce:DescribeEditor`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-emr-privesc/README.md#L167)
- [`elasticmapreduce:OpenEditorInConsole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-emr-privesc/README.md#L167)
- [`elasticmapreduce:OpenEditorInConsole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-emr-privesc/README.md#L194)
- [`elasticmapreduce:GetClusterSessionCredentials`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-emr-privesc/README.md#L216)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-emr-privesc/README.md#L216)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-emr-serverless-privesc/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-emr-serverless-privesc/README.md#L18)
- [`emr-containers:GetManagedEndpointSessionCredentials`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-emr-serverless-privesc/README.md#L60)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-emr-serverless-privesc/README.md#L60)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-eventbridge-pipes-privesc/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-eventbridge-pipes-privesc/README.md#L18)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-gamelift/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-gamelift/README.md#L13)
- [`gamelift:GetComputeAccess`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-gamelift/README.md#L58)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-iam-privesc/README.md

- [`iam:CreateRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-iam-privesc/README.md#L255)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-iam-privesc/README.md#L389)
- [`iam:ListSAMLProviders`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-iam-privesc/README.md#L463)
- [`iam:GetSAMLProvider`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-iam-privesc/README.md#L463)
- [`iam:CreateVirtualMFADevice`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-iam-privesc/README.md#L842)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-iot-core-privesc/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-iot-core-privesc/README.md#L15)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-iot-privesc/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-iot-privesc/README.md#L18)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-iot-privesc/README.md#L75)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-kms-privesc/README.md

- [`kms:ReplicateKey`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-kms-privesc/README.md#L138)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-lambda-privesc/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-lambda-privesc/README.md#L52)
- [`lambda:CreateFunction`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-lambda-privesc/README.md#L52)
- [`lambda:InvokeFunction`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-lambda-privesc/README.md#L52)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-lambda-privesc/README.md#L140)
- [`lambda:UpdateFunctionConfiguration`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-lambda-privesc/README.md#L140)
- [`lambda:InvokeFunction`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-lambda-privesc/README.md#L140)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-lambda-privesc/README.md#L173)
- [`lambda:CreateFunction`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-lambda-privesc/README.md#L173)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-lambda-privesc/README.md#L199)
- [`lambda:CreateFunction`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-lambda-privesc/README.md#L199)
- [`lambda:CreateEventSourceMapping`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-lambda-privesc/README.md#L199)
- [`lambda:UpdateFunctionCode`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-lambda-privesc/README.md#L378)
- [`lambda:UpdateFunctionConfiguration`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-lambda-privesc/README.md#L412)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-lambda-privesc/README.md#L539)
- [`lambda:CreateFunction`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-lambda-privesc/README.md#L539)
- [`lambda:InvokeFunctionUrl`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-lambda-privesc/README.md#L539)
- [`lambda:DeleteFunctionCodeSigningConfig`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-lambda-privesc/README.md#L560)
- [`lambda:PutFunctionCodeSigningConfig`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-lambda-privesc/README.md#L560)
- [`lambda:UpdateFunctionCode`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-lambda-privesc/README.md#L560)
- [`signer:StartSigningJob`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-lambda-privesc/README.md#L647)
- [`lambda:UpdateFunctionCode`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-lambda-privesc/README.md#L647)
- [`lambda:CreateMicrovmShellAuthToken`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-lambda-privesc/README.md#L715)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-managed-grafana-privesc/README.md

- [`grafana:UpdatePermissions`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-managed-grafana-privesc/README.md#L150)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-mq-privesc/README.md

- [`mq:UpdateBrokerAccessConfiguration`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-mq-privesc/README.md#L97)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-msk-privesc/README.md

- [`kafka:UpdateSecurity`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-msk-privesc/README.md#L13)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-mwaa-privesc/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-mwaa-privesc/README.md#L5)
- [`airflow:CreateWebLoginToken`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-mwaa-privesc/README.md#L76)
- [`airflow:CreateCliToken`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-mwaa-privesc/README.md#L76)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-mwaa-privesc/README.md#L116)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-pca-connector-ad-privesc/README.md

- [`pca-connector-ad:CreateTemplate`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-pca-connector-ad-privesc/README.md#L23)
- [`pca-connector-ad:UpdateTemplate`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-pca-connector-ad-privesc/README.md#L74)
- [`pca-connector-ad:CreateTemplateGroupAccessControlEntry`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-pca-connector-ad-privesc/README.md#L101)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-proton-privesc/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-proton-privesc/README.md#L17)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-quicksight-privesc/README.md

- [`quicksight:RegisterUser`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-quicksight-privesc/README.md#L60)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-rds-privesc/README.md

- [`rds:AddRoleToDBCluster`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-rds-privesc/README.md#L197)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-rds-privesc/README.md#L197)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-rds-privesc/README.md#L233)
- [`rds:AddRoleToDBInstance`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-rds-privesc/README.md#L284)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-rds-privesc/README.md#L284)
- [`rds:AddRoleToDBCluster`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-rds-privesc/README.md#L313)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-rds-privesc/README.md#L313)
- [`rds:SwitchoverBlueGreenDeployment`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-rds-privesc/README.md#L313)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-redshift-privesc/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-redshift-privesc/README.md#L93)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-redshift-privesc/README.md#L93)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-region-switch-privesc/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-region-switch-privesc/README.md#L20)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-s3-privesc/README.md

- [`s3:PutObject`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-s3-privesc/README.md#L13)
- [`s3:PutObject`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-s3-privesc/README.md#L68)
- [`s3:PutObject`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-s3-privesc/README.md#L92)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sagemaker-privesc/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sagemaker-privesc/README.md#L13)
- [`sagemaker:CreateNotebookInstance`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sagemaker-privesc/README.md#L13)
- [`sagemaker:CreatePresignedNotebookInstanceUrl`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sagemaker-privesc/README.md#L13)
- [`sagemaker:CreatePresignedNotebookInstanceUrl`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sagemaker-privesc/README.md#L50)
- [`s3:PutObject`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sagemaker-privesc/README.md#L145)
- [`sagemaker:CreateProcessingJob`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sagemaker-privesc/README.md#L248)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sagemaker-privesc/README.md#L248)
- [`sagemaker:CreateTrainingJob`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sagemaker-privesc/README.md#L289)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sagemaker-privesc/README.md#L289)
- [`sagemaker:CreateHyperParameterTuningJob`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sagemaker-privesc/README.md#L335)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sagemaker-privesc/README.md#L335)
- [`sagemaker:UpdateUserProfile`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sagemaker-privesc/README.md#L462)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sagemaker-privesc/README.md#L462)
- [`sagemaker:CreateApp`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sagemaker-privesc/README.md#L462)
- [`sagemaker:CreatePresignedDomainUrl`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sagemaker-privesc/README.md#L462)
- [`sagemaker:DeleteApp`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sagemaker-privesc/README.md#L462)
- [`sagemaker:CreateUserProfile`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sagemaker-privesc/README.md#L540)
- [`sagemaker:CreateApp`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sagemaker-privesc/README.md#L540)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sagemaker-privesc/README.md#L540)
- [`sagemaker:CreatePresignedDomainUrl`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sagemaker-privesc/README.md#L540)
- [`sagemaker:DeleteApp`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sagemaker-privesc/README.md#L540)
- [`sagemaker:CreateApp`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sagemaker-privesc/README.md#L619)
- [`sagemaker:CreatePresignedDomainUrl`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sagemaker-privesc/README.md#L619)
- [`sagemaker:UpdateClusterSoftware`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sagemaker-privesc/README.md#L663)
- [`sagemaker:UpdateNotebookInstanceLifecycleConfig`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sagemaker-privesc/README.md#L764)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-secrets-manager-privesc/README.md

- [`secretsmanager:ListSecrets`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-secrets-manager-privesc/README.md#L17)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ssm-privesc/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ssm-privesc/README.md#L92)
- [`ssm:UpdateManagedInstanceRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ssm-privesc/README.md#L149)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ssm-privesc/README.md#L149)
- [`ssm:UpdateServiceSetting`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ssm-privesc/README.md#L193)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ssm-privesc/README.md#L193)
- [`ssm:StartAccessRequest`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ssm-privesc/README.md#L333)
- [`ssm:GetAccessToken`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ssm-privesc/README.md#L333)
- [`ssm:UpdateDocument`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ssm-privesc/README.md#L430)
- [`ssm:ListDocuments`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ssm-privesc/README.md#L430)
- [`ssm:GetDocument`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ssm-privesc/README.md#L430)
- [`ssm:RegisterTargetWithMaintenanceWindow`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ssm-privesc/README.md#L486)
- [`ssm:DescribeMaintenanceWindows`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ssm-privesc/README.md#L486)
- [`ec2:DescribeInstances`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-ssm-privesc/README.md#L486)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sso-and-identitystore-privesc/README.md

- [`sso-directory:UpdatePassword`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sso-and-identitystore-privesc/README.md#L23)
- [`identitystore:CreateGroupMembership`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sso-and-identitystore-privesc/README.md#L43)
- [`sso:PutInlinePolicyToPermissionSet`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sso-and-identitystore-privesc/README.md#L66)
- [`sso:ProvisionPermissionSet`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sso-and-identitystore-privesc/README.md#L66)
- [`sso:AttachManagedPolicyToPermissionSet`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sso-and-identitystore-privesc/README.md#L108)
- [`sso:ProvisionPermissionSet`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sso-and-identitystore-privesc/README.md#L108)
- [`sso:AttachCustomerManagedPolicyReferenceToPermissionSet`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sso-and-identitystore-privesc/README.md#L136)
- [`sso:ProvisionPermissionSet`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sso-and-identitystore-privesc/README.md#L136)
- [`sso:CreateAccountAssignment`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sso-and-identitystore-privesc/README.md#L167)
- [`sso:GetRoleCredentials`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sso-and-identitystore-privesc/README.md#L191)
- [`sso:DetachManagedPolicyFromPermissionSet`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sso-and-identitystore-privesc/README.md#L195)
- [`sso:DetachCustomerManagedPolicyReferenceFromPermissionSet`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sso-and-identitystore-privesc/README.md#L219)
- [`sso:DeleteInlinePolicyFromPermissionSet`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sso-and-identitystore-privesc/README.md#L243)
- [`sso:DeletePermissionsBoundaryFromPermissionSet`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sso-and-identitystore-privesc/README.md#L267)
- [`sso:CreatePermissionSet`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sso-and-identitystore-privesc/README.md#L291)
- [`sso:CreateAccountAssignment`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sso-and-identitystore-privesc/README.md#L291)
- [`sso-admin:CreateTrustedTokenIssuer`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sso-and-identitystore-privesc/README.md#L343)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-stepfunctions-privesc/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-stepfunctions-privesc/README.md#L41)
- [`states:CreateStateMachine`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-stepfunctions-privesc/README.md#L133)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-stepfunctions-privesc/README.md#L133)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-stepfunctions-privesc/README.md#L234)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sts-privesc/README.md

- [`sts:AssumeRoleWithSAML`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sts-privesc/README.md#L59)
- [`sts:AssumeRoleWithWebIdentity`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sts-privesc/README.md#L112)
- [`sts:AssumeRoot`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sts-privesc/README.md#L125)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-workdocs-privesc/README.md

- [`workdocs:AddResourcePermissions`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-workdocs-privesc/README.md#L29)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-workspaces-privesc/README.md

- [`workspaces-instances:CreateWorkspaceInstance`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-workspaces-privesc/README.md#L21)
- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-workspaces-privesc/README.md#L21)
- [`ec2:RunInstances`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-workspaces-privesc/README.md#L21)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/eventbridgescheduler-privesc/README.md

- [`iam:PassRole`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/eventbridgescheduler-privesc/README.md#L15)
- [`scheduler:CreateSchedule`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/eventbridgescheduler-privesc/README.md#L15)
- [`scheduler:UpdateSchedule`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/eventbridgescheduler-privesc/README.md#L15)

### src/pentesting-cloud/aws-security/aws-privilege-escalation/route53-createhostedzone-route53-changeresourcerecordsets-acm-pca-issuecertificate-acm-pca-getcer/README.md

- [`route53:CreateHostedZone`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/route53-createhostedzone-route53-changeresourcerecordsets-acm-pca-issuecertificate-acm-pca-getcer/README.md#L13)
- [`acm-pca:IssueCertificate`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/route53-createhostedzone-route53-changeresourcerecordsets-acm-pca-issuecertificate-acm-pca-getcer/README.md#L13)
- [`acm-pca:GetCertificate`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/route53-createhostedzone-route53-changeresourcerecordsets-acm-pca-issuecertificate-acm-pca-getcer/README.md#L13)
- [`ec2:DescribeVpcs`](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/route53-createhostedzone-route53-changeresourcerecordsets-acm-pca-issuecertificate-acm-pca-getcer/README.md#L13)
