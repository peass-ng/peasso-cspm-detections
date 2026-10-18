# Peasso CSPM detections

This repository holds the reviewed Sigma rules used by Attack Analysis.
Rules live in `rules/<provider>/*.yml`; AWS rules are grouped further under `rules/aws/<service>/*.yml`. The CSPM reads an exact commit SHA and rejects
unsupported grammar or malformed rules. A rule change takes effect only after
the reviewed SHA is updated in the CSPM release or its
`HACKTRICKS_CSPM_RULES_GITHUB_REF` override.

The CSPM reads this public repository without a token. The rule loader fails
closed if the pinned GitHub commit is unavailable and never falls back to an
older unreviewed rule set. Do not put credentials or customer audit data here.
The GitHub repository is `peass-ng/peasso-cspm-detections`. The CSPM pin must
use this canonical name because the archive root follows the renamed repository.

The rules are deliberately narrow. A matched administrative action
requires investigation and does not by itself prove malicious intent.
The Azure Activity Log rule runs on a canonical event produced by joining
matching `Started` and `Succeeded` entries. The join is implemented in the
CSPM and is not a portable Sigma correlation rule; the Sigma selection
controls which successfully joined role grants become findings. Entra
directory audits have one narrow direct Global Administrator self-assignment
rule. Routine credential-add events are still excluded because the observed
volume cannot distinguish approved rotation from an attack by event name alone.

The local candidate pack contains 69 rules across AWS, GCP, Azure, and
Kubernetes. Recent additions report three observed Secret Manager
operations and one successful Azure Key Vault diagnostic setting deletion.
The GCP operations were checked against disposable live Admin Activity records;
the Azure delete was checked against a disposable live Activity Log record.
These are review signals, not proof of an attack. Normalizers and correlation
logic live in the CSPM application; Sigma rules match their validated canonical
events. Coverage of all
HackTricks Cloud techniques and a measured false-positive rate are not yet
established. The current public revision contains 69 rules. The CSPM release
must explicitly pin its commit and digest before using them.

The local AWS `UpdateAccessKey` rule reports an IAM user setting another
user's key to `Active`. A disposable IAM test produced a matching CloudTrail
event, while the corresponding `Inactive` event did not match. This does not
prove the key was inactive beforehand or that its activation was unauthorized.

The single-event alert for one IAM user creating another user's access key was
retired. In one bounded read-only CloudTrail sample it matched 32 of 50 recent
events, consistent with routine administration in that account. The event is
useful evidence, but cannot establish target privilege, unauthorized creation,
or later key use by itself. This sample is not a measured production false
positive rate; the rule remains in Git history for future correlated designs.

A separate rule observes an IAM user successfully removing its own permissions
boundary. A disposable IAM user produced the exact CloudTrail shape, and no
matching event appeared in a bounded pre-test history sample from that lab
account. The operation alone does not establish a net permission increase.
