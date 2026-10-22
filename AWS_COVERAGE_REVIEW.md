# AWS pages requiring direct-rule coverage review

Source snapshot: HackTricks Cloud `47c375ae496ae89f81936f47ab1cb84885c88373`. This is a **triage list**: zero direct YAML reference to a page does not prove its techniques lack rules, and a heading may be navigation, setup, duplicate or a technique not observable in CloudTrail. Review each heading against actual rule semantics and test evidence before marking it covered or uncovered.

Pages with at least three level-three headings and no direct YAML reference: **59**. Total headings: **258**.

## [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sso-and-identitystore-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sso-and-identitystore-privesc/README.md) (15 headings)

- \`sso-directory:UpdatePassword\`
- \`identitystore:CreateGroupMembership\`
- \`sso:PutInlinePolicyToPermissionSet\`, \`sso:ProvisionPermissionSet\`
- \`sso:AttachManagedPolicyToPermissionSet\`, \`sso:ProvisionPermissionSet\`
- \`sso:AttachCustomerManagedPolicyReferenceToPermissionSet\`, \`sso:ProvisionPermissionSet\`
- \`sso:CreateAccountAssignment\`
- \`sso:GetRoleCredentials\`
- \`sso:DetachManagedPolicyFromPermissionSet\`
- \`sso:DetachCustomerManagedPolicyReferenceFromPermissionSet\`
- \`sso:DeleteInlinePolicyFromPermissionSet\`
- \`sso:DeletePermissionsBoundaryFromPermissionSet\`
- \`sso:CreatePermissionSet\` (+ policy attach + \`sso:CreateAccountAssignment\`) — build an admin path from scratch
- \`identitystore:CreateUser\` / \`sso-directory:CreateUser\` (+ group membership / assignment)
- \`sso-admin:CreateTrustedTokenIssuer\` (+ \`CreateApplication\` / \`PutApplicationGrant\`) — impersonate any user via a rogue trusted token issuer
- \`account-access:CreateEntitlement\` — assign an existing IAM role to a controlled Identity Center user

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-supply-chain-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-supply-chain-post-exploitation/README.md) (9 headings)

- Redirect an ERP connection to expose credentials used by the instance role
- Read the supply-chain architecture and sensitive metadata
- Read Insights chat messages without permission to the Insight
- Export a dataset through a data integration flow
- Export complete demand and supply plans through the web app
- Replace an existing flow to poison or redirect processing
- Poison the product BOM through an import job
- Poison or delete dataset rows with real-time events
- Destructive deletion and operational denial

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-connect-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-connect-post-exploitation/README.md) (7 headings)

- \`connect:CreateParticipant\` — Mint a live chat or WebRTC participant bearer
- Collect contact metadata, attributes, references and files
- Recover flow source and integration targets
- Read or monitor live conversations
- Stream an active chat to a cross-account SNS topic
- Intercept and alter an active chat with a custom message processor
- Disable flow execution logs

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/aws-ebs-multi-attach-data-theft.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-ec2-ebs-ssm-and-vpc-post-exploitation/aws-ebs-multi-attach-data-theft.md) (7 headings)

- Summary
- Requirements
- Notes
- Prepare a Multi-Attach io2 volume and attach to victim
- Attach the same volume to the attacker instance
- Mount read-only on the attacker and read data
- Impact

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-migration-hub-strategy-recommendations-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-migration-hub-strategy-recommendations-post-exploitation/README.md) (6 headings)

- Harvest credentials from a compromised collector host
- Abuse captured collector AWS credentials
- Read migration inventory and credential/report references
- Download assessment artifacts from their disclosed S3 keys
- Poison the durable server/application inventory through a manual import
- Override migration recommendations or exclude components from assessment

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-security-hub-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-security-hub-post-exploitation/README.md) (6 headings)

- Disabling standards and controls
- Killing the alerting path (EventBridge / custom actions)
- Suppressing individual findings (\`BatchUpdateFindings\`)
- Auto-suppressing future findings (Automation Rules)
- Breaking centralization (members / admin)
- Fully disabling Security Hub / Security Hub CSPM

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-security-incident-response-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-security-incident-response-post-exploitation/README.md) (6 headings)

- Read the responders' view of the intrusion
- Classify known accounts against the victim organization and IR coverage
- Download or poison forensic attachments without direct S3 permission
- Disable triage or remove organization units from IR coverage
- Immediately destroy the Security IR membership and case access
- Sabotage the case and stop response work

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-shield-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-shield-post-exploitation/README.md) (6 headings)

- Degrading Shield Response Team engagement
- Disabling Shield Advanced subscription auto-renewal
- Removing an individual Shield Advanced protection
- Deleting a protection group
- Disabling legacy automatic application-layer response
- Detaching a health check from a protection

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-timestream-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-timestream-post-exploitation/README.md) (6 headings)

- Timestream for InfluxDB: recover the initial database administrator credential
- LiveAnalytics: query a table with \`timestream:Select\`
- LiveAnalytics: export query results to S3 with \`timestream:Unload\`
- LiveAnalytics: invisible record injection, upsert and version pinning with \`timestream:WriteRecords\`
- \`timestream:CreateScheduledQuery\` + \`iam:PassRole\` — run SQL and downstream writes as a scheduled-query role
- \`timestream:ExecuteScheduledQuery\` — trigger an already stored role workflow

## [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-emr-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-emr-privesc/README.md) (6 headings)

- \`iam:PassRole\`, \`elasticmapreduce:RunJobFlow\`
- \`elasticmapreduce:AddJobFlowSteps\` — execute as an existing cluster instance profile
- \`s3:PutObject\` on a configured bootstrap or step script
- \`elasticmapreduce:CreateEditor\`, \`iam:ListRoles\`, \`elasticmapreduce:ListClusters\`, \`iam:PassRole\`, \`elasticmapreduce:DescribeEditor\`, \`elasticmapreduce:OpenEditorInConsole\`
- Legacy \`elasticmapreduce:OpenEditorInConsole\` boundary
- \`elasticmapreduce:GetClusterSessionCredentials\` — vend a runtime role's credentials without \`iam:PassRole\`

## [src/pentesting-cloud/aws-security/aws-persistence/aws-invoicing-and-billing-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-invoicing-and-billing-persistence/README.md) (5 headings)

- Persist invoice delivery through a procurement portal preference
- Persist recurring CUR 2.0 delivery to an external S3 bucket
- Make a member account an invoice receiver
- Enable a latent legacy IAM billing entitlement
- Share a custom Billing view to an external account

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-audit-manager-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-audit-manager-post-exploitation/README.md) (5 headings)

- Redirect assessment reports or Evidence Finder exports to another S3 account
- Read evidence or download an assessment report
- Delegate a control set to another role
- Poison, suppress, or falsely review evidence
- Stop collection or destroy Audit Manager data

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-codebuild-post-exploitation/aws-codebuild-untrusted-pr-webhook-bypass.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-codebuild-post-exploitation/aws-codebuild-untrusted-pr-webhook-bypass.md) (5 headings)

- Why this is dangerous
- Misconfigurations that allow external PR code execution
- Token leakage from memory
- Finding CodeBuild URLs in GitHub PRs
- Quick audit checklist

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-elemental-inference-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-elemental-inference-post-exploitation/README.md) (5 headings)

- \`elemental-inference:GetMetadata\` — recover transcripts and inference results
- \`elemental-inference:ExportDictionaryEntries\` — steal the custom vocabulary
- \`elemental-inference:UpdateDictionary\` — poison vocabulary without read access
- \`elemental-inference:PutMedia\` — inject attacker-controlled source segments
- \`elemental-inference:UpdateFeed\` — blindly replace output configuration

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-firewall-manager-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-firewall-manager-post-exploitation/README.md) (5 headings)

- Bypass detection
- \`fms:PutNotificationChannel\`, \`fms:DeleteNotificationChannel\`
- \`fms:BatchAssociateResource\`, \`fms:BatchDisassociateResource\`, \`fms:PutResourceSet\`, \`fms:DeleteResourceSet\`
- \`fms:PutAppsList\`, \`fms:DeleteAppsList\`
- \`fms:PutProtocolsList\`, \`fms:DeleteProtocolsList\`

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-gamelift-streams-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-gamelift-streams-post-exploitation/README.md) (5 headings)

- Open an admin shell in a live runtime
- Recover bearer stream URLs and frozen session configuration
- Reconnect to an active or disconnected session
- Recover stream-session arguments, signaling data, and destinations
- Export all modified session files

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-invoicing-and-billing-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-invoicing-and-billing-post-exploitation/README.md) (5 headings)

- Steal or sabotage a procurement portal connection
- Distort billing visibility or share cost data
- Exfiltrate invoice identity, amounts, and documents
- Change future invoice routing, tax inheritance, or account grouping
- Modify billing preferences, contracts, or credits

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-macie-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-macie-post-exploitation/README.md) (5 headings)

- \`macie2:CreateInvitations\` / \`AcceptInvitation\` / \`UpdateOrganizationConfiguration\` — Macie administrator takeover
- \`macie2:GetSensitiveDataOccurrences\` (+ \`UpdateRevealConfiguration\`) — retrieve the actual sensitive values
- \`macie2:PutClassificationExportConfiguration\` — redirect the sensitive-data discovery map to an attacker bucket
- \`macie2:CreateFindingsFilter\` (SUPPRESS) / \`UpdateMacieSession\` / \`UpdateClassificationJob\` — blind the detection
- Amazon Macie - Bypass \`Reveal Sample\` Integrity Check

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-security-agent-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-security-agent-post-exploitation/README.md) (5 headings)

- \`securityagent:StartPentestJob\` — run intrusive tests against configured targets
- \`securityagent:ListActorMessages\` — recover email MFA codes and verification links
- \`securityagent:GetArtifact\` / \`BatchGetFindings\` — recover assessment context and exploit material
- \`securityagent:StartCodeRemediation\` — trigger trusted remediation pull requests
- \`securityagent:UpdateFinding\` / \`BatchDeletePentests\` — hide or destroy assessment evidence

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-snowball-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-snowball-post-exploitation/README.md) (5 headings)

- \`snowball:GetJobManifest\` + \`GetJobUnlockCode\` — recover the two device-unlock credentials
- \`snowball:UpdateLongTermPricing\` — re-enable a prepaid contract renewal
- \`snowball:CancelJob\` — cancel a newly created device workflow
- \`snowball:CreateJob\` + \`iam:PassRole\` — create a physical S3 export through a privileged role
- \`snowball:UpdateJob\` — make an existing Snow role export additional S3 data to another address

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sso-and-identitystore-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sso-and-identitystore-post-exploitation/README.md) (5 headings)

- \`sso:DeletePermissionSet\`
- \`sso:DeleteAccountAssignment\`
- \`sso:PutPermissionsBoundaryToPermissionSet\` + \`sso:ProvisionPermissionSet\`
- \`sso:GetRoleCredentials\`
- \`sso-admin:CreateTrustedTokenIssuer\` (+ \`CreateApplication\` / \`PutApplicationGrant\`) — impersonate any user via a rogue trusted token issuer

## [src/pentesting-cloud/aws-security/aws-persistence/aws-eks-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-eks-persistence/README.md) (4 headings)

- \`aws-auth\` ConfigMap mapping (legacy, CloudTrail-invisible)
- Pod Identity association bound to a namespace the attacker can reach
- Attacker-controlled OIDC identity provider
- Access entry as a standing backdoor

## [src/pentesting-cloud/aws-security/aws-persistence/aws-redshift-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-redshift-persistence/README.md) (4 headings)

- \`redshift-serverless:UpdateNamespace\` - reset the Serverless database administrator
- \`redshift:ModifyCluster\` - reset the provisioned-cluster master password
- \`redshift-serverless:UpdateWorkgroup\` - open a network path to a planted credential
- \`redshift:AuthorizeEndpointAccess\` - retain a cross-account private route

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudwatch-omni-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-cloudwatch-omni-post-exploitation/README.md) (4 headings)

- \`cloudwatch:CreateOneTimeDeepLinkCode\` — mint an authenticated Omni browser session
- Query unified logs and traces through the default Dataset
- \`cloudwatch:UpdateIntegration\` — rebind an external integration
- \`cloudwatch:UpdateAlert\` — hijack a scheduled query and its notifications

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-datazone-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-datazone-post-exploitation/README.md) (4 headings)

- Extract published asset metadata with \`SearchListings\`
- Inventory project members and private catalog content
- Map subscription and fulfillment paths
- Poison a trusted asset and republish its listing

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-devops-agent-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-devops-agent-post-exploitation/README.md) (4 headings)

- Recon registered services and agent-space associations
- Poison or expand an existing service association
- Replace a private connection's trusted certificate chain
- Disable and re-enable the Operator App with an attacker IdP

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-emr-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-emr-post-exploitation/README.md) (4 headings)

- Keep a compromised cluster alive with termination controls
- Enumerate cluster configuration, instances, and bootstrap artifacts
- Weaken EMR Block Public Access with \`PutBlockPublicAccessConfiguration\`
- Destroy a cluster with \`SetTerminationProtection\` and \`TerminateJobFlows\`

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-fraud-detector-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-fraud-detector-post-exploitation/README.md) (4 headings)

- \`frauddetector:GetEvent\` - Read a known stored event
- \`frauddetector:SendEvent\` - Blindly replace a stored event
- \`frauddetector:UpdateEventLabel\` - Blind label poisoning
- Event and decision-data destruction

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-healthlake-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-healthlake-post-exploitation/README.md) (4 headings)

- Steal clinical data with reads, searches and history
- Export the entire datastore through a service role
- Import an S3 object through a HealthLake role
- Blindly poison or destroy FHIR records

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-managed-blockchain-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-managed-blockchain-post-exploitation/README.md) (4 headings)

- Recover an Accessor bearer token
- Manipulate consortium governance
- Disable Hyperledger Fabric operational logs
- Destroy owned members, nodes or invitations

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-partner-central-channel-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-partner-central-channel-post-exploitation/README.md) (4 headings)

- Map reseller, customer and billing-transfer topology
- Divert channel benefits to an attacker-controlled account
- Manipulate billing-transfer service periods through handshakes
- Tamper with or remove Channel relationships

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-payment-cryptography-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-payment-cryptography-post-exploitation/README.md) (4 headings)

- Export an exportable payment key
- Use victim keys as a payment-cryptography oracle
- Disable or schedule deletion of payment keys
- Redirect an application alias

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-security-lake-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-security-lake-post-exploitation/README.md) (4 headings)

- Read normalized telemetry directly from the lake bucket
- \`securitylake:CreateSubscriber\` / \`UpdateSubscriber\` — external cross-account access
- Remove or redirect a legitimate subscriber
- Disable collection, retention, or organization onboarding

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-workdocs-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-workdocs-post-exploitation/README.md) (4 headings)

- WorkDocs activity, metadata, and content-read chain
- \`workdocs:AddResourcePermissions\`
- \`workdocs:CreateUser\`
- \`workdocs:UpdateUser\`

## [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-managed-grafana-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-managed-grafana-privesc/README.md) (4 headings)

- \`grafana:CreateWorkspaceApiKey\` — arbitrary-role legacy API key
- \`CreateWorkspaceServiceAccountToken\` — existing or attacker-created service account
- \`grafana:UpdateWorkspaceAuthentication\` — attacker-controlled SAML IdP
- \`grafana:UpdatePermissions\` — IAM Identity Center administrator

## [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-workdocs-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-workdocs-privesc/README.md) (4 headings)

- \`workdocs:CreateUser\`
- WorkDocs activity, metadata, and content-read chain
- \`workdocs:AddResourcePermissions\`
- \`workdocs:UpdateUser\`

## [src/pentesting-cloud/aws-security/aws-persistence/aws-elastic-beanstalk-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-elastic-beanstalk-persistence/README.md) (3 headings)

- Backdoor an instance
- Backdoor in Version
- New backdoored version

## [src/pentesting-cloud/aws-security/aws-persistence/aws-security-hub-persistence/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-persistence/aws-security-hub-persistence/README.md) (3 headings)

- Automation rules as a self-healing suppressor
- Disabled controls / standards persist
- Persistent blindness at the routing/aggregation layer

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-appstream-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-appstream-post-exploitation/README.md) (3 headings)

- \`appstream:UpdateImagePermissions\` — share and clone a private golden image cross-account
- \`appstream:CreateExportImageTask\` + \`iam:PassRole\` — turn a private image into an EC2 AMI
- \`appstream:UpdateStack\` — re-enable client data-transfer channels

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-bedrock-data-access-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-bedrock-data-access-post-exploitation/README.md) (3 headings)

- AgentCore Identity — mint a workload token and recover stored API keys
- AgentCore Identity — recover stored OAuth access tokens
- Knowledge Bases — retrieve indexed private documents without source-storage access

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-connect-cases-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-connect-cases-post-exploitation/README.md) (3 headings)

- Bulk current and historical case-data collection
- Corrupt case workflow and evidence
- Disable or widen case event publishing

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-detective-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-detective-post-exploitation/README.md) (3 headings)

- Stopping optional data source packages (blind the graph)
- Detaching accounts from the behavior graph
- Destroying the investigation surface

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-direct-connect-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-direct-connect-post-exploitation/README.md) (3 headings)

- \`directconnect:DescribeVirtualInterfaces\` / \`DescribeRouterConfiguration\` — recover BGP authentication material
- \`directconnect:CreateDirectConnectGatewayAssociationProposal\` — propose an attacker DX gateway from the victim account
- \`directconnect:AssociateMacSecKey\` / \`UpdateConnection\` — weaken link-layer encryption

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-end-user-messaging-social-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-end-user-messaging-social-post-exploitation/README.md) (3 headings)

- \`social-messaging:GetWhatsAppMessageMedia\` - Copy inbound media to an attacker destination
- \`social-messaging:SendWhatsAppMessage\` - Send trusted-brand WhatsApp messages
- WABA template and Flow writes - Build durable phishing content

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-healthomics-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-healthomics-post-exploitation/README.md) (3 headings)

- Export private workflow source and run secrets
- Exfiltrate sequence and reference data
- Poison or destroy genomic and workflow state

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-post-exploitation/aws-lambda-efs-mount-injection.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-lambda-post-exploitation/aws-lambda-efs-mount-injection.md) (3 headings)

- Requirements
- Attack
- Impact

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-mainframe-modernization-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-mainframe-modernization-post-exploitation/README.md) (3 headings)

- \`m2:GetSignedBluinsightsUrl\` - Obtain a Blu Insights portal session
- \`m2:CreateDataSetExportTask\` - Export application data sets to S3
- \`m2:CreateDataSetImportTask\` - Poison migrated application data

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-neptune-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-neptune-post-exploitation/README.md) (3 headings)

- Query a Neptune database with only \`neptune-db:ReadDataViaQuery\`
- Recover the change log with only \`neptune-db:GetStreamRecords\`
- Query a Neptune Analytics graph with only \`neptune-graph:ReadDataViaQuery\`

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-network-security-manager-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-network-security-manager-post-exploitation/README.md) (3 headings)

- \`network-security-manager:UpdateRule\` — weaken centrally deployed WAF protections
- \`network-security-manager:DeleteDeployment\` — remove centralized enforcement
- \`network-security-manager:DeleteAdminAccount\` — disable one administrator's multi-account protections

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-partner-central-benefits-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-partner-central-benefits-post-exploitation/README.md) (3 headings)

- Recover AWS credit codes and other fulfillment data
- Recover benefit applications, contacts and supporting evidence
- Redirect or destroy a benefit application

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-pinpoint-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-pinpoint-post-exploitation/README.md) (3 headings)

- \`sms-voice:SendTextMessage\` / \`SendVoiceMessage\` — smishing / vishing from a trusted origination identity
- \`mobiletargeting:SendMessages\` / \`SendUsersMessages\` — direct multi-channel send
- \`mobiletargeting:CreateCampaign\` / \`CreateJourney\` — mass phishing to the victim's own audience

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-q-business-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-q-business-post-exploitation/README.md) (3 headings)

- Anonymous web-session issuance
- ACL reconnaissance and authorized document extraction
- Public-document and retrieval poisoning with \`BatchPutDocument\`

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-rtb-fabric-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-rtb-fabric-post-exploitation/README.md) (3 headings)

- \`rtbfabric:UpdateResponderGateway\` — replace a managed responder backend
- \`rtbfabric:CreateOutboundExternalLink\` — stage a public exfiltration destination
- \`rtbfabric:UpdateLinkModuleFlow\` — suppress, filter or alter bid traffic

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sagemaker-post-exploitation/feature-store-poisoning.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sagemaker-post-exploitation/feature-store-poisoning.md) (3 headings)

- Requirements
- Steps
- Data export

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-systems-manager-incident-manager-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-systems-manager-incident-manager-post-exploitation/README.md) (3 headings)

- Recon: read the responders' view of the incident
- Erase and rewrite the incident (timeline & record sabotage)
- Anti-forensics: destroy all Incident Manager data (\`DeleteReplicationSet\`)

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-wickr-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-wickr-post-exploitation/README.md) (3 headings)

- \`wickr:GetOidcInfo\` — disclose the SSO client secret
- \`wickr:GetOpentdfConfig\` — disclose the OpenTDF client secret
- \`wickr:ListUsers\` — recover an invited user's enrollment code

## [src/pentesting-cloud/aws-security/aws-post-exploitation/aws-workmail-post-exploitation/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-post-exploitation/aws-workmail-post-exploitation/README.md) (3 headings)

- Sending paths & telemetry gaps
- \`workmailmessageflow:GetRawMessageContent\` / \`PutRawMessageContent\` — steal or rewrite in-transit email
- Abusing WorkMail to bypass SES sandbox

## [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codestar-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codestar-privesc/README.md) (3 headings)

- \`iam:PassRole\`, \`codestar:CreateProject\`
- \`codestar:CreateProject\`, \`codestar:AssociateTeamMember\`
- \`codestar:CreateProjectFromTemplate\`

## [src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-pca-connector-ad-privesc/README.md](https://github.com/HackTricks-wiki/hacktricks-cloud/blob/47c375ae496ae89f81936f47ab1cb84885c88373/src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-pca-connector-ad-privesc/README.md) (3 headings)

- \`pca-connector-ad:CreateTemplate\` — publish a malicious certificate template (ESC1 / ESC9)
- \`pca-connector-ad:UpdateTemplate\` — weaken an existing legitimate template in place
- \`pca-connector-ad:CreateTemplateGroupAccessControlEntry\` — grant enrollment to an attacker-chosen AD group
