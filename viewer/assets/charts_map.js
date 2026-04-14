// viewer/assets/charts_map.js
// Render the neutral country hover map on viewer/index.html.
// Adds choropleth heatmap mode: pick an element + stage, color by share_pct (log scale).

(function () {
  const root = document.getElementById("country-map-root");
  const tooltip = document.getElementById("country-map-tooltip");
  const dataScript = document.getElementById("atlas-country-map-data");
  const drawer = document.getElementById("country-map-drawer");
  const drawerBackdrop = document.getElementById("country-map-drawer-backdrop");
  const drawerTitle = document.getElementById("country-map-drawer-title");
  const drawerSubtitle = document.getElementById("country-map-drawer-subtitle");
  const drawerBody = document.getElementById("country-map-drawer-body");
  const drawerClose = document.getElementById("country-map-drawer-close");

  if (!root || !tooltip || !dataScript || !drawer || !drawerBackdrop || !drawerTitle || !drawerSubtitle || !drawerBody || !drawerClose || !window.d3) {
    return;
  }

  let payload;
  try {
    payload = JSON.parse(dataScript.textContent || "{}");
  } catch (error) {
    root.innerHTML = '<div class="country-map-fallback">Country map data could not be parsed.</div>';
    return;
  }

  const countries = payload.countries || {};
  const geojsonSrc = root.dataset.geojsonSrc || "assets/world_countries_50m.geojson";
  const width = 960;
  const height = 540;
  const padding = 16;
  let hoveredNode = null;
  let hoveredCode = "";
  let pinnedNode = null;
  let pinnedCode = "";

  // ── Heatmap state ─────────────────────────────────────────────────────────
  let activeSymbol = null;   // null = neutral mode
  let activeStage = "mining";
  // heatmapIndex: symbol -> stage -> { [isoCode]: { share_pct, quantity_value, quantity_unit } }
  let heatmapIndex = {};

  // ── Element metadata index ─────────────────────────────────────────────────
  const elementIndexScript = document.getElementById("atlas-element-index");
  const elementIndex = elementIndexScript ? JSON.parse(elementIndexScript.textContent || "[]") : [];

  // ── Build inverse heatmap index from payload ───────────────────────────────
  function buildHeatmapIndex(countriesData, reservesData) {
    const idx = {};
    // Mining + refining from the existing countries payload
    for (const [iso, rows] of Object.entries(countriesData)) {
      for (const row of rows) {
        const sym = row.symbol;
        const stage = row.stage; // "mining" or "refining"
        if (!idx[sym]) idx[sym] = {};
        if (!idx[sym][stage]) idx[sym][stage] = {};
        // Take the highest share row per country+symbol+stage (sorted desc by build step)
        if (!idx[sym][stage][iso]) {
          idx[sym][stage][iso] = {
            share_pct: row.global_pct,
            quantity_value: row.quantity_value,
            quantity_unit: row.quantity_unit,
          };
        }
      }
    }
    // Reserves from the augmented payload
    for (const [iso, rows] of Object.entries(reservesData)) {
      for (const row of rows) {
        const sym = row.symbol;
        if (!idx[sym]) idx[sym] = {};
        if (!idx[sym]["reserves"]) idx[sym]["reserves"] = {};
        if (!idx[sym]["reserves"][iso]) {
          idx[sym]["reserves"][iso] = {
            share_pct: row.share_pct,
            quantity_value: row.quantity_value,
            quantity_unit: row.quantity_unit,
          };
        }
      }
    }
    return idx;
  }

  // ── Log color scale (d3.interpolateYlOrRd, domain [0.1, 100]) ─────────────
  const LOG_MIN = Math.log10(0.1);
  const LOG_MAX = Math.log10(100);
  const colorInterp = window.d3.interpolateYlOrRd;
  const neutralFill = "var(--map-land)";
  const noDataFill = "var(--map-no-data)";

  function heatFill(sharePct) {
    if (sharePct == null || sharePct <= 0) return noDataFill;
    const logVal = Math.log10(Math.max(sharePct, 0.1));
    const t = Math.max(0, Math.min(1, (logVal - LOG_MIN) / (LOG_MAX - LOG_MIN)));
    return colorInterp(t);
  }

  // ── Utilities ─────────────────────────────────────────────────────────────
  const escapeHtml = (value) =>
    String(value)
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#39;");

  const formatQuantity = (value) => {
    if (!Number.isFinite(value)) return "?";
    const absValue = Math.abs(value);
    if (absValue >= 100 || Number.isInteger(value)) return new Intl.NumberFormat(undefined, { maximumFractionDigits: 0 }).format(value);
    if (absValue >= 10) return new Intl.NumberFormat(undefined, { maximumFractionDigits: 1 }).format(value);
    return new Intl.NumberFormat(undefined, { maximumFractionDigits: 2 }).format(value);
  };

  const formatPct = (value) =>
    new Intl.NumberFormat(undefined, {
      minimumFractionDigits: value >= 10 ? 0 : 1,
      maximumFractionDigits: 1,
    }).format(value);

  const formatLabel = (value) => String(value || "").replaceAll("_", " ");

  const featureCode = (feature) => {
    const props = feature && feature.properties ? feature.properties : {};
    return props.ISO_A2_EH || props.ISO_A2 || "";
  };

  const featureName = (feature) => {
    const props = feature && feature.properties ? feature.properties : {};
    return props.NAME_EN || props.ADMIN || featureCode(feature) || "Unknown";
  };

  // ── Neutral tooltip renderer ───────────────────────────────────────────────
  const renderRows = (rows) => {
    if (!rows || rows.length === 0) {
      return '<div class="country-map-empty">No attributed production/refining rows in the current dataset.</div>';
    }

    return (
      '<div class="country-map-tooltip-table-wrap">' +
        '<table class="country-map-tooltip-table">' +
          '<thead><tr><th>El</th><th>Stage</th><th style="text-align:right">% global</th></tr></thead>' +
          '<tbody>' +
            rows.map((row) => (
              '<tr>' +
                `<td class="country-map-tooltip-col-el">${escapeHtml(row.symbol)}</td>` +
                `<td class="country-map-tooltip-col-stage">${escapeHtml(row.stage)}</td>` +
                `<td class="country-map-tooltip-col-global">${escapeHtml(formatPct(row.global_pct))}%</td>` +
              '</tr>'
            )).join("") +
          '</tbody>' +
        '</table>' +
      '</div>'
    );
  };

  // ── Neutral drawer renderer ────────────────────────────────────────────────
  const renderDrawerRows = (code, rows) => {
    if (!rows || rows.length === 0) {
      return '<div class="country-map-drawer-empty">No attributed production/refining rows in the current dataset.</div>';
    }

    return (
      `<p class="country-map-drawer-summary">${escapeHtml(rows.length)} attributed 2025 rows for ${escapeHtml(code)}. Native quantities are shown as cited; percentages are relative to the corresponding global annual output row.</p>` +
      '<table class="country-map-drawer-table">' +
        '<thead><tr><th>Element</th><th>Stage</th><th>Quantity</th><th style="text-align:right">% global</th></tr></thead>' +
        '<tbody>' +
          rows.map((row) => {
            const stream = row.stream ? `<span class="country-map-drawer-stream">${escapeHtml(formatLabel(row.stream))}</span>` : "";
            return (
              '<tr>' +
                '<td>' +
                  `<a href="elements/${encodeURIComponent(row.symbol)}.html">${escapeHtml(row.symbol)}</a>` +
                  stream +
                '</td>' +
                `<td>${escapeHtml(row.stage)}</td>` +
                `<td>${escapeHtml(formatQuantity(row.quantity_value))} ${escapeHtml(row.quantity_unit)}</td>` +
                `<td class="country-map-drawer-global" style="text-align:right">${escapeHtml(formatPct(row.global_pct))}%</td>` +
              '</tr>'
            );
          }).join("") +
        '</tbody>' +
      '</table>'
    );
  };

  // ── Heatmap tooltip renderer ───────────────────────────────────────────────
  const renderHeatmapTooltip = (countryName, isoCode) => {
    const stageData = (heatmapIndex[activeSymbol] || {})[activeStage] || {};
    const entry = stageData[isoCode];

    // Find element name from index
    const elMeta = elementIndex.find((e) => e.symbol === activeSymbol);
    const elName = elMeta ? elMeta.name : activeSymbol;
    const stageLabel = activeStage.charAt(0).toUpperCase() + activeStage.slice(1);

    let content = `<div class="country-map-tooltip-title">${escapeHtml(countryName)}</div>`;
    content += `<div class="country-map-tooltip-subtitle">${escapeHtml(elName)} — ${escapeHtml(stageLabel)}</div>`;

    if (entry && entry.share_pct != null) {
      const qStr = entry.quantity_value != null
        ? ` (${escapeHtml(formatQuantity(entry.quantity_value))} ${escapeHtml(entry.quantity_unit || "")})`
        : "";
      content += `<div class="country-map-heatmap-share">${escapeHtml(formatPct(entry.share_pct))}% of global output${escapeHtml(qStr)}</div>`;
    } else {
      content += '<div class="country-map-heatmap-share country-map-heatmap-no-data">No attributed data for this stage.</div>';
    }
    return content;
  };

  // ── Heatmap drawer body renderer ──────────────────────────────────────────
  const renderHeatmapDrawerBody = (countryName, isoCode) => {
    const stageData = (heatmapIndex[activeSymbol] || {})[activeStage] || {};
    const entry = stageData[isoCode];

    const elMeta = elementIndex.find((e) => e.symbol === activeSymbol);
    const elName = elMeta ? elMeta.name : activeSymbol;
    const stageLabel = activeStage.charAt(0).toUpperCase() + activeStage.slice(1);

    let html = `<div class="heatmap-drawer-primary">`;
    html += `<div class="heatmap-drawer-element"><a href="elements/${encodeURIComponent(activeSymbol)}.html">${escapeHtml(activeSymbol)}</a> — ${escapeHtml(elName)}</div>`;
    html += `<div class="heatmap-drawer-stage-label">${escapeHtml(stageLabel)} share</div>`;
    if (entry && entry.share_pct != null) {
      const qStr = entry.quantity_value != null
        ? `${escapeHtml(formatQuantity(entry.quantity_value))} ${escapeHtml(entry.quantity_unit || "")}`
        : "";
      html += `<div class="heatmap-drawer-share-pct">${escapeHtml(formatPct(entry.share_pct))}%</div>`;
      if (qStr) html += `<div class="heatmap-drawer-quantity">${qStr}</div>`;
    } else {
      html += '<div class="heatmap-drawer-no-data">No attributed data for this stage.</div>';
    }
    html += `</div>`;

    // Divider + full element scan
    const allRows = countries[isoCode] || [];
    if (allRows.length > 0) {
      html += '<div class="heatmap-drawer-divider">— All attributed elements —</div>';
      html += renderDrawerRows(isoCode, allRows);
    }
    return html;
  };

  // ── Position + show/hide tooltip ──────────────────────────────────────────
  const positionTooltip = (event) => {
    const x = event.clientX + 18;
    const y = event.clientY + 18;
    const rect = tooltip.getBoundingClientRect();
    const maxLeft = window.innerWidth - rect.width - padding;
    const maxTop = window.innerHeight - rect.height - padding;
    tooltip.style.left = `${Math.max(padding, Math.min(x, maxLeft))}px`;
    tooltip.style.top = `${Math.max(padding, Math.min(y, maxTop))}px`;
  };

  const showTooltip = (event, feature) => {
    const code = featureCode(feature);
    if (hoveredCode !== code) {
      if (activeSymbol) {
        tooltip.innerHTML = renderHeatmapTooltip(featureName(feature), code);
      } else {
        const rows = countries[code] || [];
        tooltip.innerHTML =
          `<div class="country-map-tooltip-title">${escapeHtml(featureName(feature))}</div>` +
          '<div class="country-map-tooltip-subtitle">Quick scan. Click for detailed country view.</div>' +
          renderRows(rows);
      }
      hoveredCode = code;
    }
    tooltip.hidden = false;
    positionTooltip(event);
  };

  const hideTooltip = () => {
    tooltip.hidden = true;
    tooltip.innerHTML = "";
    hoveredCode = "";
  };

  const setHoveredNode = (node) => {
    if (hoveredNode && hoveredNode !== pinnedNode) {
      hoveredNode.classList.remove("is-hovered");
    }
    hoveredNode = node;
    if (hoveredNode && hoveredNode !== pinnedNode) {
      hoveredNode.classList.add("is-hovered");
    }
  };

  const clearHoveredNode = () => {
    if (hoveredNode) {
      hoveredNode.classList.remove("is-hovered");
    }
    hoveredNode = null;
  };

  const closeDrawer = () => {
    if (pinnedNode) {
      pinnedNode.classList.remove("is-pinned");
      pinnedNode = null;
    }
    pinnedCode = "";
    drawer.classList.remove("is-open");
    drawer.hidden = true;
    drawer.setAttribute("aria-hidden", "true");
    drawerBackdrop.classList.remove("is-open");
    drawerBackdrop.hidden = true;
  };

  // Set of ISO-2 codes that have a generated country page.
  // ZZ and XX are never generated; all other codes in the atlas data are assumed to have pages.
  const hasCountryPage = (code) => code && code !== "ZZ" && code !== "XX" && code !== "-99";

  const openDrawer = (feature, node) => {
    const code = featureCode(feature);
    const rows = countries[code] || [];

    if (pinnedCode === code) {
      closeDrawer();
      return;
    }

    if (pinnedNode) {
      pinnedNode.classList.remove("is-pinned");
    }

    pinnedCode = code;
    pinnedNode = node;
    pinnedNode.classList.add("is-pinned");
    drawerTitle.textContent = featureName(feature);

    if (activeSymbol) {
      const elMeta = elementIndex.find((e) => e.symbol === activeSymbol);
      const elName = elMeta ? elMeta.name : activeSymbol;
      drawerSubtitle.textContent = `${elName} — ${activeStage} share`;
      drawerBody.innerHTML = renderHeatmapDrawerBody(featureName(feature), code);
    } else {
      drawerSubtitle.textContent = "Pinned country detail";
      drawerBody.innerHTML = renderDrawerRows(code, rows);
    }

    // "View full country page →" link — CC-4 (independent of heatmap mode)
    let countryLink = document.getElementById("country-map-drawer-country-link");
    if (!countryLink) {
      countryLink = document.createElement("p");
      countryLink.id = "country-map-drawer-country-link";
      countryLink.className = "country-map-drawer-link";
      drawerSubtitle.after(countryLink);
    }
    if (hasCountryPage(code)) {
      countryLink.innerHTML = `<a href="countries/${encodeURIComponent(code)}.html">View full page &rarr;</a>`;
      countryLink.hidden = false;
    } else {
      countryLink.hidden = true;
    }

    drawer.hidden = false;
    drawerBackdrop.hidden = false;
    drawer.classList.add("is-open");
    drawer.setAttribute("aria-hidden", "false");
    drawerBackdrop.classList.add("is-open");
  };

  // ── Heatmap fill application ──────────────────────────────────────────────
  function applyHeatmapFills() {
    if (!activeSymbol) return;
    const stageData = (heatmapIndex[activeSymbol] || {})[activeStage] || {};
    window.d3
      .selectAll(".country-shape")
      .transition()
      .duration(300)
      .attr("fill", function () {
        const iso = this.dataset.countryCode;
        const entry = stageData[iso];
        return entry && entry.share_pct != null ? heatFill(entry.share_pct) : noDataFill;
      });
  }

  function clearHeatmapFills() {
    window.d3
      .selectAll(".country-shape")
      .transition()
      .duration(200)
      .attr("fill", null); // remove inline fill, revert to CSS var(--map-land)
  }

  // ── Legend ─────────────────────────────────────────────────────────────────
  let legendEl = null;

  function renderLegend(parentEl) {
    if (legendEl) legendEl.remove();

    legendEl = document.createElement("div");
    legendEl.className = "heatmap-legend";

    const stageData = (heatmapIndex[activeSymbol] || {})[activeStage] || {};
    const allShares = Object.values(stageData).map((e) => e.share_pct).filter((v) => v != null && v > 0);
    const hasData = allShares.length > 0;

    if (!hasData) {
      legendEl.innerHTML = '<span class="heatmap-legend-footnote">No data for this stage.</span>';
      parentEl.appendChild(legendEl);
      return;
    }

    // Canvas gradient bar
    const canvas = document.createElement("canvas");
    canvas.width = 200;
    canvas.height = 12;
    canvas.className = "heatmap-legend-bar";
    const ctx = canvas.getContext("2d");
    for (let i = 0; i < 200; i++) {
      const t = i / 199;
      ctx.fillStyle = colorInterp(t);
      ctx.fillRect(i, 0, 1, 12);
    }

    // Tick marks at 0.1%, 1%, 5%, 20%, 100%
    const ticks = [0.1, 1, 5, 20, 100];
    const ticksHtml = ticks
      .map((v) => `<span>${v < 1 ? v.toFixed(1) : v}%</span>`)
      .join("");

    const barWrap = document.createElement("div");
    barWrap.className = "heatmap-legend-bar-wrap";
    barWrap.appendChild(canvas);
    const ticksEl = document.createElement("div");
    ticksEl.className = "heatmap-legend-ticks";
    ticksEl.style.width = "200px";
    ticksEl.innerHTML = ticksHtml;
    barWrap.appendChild(ticksEl);

    legendEl.innerHTML = '<span class="heatmap-legend-label">Share of global output:</span>';
    legendEl.appendChild(barWrap);

    const footnote = document.createElement("span");
    footnote.className = "heatmap-legend-footnote";
    footnote.textContent = "Uncolored: no data or rest-of-world aggregate.";
    legendEl.appendChild(footnote);

    parentEl.appendChild(legendEl);
  }

  function removeLegend() {
    if (legendEl) {
      legendEl.remove();
      legendEl = null;
    }
  }

  // ── URL state ─────────────────────────────────────────────────────────────
  function updateURL() {
    const params = new URLSearchParams();
    if (activeSymbol) {
      params.set("heatmap", activeSymbol);
      params.set("stage", activeStage);
      history.replaceState(null, "", "?" + params.toString());
    } else {
      history.replaceState(null, "", location.pathname);
    }
  }

  function parseURL() {
    const params = new URLSearchParams(location.search);
    const sym = params.get("heatmap") || "";
    const stage = params.get("stage") || "mining";
    return { sym, stage };
  }

  // ── Map panel copy update ─────────────────────────────────────────────────
  const mapPanelCopy = document.getElementById("map-panel-copy");

  function updateMapPanelCopy() {
    if (!mapPanelCopy) return;
    if (activeSymbol) {
      const elMeta = elementIndex.find((e) => e.symbol === activeSymbol);
      const elName = elMeta ? elMeta.name : activeSymbol;
      const stageLabel = activeStage.charAt(0).toUpperCase() + activeStage.slice(1);
      mapPanelCopy.textContent = `${elName} — ${stageLabel} share by country. Click a country for detail.`;
    } else {
      mapPanelCopy.textContent = "Hover for a compact scan of attributed 2025 mining/refining rows. Click a country for a fuller breakdown with native quantities and share of global annual output.";
    }
  }

  // ── Main heatmap activation / deactivation ────────────────────────────────
  function activateHeatmap(symbol, stage) {
    if (!symbol) return;
    activeSymbol = symbol;
    activeStage = stage || "mining";

    // Auto-advance stage if selected element has no data for it
    const elMeta = elementIndex.find((e) => e.symbol === symbol);
    if (elMeta) {
      const stageOrder = ["mining", "refining", "reserves"];
      const stageFlagMap = { mining: "has_mining", refining: "has_refining", reserves: "has_reserves" };
      if (!elMeta[stageFlagMap[activeStage]]) {
        for (const s of stageOrder) {
          if (elMeta[stageFlagMap[s]]) {
            activeStage = s;
            break;
          }
        }
      }
    }

    // Update select value
    const sel = document.getElementById("heatmap-element-select");
    if (sel) sel.value = activeSymbol;

    // Update stage buttons
    updateStageButtons();

    // Enable stage toggle
    const stageToggle = document.getElementById("heatmap-stage-toggle");
    if (stageToggle) stageToggle.setAttribute("aria-disabled", "false");

    // Show clear button
    const clearBtn = document.getElementById("heatmap-clear");
    if (clearBtn) clearBtn.hidden = false;

    // Update chip styles
    document.querySelectorAll(".heatmap-chip").forEach((chip) => {
      chip.classList.toggle("is-active", chip.dataset.symbol === activeSymbol);
    });

    // Apply fills
    applyHeatmapFills();

    // Render legend (after country-map-shell)
    const shell = document.querySelector(".country-map-shell");
    if (shell && shell.parentNode) {
      renderLegend(shell.parentNode);
    }

    updateMapPanelCopy();
    updateURL();

    // Force tooltip refresh
    hoveredCode = "";
  }

  function deactivateHeatmap() {
    activeSymbol = null;
    activeStage = "mining";

    // Reset select
    const sel = document.getElementById("heatmap-element-select");
    if (sel) sel.value = "";

    // Reset stage buttons to Mining
    updateStageButtons();

    // Disable stage toggle
    const stageToggle = document.getElementById("heatmap-stage-toggle");
    if (stageToggle) stageToggle.setAttribute("aria-disabled", "true");

    // Hide clear button
    const clearBtn = document.getElementById("heatmap-clear");
    if (clearBtn) clearBtn.hidden = true;

    // Clear all chip active states
    document.querySelectorAll(".heatmap-chip").forEach((chip) => chip.classList.remove("is-active"));

    // Reset fills
    clearHeatmapFills();

    // Remove legend
    removeLegend();

    updateMapPanelCopy();
    updateURL();

    // Force tooltip refresh
    hoveredCode = "";

    // Close drawer if open
    closeDrawer();
  }

  function updateStageButtons() {
    document.querySelectorAll(".heatmap-stage-btn").forEach((btn) => {
      btn.classList.toggle("is-active", btn.dataset.stage === activeStage);
    });
  }

  // ── Populate <select> and chips ────────────────────────────────────────────
  function populateElementSelector() {
    const sel = document.getElementById("heatmap-element-select");
    const chipsEl = document.getElementById("heatmap-chips");
    if (!sel || !elementIndex.length) return;

    // Only elements that have at least one stage
    const usable = elementIndex.filter((e) => e.has_mining || e.has_refining || e.has_reserves);

    // Group by tier descending: 3 = Critical & Scarce, 4 = High-Volume, 2 = Niche, 0/1 = Other
    const tierGroups = [
      { label: "Critical & Scarce", tiers: [3] },
      { label: "High-Volume", tiers: [4] },
      { label: "Niche", tiers: [2] },
      { label: "Other", tiers: [0, 1] },
    ];

    for (const group of tierGroups) {
      const items = usable.filter((e) => group.tiers.includes(e.tier));
      if (!items.length) continue;
      const og = document.createElement("optgroup");
      og.label = group.label;
      for (const e of items) {
        const opt = document.createElement("option");
        opt.value = e.symbol;
        opt.textContent = `${e.symbol} — ${e.name}`;
        og.appendChild(opt);
      }
      sel.appendChild(og);
    }

    // Chips: critical elements only
    if (chipsEl) {
      const criticals = usable.filter((e) => e.critical);
      for (const e of criticals) {
        const chip = document.createElement("button");
        chip.type = "button";
        chip.className = "heatmap-chip";
        chip.dataset.symbol = e.symbol;
        chip.textContent = e.symbol;
        chip.title = e.name;
        chip.addEventListener("click", () => {
          if (activeSymbol === e.symbol) {
            deactivateHeatmap();
          } else {
            activateHeatmap(e.symbol, activeStage);
          }
        });
        chipsEl.appendChild(chip);
      }
    }

    // Select onChange
    sel.addEventListener("change", () => {
      const val = sel.value;
      if (val) {
        activateHeatmap(val, activeStage);
      } else {
        deactivateHeatmap();
      }
    });

    // Clear button
    const clearBtn = document.getElementById("heatmap-clear");
    if (clearBtn) {
      clearBtn.addEventListener("click", deactivateHeatmap);
    }

    // Stage toggle buttons
    document.querySelectorAll(".heatmap-stage-btn").forEach((btn) => {
      btn.addEventListener("click", () => {
        if (!activeSymbol) return;
        activeStage = btn.dataset.stage;
        updateStageButtons();
        applyHeatmapFills();

        // Re-render legend
        const shell = document.querySelector(".country-map-shell");
        if (shell && shell.parentNode) {
          renderLegend(shell.parentNode);
        }

        updateURL();
        updateMapPanelCopy();
        hoveredCode = ""; // force tooltip refresh
      });
    });
  }

  // ── GeoJSON fetch + render ─────────────────────────────────────────────────
  root.innerHTML = '<div class="country-map-fallback">Loading map geometry\u2026</div>';

  fetch(geojsonSrc)
    .then((response) => {
      if (!response.ok) {
        throw new Error(`Map fetch failed: ${response.status}`);
      }
      return response.json();
    })
    .then((geojson) => {
      const features = (geojson.features || []).filter((feature) => {
        const code = featureCode(feature);
        return code && code !== "-99";
      });

      if (!features.length) {
        throw new Error("No country geometry found");
      }

      root.innerHTML = "";

      const svg = window.d3
        .select(root)
        .append("svg")
        .attr("viewBox", `0 0 ${width} ${height}`)
        .attr("aria-label", "World map with country hover details")
        .attr("role", "img");

      const projection = window.d3.geoNaturalEarth1();
      projection.fitExtent([[12, 12], [width - 12, height - 12]], {
        type: "FeatureCollection",
        features,
      });
      const path = window.d3.geoPath(projection);

      svg
        .append("g")
        .selectAll("path")
        .data(features)
        .join("path")
        .attr("class", "country-shape")
        .attr("data-country-code", (feature) => featureCode(feature))
        .attr("d", path)
        .on("mouseenter", function (event, feature) {
          setHoveredNode(this);
          showTooltip(event, feature);
        })
        .on("mousemove", function (event, feature) {
          showTooltip(event, feature);
        })
        .on("mouseleave", function () {
          clearHoveredNode();
          hideTooltip();
        })
        .on("click", function (event, feature) {
          event.preventDefault();
          event.stopPropagation();
          openDrawer(feature, this);
        });

      drawerClose.addEventListener("click", closeDrawer);
      drawerBackdrop.addEventListener("click", closeDrawer);
      document.addEventListener("keydown", (event) => {
        if (event.key === "Escape" && pinnedCode) {
          closeDrawer();
        }
      });

      // Build heatmap index now that we have payload
      heatmapIndex = buildHeatmapIndex(countries, payload.reserves || {});

      // Populate selector + chips
      populateElementSelector();

      // Apply URL state
      const { sym, stage } = parseURL();
      if (sym && elementIndex.find((e) => e.symbol === sym)) {
        activateHeatmap(sym, stage);
      }
    })
    .catch(() => {
      root.innerHTML = '<div class="country-map-fallback">Country map geometry could not be loaded.</div>';
      hideTooltip();
      closeDrawer();
    });
})();
