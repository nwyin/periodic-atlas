/**
 * table_sort.js — Generic click-to-sort utility for HTML tables.
 *
 * Usage:
 *   initTableSort(tableEl, { numericKeys: ['atomic_number', 'tier', ...] });
 *
 * Wires every <th data-sort-key="..."> in <thead> to sort the <tbody> rows on
 * click. Cycles: none → ascending → descending → none (restores original order).
 *
 * The sort key is taken from the <tr> dataset attribute matching the key
 * (e.g. data-sort-key="tier" reads row.dataset.tier). Numeric comparisons are
 * used for keys listed in numericKeys; all others compare text content.
 *
 * External callers (table_filter.js) may override the sort function by passing
 * a sortFn option, or hook into onChange to be notified after each sort.
 */

"use strict";

/**
 * @param {HTMLTableElement} table
 * @param {object} [opts]
 * @param {string[]} [opts.numericKeys]  - data-* keys compared numerically (nulls last).
 * @param {function} [opts.onChange]     - called after each sort with (key, dir).
 * @returns {{ getSortState: () => {key: string|null, dir: string|null} }}
 */
function initTableSort(table, opts) {
  opts = opts || {};
  const numericKeys = new Set(opts.numericKeys || []);
  const onChange = opts.onChange || null;

  const thead = table.querySelector("thead");
  const tbody = table.querySelector("tbody");
  if (!thead || !tbody) return { getSortState: () => ({ key: null, dir: null }) };

  /** Original DOM order preserved by index — used to restore "none" sort. */
  const originalOrder = Array.from(tbody.querySelectorAll("tr:not(.table-empty-state)")).map(
    (tr, i) => ({ tr, i })
  );

  let sortKey = null;
  let sortDir = null; // 'asc' | 'desc' | null

  const headers = Array.from(thead.querySelectorAll("th[data-sort-key]"));

  headers.forEach((th) => {
    th.setAttribute("role", "columnheader");
    if (!th.hasAttribute("aria-sort")) th.setAttribute("aria-sort", "none");

    const handler = () => {
      const key = th.dataset.sortKey;
      if (sortKey === key) {
        // Cycle: asc → desc → none
        if (sortDir === "asc") sortDir = "desc";
        else if (sortDir === "desc") { sortDir = null; sortKey = null; }
        else { sortDir = "asc"; sortKey = key; }
      } else {
        sortKey = key;
        sortDir = "asc";
      }
      applySort();
      if (onChange) onChange(sortKey, sortDir);
    };

    th.addEventListener("click", handler);
    th.addEventListener("keydown", (e) => {
      if (e.key === "Enter" || e.key === " ") { e.preventDefault(); handler(); }
    });
  });

  function applySort() {
    // Update aria-sort on all headers
    headers.forEach((th) => {
      if (th.dataset.sortKey === sortKey && sortDir) {
        th.setAttribute("aria-sort", sortDir === "asc" ? "ascending" : "descending");
      } else {
        th.setAttribute("aria-sort", "none");
      }
    });

    const dataRows = Array.from(tbody.querySelectorAll("tr:not(.table-empty-state)"));

    if (!sortKey || !sortDir) {
      // Restore original order
      const byIndex = new Map(originalOrder.map(({ tr, i }) => [tr, i]));
      dataRows.sort((a, b) => (byIndex.get(a) ?? 0) - (byIndex.get(b) ?? 0));
    } else {
      const numeric = numericKeys.has(sortKey);
      dataRows.sort((a, b) => {
        let av = a.dataset[toCamel(sortKey)];
        let bv = b.dataset[toCamel(sortKey)];

        if (numeric) {
          // Nulls (empty string) always sort last regardless of direction
          const an = av === "" || av === undefined ? null : parseFloat(av);
          const bn = bv === "" || bv === undefined ? null : parseFloat(bv);
          if (an === null && bn === null) return 0;
          if (an === null) return 1;
          if (bn === null) return -1;
          return sortDir === "asc" ? an - bn : bn - an;
        } else {
          av = av || "";
          bv = bv || "";
          const cmp = av.localeCompare(bv, undefined, { sensitivity: "base" });
          return sortDir === "asc" ? cmp : -cmp;
        }
      });
    }

    // Re-append in sorted order (empty-state row stays last — it's excluded)
    dataRows.forEach((tr) => tbody.appendChild(tr));
  }

  /** Convert kebab-case or snake_case sort key to camelCase dataset property. */
  function toCamel(key) {
    return key.replace(/[-_]([a-z])/g, (_, c) => c.toUpperCase());
  }

  return {
    getSortState: () => ({ key: sortKey, dir: sortDir }),
    applySort,
  };
}
