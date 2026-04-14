// viewer/assets/charts_country.js
// Client-side rendering for country pages:
//   1. Horizontal bar chart from #country-chart-data JSON.
//   2. World-map thumbnail highlighting this country's feature.
//   3. Sortable column headers on .sortable-table elements.

(function () {
  "use strict";

  // ── Helpers ─────────────────────────────────────────────────────────────────

  const escapeHtml = (value) =>
    String(value)
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#39;");

  const featureCode = (feature) => {
    const props = feature && feature.properties ? feature.properties : {};
    return props.ISO_A2 || props.ISO_A2_EH || "";
  };

  // ── 1. Horizontal bar chart ──────────────────────────────────────────────────

  const chartEl = document.getElementById("country-bar-chart");
  const chartDataScript = document.getElementById("country-chart-data");

  if (chartEl && chartDataScript && window.d3) {
    let chartData;
    try {
      chartData = JSON.parse(chartDataScript.textContent || "[]");
    } catch (_e) {
      chartData = [];
    }

    if (Array.isArray(chartData) && chartData.length > 0) {
      const STAGE_COLORS = {
        mining: "var(--accent, #2563eb)",
        refining: "#ea580c",
        reserves: "#16a34a",
      };

      const margin = { top: 8, right: 60, bottom: 52, left: 120 };
      const width = Math.min(600, chartEl.clientWidth || 600);
      const barHeight = 20;
      const barGap = 4;
      const innerWidth = width - margin.left - margin.right;
      const innerHeight = chartData.length * (barHeight + barGap);
      const totalHeight = innerHeight + margin.top + margin.bottom;

      const xMax = d3.max(chartData, (d) => d.share_pct || 0) || 100;
      const xScale = d3.scaleLinear().domain([0, xMax]).range([0, innerWidth]);

      const svg = d3
        .select(chartEl)
        .append("svg")
        .attr("width", width)
        .attr("height", totalHeight)
        .attr("aria-label", "Element share bar chart")
        .attr("role", "img");

      const g = svg.append("g").attr("transform", `translate(${margin.left},${margin.top})`);

      // Bars
      chartData.forEach((d, i) => {
        const y = i * (barHeight + barGap);
        const barW = xScale(d.share_pct || 0);
        const color = STAGE_COLORS[d.stage] || "var(--accent, #2563eb)";

        // Bar rect
        g.append("rect")
          .attr("x", 0)
          .attr("y", y)
          .attr("width", barW)
          .attr("height", barHeight)
          .attr("fill", color);

        // Symbol label (left)
        g.append("text")
          .attr("x", -4)
          .attr("y", y + barHeight / 2 + 4)
          .attr("text-anchor", "end")
          .attr("font-size", "11px")
          .attr("fill", "currentColor")
          .text(d.symbol || "");

        // Value label (right of bar)
        if (d.share_pct != null) {
          g.append("text")
            .attr("x", barW + 4)
            .attr("y", y + barHeight / 2 + 4)
            .attr("font-size", "10px")
            .attr("fill", "var(--muted, #6b7280)")
            .text(`${d.share_pct.toFixed(1)}%`);
        }
      });

      // X axis
      g.append("g")
        .attr("transform", `translate(0,${innerHeight})`)
        .call(d3.axisBottom(xScale).ticks(4).tickFormat((d) => `${d}%`))
        .call((axis) => axis.select(".domain").remove());

      // Legend (sits below x-axis tick labels with a clear gap)
      const legendItems = [...new Set(chartData.map((d) => d.stage))];
      const legendY = margin.top + innerHeight + 40;
      const legendG = svg.append("g").attr("transform", `translate(${margin.left},${legendY})`);
      legendItems.forEach((stage, idx) => {
        const lx = idx * 100;
        legendG.append("rect").attr("x", lx).attr("y", -9).attr("width", 10).attr("height", 10).attr("fill", STAGE_COLORS[stage] || "#999");
        legendG
          .append("text")
          .attr("x", lx + 15)
          .attr("y", 0)
          .attr("font-size", "10px")
          .attr("letter-spacing", "0.06em")
          .attr("fill", "currentColor")
          .text(String(stage).toUpperCase());
      });
    }
  }

  // ── 2. World-map thumbnail ───────────────────────────────────────────────────

  const thumb = document.getElementById("country-map-thumb");

  if (thumb && window.d3) {
    const iso = thumb.dataset.countryCode || "";
    const geojsonSrc = "../assets/world_countries_50m.geojson";
    const thumbW = 240;
    const thumbH = 135;

    const svg = d3
      .select(thumb)
      .append("svg")
      .attr("width", thumbW)
      .attr("height", thumbH)
      .attr("aria-label", `World map highlighting ${iso}`)
      .attr("role", "img");

    svg.append("rect").attr("width", thumbW).attr("height", thumbH).attr("fill", "var(--surface, #f6f7f8)");

    fetch(geojsonSrc)
      .then((r) => (r.ok ? r.json() : Promise.reject(r.status)))
      .then((geojson) => {
        const features = (geojson.features || []).filter((f) => {
          const code = featureCode(f);
          return code && code !== "-99";
        });

        const projection = d3.geoNaturalEarth1();
        projection.fitExtent([[2, 2], [thumbW - 2, thumbH - 2]], { type: "FeatureCollection", features });
        const path = d3.geoPath(projection);

        svg
          .selectAll("path")
          .data(features)
          .enter()
          .append("path")
          .attr("d", path)
          .attr("fill", (f) => (featureCode(f) === iso ? "var(--map-land-hover, #bfdbfe)" : "var(--map-land, #dbe4ee)"))
          .attr("stroke", (f) => (featureCode(f) === iso ? "var(--map-land-hover-stroke, #2563eb)" : "var(--map-land-stroke, #94a3b8)"))
          .attr("stroke-width", (f) => (featureCode(f) === iso ? 1.2 : 0.4));
      })
      .catch(() => {
        // Silently degrade if fetch fails (e.g. file:// protocol)
        svg.append("text").attr("x", thumbW / 2).attr("y", thumbH / 2).attr("text-anchor", "middle").attr("font-size", "10px").attr("fill", "var(--muted, #6b7280)").text("Map unavailable");
      });
  }

  // ── 3. Column-sort for .sortable-table elements ──────────────────────────────
  // Minimal inline sort; will be refactored into table_sort.js by the
  // table-filter-sort PR (CC-5 acceptable temporary duplication).

  document.querySelectorAll("table.sortable-table").forEach((table) => {
    const headers = table.querySelectorAll("thead th");
    headers.forEach((th, colIdx) => {
      th.style.cursor = "pointer";
      th.setAttribute("aria-sort", "none");

      th.addEventListener("click", () => {
        const tbody = table.querySelector("tbody");
        if (!tbody) return;

        const currentSort = th.getAttribute("aria-sort");
        const ascending = currentSort !== "ascending";

        // Reset all headers
        headers.forEach((h) => h.setAttribute("aria-sort", "none"));
        th.setAttribute("aria-sort", ascending ? "ascending" : "descending");

        const rows = Array.from(tbody.querySelectorAll("tr"));
        rows.sort((a, b) => {
          const aCell = a.querySelectorAll("td")[colIdx];
          const bCell = b.querySelectorAll("td")[colIdx];
          const aText = aCell ? aCell.innerText.trim() : "";
          const bText = bCell ? bCell.innerText.trim() : "";

          // Try numeric comparison first
          const aNum = parseFloat(aText.replace(/[^0-9.-]/g, ""));
          const bNum = parseFloat(bText.replace(/[^0-9.-]/g, ""));
          if (!isNaN(aNum) && !isNaN(bNum)) {
            return ascending ? aNum - bNum : bNum - aNum;
          }
          // Ordinal rank: 1st, 2nd, 3rd…
          const aOrd = parseInt(aText, 10);
          const bOrd = parseInt(bText, 10);
          if (!isNaN(aOrd) && !isNaN(bOrd)) {
            return ascending ? aOrd - bOrd : bOrd - aOrd;
          }
          return ascending ? aText.localeCompare(bText) : bText.localeCompare(aText);
        });

        rows.forEach((row) => tbody.appendChild(row));
      });
    });
  });
})();
