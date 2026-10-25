CAT = "Data Display"
CAT_ID = "data"

PAGES = [
 {
  "folder": "data", "slug": "avatars", "title": "Avatars",
  "desc": "Initial avatars in sizes, with status dots and rings.",
  "idx_desc": "Initial avatars in sizes with status dots.",
  "mini": '<div class="p-row-tight"><span class="p-av" style="width: 22px; height: 22px;"></span><span class="p-av" style="width: 26px; height: 26px;"></span></div>',
  "blocks": [{
   "id": "avatars", "title": "Avatar sizes",
   "html": '''<div class="av-sec">
  <p class="av-lb">Sizes</p>
  <div class="av-row">
    <span class="av-el av-xs">AK</span>
    <span class="av-el av-sm">RS</span>
    <span class="av-el av-md">MP</span>
    <span class="av-el av-lg">TN</span>
  </div>
</div>
<div class="av-sec">
  <p class="av-lb">Status</p>
  <div class="av-row">
    <span class="av-wrap"><span class="av-el av-md av-a">AK</span><span class="av-dot is-on" aria-label="Online"></span></span>
    <span class="av-wrap"><span class="av-el av-md av-b">RS</span><span class="av-dot is-away" aria-label="Away"></span></span>
    <span class="av-wrap"><span class="av-el av-md av-c">MP</span><span class="av-dot is-off" aria-label="Offline"></span></span>
  </div>
</div>
<div class="av-sec">
  <p class="av-lb">Ring</p>
  <div class="av-row">
    <span class="av-el av-md av-a av-ring">AK</span>
    <span class="av-el av-md av-b av-ring av-ring-alt">RS</span>
  </div>
</div>''',
   "css": '''.av-sec { margin-bottom: 16px; }
.av-lb { margin: 0 0 8px; font-size: 0.7rem; font-weight: 700; letter-spacing: 0.07em; text-transform: uppercase; color: var(--muted); }
.av-row { display: flex; align-items: center; gap: 12px; flex-wrap: wrap; }
.av-el { display: inline-flex; align-items: center; justify-content: center; border-radius: 999px; color: #fff; font-weight: 700; letter-spacing: 0.02em; flex: 0 0 auto; background: linear-gradient(135deg, #4f6bed, #8b5cf6); }
.av-xs { width: 26px; height: 26px; font-size: 0.6rem; }
.av-sm { width: 34px; height: 34px; font-size: 0.7rem; }
.av-md { width: 44px; height: 44px; font-size: 0.82rem; }
.av-lg { width: 58px; height: 58px; font-size: 1rem; }
.av-a { background: linear-gradient(135deg, #4f6bed, #8b5cf6); }
.av-b { background: linear-gradient(135deg, #22a06b, #0ea5e9); }
.av-c { background: linear-gradient(135deg, #e5484d, #f0b543); }
.av-wrap { position: relative; display: inline-flex; }
.av-dot { position: absolute; right: 0; bottom: 0; width: 11px; height: 11px; border-radius: 999px; border: 2px solid var(--card); }
.av-dot.is-on { background: var(--yes); }
.av-dot.is-away { background: var(--warn); }
.av-dot.is-off { background: var(--muted); }
.av-ring { box-shadow: 0 0 0 2px var(--card), 0 0 0 4px var(--accent); }
.av-ring-alt { box-shadow: 0 0 0 2px var(--card), 0 0 0 4px var(--yes); }''',
  }],
 },
 {
  "folder": "data", "slug": "avatar-groups", "title": "Avatar Groups",
  "desc": "Overlapping avatar stacks with a plus-count chip.",
  "idx_desc": "Overlapping avatar stacks with plus count.",
  "mini": '<div class="p-avgroup"><span></span><span></span><span></span></div>',
  "blocks": [{
   "id": "avatar-groups", "title": "Stacked avatars",
   "html": '''<div class="ag-sec">
  <p class="ag-lb">Project members</p>
  <div class="ag-group">
    <span class="ag-el ag-1">AK</span>
    <span class="ag-el ag-2">RS</span>
    <span class="ag-el ag-3">MP</span>
    <span class="ag-el ag-4">TN</span>
    <span class="ag-el ag-more">+7</span>
  </div>
</div>
<div class="ag-sec">
  <p class="ag-lb">Small with count</p>
  <div class="ag-group ag-sm">
    <span class="ag-el ag-1">AK</span>
    <span class="ag-el ag-3">MP</span>
    <span class="ag-el ag-more">+2</span>
  </div>
</div>
<div class="ag-sec">
  <p class="ag-lb">Assigned to</p>
  <div class="ag-assign">
    <div class="ag-group">
      <span class="ag-el ag-1">RS</span>
      <span class="ag-el ag-2">TN</span>
    </div>
    <span class="ag-note">2 people working on this</span>
  </div>
</div>''',
   "css": '''.ag-sec { margin-bottom: 18px; }
.ag-lb { margin: 0 0 8px; font-size: 0.7rem; font-weight: 700; letter-spacing: 0.07em; text-transform: uppercase; color: var(--muted); }
.ag-group { display: inline-flex; align-items: center; }
.ag-el { width: 40px; height: 40px; border-radius: 999px; border: 2px solid var(--card); display: flex; align-items: center; justify-content: center; color: #fff; font-size: 0.76rem; font-weight: 700; margin-left: -10px; }
.ag-el:first-child { margin-left: 0; }
.ag-sm .ag-el { width: 32px; height: 32px; font-size: 0.66rem; margin-left: -8px; }
.ag-1 { background: linear-gradient(135deg, #4f6bed, #8b5cf6); }
.ag-2 { background: linear-gradient(135deg, #22a06b, #0ea5e9); }
.ag-3 { background: linear-gradient(135deg, #e5484d, #f0b543); }
.ag-4 { background: linear-gradient(135deg, #8b5cf6, #e5484d); }
.ag-more { background: var(--bg); color: var(--muted); border-color: var(--card); box-shadow: inset 0 0 0 1px var(--border); font-size: 0.72rem; }
.ag-assign { display: flex; align-items: center; gap: 10px; flex-wrap: wrap; }
.ag-note { font-size: 0.76rem; color: var(--muted); }''',
  }],
 },
 {
  "folder": "data", "slug": "stats-cards", "title": "Stats Cards",
  "desc": "Four KPI cards with trend deltas and sparklines.",
  "idx_desc": "KPI cards with trend deltas and sparklines.",
  "mini": '<div class="p-row-tight"><span class="p-card" style="width: 30px; height: 24px;"></span><span class="p-card" style="width: 30px; height: 24px;"></span></div>',
  "blocks": [{
   "id": "stats-cards", "title": "Dashboard KPIs",
   "html": '''<div class="st-grid">
  <article class="st-card">
    <p class="st-lb">Revenue</p>
    <p class="st-val">$24,780</p>
    <p class="st-delta is-up"><span class="st-arrow" aria-hidden="true">&#9650;</span> 12.4% vs last month</p>
    <svg class="st-spark" viewBox="0 0 100 28" fill="none" aria-hidden="true"><path d="M2 22L16 18L30 20L44 13L58 15L72 8L86 10L98 3" stroke="var(--yes)" stroke-width="2" stroke-linecap="round"/></svg>
  </article>
  <article class="st-card">
    <p class="st-lb">Active users</p>
    <p class="st-val">8,412</p>
    <p class="st-delta is-up"><span class="st-arrow" aria-hidden="true">&#9650;</span> 5.1% vs last month</p>
    <svg class="st-spark" viewBox="0 0 100 28" fill="none" aria-hidden="true"><path d="M2 20L16 21L30 15L44 17L58 11L72 12L86 6L98 7" stroke="var(--accent)" stroke-width="2" stroke-linecap="round"/></svg>
  </article>
  <article class="st-card">
    <p class="st-lb">Churn rate</p>
    <p class="st-val">1.8%</p>
    <p class="st-delta is-down"><span class="st-arrow" aria-hidden="true">&#9660;</span> 0.4% vs last month</p>
    <svg class="st-spark" viewBox="0 0 100 28" fill="none" aria-hidden="true"><path d="M2 6L16 9L30 7L44 13L58 12L72 17L86 16L98 22" stroke="var(--no)" stroke-width="2" stroke-linecap="round"/></svg>
  </article>
  <article class="st-card">
    <p class="st-lb">Open tickets</p>
    <p class="st-val">37</p>
    <p class="st-delta is-flat">No change this week</p>
    <svg class="st-spark" viewBox="0 0 100 28" fill="none" aria-hidden="true"><path d="M2 14L16 14L30 13L44 15L58 14L72 15L86 14L98 14" stroke="var(--muted)" stroke-width="2" stroke-linecap="round"/></svg>
  </article>
</div>''',
   "css": '''.st-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 10px; }
.st-card { border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 13px; }
.st-lb { margin: 0 0 4px; font-size: 0.7rem; font-weight: 600; color: var(--muted); text-transform: uppercase; letter-spacing: 0.05em; }
.st-val { margin: 0 0 3px; font-size: 1.3rem; font-weight: 800; letter-spacing: -0.02em; }
.st-delta { margin: 0; font-size: 0.68rem; color: var(--muted); display: flex; align-items: center; gap: 3px; flex-wrap: wrap; }
.st-arrow { font-size: 0.55rem; }
.is-up .st-arrow, .st-delta.is-up { color: var(--yes); }
.is-down .st-arrow, .st-delta.is-down { color: var(--no); }
.st-spark { width: 100%; height: 28px; margin-top: 6px; }''',
  }],
 },
 {
  "folder": "data", "slug": "comparison-table", "title": "Comparison Table",
  "desc": "Three-plan feature comparison with highlighted column.",
  "idx_desc": "Three-plan feature comparison table.",
  "mini": '<div class="p-table" style="height: 46px;"><span></span><span></span></div>',
  "blocks": [{
   "id": "comparison-table", "title": "Plan comparison",
   "html": '''<div class="cmp-scroll">
  <table class="cmp-table">
    <thead>
      <tr>
        <th class="cmp-th cmp-feat">Feature</th>
        <th class="cmp-th">Starter</th>
        <th class="cmp-th cmp-hot">Pro</th>
        <th class="cmp-th">Team</th>
      </tr>
    </thead>
    <tbody>
      <tr class="cmp-tr"><td class="cmp-td cmp-feat">Projects</td><td class="cmp-td">3</td><td class="cmp-td cmp-hot">Unlimited</td><td class="cmp-td">Unlimited</td></tr>
      <tr class="cmp-tr"><td class="cmp-td cmp-feat">Custom domain</td><td class="cmp-td"><span class="cmp-no" aria-label="No">&#10005;</span></td><td class="cmp-td cmp-hot"><span class="cmp-yes" aria-label="Yes">&#10003;</span></td><td class="cmp-td"><span class="cmp-yes" aria-label="Yes">&#10003;</span></td></tr>
      <tr class="cmp-tr"><td class="cmp-td cmp-feat">Analytics</td><td class="cmp-td">Basic</td><td class="cmp-td cmp-hot">Advanced</td><td class="cmp-td">Advanced</td></tr>
      <tr class="cmp-tr"><td class="cmp-td cmp-feat">Team seats</td><td class="cmp-td">1</td><td class="cmp-td cmp-hot">5</td><td class="cmp-td">25</td></tr>
      <tr class="cmp-tr"><td class="cmp-td cmp-feat">Priority support</td><td class="cmp-td"><span class="cmp-no" aria-label="No">&#10005;</span></td><td class="cmp-td cmp-hot"><span class="cmp-yes" aria-label="Yes">&#10003;</span></td><td class="cmp-td"><span class="cmp-yes" aria-label="Yes">&#10003;</span></td></tr>
      <tr class="cmp-tr"><td class="cmp-td cmp-feat">SLA</td><td class="cmp-td"><span class="cmp-no" aria-label="No">&#10005;</span></td><td class="cmp-td cmp-hot"><span class="cmp-no" aria-label="No">&#10005;</span></td><td class="cmp-td"><span class="cmp-yes" aria-label="Yes">&#10003;</span></td></tr>
    </tbody>
  </table>
</div>''',
   "css": '''.cmp-scroll { overflow-x: auto; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); }
.cmp-table { width: 100%; border-collapse: collapse; min-width: 420px; }
.cmp-th { padding: 11px 12px; text-align: center; font-size: 0.76rem; font-weight: 700; border-bottom: 1px solid var(--border); white-space: nowrap; }
.cmp-feat { text-align: left; color: var(--muted); font-weight: 600; }
.cmp-hot { background: var(--accent-soft); color: var(--accent); }
.cmp-th.cmp-hot { border-bottom-color: var(--accent); }
.cmp-tr + .cmp-tr .cmp-td { border-top: 1px solid var(--border); }
.cmp-td { padding: 10px 12px; text-align: center; font-size: 0.78rem; }
.cmp-td.cmp-feat { color: var(--text); }
.cmp-yes { color: var(--yes); font-weight: 700; }
.cmp-no { color: var(--muted); }''',
  }],
 },
 {
  "folder": "data", "slug": "data-table", "title": "Data Table",
  "desc": "Sortable, searchable table with row selection.",
  "idx_desc": "Sortable table with search and row selection.",
  "mini": '<div class="p-table" style="height: 48px;"><span></span><span></span><span></span></div>',
  "blocks": [{
   "id": "data-table", "title": "Team members",
   "html": '''<div class="dtx-card">
  <div class="dtx-top">
    <input class="dtx-search" id="dtxSearch" type="search" placeholder="Search members..." aria-label="Search members">
    <span class="dtx-sel" id="dtxSel">0 selected</span>
  </div>
  <div class="dtx-scroll">
    <table class="dtx-table">
      <thead>
        <tr>
          <th class="dtx-th dtx-checkcol"><input class="dtx-check" id="dtxAll" type="checkbox" aria-label="Select all rows"></th>
          <th class="dtx-th"><button class="dtx-sort" type="button" data-key="0">Name <span class="dtx-ind" aria-hidden="true"></span></button></th>
          <th class="dtx-th"><button class="dtx-sort" type="button" data-key="1">Role <span class="dtx-ind" aria-hidden="true"></span></button></th>
          <th class="dtx-th"><button class="dtx-sort" type="button" data-key="2">Status <span class="dtx-ind" aria-hidden="true"></span></button></th>
        </tr>
      </thead>
      <tbody id="dtxBody">
        <tr class="dtx-tr"><td class="dtx-td dtx-checkcol"><input class="dtx-check dtx-row" type="checkbox" aria-label="Select Ayesha Khan"></td><td class="dtx-td">Ayesha Khan</td><td class="dtx-td">Designer</td><td class="dtx-td"><span class="dtx-tag is-active">Active</span></td></tr>
        <tr class="dtx-tr"><td class="dtx-td dtx-checkcol"><input class="dtx-check dtx-row" type="checkbox" aria-label="Select Rohan Shah"></td><td class="dtx-td">Rohan Shah</td><td class="dtx-td">Engineer</td><td class="dtx-td"><span class="dtx-tag is-active">Active</span></td></tr>
        <tr class="dtx-tr"><td class="dtx-td dtx-checkcol"><input class="dtx-check dtx-row" type="checkbox" aria-label="Select Mira Patel"></td><td class="dtx-td">Mira Patel</td><td class="dtx-td">Manager</td><td class="dtx-td"><span class="dtx-tag is-away">Away</span></td></tr>
        <tr class="dtx-tr"><td class="dtx-td dtx-checkcol"><input class="dtx-check dtx-row" type="checkbox" aria-label="Select Tarun Nair"></td><td class="dtx-td">Tarun Nair</td><td class="dtx-td">Engineer</td><td class="dtx-td"><span class="dtx-tag is-off">Offline</span></td></tr>
        <tr class="dtx-tr"><td class="dtx-td dtx-checkcol"><input class="dtx-check dtx-row" type="checkbox" aria-label="Select Sana Iqbal"></td><td class="dtx-td">Sana Iqbal</td><td class="dtx-td">Marketing</td><td class="dtx-td"><span class="dtx-tag is-active">Active</span></td></tr>
      </tbody>
    </table>
  </div>
</div>''',
   "css": '''.dtx-card { border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); overflow: hidden; }
.dtx-top { display: flex; align-items: center; justify-content: space-between; gap: 10px; padding: 10px; border-bottom: 1px solid var(--border); flex-wrap: wrap; }
.dtx-search { flex: 1; min-width: 140px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--bg); color: var(--text); font: inherit; font-size: 0.79rem; padding: 7px 10px; outline: none; }
.dtx-search:focus { border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-soft); }
.dtx-sel { font-size: 0.72rem; color: var(--muted); white-space: nowrap; }
.dtx-scroll { overflow-x: auto; }
.dtx-table { width: 100%; border-collapse: collapse; min-width: 420px; }
.dtx-th { text-align: left; padding: 8px 10px; font-size: 0.68rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--muted); border-bottom: 1px solid var(--border); white-space: nowrap; }
.dtx-checkcol { width: 34px; }
.dtx-check { accent-color: var(--accent); width: 14px; height: 14px; cursor: pointer; }
.dtx-sort { border: 0; background: transparent; color: inherit; font: inherit; font-size: inherit; text-transform: inherit; letter-spacing: inherit; cursor: pointer; padding: 0; display: inline-flex; align-items: center; gap: 4px; }
.dtx-sort:hover { color: var(--accent); }
.dtx-sort:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.dtx-ind { font-size: 0.6rem; color: var(--accent); }
.dtx-tr:hover { background: var(--bg); }
.dtx-td { padding: 9px 10px; font-size: 0.78rem; border-bottom: 1px solid var(--border); }
.dtx-tag { font-size: 0.64rem; font-weight: 700; padding: 2px 7px; border-radius: 999px; }
.dtx-tag.is-active { background: rgba(34, 160, 107, 0.12); color: var(--yes); }
.dtx-tag.is-away { background: rgba(194, 116, 10, 0.12); color: var(--warn); }
.dtx-tag.is-off { background: var(--bg); color: var(--muted); }''',
   "js": '''(function () {
  var body = document.getElementById("dtxBody");
  var rows = Array.prototype.slice.call(body.querySelectorAll(".dtx-tr"));
  var all = document.getElementById("dtxAll");
  var selLabel = document.getElementById("dtxSel");
  var search = document.getElementById("dtxSearch");
  var dir = {};

  function visible() { return rows.filter(function (r) { return !r.hidden; }); }

  function syncSel() {
    var checked = rows.filter(function (r) { return r.querySelector(".dtx-row").checked; });
    selLabel.textContent = checked.length + " selected";
    var vis = visible();
    all.checked = vis.length > 0 && vis.every(function (r) { return r.querySelector(".dtx-row").checked; });
  }

  all.addEventListener("change", function () {
    visible().forEach(function (r) { r.querySelector(".dtx-row").checked = all.checked; });
    syncSel();
  });

  rows.forEach(function (r) {
    r.querySelector(".dtx-row").addEventListener("change", syncSel);
  });

  search.addEventListener("input", function () {
    var q = search.value.toLowerCase();
    rows.forEach(function (r) { r.hidden = r.textContent.toLowerCase().indexOf(q) === -1; });
    syncSel();
  });

  document.querySelectorAll(".dtx-sort").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var key = Number(btn.getAttribute("data-key"));
      dir[key] = !dir[key];
      document.querySelectorAll(".dtx-ind").forEach(function (i) { i.textContent = ""; });
      btn.querySelector(".dtx-ind").textContent = dir[key] ? "\\u25B2" : "\\u25BC";
      rows.sort(function (a, b) {
        var at = a.children[key].textContent.trim().toLowerCase();
        var bt = b.children[key].textContent.trim().toLowerCase();
        return at < bt ? (dir[key] ? -1 : 1) : at > bt ? (dir[key] ? 1 : -1) : 0;
      });
      rows.forEach(function (r) { body.appendChild(r); });
    });
  });
})();''',
  }],
 },
 {
  "folder": "data", "slug": "timeline", "title": "Timeline",
  "desc": "Vertical timeline with coloured markers and dates.",
  "idx_desc": "Vertical timeline with coloured markers.",
  "mini": '<div class="p-tl"><span></span><span></span><span></span></div>',
  "blocks": [{
   "id": "timeline", "title": "Project timeline",
   "html": '''<ol class="tl-list">
  <li class="tl-item">
    <span class="tl-dot is-done" aria-hidden="true"></span>
    <div class="tl-box">
      <span class="tl-date">12 Oct 2026</span>
      <p class="tl-t">Project kickoff</p>
      <p class="tl-d">Scope approved and the team was assigned.</p>
    </div>
  </li>
  <li class="tl-item">
    <span class="tl-dot is-done" aria-hidden="true"></span>
    <div class="tl-box">
      <span class="tl-date">18 Oct 2026</span>
      <p class="tl-t">Design handoff</p>
      <p class="tl-d">Final screens and tokens were delivered to engineering.</p>
    </div>
  </li>
  <li class="tl-item">
    <span class="tl-dot is-now" aria-hidden="true"></span>
    <div class="tl-box is-now">
      <span class="tl-date">22 Oct 2026</span>
      <p class="tl-t">Build in progress</p>
      <p class="tl-d">Components are being assembled and reviewed daily.</p>
    </div>
  </li>
  <li class="tl-item">
    <span class="tl-dot" aria-hidden="true"></span>
    <div class="tl-box">
      <span class="tl-date">05 Nov 2026</span>
      <p class="tl-t">Launch</p>
      <p class="tl-d">Public release with the first documentation pass.</p>
    </div>
  </li>
</ol>''',
   "css": '''.tl-list { list-style: none; margin: 0; padding: 0 0 0 4px; }
.tl-item { position: relative; padding: 0 0 18px 22px; border-left: 2px solid var(--border); }
.tl-item:last-child { border-left-color: transparent; padding-bottom: 0; }
.tl-dot { position: absolute; left: -7px; top: 2px; width: 12px; height: 12px; border-radius: 999px; background: var(--card); border: 2px solid var(--border); }
.tl-dot.is-done { background: var(--yes); border-color: var(--yes); }
.tl-dot.is-now { background: var(--accent); border-color: var(--accent); box-shadow: 0 0 0 4px var(--accent-soft); }
.tl-box { background: var(--card); border: 1px solid var(--border); border-radius: var(--radius); padding: 10px 12px; }
.tl-box.is-now { border-color: var(--accent); }
.tl-date { display: inline-block; font-size: 0.66rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: var(--muted); margin-bottom: 2px; }
.tl-t { margin: 0 0 2px; font-size: 0.83rem; font-weight: 700; }
.tl-d { margin: 0; font-size: 0.75rem; color: var(--muted); line-height: 1.45; }''',
  }],
 },
 {
  "folder": "data", "slug": "activity-feed", "title": "Activity Feed",
  "desc": "Team activity list with avatars and relative times.",
  "idx_desc": "Team activity list with avatars and times.",
  "mini": '<div class="p-row-tight"><span class="p-av" style="width: 18px; height: 18px;"></span><span class="p-line" style="width: 34px;"></span></div>',
  "blocks": [{
   "id": "activity-feed", "title": "Recent activity",
   "html": '''<div class="af-card">
  <div class="af-head">
    <span class="af-title">Recent activity</span>
    <span class="af-live"><span class="af-dot" aria-hidden="true"></span>Live</span>
  </div>
  <ul class="af-list">
    <li class="af-item">
      <span class="af-av af-1">AK</span>
      <div class="af-body"><p class="af-t"><strong>Ayesha</strong> commented on <span class="af-link">Checkout flow</span></p><p class="af-time">2 min ago</p></div>
    </li>
    <li class="af-item">
      <span class="af-av af-2">RS</span>
      <div class="af-body"><p class="af-t"><strong>Rohan</strong> merged pull request <span class="af-link">#248</span></p><p class="af-time">18 min ago</p></div>
    </li>
    <li class="af-item">
      <span class="af-av af-3">MP</span>
      <div class="af-body"><p class="af-t"><strong>Mira</strong> moved 3 tasks to <span class="af-link">Review</span></p><p class="af-time">1 hour ago</p></div>
    </li>
    <li class="af-item">
      <span class="af-av af-4">TN</span>
      <div class="af-body"><p class="af-t"><strong>Tarun</strong> uploaded <span class="af-link">brand-assets.zip</span></p><p class="af-time">3 hours ago</p></div>
    </li>
  </ul>
</div>''',
   "css": '''.af-card { max-width: 380px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); overflow: hidden; }
.af-head { display: flex; align-items: center; justify-content: space-between; padding: 11px 13px; border-bottom: 1px solid var(--border); }
.af-title { font-size: 0.8rem; font-weight: 700; }
.af-live { display: inline-flex; align-items: center; gap: 4px; font-size: 0.68rem; font-weight: 600; color: var(--yes); }
.af-dot { width: 6px; height: 6px; border-radius: 999px; background: currentColor; animation: afPulse 1.6s ease-in-out infinite; }
.af-list { list-style: none; margin: 0; padding: 4px; }
.af-item { display: flex; gap: 9px; padding: 9px; border-radius: 4px; }
.af-item:hover { background: var(--bg); }
.af-av { width: 30px; height: 30px; border-radius: 999px; display: flex; align-items: center; justify-content: center; color: #fff; font-size: 0.65rem; font-weight: 700; flex: 0 0 auto; }
.af-1 { background: linear-gradient(135deg, #4f6bed, #8b5cf6); }
.af-2 { background: linear-gradient(135deg, #22a06b, #0ea5e9); }
.af-3 { background: linear-gradient(135deg, #e5484d, #f0b543); }
.af-4 { background: linear-gradient(135deg, #8b5cf6, #e5484d); }
.af-body { min-width: 0; }
.af-t { margin: 0; font-size: 0.77rem; line-height: 1.4; }
.af-t strong { font-weight: 700; }
.af-link { color: var(--accent); font-weight: 600; }
.af-time { margin: 2px 0 0; font-size: 0.68rem; color: var(--muted); }
@keyframes afPulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.3; } }
@media (prefers-reduced-motion: reduce) { .af-dot { animation: none; } }''',
  }],
 },
 {
  "folder": "data", "slug": "charts", "title": "Charts",
  "desc": "CSS bar chart, SVG line sparkline and donut.",
  "idx_desc": "Bar chart, line sparkline and donut chart.",
  "mini": '<div class="p-row-tight" style="align-items: flex-end;"><span class="p-bar" style="height: 12px;"></span><span class="p-bar" style="height: 20px;"></span><span class="p-bar" style="height: 16px;"></span></div>',
  "blocks": [
   {"id": "bar-chart", "title": "Weekly rentals", "html": '''<div class="ch-card">
  <div class="ch-head"><span class="ch-title">Weekly rentals</span><span class="ch-badge">+18.2%</span></div>
  <div class="ch-bars" role="img" aria-label="Rentals by day: Mon 42, Tue 58, Wed 47, Thu 71, Fri 64, Sat 88, Sun 76">
    <div class="ch-col"><span class="ch-bar" style="height: 42%"></span><span class="ch-x">Mon</span></div>
    <div class="ch-col"><span class="ch-bar" style="height: 58%"></span><span class="ch-x">Tue</span></div>
    <div class="ch-col"><span class="ch-bar" style="height: 47%"></span><span class="ch-x">Wed</span></div>
    <div class="ch-col"><span class="ch-bar" style="height: 71%"></span><span class="ch-x">Thu</span></div>
    <div class="ch-col"><span class="ch-bar" style="height: 64%"></span><span class="ch-x">Fri</span></div>
    <div class="ch-col"><span class="ch-bar is-hot" style="height: 88%"></span><span class="ch-x">Sat</span></div>
    <div class="ch-col"><span class="ch-bar" style="height: 76%"></span><span class="ch-x">Sun</span></div>
  </div>
</div>''', "css": '''.ch-card { max-width: 380px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 14px; }
.ch-head { display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px; }
.ch-title { font-size: 0.82rem; font-weight: 700; }
.ch-badge { font-size: 0.66rem; font-weight: 700; color: var(--yes); background: rgba(34, 160, 107, 0.12); padding: 2px 7px; border-radius: 999px; }
.ch-bars { display: flex; align-items: flex-end; gap: 7px; height: 140px; }
.ch-col { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; height: 100%; gap: 5px; }
.ch-bar { width: 100%; max-width: 26px; background: var(--accent-soft); border-radius: 3px 3px 0 0; transition: height 0.3s; }
.ch-bar.is-hot { background: var(--accent); }
.ch-x { font-size: 0.62rem; color: var(--muted); }'''},
   {"id": "sparkline", "title": "Trend line", "html": '''<div class="ch-card">
  <div class="ch-head"><span class="ch-title">Response time</span><span class="ch-badge">-24%</span></div>
  <p class="ch-big">182<span class="ch-unit">ms</span></p>
  <svg class="ch-line" viewBox="0 0 300 80" fill="none" role="img" aria-label="Response time trending down over seven days">
    <path d="M0 62L50 54L100 58L150 38L200 44L250 22L300 12" stroke="var(--accent)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M0 62L50 54L100 58L150 38L200 44L250 22L300 12V80H0Z" fill="var(--accent)" opacity="0.1"/>
    <circle cx="300" cy="12" r="4" fill="var(--accent)"/>
  </svg>
  <div class="ch-days" aria-hidden="true"><span class="ch-d">Mon</span><span class="ch-d">Tue</span><span class="ch-d">Wed</span><span class="ch-d">Thu</span><span class="ch-d">Fri</span><span class="ch-d">Sat</span><span class="ch-d">Sun</span></div>
</div>''', "css": '''.ch-card { max-width: 380px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 14px; }
.ch-head { display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px; }
.ch-title { font-size: 0.82rem; font-weight: 700; }
.ch-badge { font-size: 0.66rem; font-weight: 700; color: var(--yes); background: rgba(34, 160, 107, 0.12); padding: 2px 7px; border-radius: 999px; }
.ch-big { margin: 0 0 6px; font-size: 1.6rem; font-weight: 800; letter-spacing: -0.02em; }
.ch-unit { font-size: 0.8rem; font-weight: 600; color: var(--muted); margin-left: 3px; }
.ch-line { width: 100%; height: 80px; }
.ch-days { display: flex; justify-content: space-between; }
.ch-d { font-size: 0.6rem; color: var(--muted); }'''},
   {"id": "donut", "title": "Traffic split", "html": '''<div class="ch-card">
  <div class="ch-head"><span class="ch-title">Traffic split</span></div>
  <div class="ch-donutwrap">
    <svg class="ch-donut" viewBox="0 0 90 90" role="img" aria-label="Traffic: direct 62 percent, search 26 percent, social 12 percent">
      <circle class="ch-track" cx="45" cy="45" r="34"/>
      <circle class="ch-seg ch-seg-a" cx="45" cy="45" r="34"/>
      <circle class="ch-seg ch-seg-b" cx="45" cy="45" r="34"/>
    </svg>
    <div class="ch-center"><span class="ch-cv">62%</span><span class="ch-cl">Direct</span></div>
  </div>
  <ul class="ch-legend">
    <li class="ch-li"><span class="ch-key ch-key-a"></span>Direct <span class="ch-pct">62%</span></li>
    <li class="ch-li"><span class="ch-key ch-key-b"></span>Search <span class="ch-pct">26%</span></li>
    <li class="ch-li"><span class="ch-key ch-key-c"></span>Social <span class="ch-pct">12%</span></li>
  </ul>
</div>''', "css": '''.ch-card { max-width: 320px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 14px; }
.ch-head { display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px; }
.ch-title { font-size: 0.82rem; font-weight: 700; }
.ch-donutwrap { position: relative; width: 150px; height: 150px; margin: 0 auto 10px; }
.ch-donut { width: 150px; height: 150px; transform: rotate(-90deg); }
.ch-track { fill: none; stroke: var(--bg); stroke-width: 12; }
.ch-seg { fill: none; stroke-width: 12; stroke-linecap: butt; }
.ch-seg-a { stroke: var(--accent); stroke-dasharray: 132 214; }
.ch-seg-b { stroke: var(--yes); stroke-dasharray: 56 214; stroke-dashoffset: -132; }
.ch-center { position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; }
.ch-cv { font-size: 1.2rem; font-weight: 800; }
.ch-cl { font-size: 0.64rem; color: var(--muted); }
.ch-legend { list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 5px; }
.ch-li { display: flex; align-items: center; gap: 6px; font-size: 0.73rem; color: var(--muted); }
.ch-key { width: 8px; height: 8px; border-radius: 2px; }
.ch-key-a { background: var(--accent); }
.ch-key-b { background: var(--yes); }
.ch-key-c { background: var(--border); }
.ch-pct { margin-left: auto; color: var(--text); font-weight: 700; }'''},
  ],
 },
 {
  "folder": "data", "slug": "key-value", "title": "Key-Value List",
  "desc": "Definition list for order and account details.",
  "idx_desc": "Definition list for order and account details.",
  "mini": '<div class="p-row"><span class="p-line" style="width: 22px;"></span><span class="p-line" style="width: 34px;"></span></div>',
  "blocks": [{
   "id": "key-value", "title": "Order details",
   "html": '''<div class="kv-card">
  <p class="kv-head">Order details</p>
  <dl class="kv-list">
    <div class="kv-row"><dt class="kv-k">Order ID</dt><dd class="kv-v">#ORD-8241</dd></div>
    <div class="kv-row"><dt class="kv-k">Placed on</dt><dd class="kv-v">18 October 2026</dd></div>
    <div class="kv-row"><dt class="kv-k">Payment</dt><dd class="kv-v">Visa ending 4242</dd></div>
    <div class="kv-row"><dt class="kv-k">Shipping</dt><dd class="kv-v">Standard, 3-5 days</dd></div>
    <div class="kv-row"><dt class="kv-k">Status</dt><dd class="kv-v"><span class="kv-tag">In transit</span></dd></div>
    <div class="kv-row"><dt class="kv-k">Total</dt><dd class="kv-v kv-total">$148.00</dd></div>
  </dl>
</div>''',
   "css": '''.kv-card { max-width: 360px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 14px; }
.kv-head { margin: 0 0 8px; font-size: 0.8rem; font-weight: 700; }
.kv-list { margin: 0; }
.kv-row { display: flex; align-items: baseline; gap: 10px; padding: 7px 0; border-bottom: 1px dashed var(--border); }
.kv-row:last-child { border-bottom: 0; }
.kv-k { flex: 0 0 40%; font-size: 0.74rem; color: var(--muted); }
.kv-v { flex: 1; margin: 0; font-size: 0.78rem; font-weight: 600; text-align: right; }
.kv-total { font-size: 0.92rem; color: var(--accent); }
.kv-tag { font-size: 0.64rem; font-weight: 700; color: var(--warn); background: rgba(194, 116, 10, 0.12); padding: 2px 7px; border-radius: 999px; }''',
  }],
 },
 {
  "folder": "data", "slug": "rating-stars", "title": "Rating Summary",
  "desc": "Average score, star display and score breakdown.",
  "idx_desc": "Average score with star breakdown bars.",
  "mini": '<div class="p-row-tight"><span class="p-star">★</span><span class="p-star is-dim">★</span></div>',
  "blocks": [{
   "id": "rating-stars", "title": "Product rating",
   "html": '''<div class="rs-card">
  <div class="rs-top">
    <div class="rs-score">
      <span class="rs-num">4.6</span>
      <span class="rs-stars" role="img" aria-label="4.6 out of 5 stars">
        <span class="rs-star">&#9733;</span><span class="rs-star">&#9733;</span><span class="rs-star">&#9733;</span><span class="rs-star">&#9733;</span><span class="rs-star is-half">&#9733;</span>
      </span>
      <span class="rs-count">Based on 1,284 reviews</span>
    </div>
    <button class="rs-write" type="button">Write a review</button>
  </div>
  <ul class="rs-bars">
    <li class="rs-li"><span class="rs-lb">5</span><span class="rs-track"><span class="rs-fill" style="width: 78%"></span></span><span class="rs-pc">78%</span></li>
    <li class="rs-li"><span class="rs-lb">4</span><span class="rs-track"><span class="rs-fill" style="width: 14%"></span></span><span class="rs-pc">14%</span></li>
    <li class="rs-li"><span class="rs-lb">3</span><span class="rs-track"><span class="rs-fill" style="width: 5%"></span></span><span class="rs-pc">5%</span></li>
    <li class="rs-li"><span class="rs-lb">2</span><span class="rs-track"><span class="rs-fill" style="width: 2%"></span></span><span class="rs-pc">2%</span></li>
    <li class="rs-li"><span class="rs-lb">1</span><span class="rs-track"><span class="rs-fill" style="width: 1%"></span></span><span class="rs-pc">1%</span></li>
  </ul>
</div>''',
   "css": '''.rs-card { max-width: 380px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 16px; }
.rs-top { display: flex; align-items: flex-start; justify-content: space-between; gap: 10px; flex-wrap: wrap; margin-bottom: 12px; }
.rs-score { display: flex; flex-direction: column; gap: 2px; }
.rs-num { font-size: 1.9rem; font-weight: 800; line-height: 1; }
.rs-stars { color: #f0b543; font-size: 0.86rem; letter-spacing: 1px; }
.rs-star.is-half { opacity: 0.45; }
.rs-count { font-size: 0.68rem; color: var(--muted); }
.rs-write { border: 1px solid var(--border); background: transparent; color: var(--accent); font: inherit; font-size: 0.72rem; font-weight: 700; padding: 7px 11px; border-radius: var(--radius); cursor: pointer; }
.rs-write:hover { border-color: var(--accent); }
.rs-write:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.rs-bars { list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 5px; }
.rs-li { display: flex; align-items: center; gap: 7px; }
.rs-lb { font-size: 0.68rem; color: var(--muted); width: 8px; }
.rs-track { flex: 1; height: 7px; border-radius: 999px; background: var(--bg); overflow: hidden; }
.rs-fill { display: block; height: 100%; border-radius: 999px; background: #f0b543; }
.rs-pc { font-size: 0.66rem; color: var(--muted); width: 30px; text-align: right; }''',
  }],
 },
 {
  "folder": "data", "slug": "gallery", "title": "Image Gallery",
  "desc": "Responsive masonry-style grid with hover captions.",
  "idx_desc": "Responsive gallery grid with hover captions.",
  "mini": '<div class="p-gal"><span></span><span></span><span></span></div>',
  "blocks": [{
   "id": "gallery", "title": "Photo grid",
   "html": '''<div class="gl-grid">
  <figure class="gl-item gl-tall gl-g1">
    <figcaption class="gl-cap"><span class="gl-t">Mountain trail</span><span class="gl-s">Landscape</span></figcaption>
  </figure>
  <figure class="gl-item gl-g2">
    <figcaption class="gl-cap"><span class="gl-t">Studio light</span><span class="gl-s">Interior</span></figcaption>
  </figure>
  <figure class="gl-item gl-g3">
    <figcaption class="gl-cap"><span class="gl-t">Coastline</span><span class="gl-s">Travel</span></figcaption>
  </figure>
  <figure class="gl-item gl-wide gl-g4">
    <figcaption class="gl-cap"><span class="gl-t">Night market</span><span class="gl-s">Street</span></figcaption>
  </figure>
  <figure class="gl-item gl-g5">
    <figcaption class="gl-cap"><span class="gl-t">Desert dunes</span><span class="gl-s">Nature</span></figcaption>
  </figure>
  <figure class="gl-item gl-g6">
    <figcaption class="gl-cap"><span class="gl-t">City lines</span><span class="gl-s">Architecture</span></figcaption>
  </figure>
</div>''',
   "css": '''.gl-grid { display: grid; grid-template-columns: repeat(3, 1fr); grid-auto-rows: 92px; gap: 8px; }
.gl-item { position: relative; margin: 0; border-radius: var(--radius); overflow: hidden; display: flex; align-items: flex-end; }
.gl-item::after { content: ""; position: absolute; inset: 0; background: linear-gradient(180deg, transparent 40%, rgba(10, 12, 18, 0.72)); opacity: 0.75; transition: opacity 0.2s; }
.gl-item:hover::after { opacity: 1; }
.gl-tall { grid-row: span 2; }
.gl-wide { grid-column: span 2; }
.gl-g1 { background: linear-gradient(150deg, #7c9cff, #4f6bed 55%, #24306b); }
.gl-g2 { background: linear-gradient(160deg, #f5d0a9, #c2740a 60%, #6b3d10); }
.gl-g3 { background: linear-gradient(150deg, #9be7d8, #22a06b 60%, #0b4f3c); }
.gl-g4 { background: linear-gradient(150deg, #f3a6b6, #8b5cf6 60%, #3b1d6b); }
.gl-g5 { background: linear-gradient(150deg, #f7e2a1, #e5484d 65%, #6b1a1d); }
.gl-g6 { background: linear-gradient(150deg, #b9c4d8, #5d6b85 60%, #232a3a); }
.gl-cap { position: relative; z-index: 2; padding: 9px; display: flex; flex-direction: column; opacity: 0; transform: translateY(6px); transition: opacity 0.2s, transform 0.2s; }
.gl-item:hover .gl-cap, .gl-item:focus-within .gl-cap { opacity: 1; transform: translateY(0); }
.gl-t { font-size: 0.74rem; font-weight: 700; color: #fff; }
.gl-s { font-size: 0.62rem; color: rgba(255, 255, 255, 0.72); }''',
  }],
 },
 {
  "folder": "data", "slug": "lightbox", "title": "Lightbox",
  "desc": "Thumbnail grid that opens a full-size viewer.",
  "idx_desc": "Thumbnail grid with full-size lightbox viewer.",
  "mini": '<div class="p-gal"><span></span><span></span></div><div class="p-drop" style="width: 24px; height: 16px;"></div>',
  "blocks": [{
   "id": "lightbox", "title": "Gallery viewer",
   "note": "Thumbnail par click karein — overlay khulega, Escape se band hoga.",
   "html": '''<div class="lb-wrap">
  <div class="lb-grid">
    <button class="lb-thumb lb-a" type="button" data-label="Aurora over the ridge" aria-label="Open Aurora over the ridge"></button>
    <button class="lb-thumb lb-b" type="button" data-label="Warm studio corner" aria-label="Open Warm studio corner"></button>
    <button class="lb-thumb lb-c" type="button" data-label="Tide at blue hour" aria-label="Open Tide at blue hour"></button>
  </div>
  <div class="lb-overlay" id="lbOverlay" role="dialog" aria-modal="true" aria-label="Image viewer" hidden>
    <div class="lb-stage" id="lbStage">
      <button class="lb-close" type="button" id="lbClose" aria-label="Close viewer">&times;</button>
      <p class="lb-caption" id="lbCaption"></p>
    </div>
  </div>
</div>''',
   "css": '''.lb-wrap { position: relative; border: 1px dashed var(--border); border-radius: var(--radius); padding: 12px; }
.lb-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; }
.lb-thumb { height: 80px; border: 0; border-radius: var(--radius); cursor: pointer; padding: 0; position: relative; }
.lb-thumb::after { content: ""; position: absolute; inset: 0; border-radius: inherit; box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.18); }
.lb-thumb:hover { transform: scale(1.02); }
.lb-thumb:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.lb-a { background: linear-gradient(140deg, #22305e, #4f6bed 55%, #8b5cf6); }
.lb-b { background: linear-gradient(140deg, #6b3d10, #c2740a 60%, #f5d0a9); }
.lb-c { background: linear-gradient(140deg, #0b4f3c, #22a06b 55%, #9be7d8); }
.lb-overlay { position: absolute; inset: 0; background: rgba(10, 12, 18, 0.72); border-radius: var(--radius); display: flex; align-items: center; justify-content: center; padding: 12px; z-index: 10; }
.lb-stage { position: relative; width: 100%; height: 190px; border-radius: var(--radius); overflow: hidden; transition: background 0.2s; }
.lb-close { position: absolute; top: 8px; right: 8px; width: 28px; height: 28px; border-radius: 999px; border: 0; background: rgba(0, 0, 0, 0.4); color: #fff; font-size: 1.1rem; cursor: pointer; line-height: 1; }
.lb-close:hover { background: rgba(0, 0, 0, 0.6); }
.lb-close:focus-visible { outline: 2px solid #fff; outline-offset: 2px; }
.lb-caption { position: absolute; left: 0; right: 0; bottom: 0; margin: 0; padding: 22px 12px 10px; color: #fff; font-size: 0.78rem; font-weight: 600; background: linear-gradient(180deg, transparent, rgba(0, 0, 0, 0.55)); }''',
   "js": '''(function () {
  var overlay = document.getElementById("lbOverlay");
  var stage = document.getElementById("lbStage");
  var caption = document.getElementById("lbCaption");
  var close = document.getElementById("lbClose");
  var last = null;

  function open(bg, label, trigger) {
    stage.style.background = bg;
    caption.textContent = label;
    overlay.hidden = false;
    last = trigger;
    close.focus();
  }

  function hide() {
    overlay.hidden = true;
    if (last) last.focus();
  }

  document.querySelectorAll(".lb-thumb").forEach(function (b) {
    b.addEventListener("click", function () {
      var bg = window.getComputedStyle(b).backgroundImage;
      open(bg, b.getAttribute("data-label"), b);
    });
  });

  close.addEventListener("click", hide);
  overlay.addEventListener("click", function (e) { if (e.target === overlay) hide(); });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && !overlay.hidden) hide();
  });
})();''',
  }],
 },
 {
  "folder": "data", "slug": "carousel", "title": "Carousel",
  "desc": "Sliding cards with arrows, dots and wrap-around.",
  "idx_desc": "Sliding cards with arrows and dot navigation.",
  "mini": '<div class="p-row-tight"><span class="p-card" style="width: 26px; height: 20px;"></span><span class="p-card" style="width: 26px; height: 20px; opacity: .5;"></span></div>',
  "blocks": [{
   "id": "carousel", "title": "Feature carousel",
   "html": '''<div class="cr-wrap">
  <div class="cr-view">
    <div class="cr-track" id="crTrack">
      <article class="cr-slide cr-s1"><span class="cr-k">01</span><p class="cr-t">Design tokens</p><p class="cr-d">One source of truth for colour, spacing and radius.</p></article>
      <article class="cr-slide cr-s2"><span class="cr-k">02</span><p class="cr-t">Reusable blocks</p><p class="cr-d">Copy a block, paste it, then adjust the content.</p></article>
      <article class="cr-slide cr-s3"><span class="cr-k">03</span><p class="cr-t">Dark mode ready</p><p class="cr-d">Every component responds to the theme attribute.</p></article>
    </div>
  </div>
  <div class="cr-ctrl">
    <button class="cr-arrow" type="button" id="crPrev" aria-label="Previous slide">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 6l-6 6 6 6"/></svg>
    </button>
    <div class="cr-dots" id="crDots" role="tablist" aria-label="Slides">
      <button class="cr-dot is-on" type="button" role="tab" aria-selected="true" aria-label="Slide 1"></button>
      <button class="cr-dot" type="button" role="tab" aria-selected="false" aria-label="Slide 2"></button>
      <button class="cr-dot" type="button" role="tab" aria-selected="false" aria-label="Slide 3"></button>
    </div>
    <button class="cr-arrow" type="button" id="crNext" aria-label="Next slide">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg>
    </button>
  </div>
</div>''',
   "css": '''.cr-wrap { max-width: 380px; }
.cr-view { overflow: hidden; border-radius: var(--radius); }
.cr-track { display: flex; transition: transform 0.3s ease; }
.cr-slide { flex: 0 0 100%; min-height: 160px; padding: 18px; display: flex; flex-direction: column; justify-content: flex-end; color: #fff; }
.cr-s1 { background: linear-gradient(150deg, #4f6bed, #8b5cf6); }
.cr-s2 { background: linear-gradient(150deg, #22a06b, #0ea5e9); }
.cr-s3 { background: linear-gradient(150deg, #242833, #4f6bed); }
.cr-k { font-size: 0.66rem; font-weight: 700; opacity: 0.7; letter-spacing: 0.1em; }
.cr-t { margin: 4px 0 4px; font-size: 1.05rem; font-weight: 800; }
.cr-d { margin: 0; font-size: 0.78rem; line-height: 1.5; opacity: 0.88; }
.cr-ctrl { display: flex; align-items: center; justify-content: space-between; gap: 10px; margin-top: 10px; }
.cr-arrow { width: 30px; height: 30px; border: 1px solid var(--border); border-radius: 999px; background: var(--card); color: var(--muted); display: flex; align-items: center; justify-content: center; cursor: pointer; }
.cr-arrow svg { width: 15px; height: 15px; }
.cr-arrow:hover { border-color: var(--accent); color: var(--accent); }
.cr-arrow:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.cr-dots { display: flex; gap: 5px; }
.cr-dot { width: 7px; height: 7px; border-radius: 999px; border: 0; background: var(--border); cursor: pointer; padding: 0; }
.cr-dot.is-on { background: var(--accent); width: 18px; }
.cr-dot:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
@media (prefers-reduced-motion: reduce) { .cr-track { transition: none; } }''',
   "js": '''(function () {
  var track = document.getElementById("crTrack");
  var dots = Array.prototype.slice.call(document.querySelectorAll(".cr-dot"));
  var index = 0;
  var total = track.children.length;

  function go(i) {
    index = (i + total) % total;
    track.style.transform = "translateX(-" + index * 100 + "%)";
    dots.forEach(function (d, k) {
      d.classList.toggle("is-on", k === index);
      d.setAttribute("aria-selected", String(k === index));
    });
  }

  document.getElementById("crPrev").addEventListener("click", function () { go(index - 1); });
  document.getElementById("crNext").addEventListener("click", function () { go(index + 1); });
  dots.forEach(function (d, k) { d.addEventListener("click", function () { go(k); }); });
})();''',
  }],
 },
]
