"""Validate every YAML in atlas/elements/ through the Pydantic schema.

Runnable snippet:
    cd inquiries/material-world/atlas
    uv run python scripts/validate.py
"""

from __future__ import annotations

import sys
from pathlib import Path

from pydantic import ValidationError
from rich.console import Console
from rich.table import Table

from atlas.models import Element, load_element

ROOT = Path(__file__).resolve().parents[1]
ELEMENTS_DIR = ROOT / "elements"


def main() -> int:
    console = Console()
    errors: list[tuple[Path, str]] = []
    loaded: list[Element] = []

    for path in sorted(ELEMENTS_DIR.glob("*.yaml")):
        try:
            loaded.append(load_element(path))
        except ValidationError as e:
            errors.append((path, str(e)))
        except Exception as e:
            errors.append((path, f"{type(e).__name__}: {e}"))

    table = Table(title="Atlas element validation")
    table.add_column("Z", justify="right")
    table.add_column("Symbol")
    table.add_column("Name")
    table.add_column("Tier", justify="right")
    table.add_column("Commercial", justify="center")
    table.add_column("Status")

    for el in sorted(loaded, key=lambda e: e.atomic_number):
        table.add_row(
            str(el.atomic_number),
            el.symbol,
            el.name,
            str(el.industrial_tier.value),
            "yes" if el.commercial_production else "no",
            "[green]ok[/green]",
        )

    console.print(table)
    console.print(f"\n[bold]{len(loaded)}[/bold] elements validated.")

    if errors:
        console.print(f"\n[red bold]{len(errors)} errors:[/red bold]")
        for path, msg in errors:
            console.rule(path.name)
            console.print(msg)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
