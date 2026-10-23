# AWS action-name review queue

Generated from [AWS_COVERAGE_REVIEW.md](AWS_COVERAGE_REVIEW.md) and the current AWS YAML pack.
This is a **search aid**, not a count of uncovered attacks: IAM action names can
differ from CloudTrail event names, some actions emit no standalone event, and
matching an event name does not prove that the rule detects the attack route.

- Direct-reference triage pages: 43
- Headings in those pages: 190
- Action mentions lacking an exact `event.name` in the pack: 92
- Action mentions with an exact name in the pack: 12
- Headings needing manual review because no `service:Action` appears: 102

For each candidate, inspect the source text, actual CloudTrail event shape,
existing normalizers, service availability, and a disposable live test before
calling the technique uncovered or publishing a rule.

## src/pentesting-cloud/aws-security/aws-post-exploitation/aws-direct-connect-post-exploitation/README.md

| Action candidate | Source heading |
|---|---|
| `directconnect:DescribeVirtualInterfaces` | `directconnect:DescribeVirtualInterfaces` / `DescribeRouterConfiguration` — recover BGP authentication material |
| `directconnect:CreateDirectConnectGatewayAssociationProposal` | `directconnect:CreateDirectConnectGatewayAssociationProposal` — propose an attacker DX gateway from the victim account |
| `directconnect:AssociateMacSecKey` | `directconnect:AssociateMacSecKey` / `UpdateConnection` — weaken link-layer encryption |

## src/pentesting-cloud/aws-security/aws-post-exploitation/aws-elemental-inference-post-exploitation/README.md

| Action candidate | Source heading |
|---|---|
| `elemental-inference:GetMetadata` | `elemental-inference:GetMetadata` — recover transcripts and inference results |
| `elemental-inference:ExportDictionaryEntries` | `elemental-inference:ExportDictionaryEntries` — steal the custom vocabulary |
| `elemental-inference:UpdateDictionary` | `elemental-inference:UpdateDictionary` — poison vocabulary without read access |
| `elemental-inference:PutMedia` | `elemental-inference:PutMedia` — inject attacker-controlled source segments |
| `elemental-inference:UpdateFeed` | `elemental-inference:UpdateFeed` — blindly replace output configuration |

## src/pentesting-cloud/aws-security/aws-post-exploitation/aws-end-user-messaging-social-post-exploitation/README.md

| Action candidate | Source heading |
|---|---|
| `social-messaging:GetWhatsAppMessageMedia` | `social-messaging:GetWhatsAppMessageMedia` - Copy inbound media to an attacker destination |
| `social-messaging:SendWhatsAppMessage` | `social-messaging:SendWhatsAppMessage` - Send trusted-brand WhatsApp messages |

## src/pentesting-cloud/aws-security/aws-post-exploitation/aws-firewall-manager-post-exploitation/README.md

| Action candidate | Source heading |
|---|---|
| `fms:PutNotificationChannel` | `fms:PutNotificationChannel`, `fms:DeleteNotificationChannel` |
| `fms:DeleteNotificationChannel` | `fms:PutNotificationChannel`, `fms:DeleteNotificationChannel` |
| `fms:BatchAssociateResource` | `fms:BatchAssociateResource`, `fms:BatchDisassociateResource`, `fms:PutResourceSet`, `fms:DeleteResourceSet` |
| `fms:BatchDisassociateResource` | `fms:BatchAssociateResource`, `fms:BatchDisassociateResource`, `fms:PutResourceSet`, `fms:DeleteResourceSet` |
| `fms:PutResourceSet` | `fms:BatchAssociateResource`, `fms:BatchDisassociateResource`, `fms:PutResourceSet`, `fms:DeleteResourceSet` |
| `fms:DeleteResourceSet` | `fms:BatchAssociateResource`, `fms:BatchDisassociateResource`, `fms:PutResourceSet`, `fms:DeleteResourceSet` |
| `fms:PutAppsList` | `fms:PutAppsList`, `fms:DeleteAppsList` |
| `fms:DeleteAppsList` | `fms:PutAppsList`, `fms:DeleteAppsList` |
| `fms:PutProtocolsList` | `fms:PutProtocolsList`, `fms:DeleteProtocolsList` |
| `fms:DeleteProtocolsList` | `fms:PutProtocolsList`, `fms:DeleteProtocolsList` |

## src/pentesting-cloud/aws-security/aws-post-exploitation/aws-macie-post-exploitation/README.md

| Action candidate | Source heading |
|---|---|
| `macie2:CreateInvitations` | `macie2:CreateInvitations` / `AcceptInvitation` / `UpdateOrganizationConfiguration` — Macie administrator takeover |
| `macie2:GetSensitiveDataOccurrences` | `macie2:GetSensitiveDataOccurrences` (+ `UpdateRevealConfiguration`) — retrieve the actual sensitive values |
| `macie2:PutClassificationExportConfiguration` | `macie2:PutClassificationExportConfiguration` — redirect the sensitive-data discovery map to an attacker bucket |
| `macie2:CreateFindingsFilter` | `macie2:CreateFindingsFilter` (SUPPRESS) / `UpdateMacieSession` / `UpdateClassificationJob` — blind the detection |

## src/pentesting-cloud/aws-security/aws-post-exploitation/aws-mainframe-modernization-post-exploitation/README.md

| Action candidate | Source heading |
|---|---|
| `m2:GetSignedBluinsightsUrl` | `m2:GetSignedBluinsightsUrl` - Obtain a Blu Insights portal session |
| `m2:CreateDataSetExportTask` | `m2:CreateDataSetExportTask` - Export application data sets to S3 |
| `m2:CreateDataSetImportTask` | `m2:CreateDataSetImportTask` - Poison migrated application data |

## src/pentesting-cloud/aws-security/aws-post-exploitation/aws-neptune-post-exploitation/README.md

| Action candidate | Source heading |
|---|---|
| `neptune-db:ReadDataViaQuery` | Query a Neptune database with only `neptune-db:ReadDataViaQuery` |
| `neptune-db:GetStreamRecords` | Recover the change log with only `neptune-db:GetStreamRecords` |
| `neptune-graph:ReadDataViaQuery` | Query a Neptune Analytics graph with only `neptune-graph:ReadDataViaQuery` |

## src/pentesting-cloud/aws-security/aws-post-exploitation/aws-network-security-manager-post-exploitation/README.md

| Action candidate | Source heading |
|---|---|
| `network-security-manager:UpdateRule` | `network-security-manager:UpdateRule` — weaken centrally deployed WAF protections |
| `network-security-manager:DeleteAdminAccount` | `network-security-manager:DeleteAdminAccount` — disable one administrator's multi-account protections |

## src/pentesting-cloud/aws-security/aws-post-exploitation/aws-pinpoint-post-exploitation/README.md

| Action candidate | Source heading |
|---|---|
| `sms-voice:SendTextMessage` | `sms-voice:SendTextMessage` / `SendVoiceMessage` — smishing / vishing from a trusted origination identity |
| `mobiletargeting:SendMessages` | `mobiletargeting:SendMessages` / `SendUsersMessages` — direct multi-channel send |
| `mobiletargeting:CreateCampaign` | `mobiletargeting:CreateCampaign` / `CreateJourney` — mass phishing to the victim's own audience |

## src/pentesting-cloud/aws-security/aws-post-exploitation/aws-rtb-fabric-post-exploitation/README.md

| Action candidate | Source heading |
|---|---|
| `rtbfabric:UpdateResponderGateway` | `rtbfabric:UpdateResponderGateway` — replace a managed responder backend |
| `rtbfabric:CreateOutboundExternalLink` | `rtbfabric:CreateOutboundExternalLink` — stage a public exfiltration destination |
| `rtbfabric:UpdateLinkModuleFlow` | `rtbfabric:UpdateLinkModuleFlow` — suppress, filter or alter bid traffic |

## src/pentesting-cloud/aws-security/aws-post-exploitation/aws-security-agent-post-exploitation/README.md

| Action candidate | Source heading |
|---|---|
| `securityagent:StartPentestJob` | `securityagent:StartPentestJob` — run intrusive tests against configured targets |
| `securityagent:ListActorMessages` | `securityagent:ListActorMessages` — recover email MFA codes and verification links |
| `securityagent:GetArtifact` | `securityagent:GetArtifact` / `BatchGetFindings` — recover assessment context and exploit material |
| `securityagent:StartCodeRemediation` | `securityagent:StartCodeRemediation` — trigger trusted remediation pull requests |
| `securityagent:UpdateFinding` | `securityagent:UpdateFinding` / `BatchDeletePentests` — hide or destroy assessment evidence |

## src/pentesting-cloud/aws-security/aws-post-exploitation/aws-security-lake-post-exploitation/README.md

| Action candidate | Source heading |
|---|---|
| `securitylake:CreateSubscriber` | `securitylake:CreateSubscriber` / `UpdateSubscriber` — external cross-account access |

## src/pentesting-cloud/aws-security/aws-post-exploitation/aws-snowball-post-exploitation/README.md

| Action candidate | Source heading |
|---|---|
| `snowball:GetJobManifest` | `snowball:GetJobManifest` + `GetJobUnlockCode` — recover the two device-unlock credentials |
| `snowball:UpdateLongTermPricing` | `snowball:UpdateLongTermPricing` — re-enable a prepaid contract renewal |
| `snowball:CancelJob` | `snowball:CancelJob` — cancel a newly created device workflow |
| `snowball:CreateJob` | `snowball:CreateJob` + `iam:PassRole` — create a physical S3 export through a privileged role |
| `iam:PassRole` | `snowball:CreateJob` + `iam:PassRole` — create a physical S3 export through a privileged role |

## src/pentesting-cloud/aws-security/aws-post-exploitation/aws-sso-and-identitystore-post-exploitation/README.md

| Action candidate | Source heading |
|---|---|
| `sso:DeletePermissionSet` | `sso:DeletePermissionSet` |
| `sso:DeleteAccountAssignment` | `sso:DeleteAccountAssignment` |
| `sso:PutPermissionsBoundaryToPermissionSet` | `sso:PutPermissionsBoundaryToPermissionSet` + `sso:ProvisionPermissionSet` |
| `sso:ProvisionPermissionSet` | `sso:PutPermissionsBoundaryToPermissionSet` + `sso:ProvisionPermissionSet` |
| `sso:GetRoleCredentials` | `sso:GetRoleCredentials` |
| `sso-admin:CreateTrustedTokenIssuer` | `sso-admin:CreateTrustedTokenIssuer` (+ `CreateApplication` / `PutApplicationGrant`) — impersonate any user via a rogue trusted token issuer |

## src/pentesting-cloud/aws-security/aws-post-exploitation/aws-timestream-post-exploitation/README.md

| Action candidate | Source heading |
|---|---|
| `timestream:Unload` | LiveAnalytics: export query results to S3 with `timestream:Unload` |
| `timestream:WriteRecords` | LiveAnalytics: invisible record injection, upsert and version pinning with `timestream:WriteRecords` |
| `iam:PassRole` | `timestream:CreateScheduledQuery` + `iam:PassRole` — run SQL and downstream writes as a scheduled-query role |
| `timestream:ExecuteScheduledQuery` | `timestream:ExecuteScheduledQuery` — trigger an already stored role workflow |

## src/pentesting-cloud/aws-security/aws-post-exploitation/aws-wickr-post-exploitation/README.md

| Action candidate | Source heading |
|---|---|
| `wickr:GetOidcInfo` | `wickr:GetOidcInfo` — disclose the SSO client secret |
| `wickr:GetOpentdfConfig` | `wickr:GetOpentdfConfig` — disclose the OpenTDF client secret |

## src/pentesting-cloud/aws-security/aws-post-exploitation/aws-workdocs-post-exploitation/README.md

| Action candidate | Source heading |
|---|---|
| `workdocs:AddResourcePermissions` | `workdocs:AddResourcePermissions` |

## src/pentesting-cloud/aws-security/aws-post-exploitation/aws-workmail-post-exploitation/README.md

| Action candidate | Source heading |
|---|---|
| `workmailmessageflow:GetRawMessageContent` | `workmailmessageflow:GetRawMessageContent` / `PutRawMessageContent` — steal or rewrite in-transit email |

## src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-codestar-privesc/README.md

| Action candidate | Source heading |
|---|---|
| `iam:PassRole` | `iam:PassRole`, `codestar:CreateProject` |
| `codestar:CreateProject` | `iam:PassRole`, `codestar:CreateProject` |
| `codestar:CreateProject` | `codestar:CreateProject`, `codestar:AssociateTeamMember` |
| `codestar:AssociateTeamMember` | `codestar:CreateProject`, `codestar:AssociateTeamMember` |
| `codestar:CreateProjectFromTemplate` | `codestar:CreateProjectFromTemplate` |

## src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-managed-grafana-privesc/README.md

| Action candidate | Source heading |
|---|---|
| `grafana:CreateWorkspaceApiKey` | `grafana:CreateWorkspaceApiKey` — arbitrary-role legacy API key |
| `grafana:UpdateWorkspaceAuthentication` | `grafana:UpdateWorkspaceAuthentication` — attacker-controlled SAML IdP |
| `grafana:UpdatePermissions` | `grafana:UpdatePermissions` — IAM Identity Center administrator |

## src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-pca-connector-ad-privesc/README.md

| Action candidate | Source heading |
|---|---|
| `pca-connector-ad:CreateTemplate` | `pca-connector-ad:CreateTemplate` — publish a malicious certificate template (ESC1 / ESC9) |
| `pca-connector-ad:UpdateTemplate` | `pca-connector-ad:UpdateTemplate` — weaken an existing legitimate template in place |
| `pca-connector-ad:CreateTemplateGroupAccessControlEntry` | `pca-connector-ad:CreateTemplateGroupAccessControlEntry` — grant enrollment to an attacker-chosen AD group |

## src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-sso-and-identitystore-privesc/README.md

| Action candidate | Source heading |
|---|---|
| `sso-directory:UpdatePassword` | `sso-directory:UpdatePassword` |
| `identitystore:CreateGroupMembership` | `identitystore:CreateGroupMembership` |
| `sso:PutInlinePolicyToPermissionSet` | `sso:PutInlinePolicyToPermissionSet`, `sso:ProvisionPermissionSet` |
| `sso:ProvisionPermissionSet` | `sso:PutInlinePolicyToPermissionSet`, `sso:ProvisionPermissionSet` |
| `sso:AttachManagedPolicyToPermissionSet` | `sso:AttachManagedPolicyToPermissionSet`, `sso:ProvisionPermissionSet` |
| `sso:ProvisionPermissionSet` | `sso:AttachManagedPolicyToPermissionSet`, `sso:ProvisionPermissionSet` |
| `sso:AttachCustomerManagedPolicyReferenceToPermissionSet` | `sso:AttachCustomerManagedPolicyReferenceToPermissionSet`, `sso:ProvisionPermissionSet` |
| `sso:ProvisionPermissionSet` | `sso:AttachCustomerManagedPolicyReferenceToPermissionSet`, `sso:ProvisionPermissionSet` |
| `sso:CreateAccountAssignment` | `sso:CreateAccountAssignment` |
| `sso:GetRoleCredentials` | `sso:GetRoleCredentials` |
| `sso:DetachManagedPolicyFromPermissionSet` | `sso:DetachManagedPolicyFromPermissionSet` |
| `sso:DetachCustomerManagedPolicyReferenceFromPermissionSet` | `sso:DetachCustomerManagedPolicyReferenceFromPermissionSet` |
| `sso:DeleteInlinePolicyFromPermissionSet` | `sso:DeleteInlinePolicyFromPermissionSet` |
| `sso:DeletePermissionsBoundaryFromPermissionSet` | `sso:DeletePermissionsBoundaryFromPermissionSet` |
| `sso:CreatePermissionSet` | `sso:CreatePermissionSet` (+ policy attach + `sso:CreateAccountAssignment`) — build an admin path from scratch |
| `sso:CreateAccountAssignment` | `sso:CreatePermissionSet` (+ policy attach + `sso:CreateAccountAssignment`) — build an admin path from scratch |
| `sso-admin:CreateTrustedTokenIssuer` | `sso-admin:CreateTrustedTokenIssuer` (+ `CreateApplication` / `PutApplicationGrant`) — impersonate any user via a rogue trusted token issuer |

## src/pentesting-cloud/aws-security/aws-privilege-escalation/aws-workdocs-privesc/README.md

| Action candidate | Source heading |
|---|---|
| `workdocs:AddResourcePermissions` | `workdocs:AddResourcePermissions` |
