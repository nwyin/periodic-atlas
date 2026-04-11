// viewer/assets/charts_isotopes.js
// B5 viewer: isotope markets panel
//
// Reads inline JSON from <script id="isotope-data" type="application/json">
// Expected shape per item:
//   { isotope, half_life_seconds, half_life_display, production_mode,
//     precursor, delivery_form, reporting_year,
//     production_quantity: {value, unit},
//     producers: [{country, share_pct, confidence, notes}, ...],
//     producers_completeness, notes }
//
// The server-side renderer already generates a static HTML table for each
// isotope card. This script optionally enhances the producers section with
// an SVG horizontal bar chart (for elements with ≥ 4 producers) or leaves
// the static table in place.

document.addEventListener("DOMContentLoaded", function () {
    "use strict";

    var dataEl = document.getElementById("isotope-data");
    if (!dataEl) return;

    var isotopes;
    try {
        isotopes = JSON.parse(dataEl.textContent);
    } catch (_) {
        return;
    }

    if (!Array.isArray(isotopes) || isotopes.length === 0) return;

    var style = getComputedStyle(document.documentElement);
    var C = {
        accent:  (style.getPropertyValue("--accent")  || "#2563eb").trim(),
        muted:   (style.getPropertyValue("--muted")   || "#6b7280").trim(),
        border:  (style.getPropertyValue("--border")  || "#d4d8de").trim(),
        text:    (style.getPropertyValue("--text")    || "#1a1c1e").trim(),
        surface: (style.getPropertyValue("--surface") || "#f6f7f8").trim(),
    };

    // Mode badge color mapping (mirrors atlas.css badge-mode-* classes)
    var MODE_COLORS = {
        stockpile_separated:   "#7c3aed",
        reactor_generated:     "#0369a1",
        accelerator_generated: "#b45309",
        decay_product:         "#059669",
        naturally_occurring:   "#6b7280",
    };

    // ── For each isotope, optionally enhance the producers section ────────────
    isotopes.forEach(function (iso) {
        var producers = Array.isArray(iso.producers) ? iso.producers : [];
        if (producers.length < 4) return; // small lists: keep static table

        // Find the producers-chart container for this isotope
        var chartDiv = document.querySelector(".producers-chart[data-isotope='" + iso.isotope + "']");
        if (!chartDiv) return;

        // Build SVG horizontal bar chart with d3
        renderProducersBarChart(chartDiv, producers, iso.isotope);
    });


    // ──────────────────────────────────────────────────────────────��─────────
    // SVG horizontal bar chart for producer shares
    // ────────────────────────────────────────────────────────────────────────
    function renderProducersBarChart(container, producers, isotopeName) {
        if (typeof d3 === "undefined") return; // d3 not loaded

        container.innerHTML = "";

        var margin = { top: 8, right: 60, bottom: 20, left: 48 };
        var containerW = container.getBoundingClientRect().width || 500;
        var totalW = Math.min(Math.max(containerW, 280), 620);
        var barH = 22;
        var gap = 4;
        var height = producers.length * (barH + gap) - gap;
        var width = totalW - margin.left - margin.right;

        var x = d3.scaleLinear()
            .domain([0, 100])
            .range([0, width]);

        var svg = d3.select(container).append("svg")
            .attr("width", totalW)
            .attr("height", height + margin.top + margin.bottom);

        var g = svg.append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        // Grid lines at 25%, 50%, 75%
        [25, 50, 75].forEach(function (pct) {
            g.append("line")
                .attr("x1", x(pct)).attr("x2", x(pct))
                .attr("y1", 0).attr("y2", height)
                .attr("stroke", C.border)
                .attr("stroke-dasharray", "3 3")
                .attr("stroke-width", 1);
        });

        // Bars
        producers.forEach(function (p, i) {
            var y = i * (barH + gap);
            var isLow = p.confidence === "low";
            var pct = p.share_pct != null ? p.share_pct : 0;

            // Bar rect
            var rect = g.append("rect")
                .attr("x", 0)
                .attr("y", y)
                .attr("width", x(pct))
                .attr("height", barH)
                .attr("fill", C.accent)
                .attr("rx", 3);

            if (isLow) {
                rect.attr("opacity", 0.55);
                rect.attr("stroke", C.border).attr("stroke-dasharray", "4 2").attr("stroke-width", 1.5);
            }

            // Country label
            g.append("text")
                .attr("x", -6)
                .attr("y", y + barH / 2 + 4)
                .attr("text-anchor", "end")
                .attr("font-size", "0.75rem")
                .attr("fill", isLow ? C.muted : C.text)
                .attr("font-style", isLow ? "italic" : "normal")
                .text(p.country || "?");

            // Pct label at end of bar
            if (pct > 0) {
                g.append("text")
                    .attr("x", x(pct) + 4)
                    .attr("y", y + barH / 2 + 4)
                    .attr("font-size", "0.72rem")
                    .attr("fill", isLow ? C.muted : C.text)
                    .text(pct.toFixed(0) + "%");
            }
        });

        // X-axis
        g.append("line")
            .attr("x1", 0).attr("x2", width)
            .attr("y1", height + 4).attr("y2", height + 4)
            .attr("stroke", C.border).attr("stroke-width", 1);

        g.append("text")
            .attr("x", width / 2)
            .attr("y", height + margin.bottom)
            .attr("text-anchor", "middle")
            .attr("font-size", "0.72rem")
            .attr("fill", C.muted)
            .text("Share (%)");
    }
});
