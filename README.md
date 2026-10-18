# HackTricks CSPM detections

This repository holds the reviewed Sigma rules used by Attack Analysis.
Rules live in `rules/*.yml`. The CSPM reads an exact commit SHA and rejects
unsupported grammar or malformed rules. A rule change takes effect only after
the deployed `HACKTRICKS_CSPM_RULES_GITHUB_REF` is updated to the reviewed SHA.

The CSPM reads this public repository without a token. The rule loader fails
closed if the pinned GitHub commit is unavailable and never falls back to an
older unreviewed rule set. Do not put credentials or customer audit data here.

The initial five rules are deliberately narrow. A matched administrative action
requires investigation and does not by itself prove malicious intent.
