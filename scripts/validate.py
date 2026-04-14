"""Validate every YAML in atlas/elements/ through the Pydantic schema.

Also reports missing / extra element files vs. the canonical 118-element list,
and flags `byproduct_of` references pointing to elements that are not present
(relevant to the byproduct dependency graph).

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

# Canonical list of the 118 IUPAC-recognized elements, in atomic-number order.
# Source: IUPAC periodic table (Og — oganesson — is the heaviest named element as of 2025).
CANONICAL_SYMBOLS: tuple[str, ...] = (
    "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
    "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca",
    "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
    "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr",
    "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",
    "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd",
    "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
    "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
    "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th",
    "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm",
    "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds",
    "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og",
)

# Symbols intentionally out of scope for the atlas. These are skipped in the
# "missing elements" warning. Add a new entry only after deliberate review — the
# default stance is "every element deserves a row, even synthetics with no
# commercial supply chain" (see existing Og.yaml, Ds.yaml, etc.).
OUT_OF_SCOPE_SYMBOLS: frozenset[str] = frozenset({
    # Synthetic actinides with no documented commercial supply chain. Their
    # characterization is confined to research reactor stock and university
    # cyclotrons; no public production/consumption numbers exist to cite.
    "Es", "Fm", "Md", "No", "Lr",
})


def _check_missing_elements(present_symbols: set[str]) -> list[str]:
    """Return list of canonical symbols that lack a YAML and are not opted out."""
    missing: list[str] = []
    for sym in CANONICAL_SYMBOLS:
        if sym in present_symbols:
            continue
        if sym in OUT_OF_SCOPE_SYMBOLS:
            continue
        missing.append(sym)
    return missing


def _check_unexpected_elements(present_symbols: set[str]) -> list[str]:
    """Return YAML filenames whose symbol is not in the canonical 118-element list."""
    canonical = set(CANONICAL_SYMBOLS)
    return sorted(sym for sym in present_symbols if sym not in canonical)


def _check_byproduct_refs(loaded: list[Element]) -> list[tuple[str, str]]:
    """Return (element_symbol, dangling_byproduct_ref) pairs for broken `byproduct_of` links."""
    known = {el.symbol for el in loaded}
    dangling: list[tuple[str, str]] = []
    for el in loaded:
        for ref in el.byproduct_of or []:
            if ref not in known:
                dangling.append((el.symbol, ref))
    return dangling


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

    # ── Coverage checks against the canonical 118-element list ─────────────
    present_symbols = {el.symbol for el in loaded}
    missing = _check_missing_elements(present_symbols)
    unexpected = _check_unexpected_elements(present_symbols)
    dangling = _check_byproduct_refs(loaded)

    warnings_emitted = False

    if missing:
        warnings_emitted = True
        missing_table = Table(title="Missing elements (not opted out)", show_lines=False)
        missing_table.add_column("Symbol")
        missing_table.add_column("Atomic #", justify="right")
        for sym in missing:
            z = CANONICAL_SYMBOLS.index(sym) + 1
            missing_table.add_row(sym, str(z))
        console.print()
        console.print(missing_table)
        console.print(
            f"[yellow]{len(missing)} element(s) missing a YAML. "
            "Add the file, or add the symbol to OUT_OF_SCOPE_SYMBOLS with a justification comment.[/yellow]"
        )

    if unexpected:
        warnings_emitted = True
        console.print(
            f"\n[yellow]Unexpected element symbol(s) not in canonical 118: "
            f"{', '.join(unexpected)}. "
            "Check for typos or update CANONICAL_SYMBOLS.[/yellow]"
        )

    if dangling:
        warnings_emitted = True
        dangling_table = Table(title="Dangling byproduct_of references", show_lines=False)
        dangling_table.add_column("Element")
        dangling_table.add_column("Points to (missing)")
        for sym, ref in dangling:
            dangling_table.add_row(sym, ref)
        console.print()
        console.print(dangling_table)
        console.print(
            "[yellow]The element on the left lists a byproduct_of target that has no YAML in the atlas. "
            "Either add the target element or remove the reference.[/yellow]"
        )

    if not warnings_emitted and not errors:
        console.print("[green]✓ Coverage checks passed — no missing, unexpected, or dangling elements.[/green]")

    if errors:
        console.print(f"\n[red bold]{len(errors)} errors:[/red bold]")
        for path, msg in errors:
            console.rule(path.name)
            console.print(msg)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
