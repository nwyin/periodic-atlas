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

        // ── Axis SVG (numbered dots only; event text lives in the HTML list below) ──
        var margin = { top: 14, right: 24, bottom: 28, left: 24 };
        var containerW = parent.getBoundingClientRect().width || 700;
        var svgWidth = Math.min(Math.max(containerW, 400), 840);
        var width = svgWidth - margin.left - margin.right;
        var axisY = 24;
        var svgHeight = margin.top + axisY + margin.bottom;

        var allDates = sorted.map(function (e) { return parseEventDate(e.date); });
        var minD = d3.min(allDates);
        var maxD = d3.max(allDates);
        var span = maxD - minD;
        var pad = span > 0 ? span * 0.14 : 1000 * 60 * 60 * 24 * 180;

        var x = d3.scaleTime()
            .domain([new Date(+minD - pad), new Date(+maxD + pad)])
            .range([0, width]);

        var svgWrap = d3.select(parent)
            .append("svg")
                .attr("width", "100%")
                .attr("viewBox", "0 0 " + svgWidth + " " + svgHeight)
                .attr("preserveAspectRatio", "xMidYMid meet")
                .style("display", "block")
                .style("max-width", svgWidth + "px")
                .attr("role", "img")
                .attr("aria-label", "Geopolitical events timeline");

        var svg = svgWrap.append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        svg.append("g")
            .attr("transform", "translate(0," + axisY + ")")
            .call(
                d3.axisBottom(x)
                    .tickFormat(d3.timeFormat("%Y"))
                    .ticks(Math.min(sorted.length + 2, 8))
            );

        // Numbered dots on axis; each one is linked to its list-item below via data-evt-idx
        var dotSel = [];
        sorted.forEach(function (ev, i) {
            var xPos = x(parseEventDate(ev.date));
            var num = i + 1;

            var group = svg.append("g")
                .attr("class", "evt-dot")
                .attr("data-evt-idx", num)
                .style("cursor", "pointer");

            group.append("circle")
                .attr("cx", xPos)
                .attr("cy", axisY)
                .attr("r", 9)
                .attr("fill", "var(--accent, #2563eb)")
                .attr("stroke", "var(--bg, #fff)")
                .attr("stroke-width", 2);

            group.append("text")
                .attr("x", xPos)
                .attr("y", axisY)
                .attr("text-anchor", "middle")
                .attr("dy", "0.35em")
                .attr("font-size", "10px")
                .attr("font-weight", "600")
                .attr("fill", "#fff")
                .style("pointer-events", "none")
                .text(num);

            group
                .on("mouseover", function (event) {
                    showTooltip(event,
                        ev.date + "\n" + ev.event +
                        (ev.impact ? "\n\n" + ev.impact : "")
                    );
                    highlight(num, true);
                })
                .on("mousemove", function (event) {
                    showTooltip(event,
                        ev.date + "\n" + ev.event +
                        (ev.impact ? "\n\n" + ev.impact : "")
                    );
                })
                .on("mouseout", function () {
                    hideTooltip();
                    highlight(num, false);
                });

            dotSel.push(group);
        });

        // ── Event list (HTML, wraps naturally; no SVG clipping) ──────────────────
        var list = d3.select(parent)
            .append("ol")
                .attr("class", "events-list")
                .style("list-style", "none")
                .style("padding", "0")
                .style("margin", "0.75rem 0 0")
                .style("font-size", "0.88rem")
                .style("line-height", "1.45");

        sorted.forEach(function (ev, i) {
            var num = i + 1;
            var item = list.append("li")
                .attr("data-evt-idx", num)
                .style("display", "grid")
                .style("grid-template-columns", "1.8rem 5.5rem 1fr")
                .style("gap", "0.6rem")
                .style("padding", "0.55rem 0.5rem")
                .style("border-top", "1px solid var(--border, #e5e7eb)")
                .style("align-items", "baseline")
                .style("transition", "background 0.12s");

            item.append("span")
                .style("display", "inline-flex")
                .style("width", "1.4rem")
                .style("height", "1.4rem")
                .style("border-radius", "50%")
                .style("background", "var(--accent, #2563eb)")
                .style("color", "#fff")
                .style("font-size", "0.75rem")
                .style("font-weight", "600")
                .style("align-items", "center")
                .style("justify-content", "center")
                .style("flex-shrink", "0")
                .text(num);

            item.append("span")
                .style("font-variant-numeric", "tabular-nums")
                .style("color", "var(--muted, #6b7280)")
                .style("font-size", "0.82rem")
                .text(ev.date);

            var body = item.append("div");
            body.append("div")
                .style("font-weight", "500")
                .text(ev.event);
            if (ev.impact) {
                body.append("div")
                    .style("margin-top", "0.25rem")
                    .style("color", "var(--muted, #6b7280)")
                    .style("font-size", "0.83rem")
                    .text(ev.impact);
            }

            item
                .on("mouseover", function () { highlight(num, true); })
                .on("mouseout",  function () { highlight(num, false); });
        });

        function highlight(num, on) {
            svgWrap.selectAll(".evt-dot circle")
                .attr("r", function () {
                    var idx = +this.parentNode.getAttribute("data-evt-idx");
                    return (on && idx === num) ? 11 : 9;
                });
            list.selectAll("li")
                .style("background", function () {
                    var idx = +this.getAttribute("data-evt-idx");
                    return (on && idx === num) ? "var(--surface, #f6f7f8)" : "transparent";
                });
        }
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
