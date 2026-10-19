#!/usr/bin/env python3
"""Report AWS HackTricks page and attack-heading changes since a pinned commit.

Example:
  python scripts/refresh_aws_source_delta.py --repo ../hacktricks-cloud \
    --baseline fd9bf8863bf7a36de10b8695d366a53a9063c81c --current origin/master
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import subprocess


AWS_ROOT = "src/pentesting-cloud/aws-security/"
HEADING = re.compile(r"^#{2,4} (.+?)\s*$", re.MULTILINE)


def git(repo: Path, *args: str) -> str:
    result = subprocess.run(["git", *args], cwd=repo, text=True, capture_output=True, check=True)
    return result.stdout


def page(repo: Path, revision: str, path: str) -> str:
    result = subprocess.run(["git", "show", f"{revision}:{path}"], cwd=repo,
                            text=True, capture_output=True)
    if result.returncode:
        return ""
    return result.stdout


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.home() / "git/hacktricks-cloud")
    parser.add_argument("--baseline", default="fd9bf8863bf7a36de10b8695d366a53a9063c81c")
    parser.add_argument("--current", default="origin/master")
    args = parser.parse_args()
    repo = args.repo.expanduser().resolve()
    baseline = git(repo, "rev-parse", "--verify", args.baseline).strip()
    current = git(repo, "rev-parse", "--verify", args.current).strip()
    changed = git(repo, "diff", "--name-status", baseline, current, "--", AWS_ROOT)
    rows = []
    for line in changed.splitlines():
        columns = line.split("\t")
        status, path = columns[0], columns[-1]
        if not path.endswith((".md", ".mdx")):
            continue
        before = page(repo, baseline, path)
        after = page(repo, current, path)
        old_headings = set(HEADING.findall(before))
        new_headings = set(HEADING.findall(after))
        rows.append({"status": status, "path": path,
                     "added_headings": sorted(new_headings - old_headings),
                     "removed_headings": sorted(old_headings - new_headings)})
    print(json.dumps({"baseline": baseline, "current": current,
                      "changed_pages": len(rows),
                      "pages_with_heading_changes": sum(bool(x["added_headings"] or x["removed_headings"])
                                                      for x in rows),
                      "changes": rows}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
