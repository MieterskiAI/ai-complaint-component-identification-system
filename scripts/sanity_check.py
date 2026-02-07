#!/usr/bin/env python3
"""Minimal sanity checks for docs/examples."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    sys.exit(1)


def require_file(path: Path) -> None:
    if not path.exists():
        fail(f"Required file missing: {path.relative_to(ROOT)}")


def require_markdown_sections(path: Path, sections: list[str]) -> None:
    content = path.read_text(encoding="utf-8")
    for section in sections:
        if section not in content:
            fail(
                f"Missing section '{section}' in {path.relative_to(ROOT)}"
            )


def check_complaint_input(path: Path) -> None:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")

    if "schema" not in payload or "examples" not in payload:
        fail("complaint_input.json must include 'schema' and 'examples'")

    examples = payload.get("examples")
    if not isinstance(examples, list) or not examples:
        fail("complaint_input.json must include at least one example")



def main() -> None:
    complaint_input = ROOT / "examples" / "complaint_input.json"
    analysis_output = ROOT / "examples" / "analysis_output.md"
    operator_checklist = ROOT / "examples" / "operator_checklist.md"

    require_file(complaint_input)
    require_file(analysis_output)
    require_file(operator_checklist)

    check_complaint_input(complaint_input)

    require_markdown_sections(
        analysis_output,
        [
            "# Example Analysis Output (synthetic)",
            "## Case:",
            "**Eliminated**",
            "**Top candidates**",
            "**Reasoning**",
        ],
    )

    require_markdown_sections(
        operator_checklist,
        [
            "## Data integrity",
            "## Symptom validation",
            "## Compatibility verification",
            "## Risk & escalation",
            "## Decision logging",
        ],
    )

    print("Sanity checks passed.")


if __name__ == "__main__":
    main()
