/**
 * table_filter.js — Client-side filter, search, and sort for the element index table.
 *
 * Reads state from URL query params on load; writes state back with history.replaceState.
 * All filtering is based on data-* attributes on <tr> elements emitted by build_viewer.py.
 *
 * URL params:
 *   q        - free-text search (symbol, name, atomic number)
 *   filters  - comma-separated active chip keys (us_critical, eu_crm, eu_strategic,
 *              doe_rank, tier_1…tier_4, cat_*, commercial_only, no_commercial, byproduct_only)
 *   enduse   - active end-use bucket slug
 *   country  - active producer country ISO-2
 *   sort     - column key + _asc or _desc (e.g. hhi_mining_desc)
 */

"use strict";

// ─── Constants ───────────────────────────────────────────────────────────────

const END_USE_BUCKETS = [
  { slug: "batteries",         label: "Batteries" },
  { slug: "magnets",           label: "Magnets" },
  { slug: "superalloys",       label: "Superalloys" },
  { slug: "semiconductors",    label: "Semiconductors" },
  { slug: "catalysts",         label: "Catalysts" },
  { slug: "fertilizers",       label: "Fertilizers" },
  { slug: "steel_and_alloys",  label: "Steel & alloys" },
  { slug: "cutting_tools",     label: "Cutting tools" },
  { slug: "glass_and_ceramics",label: "Glass & ceramics" },
  { slug: "pigments_and_coatings", label: "Pigments & coatings" },
  { slug: "nuclear",           label: "Nuclear" },
  { slug: "medical",           label: "Medical" },
  { slug: "lighting",          label: "Lighting" },
  { slug: "other",             label: "Other" },
];

const CATEGORY_LABELS = {
  actinide:              "Actinide",
  alkali_metal:          "Alkali metal",
  alkaline_earth_metal:  "Alkaline earth metal",
  lanthanide:            "Lanthanide",
  metalloid:             "Metalloid",
  noble_gas:             "Noble gas",
  nonmetal:              "Nonmetal",
  post_transition_metal: "Post-transition metal",
  synthetic_superheavy:  "Synthetic superheavy",
  transition_metal:      "Transition metal",
};

/** Numeric data-* keys (parsed with parseFloat; empty string = null, sorts last). */
const NUMERIC_SORT_KEYS = new Set([
  "atomicNumber",
  "tier",
  "topShare",
  "hhiMining",
  "doeRank",
]);

// ─── State ───────────────────────────────────────────────────────────────────

let activeFilters = new Set(); // chip filter keys
let activeEnduse  = null;      // end-use bucket slug | null
let activeCountry = null;      // ISO-2 | null
let sortKey       = null;      // column sort key | null
let sortDir       = null;      // 'asc' | 'desc' | null
let searchQuery   = "";

// ─── DOM handles ─────────────────────────────────────────────────────────────

let table, tbody, searchInput, clearAllBtn, enduseSelect, countrySelect,
    countryPageLink, byproductCta, tableControls;

// ─── Sort utility handle ──────────────────────────────────────────────────────

let tableSorter = null;

// ─── Init ─────────────────────────────────────────────────────────────────────

document.addEventListener("DOMContentLoaded", init);

function init() {
  table          = document.getElementById("element-table");
  tbody          = table ? table.querySelector("tbody") : null;
  searchInput    = document.getElementById("table-search");
  clearAllBtn    = document.getElementById("clear-all-btn");
  enduseSelect   = document.getElementById("enduse-select");
  countrySelect  = document.getElementById("country-select");
  countryPageLink= document.getElementById("country-page-link");
  byproductCta   = document.getElementById("byproduct-graph-cta");
  tableControls  = document.getElementById("table-controls");

  if (!table || !tbody) return; // not on the index page

  // Read feature flags from the controls container
  const countryPagesEnabled    = tableControls && tableControls.dataset.countryPagesEnabled === "true";
  const byproductGraphEnabled  = tableControls && tableControls.dataset.byproductGraphEnabled === "true";

  // Wire table_sort.js (loaded before us)
  if (typeof initTableSort === "function") {
    tableSorter = initTableSort(table, {
      numericKeys: ["atomic_number", "tier", "top_share", "hhi_mining", "doe_rank"],
      onChange: (key, dir) => {
        sortKey = key;
        sortDir = dir;
        updateEmptyState();
        pushUrlState();
      },
    });
  }

  // Populate selects from element index
  const elementIndex = loadElementIndex();
  buildSelectOptions(elementIndex);
  initDerivedColumns(elementIndex);

  parseUrlState();
  attachEventListeners(countryPagesEnabled, byproductGraphEnabled);
  applyState();
}

// ─── Element index ────────────────────────────────────────────────────────────

function loadElementIndex() {
  const script = document.getElementById("atlas-element-index");
  if (!script) return [];
  try { return JSON.parse(script.textContent); }
  catch { return []; }
}

// ─── Select population ───────────────────────────────────────────────────────

function buildSelectOptions(elementIndex) {
  // End-use select
  if (enduseSelect) {
    END_USE_BUCKETS.forEach(({ slug, label }) => {
      const opt = document.createElement("option");
      opt.value = slug;
      opt.textContent = label;
      enduseSelect.appendChild(opt);
    });
  }

  // Country select — derive from element index mining countries
  if (countrySelect && elementIndex.length) {
    const countrySet = new Set();
    elementIndex.forEach((el) => {
      (el.producer_countries_mining || []).forEach((c) => countrySet.add(c));
    });
    Array.from(countrySet).sort().forEach((iso) => {
      const opt = document.createElement("option");
      opt.value = iso;
      opt.textContent = iso;
      countrySelect.appendChild(opt);
    });
  }
}

// ─── Derived columns ─────────────────────────────────────────────────────────

function initDerivedColumns(elementIndex) {
  if (!elementIndex.length) return;

  const bySymbol = new Map(elementIndex.map((el) => [el.symbol, el]));

  // Insert two new <th> cells are already in the HTML (build_viewer.py emits them).
  // We populate the <td> cells for each data row.
  const rows = Array.from(tbody.querySelectorAll("tr:not(.table-empty-state)"));
  rows.forEach((tr) => {
    const sym = tr.dataset.symbol;
    const entry = bySymbol.get(sym) || {};

    // Top country <td>
    const topTd = document.createElement("td");
    const topCountry = entry.top_country_mining || null;
    const topShare   = entry.top_country_share_pct != null ? entry.top_country_share_pct : null;
    if (topCountry && topShare !== null) {
      topTd.textContent = `${topCountry} ${topShare.toFixed(0)}%`;
      topTd.title = `${topCountry}: ${topShare.toFixed(1)}% of global mining output`;
    } else {
      topTd.textContent = "\u2014";
      topTd.style.color = "var(--muted)";
    }
    tr.appendChild(topTd);

    // HHI <td>
    const hhiTd = document.createElement("td");
    const hhi = entry.hhi_mining != null ? entry.hhi_mining : null;
    if (hhi !== null) {
      hhiTd.textContent = hhi.toLocaleString();
      hhiTd.title = "Herfindahl-Hirschman Index (mining). Higher = more concentrated. Max 10,000 = single-country monopoly.";
    } else {
      hhiTd.textContent = "\u2014";
      hhiTd.style.color = "var(--muted)";
    }
    tr.appendChild(hhiTd);
  });
}

// ─── URL state ────────────────────────────────────────────────────────────────

function parseUrlState() {
  const params = new URLSearchParams(window.location.search);

  searchQuery = params.get("q") || "";
  activeEnduse  = params.get("enduse") || null;
  activeCountry = params.get("country") || null;

  const filtersParam = params.get("filters") || "";
  activeFilters = new Set(filtersParam ? filtersParam.split(",").filter(Boolean) : []);

  const sortParam = params.get("sort") || "";
  if (sortParam) {
    const asc  = sortParam.endsWith("_asc");
    const desc = sortParam.endsWith("_desc");
    if (asc || desc) {
      sortDir = asc ? "asc" : "desc";
      sortKey = sortParam.slice(0, asc ? -4 : -5);
    }
  }

  // Sync UI controls
  if (searchInput) searchInput.value = searchQuery;
  if (enduseSelect) enduseSelect.value = activeEnduse || "";
  if (countrySelect) countrySelect.value = activeCountry || "";
}

function pushUrlState() {
  const params = new URLSearchParams();
  if (searchQuery)   params.set("q", searchQuery);
  if (activeFilters.size) params.set("filters", Array.from(activeFilters).join(","));
  if (activeEnduse)  params.set("enduse", activeEnduse);
  if (activeCountry) params.set("country", activeCountry);
  if (sortKey && sortDir) params.set("sort", `${sortKey}_${sortDir}`);
  const qs = params.toString();
  history.replaceState(null, "", qs ? `?${qs}` : window.location.pathname);
}

// ─── Event listeners ──────────────────────────────────────────────────────────

let _searchTimer = null;

function attachEventListeners(countryPagesEnabled, byproductGraphEnabled) {
  // Chip clicks
  document.querySelectorAll(".filter-chip").forEach((btn) => {
    btn.addEventListener("click", () => {
      const key = btn.dataset.filterKey;
      const val = btn.dataset.filterVal; // may be undefined
      const token = val !== undefined ? `${key}_${val}` : key;

      if (activeFilters.has(token)) {
        activeFilters.delete(token);
      } else {
        // For exclusive groups (tier, cat) remove other members of the same key first?
        // Spec says single-select for tier? No — chips are independent toggles.
        activeFilters.add(token);
      }
      applyState();
    });
  });

  // Search box
  if (searchInput) {
    searchInput.addEventListener("input", () => {
      clearTimeout(_searchTimer);
      _searchTimer = setTimeout(() => {
        searchQuery = searchInput.value.trim();
        applyState();
      }, 150);
    });
    searchInput.addEventListener("keydown", (e) => {
      if (e.key === "Escape") {
        searchInput.value = "";
        searchQuery = "";
        applyState();
      }
    });
  }

  // End-use select
  if (enduseSelect) {
    enduseSelect.addEventListener("change", () => {
      activeEnduse = enduseSelect.value || null;
      applyState();
    });
  }

  // Country select
  if (countrySelect) {
    countrySelect.addEventListener("change", () => {
      activeCountry = countrySelect.value || null;
      updateCountryPageLink(countryPagesEnabled);
      applyState();
    });
  }

  // Clear all
  if (clearAllBtn) {
    clearAllBtn.addEventListener("click", () => {
      clearAll();
      applyState();
    });
  }

  // Empty-state inline clear button (delegated)
  if (tbody) {
    tbody.addEventListener("click", (e) => {
      if (e.target.classList.contains("clear-inline-btn")) {
        clearAll();
        applyState();
      }
    });
  }

  // Country page link update on initial load
  updateCountryPageLink(countryPagesEnabled);

  // Byproduct CTA visibility toggled in applyState
  void byproductGraphEnabled; // referenced later in applyState via closure in init
}

// ─── Core state application ───────────────────────────────────────────────────

function applyState() {
  // Re-read feature flags from DOM each call so tests can mutate them
  const countryPagesEnabled   = tableControls && tableControls.dataset.countryPagesEnabled === "true";
  const byproductGraphEnabled = tableControls && tableControls.dataset.byproductGraphEnabled === "true";

  filterRows();
  // Sort is managed by table_sort.js; we just re-apply the current sort state
  if (tableSorter && sortKey && sortDir) {
    // Table sorter already tracks its own state — only needs re-sort if filter changed row visibility
    tableSorter.applySort();
  }
  updateHeaderArrows();
  updateChipActiveClass();
  updateEmptyState();
  updateClearAllBtn();
  updateCountryPageLink(countryPagesEnabled);
  updateByproductCta(byproductGraphEnabled);
  pushUrlState();
}

function clearAll() {
  activeFilters.clear();
  activeEnduse  = null;
  activeCountry = null;
  searchQuery   = "";
  sortKey       = null;
  sortDir       = null;
  if (searchInput)   searchInput.value = "";
  if (enduseSelect)  enduseSelect.value = "";
  if (countrySelect) countrySelect.value = "";
}

// ─── Filtering ────────────────────────────────────────────────────────────────

function filterRows() {
  const q = searchQuery.toLowerCase();
  const rows = Array.from(tbody.querySelectorAll("tr:not(.table-empty-state)"));
  rows.forEach((tr) => {
    tr.hidden = !matchesAllFilters(tr, q);
  });
}

function matchesAllFilters(tr, q) {
  const ds = tr.dataset;

  // Free-text search
  if (q) {
    const haystack = `${ds.symbol} ${ds.name} ${ds.atomicNumber}`.toLowerCase();
    if (!haystack.includes(q)) return false;
  }

  // Criticality chips
  if (activeFilters.has("us_critical")  && ds.usCritical  !== "true") return false;
  if (activeFilters.has("eu_crm")       && ds.euCrm       !== "true") return false;
  if (activeFilters.has("eu_strategic") && ds.euStrategic !== "true") return false;
  if (activeFilters.has("doe_rank")     && (!ds.doeRank || ds.doeRank === "0")) return false;

  // Tier chips (OR within tier group if multiple selected, AND with other groups)
  const tierFilters = ["1","2","3","4"].filter((v) => activeFilters.has(`tier_${v}`));
  if (tierFilters.length && !tierFilters.includes(ds.tier)) return false;

  // Category chips (OR within category group)
  const catKeys = Array.from(activeFilters).filter((k) => k.startsWith("cat_"));
  if (catKeys.length) {
    const cats = catKeys.map((k) => k.slice(4));
    if (!cats.includes(ds.category)) return false;
  }

  // Commercial production
  if (activeFilters.has("commercial_only") && ds.commercial !== "true") return false;
  if (activeFilters.has("no_commercial")   && ds.commercial !== "false") return false;

  // Byproduct-only
  if (activeFilters.has("byproduct_only") && ds.byproduct !== "true") return false;

  // End-use bucket (single-select)
  if (activeEnduse) {
    const buckets = ds.endusesBuckets ? ds.endusesBuckets.split(" ") : [];
    if (!buckets.includes(activeEnduse)) return false;
  }

  // Producer country (single-select)
  if (activeCountry) {
    const countries = ds.producerCountries ? ds.producerCountries.split(" ") : [];
    if (!countries.includes(activeCountry)) return false;
  }

  return true;
}

// ─── UI update helpers ────────────────────────────────────────────────────────

function updateChipActiveClass() {
  document.querySelectorAll(".filter-chip").forEach((btn) => {
    const key = btn.dataset.filterKey;
    const val = btn.dataset.filterVal;
    const token = val !== undefined ? `${key}_${val}` : key;
    btn.classList.toggle("active", activeFilters.has(token));
    btn.setAttribute("aria-pressed", activeFilters.has(token) ? "true" : "false");
  });
}

function updateHeaderArrows() {
  if (!table) return;
  table.querySelectorAll("th[data-sort-key]").forEach((th) => {
    const key = th.dataset.sortKey;
    if (key === sortKey && sortDir) {
      th.setAttribute("aria-sort", sortDir === "asc" ? "ascending" : "descending");
    } else {
      th.setAttribute("aria-sort", "none");
    }
  });
}

function updateEmptyState() {
  const emptyRow = tbody && tbody.querySelector(".table-empty-state");
  if (!emptyRow) return;
  const visibleCount = Array.from(tbody.querySelectorAll("tr:not(.table-empty-state)")).filter((tr) => !tr.hidden).length;
  emptyRow.hidden = visibleCount > 0;
}

function updateClearAllBtn() {
  if (!clearAllBtn) return;
  const hasState = activeFilters.size > 0 || activeEnduse || activeCountry || searchQuery || (sortKey && sortDir);
  clearAllBtn.hidden = !hasState;
}

function updateCountryPageLink(countryPagesEnabled) {
  if (!countryPageLink) return;
  if (countryPagesEnabled && activeCountry) {
    countryPageLink.href = `countries/${activeCountry}.html`;
    countryPageLink.hidden = false;
  } else {
    countryPageLink.hidden = true;
  }
}

function updateByproductCta(byproductGraphEnabled) {
  if (!byproductCta) return;
  // Show only when byproduct_only is the sole active filter and graph is enabled
  const onlyByproduct = activeFilters.size === 1 && activeFilters.has("byproduct_only");
  byproductCta.hidden = !(byproductGraphEnabled && onlyByproduct && !activeEnduse && !activeCountry && !searchQuery);
}
