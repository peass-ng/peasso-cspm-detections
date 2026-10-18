# HackTricks CSPM detections

This private repository holds the reviewed Sigma rules used by Attack Analysis.
Rules live in `rules/*.yml`. The CSPM reads an exact commit SHA and rejects
unsupported grammar or malformed rules. A rule change takes effect only after
the deployed `HACKTRICKS_CSPM_RULES_GITHUB_REF` is updated to the reviewed SHA.

The runtime credential needs **Contents: read** access to this repository only.
Store it in AWS Secrets Manager; do not put tokens in source code, image layers,
GitHub Actions logs, or connector records. Revoke a token before deleting the
corresponding secret. The rule loader fails closed if GitHub or the secret is
unavailable and never falls back to an older unreviewed rule set.

The initial five rules are deliberately narrow. A matched administrative action
requires investigation and does not by itself prove malicious intent.
