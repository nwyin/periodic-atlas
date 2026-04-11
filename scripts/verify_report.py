"""Aggregate per-element verification reports into build/verification_summary.json.

Each verification/{symbol}.md report cross-checks numeric claims in elements/{symbol}.yaml
against the source URLs they cite.

Runnable:
    uv run python scripts/verify_report.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from rich.console import Console
from rich.table import Table

ROOT = Path(__file__).resolve().parents[1]
VERIFICATION_DIR = ROOT / "verification"
BUILD_DIR = ROOT / "build"

ALLOWED_STATUSES: frozenset[str] = frozenset({"verified", "discrepancy", "inferred", "source_unreachable"})
SKIP_FILES: frozenset[str] = frozenset({"_template.md", "README.md"})
STATUS_KEYS: list[str] = ["verified", "discrepancy", "inferred", "source_unreachable"]
ZERO_COUNTS: dict[str, int] = {k: 0 for k in STATUS_KEYS}


class ParseError(Exception):
    """Raised when a verification report cannot be parsed."""

    def __init__(self, path: Path, message: str) -> None:
        self.path = path
        self.message = message
        super().__init__(f"{path}: {message}")


def _extract_section(text: str, heading: str) -> str | None:
    """Return the text block under `## {heading}`, up to the next ## heading."""
    pattern = rf"^##\s+{re.escape(heading)}\s*$"
    lines = text.splitlines()
    start: int | None = None
    for i, line in enumerate(lines):
        if re.match(pattern, line.rstrip(), re.IGNORECASE):
            start = i + 1
            break
    if start is None:
        return None
    section_lines: list[str] = []
    for line in lines[start:]:
        if re.match(r"^##\s+", line):
            break
        section_lines.append(line)
    return "\n".join(section_lines)


def _parse_md_table(text: str) -> list[list[str]] | None:
    """Parse a markdown table, returning data rows (post-separator) as lists of cell strings.

    Returns None if no valid table structure (header + separator) is found.
    """
    table_lines = [line.strip() for line in text.splitlines() if line.strip().startswith("|")]
    if len(table_lines) < 2:
        return None

    # Locate the separator row (cells made up of dashes/colons/spaces)
    sep_idx: int | None = None
    for i, line in enumerate(table_lines):
        cells = [c.strip() for c in line.strip("|").split("|")]
        if cells and all(re.match(r"^[-: ]+$", c) for c in cells):
            sep_idx = i
            break

    if sep_idx is None:
        return None

    data_rows: list[list[str]] = []
    for line in table_lines[sep_idx + 1 :]:
        cells = [c.strip() for c in line.strip("|").split("|")]
        data_rows.append(cells)
    return data_rows


def _parse_snapshot_year(text: str) -> int | None:
    """Parse `- Snapshot year: {year}` from report header metadata."""
    m = re.search(r"-\s+Snapshot year:\s*(\d{4})", text)
    return int(m.group(1)) if m else None


def parse_summary_table(path: Path, text: str) -> dict[str, int]:
    """Parse the ## Summary table from a report.

    Returns a dict of status → count for the four allowed statuses.
    Raises ParseError if the section is missing or the table is malformed.
    """
    section = _extract_section(text, "Summary")
    if section is None:
        raise ParseError(path, "missing ## Summary section")

    rows = _parse_md_table(section)
    if rows is None:
        raise ParseError(path, f"malformed Summary table in {path}: no separator row found")

    counts = dict(ZERO_COUNTS)
    for row in rows:
        if len(row) < 2:
            continue
        metric, count_str = row[0].strip(), row[1].strip()
        if metric not in counts:
            continue
        try:
            counts[metric] = int(count_str)
        except ValueError:
            raise ParseError(path, f"non-integer count for metric {metric!r}: {count_str!r}")
    return counts


def parse_claims_table(path: Path, text: str) -> list[dict[str, str]]:
    """Parse the ## Claims table from a report.

    Raises ValueError if any row has a status outside the allowed vocabulary.
    Returns an empty list if the Claims section or its table is absent.
    """
    section = _extract_section(text, "Claims")
    if section is None:
        return []

    rows = _parse_md_table(section)
    if rows is None:
        return []

    claims: list[dict[str, str]] = []
    # Column order: Claim location | Value in YAML | Source id | Status | Evidence
    for row in rows:
        if len(row) < 4:
            continue
        status = row[3].strip()
        if status not in ALLOWED_STATUSES:
            raise ValueError(f"{path}: unknown claim status {status!r} — allowed values are {sorted(ALLOWED_STATUSES)}")
        claims.append(
            {
                "claim_location": row[0],
                "value_in_yaml": row[1],
                "source_id": row[2],
                "status": status,
                "evidence": row[4] if len(row) > 4 else "",
            }
        )
    return claims


def parse_report(path: Path) -> tuple[str, dict[str, int], int | None]:
    """Parse a verification report file.

    Returns (symbol, counts, snapshot_year).
    Raises:
        ParseError  — missing or malformed Summary table
        ValueError  — claim row with unrecognised status
    """
    text = path.read_text(encoding="utf-8")
    symbol = path.stem
    counts = parse_summary_table(path, text)
    parse_claims_table(path, text)  # validate; raises ValueError on bad status
    snapshot_year = _parse_snapshot_year(text)
    return symbol, counts, snapshot_year


def aggregate_reports(verification_dir: Path) -> tuple[dict, list[str]]:
    """Aggregate all {symbol}.md reports in verification_dir.

    Returns (summary_dict, list_of_error_messages).
    Parse errors and validation errors are collected; the run never crashes.
    Output is deterministic: elements are sorted by symbol.
    """
    elements: dict[str, dict[str, int]] = {}
    errors: list[str] = []
    snapshot_year: int | None = None

    paths = sorted(verification_dir.glob("*.md"))
    for path in paths:
        if path.name in SKIP_FILES:
            continue
        try:
            symbol, counts, sy = parse_report(path)
            elements[symbol] = counts
            if snapshot_year is None and sy is not None:
                snapshot_year = sy
        except (ParseError, ValueError) as exc:
            errors.append(str(exc))

    totals: dict[str, int] = {k: sum(el.get(k, 0) for el in elements.values()) for k in STATUS_KEYS}

    summary: dict = {
        "snapshot_year": snapshot_year,
        "elements": dict(sorted(elements.items())),
        "totals": totals,
    }
    return summary, errors


def main() -> int:
    console = Console()

    summary, errors = aggregate_reports(VERIFICATION_DIR)

    if errors:
        console.print(f"[bold red]{len(errors)} parse error(s):[/bold red]")
        for err in errors:
            console.print(f"  [red]{err}[/red]")

    table = Table(title="Verification summary")
    table.add_column("Symbol", style="cyan")
    for key in STATUS_KEYS:
        justify = "right"
        style = "green" if key == "verified" else ("red" if key == "discrepancy" else "yellow")
        table.add_column(key, justify=justify, style=style)

    for symbol, counts in sorted(summary["elements"].items()):
        table.add_row(symbol, *[str(counts.get(k, 0)) for k in STATUS_KEYS])

    totals = summary["totals"]
    table.add_section()
    table.add_row("TOTAL", *[str(totals.get(k, 0)) for k in STATUS_KEYS])

    console.print(table)
    console.print(f"Snapshot year: {summary['snapshot_year']}")

    BUILD_DIR.mkdir(exist_ok=True)
    out_path = BUILD_DIR / "verification_summary.json"
    out_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    console.print(f"Wrote {out_path}")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
