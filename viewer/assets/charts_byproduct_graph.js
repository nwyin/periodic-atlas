// Each marked intersection represents one recorded host-to-byproduct link.
(() => {
  const root = document.getElementById("byproduct-graph-root");
  const payload = document.getElementById("byproduct-graph-data");
  if (!root || !payload) return;
  const {nodes, edges} = JSON.parse(payload.textContent);
  if (!edges.length) {
    root.textContent = "No byproduct relationships recorded.";
    return;
  }

  const elements = new Map(nodes.map(node => [node.symbol, node]));
  const productsOf = new Map();
  const hostsOf = new Map();
  for (const {source, target} of edges) {
    if (!productsOf.has(source)) productsOf.set(source, new Set());
    if (!hostsOf.has(target)) hostsOf.set(target, new Set());
    productsOf.get(source).add(target);
    hostsOf.get(target).add(source);
  }

  function ranked(groups) {
    return Array.from(groups.keys()).sort((a, b) => groups.get(b).size - groups.get(a).size
      || elements.get(a).name.localeCompare(elements.get(b).name));
  }
  const hosts = ranked(productsOf);
  const products = ranked(hostsOf);
  function tag(name, className, text) {
    const el = document.createElement(name);
    if (className) el.className = className;
    if (text !== undefined) el.textContent = text;
    return el;
  }
  function elementLink(symbol) {
    const link = tag("a", "", elements.get(symbol).name);
    link.href = 'elements/' + encodeURIComponent(symbol) + '.html';
    return link;
  }

  const counts = tag("strong", "dependency-summary", edges.length + " links · " + hosts.length + " hosts · " + products.length + " byproducts");
  const viewport = tag("div", "dependency-scroll");
  viewport.tabIndex = 0;
  viewport.setAttribute("role", "region");
  viewport.setAttribute("aria-label", "Scrollable host and byproduct matrix");

  const table = tag("table", "dependency-matrix");
  table.setAttribute("aria-label", "Recorded byproduct relationships, most connections first");
  const head = table.createTHead().insertRow();
  const corner = tag("th", "dependency-corner", "Host ↓");
  corner.append(tag("small", "", "Byproduct →"));
  head.append(corner);
  const columns = new Map();
  for (const symbol of products) {
    const th = tag("th");
    th.scope = "col";
    th.append(tag("strong", "", symbol), tag("small", "", elements.get(symbol).name));
    columns.set(symbol, th);
    head.append(th);
  }
  const body = table.createTBody();
  const detail = tag("div", "dependency-detail");
  detail.setAttribute("aria-live", "polite");
  let selected;

  function select(button, host, product) {
    if (selected) {
      selected.button.setAttribute("aria-pressed", "false");
      selected.row.classList.remove("is-selected");
      selected.column.classList.remove("is-selected");
    }
    const row = button.closest("tr");
    const column = columns.get(product);
    selected = {button, row, column};
    row.classList.add("is-selected");
    column.classList.add("is-selected");
    button.setAttribute("aria-pressed", "true");
    const pair = tag("strong", "dependency-pair");
    pair.append(elementLink(host), " → ", elementLink(product));
    const others = hosts.filter(symbol => symbol !== host && hostsOf.get(product).has(symbol));
    const note = tag("span", "", others.length ? "Other recorded hosts include " : "Only recorded host in this atlas.");
    others.forEach((symbol, i) => {
      if (i) note.append(i === others.length - 1 ? " and " : ", ");
      note.append(elementLink(symbol));
    });
    if (others.length) note.append(".");
    detail.replaceChildren(pair, note);
  }

  for (const host of hosts) {
    const row = body.insertRow();
    const label = tag("th");
    label.scope = "row";
    const count = tag("span", "dependency-count", productsOf.get(host).size);
    count.title = productsOf.get(host).size + " recorded byproducts";
    label.append(tag("strong", "", host), " " + elements.get(host).name, count);
    row.append(label);
    for (const product of products) {
      const cell = row.insertCell();
      if (!productsOf.get(host).has(product)) continue;
      const button = tag("button", "dependency-mark");
      button.type = "button";
      button.title = elements.get(product).name + " can be recovered alongside " + elements.get(host).name;
      button.setAttribute("aria-label", button.title);
      button.setAttribute("aria-pressed", "false");
      button.addEventListener("click", () => select(button, host, product));
      cell.append(button);
      if (!selected) select(button, host, product);
    }
  }
  viewport.append(table);
  root.replaceChildren(counts, viewport, detail);
})();
