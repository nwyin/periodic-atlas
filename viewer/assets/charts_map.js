// viewer/assets/charts_map.js
// Render the neutral country hover map on viewer/index.html.

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

  const escapeHtml = (value) =>
    String(value)
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#39;");

  const formatQuantity = (value) => {
    if (!Number.isFinite(value)) {
      return "?";
    }
    const absValue = Math.abs(value);
    if (absValue >= 100 || Number.isInteger(value)) {
      return new Intl.NumberFormat(undefined, { maximumFractionDigits: 0 }).format(value);
    }
    if (absValue >= 10) {
      return new Intl.NumberFormat(undefined, { maximumFractionDigits: 1 }).format(value);
    }
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
      const rows = countries[code] || [];
      tooltip.innerHTML =
        `<div class="country-map-tooltip-title">${escapeHtml(featureName(feature))}</div>` +
        '<div class="country-map-tooltip-subtitle">Quick scan. Click for detailed country view.</div>' +
        renderRows(rows);
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
    drawerSubtitle.textContent = "Pinned country detail";

    // "View full country page →" link — CC-4
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

    drawerBody.innerHTML = renderDrawerRows(code, rows);
    drawer.hidden = false;
    drawerBackdrop.hidden = false;
    drawer.classList.add("is-open");
    drawer.setAttribute("aria-hidden", "false");
    drawerBackdrop.classList.add("is-open");
  };

  root.innerHTML = '<div class="country-map-fallback">Loading map geometry…</div>';

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
    })
    .catch(() => {
      root.innerHTML = '<div class="country-map-fallback">Country map geometry could not be loaded.</div>';
      hideTooltip();
      closeDrawer();
    });
})();
