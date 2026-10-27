// Contradiction matrix lookup. Data comes from data.json, built by
// tools/build_site.py from skills/triz/data.

(async function () {
  const $ = (id) => document.getElementById(id);
  const data = await (await fetch("data.json")).json();
  const params = new Map(data.parameters.map((p) => [p.id, p]));
  const principles = new Map(data.principles.map((p) => [p.id, p]));
  const label = (p) => `${p.id}. ${p.name}`;

  $("params").innerHTML = data.parameters
    .map((p) => `<option value="${label(p)}">${p.aliases.join(", ")}</option>`)
    .join("");

  // Accept "25", "25. Loss of time", a name or an alias.
  function resolve(text) {
    const t = text.trim().toLowerCase();
    if (!t) return null;
    const n = parseInt(t, 10);
    if (params.has(n)) return params.get(n);
    return (
      data.parameters.find((p) => p.name.toLowerCase() === t) ||
      data.parameters.find((p) => p.aliases.some((a) => a.toLowerCase() === t)) ||
      data.parameters.find((p) => p.name.toLowerCase().includes(t)) ||
      data.parameters.find((p) => p.aliases.some((a) => a.toLowerCase().includes(t))) ||
      null
    );
  }

  const esc = (s) => s.replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);

  function card(id) {
    const p = principles.get(id);
    const ex = ["software", "business", "engineering", "everyday"]
      .filter((k) => p.examples[k])
      .map((k) => `<li><b>${k[0].toUpperCase() + k.slice(1)}:</b> ${esc(p.examples[k])}</li>`)
      .join("");
    return `<article class="card"><h3><span class="num">#${id}</span> <a href="${p.page}">${esc(p.name)}</a></h3>
<p>${esc(p.subprinciples[0])}</p><ul class="ex">${ex}</ul></article>`;
  }

  function render() {
    const a = resolve($("improve").value);
    const b = resolve($("worsen").value);
    const out = $("result");
    if (!a || !b) {
      out.innerHTML = "";
      return;
    }
    const key = `${a.id}-${b.id}`;
    history.replaceState(null, "", `?improve=${a.id}&worsen=${b.id}`);
    let head = `<h2>Improving <em>${esc(a.name)}</em> worsens <em>${esc(b.name)}</em></h2>
<p class="defs"><b>${esc(a.name)}:</b> ${esc(a.definition)}<br><b>${esc(b.name)}:</b> ${esc(b.definition)}</p>`;
    if (a.id === b.id) {
      out.innerHTML = head + `<p class="note">The same parameter on both sides is a physical contradiction: the thing must be one way and the opposite. Separate the two needs in time, in space, by condition, or between the whole and its parts.</p>`;
      return;
    }
    const ids = data.matrix[key] || [];
    if (!ids.length) {
      out.innerHTML = head + `<p class="note">The matrix has no suggestion for this pair. Try a nearby parameter, or swap the two.</p>`;
      return;
    }
    if (key in data.disputed) {
      const other = data.disputed[key];
      head += `<p class="note">Disputed cell: the 1973 Altshuller table gives ${other.length ? other.join(", ") : "no principles"} here.</p>`;
    }
    out.innerHTML = head + `<div class="cards">${ids.map(card).join("")}</div>`;
  }

  $("improve").addEventListener("input", render);
  $("worsen").addEventListener("input", render);
  $("swap").addEventListener("click", () => {
    [$("improve").value, $("worsen").value] = [$("worsen").value, $("improve").value];
    render();
  });

  const q = new URLSearchParams(location.search);
  const qa = params.get(parseInt(q.get("improve"), 10));
  const qb = params.get(parseInt(q.get("worsen"), 10));
  $("improve").value = qa ? label(qa) : label(params.get(9));
  $("worsen").value = qb ? label(qb) : label(params.get(27));
  render();
})();
