#!/usr/bin/env python3
"""Build an action-name triage index from the direct-reference AWS queue.

This is a search aid, not a statement of missing attack coverage. CloudTrail
event names can differ from IAM action names, and a matching action name alone
does not establish that a rule detects a particular technique.
"""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import re

import yaml


ROOT = Path(__file__).resolve().parents[1]
PAGE = re.compile(r"^## \[([^]]+)\]", re.MULTILINE)
ACTION = re.compile(r"`([a-z0-9-]+):([A-Z][A-Za-z0-9]+)`")


def rule_event_names() -> set[str]:
    names: set[str] = set()
    for path in (ROOT / "rules/aws").rglob("*.yml"):
        rule = yaml.safe_load(path.read_text(encoding="utf-8"))
        selected = rule["detection"]["selection"].get("event.name")
        if isinstance(selected, str):
            names.add(selected)
        elif isinstance(selected, list):
            names.update(item for item in selected if isinstance(item, str))
    return names


def main() -> None:
    names = rule_event_names()
    review = (ROOT / "AWS_COVERAGE_REVIEW.md").read_text(encoding="utf-8")
    pages: dict[str, list[tuple[str, str]]] = defaultdict(list)
    page = ""
    total = matched = missing = manual = 0
    for line in review.replace("\\`", "`").splitlines():
        found = PAGE.match(line)
        if found:
            page = found.group(1)
            continue
        if not page or not line.startswith("- "):
            continue
        total += 1
        actions = ACTION.findall(line)
        if not actions:
            manual += 1
            continue
        for service, action in actions:
            if action in names:
                matched += 1
            else:
                missing += 1
                pages[page].append((f"{service}:{action}", line[2:]))
    lines = [
        "# AWS action-name review queue",
        "",
        "Generated from [AWS_COVERAGE_REVIEW.md](AWS_COVERAGE_REVIEW.md) and the current AWS YAML pack.",
        "This is a **search aid**, not a count of uncovered attacks: IAM action names can",
        "differ from CloudTrail event names, some actions emit no standalone event, and",
        "matching an event name does not prove that the rule detects the attack route.",
        "",
        f"- Direct-reference triage pages: {len(PAGE.findall(review))}",
        f"- Headings in those pages: {total}",
        f"- Action mentions lacking an exact `event.name` in the pack: {missing}",
        f"- Action mentions with an exact name in the pack: {matched}",
        f"- Headings needing manual review because no `service:Action` appears: {manual}",
        "",
        "For each candidate, inspect the source text, actual CloudTrail event shape,",
        "existing normalizers, service availability, and a disposable live test before",
        "calling the technique uncovered or publishing a rule.",
        "",
    ]
    for path in sorted(pages):
        lines.extend((f"## {path}", "", "| Action candidate | Source heading |", "|---|---|"))
        for action, heading in pages[path]:
            lines.append(f"| `{action}` | {heading.replace('|', '&#124;')} |")
        lines.append("")
    (ROOT / "AWS_ACTION_GAPS.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"pages={len(PAGE.findall(review))} headings={total} missing_action_mentions={missing} manual_headings={manual}")


if __name__ == "__main__":
    main()
