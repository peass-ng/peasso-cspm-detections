# HackTricks CSPM detections

This repository holds the reviewed Sigma rules used by Attack Analysis.
Rules live in `rules/*.yml`. The CSPM reads an exact commit SHA and rejects
unsupported grammar or malformed rules. A rule change takes effect only after
the reviewed SHA is updated in the CSPM release or its
`HACKTRICKS_CSPM_RULES_GITHUB_REF` override.

The CSPM reads this public repository without a token. The rule loader fails
closed if the pinned GitHub commit is unavailable and never falls back to an
older unreviewed rule set. Do not put credentials or customer audit data here.

The rules are deliberately narrow. A matched administrative action
requires investigation and does not by itself prove malicious intent.
The Azure Activity Log rule runs on a canonical event produced by joining
matching `Started` and `Succeeded` entries. The join is implemented in the
CSPM and is not a portable Sigma correlation rule; the Sigma selection
controls which successfully joined role grants become findings. Entra
directory audits have one narrow direct Global Administrator self-assignment
rule. Routine credential-add events are still excluded because the observed
volume cannot distinguish approved rotation from an attack by event name alone.

The current candidate pack contains 45 rules across AWS, GCP, Azure, and
Kubernetes. Four recent additions report three observed Secret Manager
operations and one successful Azure Key Vault diagnostic setting deletion.
The GCP operations were checked against disposable live Admin Activity records;
the Azure delete was checked against a disposable live Activity Log record.
These are review signals, not proof of an attack. Normalizers and correlation
logic live in the CSPM application; Sigma rules match their validated canonical
events. Coverage of all
HackTricks Cloud techniques and a measured false-positive rate are not yet
established.

The single-event alert for one IAM user creating another user's access key was
retired. In one bounded read-only CloudTrail sample it matched 32 of 50 recent
events, consistent with routine administration in that account. The event is
useful evidence, but cannot establish target privilege, unauthorized creation,
or later key use by itself. This sample is not a measured production false
positive rate; the rule remains in Git history for future correlated designs.
