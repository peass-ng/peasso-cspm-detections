# Peasso CSPM detections

This repository holds the reviewed Sigma rules used by Attack Analysis.
Rules live in `rules/<provider>/*.yml`; AWS rules are grouped further under `rules/aws/<service>/*.yml`. The CSPM rejects unsupported grammar or malformed rules. Attack Analysis can use its reviewed pinned catalog or fetch the latest `main` catalog from this repository. The latest option resolves `main` to an immutable commit and verifies the archive before analysis. The `HACKTRICKS_CSPM_RULES_GITHUB_REF` override can select a specific commit for a deployment.

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

Normalizers and correlation logic live in the CSPM application; Sigma rules match their validated canonical events. Simple resource-scoped CloudTrail event rules can use the CSPM's opt-in declarative raw mode and ship through this catalog alone. Rules requiring new provider collection, request parsing, or correlation still need application support. Coverage of all HackTricks Cloud techniques and a measured false-positive rate are not yet established. The pinned catalog must specify its commit and digest; the latest option resolves and verifies both at run time.

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
