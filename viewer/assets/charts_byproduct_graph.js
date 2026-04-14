/**
 * charts_byproduct_graph.js — Byproduct dependency DAG viewer
 *
 * Reads inline JSON from <script id="byproduct-graph-data" type="application/json">
 * and renders a hierarchical SVG DAG into #byproduct-graph-root.
 *
 * Layout:   Sugiyama-style: layer 0 = primary nodes (no parents), layer 1+ = byproducts.
 *           Within each layer, nodes are sorted by mean x-position of their parents to
 *           minimize edge crossings.
 *
 * Encoding:
 *   - Circles (primaries rendered as rounded squares)
 *   - Size    = log-scaled mine output (10px – 36px radius); null → 10px
 *   - Fill    = criticality tier: tier 3 → amber, tier 4 → steel blue, else → gray
 *   - Stroke  = thick ring (3px) if us_critical == true
 *   - Arrows  = parent → child, dark gray, SVG marker arrowhead
 *
 * Interactions:
 *   - Hover node: tooltip + highlight connected edges/neighbors, dim others
 *   - Hover edge: tooltip + highlight edge + endpoints
 *   - Click node: navigate to elements/{Symbol}.html
 *   - Mouse-leave: reset opacity
 *   - Keyboard: Tab navigates nodes; Enter = highlight, Space = navigate
 */
(function () {
  "use strict";

  // ── Data ──────────────────────────────────────────────────────────────────
  const dataEl = document.getElementById("byproduct-graph-data");
  if (!dataEl) return;

  let graphData;
  try {
    graphData = JSON.parse(dataEl.textContent);
  } catch (e) {
    console.error("charts_byproduct_graph: failed to parse byproduct-graph-data JSON", e);
    return;
  }

  const root = document.getElementById("byproduct-graph-root");
  if (!root) return;

  const { nodes, edges } = graphData;
  if (!nodes || !nodes.length) {
    root.textContent = "No byproduct graph data available.";
    return;
  }

  // ── CSS custom properties ─────────────────────────────────────────────────
  const style = getComputedStyle(document.documentElement);
  const C = {
    bg:      style.getPropertyValue("--bg").trim()      || "#ffffff",
    surface: style.getPropertyValue("--surface").trim() || "#f6f7f8",
    border:  style.getPropertyValue("--border").trim()  || "#d4d8de",
    text:    style.getPropertyValue("--text").trim()    || "#1a1c1e",
    muted:   style.getPropertyValue("--muted").trim()   || "#6b7280",
    accent:  style.getPropertyValue("--accent").trim()  || "#2563eb",
  };

  // ── Node color by tier ────────────────────────────────────────────────────
  const TIER_COLOR = {
    3: "#d97706",   // amber — CRITICAL_SCARCE
    4: "#2563eb",   // steel blue — HIGH_VOLUME_WORKHORSE
  };
  const DEFAULT_COLOR = "#9ca3af"; // muted gray — niche / novelty / unknown

  function tierColor(tier) {
    return TIER_COLOR[tier] || DEFAULT_COLOR;
  }

  // ── Node size (log-scaled mine output) ────────────────────────────────────
  const MIN_R = 10;
  const MAX_R = 36;
  const mineValues = nodes.map((n) => n.mine_value).filter((v) => v != null && v > 0);
  const logScale =
    mineValues.length >= 2
      ? d3.scaleLog().domain([d3.min(mineValues), d3.max(mineValues)]).range([MIN_R, MAX_R]).clamp(true)
      : () => MIN_R;

  function nodeRadius(n) {
    if (n.mine_value == null || n.mine_value <= 0) return MIN_R;
    return logScale(n.mine_value);
  }

  // ── Build adjacency maps ───────────────────────────────────────────────────
  const nodeMap = new Map(nodes.map((n) => [n.symbol, n]));
  // children[parent] = [child, ...]
  const children = new Map(nodes.map((n) => [n.symbol, []]));
  // parents[child] = [parent, ...]
  const parents = new Map(nodes.map((n) => [n.symbol, []]));

  for (const e of edges) {
    children.get(e.source)?.push(e.target);
    parents.get(e.target)?.push(e.source);
  }

  // ── Layer assignment (topological sort / BFS from roots) ──────────────────
  const layer = new Map();
  const queue = [];
  for (const n of nodes) {
    if ((parents.get(n.symbol) || []).length === 0) {
      layer.set(n.symbol, 0);
      queue.push(n.symbol);
    }
  }
  while (queue.length) {
    const sym = queue.shift();
    const l = layer.get(sym);
    for (const child of children.get(sym) || []) {
      const existing = layer.has(child) ? layer.get(child) : -1;
      if (l + 1 > existing) {
        layer.set(child, l + 1);
        queue.push(child);
      }
    }
  }

  const numLayers = Math.max(...layer.values()) + 1;

  // ── Group nodes by layer ───────────────────────────────────────────────────
  const layerNodes = Array.from({ length: numLayers }, () => []);
  for (const n of nodes) {
    const l = layer.get(n.symbol) ?? 0;
    layerNodes[l].push(n.symbol);
  }

  // ── Crossing reduction — sort layer-1+ nodes by mean parent x ─────────────
  // We'll compute positions iteratively: first assign preliminary x in layer 0
  // (alphabetical order), then sort each subsequent layer by mean parent position.
  const pos = new Map(); // symbol → { x, y }

  // Layer 0: evenly spaced
  const baseX = (i, total) => (i + 0.5) / total;
  for (let i = 0; i < layerNodes[0].length; i++) {
    const sym = layerNodes[0][i];
    pos.set(sym, { x: baseX(i, layerNodes[0].length), y: 0 });
  }

  for (let l = 1; l < numLayers; l++) {
    // Sort layer l by mean parent x
    layerNodes[l].sort((a, b) => {
      const meanX = (sym) => {
        const ps = parents.get(sym) || [];
        if (!ps.length) return 0.5;
        return ps.reduce((s, p) => s + (pos.get(p)?.x ?? 0.5), 0) / ps.length;
      };
      return meanX(a) - meanX(b);
    });
    for (let i = 0; i < layerNodes[l].length; i++) {
      const sym = layerNodes[l][i];
      pos.set(sym, { x: baseX(i, layerNodes[l].length), y: l });
    }
  }

  // ── Layout geometry ────────────────────────────────────────────────────────
  const ROW_HEIGHT = 110;
  const SVG_WIDTH = 860;
  const SVG_HEIGHT = numLayers * ROW_HEIGHT + 40;
  const PAD_TOP = 50;

  function nodeX(sym) {
    return (pos.get(sym)?.x ?? 0.5) * SVG_WIDTH;
  }
  function nodeY(sym) {
    return PAD_TOP + (pos.get(sym)?.y ?? 0) * ROW_HEIGHT;
  }

  // ── SVG setup ─────────────────────────────────────────────────────────────
  const svg = d3
    .select(root)
    .append("svg")
    .attr("viewBox", `0 0 ${SVG_WIDTH} ${SVG_HEIGHT}`)
    .attr("width", SVG_WIDTH)
    .attr("height", SVG_HEIGHT)
    .style("overflow", "visible");

  // Arrowhead marker
  const defs = svg.append("defs");
  defs
    .append("marker")
    .attr("id", "bpg-arrow")
    .attr("viewBox", "0 0 8 8")
    .attr("refX", 7)
    .attr("refY", 4)
    .attr("markerWidth", 6)
    .attr("markerHeight", 6)
    .attr("orient", "auto-start-reverse")
    .append("path")
    .attr("d", "M0,0 L0,8 L8,4 z")
    .attr("fill", "#4b5563");

  // Highlighted arrowhead
  defs
    .append("marker")
    .attr("id", "bpg-arrow-hi")
    .attr("viewBox", "0 0 8 8")
    .attr("refX", 7)
    .attr("refY", 4)
    .attr("markerWidth", 6)
    .attr("markerHeight", 6)
    .attr("orient", "auto-start-reverse")
    .append("path")
    .attr("d", "M0,0 L0,8 L8,4 z")
    .attr("fill", C.accent);

  // ── Draw edges ─────────────────────────────────────────────────────────────
  const edgeGroup = svg.append("g").attr("class", "bpg-edges");

  // Compute an offset path for edges sharing the same source node to avoid overlap
  const edgePaths = edges.map((e) => {
    const sx = nodeX(e.source);
    const sy = nodeY(e.source);
    const tx = nodeX(e.target);
    const ty = nodeY(e.target);
    const r = nodeRadius(nodeMap.get(e.target) || {});
    // Shorten the path so it ends at the node boundary
    const angle = Math.atan2(ty - sy, tx - sx);
    const ex = tx - Math.cos(angle) * r;
    const ey = ty - Math.sin(angle) * r;
    const mx = (sx + ex) / 2;
    const my = (sy + ey) / 2 - ROW_HEIGHT * 0.1;
    return {
      e,
      d: `M${sx},${sy} Q${mx},${my} ${ex},${ey}`,
    };
  });

  const edgeSels = edgeGroup
    .selectAll("path.bpg-edge")
    .data(edgePaths)
    .enter()
    .append("path")
    .attr("class", "bpg-edge")
    .attr("d", (d) => d.d)
    .attr("fill", "none")
    .attr("stroke", "#4b5563")
    .attr("stroke-width", 1.5)
    .attr("marker-end", "url(#bpg-arrow)")
    .style("cursor", "default");

  // ── Draw nodes ─────────────────────────────────────────────────────────────
  const nodeGroup = svg.append("g").attr("class", "bpg-nodes");

  const isPrimary = (sym) => (parents.get(sym) || []).length === 0;

  const nodeSels = nodeGroup
    .selectAll("g.bpg-node")
    .data(nodes)
    .enter()
    .append("g")
    .attr("class", "bpg-node")
    .attr("transform", (n) => `translate(${nodeX(n.symbol)},${nodeY(n.symbol)})`)
    .attr("tabindex", 0)
    .attr("role", "button")
    .attr("aria-label", (n) => {
      const parents_ = n.byproduct_of || [];
      return parents_.length
        ? `${n.name} (${n.symbol}) — byproduct of ${parents_.join(", ")}`
        : `${n.name} (${n.symbol}) — primary element`;
    })
    .style("cursor", "pointer");

  // Shape: primaries = rounded squares, byproducts = circles
  nodeSels.each(function (n) {
    const g = d3.select(this);
    const r = nodeRadius(n);
    const fill = tierColor(n.tier);
    const strokeWidth = n.us_critical ? 3 : 1;
    const strokeColor = n.us_critical ? "#dc2626" : "#6b7280";

    if (isPrimary(n.symbol)) {
      // Rounded rectangle (D-shape approximation)
      const side = r * 1.6;
      g.append("rect")
        .attr("x", -side / 2)
        .attr("y", -side / 2)
        .attr("width", side)
        .attr("height", side)
        .attr("rx", 5)
        .attr("ry", 5)
        .attr("fill", fill)
        .attr("stroke", strokeColor)
        .attr("stroke-width", strokeWidth)
        .attr("class", "bpg-node-shape");
    } else {
      g.append("circle")
        .attr("r", r)
        .attr("fill", fill)
        .attr("stroke", strokeColor)
        .attr("stroke-width", strokeWidth)
        .attr("class", "bpg-node-shape");
    }

    g.append("text")
      .attr("text-anchor", "middle")
      .attr("dominant-baseline", "central")
      .attr("font-size", r < 14 ? "9px" : r < 20 ? "11px" : "13px")
      .attr("font-weight", "700")
      .attr("fill", "#fff")
      .attr("pointer-events", "none")
      .text(n.symbol);
  });

  // ── Tooltip ────────────────────────────────────────────────────────────────
  const tooltip = document.getElementById("byproduct-tooltip");

  function formatValue(v) {
    if (v == null) return "no data";
    if (v >= 1_000_000) return (v / 1_000_000).toFixed(1) + " Mt/yr";
    if (v >= 1_000) return (v / 1_000).toFixed(0) + " kt/yr";
    return v.toFixed(1) + " t/yr";
  }

  function showNodeTooltip(event, n) {
    if (!tooltip) return;
    const parents_ = n.byproduct_of || [];
    const criticality = [n.us_critical ? "US Critical" : null, n.eu_crm ? "EU CRM" : null, n.eu_strategic ? "EU Strategic" : null]
      .filter(Boolean)
      .join(", ");

    // Re tooltip for Re ← Mo ← Cu chain: add contextual note
    let moNote = "";
    if (n.symbol === "Re" && parents_.includes("Mo")) {
      moNote =
        '<div class="byproduct-tooltip-row" style="margin-top:0.35rem;font-style:italic">Also recovered indirectly via Mo, which is itself partly a Cu byproduct.</div>';
    }

    tooltip.innerHTML = `
      <div class="byproduct-tooltip-title">${n.symbol} &mdash; ${n.name}</div>
      <div class="byproduct-tooltip-row"><strong>Tier:</strong> ${n.tier ?? "?"}</div>
      ${criticality ? `<div class="byproduct-tooltip-row"><strong>Criticality:</strong> ${criticality}</div>` : ""}
      <div class="byproduct-tooltip-row"><strong>Mine output:</strong> ${formatValue(n.mine_value)}</div>
      <div class="byproduct-tooltip-row"><strong>Supply dependency:</strong> ${
        parents_.length ? "byproduct of " + parents_.join(", ") : "primary — no byproduct dependency"
      }</div>
      ${moNote}
      <div class="byproduct-tooltip-row" style="margin-top:0.35rem;font-size:0.75rem;opacity:0.7">Click to open element page</div>
    `;
    positionTooltip(event);
    tooltip.removeAttribute("hidden");
  }

  function showEdgeTooltip(event, ep) {
    if (!tooltip) return;
    const src = nodeMap.get(ep.e.source);
    const tgt = nodeMap.get(ep.e.target);
    tooltip.innerHTML = `
      <div class="byproduct-tooltip-title">${tgt?.symbol ?? ep.e.target} is a byproduct of ${src?.symbol ?? ep.e.source}</div>
      <div class="byproduct-tooltip-row">${tgt?.name ?? ""} cannot be mined independently — its supply is governed by ${src?.name ?? ""} economics.</div>
    `;
    positionTooltip(event);
    tooltip.removeAttribute("hidden");
  }

  function hideTooltip() {
    if (tooltip) tooltip.setAttribute("hidden", "");
  }

  function positionTooltip(event) {
    if (!tooltip) return;
    const W = window.innerWidth;
    const TW = tooltip.offsetWidth || 300;
    let x = event.clientX + 14;
    let y = event.clientY - 10;
    if (x + TW > W - 10) x = event.clientX - TW - 14;
    tooltip.style.left = x + "px";
    tooltip.style.top = y + "px";
  }

  // ── Highlight helpers ──────────────────────────────────────────────────────
  const DIM = 0.12;

  function highlightNode(sym) {
    const connected = new Set([sym]);
    const connectedEdges = new Set();
    for (let i = 0; i < edges.length; i++) {
      const e = edges[i];
      if (e.source === sym || e.target === sym) {
        connected.add(e.source);
        connected.add(e.target);
        connectedEdges.add(i);
      }
    }
    nodeSels.style("opacity", (n) => (connected.has(n.symbol) ? 1 : DIM));
    edgeSels
      .style("opacity", (_, i) => (connectedEdges.has(i) ? 1 : DIM))
      .attr("stroke", (_, i) => (connectedEdges.has(i) ? C.accent : "#4b5563"))
      .attr("marker-end", (_, i) => (connectedEdges.has(i) ? "url(#bpg-arrow-hi)" : "url(#bpg-arrow)"))
      .attr("stroke-width", (_, i) => (connectedEdges.has(i) ? 2.5 : 1.5));
  }

  function highlightEdge(edgeIdx) {
    const e = edges[edgeIdx];
    const connected = new Set([e.source, e.target]);
    nodeSels.style("opacity", (n) => (connected.has(n.symbol) ? 1 : DIM));
    edgeSels
      .style("opacity", (_, i) => (i === edgeIdx ? 1 : DIM))
      .attr("stroke", (_, i) => (i === edgeIdx ? C.accent : "#4b5563"))
      .attr("marker-end", (_, i) => (i === edgeIdx ? "url(#bpg-arrow-hi)" : "url(#bpg-arrow)"))
      .attr("stroke-width", (_, i) => (i === edgeIdx ? 2.5 : 1.5));
  }

  function resetHighlight() {
    nodeSels.style("opacity", 1);
    edgeSels
      .style("opacity", 1)
      .attr("stroke", "#4b5563")
      .attr("marker-end", "url(#bpg-arrow)")
      .attr("stroke-width", 1.5);
  }

  // ── Node interactions ──────────────────────────────────────────────────────
  nodeSels
    .on("mouseenter", function (event, n) {
      highlightNode(n.symbol);
      showNodeTooltip(event, n);
    })
    .on("mousemove", (event) => {
      positionTooltip(event);
    })
    .on("mouseleave", () => {
      resetHighlight();
      hideTooltip();
    })
    .on("click", (event, n) => {
      window.location.href = `elements/${n.symbol}.html`;
    })
    .on("keydown", function (event, n) {
      if (event.key === "Enter") {
        highlightNode(n.symbol);
        showNodeTooltip(event, n);
      } else if (event.key === " ") {
        event.preventDefault();
        window.location.href = `elements/${n.symbol}.html`;
      }
    })
    .on("blur", () => {
      resetHighlight();
      hideTooltip();
    });

  // ── Edge interactions ──────────────────────────────────────────────────────
  edgeSels
    .on("mouseenter", function (event, ep, i) {
      const idx = edgePaths.indexOf(ep);
      highlightEdge(idx);
      showEdgeTooltip(event, ep);
    })
    .on("mousemove", (event) => {
      positionTooltip(event);
    })
    .on("mouseleave", () => {
      resetHighlight();
      hideTooltip();
    });

  // ── Legend ─────────────────────────────────────────────────────────────────
  const legendEl = document.createElement("div");
  legendEl.className = "byproduct-legend";
  legendEl.innerHTML = `
    <span class="byproduct-legend-item">
      <span class="byproduct-legend-swatch-sq" style="background:#d97706"></span>
      Critical / scarce (tier 3)
    </span>
    <span class="byproduct-legend-item">
      <span class="byproduct-legend-swatch" style="background:#2563eb"></span>
      Workhorse (tier 4)
    </span>
    <span class="byproduct-legend-item">
      <span class="byproduct-legend-swatch" style="background:#9ca3af"></span>
      Niche / novelty
    </span>
    <span class="byproduct-legend-item">
      <span class="byproduct-legend-swatch" style="background:#dc2626;border-radius:50%;outline:3px solid #dc2626;outline-offset:2px"></span>
      US critical minerals list
    </span>
    <span class="byproduct-legend-item">
      <span class="byproduct-legend-swatch-sq" style="background:#6b7280"></span>
      Primary node (no byproduct dependency)
    </span>
    <span class="byproduct-legend-item">
      <span class="byproduct-legend-swatch" style="background:#2563eb"></span>
      Byproduct node (circle)
    </span>
    <span class="byproduct-legend-item" style="font-size:0.75rem">
      Circle size = mine output (log scale)
    </span>
  `;
  root.parentNode.insertBefore(legendEl, root.nextSibling);

  // ── Layer labels ───────────────────────────────────────────────────────────
  const labelGroup = svg.append("g").attr("class", "bpg-labels");
  const layerLabels = ["Primary metals", "Byproduct (1-hop)", "Byproduct (2-hop)"];
  for (let l = 0; l < numLayers; l++) {
    labelGroup
      .append("text")
      .attr("x", 4)
      .attr("y", PAD_TOP + l * ROW_HEIGHT - 18)
      .attr("font-size", "10px")
      .attr("fill", C.muted)
      .attr("font-style", "italic")
      .text(layerLabels[l] || `Layer ${l}`);
  }
})();
