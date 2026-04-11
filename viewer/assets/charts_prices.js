// viewer/assets/charts_prices.js
// B3 viewer: price timeline + geopolitical events timeline
//
// Unit normalisation (pre-applied in build_viewer.py before JSON injection):
//   usd_per_lb → usd_per_kg   using   1 lb = 0.4536 kg
//   i.e.  price_per_kg = price_per_lb / 0.4536  (≈ × 2.2046)
//   Rationale: usd_per_kg is the SI-adjacent unit preferred by USGS tables.
//   This normalises series that would otherwise share an x-axis but have
//   mismatched y-axis units, making multi-series charts directly comparable.
//
// Data source: <script type="application/json" id="atlas-chart-data">
// Expected shape: { "prices": [{year, value, unit, form, basis, region}, ...],
//                  "events": [{date, event, impact}, ...] }

document.addEventListener("DOMContentLoaded", function () {
    "use strict";

    var dataEl = document.getElementById("atlas-chart-data");
    if (!dataEl) return;

    var data;
    try {
        data = JSON.parse(dataEl.textContent);
    } catch (_) {
        return;
    }

    var prices = Array.isArray(data.prices) ? data.prices : [];
    var events = Array.isArray(data.events) ? data.events : [];

    var container = document.getElementById("prices-chart");
    if (!container) return;

    // Clear placeholder text; remove dashed-border class
    container.innerHTML = "";
    container.classList.remove("chart-placeholder");

    // ── Price history section ────────────────────────────────────────────────
    var priceSection = _section(container, "Price History");

    if (prices.length === 0) {
        _emptyState(priceSection, "No price history");
    } else {
        renderPricesChart(priceSection, prices);
    }

    // ── Events timeline section ──────────────────────────────────────────────
    var eventsSection = _section(container, "Geopolitical Events");
    eventsSection.style.marginTop = "2rem";

    if (events.length === 0) {
        _emptyState(eventsSection, "No geopolitical events recorded");
    } else {
        renderEventsTimeline(eventsSection, events);
    }


    // ────────────────────────────────────────────────────────────────────────
    // Prices line chart
    // ────────────────────────────────────────────────────────────────────────
    function renderPricesChart(parent, prices) {
        var margin = { top: 20, right: 175, bottom: 45, left: 72 };
        var containerW = parent.getBoundingClientRect().width || 700;
        var totalW = Math.min(Math.max(containerW, 400), 840);
        var width = totalW - margin.left - margin.right;
        var height = 260 - margin.top - margin.bottom;

        // Group by "basis / region" key — each group is one line
        var groups = d3.group(prices, function (d) { return d.basis + " / " + d.region; });
        var groupKeys = Array.from(groups.keys()).sort();
        var color = d3.scaleOrdinal(d3.schemeTableau10).domain(groupKeys);

        var years = prices.map(function (d) { return d.year; });
        var x = d3.scaleLinear()
            .domain([d3.min(years) - 0.4, d3.max(years) + 0.4])
            .range([0, width]);

        var y = d3.scaleLinear()
            .domain([0, d3.max(prices, function (d) { return d.value; }) * 1.15])
            .nice()
            .range([height, 0]);

        var svg = d3.select(parent)
            .append("svg")
                .attr("width", totalW)
                .attr("height", height + margin.top + margin.bottom)
                .attr("role", "img")
                .attr("aria-label", "Price history line chart")
            .append("g")
                .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        // Subtle horizontal grid
        svg.append("g")
            .attr("class", "grid")
            .call(
                d3.axisLeft(y)
                    .ticks(5)
                    .tickSize(-width)
                    .tickFormat("")
            )
            .call(function (g) { g.select(".domain").remove(); })
            .selectAll(".tick line")
                .attr("stroke", "var(--border, #d4d8de)")
                .attr("stroke-dasharray", "3,3");

        // X axis — integer year labels
        svg.append("g")
            .attr("transform", "translate(0," + height + ")")
            .call(
                d3.axisBottom(x)
                    .tickFormat(d3.format("d"))
                    .ticks(Math.min(years.length, 8))
            );

        // Y axis
        svg.append("g")
            .call(d3.axisLeft(y));

        // Y-axis unit label
        var yUnit = prices[0].unit;
        svg.append("text")
            .attr("transform", "rotate(-90)")
            .attr("y", -58)
            .attr("x", -(height / 2))
            .attr("text-anchor", "middle")
            .attr("font-size", "11px")
            .attr("fill", "currentColor")
            .text(yUnit);

        // One line + dots per (basis, region) group
        var lineGen = d3.line()
            .x(function (d) { return x(d.year); })
            .y(function (d) { return y(d.value); })
            .defined(function (d) { return d.value != null; });

        groupKeys.forEach(function (key) {
            var pts = groups.get(key);
            var sorted = pts.slice().sort(function (a, b) { return a.year - b.year; });

            svg.append("path")
                .datum(sorted)
                .attr("fill", "none")
                .attr("stroke", color(key))
                .attr("stroke-width", 2.2)
                .attr("d", lineGen);

            svg.selectAll(null)
                .data(sorted)
                .join("circle")
                    .attr("cx", function (d) { return x(d.year); })
                    .attr("cy", function (d) { return y(d.value); })
                    .attr("r", 4.5)
                    .attr("fill", color(key))
                    .attr("stroke", "var(--bg, #fff)")
                    .attr("stroke-width", 1.5)
                    .style("cursor", "crosshair")
                    .on("mouseover", function (event, d) {
                        showTooltip(event,
                            d.year + "  \u2192  " + d.value + " " + d.unit +
                            "\nform: " + d.form +
                            "\nbasis: " + d.basis + " / region: " + d.region
                        );
                    })
                    .on("mouseout", hideTooltip);
        });

        // Legend (right side)
        groupKeys.forEach(function (key, i) {
            var ly = i * 20;
            svg.append("rect")
                .attr("x", width + 14)
                .attr("y", ly)
                .attr("width", 12)
                .attr("height", 12)
                .attr("rx", 2)
                .attr("fill", color(key));
            svg.append("text")
                .attr("x", width + 30)
                .attr("y", ly + 10)
                .attr("font-size", "11px")
                .attr("fill", "currentColor")
                .text(key);
        });
    }


    // ────────────────────────────────────────────────────────────────────────
    // Events timeline
    // ────────────────────────────────────────────────────────────────────────

    function parseEventDate(s) {
        // yyyy-mm-dd → exact date
        if (/^\d{4}-\d{2}-\d{2}$/.test(s)) return new Date(s + "T12:00:00");
        // yyyy-mm  → month midpoint (day 15); see task spec for rationale
        if (/^\d{4}-\d{2}$/.test(s)) {
            var parts = s.split("-");
            return new Date(parseInt(parts[0]), parseInt(parts[1]) - 1, 15);
        }
        // yyyy → July 1 (calendar midpoint)
        if (/^\d{4}$/.test(s)) return new Date(parseInt(s), 6, 1);
        return new Date(s);
    }

    function renderEventsTimeline(parent, events) {
        // Sort chronologically (INV-2)
        var sorted = events.slice().sort(function (a, b) {
            return parseEventDate(a.date) - parseEventDate(b.date);
        });

        var margin = { top: 30, right: 20, bottom: 30, left: 20 };
        var containerW = parent.getBoundingClientRect().width || 700;
        var svgWidth = Math.min(Math.max(containerW, 400), 840);
        var width = svgWidth - margin.left - margin.right;

        // Axis at fixed y; label rows stacked below
        var axisY = 20;
        var labelRowH = 22;
        var svgHeight = margin.top + axisY + 20 + sorted.length * labelRowH + margin.bottom;

        var allDates = sorted.map(function (e) { return parseEventDate(e.date); });
        var minD = d3.min(allDates);
        var maxD = d3.max(allDates);
        var span = maxD - minD;
        // Pad domain so single events don't collide with axis ends
        var pad = span > 0 ? span * 0.14 : 1000 * 60 * 60 * 24 * 180;

        var x = d3.scaleTime()
            .domain([new Date(+minD - pad), new Date(+maxD + pad)])
            .range([0, width]);

        var svg = d3.select(parent)
            .append("svg")
                .attr("width", svgWidth)
                .attr("height", svgHeight)
                .attr("role", "img")
                .attr("aria-label", "Geopolitical events timeline")
            .append("g")
                .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        // Time axis
        svg.append("g")
            .attr("transform", "translate(0," + axisY + ")")
            .call(
                d3.axisBottom(x)
                    .tickFormat(d3.timeFormat("%Y"))
                    .ticks(Math.min(sorted.length + 2, 8))
            );

        sorted.forEach(function (ev, i) {
            var xPos = x(parseEventDate(ev.date));
            var shortLabel = ev.date + ": " +
                (ev.event.length > 60 ? ev.event.slice(0, 60) + "\u2026" : ev.event);
            var labelY = axisY + 28 + i * labelRowH;

            // Tick mark on axis
            svg.append("line")
                .attr("x1", xPos).attr("x2", xPos)
                .attr("y1", axisY - 6).attr("y2", axisY + 6)
                .attr("stroke", "var(--accent, #2563eb)")
                .attr("stroke-width", 2);

            // Dot
            svg.append("circle")
                .attr("cx", xPos)
                .attr("cy", axisY)
                .attr("r", 6)
                .attr("fill", "var(--accent, #2563eb)")
                .attr("stroke", "var(--bg, #fff)")
                .attr("stroke-width", 2)
                .style("cursor", "pointer")
                .on("mouseover", function (event) {
                    showTooltip(event,
                        ev.date + "\n" + ev.event +
                        (ev.impact ? "\n\n" + ev.impact : "")
                    );
                })
                .on("mouseout", hideTooltip);

            // Connector line from dot to label row
            svg.append("line")
                .attr("x1", xPos).attr("x2", xPos)
                .attr("y1", axisY + 8).attr("y2", labelY - 6)
                .attr("stroke", "var(--border, #d4d8de)")
                .attr("stroke-width", 1)
                .attr("stroke-dasharray", "3,2");

            // Label text (left-aligned for readability)
            svg.append("text")
                .attr("x", 0)
                .attr("y", labelY)
                .attr("font-size", "11px")
                .attr("fill", "currentColor")
                .text(shortLabel);
        });
    }


    // ────────────────────────────────────────────────────────────────────────
    // Helpers
    // ────────────────────────────────────────────────────────────────────────

    function _section(parent, title) {
        var div = document.createElement("div");
        div.className = "chart-section";
        var h = document.createElement("h3");
        h.style.cssText = "margin:0 0 0.5rem;font-size:1rem;font-weight:600;";
        h.textContent = title;
        div.appendChild(h);
        parent.appendChild(div);
        return div;
    }

    function _emptyState(parent, msg) {
        var p = document.createElement("p");
        p.className = "empty-state";
        p.style.cssText = "color:var(--muted,#6b7280);font-style:italic;margin:0.25rem 0;";
        p.textContent = msg;
        parent.appendChild(p);
    }

    var _tooltip = null;

    function ensureTooltip() {
        if (!_tooltip) {
            _tooltip = d3.select("body")
                .append("div")
                    .style("position", "fixed")
                    .style("pointer-events", "none")
                    .style("background", "rgba(15,17,23,0.92)")
                    .style("color", "#e8eaf0")
                    .style("font-size", "12px")
                    .style("line-height", "1.5")
                    .style("padding", "8px 12px")
                    .style("border-radius", "5px")
                    .style("white-space", "pre-wrap")
                    .style("max-width", "360px")
                    .style("box-shadow", "0 2px 8px rgba(0,0,0,0.4)")
                    .style("opacity", "0")
                    .style("z-index", "9999")
                    .style("transition", "opacity 0.1s");
        }
        return _tooltip;
    }

    function showTooltip(event, text) {
        ensureTooltip()
            .text(text)
            .style("opacity", "1")
            .style("left", (event.clientX + 14) + "px")
            .style("top", (event.clientY - 36) + "px");
    }

    function hideTooltip() {
        if (_tooltip) _tooltip.style("opacity", "0");
    }
});
