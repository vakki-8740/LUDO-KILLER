CAT = "Dashboard & App"
CAT_ID = "dashboard"

PAGES = [
 {
  "folder": "dashboard", "slug": "layout", "title": "Dashboard Layout",
  "desc": "Sidebar, topbar and content shell in one frame.",
  "idx_desc": "Sidebar, topbar and content shell layout.",
  "mini": '<div class="p-row" style="gap: 3px;"><div class="p-page" style="width: 16px; height: 34px;"></div><div class="p-page" style="flex: 1; height: 34px;"></div></div>',
  "blocks": [{
   "id": "dashboard-layout", "title": "App shell",
   "html": '''<div class="dl-frame">
  <aside class="dl-side">
    <div class="dl-brand"><span class="dl-logo" aria-hidden="true">O</span><span class="dl-brandT">OWN</span></div>
    <nav class="dl-nav" aria-label="Main">
      <button class="dl-item is-on" type="button">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/></svg>
        <span class="dl-label">Overview</span>
      </button>
      <button class="dl-item" type="button">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 3h8a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>
        <span class="dl-label">Projects</span>
      </button>
      <button class="dl-item" type="button">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
        <span class="dl-label">Messages</span>
      </button>
      <button class="dl-item" type="button">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.9l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.9-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1-1.5 1.7 1.7 0 0 0-1.9.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.9 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1 1.7 1.7 0 0 0-.3-1.9l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.9.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.9-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.9V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/></svg>
        <span class="dl-label">Settings</span>
      </button>
    </nav>
    <div class="dl-promo"><span class="dl-promoT">Pro plan</span><span class="dl-promoD">Unlock analytics</span></div>
  </aside>
  <div class="dl-main">
    <div class="dl-top">
      <input class="dl-search" type="search" placeholder="Search..." aria-label="Search dashboard">
      <span class="dl-bell" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 8a6 6 0 0 0-12 0c0 7-3 7-3 9h18c0-2-3-2-3-9"/><path d="M10.3 21a2 2 0 0 0 3.4 0"/></svg>
      </span>
      <span class="dl-av" aria-hidden="true">AK</span>
    </div>
    <div class="dl-content">
      <p class="dl-h">Overview</p>
      <div class="dl-stats">
        <div class="dl-stat"><span class="dl-sk">Projects</span><span class="dl-sv">12</span></div>
        <div class="dl-stat"><span class="dl-sk">Tasks</span><span class="dl-sv">48</span></div>
        <div class="dl-stat"><span class="dl-sk">Done</span><span class="dl-sv">31</span></div>
      </div>
      <div class="dl-panel">
        <p class="dl-pt">Recent projects</p>
        <div class="dl-row"><span class="dl-pdot" style="background: var(--accent);"></span><span class="dl-pn">Website refresh</span><span class="dl-pm">6 tasks</span></div>
        <div class="dl-row"><span class="dl-pdot" style="background: var(--yes);"></span><span class="dl-pn">Mobile app</span><span class="dl-pm">4 tasks</span></div>
        <div class="dl-row"><span class="dl-pdot" style="background: var(--warn);"></span><span class="dl-pn">Brand kit</span><span class="dl-pm">2 tasks</span></div>
      </div>
    </div>
  </div>
</div>''',
   "css": '''.dl-frame { display: grid; grid-template-columns: 150px 1fr; height: 340px; border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; background: var(--card); }
.dl-side { display: flex; flex-direction: column; background: var(--bg); border-right: 1px solid var(--border); padding: 10px 8px; }
.dl-brand { display: flex; align-items: center; gap: 6px; padding: 2px 4px 12px; }
.dl-logo { width: 20px; height: 20px; border-radius: 4px; background: var(--accent); color: #fff; font-size: 0.66rem; font-weight: 800; display: flex; align-items: center; justify-content: center; }
.dl-brandT { font-size: 0.76rem; font-weight: 800; letter-spacing: 0.04em; }
.dl-nav { display: flex; flex-direction: column; gap: 2px; }
.dl-item { display: flex; align-items: center; gap: 7px; border: 0; background: transparent; color: var(--muted); font: inherit; font-size: 0.72rem; font-weight: 600; padding: 7px; border-radius: 4px; cursor: pointer; text-align: left; }
.dl-item svg { width: 14px; height: 14px; flex: 0 0 auto; }
.dl-item:hover { color: var(--text); background: var(--card); }
.dl-item.is-on { background: var(--accent-soft); color: var(--accent); }
.dl-item:focus-visible { outline: 2px solid var(--accent); outline-offset: -2px; }
.dl-promo { margin-top: auto; background: var(--accent-soft); border-radius: 4px; padding: 7px; }
.dl-promoT { display: block; font-size: 0.66rem; font-weight: 700; color: var(--accent); }
.dl-promoD { display: block; font-size: 0.6rem; color: var(--muted); }
.dl-main { display: flex; flex-direction: column; min-width: 0; }
.dl-top { display: flex; align-items: center; gap: 8px; padding: 8px 10px; border-bottom: 1px solid var(--border); }
.dl-search { flex: 1; min-width: 0; border: 1px solid var(--border); border-radius: 999px; background: var(--bg); color: var(--text); font: inherit; font-size: 0.72rem; padding: 5px 10px; outline: none; }
.dl-search:focus { border-color: var(--accent); }
.dl-bell { width: 18px; height: 18px; color: var(--muted); flex: 0 0 auto; }
.dl-bell svg { width: 100%; height: 100%; }
.dl-av { width: 24px; height: 24px; border-radius: 999px; background: linear-gradient(135deg, #4f6bed, #8b5cf6); color: #fff; font-size: 0.56rem; font-weight: 700; display: flex; align-items: center; justify-content: center; flex: 0 0 auto; }
.dl-content { padding: 10px; overflow: auto; }
.dl-h { margin: 0 0 8px; font-size: 0.8rem; font-weight: 700; }
.dl-stats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; margin-bottom: 8px; }
.dl-stat { border: 1px solid var(--border); border-radius: 4px; padding: 7px; }
.dl-sk { display: block; font-size: 0.6rem; color: var(--muted); }
.dl-sv { font-size: 0.9rem; font-weight: 800; }
.dl-panel { border: 1px solid var(--border); border-radius: 4px; padding: 8px; }
.dl-pt { margin: 0 0 4px; font-size: 0.68rem; font-weight: 700; color: var(--muted); text-transform: uppercase; letter-spacing: 0.05em; }
.dl-row { display: flex; align-items: center; gap: 6px; padding: 5px 0; border-bottom: 1px solid var(--border); }
.dl-row:last-child { border-bottom: 0; }
.dl-pdot { width: 6px; height: 6px; border-radius: 999px; flex: 0 0 auto; }
.dl-pn { flex: 1; font-size: 0.69rem; font-weight: 600; }
.dl-pm { font-size: 0.62rem; color: var(--muted); }
@media (max-width: 520px) {
  .dl-frame { grid-template-columns: 44px 1fr; }
  .dl-label, .dl-brandT, .dl-promo { display: none; }
  .dl-item { justify-content: center; }
  .dl-brand { justify-content: center; padding: 2px 0 12px; }
}''',
  }],
 },
 {
  "folder": "dashboard", "slug": "analytics", "title": "Analytics Overview",
  "desc": "Range picker, KPI row, bar chart and channel ranking.",
  "idx_desc": "Analytics KPIs, bar chart and channel ranking.",
  "mini": '<div class="p-bars"><span></span><span></span><span></span><span></span></div>',
  "blocks": [{
   "id": "analytics-overview", "title": "Analytics",
   "html": '''<div class="an-card">
  <div class="an-head">
    <span class="an-t">Analytics</span>
    <div class="an-range" role="group" aria-label="Date range">
      <button class="an-r is-on" type="button">7d</button>
      <button class="an-r" type="button">30d</button>
      <button class="an-r" type="button">90d</button>
    </div>
  </div>
  <div class="an-kpis">
    <div class="an-k"><span class="an-kl">Visitors</span><span class="an-kv">12.4k</span><span class="an-kd is-up">+8.2%</span></div>
    <div class="an-k"><span class="an-kl">Sessions</span><span class="an-kv">18.1k</span><span class="an-kd is-up">+4.6%</span></div>
    <div class="an-k"><span class="an-kl">Bounce</span><span class="an-kv">32%</span><span class="an-kd is-down">-1.4%</span></div>
  </div>
  <p class="an-sub">Sessions this week</p>
  <div class="an-bars" role="img" aria-label="Sessions by day, highest on Saturday">
    <span class="an-bar" style="height: 40%"></span><span class="an-bar" style="height: 55%"></span><span class="an-bar" style="height: 48%"></span><span class="an-bar" style="height: 66%"></span><span class="an-bar" style="height: 58%"></span><span class="an-bar is-hot" style="height: 86%"></span><span class="an-bar" style="height: 72%"></span>
  </div>
  <div class="an-days" aria-hidden="true"><span class="an-d">M</span><span class="an-d">T</span><span class="an-d">W</span><span class="an-d">T</span><span class="an-d">F</span><span class="an-d">S</span><span class="an-d">S</span></div>
  <p class="an-sub">Top channels</p>
  <div class="an-ch"><span class="an-cn">Direct</span><span class="an-ct"><span class="an-cf" style="width: 62%"></span></span><span class="an-cp">62%</span></div>
  <div class="an-ch"><span class="an-cn">Search</span><span class="an-ct"><span class="an-cf" style="width: 26%"></span></span><span class="an-cp">26%</span></div>
  <div class="an-ch"><span class="an-cn">Social</span><span class="an-ct"><span class="an-cf" style="width: 12%"></span></span><span class="an-cp">12%</span></div>
</div>''',
   "css": '''.an-card { max-width: 400px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 14px; }
.an-head { display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-bottom: 10px; }
.an-t { font-size: 0.86rem; font-weight: 700; }
.an-range { display: flex; gap: 2px; background: var(--bg); border-radius: 999px; padding: 2px; }
.an-r { border: 0; background: transparent; color: var(--muted); font: inherit; font-size: 0.65rem; font-weight: 700; padding: 3px 8px; border-radius: 999px; cursor: pointer; }
.an-r.is-on { background: var(--accent); color: #fff; }
.an-r:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.an-kpis { display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; margin-bottom: 12px; }
.an-k { border: 1px solid var(--border); border-radius: 4px; padding: 7px; display: flex; flex-direction: column; gap: 1px; }
.an-kl { font-size: 0.58rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.05em; }
.an-kv { font-size: 0.95rem; font-weight: 800; }
.an-kd { font-size: 0.6rem; font-weight: 600; }
.an-kd.is-up { color: var(--yes); }
.an-kd.is-down { color: var(--no); }
.an-sub { margin: 10px 0 6px; font-size: 0.66rem; font-weight: 700; color: var(--muted); text-transform: uppercase; letter-spacing: 0.05em; }
.an-bars { display: flex; align-items: flex-end; gap: 6px; height: 90px; }
.an-bar { flex: 1; background: var(--accent-soft); border-radius: 2px 2px 0 0; }
.an-bar.is-hot { background: var(--accent); }
.an-days { display: flex; justify-content: space-between; margin-top: 4px; }
.an-d { flex: 1; text-align: center; font-size: 0.58rem; color: var(--muted); }
.an-ch { display: flex; align-items: center; gap: 6px; margin-bottom: 4px; }
.an-cn { width: 44px; font-size: 0.66rem; color: var(--muted); }
.an-ct { flex: 1; height: 5px; border-radius: 999px; background: var(--bg); overflow: hidden; }
.an-cf { display: block; height: 100%; background: var(--accent); border-radius: 999px; }
.an-cp { width: 28px; text-align: right; font-size: 0.64rem; font-weight: 700; }''',
   "js": '''(function () {
  var btns = Array.prototype.slice.call(document.querySelectorAll(".an-r"));
  btns.forEach(function (b) {
    b.addEventListener("click", function () {
      btns.forEach(function (x) { x.classList.remove("is-on"); });
      b.classList.add("is-on");
    });
  });
})();''',
  }],
 },
 {
  "folder": "dashboard", "slug": "wallet", "title": "Wallet Card",
  "desc": "Balance, virtual card and recent transactions.",
  "idx_desc": "Wallet balance, virtual card and recent activity.",
  "mini": '<div class="p-card" style="width: 44px; height: 26px; background: linear-gradient(135deg, #4f6bed, #8b5cf6);"></div>',
  "blocks": [{
   "id": "wallet-card", "title": "Wallet",
   "html": '''<div class="wa-card">
  <div class="wa-bal">
    <span class="wa-lb">Available balance</span>
    <span class="wa-v">$4,862.40</span>
    <span class="wa-d">+$240 this week</span>
  </div>
  <div class="wa-actions">
    <button class="wa-btn" type="button">Add money</button>
    <button class="wa-btn wa-ghost" type="button">Send</button>
  </div>
  <div class="wa-visa" aria-label="Visa card ending 4242">
    <div class="wa-visaTop"><span class="wa-chip" aria-hidden="true"></span><span class="wa-brand">VISA</span></div>
    <span class="wa-num">4242 &#8226;&#8226;&#8226;&#8226; &#8226;&#8226;&#8226;&#8226; 8210</span>
    <div class="wa-visaBot"><span class="wa-holder">AYESHA KHAN</span><span class="wa-exp">09/29</span></div>
  </div>
  <p class="wa-sub">Recent</p>
  <ul class="wa-list">
    <li class="wa-item"><span class="wa-ii" aria-hidden="true">&#8595;</span><div><p class="wa-it">Figma subscription</p><p class="wa-id">Today, 10:24</p></div><span class="wa-amt is-out">-$15.00</span></li>
    <li class="wa-item"><span class="wa-ii is-in" aria-hidden="true">&#8593;</span><div><p class="wa-it">Client payment</p><p class="wa-id">Yesterday</p></div><span class="wa-amt is-in">+$1,200.00</span></li>
    <li class="wa-item"><span class="wa-ii" aria-hidden="true">&#8595;</span><div><p class="wa-it">Cloud hosting</p><p class="wa-id">20 Oct</p></div><span class="wa-amt is-out">-$28.00</span></li>
  </ul>
</div>''',
   "css": '''.wa-card { max-width: 340px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 14px; }
.wa-bal { display: flex; flex-direction: column; gap: 1px; margin-bottom: 10px; }
.wa-lb { font-size: 0.66rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.05em; }
.wa-v { font-size: 1.5rem; font-weight: 800; letter-spacing: -0.02em; }
.wa-d { font-size: 0.66rem; color: var(--yes); font-weight: 600; }
.wa-actions { display: flex; gap: 7px; margin-bottom: 12px; }
.wa-btn { flex: 1; border: 0; background: var(--accent); color: #fff; font: inherit; font-size: 0.72rem; font-weight: 600; padding: 7px; border-radius: var(--radius); cursor: pointer; }
.wa-btn:hover { opacity: 0.92; }
.wa-ghost { background: transparent; border: 1px solid var(--border); color: var(--text); }
.wa-ghost:hover { border-color: var(--accent); color: var(--accent); opacity: 1; }
.wa-btn:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.wa-visa { background: linear-gradient(135deg, #2a2350, #4f6bed 60%, #8b5cf6); border-radius: 10px; padding: 12px; color: #fff; margin-bottom: 12px; }
.wa-visaTop { display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px; }
.wa-chip { width: 24px; height: 17px; border-radius: 3px; background: linear-gradient(135deg, #f5d787, #c9a44c); }
.wa-brand { font-size: 0.72rem; font-weight: 800; letter-spacing: 0.08em; font-style: italic; }
.wa-num { display: block; font-size: 0.76rem; letter-spacing: 0.12em; margin-bottom: 10px; font-variant-numeric: tabular-nums; }
.wa-visaBot { display: flex; align-items: center; justify-content: space-between; font-size: 0.58rem; color: rgba(255, 255, 255, 0.8); letter-spacing: 0.06em; }
.wa-sub { margin: 0 0 4px; font-size: 0.64rem; font-weight: 700; color: var(--muted); text-transform: uppercase; letter-spacing: 0.05em; }
.wa-list { list-style: none; margin: 0; padding: 0; }
.wa-item { display: flex; align-items: center; gap: 8px; padding: 6px 0; border-bottom: 1px solid var(--border); }
.wa-item:last-child { border-bottom: 0; }
.wa-ii { width: 24px; height: 24px; border-radius: 999px; background: var(--bg); color: var(--no); font-size: 0.7rem; display: flex; align-items: center; justify-content: center; flex: 0 0 auto; }
.wa-ii.is-in { color: var(--yes); }
.wa-item > div { flex: 1; min-width: 0; }
.wa-it { margin: 0; font-size: 0.72rem; font-weight: 600; }
.wa-id { margin: 1px 0 0; font-size: 0.62rem; color: var(--muted); }
.wa-amt { font-size: 0.72rem; font-weight: 700; }
.wa-amt.is-out { color: var(--text); }
.wa-amt.is-in { color: var(--yes); }''',
  }],
 },
 {
  "folder": "dashboard", "slug": "transactions", "title": "Transactions List",
  "desc": "Payment rows with status chips and a filter bar.",
  "idx_desc": "Payment rows with status chips and filters.",
  "mini": '<div class="p-table" style="height: 44px;"><span></span><span></span></div>',
  "blocks": [{
   "id": "transactions", "title": "Transactions",
   "html": '''<div class="tx-card">
  <div class="tx-head">
    <span class="tx-t">Transactions</span>
    <button class="tx-export" type="button" id="txExport">Export CSV</button>
  </div>
  <div class="tx-filters" role="group" aria-label="Filter transactions">
    <button class="tx-f is-on" type="button" data-f="all">All</button>
    <button class="tx-f" type="button" data-f="paid">Paid</button>
    <button class="tx-f" type="button" data-f="pending">Pending</button>
    <button class="tx-f" type="button" data-f="failed">Failed</button>
  </div>
  <ul class="tx-list" id="txList">
    <li class="tx-item" data-s="paid"><span class="tx-av">FC</span><div class="tx-m"><p class="tx-n">Figma subscription</p><p class="tx-d">22 Oct 2026 &#183; Card</p></div><span class="tx-amt">$15.00</span><span class="tx-badge is-paid">Paid</span></li>
    <li class="tx-item" data-s="paid"><span class="tx-av">CL</span><div class="tx-m"><p class="tx-n">Cloud hosting</p><p class="tx-d">20 Oct 2026 &#183; Card</p></div><span class="tx-amt">$28.00</span><span class="tx-badge is-paid">Paid</span></li>
    <li class="tx-item" data-s="pending"><span class="tx-av">AC</span><div class="tx-m"><p class="tx-n">Agency invoice</p><p class="tx-d">18 Oct 2026 &#183; Bank</p></div><span class="tx-amt">$840.00</span><span class="tx-badge is-pending">Pending</span></li>
    <li class="tx-item" data-s="failed"><span class="tx-av">SP</span><div class="tx-m"><p class="tx-n">Stock photos</p><p class="tx-d">17 Oct 2026 &#183; Card</p></div><span class="tx-amt">$12.00</span><span class="tx-badge is-failed">Failed</span></li>
    <li class="tx-item" data-s="paid"><span class="tx-av">SW</span><div class="tx-m"><p class="tx-n">Software license</p><p class="tx-d">15 Oct 2026 &#183; Card</p></div><span class="tx-amt">$99.00</span><span class="tx-badge is-paid">Paid</span></li>
  </ul>
  <p class="tx-msg" id="txMsg" aria-live="polite"></p>
</div>''',
   "css": '''.tx-card { max-width: 420px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 12px; }
.tx-head { display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-bottom: 8px; }
.tx-t { font-size: 0.82rem; font-weight: 700; }
.tx-export { border: 1px solid var(--border); background: transparent; color: var(--accent); font: inherit; font-size: 0.66rem; font-weight: 700; padding: 4px 8px; border-radius: 4px; cursor: pointer; }
.tx-export:hover { border-color: var(--accent); }
.tx-export:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.tx-filters { display: flex; gap: 4px; flex-wrap: wrap; margin-bottom: 8px; }
.tx-f { border: 1px solid var(--border); background: transparent; color: var(--muted); font: inherit; font-size: 0.64rem; font-weight: 600; padding: 3px 8px; border-radius: 999px; cursor: pointer; }
.tx-f.is-on { background: var(--accent); border-color: var(--accent); color: #fff; }
.tx-f:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.tx-list { list-style: none; margin: 0; padding: 0; }
.tx-item { display: flex; align-items: center; gap: 8px; padding: 7px 0; border-bottom: 1px solid var(--border); }
.tx-item:last-child { border-bottom: 0; }
.tx-av { width: 28px; height: 28px; border-radius: 999px; background: var(--bg); color: var(--muted); font-size: 0.58rem; font-weight: 700; display: flex; align-items: center; justify-content: center; flex: 0 0 auto; }
.tx-m { flex: 1; min-width: 0; }
.tx-n { margin: 0; font-size: 0.72rem; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.tx-d { margin: 1px 0 0; font-size: 0.61rem; color: var(--muted); }
.tx-amt { font-size: 0.71rem; font-weight: 700; white-space: nowrap; }
.tx-badge { font-size: 0.56rem; font-weight: 700; padding: 2px 6px; border-radius: 999px; white-space: nowrap; }
.tx-badge.is-paid { background: rgba(34, 160, 107, 0.12); color: var(--yes); }
.tx-badge.is-pending { background: rgba(194, 116, 10, 0.12); color: var(--warn); }
.tx-badge.is-failed { background: rgba(229, 72, 77, 0.1); color: var(--no); }
.tx-msg { min-height: 1em; margin: 6px 0 0; font-size: 0.66rem; color: var(--muted); }''',
   "js": '''(function () {
  var items = Array.prototype.slice.call(document.querySelectorAll(".tx-item"));
  var btns = Array.prototype.slice.call(document.querySelectorAll(".tx-f"));
  var msg = document.getElementById("txMsg");

  btns.forEach(function (b) {
    b.addEventListener("click", function () {
      btns.forEach(function (x) { x.classList.remove("is-on"); });
      b.classList.add("is-on");
      var f = b.getAttribute("data-f");
      var n = 0;
      items.forEach(function (it) {
        var show = f === "all" || it.getAttribute("data-s") === f;
        it.hidden = !show;
        if (show) n += 1;
      });
      msg.textContent = n + " transaction" + (n === 1 ? "" : "s") + " shown.";
    });
  });

  document.getElementById("txExport").addEventListener("click", function () {
    msg.textContent = "Export queued (demo).";
  });
})();''',
  }],
 },
 {
  "folder": "dashboard", "slug": "search-filter", "title": "Search & Filter",
  "desc": "Live search with toggleable category filters.",
  "idx_desc": "Live search with toggleable category filters.",
  "mini": '<div class="p-search" style="width: 48px;"></div><div class="p-line" style="width: 20px;"></div>',
  "blocks": [{
   "id": "search-filter", "title": "Filtered results",
   "html": '''<div class="sf-card">
  <div class="sf-bar">
    <svg class="sf-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>
    <input class="sf-input" id="sfInput" type="search" placeholder="Search documents..." aria-label="Search documents">
  </div>
  <div class="sf-chips" role="group" aria-label="Categories">
    <button class="sf-chip is-on" type="button" data-c="all">All</button>
    <button class="sf-chip" type="button" data-c="design">Design</button>
    <button class="sf-chip" type="button" data-c="dev">Development</button>
    <button class="sf-chip" type="button" data-c="ops">Operations</button>
  </div>
  <p class="sf-count" id="sfCount">3 results</p>
  <ul class="sf-list" id="sfList">
    <li class="sf-item" data-c="design"><span class="sf-doc" aria-hidden="true">PDF</span><div class="sf-m"><p class="sf-n">Brand guidelines</p><p class="sf-d">Design &#183; Updated 2 days ago</p></div></li>
    <li class="sf-item" data-c="dev"><span class="sf-doc" aria-hidden="true">MD</span><div class="sf-m"><p class="sf-n">API reference</p><p class="sf-d">Development &#183; Updated today</p></div></li>
    <li class="sf-item" data-c="ops"><span class="sf-doc" aria-hidden="true">XLS</span><div class="sf-m"><p class="sf-n">Q4 budget</p><p class="sf-d">Operations &#183; Updated last week</p></div></li>
    <li class="sf-item" data-c="design"><span class="sf-doc" aria-hidden="true">FIG</span><div class="sf-m"><p class="sf-n">Mobile screens</p><p class="sf-d">Design &#183; Updated 4 days ago</p></div></li>
  </ul>
  <p class="sf-empty" id="sfEmpty" hidden>No documents match your search.</p>
</div>''',
   "css": '''.sf-card { max-width: 400px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 12px; }
.sf-bar { display: flex; align-items: center; gap: 7px; border: 1px solid var(--border); border-radius: 999px; background: var(--bg); padding: 5px 10px; margin-bottom: 8px; }
.sf-bar:focus-within { border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-soft); }
.sf-ic { width: 14px; height: 14px; color: var(--muted); flex: 0 0 auto; }
.sf-input { flex: 1; min-width: 0; border: 0; background: transparent; color: var(--text); font: inherit; font-size: 0.75rem; outline: none; padding: 3px 0; }
.sf-chips { display: flex; gap: 4px; flex-wrap: wrap; margin-bottom: 6px; }
.sf-chip { border: 1px solid var(--border); background: transparent; color: var(--muted); font: inherit; font-size: 0.64rem; font-weight: 600; padding: 3px 8px; border-radius: 999px; cursor: pointer; }
.sf-chip.is-on { background: var(--accent-soft); border-color: var(--accent); color: var(--accent); }
.sf-chip:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.sf-count { margin: 0 0 4px; font-size: 0.62rem; color: var(--muted); }
.sf-list { list-style: none; margin: 0; padding: 0; }
.sf-item { display: flex; align-items: center; gap: 8px; padding: 6px 0; border-bottom: 1px solid var(--border); }
.sf-item:last-child { border-bottom: 0; }
.sf-doc { width: 28px; height: 28px; border-radius: 4px; background: var(--bg); color: var(--accent); font-size: 0.52rem; font-weight: 800; display: flex; align-items: center; justify-content: center; flex: 0 0 auto; }
.sf-m { min-width: 0; }
.sf-n { margin: 0; font-size: 0.73rem; font-weight: 600; }
.sf-d { margin: 1px 0 0; font-size: 0.62rem; color: var(--muted); }
.sf-empty { margin: 8px 0 0; font-size: 0.72rem; color: var(--muted); text-align: center; padding: 8px 0; }''',
   "js": '''(function () {
  var input = document.getElementById("sfInput");
  var chips = Array.prototype.slice.call(document.querySelectorAll(".sf-chip"));
  var items = Array.prototype.slice.call(document.querySelectorAll(".sf-item"));
  var count = document.getElementById("sfCount");
  var empty = document.getElementById("sfEmpty");
  var cat = "all";

  function paint() {
    var q = input.value.trim().toLowerCase();
    var n = 0;
    items.forEach(function (it) {
      var okCat = cat === "all" || it.getAttribute("data-c") === cat;
      var okText = it.textContent.toLowerCase().indexOf(q) > -1;
      var show = okCat && okText;
      it.hidden = !show;
      if (show) n += 1;
    });
    count.textContent = n + " result" + (n === 1 ? "" : "s");
    empty.hidden = n > 0;
  }

  input.addEventListener("input", paint);
  chips.forEach(function (c) {
    c.addEventListener("click", function () {
      chips.forEach(function (x) { x.classList.remove("is-on"); });
      c.classList.add("is-on");
      cat = c.getAttribute("data-c");
      paint();
    });
  });
  paint();
})();''',
  }],
 },
 {
  "folder": "dashboard", "slug": "admin-panel", "title": "Admin Panel",
  "desc": "User administration rows with roles and actions.",
  "idx_desc": "User administration rows with roles and actions.",
  "mini": '<div class="p-table" style="height: 44px;"><span></span><span></span><span></span></div>',
  "blocks": [{
   "id": "admin-panel", "title": "Admin users",
   "html": '''<div class="ad-card">
  <div class="ad-head">
    <div><p class="ad-t">Team members</p><p class="ad-s">Manage roles and access</p></div>
    <button class="ad-invite" type="button" id="adInvite">Invite</button>
  </div>
  <div class="ad-scroll">
    <table class="ad-table">
      <thead><tr><th class="ad-th">Member</th><th class="ad-th">Role</th><th class="ad-th">Last active</th><th class="ad-th ad-actcol">Actions</th></tr></thead>
      <tbody>
        <tr class="ad-tr"><td class="ad-td"><div class="ad-user"><span class="ad-av a1">AK</span><div><p class="ad-n">Ayesha Khan</p><p class="ad-e">ayesha@own.dev</p></div></div></td><td class="ad-td"><span class="ad-role is-admin">Admin</span></td><td class="ad-td ad-mut">2 min ago</td><td class="ad-td ad-actcol"><button class="ad-manage" type="button">Manage</button></td></tr>
        <tr class="ad-tr"><td class="ad-td"><div class="ad-user"><span class="ad-av a2">RS</span><div><p class="ad-n">Rohan Shah</p><p class="ad-e">rohan@own.dev</p></div></div></td><td class="ad-td"><span class="ad-role is-editor">Editor</span></td><td class="ad-td ad-mut">1 hour ago</td><td class="ad-td ad-actcol"><button class="ad-manage" type="button">Manage</button></td></tr>
        <tr class="ad-tr"><td class="ad-td"><div class="ad-user"><span class="ad-av a3">MP</span><div><p class="ad-n">Mira Patel</p><p class="ad-e">mira@own.dev</p></div></div></td><td class="ad-td"><span class="ad-role is-viewer">Viewer</span></td><td class="ad-td ad-mut">Yesterday</td><td class="ad-td ad-actcol"><button class="ad-manage" type="button">Manage</button></td></tr>
      </tbody>
    </table>
  </div>
  <p class="ad-msg" id="adMsg" aria-live="polite"></p>
</div>''',
   "css": '''.ad-card { max-width: 430px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 12px; }
.ad-head { display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-bottom: 8px; }
.ad-t { margin: 0; font-size: 0.8rem; font-weight: 700; }
.ad-s { margin: 1px 0 0; font-size: 0.62rem; color: var(--muted); }
.ad-invite { border: 0; background: var(--accent); color: #fff; font: inherit; font-size: 0.68rem; font-weight: 700; padding: 5px 11px; border-radius: 4px; cursor: pointer; }
.ad-invite:hover { opacity: 0.92; }
.ad-invite:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.ad-scroll { overflow-x: auto; }
.ad-table { width: 100%; border-collapse: collapse; min-width: 390px; }
.ad-th { text-align: left; font-size: 0.58rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--muted); padding: 6px 5px; border-bottom: 1px solid var(--border); }
.ad-td { padding: 7px 5px; border-bottom: 1px solid var(--border); font-size: 0.7rem; }
.ad-actcol { text-align: right; }
.ad-user { display: flex; align-items: center; gap: 6px; }
.ad-av { width: 24px; height: 24px; border-radius: 999px; color: #fff; font-size: 0.52rem; font-weight: 700; display: flex; align-items: center; justify-content: center; flex: 0 0 auto; }
.a1 { background: linear-gradient(135deg, #4f6bed, #8b5cf6); }
.a2 { background: linear-gradient(135deg, #22a06b, #0ea5e9); }
.a3 { background: linear-gradient(135deg, #e5484d, #f0b543); }
.ad-n { margin: 0; font-size: 0.7rem; font-weight: 600; }
.ad-e { margin: 0; font-size: 0.58rem; color: var(--muted); }
.ad-role { font-size: 0.56rem; font-weight: 700; padding: 2px 6px; border-radius: 999px; }
.ad-role.is-admin { background: var(--accent-soft); color: var(--accent); }
.ad-role.is-editor { background: rgba(34, 160, 107, 0.12); color: var(--yes); }
.ad-role.is-viewer { background: var(--bg); color: var(--muted); }
.ad-mut { color: var(--muted); font-size: 0.64rem; white-space: nowrap; }
.ad-manage { border: 1px solid var(--border); background: transparent; color: var(--muted); font: inherit; font-size: 0.58rem; font-weight: 600; padding: 3px 7px; border-radius: 4px; cursor: pointer; }
.ad-manage:hover { border-color: var(--accent); color: var(--accent); }
.ad-manage:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.ad-msg { min-height: 1em; margin: 6px 0 0; font-size: 0.64rem; color: var(--muted); }''',
   "js": '''(function () {
  var msg = document.getElementById("adMsg");
  document.getElementById("adInvite").addEventListener("click", function () {
    msg.textContent = "Invite link copied (demo).";
  });
  document.querySelectorAll(".ad-manage").forEach(function (b) {
    b.addEventListener("click", function () {
      var name = b.closest(".ad-tr").querySelector(".ad-n").textContent;
      msg.textContent = "Managing " + name + " (demo).";
    });
  });
})();''',
  }],
 },
 {
  "folder": "dashboard", "slug": "settings-panel", "title": "Settings Panel",
  "desc": "Tabbed settings with toggle switches.",
  "idx_desc": "Tabbed settings with toggle switches.",
  "mini": '<div class="p-row"><span class="p-line" style="width: 24px;"></span><span class="p-tog"></span></div>',
  "blocks": [{
   "id": "settings-panel", "title": "Workspace settings",
   "html": '''<div class="ds-card">
  <div class="ds-tabs" role="tablist" aria-label="Settings sections">
    <button class="ds-tab is-on" type="button" role="tab" aria-selected="true" data-p="general">General</button>
    <button class="ds-tab" type="button" role="tab" aria-selected="false" data-p="notify">Notifications</button>
    <button class="ds-tab" type="button" role="tab" aria-selected="false" data-p="security">Security</button>
  </div>
  <div class="ds-panel" id="dsGeneral">
    <label class="ds-lbl" for="dsName">Workspace name</label>
    <input class="ds-input" id="dsName" type="text" value="OWN Studio">
    <label class="ds-lbl" for="dsUrl">Workspace URL</label>
    <input class="ds-input" id="dsUrl" type="text" value="own.studio">
  </div>
  <div class="ds-panel" id="dsNotify" hidden>
    <div class="ds-row"><div><p class="ds-rt">Product updates</p><p class="ds-rd">Monthly changelog email.</p></div><label class="ds-switch"><input class="ds-toggle" type="checkbox" checked aria-label="Product updates"><span class="ds-slider"></span></label></div>
    <div class="ds-row"><div><p class="ds-rt">Comments</p><p class="ds-rd">When someone mentions you.</p></div><label class="ds-switch"><input class="ds-toggle" type="checkbox" checked aria-label="Comments"><span class="ds-slider"></span></label></div>
    <div class="ds-row"><div><p class="ds-rt">Weekly digest</p><p class="ds-rd">Summary every Monday.</p></div><label class="ds-switch"><input class="ds-toggle" type="checkbox" aria-label="Weekly digest"><span class="ds-slider"></span></label></div>
  </div>
  <div class="ds-panel" id="dsSecurity" hidden>
    <div class="ds-row"><div><p class="ds-rt">Two-factor auth</p><p class="ds-rd">Require a code at sign-in.</p></div><label class="ds-switch"><input class="ds-toggle" type="checkbox" checked aria-label="Two-factor auth"><span class="ds-slider"></span></label></div>
    <div class="ds-row"><div><p class="ds-rt">Session alerts</p><p class="ds-rd">Email on new device login.</p></div><label class="ds-switch"><input class="ds-toggle" type="checkbox" aria-label="Session alerts"><span class="ds-slider"></span></label></div>
  </div>
  <div class="ds-foot"><button class="ds-save" type="button" id="dsSave">Save changes</button></div>
  <p class="ds-msg" id="dsMsg" role="status"></p>
</div>''',
   "css": '''.ds-card { max-width: 380px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 12px; }
.ds-tabs { display: flex; gap: 3px; border-bottom: 1px solid var(--border); margin-bottom: 10px; }
.ds-tab { border: 0; background: transparent; color: var(--muted); font: inherit; font-size: 0.68rem; font-weight: 600; padding: 6px 7px; cursor: pointer; border-bottom: 2px solid transparent; margin-bottom: -1px; }
.ds-tab.is-on { color: var(--accent); border-bottom-color: var(--accent); }
.ds-tab:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.ds-lbl { display: block; margin: 0 0 4px; font-size: 0.64rem; font-weight: 600; color: var(--muted); }
.ds-input { width: 100%; border: 1px solid var(--border); border-radius: var(--radius); background: var(--bg); color: var(--text); font: inherit; font-size: 0.74rem; padding: 6px 8px; margin-bottom: 9px; outline: none; }
.ds-input:focus { border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-soft); }
.ds-row { display: flex; align-items: center; justify-content: space-between; gap: 10px; padding: 8px 0; border-bottom: 1px solid var(--border); }
.ds-row:last-child { border-bottom: 0; }
.ds-rt { margin: 0; font-size: 0.72rem; font-weight: 600; }
.ds-rd { margin: 1px 0 0; font-size: 0.6rem; color: var(--muted); }
.ds-switch { position: relative; width: 34px; height: 19px; flex: 0 0 auto; display: inline-block; }
.ds-toggle { opacity: 0; width: 0; height: 0; position: absolute; }
.ds-slider { position: absolute; inset: 0; background: var(--track-off); border-radius: 999px; cursor: pointer; transition: background 0.2s; }
.ds-slider::before { content: ""; position: absolute; width: 15px; height: 15px; left: 2px; top: 2px; background: #fff; border-radius: 999px; transition: transform 0.2s; }
.ds-toggle:checked + .ds-slider { background: var(--accent); }
.ds-toggle:checked + .ds-slider::before { transform: translateX(15px); }
.ds-toggle:focus-visible + .ds-slider { outline: 2px solid var(--accent); outline-offset: 2px; }
.ds-foot { margin-top: 10px; display: flex; justify-content: flex-end; }
.ds-save { border: 0; background: var(--accent); color: #fff; font: inherit; font-size: 0.7rem; font-weight: 600; padding: 6px 12px; border-radius: 4px; cursor: pointer; }
.ds-save:hover { opacity: 0.92; }
.ds-save:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.ds-msg { min-height: 1em; margin: 6px 0 0; font-size: 0.64rem; color: var(--yes); text-align: right; }''',
   "js": '''(function () {
  var tabs = Array.prototype.slice.call(document.querySelectorAll(".ds-tab"));
  var panels = { general: document.getElementById("dsGeneral"), notify: document.getElementById("dsNotify"), security: document.getElementById("dsSecurity") };

  tabs.forEach(function (t) {
    t.addEventListener("click", function () {
      tabs.forEach(function (x) {
        x.classList.remove("is-on");
        x.setAttribute("aria-selected", "false");
      });
      t.classList.add("is-on");
      t.setAttribute("aria-selected", "true");
      Object.keys(panels).forEach(function (k) { panels[k].hidden = k !== t.getAttribute("data-p"); });
    });
  });

  var msg = document.getElementById("dsMsg");
  document.getElementById("dsSave").addEventListener("click", function () {
    msg.textContent = "Settings saved.";
  });
})();''',
  }],
 },
 {
  "folder": "dashboard", "slug": "user-table", "title": "User Table",
  "desc": "Member table with avatars, status and pagination.",
  "idx_desc": "Member table with avatars and pagination.",
  "mini": '<div class="p-table" style="height: 44px;"><span></span><span></span></div><div class="p-line" style="width: 26px;"></div>',
  "blocks": [{
   "id": "user-table", "title": "Team directory",
   "html": '''<div class="ut-card">
  <div class="ut-head">
    <span class="ut-t">Team directory</span>
    <span class="ut-pill">24 members</span>
  </div>
  <div class="ut-scroll">
    <table class="ut-table">
      <thead><tr><th class="ut-th">User</th><th class="ut-th">Department</th><th class="ut-th">Status</th><th class="ut-th ut-last"></th></tr></thead>
      <tbody>
        <tr class="ut-tr"><td class="ut-td"><div class="ut-u"><span class="ut-av u1">AK</span><div><p class="ut-n">Ayesha Khan</p><p class="ut-e">ayesha@own.dev</p></div></div></td><td class="ut-td ut-mut">Design</td><td class="ut-td"><span class="ut-st is-on"><span class="ut-dot"></span>Active</span></td><td class="ut-td ut-last"><button class="ut-more" type="button" aria-label="More actions for Ayesha">&#8942;</button></td></tr>
        <tr class="ut-tr"><td class="ut-td"><div class="ut-u"><span class="ut-av u2">RS</span><div><p class="ut-n">Rohan Shah</p><p class="ut-e">rohan@own.dev</p></div></div></td><td class="ut-td ut-mut">Engineering</td><td class="ut-td"><span class="ut-st is-on"><span class="ut-dot"></span>Active</span></td><td class="ut-td ut-last"><button class="ut-more" type="button" aria-label="More actions for Rohan">&#8942;</button></td></tr>
        <tr class="ut-tr"><td class="ut-td"><div class="ut-u"><span class="ut-av u3">MP</span><div><p class="ut-n">Mira Patel</p><p class="ut-e">mira@own.dev</p></div></div></td><td class="ut-td ut-mut">Marketing</td><td class="ut-td"><span class="ut-st is-away"><span class="ut-dot"></span>Away</span></td><td class="ut-td ut-last"><button class="ut-more" type="button" aria-label="More actions for Mira">&#8942;</button></td></tr>
        <tr class="ut-tr"><td class="ut-td"><div class="ut-u"><span class="ut-av u4">TN</span><div><p class="ut-n">Tarun Nair</p><p class="ut-e">tarun@own.dev</p></div></div></td><td class="ut-td ut-mut">Engineering</td><td class="ut-td"><span class="ut-st is-off"><span class="ut-dot"></span>Offline</span></td><td class="ut-td ut-last"><button class="ut-more" type="button" aria-label="More actions for Tarun">&#8942;</button></td></tr>
      </tbody>
    </table>
  </div>
  <div class="ut-foot">
    <span class="ut-show">Showing 1-4 of 24</span>
    <div class="ut-pages">
      <button class="ut-pg" type="button" aria-label="Previous page" disabled>&#8249;</button>
      <button class="ut-pg is-on" type="button" aria-current="page">1</button>
      <button class="ut-pg" type="button">2</button>
      <button class="ut-pg" type="button" aria-label="Next page">&#8250;</button>
    </div>
  </div>
</div>''',
   "css": '''.ut-card { max-width: 430px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 12px; }
.ut-head { display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-bottom: 8px; }
.ut-t { font-size: 0.8rem; font-weight: 700; }
.ut-pill { font-size: 0.58rem; font-weight: 700; color: var(--accent); background: var(--accent-soft); padding: 2px 7px; border-radius: 999px; }
.ut-scroll { overflow-x: auto; }
.ut-table { width: 100%; border-collapse: collapse; min-width: 360px; }
.ut-th { text-align: left; font-size: 0.58rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--muted); padding: 5px; border-bottom: 1px solid var(--border); }
.ut-last { text-align: right; width: 28px; }
.ut-tr:hover { background: var(--bg); }
.ut-td { padding: 7px 5px; border-bottom: 1px solid var(--border); font-size: 0.68rem; }
.ut-u { display: flex; align-items: center; gap: 6px; }
.ut-av { width: 24px; height: 24px; border-radius: 999px; color: #fff; font-size: 0.52rem; font-weight: 700; display: flex; align-items: center; justify-content: center; flex: 0 0 auto; }
.u1 { background: linear-gradient(135deg, #4f6bed, #8b5cf6); }
.u2 { background: linear-gradient(135deg, #22a06b, #0ea5e9); }
.u3 { background: linear-gradient(135deg, #e5484d, #f0b543); }
.u4 { background: linear-gradient(135deg, #8b5cf6, #e5484d); }
.ut-n { margin: 0; font-size: 0.68rem; font-weight: 600; }
.ut-e { margin: 0; font-size: 0.56rem; color: var(--muted); }
.ut-mut { color: var(--muted); font-size: 0.64rem; }
.ut-st { display: inline-flex; align-items: center; gap: 4px; font-size: 0.6rem; font-weight: 600; }
.ut-dot { width: 5px; height: 5px; border-radius: 999px; background: currentColor; }
.ut-st.is-on { color: var(--yes); }
.ut-st.is-away { color: var(--warn); }
.ut-st.is-off { color: var(--muted); }
.ut-more { border: 0; background: transparent; color: var(--muted); font-size: 0.9rem; cursor: pointer; padding: 1px 4px; border-radius: 3px; line-height: 1; }
.ut-more:hover { background: var(--bg); color: var(--text); }
.ut-more:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.ut-foot { display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-top: 8px; flex-wrap: wrap; }
.ut-show { font-size: 0.6rem; color: var(--muted); }
.ut-pages { display: flex; gap: 3px; }
.ut-pg { min-width: 20px; height: 20px; border: 1px solid var(--border); background: transparent; color: var(--muted); font: inherit; font-size: 0.6rem; border-radius: 3px; cursor: pointer; padding: 0 4px; }
.ut-pg.is-on { background: var(--accent); border-color: var(--accent); color: #fff; }
.ut-pg[disabled] { opacity: 0.4; cursor: default; }
.ut-pg:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }''',
  }],
 },
 {
  "folder": "dashboard", "slug": "activity-logs", "title": "Activity Logs",
  "desc": "Audit log entries with type filters and times.",
  "idx_desc": "Audit log entries with type filters and times.",
  "mini": '<div class="p-tl"><span></span><span></span><span></span></div>',
  "blocks": [{
   "id": "activity-logs", "title": "Audit log",
   "html": '''<div class="al-card">
  <div class="al-head">
    <span class="al-t">Activity log</span>
    <button class="al-clear" type="button" id="alClear">Clear view</button>
  </div>
  <div class="al-chips" role="group" aria-label="Log type">
    <button class="al-chip is-on" type="button" data-l="all">All</button>
    <button class="al-chip" type="button" data-l="auth">Auth</button>
    <button class="al-chip" type="button" data-l="billing">Billing</button>
    <button class="al-chip" type="button" data-l="system">System</button>
  </div>
  <ul class="al-list" id="alList">
    <li class="al-item" data-l="auth"><span class="al-ic is-auth" aria-hidden="true">A</span><div class="al-m"><p class="al-x">Ayesha signed in from Chrome</p><p class="al-d">IP 103.44.2.18 &#183; 2 minutes ago</p></div></li>
    <li class="al-item" data-l="billing"><span class="al-ic is-bill" aria-hidden="true">$</span><div class="al-m"><p class="al-x">Invoice #2841 paid</p><p class="al-d">$48.00 &#183; 26 minutes ago</p></div></li>
    <li class="al-item" data-l="system"><span class="al-ic is-sys" aria-hidden="true">S</span><div class="al-m"><p class="al-x">Nightly backup completed</p><p class="al-d">142 MB synced &#183; 3 hours ago</p></div></li>
    <li class="al-item" data-l="auth"><span class="al-ic is-auth" aria-hidden="true">A</span><div class="al-m"><p class="al-x">New device approved</p><p class="al-d">macOS &#183; Yesterday</p></div></li>
    <li class="al-item" data-l="billing"><span class="al-ic is-bill" aria-hidden="true">$</span><div class="al-m"><p class="al-x">Plan upgraded to Pro</p><p class="al-d">Monthly billing &#183; 2 days ago</p></div></li>
  </ul>
  <p class="al-msg" id="alMsg" aria-live="polite"></p>
</div>''',
   "css": '''.al-card { max-width: 400px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 12px; }
.al-head { display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-bottom: 7px; }
.al-t { font-size: 0.8rem; font-weight: 700; }
.al-clear { border: 0; background: transparent; color: var(--muted); font: inherit; font-size: 0.62rem; font-weight: 600; cursor: pointer; padding: 2px 4px; border-radius: 3px; }
.al-clear:hover { color: var(--no); }
.al-clear:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.al-chips { display: flex; gap: 4px; flex-wrap: wrap; margin-bottom: 7px; }
.al-chip { border: 1px solid var(--border); background: transparent; color: var(--muted); font: inherit; font-size: 0.62rem; font-weight: 600; padding: 2px 7px; border-radius: 999px; cursor: pointer; }
.al-chip.is-on { background: var(--accent-soft); border-color: var(--accent); color: var(--accent); }
.al-chip:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.al-list { list-style: none; margin: 0; padding: 0; }
.al-item { display: flex; gap: 8px; padding: 7px 0; border-bottom: 1px solid var(--border); }
.al-item:last-child { border-bottom: 0; }
.al-ic { width: 22px; height: 22px; border-radius: 999px; display: flex; align-items: center; justify-content: center; font-size: 0.58rem; font-weight: 800; flex: 0 0 auto; }
.al-ic.is-auth { background: var(--accent-soft); color: var(--accent); }
.al-ic.is-bill { background: rgba(34, 160, 107, 0.12); color: var(--yes); }
.al-ic.is-sys { background: rgba(194, 116, 10, 0.12); color: var(--warn); }
.al-m { min-width: 0; }
.al-x { margin: 0; font-size: 0.7rem; font-weight: 600; }
.al-d { margin: 1px 0 0; font-size: 0.6rem; color: var(--muted); }
.al-msg { min-height: 1em; margin: 6px 0 0; font-size: 0.62rem; color: var(--muted); }''',
   "js": '''(function () {
  var items = Array.prototype.slice.call(document.querySelectorAll(".al-item"));
  var chips = Array.prototype.slice.call(document.querySelectorAll(".al-chip"));
  var msg = document.getElementById("alMsg");

  chips.forEach(function (c) {
    c.addEventListener("click", function () {
      chips.forEach(function (x) { x.classList.remove("is-on"); });
      c.classList.add("is-on");
      var f = c.getAttribute("data-l");
      var n = 0;
      items.forEach(function (it) {
        var show = f === "all" || it.getAttribute("data-l") === f;
        it.hidden = !show;
        if (show) n += 1;
      });
      msg.textContent = n + " entr" + (n === 1 ? "y" : "ies") + " shown.";
    });
  });

  document.getElementById("alClear").addEventListener("click", function () {
    items.forEach(function (it) { it.hidden = false; });
    chips.forEach(function (x) { x.classList.remove("is-on"); });
    chips[0].classList.add("is-on");
    msg.textContent = "View cleared.";
  });
})();''',
  }],
 },
 {
  "folder": "dashboard", "slug": "file-manager", "title": "File Manager",
  "desc": "Folder rail, breadcrumb, file tiles and storage bar.",
  "idx_desc": "Folder rail, file tiles and storage usage.",
  "mini": '<div class="p-gal"><span></span><span></span></div>',
  "blocks": [{
   "id": "file-manager", "title": "Files",
   "html": '''<div class="fl-frame">
  <aside class="fl-side">
    <p class="fl-sideT">Folders</p>
    <button class="fl-folder is-on" type="button"><span class="fl-fi" aria-hidden="true"></span>Design</button>
    <button class="fl-folder" type="button"><span class="fl-fi" aria-hidden="true"></span>Documents</button>
    <button class="fl-folder" type="button"><span class="fl-fi" aria-hidden="true"></span>Media</button>
    <button class="fl-folder" type="button"><span class="fl-fi" aria-hidden="true"></span>Archive</button>
    <div class="fl-store"><span class="fl-storeT">Storage</span><span class="fl-track"><span class="fl-fill"></span></span><span class="fl-storeD">6.4 of 10 GB</span></div>
  </aside>
  <div class="fl-main">
    <div class="fl-top">
      <span class="fl-crumb">Files <span class="fl-sep">/</span> <strong>Design</strong></span>
      <button class="fl-upload" type="button" id="flUpload">Upload</button>
    </div>
    <div class="fl-grid">
      <button class="fl-tile" type="button"><span class="fl-ft is-fig">FIG</span><span class="fl-n">Brand kit</span><span class="fl-s">12.4 MB</span></button>
      <button class="fl-tile" type="button"><span class="fl-ft is-img">PNG</span><span class="fl-n">Hero shots</span><span class="fl-s">8.1 MB</span></button>
      <button class="fl-tile" type="button"><span class="fl-ft is-pdf">PDF</span><span class="fl-n">Guidelines</span><span class="fl-s">2.3 MB</span></button>
      <button class="fl-tile" type="button"><span class="fl-ft is-zip">ZIP</span><span class="fl-n">Assets</span><span class="fl-s">44.0 MB</span></button>
    </div>
    <p class="fl-msg" id="flMsg" aria-live="polite"></p>
  </div>
</div>''',
   "css": '''.fl-frame { display: grid; grid-template-columns: 120px 1fr; height: 290px; border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; background: var(--card); }
.fl-side { background: var(--bg); border-right: 1px solid var(--border); padding: 9px 7px; display: flex; flex-direction: column; gap: 2px; }
.fl-sideT { margin: 0 0 4px; padding: 0 4px; font-size: 0.56rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; color: var(--muted); }
.fl-folder { display: flex; align-items: center; gap: 5px; border: 0; background: transparent; color: var(--muted); font: inherit; font-size: 0.66rem; font-weight: 600; text-align: left; padding: 5px 6px; border-radius: 4px; cursor: pointer; }
.fl-folder:hover { color: var(--text); }
.fl-folder.is-on { background: var(--accent-soft); color: var(--accent); }
.fl-folder:focus-visible { outline: 2px solid var(--accent); outline-offset: -2px; }
.fl-fi { width: 9px; height: 7px; border-radius: 1px; background: currentColor; opacity: 0.7; flex: 0 0 auto; }
.fl-store { margin-top: auto; padding: 6px 4px 2px; }
.fl-storeT { display: block; font-size: 0.56rem; font-weight: 700; color: var(--muted); margin-bottom: 3px; }
.fl-track { display: block; height: 4px; border-radius: 999px; background: var(--border); overflow: hidden; margin-bottom: 3px; }
.fl-fill { display: block; width: 64%; height: 100%; background: var(--accent); border-radius: 999px; }
.fl-storeD { font-size: 0.54rem; color: var(--muted); }
.fl-main { padding: 9px; overflow: auto; min-width: 0; }
.fl-top { display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-bottom: 8px; }
.fl-crumb { font-size: 0.64rem; color: var(--muted); }
.fl-sep { margin: 0 3px; }
.fl-crumb strong { color: var(--text); }
.fl-upload { border: 0; background: var(--accent); color: #fff; font: inherit; font-size: 0.6rem; font-weight: 700; padding: 4px 8px; border-radius: 3px; cursor: pointer; }
.fl-upload:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.fl-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(74px, 1fr)); gap: 6px; }
.fl-tile { display: flex; flex-direction: column; align-items: flex-start; gap: 2px; border: 1px solid var(--border); background: var(--bg); border-radius: 4px; padding: 7px; cursor: pointer; text-align: left; font: inherit; }
.fl-tile:hover { border-color: var(--accent); }
.fl-tile:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.fl-ft { width: 28px; height: 22px; border-radius: 3px; display: flex; align-items: center; justify-content: center; font-size: 0.46rem; font-weight: 800; margin-bottom: 2px; }
.fl-ft.is-fig { background: rgba(139, 92, 246, 0.16); color: #8b5cf6; }
.fl-ft.is-img { background: rgba(14, 165, 233, 0.14); color: #0ea5e9; }
.fl-ft.is-pdf { background: rgba(229, 72, 77, 0.12); color: var(--no); }
.fl-ft.is-zip { background: rgba(194, 116, 10, 0.14); color: var(--warn); }
.fl-n { font-size: 0.64rem; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 100%; }
.fl-s { font-size: 0.56rem; color: var(--muted); }
.fl-msg { min-height: 1em; margin: 6px 0 0; font-size: 0.6rem; color: var(--muted); }
@media (max-width: 480px) { .fl-frame { grid-template-columns: 44px 1fr; } .fl-folder { font-size: 0; justify-content: center; } .fl-sideT, .fl-store { display: none; } }''',
   "js": '''(function () {
  var folders = Array.prototype.slice.call(document.querySelectorAll(".fl-folder"));
  var msg = document.getElementById("flMsg");
  var crumb = document.querySelector(".fl-crumb strong");
  folders.forEach(function (f) {
    f.addEventListener("click", function () {
      folders.forEach(function (x) { x.classList.remove("is-on"); });
      f.classList.add("is-on");
      var name = f.textContent.trim();
      crumb.textContent = name;
      msg.textContent = "Opened " + name + " (demo).";
    });
  });
  document.getElementById("flUpload").addEventListener("click", function () {
    msg.textContent = "Upload dialog would open here.";
  });
  document.querySelectorAll(".fl-tile").forEach(function (t) {
    t.addEventListener("click", function () {
      msg.textContent = t.querySelector(".fl-n").textContent + " selected.";
    });
  });
})();''',
  }],
 },
 {
  "folder": "dashboard", "slug": "chat", "title": "Chat Interface",
  "desc": "Conversation list, message bubbles and composer.",
  "idx_desc": "Chat list, message bubbles and composer.",
  "mini": '<div class="p-bubble"></div><div class="p-bubble is-me"></div>',
  "blocks": [
   {"id": "chat-shell", "title": "Chat layout", "html": '''<div class="ct-frame">
  <aside class="ct-side">
    <div class="ct-sideTop"><span class="ct-sideT">Messages</span><button class="ct-new" type="button" id="ctNew" aria-label="New message">+</button></div>
    <div class="ct-item is-on"><span class="ct-av c1">RS</span><div class="ct-im"><p class="ct-n">Rohan Shah</p><p class="ct-p">Sent the updated files</p></div><span class="ct-un">2</span></div>
    <div class="ct-item"><span class="ct-av c2">MP</span><div class="ct-im"><p class="ct-n">Mira Patel</p><p class="ct-p">Looks good to me</p></div></div>
    <div class="ct-item"><span class="ct-av c3">TN</span><div class="ct-im"><p class="ct-n">Tarun Nair</p><p class="ct-p">See you tomorrow</p></div></div>
  </aside>
  <div class="ct-pane">
    <div class="ct-head"><span class="ct-av c1">RS</span><div><p class="ct-hn">Rohan Shah</p><p class="ct-hs">Online</p></div></div>
    <div class="ct-thread">
      <div class="ct-bub is-them"><p class="ct-bt">Hey! The new dashboard is live on staging.</p><span class="ct-bs">10:12</span></div>
      <div class="ct-bub is-me"><p class="ct-bt">Nice. I will review it after standup.</p><span class="ct-bs">10:14</span></div>
      <div class="ct-bub is-them"><p class="ct-bt">Great — the mobile view needs a check too.</p><span class="ct-bs">10:15</span></div>
    </div>
    <div class="ct-compose">
      <input class="ct-input" type="text" placeholder="Write a message..." aria-label="Message">
      <button class="ct-send" type="button" id="ctSend" aria-label="Send message">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 2L11 13M22 2l-7 20-4-9-9-4z"/></svg>
      </button>
    </div>
  </div>
</div>''', "css": '''.ct-frame { display: grid; grid-template-columns: 170px 1fr; height: 300px; border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; background: var(--card); }
.ct-side { background: var(--bg); border-right: 1px solid var(--border); overflow: auto; }
.ct-sideTop { display: flex; align-items: center; justify-content: space-between; padding: 8px 9px 6px; }
.ct-sideT { font-size: 0.66rem; font-weight: 700; }
.ct-new { width: 18px; height: 18px; border: 1px solid var(--border); border-radius: 3px; background: var(--card); color: var(--muted); font-size: 0.8rem; line-height: 1; cursor: pointer; }
.ct-new:hover { border-color: var(--accent); color: var(--accent); }
.ct-new:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.ct-item { display: flex; align-items: center; gap: 6px; padding: 6px 9px; cursor: pointer; }
.ct-item.is-on { background: var(--accent-soft); }
.ct-item:hover { background: var(--bg); }
.ct-item.is-on:hover { background: var(--accent-soft); }
.ct-av { width: 24px; height: 24px; border-radius: 999px; color: #fff; font-size: 0.52rem; font-weight: 700; display: flex; align-items: center; justify-content: center; flex: 0 0 auto; }
.ct-av.c1 { background: linear-gradient(135deg, #4f6bed, #8b5cf6); }
.ct-av.c2 { background: linear-gradient(135deg, #22a06b, #0ea5e9); }
.ct-av.c3 { background: linear-gradient(135deg, #e5484d, #f0b543); }
.ct-im { flex: 1; min-width: 0; }
.ct-n { margin: 0; font-size: 0.64rem; font-weight: 700; }
.ct-p { margin: 0; font-size: 0.55rem; color: var(--muted); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.ct-un { min-width: 14px; height: 14px; padding: 0 3px; border-radius: 999px; background: var(--accent); color: #fff; font-size: 0.5rem; font-weight: 700; display: flex; align-items: center; justify-content: center; }
.ct-pane { display: flex; flex-direction: column; min-width: 0; }
.ct-head { display: flex; align-items: center; gap: 6px; padding: 7px 9px; border-bottom: 1px solid var(--border); }
.ct-hn { margin: 0; font-size: 0.68rem; font-weight: 700; }
.ct-hs { margin: 0; font-size: 0.55rem; color: var(--yes); }
.ct-thread { flex: 1; padding: 8px; overflow: auto; display: flex; flex-direction: column; gap: 6px; background: var(--bg); }
.ct-bub { max-width: 82%; border-radius: 8px; padding: 6px 8px; }
.ct-bub.is-them { align-self: flex-start; background: var(--card); border: 1px solid var(--border); }
.ct-bub.is-me { align-self: flex-end; background: var(--accent); color: #fff; }
.ct-bt { margin: 0; font-size: 0.66rem; line-height: 1.45; }
.ct-bs { display: block; margin-top: 2px; font-size: 0.5rem; opacity: 0.6; text-align: right; }
.ct-compose { display: flex; align-items: center; gap: 6px; padding: 6px 8px; border-top: 1px solid var(--border); }
.ct-input { flex: 1; min-width: 0; border: 1px solid var(--border); border-radius: 999px; background: var(--bg); color: var(--text); font: inherit; font-size: 0.66rem; padding: 5px 9px; outline: none; }
.ct-input:focus { border-color: var(--accent); }
.ct-send { width: 26px; height: 26px; border: 0; border-radius: 999px; background: var(--accent); color: #fff; display: flex; align-items: center; justify-content: center; cursor: pointer; flex: 0 0 auto; }
.ct-send svg { width: 13px; height: 13px; }
.ct-send:hover { opacity: 0.92; }
.ct-send:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
@media (max-width: 480px) { .ct-frame { grid-template-columns: 1fr; } .ct-side { display: none; } }'''},
   {"id": "chat-bubbles", "title": "Message bubbles", "html": '''<div class="cb-list">
  <div class="cb-row"><span class="cb-av" aria-hidden="true">RS</span><div class="cb-bub is-them"><p class="cb-t">The staging build is ready for review.</p><span class="cb-time">Rohan &#183; 10:12</span></div></div>
  <div class="cb-row is-me"><div class="cb-bub is-me"><p class="cb-t">Looks great. I will add notes in Figma.</p><span class="cb-time">You &#183; 10:14</span></div></div>
  <div class="cb-row"><span class="cb-av" aria-hidden="true">MP</span><div class="cb-bub is-them"><p class="cb-t">Can we ship the mobile fix today?</p><span class="cb-time">Mira &#183; 10:18</span></div></div>
  <div class="cb-typing" aria-label="Ayesha is typing"><span class="cb-tdot"></span><span class="cb-tdot"></span><span class="cb-tdot"></span></div>
</div>''', "css": '''.cb-list { max-width: 380px; display: flex; flex-direction: column; gap: 7px; }
.cb-row { display: flex; align-items: flex-end; gap: 6px; }
.cb-row.is-me { justify-content: flex-end; }
.cb-av { width: 22px; height: 22px; border-radius: 999px; background: linear-gradient(135deg, #22a06b, #0ea5e9); color: #fff; font-size: 0.5rem; font-weight: 700; display: flex; align-items: center; justify-content: center; flex: 0 0 auto; }
.cb-bub { max-width: 78%; border-radius: 9px; padding: 7px 9px; background: var(--card); border: 1px solid var(--border); }
.cb-bub.is-me { background: var(--accent); border-color: var(--accent); color: #fff; }
.cb-t { margin: 0; font-size: 0.72rem; line-height: 1.45; }
.cb-time { display: block; margin-top: 2px; font-size: 0.54rem; opacity: 0.62; }
.cb-typing { display: inline-flex; align-items: center; gap: 3px; width: 40px; padding: 8px 9px; background: var(--card); border: 1px solid var(--border); border-radius: 9px; margin-left: 28px; }
.cb-tdot { width: 4px; height: 4px; border-radius: 999px; background: var(--muted); animation: cbBounce 1.2s infinite; }
.cb-tdot:nth-child(2) { animation-delay: 0.15s; }
.cb-tdot:nth-child(3) { animation-delay: 0.3s; }
@keyframes cbBounce { 0%, 60%, 100% { transform: translateY(0); opacity: 0.5; } 30% { transform: translateY(-3px); opacity: 1; } }
@media (prefers-reduced-motion: reduce) { .cb-tdot { animation: none; } }'''},
   {"id": "chat-composer", "title": "Composer", "html": '''<div class="cc-box">
  <textarea class="cc-input" id="ccInput" rows="2" placeholder="Write a message..." aria-label="Message"></textarea>
  <div class="cc-foot">
    <div class="cc-tools">
      <button class="cc-tool" type="button" aria-label="Attach file">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.5l-8.5 8.5a6 6 0 0 1-8.5-8.5L12.5 4a4 4 0 0 1 5.7 5.7l-8.5 8.5a2 2 0 0 1-2.8-2.8l8-8"/></svg>
      </button>
      <button class="cc-tool" type="button" aria-label="Add emoji">&#9786;</button>
      <span class="cc-count" id="ccCount">0 / 500</span>
    </div>
    <button class="cc-send" type="button" id="ccSend">Send</button>
  </div>
  <p class="cc-msg" id="ccMsg" aria-live="polite"></p>
</div>''', "css": '''.cc-box { max-width: 380px; border: 1px solid var(--border); border-radius: 8px; background: var(--card); padding: 8px; }
.cc-input { width: 100%; border: 0; background: transparent; color: var(--text); font: inherit; font-size: 0.76rem; line-height: 1.5; outline: none; resize: none; padding: 4px; }
.cc-foot { display: flex; align-items: center; justify-content: space-between; gap: 8px; padding-top: 5px; border-top: 1px solid var(--border); }
.cc-tools { display: flex; align-items: center; gap: 3px; }
.cc-tool { border: 0; background: transparent; color: var(--muted); font-size: 0.9rem; padding: 3px 5px; border-radius: 3px; cursor: pointer; display: flex; }
.cc-tool svg { width: 14px; height: 14px; }
.cc-tool:hover { color: var(--accent); }
.cc-tool:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.cc-count { font-size: 0.56rem; color: var(--muted); margin-left: 3px; }
.cc-send { border: 0; background: var(--accent); color: #fff; font: inherit; font-size: 0.66rem; font-weight: 700; padding: 5px 12px; border-radius: 999px; cursor: pointer; }
.cc-send:hover { opacity: 0.92; }
.cc-send:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.cc-msg { min-height: 1em; margin: 5px 2px 0; font-size: 0.6rem; color: var(--yes); }''', "js": '''(function () {
  var input = document.getElementById("ccInput");
  var count = document.getElementById("ccCount");
  var msg = document.getElementById("ccMsg");

  input.addEventListener("input", function () {
    if (input.value.length > 500) input.value = input.value.slice(0, 500);
    count.textContent = input.value.length + " / 500";
  });

  document.getElementById("ccSend").addEventListener("click", function () {
    if (!input.value.trim()) { msg.textContent = "Type a message first."; return; }
    msg.textContent = "Message sent (demo).";
    input.value = "";
    count.textContent = "0 / 500";
    input.focus();
  });
})();'''},
  ],
 },
 {
  "folder": "dashboard", "slug": "profile-page", "title": "Profile Page",
  "desc": "Cover, avatar, stats and tabbed profile content.",
  "idx_desc": "Cover, avatar, stats and tabbed profile content.",
  "mini": '<div class="p-av" style="width: 26px; height: 26px;"></div><div class="p-line" style="width: 30px;"></div>',
  "blocks": [{
   "id": "profile-page", "title": "Member profile",
   "html": '''<div class="pp-card">
  <div class="pp-cover"><span class="pp-coverArt" aria-hidden="true"></span></div>
  <div class="pp-body">
    <div class="pp-id">
      <span class="pp-av" aria-hidden="true">AK</span>
      <div class="pp-idm"><p class="pp-n">Ayesha Khan</p><p class="pp-r">Product designer &#183; Mumbai</p></div>
    </div>
    <div class="pp-stats">
      <div class="pp-st"><span class="pp-sv">24</span><span class="pp-sl">Projects</span></div>
      <div class="pp-st"><span class="pp-sv">1.8k</span><span class="pp-sl">Followers</span></div>
      <div class="pp-st"><span class="pp-sv">312</span><span class="pp-sl">Following</span></div>
    </div>
    <div class="pp-tabs" role="tablist" aria-label="Profile sections">
      <button class="pp-tab is-on" type="button" role="tab" aria-selected="true" data-p="about">About</button>
      <button class="pp-tab" type="button" role="tab" aria-selected="false" data-p="activity">Activity</button>
    </div>
    <div class="pp-panel" id="ppAbout">
      <p class="pp-text">Designing calm interfaces and reusable systems. Currently focused on accessible dashboards and design tokens.</p>
      <div class="pp-skills"><span class="pp-skill">UI design</span><span class="pp-skill">Design systems</span><span class="pp-skill">Accessibility</span></div>
    </div>
    <div class="pp-panel" id="ppActivity" hidden>
      <div class="pp-act"><span class="pp-dot" aria-hidden="true"></span>Updated the component library &#183; 2h ago</div>
      <div class="pp-act"><span class="pp-dot" aria-hidden="true"></span>Commented on Checkout flow &#183; yesterday</div>
      <div class="pp-act"><span class="pp-dot" aria-hidden="true"></span>Published the dashboard spec &#183; 3 days ago</div>
    </div>
  </div>
</div>''',
   "css": '''.pp-card { max-width: 380px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); overflow: hidden; }
.pp-cover { height: 76px; background: linear-gradient(120deg, #2a2350, #4f6bed 55%, #8b5cf6); }
.pp-coverArt { display: block; height: 100%; background: radial-gradient(circle at 78% 30%, rgba(255, 255, 255, 0.28), transparent 40%); }
.pp-body { padding: 0 13px 13px; }
.pp-id { display: flex; align-items: flex-end; gap: 8px; margin-top: -22px; margin-bottom: 8px; }
.pp-av { width: 46px; height: 46px; border-radius: 999px; background: linear-gradient(135deg, #4f6bed, #8b5cf6); border: 3px solid var(--card); color: #fff; font-size: 0.8rem; font-weight: 700; display: flex; align-items: center; justify-content: center; flex: 0 0 auto; }
.pp-idm { padding-bottom: 1px; }
.pp-n { margin: 0; font-size: 0.88rem; font-weight: 800; }
.pp-r { margin: 0; font-size: 0.62rem; color: var(--muted); }
.pp-stats { display: flex; gap: 14px; padding: 6px 0 8px; border-bottom: 1px solid var(--border); }
.pp-st { display: flex; flex-direction: column; }
.pp-sv { font-size: 0.8rem; font-weight: 800; }
.pp-sl { font-size: 0.56rem; color: var(--muted); }
.pp-tabs { display: flex; gap: 3px; margin: 8px 0; }
.pp-tab { border: 1px solid var(--border); background: transparent; color: var(--muted); font: inherit; font-size: 0.62rem; font-weight: 600; padding: 3px 9px; border-radius: 999px; cursor: pointer; }
.pp-tab.is-on { background: var(--accent-soft); border-color: var(--accent); color: var(--accent); }
.pp-tab:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.pp-text { margin: 0 0 7px; font-size: 0.7rem; line-height: 1.5; color: var(--text); }
.pp-skills { display: flex; gap: 4px; flex-wrap: wrap; }
.pp-skill { font-size: 0.56rem; font-weight: 600; color: var(--muted); background: var(--bg); border-radius: 999px; padding: 2px 7px; }
.pp-act { display: flex; align-items: center; gap: 5px; font-size: 0.66rem; color: var(--muted); padding: 4px 0; }
.pp-dot { width: 5px; height: 5px; border-radius: 999px; background: var(--accent); flex: 0 0 auto; }''',
   "js": '''(function () {
  var tabs = Array.prototype.slice.call(document.querySelectorAll(".pp-tab"));
  var about = document.getElementById("ppAbout");
  var activity = document.getElementById("ppActivity");
  tabs.forEach(function (t) {
    t.addEventListener("click", function () {
      tabs.forEach(function (x) {
        x.classList.remove("is-on");
        x.setAttribute("aria-selected", "false");
      });
      t.classList.add("is-on");
      t.setAttribute("aria-selected", "true");
      var isAbout = t.getAttribute("data-p") === "about";
      about.hidden = !isAbout;
      activity.hidden = isAbout;
    });
  });
})();''',
  }],
 },
]
