/**
 * charts_production.js — B1 mining + refining share bar charts
 *
 * Reads inline JSON from <script id="production-data" type="application/json">
 * and renders into #production-chart:
 *   - For each stream: a grouped bar chart with mining shares and (if present)
 *     refining shares side-by-side on the same x-axis (country ISO2 codes).
 *   - World-total reference text above each chart group.
 *   - Completeness badges (complete / top_producers_only / partial).
 *   - Low-confidence shares get reduced opacity (0.45).
 *   - Tooltip on hover: country full name, share %, quantity + unit.
 *   - Elements with no production data keep the placeholder empty-state message.
 *
 * JSON shape expected (from build_viewer.py _production_json):
 *   {
 *     "streams": [
 *       {
 *         "stream_id": int|null,
 *         "mining": [{"country": str, "share_pct": float, "quantity": float|null,
 *                      "unit": str|null, "form": str|null, "confidence": str}, ...],
 *         "refining": [...same shape...],
 *         "completeness": {"mining": str, "refining": str},
 *         "world_mine": {"value": float|null, "unit": str|null, "form": str|null},
 *         "world_refined": {"value": float|null, "unit": str|null, "form": str|null}
 *       }, ...
 *     ]
 *   }
 */
(function () {
  "use strict";

  // ── Data ────────────────────────���─────────────────────────��───────────────
  const dataEl = document.getElementById("production-data");
  if (!dataEl) return;

  let data;
  try {
    data = JSON.parse(dataEl.textContent);
  } catch (e) {
    console.error("charts_production: failed to parse production-data JSON", e);
    return;
  }

  const container = document.getElementById("production-chart");
  if (!container) return;

  const streams = data.streams || [];

  if (!streams.length) {
    // No production data — keep the placeholder message
    return;
  }

  // Remove the placeholder styling and clear text
  container.textContent = "";
  container.classList.remove("chart-placeholder");
  container.style.cssText = "margin: 1.25rem 0;";

  // ── CSS custom properties ─────────────────────────────────────────────────
  const style = getComputedStyle(document.documentElement);
  const C = {
    accent:  style.getPropertyValue("--accent").trim()  || "#2563eb",
    muted:   style.getPropertyValue("--muted").trim()   || "#6b7280",
    border:  style.getPropertyValue("--border").trim()  || "#d4d8de",
    text:    style.getPropertyValue("--text").trim()    || "#1a1c1e",
    surface: style.getPropertyValue("--surface").trim() || "#f6f7f8",
  };

  // Color pair: mining = blue family, refining = teal family
  const COLOR_MINING   = "#2563eb";
  const COLOR_REFINING = "#0891b2";

  // ── Country name map (ISO2 → full name) ───────────────────────────────────
  const COUNTRY_NAMES = {
    AU: "Australia",
    CA: "Canada",
    CD: "DR Congo",
    CN: "China",
    CU: "Cuba",
    DZ: "Algeria",
    F:  "France",
    FI: "Finland",
    ID: "Indonesia",
    JP: "Japan",
    KR: "South Korea",
    MG: "Madagascar",
    MM: "Myanmar",
    MN: "Mongolia",
    MX: "Mexico",
    NC: "New Caledonia",
    NG: "Nigeria",
    NO: "Norway",
    PG: "Papua New Guinea",
    PH: "Philippines",
    PL: "Poland",
    QA: "Qatar",
    RU: "Russia",
    SK: "Slovakia",
    TR: "Turkey",
    UA: "Ukraine",
    US: "United States",
    ZA: "South Africa",
    ZZ: "Other",
  };

  function countryName(iso2) {
    return COUNTRY_NAMES[iso2] || iso2;
  }

  // ── Number formatter ────────────────────────────��─────────────────────────
  function formatNumber(v) {
    if (v == null) return "—";
    if (v >= 1e9) return (v / 1e9).toFixed(1) + " B";
    if (v >= 1e6) return (v / 1e6).toFixed(1) + " M";
    if (v >= 1e3) return (v / 1e3).toFixed(1) + " k";
    return v.toLocaleString();
  }

  // ── Completeness helpers ──────────────────────────────────────────────────
  function completenessLabel(c) {
    const map = {
      complete:           "Complete",
      top_producers_only: "Top producers only",
      partial:            "Partial",
      unknown:            "Unknown",
    };
    return map[c] || c || "Unknown";
  }

  function completenessColor(c) {
    return c === "complete" ? "#16a34a" : c === "top_producers_only" ? "#d97706" : C.muted;
  }

  // ── Tooltip ─────────────────────────────���──────────────────────��──────────
  const tooltip = document.createElement("div");
  tooltip.style.cssText = [
    "position:fixed",
    "pointer-events:none",
    "display:none",
    "background:" + C.text,
    "color:#fff",
    "font-size:0.78rem",
    "padding:0.4em 0.65em",
    "border-radius:4px",
    "z-index:9999",
    "max-width:200px",
    "line-height:1.4",
  ].join(";");
  document.body.appendChild(tooltip);

  function showTooltip(evt, html) {
    tooltip.innerHTML = html;
    tooltip.style.display = "block";
    positionTooltip(evt);
  }

  function positionTooltip(evt) {
    const x = evt.clientX + 12;
    const y = evt.clientY - 8;
    tooltip.style.left = x + "px";
    tooltip.style.top  = y + "px";
  }

  function hideTooltip() {
    tooltip.style.display = "none";
  }

  // ── Badge helper ───────────────────────────────────────────────────��──────
  function makeBadge(text, color) {
    const s = document.createElement("span");
    s.textContent = text;
    s.style.cssText = [
      "display:inline-block",
      "font-size:0.72rem",
      "font-weight:600",
      "padding:0.15em 0.5em",
      "border-radius:4px",
      "color:#fff",
      "background:" + color,
      "margin-left:0.4em",
      "vertical-align:middle",
    ].join(";");
    return s;
  }

  // ── Section header ────────────────────────────────────────────────────────
  function makeSection(heading, subTitle) {
    const sec = document.createElement("div");
    sec.style.cssText = "margin-bottom: 1.75rem;";
    const h = document.createElement("h3");
    h.textContent = heading;
    h.style.cssText = "font-size:1rem; margin:0 0 0.75rem; color:" + C.text + ";";
    if (subTitle) {
      const sub = document.createElement("span");
      sub.textContent = " — " + subTitle;
      sub.style.cssText = "font-weight:400; color:" + C.muted + ";";
      h.appendChild(sub);
    }
    sec.appendChild(h);
    return sec;
  }

  // ── World-total callout ───────────────────��───────────────────────────────
  function makeWorldTotal(stream) {
    const items = [];
    if (stream.world_mine && stream.world_mine.value != null) {
      items.push({
        label: "World mine production",
        value: stream.world_mine.value,
        unit:  stream.world_mine.unit,
        form:  stream.world_mine.form,
      });
    }
    if (stream.world_refined && stream.world_refined.value != null) {
      items.push({
        label: "World refined production",
        value: stream.world_refined.value,
        unit:  stream.world_refined.unit,
        form:  stream.world_refined.form,
      });
    }
    if (!items.length) return null;

    const row = document.createElement("div");
    row.style.cssText = [
      "display:flex",
      "flex-wrap:wrap",
      "gap:0.75rem",
      "margin-bottom:1rem",
    ].join(";");

    items.forEach(function (item) {
      const card = document.createElement("div");
      card.style.cssText = [
        "background:" + C.surface,
        "border:1px solid " + C.border,
        "border-radius:6px",
        "padding:0.6rem 0.9rem",
        "min-width:160px",
      ].join(";");

      const val = document.createElement("div");
      val.style.cssText = "font-size:1.5rem; font-weight:700; line-height:1;";
      val.textContent = formatNumber(item.value);

      const lbl = document.createElement("div");
      lbl.style.cssText = "font-size:0.78rem; color:" + C.muted + "; margin-top:0.2rem;";
      const unitStr = item.unit ? " " + item.unit : "";
      lbl.textContent = item.label + unitStr;

      card.appendChild(val);
      card.appendChild(lbl);
      row.appendChild(card);
    });
    return row;
  }

  // ── Single bar chart (mining or refining) ──────────────────��──────────────
  /**
   * renderBarChart(parentEl, shares, seriesLabel, seriesColor, completeness)
   * shares = [{ country, share_pct, quantity, unit, form, confidence }, ...]
   */
  function renderBarChart(parentEl, shares, seriesLabel, seriesColor, completenessVal) {
    if (!shares || !shares.length) {
      const empty = document.createElement("div");
      empty.style.cssText = [
        "border:1px dashed " + C.border,
        "border-radius:4px",
        "padding:0.75rem 1rem",
        "color:" + C.muted,
        "font-size:0.83rem",
        "margin-bottom:0.75rem",
      ].join(";");
      empty.textContent = "No " + seriesLabel.toLowerCase() + " share data";
      parentEl.appendChild(empty);
      return;
    }

    // Header row: series label only
    const hdr = document.createElement("div");
    hdr.style.cssText = "display:flex; align-items:center; margin-bottom:0.5rem;";
    const lbl = document.createElement("span");
    lbl.style.cssText = "font-size:0.95rem; font-weight:600; color:" + C.text + ";";
    lbl.textContent = seriesLabel;
    hdr.appendChild(lbl);
    parentEl.appendChild(hdr);

    // Dimensions
    const margin = { top: 4, right: 60, bottom: 28, left: 44 };
    const BAR_HEIGHT = 22;
    const BAR_GAP    = 6;
    const innerH = shares.length * (BAR_HEIGHT + BAR_GAP);
    const totalH = innerH + margin.top + margin.bottom;
    const containerW = container.clientWidth || 640;
    const innerW = Math.max(containerW - margin.left - margin.right, 200);

    const maxPct = d3.max(shares, function (d) { return d.share_pct || 0; });
    const xScale = d3.scaleLinear().domain([0, maxPct]).range([0, innerW]);

    const svg = d3.create("svg")
      .attr("width", "100%")
      .attr("viewBox", [0, 0, containerW, totalH])
      .attr("role", "img")
      .attr("aria-label", seriesLabel + " share by country");

    const g = svg.append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    shares.forEach(function (d, i) {
      const y = i * (BAR_HEIGHT + BAR_GAP);
      const w = xScale(d.share_pct || 0);
      const isLowConf = d.confidence && d.confidence !== "high";

      // Country label
      g.append("text")
        .attr("x", -4)
        .attr("y", y + BAR_HEIGHT / 2)
        .attr("dy", "0.35em")
        .attr("text-anchor", "end")
        .attr("font-size", "12px")
        .attr("fill", C.muted)
        .text(d.country || "?");

      // Bar rect
      const rect = g.append("rect")
        .attr("x", 0)
        .attr("y", y)
        .attr("width", Math.max(w, 1))
        .attr("height", BAR_HEIGHT)
        .attr("rx", 2)
        .attr("fill", seriesColor)
        .attr("opacity", isLowConf ? 0.45 : 0.85);

      // Pct label
      g.append("text")
        .attr("x", w + 4)
        .attr("y", y + BAR_HEIGHT / 2)
        .attr("dy", "0.35em")
        .attr("font-size", "12px")
        .attr("fill", C.text)
        .text((d.share_pct != null ? d.share_pct : "?") + "%");

      // Tooltip
      const tooltipHtml = buildTooltip(d, isLowConf);
      rect
        .on("mouseover", function (evt) { showTooltip(evt, tooltipHtml); })
        .on("mousemove", positionTooltip)
        .on("mouseout",  hideTooltip);
    });

    // x-axis tick labels at 0 and max
    const axisG = g.append("g")
      .attr("transform", "translate(0," + innerH + ")");
    axisG.append("line")
      .attr("x1", 0).attr("x2", innerW)
      .attr("y1", 0).attr("y2", 0)
      .attr("stroke", C.border);
    axisG.append("text")
      .attr("x", 0).attr("y", 14)
      .attr("font-size", "10px").attr("fill", C.muted)
      .text("0%");
    axisG.append("text")
      .attr("x", innerW).attr("y", 14)
      .attr("font-size", "10px").attr("fill", C.muted)
      .attr("text-anchor", "end")
      .text(maxPct + "%");

    parentEl.appendChild(svg.node());
  }

  function buildTooltip(d, isLowConf) {
    const name = countryName(d.country);
    let html = "<strong>" + name + "</strong><br>" + (d.share_pct != null ? d.share_pct : "?") + "%";
    if (d.quantity != null) {
      const unit = d.unit ? " " + d.unit : "";
      html += "<br>" + formatNumber(d.quantity) + unit;
    }
    if (d.form) {
      html += "<br><em>" + d.form + "</em>";
    }
    if (isLowConf) {
      html += "<br><span style='opacity:0.7;font-size:0.9em'>⚠ low confidence</span>";
    }
    return html;
  }

  // ── Render all streams ────────────────────────────────────────────────────
  streams.forEach(function (stream, idx) {
    const streamLabel = stream.stream_id != null ? "Stream " + stream.stream_id : null;
    const hasMining   = stream.mining   && stream.mining.length   > 0;
    const hasRefining = stream.refining && stream.refining.length > 0;

    if (!hasMining && !hasRefining) return;  // skip empty stream

    const sec = makeSection("Production share by country", streamLabel);

    // World totals callout
    const totalsEl = makeWorldTotal(stream);
    if (totalsEl) sec.appendChild(totalsEl);

    // Stacked single-column layout — mining above refining, each full width
    const grid = document.createElement("div");
    grid.style.cssText = [
      "display:grid",
      "grid-template-columns:1fr",
      "gap:1.5rem",
      "align-items:start",
    ].join(";");

    if (hasMining) {
      const miningCol = document.createElement("div");
      renderBarChart(miningCol, stream.mining, "Mining", COLOR_MINING, stream.completeness.mining);
      grid.appendChild(miningCol);
    }

    if (hasRefining) {
      const refiningCol = document.createElement("div");
      renderBarChart(refiningCol, stream.refining, "Refining", COLOR_REFINING, stream.completeness.refining);
      grid.appendChild(refiningCol);
    }

    sec.appendChild(grid);
    container.appendChild(sec);
  });

  // If all streams were empty, fall through to placeholder
  if (!container.children.length) {
    container.textContent = "No production data";
    container.classList.add("chart-placeholder");
  }
})();
