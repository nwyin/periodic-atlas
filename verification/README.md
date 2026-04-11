# Verification Reports

Per-element verification reports cross-check numeric claims in `elements/{symbol}.yaml`
against the `Source.url` they cite. Each report is a structured Markdown file produced
by a verification agent (human or automated) who reads the cited source and confirms
whether the value in the YAML matches what the source actually says.

## Purpose

- Catch stale numbers (sources updated after the YAML was written)
- Catch transcription errors (value copied incorrectly from source)
- Surface claims that could not be verified (paywalled sources, dead URLs)
- Flag values that were inferred rather than directly cited

## Structure

Each file is named `{symbol}.md` (e.g., `Co.md`, `Nd.md`) and follows `_template.md`.

## Status vocabulary

| Status | Meaning |
|---|---|
| `verified` | Value in YAML matches the cited source exactly |
| `discrepancy` | Value in YAML differs from what the source says |
| `inferred` | No direct citation found; value was inferred or estimated |
| `source_unreachable` | URL is dead, paywalled, or otherwise inaccessible |

## Aggregation

Run `uv run python scripts/verify_report.py` from the project root to aggregate all
reports into `build/verification_summary.json` and print a summary table.
