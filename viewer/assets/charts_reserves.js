/**
 * charts_reserves.js — B2 reserves + end-uses charts
 *
 * Reads inline JSON from <script id="reserves-data" type="application/json">
 * and renders into #reserves-chart:
 *   - Big-number callouts for economic_reserves + resources
 *   - Horizontal bar chart for reserves_by_country
 *   - Donut chart for end_uses
 *
 * Low-confidence entries (confidence !== "high") get a dashed stroke.
 * Both charts show a completeness badge.
 * Elements with no data show an empty-state message instead of crashing.
 */
(function () {
  "use strict";

  // ── Data ───────────────────────────────────────────────────���─────────────
  const dataEl = document.getElementById("reserves-data");
  if (!dataEl) return;

  let data;
  try {
    data = JSON.parse(dataEl.textContent);
  } catch (e) {
    console.error("charts_reserves: failed to parse reserves-data JSON", e);
    return;
  }

  const container = document.getElementById("reserves-chart");
  if (!container) return;

  // Remove the placeholder text
  container.textContent = "";
  container.classList.remove("chart-placeholder");
  container.style.cssText = "margin: 1.25rem 0;";

  const { reserves, reserves_by_country, end_uses } = data;

  // ── CSS custom properties (read from :root) ───────────────────────────────
  const style = getComputedStyle(document.documentElement);
  const C = {
    accent:  style.getPropertyValue("--accent").trim()  || "#2563eb",
    muted:   style.getPropertyValue("--muted").trim()   || "#6b7280",
    border:  style.getPropertyValue("--border").trim()  || "#d4d8de",
    text:    style.getPropertyValue("--text").trim()    || "#1a1c1e",
    surface: style.getPropertyValue("--surface").trim() || "#f6f7f8",
  };

  // Palette for donut slices
  const COLOR_PALETTE = [
    "#2563eb", "#16a34a", "#d97706", "#dc2626", "#7c3aed",
    "#0891b2", "#b45309", "#9333ea", "#059669", "#c2410c",
  ];

  // ── Helpers ───────────────────────────────────────────────────────────────
  function formatNumber(v) {
    if (v == null) return "—";
    if (v >= 1e9) return (v / 1e9).toFixed(1) + " B";
    if (v >= 1e6) return (v / 1e6).toFixed(1) + " M";
    if (v >= 1e3) return (v / 1e3).toFixed(1) + " k";
    return v.toLocaleString();
  }

  function completenessLabel(c) {
    const labels = { complete: "Complete", partial: "Partial", unknown: "Unknown" };
    return labels[c] || c || "Unknown";
  }

  function completenessClass(c) {
    const classes = { complete: "complete", partial: "partial", unknown: "unknown" };
    return classes[c] || "unknown";
  }

  // ── Section header helper ─────────────────────────────────────────────────
  function makeSection(heading) {
    const sec = document.createElement("div");
    sec.style.cssText = "margin-bottom: 1.5rem;";
    const h = document.createElement("h3");
    h.textContent = heading;
    h.style.cssText = "font-size:1rem; margin:0 0 0.75rem; color:" + C.text + ";";
    sec.appendChild(h);
    return sec;
  }

  function makeBadge(text, type) {
    const s = document.createElement("span");
    s.textContent = text;
    const colors = { complete: "#16a34a", partial: "#d97706", unknown: C.muted };
    s.style.cssText = [
      "display:inline-block",
      "font-size:0.72rem",
      "font-weight:600",
      "padding:0.15em 0.5em",
      "border-radius:4px",
      "color:#fff",
      "background:" + (colors[type] || C.muted),
      "margin-left:0.5em",
      "vertical-align:middle",
    ].join(";");
    return s;
  }

  function makeEmptyState(message) {
    const div = document.createElement("div");
    div.style.cssText = [
      "border:2px dashed " + C.border,
      "border-radius:6px",
      "padding:1.5rem",
      "text-align:center",
      "color:" + C.muted,
      "font-size:0.88rem",
    ].join(";");
    div.textContent = message;
    return div;
  }

  // ── Big-number callouts ───────────────────────────────────────────────────
  const hasReserves = reserves && (reserves.economic_reserves != null || reserves.resources != null);

  if (hasReserves) {
    const calloutRow = document.createElement("div");
    calloutRow.style.cssText = [
      "display:grid",
      "grid-template-columns:repeat(auto-fit,minmax(160px,1fr))",
      "gap:0.75rem",
      "margin-bottom:1.25rem",
    ].join(";");

    const items = [
      { label: "Economic Reserves", value: reserves.economic_reserves, unit: reserves.unit },
      { label: "Resources",         value: reserves.resources,         unit: reserves.unit },
    ];

    items.forEach(function (item) {
      const card = document.createElement("div");
      card.style.cssText = [
        "background:" + C.surface,
        "border:1px solid " + C.border,
        "border-radius:6px",
        "padding:0.75rem 1rem",
      ].join(";");

      const val = document.createElement("div");
      val.style.cssText = "font-size:1.75rem;font-weight:700;line-height:1;";
      val.textContent = item.value != null ? formatNumber(item.value) : "—";

      const lbl = document.createElement("div");
      lbl.style.cssText = "font-size:0.8rem;color:" + C.muted + ";margin-top:0.2rem;";
      lbl.textContent = item.label + (item.unit ? " (" + item.unit + ")" : "");

      card.appendChild(val);
      card.appendChild(lbl);
      calloutRow.appendChild(card);
    });

    container.appendChild(calloutRow);
  }

  // ── Reserves by Country (horizontal bar chart) ────────────────────────────
  {
    const sec = makeSection("Reserves by Country");

    const hasData = reserves_by_country && reserves_by_country.length > 0;

    if (!hasData) {
      sec.appendChild(makeEmptyState("No reserves data"));
      container.appendChild(sec);
    } else {
      // Build SVG bar chart
      const margin = { top: 8, right: 60, bottom: 8, left: 50 };
      const BAR_HEIGHT = 22;
      const BAR_GAP = 6;
      const innerH = reserves_by_country.length * (BAR_HEIGHT + BAR_GAP);
      const totalH = innerH + margin.top + margin.bottom;
      const containerW = container.clientWidth || 600;
      const innerW = Math.max(containerW - margin.left - margin.right, 200);

      const maxPct = d3.max(reserves_by_country, function (d) { return d.share_pct || 0; });
      const xScale = d3.scaleLinear().domain([0, maxPct]).range([0, innerW]);

      const svg = d3.create("svg")
        .attr("width", "100%")
        .attr("viewBox", [0, 0, containerW, totalH])
        .attr("role", "img")
        .attr("aria-label", "Reserves by country bar chart");

      const g = svg.append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

      reserves_by_country.forEach(function (d, i) {
        const y = i * (BAR_HEIGHT + BAR_GAP);
        const isLowConf = d.confidence && d.confidence !== "high";
        const barW = xScale(d.share_pct || 0);

        // Country label
        g.append("text")
          .attr("x", -4)
          .attr("y", y + BAR_HEIGHT / 2 + 4)
          .attr("text-anchor", "end")
          .attr("font-size", "12")
          .attr("fill", C.text)
          .text(d.country);

        // Bar rect
        const rect = g.append("rect")
          .attr("x", 0)
          .attr("y", y)
          .attr("width", barW)
          .attr("height", BAR_HEIGHT)
          .attr("rx", 3)
          .attr("fill", C.accent)
          .attr("opacity", isLowConf ? 0.5 : 0.85);

        if (isLowConf) {
          rect
            .attr("stroke", C.muted)
            .attr("stroke-width", 1.5)
            .attr("stroke-dasharray", "4 3");
        }

        // Percentage label
        g.append("text")
          .attr("x", barW + 5)
          .attr("y", y + BAR_HEIGHT / 2 + 4)
          .attr("font-size", "11")
          .attr("fill", C.muted)
          .text((d.share_pct != null ? d.share_pct.toFixed(0) : "?") + "%"
            + (isLowConf ? " ⚠" : ""));
      });

      sec.appendChild(svg.node());
      container.appendChild(sec);
    }
  }

  // ── End Uses (donut chart) ─────────────────────────────────────���──────────
  {
    const sec = makeSection("End Uses");
    const hdr = sec.querySelector("h3");

    const hasUses = end_uses && end_uses.uses && end_uses.uses.length > 0;

    if (hasUses) {
      const comp = end_uses.completeness || "partial";
      hdr.appendChild(makeBadge(completenessLabel(comp), completenessClass(comp)));
    }

    if (!hasUses) {
      sec.appendChild(makeEmptyState("No end-use data"));
      container.appendChild(sec);
    } else {
      const uses = end_uses.uses;

      // Layout: donut on left, legend on right
      const wrapper = document.createElement("div");
      wrapper.style.cssText = "display:flex;gap:1.5rem;align-items:flex-start;flex-wrap:wrap;";

      const DONUT_SIZE = 200;
      const outerR = DONUT_SIZE / 2 - 4;
      const innerR = outerR * 0.54;

      const pie = d3.pie()
        .value(function (d) { return d.share_pct || 0; })
        .sort(null);

      const arc = d3.arc().innerRadius(innerR).outerRadius(outerR);
      const labelArc = d3.arc().innerRadius(outerR * 0.78).outerRadius(outerR * 0.78);

      const arcs = pie(uses);

      const svg = d3.create("svg")
        .attr("width", DONUT_SIZE)
        .attr("height", DONUT_SIZE)
        .attr("viewBox", [0, 0, DONUT_SIZE, DONUT_SIZE])
        .attr("role", "img")
        .attr("aria-label", "End uses donut chart");

      const g = svg.append("g")
        .attr("transform", "translate(" + DONUT_SIZE / 2 + "," + DONUT_SIZE / 2 + ")");

      arcs.forEach(function (d, i) {
        const isLowConf = d.data.confidence && d.data.confidence !== "high";
        const color = COLOR_PALETTE[i % COLOR_PALETTE.length];

        const path = g.append("path")
          .attr("d", arc(d))
          .attr("fill", color)
          .attr("opacity", isLowConf ? 0.5 : 0.85);

        if (isLowConf) {
          path
            .attr("stroke", "#fff")
            .attr("stroke-width", 2)
            .attr("stroke-dasharray", "4 3");
        } else {
          path.attr("stroke", "#fff").attr("stroke-width", 1.5);
        }

        // Label on slice if large enough
        const midAngle = d.startAngle + (d.endAngle - d.startAngle) / 2;
        const pct = d.data.share_pct || 0;
        if (pct >= 8) {
          const pos = labelArc.centroid(d);
          g.append("text")
            .attr("transform", "translate(" + pos + ")")
            .attr("text-anchor", "middle")
            .attr("font-size", "10")
            .attr("fill", "#fff")
            .attr("font-weight", "600")
            .text(pct.toFixed(0) + "%");
        }
      });

      wrapper.appendChild(svg.node());

      // Legend
      const legend = document.createElement("div");
      legend.style.cssText = "flex:1;min-width:180px;font-size:0.82rem;line-height:1.8;";
      uses.forEach(function (u, i) {
        const isLowConf = u.confidence && u.confidence !== "high";
        const color = COLOR_PALETTE[i % COLOR_PALETTE.length];
        const item = document.createElement("div");
        item.style.cssText = "display:flex;align-items:center;gap:0.4rem;";

        const swatch = document.createElement("span");
        swatch.style.cssText = [
          "display:inline-block",
          "width:10px",
          "height:10px",
          "border-radius:2px",
          "flex-shrink:0",
          "background:" + color,
          "opacity:" + (isLowConf ? "0.5" : "0.85"),
          isLowConf ? "outline:1.5px dashed " + C.muted : "",
        ].join(";");

        const label = document.createElement("span");
        const displayName = u.application.replace(/_/g, " ");
        label.textContent = displayName + " — " + (u.share_pct != null ? u.share_pct.toFixed(0) : "?") + "%"
          + (isLowConf ? " ⚠" : "");
        label.style.color = isLowConf ? C.muted : C.text;
        if (isLowConf) label.title = "Low-confidence estimate";

        item.appendChild(swatch);
        item.appendChild(label);
        legend.appendChild(item);
      });

      wrapper.appendChild(legend);
      sec.appendChild(wrapper);
      container.appendChild(sec);
    }
  }
})();
