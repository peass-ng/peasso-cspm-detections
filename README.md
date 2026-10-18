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

The current candidate pack contains 39 rules across AWS, GCP, Azure, and
Kubernetes. Five additions in this wave identify a role boundary deletion,
unconditional wildcard role trust, a Cloud Storage HMAC key creation, a
resource-group Owner self-assignment, and an accepted privileged Pod spec with
a writable host runtime socket. These are review signals, not proof of an
attack. Normalizers and correlation logic live in the CSPM application;
Sigma rules match their validated canonical events. Coverage of all
HackTricks Cloud techniques and a measured false-positive rate are not yet
established.
