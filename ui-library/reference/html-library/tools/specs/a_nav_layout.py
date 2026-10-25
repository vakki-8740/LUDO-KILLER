CAT = "Navigation & Layout"
CAT_ID = "navigation"

PAGES = [
    {
        "folder": "navigation",
        "slug": "mega-menu",
        "title": "Mega Menu",
        "desc": "Wide dropdown with grouped links and a featured panel.",
        "idx_desc": "Wide dropdown with link columns and a featured card.",
        "mini": '<div class="p-drop"><span></span><span></span><span></span></div>',
        "blocks": [
            {
                "id": "mega-menu",
                "title": "Mega menu",
                "note": "Trigger par click, bahar click ya Escape se band.",
                "html": '''<div class="mm-bar">
  <span class="mm-logo"></span>
  <nav class="mm-nav" aria-label="Main">
    <div class="mm-item">
      <button class="mm-trigger" type="button" id="mmTrigger" aria-expanded="false" aria-controls="mmPanel">Products
        <svg class="mm-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
      </button>
      <div class="mm-panel" id="mmPanel" role="region" aria-label="Products" hidden>
        <div class="mm-grid">
          <div class="mm-col">
            <p class="mm-ct">Design</p>
            <a class="mm-link" href="#">UI Kit</a>
            <a class="mm-link" href="#">Icons</a>
            <a class="mm-link" href="#">Templates</a>
          </div>
          <div class="mm-col">
            <p class="mm-ct">Build</p>
            <a class="mm-link" href="#">Components</a>
            <a class="mm-link" href="#">Charts</a>
            <a class="mm-link" href="#">Forms</a>
          </div>
          <div class="mm-col">
            <p class="mm-ct">Ship</p>
            <a class="mm-link" href="#">Templates</a>
            <a class="mm-link" href="#">Changelog</a>
            <a class="mm-link" href="#">Docs</a>
          </div>
          <div class="mm-feat">
            <span class="mm-feat-tile"></span>
            <p class="mm-feat-k">New</p>
            <p class="mm-feat-h">Library v2 is live</p>
            <p class="mm-feat-d">120+ ready blocks with copyable code.</p>
            <span class="mm-feat-btn">Explore</span>
          </div>
        </div>
      </div>
    </div>
    <a class="mm-link mm-top" href="#">Pricing</a>
    <a class="mm-link mm-top" href="#">Docs</a>
  </nav>
</div>''',
                "css": '''.mm-bar {
  display: flex;
  align-items: center;
  gap: 18px;
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 10px 14px;
  box-shadow: var(--shadow);
}
.mm-logo { width: 26px; height: 26px; border-radius: 6px; background: var(--accent); flex: 0 0 auto; }
.mm-nav { display: flex; align-items: center; gap: 6px; flex: 1; }
.mm-item { position: relative; }
.mm-trigger {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  border: 0;
  background: transparent;
  color: var(--text);
  font: inherit;
  font-size: 0.88rem;
  font-weight: 600;
  padding: 8px 12px;
  border-radius: var(--radius);
  cursor: pointer;
}
.mm-trigger:hover, .mm-trigger[aria-expanded="true"] { background: var(--accent-soft); color: var(--accent); }
.mm-trigger:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.mm-chev { width: 14px; height: 14px; transition: transform 0.2s; }
.mm-trigger[aria-expanded="true"] .mm-chev { transform: rotate(180deg); }
.mm-top { text-decoration: none; }
.mm-panel {
  position: absolute;
  top: calc(100% + 10px);
  left: -40px;
  width: min(620px, 86vw);
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: 16px;
  z-index: 30;
}
.mm-grid { display: grid; grid-template-columns: 1fr 1fr 1fr 1.2fr; gap: 14px; }
.mm-ct { margin: 0 0 8px; font-size: 0.7rem; font-weight: 700; letter-spacing: 0.07em; text-transform: uppercase; color: var(--muted); }
.mm-link {
  display: block;
  color: var(--text);
  text-decoration: none;
  font-size: 0.85rem;
  padding: 6px 8px;
  border-radius: var(--radius);
}
.mm-link:hover { background: var(--bg); color: var(--accent); }
.mm-feat { background: var(--bg); border: 1px solid var(--border); border-radius: var(--radius); padding: 12px; }
.mm-feat-tile { display: block; height: 54px; border-radius: 5px; background: linear-gradient(135deg, var(--accent), #8b5cf6); margin-bottom: 8px; }
.mm-feat-k { margin: 0; font-size: 0.66rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: var(--accent); }
.mm-feat-h { margin: 2px 0; font-size: 0.86rem; font-weight: 700; }
.mm-feat-d { margin: 0 0 8px; font-size: 0.74rem; color: var(--muted); line-height: 1.4; }
.mm-feat-btn { display: inline-block; font-size: 0.74rem; font-weight: 700; color: var(--accent); }
@media (max-width: 640px) {
  .mm-panel { left: -60px; width: min(320px, 88vw); }
  .mm-grid { grid-template-columns: 1fr 1fr; }
  .mm-feat { grid-column: span 2; }
}''',
                "js": '''var trigger = document.getElementById("mmTrigger");
var panel = document.getElementById("mmPanel");

function mmSet(open) {
  panel.hidden = !open;
  trigger.setAttribute("aria-expanded", String(open));
}

trigger.addEventListener("click", function (e) {
  e.stopPropagation();
  mmSet(panel.hidden);
});

document.addEventListener("click", function (e) {
  if (!panel.hidden && !panel.contains(e.target) && e.target !== trigger) mmSet(false);
});

document.addEventListener("keydown", function (e) {
  if (e.key === "Escape" && !panel.hidden) {
    mmSet(false);
    trigger.focus();
  }
});''',
            }
        ],
    },
    {
        "folder": "navigation",
        "slug": "tabs",
        "title": "Tabs Navigation",
        "desc": "ARIA tabs with underline and pill variants.",
        "idx_desc": "Underline and pill tabs with keyboard support.",
        "mini": '<div class="p-row" style="gap: 6px;"><span class="p-btn accent" style="width: 34px;"></span><span class="p-btn" style="width: 34px;"></span><span class="p-btn" style="width: 34px;"></span></div>',
        "blocks": [
            {
                "id": "tabs-underline",
                "title": "Underline tabs",
                "note": "Arrow keys se tab badlein.",
                "html": '''<div class="tu-wrap">
  <div class="tu-bar" role="tablist" aria-label="Account sections">
    <button class="tu-tab is-on" type="button" role="tab" id="tuT1" aria-selected="true" aria-controls="tuP1" tabindex="0">Profile</button>
    <button class="tu-tab" type="button" role="tab" id="tuT2" aria-selected="false" aria-controls="tuP2" tabindex="-1">Security</button>
    <button class="tu-tab" type="button" role="tab" id="tuT3" aria-selected="false" aria-controls="tuP3" tabindex="-1">Billing</button>
    <button class="tu-tab" type="button" role="tab" id="tuT4" aria-selected="false" aria-controls="tuP4" tabindex="-1">Team</button>
  </div>
  <div class="tu-panel" role="tabpanel" id="tuP1" aria-labelledby="tuT1" tabindex="0">
    <p class="tu-h">Public profile</p>
    <p class="tu-d">Name, avatar aur bio jo sabko dikhti hai.</p>
    <div class="tu-rows"><span></span><span></span></div>
  </div>
  <div class="tu-panel" role="tabpanel" id="tuP2" aria-labelledby="tuT2" tabindex="0" hidden>
    <p class="tu-h">Security</p>
    <p class="tu-d">Password badlein aur 2FA enable karein.</p>
    <div class="tu-rows"><span></span><span></span></div>
  </div>
  <div class="tu-panel" role="tabpanel" id="tuP3" aria-labelledby="tuT3" tabindex="0" hidden>
    <p class="tu-h">Billing</p>
    <p class="tu-d">Plan, invoices aur payment methods.</p>
    <div class="tu-rows"><span></span><span></span></div>
  </div>
  <div class="tu-panel" role="tabpanel" id="tuP4" aria-labelledby="tuT4" tabindex="0" hidden>
    <p class="tu-h">Team</p>
    <p class="tu-d">Members invite karein aur roles manage karein.</p>
    <div class="tu-rows"><span></span><span></span></div>
  </div>
</div>''',
                "css": '''.tu-bar {
  display: flex;
  gap: 4px;
  border-bottom: 1px solid var(--border);
  overflow-x: auto;
  scrollbar-width: none;
}
.tu-tab {
  border: 0;
  background: transparent;
  color: var(--muted);
  font: inherit;
  font-size: 0.88rem;
  font-weight: 600;
  padding: 10px 14px;
  cursor: pointer;
  border-bottom: 2px solid transparent;
  white-space: nowrap;
}
.tu-tab:hover { color: var(--text); }
.tu-tab.is-on { color: var(--accent); border-bottom-color: var(--accent); }
.tu-tab:focus-visible { outline: 2px solid var(--accent); outline-offset: -2px; }
.tu-panel { padding: 16px 4px 4px; }
.tu-h { margin: 0 0 4px; font-size: 0.95rem; font-weight: 700; }
.tu-d { margin: 0 0 12px; font-size: 0.84rem; color: var(--muted); }
.tu-rows { display: flex; flex-direction: column; gap: 8px; }
.tu-rows span { height: 10px; border-radius: 4px; background: var(--border); }
.tu-rows span:nth-child(2) { width: 70%; }''',
                "js": '''document.querySelectorAll(".tu-wrap").forEach(function (wrap) {
  var tabs = Array.prototype.slice.call(wrap.querySelectorAll('[role="tab"]'));
  var panels = Array.prototype.slice.call(wrap.querySelectorAll('[role="tabpanel"]'));

  function activate(i) {
    tabs.forEach(function (t, j) {
      var on = i === j;
      t.classList.toggle("is-on", on);
      t.setAttribute("aria-selected", String(on));
      t.tabIndex = on ? 0 : -1;
      panels[j].hidden = !on;
    });
    tabs[i].focus();
  }

  tabs.forEach(function (tab, i) {
    tab.addEventListener("click", function () { activate(i); });
    tab.addEventListener("keydown", function (e) {
      var n = null;
      if (e.key === "ArrowRight") n = (i + 1) % tabs.length;
      else if (e.key === "ArrowLeft") n = (i - 1 + tabs.length) % tabs.length;
      else if (e.key === "Home") n = 0;
      else if (e.key === "End") n = tabs.length - 1;
      if (n !== null) { e.preventDefault(); activate(n); }
    });
  });
});''',
            },
            {
                "id": "tabs-pills",
                "title": "Pill tabs",
                "html": '''<div class="tp-wrap">
  <div class="tp-bar" role="tablist" aria-label="Project views">
    <button class="tp-tab is-on" type="button" role="tab" id="tpT1" aria-selected="true" aria-controls="tpP1" tabindex="0">Overview</button>
    <button class="tp-tab" type="button" role="tab" id="tpT2" aria-selected="false" aria-controls="tpP2" tabindex="-1">Activity</button>
    <button class="tp-tab" type="button" role="tab" id="tpT3" aria-selected="false" aria-controls="tpP3" tabindex="-1">Documents</button>
  </div>
  <div class="tp-panel" role="tabpanel" id="tpP1" aria-labelledby="tpT1" tabindex="0">
    <p class="tp-d">Project stats, milestones aur quick links ek jagah.</p>
    <div class="tp-stats"><span><strong>24</strong>Tasks</span><span><strong>8</strong>Members</span><span><strong>92%</strong>Done</span></div>
  </div>
  <div class="tp-panel" role="tabpanel" id="tpP2" aria-labelledby="tpT2" tabindex="0" hidden>
    <p class="tp-d">Recent updates from the team.</p>
    <div class="tp-rows"><span></span><span></span><span></span></div>
  </div>
  <div class="tp-panel" role="tabpanel" id="tpP3" aria-labelledby="tpT3" tabindex="0" hidden>
    <p class="tp-d">Shared files and specs.</p>
    <div class="tp-rows"><span></span><span></span></div>
  </div>
</div>''',
                "css": '''.tp-bar {
  display: inline-flex;
  gap: 4px;
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 999px;
  padding: 4px;
  overflow-x: auto;
  max-width: 100%;
  scrollbar-width: none;
}
.tp-tab {
  border: 0;
  background: transparent;
  color: var(--muted);
  font: inherit;
  font-size: 0.84rem;
  font-weight: 600;
  padding: 7px 14px;
  border-radius: 999px;
  cursor: pointer;
  white-space: nowrap;
}
.tp-tab:hover { color: var(--text); }
.tp-tab.is-on { background: var(--accent); color: #fff; }
.tp-tab:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.tp-panel { padding-top: 14px; }
.tp-d { margin: 0 0 12px; font-size: 0.85rem; color: var(--muted); }
.tp-stats { display: flex; gap: 10px; flex-wrap: wrap; }
.tp-stats span {
  flex: 1;
  min-width: 90px;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 10px;
  font-size: 0.72rem;
  color: var(--muted);
  text-align: center;
}
.tp-stats strong { display: block; font-size: 1rem; color: var(--text); }
.tp-rows { display: flex; flex-direction: column; gap: 8px; }
.tp-rows span { height: 10px; border-radius: 4px; background: var(--border); }
.tp-rows span:nth-child(2) { width: 80%; }
.tp-rows span:nth-child(3) { width: 60%; }''',
                "js": '''document.querySelectorAll(".tp-wrap").forEach(function (wrap) {
  var tabs = Array.prototype.slice.call(wrap.querySelectorAll('[role="tab"]'));
  var panels = Array.prototype.slice.call(wrap.querySelectorAll('[role="tabpanel"]'));

  function activate(i) {
    tabs.forEach(function (t, j) {
      var on = i === j;
      t.classList.toggle("is-on", on);
      t.setAttribute("aria-selected", String(on));
      t.tabIndex = on ? 0 : -1;
      panels[j].hidden = !on;
    });
    tabs[i].focus();
  }

  tabs.forEach(function (tab, i) {
    tab.addEventListener("click", function () { activate(i); });
    tab.addEventListener("keydown", function (e) {
      var n = null;
      if (e.key === "ArrowRight") n = (i + 1) % tabs.length;
      else if (e.key === "ArrowLeft") n = (i - 1 + tabs.length) % tabs.length;
      if (n !== null) { e.preventDefault(); activate(n); }
    });
  });
});''',
            },
        ],
    },
    {
        "folder": "navigation",
        "slug": "bottom-nav",
        "title": "Bottom Navigation Bar",
        "desc": "Mobile app style bottom bar with active states and badge.",
        "idx_desc": "App-style bottom bar with badge and center action.",
        "mini": '<div class="p-nav"><span class="p-logo"></span><span class="p-line" style="width: 20px;"></span><span class="p-line" style="width: 16px;"></span><span class="p-pill"></span></div>',
        "blocks": [
            {
                "id": "bottom-nav",
                "title": "Bottom navigation",
                "html": '''<div class="bn-app">
  <div class="bn-top">
    <p class="bn-h">Wallet</p>
    <p class="bn-bal">₹12,480.50</p>
    <div class="bn-tiles"><span></span><span></span><span></span></div>
    <div class="bn-rows"><i></i><i></i><i></i><i></i></div>
  </div>
  <nav class="bn-bar" aria-label="App">
    <button class="bn-item is-on" type="button" aria-current="page">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 10.5L12 3l9 7.5"/><path d="M5 9.5V21h14V9.5"/></svg>
      <span>Home</span>
    </button>
    <button class="bn-item" type="button">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>
      <span>Search</span>
    </button>
    <button class="bn-create" type="button" aria-label="Create new">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg>
    </button>
    <button class="bn-item" type="button">
      <span class="bn-badge">3</span>
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 8a6 6 0 1 0-12 0c0 7-3 8-3 8h18s-3-1-3-8"/><path d="M13.7 21a2 2 0 0 1-3.4 0"/></svg>
      <span>Activity</span>
    </button>
    <button class="bn-item" type="button">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-3.5 4.5-5 8-5s6.5 1.5 8 5"/></svg>
      <span>Profile</span>
    </button>
  </nav>
</div>''',
                "css": '''.bn-app {
  position: relative;
  max-width: 340px;
  margin: 0 auto;
  height: 400px;
  border: 1px solid var(--border);
  border-radius: 12px;
  overflow: hidden;
  background: var(--bg);
  display: flex;
  flex-direction: column;
}
.bn-top { flex: 1; padding: 18px 16px 64px; overflow: hidden; }
.bn-h { margin: 0; font-size: 0.78rem; color: var(--muted); }
.bn-bal { margin: 2px 0 14px; font-size: 1.4rem; font-weight: 700; letter-spacing: -0.02em; }
.bn-tiles { display: flex; gap: 8px; margin-bottom: 14px; }
.bn-tiles span { flex: 1; height: 52px; border-radius: var(--radius); background: var(--accent-soft); border: 1px solid var(--border); }
.bn-tiles span:nth-child(2) { background: var(--card); }
.bn-rows { display: flex; flex-direction: column; gap: 10px; }
.bn-rows i { display: block; height: 12px; border-radius: 4px; background: var(--card); border: 1px solid var(--border); }
.bn-rows i:nth-child(2) { width: 85%; }
.bn-rows i:nth-child(3) { width: 70%; }
.bn-rows i:nth-child(4) { width: 90%; }
.bn-bar {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  align-items: center;
  justify-content: space-around;
  background: var(--card);
  border-top: 1px solid var(--border);
  padding: 6px 4px calc(6px + env(safe-area-inset-bottom, 0px));
}
.bn-item {
  position: relative;
  border: 0;
  background: transparent;
  color: var(--muted);
  font: inherit;
  font-size: 0.62rem;
  font-weight: 600;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
  padding: 5px 8px;
  border-radius: var(--radius);
  cursor: pointer;
  flex: 1;
}
.bn-item svg { width: 21px; height: 21px; }
.bn-item:hover { color: var(--text); }
.bn-item.is-on { color: var(--accent); }
.bn-item:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.bn-badge {
  position: absolute;
  top: 0;
  right: 10px;
  min-width: 15px;
  height: 15px;
  border-radius: 999px;
  background: var(--no);
  color: #fff;
  font-size: 0.58rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 3px;
}
.bn-create {
  width: 44px;
  height: 44px;
  border-radius: 999px;
  border: 0;
  background: var(--accent);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  margin: -18px 6px 0;
  box-shadow: 0 6px 16px rgba(79, 107, 237, 0.35);
  flex: 0 0 auto;
}
.bn-create svg { width: 20px; height: 20px; }
.bn-create:hover { opacity: 0.92; }
.bn-create:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }''',
                "js": '''document.querySelectorAll(".bn-bar").forEach(function (bar) {
  var items = Array.prototype.slice.call(bar.querySelectorAll(".bn-item"));
  items.forEach(function (item) {
    item.addEventListener("click", function () {
      items.forEach(function (i) {
        i.classList.remove("is-on");
        i.removeAttribute("aria-current");
      });
      item.classList.add("is-on");
      item.setAttribute("aria-current", "page");
    });
  });
});''',
            }
        ],
    },
    {
        "folder": "navigation",
        "slug": "stepper",
        "title": "Stepper / Progress Steps",
        "desc": "Horizontal and vertical step indicators with working controls.",
        "idx_desc": "Progress steps with next/back controls.",
        "mini": '<div class="p-steps"><i class="done"></i><b class="done"></b><i class="done"></i><b></b><i></i><b></b><i></i></div>',
        "blocks": [
            {
                "id": "stepper-horizontal",
                "title": "Horizontal stepper",
                "note": "Next / Back se state badlein.",
                "html": '''<div class="sh-wrap">
  <ol class="sh-steps" id="shSteps">
    <li class="sh-step is-now" aria-current="step">
      <span class="sh-dot">1</span>
      <span class="sh-lb">Cart</span>
    </li>
    <li class="sh-step">
      <span class="sh-dot">2</span>
      <span class="sh-lb">Shipping</span>
    </li>
    <li class="sh-step">
      <span class="sh-dot">3</span>
      <span class="sh-lb">Payment</span>
    </li>
    <li class="sh-step">
      <span class="sh-dot">4</span>
      <span class="sh-lb">Review</span>
    </li>
  </ol>
  <p class="sh-status" id="shStatus" aria-live="polite">Step 1 of 4 — Cart</p>
  <div class="sh-ctrl">
    <button class="sh-btn" type="button" id="shBack" disabled>Back</button>
    <button class="sh-btn sh-go" type="button" id="shNext">Next</button>
  </div>
</div>''',
                "css": '''.sh-wrap { max-width: 520px; margin: 0 auto; }
.sh-steps {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  align-items: flex-start;
}
.sh-step { flex: 1; display: flex; flex-direction: column; align-items: center; gap: 6px; position: relative; }
.sh-step::before {
  content: "";
  position: absolute;
  top: 14px;
  right: 50%;
  width: 100%;
  height: 2px;
  background: var(--border);
}
.sh-step:first-child::before { display: none; }
.sh-step.is-done::before, .sh-step.is-now::before { background: var(--accent); }
.sh-dot {
  position: relative;
  width: 30px;
  height: 30px;
  border-radius: 999px;
  border: 2px solid var(--border);
  background: var(--card);
  color: var(--muted);
  font-size: 0.78rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
}
.sh-step.is-done .sh-dot { background: var(--accent); border-color: var(--accent); color: #fff; }
.sh-step.is-now .sh-dot { border-color: var(--accent); color: var(--accent); box-shadow: 0 0 0 4px var(--accent-soft); }
.sh-lb { font-size: 0.74rem; font-weight: 600; color: var(--muted); }
.sh-step.is-now .sh-lb { color: var(--text); }
.sh-status { text-align: center; font-size: 0.8rem; color: var(--muted); margin: 16px 0 12px; }
.sh-ctrl { display: flex; justify-content: center; gap: 10px; }
.sh-btn {
  font: inherit;
  font-size: 0.85rem;
  font-weight: 600;
  padding: 9px 18px;
  border-radius: var(--radius);
  border: 1px solid var(--border);
  background: var(--card);
  color: var(--text);
  cursor: pointer;
}
.sh-btn:hover:not(:disabled) { border-color: var(--accent); color: var(--accent); }
.sh-btn:disabled { opacity: 0.45; cursor: not-allowed; }
.sh-go { background: var(--accent); border-color: var(--accent); color: #fff; }
.sh-go:hover:not(:disabled) { opacity: 0.92; color: #fff; }
.sh-btn:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
@media (max-width: 480px) {
  .sh-lb { font-size: 0.66rem; }
  .sh-dot { width: 26px; height: 26px; font-size: 0.7rem; }
  .sh-step::before { top: 12px; }
}''',
                "js": '''(function () {
  var steps = Array.prototype.slice.call(document.querySelectorAll("#shSteps .sh-step"));
  var status = document.getElementById("shStatus");
  var back = document.getElementById("shBack");
  var next = document.getElementById("shNext");
  var names = ["Cart", "Shipping", "Payment", "Review"];
  var cur = 0;

  function render() {
    steps.forEach(function (s, i) {
      s.classList.toggle("is-done", i < cur);
      s.classList.toggle("is-now", i === cur);
      if (i === cur) s.setAttribute("aria-current", "step");
      else s.removeAttribute("aria-current");
      s.querySelector(".sh-dot").textContent = i < cur ? "\\u2713" : String(i + 1);
    });
    status.textContent = "Step " + (cur + 1) + " of " + steps.length + " — " + names[cur];
    back.disabled = cur === 0;
    next.disabled = cur === steps.length - 1;
  }

  back.addEventListener("click", function () { if (cur > 0) { cur--; render(); } });
  next.addEventListener("click", function () { if (cur < steps.length - 1) { cur++; render(); } });
  render();
})();''',
            },
            {
                "id": "stepper-vertical",
                "title": "Vertical stepper",
                "html": '''<ol class="sv-steps">
  <li class="sv-step is-done">
    <span class="sv-dot">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg>
    </span>
    <div class="sv-body">
      <p class="sv-h">Order placed</p>
      <p class="sv-d">12 Oct, 9:12 AM</p>
    </div>
  </li>
  <li class="sv-step is-done">
    <span class="sv-dot">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg>
    </span>
    <div class="sv-body">
      <p class="sv-h">Packed</p>
      <p class="sv-d">12 Oct, 2:40 PM</p>
    </div>
  </li>
  <li class="sv-step is-now" aria-current="step">
    <span class="sv-dot">3</span>
    <div class="sv-body">
      <p class="sv-h">Out for delivery</p>
      <p class="sv-d">Expected by 6:00 PM</p>
    </div>
  </li>
  <li class="sv-step">
    <span class="sv-dot">4</span>
    <div class="sv-body">
      <p class="sv-h">Delivered</p>
      <p class="sv-d">Pending</p>
    </div>
  </li>
</ol>''',
                "css": '''.sv-steps { list-style: none; margin: 0; padding: 0; max-width: 360px; }
.sv-step { display: flex; gap: 12px; position: relative; padding-bottom: 22px; }
.sv-step:last-child { padding-bottom: 0; }
.sv-step::before {
  content: "";
  position: absolute;
  left: 13px;
  top: 30px;
  bottom: 4px;
  width: 2px;
  background: var(--border);
}
.sv-step:last-child::before { display: none; }
.sv-step.is-done::before { background: var(--accent); }
.sv-dot {
  position: relative;
  z-index: 1;
  width: 28px;
  height: 28px;
  border-radius: 999px;
  border: 2px solid var(--border);
  background: var(--card);
  color: var(--muted);
  font-size: 0.74rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  flex: 0 0 auto;
}
.sv-dot svg { width: 13px; height: 13px; }
.sv-step.is-done .sv-dot { background: var(--accent); border-color: var(--accent); color: #fff; }
.sv-step.is-now .sv-dot { border-color: var(--accent); color: var(--accent); box-shadow: 0 0 0 4px var(--accent-soft); }
.sv-body { padding-top: 3px; }
.sv-h { margin: 0; font-size: 0.88rem; font-weight: 600; }
.sv-step:not(.is-done):not(.is-now) .sv-h { color: var(--muted); }
.sv-d { margin: 2px 0 0; font-size: 0.74rem; color: var(--muted); }''',
            },
        ],
    },
    {
        "folder": "layout",
        "slug": "split-screen",
        "title": "Split Screen Layout",
        "desc": "Two-pane layout that stacks on small screens.",
        "idx_desc": "Two-pane auth style layout, stacks on mobile.",
        "cat_id": "layout",
        "mini": '<div class="p-frame"><div class="p-sidebar"></div><div class="p-content"><span class="p-line" style="width: 60%;"></span><span class="p-line" style="width: 40%;"></span></div></div>',
        "blocks": [
            {
                "id": "split-screen",
                "title": "Split screen",
                "html": '''<div class="ss-wrap">
  <div class="ss-left">
    <p class="ss-k">Welcome back</p>
    <h3 class="ss-h">Sign in to your account</h3>
    <label class="ss-lb" for="ssE">Email</label>
    <input class="ss-in" id="ssE" type="email" placeholder="you@example.com" />
    <label class="ss-lb" for="ssP">Password</label>
    <input class="ss-in" id="ssP" type="password" placeholder="Enter password" />
    <button class="ss-btn" type="button">Sign in</button>
    <p class="ss-note">New here? <span class="ss-lnk">Create an account</span></p>
  </div>
  <div class="ss-right">
    <span class="ss-mark"></span>
    <p class="ss-quote">"Design once, reuse everywhere."</p>
    <ul class="ss-list">
      <li>120+ copyable components</li>
      <li>Light and dark themes</li>
      <li>Zero dependencies</li>
    </ul>
  </div>
</div>''',
                "css": '''.ss-wrap {
  display: grid;
  grid-template-columns: 1fr 1fr;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  overflow: hidden;
  background: var(--card);
  box-shadow: var(--shadow);
}
.ss-left { padding: 26px 24px; }
.ss-k { margin: 0; font-size: 0.72rem; font-weight: 700; letter-spacing: 0.07em; text-transform: uppercase; color: var(--accent); }
.ss-h { margin: 4px 0 18px; font-size: 1.15rem; letter-spacing: -0.01em; }
.ss-lb { display: block; font-size: 0.78rem; font-weight: 600; margin-bottom: 5px; }
.ss-in {
  width: 100%;
  box-sizing: border-box;
  font: inherit;
  font-size: 0.9rem;
  padding: 10px 12px;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  background: var(--bg);
  color: var(--text);
  margin-bottom: 13px;
}
.ss-in:focus { outline: 2px solid var(--accent); outline-offset: 1px; border-color: var(--accent); }
.ss-btn {
  width: 100%;
  border: 0;
  background: var(--accent);
  color: #fff;
  font: inherit;
  font-size: 0.92rem;
  font-weight: 600;
  padding: 11px;
  border-radius: var(--radius);
  cursor: pointer;
  margin-top: 4px;
}
.ss-btn:hover { opacity: 0.92; }
.ss-btn:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.ss-note { margin: 14px 0 0; font-size: 0.78rem; color: var(--muted); text-align: center; }
.ss-lnk { color: var(--accent); font-weight: 600; cursor: pointer; }
.ss-right {
  background: linear-gradient(150deg, var(--accent), #7c3aed);
  color: #fff;
  padding: 30px 26px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 12px;
}
.ss-mark { width: 36px; height: 36px; border-radius: 8px; background: rgba(255, 255, 255, 0.22); }
.ss-quote { margin: 0; font-size: 1.15rem; font-weight: 700; line-height: 1.35; letter-spacing: -0.01em; }
.ss-list { margin: 0; padding: 0; list-style: none; display: flex; flex-direction: column; gap: 8px; font-size: 0.85rem; opacity: 0.92; }
.ss-list li::before { content: "\\2713"; margin-right: 8px; font-weight: 700; }
@media (max-width: 768px) {
  .ss-wrap { grid-template-columns: 1fr; }
  .ss-right { order: -1; padding: 22px 20px; gap: 8px; }
  .ss-quote { font-size: 1rem; }
}''',
            }
        ],
    },
    {
        "folder": "layout",
        "slug": "accordion",
        "title": "Accordion / Collapsible Sections",
        "desc": "Single-open and multi-open accordions with smooth animation.",
        "idx_desc": "Collapsible sections, single or multi open.",
        "cat_id": "layout",
        "mini": '<div class="p-table"><span></span><span></span><span></span></div>',
        "blocks": [
            {
                "id": "accordion-single",
                "title": "Single open",
                "note": "Ek khule tab baaki band.",
                "html": '''<div class="as-list">
  <div class="as-item is-open">
    <button class="as-head" type="button" id="asH1" aria-expanded="true" aria-controls="asP1">What is OWN Library?
      <svg class="as-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
    </button>
    <div class="as-body" id="asP1" role="region" aria-labelledby="asH1">
      <div class="as-inner"><p>Ek personal component library jisme har UI ka live preview aur copyable code milta hai.</p></div>
    </div>
  </div>
  <div class="as-item">
    <button class="as-head" type="button" id="asH2" aria-expanded="false" aria-controls="asP2">Kya code copy kar sakte hain?
      <svg class="as-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
    </button>
    <div class="as-body" id="asP2" role="region" aria-labelledby="asH2">
      <div class="as-inner"><p>Har component ke HTML, CSS aur JS tabs hain — ek click me poora code copy ho jata hai.</p></div>
    </div>
  </div>
  <div class="as-item">
    <button class="as-head" type="button" id="asH3" aria-expanded="false" aria-controls="asP3">Dark mode supported hai?
      <svg class="as-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
    </button>
    <div class="as-body" id="asP3" role="region" aria-labelledby="asH3">
      <div class="as-inner"><p>Haan — sab components design tokens par bane hain, theme switch par automatically adapt hote hain.</p></div>
    </div>
  </div>
  <div class="as-item">
    <button class="as-head" type="button" id="asH4" aria-expanded="false" aria-controls="asP4">Mobile pe kaisa chalta hai?
      <svg class="as-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
    </button>
    <div class="as-body" id="asP4" role="region" aria-labelledby="asH4">
      <div class="as-inner"><p>Har page responsive hai — 360px width tak sab components sahi dikhte hain.</p></div>
    </div>
  </div>
</div>''',
                "css": '''.as-list {
  border: 1px solid var(--border);
  border-radius: var(--radius);
  background: var(--card);
  overflow: hidden;
  max-width: 520px;
}
.as-item + .as-item { border-top: 1px solid var(--border); }
.as-head {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  border: 0;
  background: transparent;
  color: var(--text);
  font: inherit;
  font-size: 0.9rem;
  font-weight: 600;
  text-align: left;
  padding: 14px 16px;
  cursor: pointer;
}
.as-head:hover { background: var(--bg); }
.as-head:focus-visible { outline: 2px solid var(--accent); outline-offset: -2px; }
.as-chev { width: 16px; height: 16px; color: var(--muted); transition: transform 0.25s; flex: 0 0 auto; }
.as-item.is-open .as-chev { transform: rotate(180deg); color: var(--accent); }
.as-body { display: grid; grid-template-rows: 0fr; transition: grid-template-rows 0.25s ease; }
.as-item.is-open .as-body { grid-template-rows: 1fr; }
.as-inner { overflow: hidden; }
.as-inner p { margin: 0; padding: 0 16px 14px; font-size: 0.85rem; color: var(--muted); line-height: 1.55; }''',
                "js": '''document.querySelectorAll(".as-list").forEach(function (list) {
  var items = Array.prototype.slice.call(list.querySelectorAll(".as-item"));
  items.forEach(function (item) {
    var head = item.querySelector(".as-head");
    head.addEventListener("click", function () {
      var open = item.classList.contains("is-open");
      items.forEach(function (other) {
        other.classList.remove("is-open");
        other.querySelector(".as-head").setAttribute("aria-expanded", "false");
      });
      if (!open) {
        item.classList.add("is-open");
        head.setAttribute("aria-expanded", "true");
      }
    });
  });
});''',
            },
            {
                "id": "accordion-multiple",
                "title": "Multi open",
                "html": '''<div class="am-list">
  <div class="am-item is-open">
    <button class="am-head" type="button" id="amH1" aria-expanded="true" aria-controls="amP1">General
      <svg class="am-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
    </button>
    <div class="am-body" id="amP1" role="region" aria-labelledby="amH1">
      <div class="am-inner"><p>Workspace name, language aur timezone settings.</p></div>
    </div>
  </div>
  <div class="am-item is-open">
    <button class="am-head" type="button" id="amH2" aria-expanded="true" aria-controls="amP2">Notifications
      <svg class="am-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
    </button>
    <div class="am-body" id="amP2" role="region" aria-labelledby="amH2">
      <div class="am-inner"><p>Email, push aur weekly digest preferences.</p></div>
    </div>
  </div>
  <div class="am-item">
    <button class="am-head" type="button" id="amH3" aria-expanded="false" aria-controls="amP3">Integrations
      <svg class="am-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
    </button>
    <div class="am-body" id="amP3" role="region" aria-labelledby="amH3">
      <div class="am-inner"><p>Slack, GitHub aur Figma connections manage karein.</p></div>
    </div>
  </div>
  <div class="am-item">
    <button class="am-head" type="button" id="amH4" aria-expanded="false" aria-controls="amP4">Billing
      <svg class="am-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
    </button>
    <div class="am-body" id="amP4" role="region" aria-labelledby="amH4">
      <div class="am-inner"><p>Plan details, invoices aur payment methods.</p></div>
    </div>
  </div>
</div>''',
                "css": '''.am-list {
  border: 1px solid var(--border);
  border-radius: var(--radius);
  background: var(--card);
  overflow: hidden;
  max-width: 520px;
}
.am-item + .am-item { border-top: 1px solid var(--border); }
.am-head {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  border: 0;
  background: transparent;
  color: var(--text);
  font: inherit;
  font-size: 0.9rem;
  font-weight: 600;
  text-align: left;
  padding: 14px 16px;
  cursor: pointer;
}
.am-head:hover { background: var(--bg); }
.am-head:focus-visible { outline: 2px solid var(--accent); outline-offset: -2px; }
.am-chev { width: 16px; height: 16px; color: var(--muted); transition: transform 0.25s; flex: 0 0 auto; }
.am-item.is-open .am-chev { transform: rotate(180deg); color: var(--accent); }
.am-body { display: grid; grid-template-rows: 0fr; transition: grid-template-rows 0.25s ease; }
.am-item.is-open .am-body { grid-template-rows: 1fr; }
.am-inner { overflow: hidden; }
.am-inner p { margin: 0; padding: 0 16px 14px; font-size: 0.85rem; color: var(--muted); line-height: 1.55; }''',
                "js": '''document.querySelectorAll(".am-list").forEach(function (list) {
  list.querySelectorAll(".am-head").forEach(function (head) {
    head.addEventListener("click", function () {
      var item = head.closest(".am-item");
      var open = item.classList.toggle("is-open");
      head.setAttribute("aria-expanded", String(open));
    });
  });
});''',
            },
        ],
    },
    {
        "folder": "layout",
        "slug": "responsive-table",
        "title": "Responsive Table",
        "desc": "Data table that becomes stacked cards on small screens.",
        "idx_desc": "Table with status pills that stacks on mobile.",
        "cat_id": "layout",
        "mini": '<div class="p-table"><span></span><span></span><span></span></div>',
        "blocks": [
            {
                "id": "responsive-table",
                "title": "Responsive table",
                "note": "640px se chhoti width par cards ban jate hain.",
                "html": '''<div class="rt-wrap">
  <table class="rt-table" aria-label="Recent orders">
    <thead>
      <tr>
        <th scope="col">Customer</th>
        <th scope="col">Order</th>
        <th scope="col">Date</th>
        <th scope="col">Status</th>
        <th scope="col" class="rt-num">Amount</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td data-label="Customer">Aman Kumar</td>
        <td data-label="Order">#1024</td>
        <td data-label="Date">12 Oct</td>
        <td data-label="Status"><span class="rt-pill rt-yes">Paid</span></td>
        <td data-label="Amount" class="rt-num">₹1,240</td>
      </tr>
      <tr>
        <td data-label="Customer">Riya Sharma</td>
        <td data-label="Order">#1025</td>
        <td data-label="Date">12 Oct</td>
        <td data-label="Status"><span class="rt-pill rt-warn">Pending</span></td>
        <td data-label="Amount" class="rt-num">₹860</td>
      </tr>
      <tr>
        <td data-label="Customer">Vikram Singh</td>
        <td data-label="Order">#1026</td>
        <td data-label="Date">11 Oct</td>
        <td data-label="Status"><span class="rt-pill rt-accent">Shipped</span></td>
        <td data-label="Amount" class="rt-num">₹2,150</td>
      </tr>
      <tr>
        <td data-label="Customer">Neha Gupta</td>
        <td data-label="Order">#1027</td>
        <td data-label="Date">11 Oct</td>
        <td data-label="Status"><span class="rt-pill rt-no">Failed</span></td>
        <td data-label="Amount" class="rt-num">₹499</td>
      </tr>
      <tr>
        <td data-label="Customer">Arjun Mehta</td>
        <td data-label="Order">#1028</td>
        <td data-label="Date">10 Oct</td>
        <td data-label="Status"><span class="rt-pill rt-yes">Paid</span></td>
        <td data-label="Amount" class="rt-num">₹3,400</td>
      </tr>
    </tbody>
  </table>
</div>''',
                "css": '''.rt-wrap {
  border: 1px solid var(--border);
  border-radius: var(--radius);
  background: var(--card);
  overflow: hidden;
}
.rt-table { width: 100%; border-collapse: collapse; font-size: 0.85rem; }
.rt-table th {
  text-align: left;
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--muted);
  padding: 12px 14px;
  border-bottom: 1px solid var(--border);
  background: var(--bg);
}
.rt-table td { padding: 12px 14px; border-bottom: 1px solid var(--border); }
.rt-table tbody tr:last-child td { border-bottom: 0; }
.rt-table tbody tr:hover { background: var(--bg); }
.rt-num { text-align: right; font-variant-numeric: tabular-nums; }
.rt-pill {
  display: inline-block;
  font-size: 0.7rem;
  font-weight: 700;
  padding: 3px 9px;
  border-radius: 999px;
}
.rt-yes { background: rgba(34, 160, 107, 0.12); color: var(--yes); }
.rt-warn { background: rgba(194, 116, 10, 0.12); color: var(--warn); }
.rt-no { background: rgba(229, 72, 77, 0.12); color: var(--no); }
.rt-accent { background: var(--accent-soft); color: var(--accent); }
@media (max-width: 640px) {
  .rt-table thead { display: none; }
  .rt-table, .rt-table tbody, .rt-table tr, .rt-table td { display: block; width: 100%; }
  .rt-table tr { border-bottom: 1px solid var(--border); padding: 6px 0; }
  .rt-table tbody tr:last-child { border-bottom: 0; }
  .rt-table td {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
    border-bottom: 0;
    padding: 6px 14px;
    text-align: right;
  }
  .rt-table td::before {
    content: attr(data-label);
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    color: var(--muted);
    text-align: left;
  }
  .rt-num { text-align: right; }
}''',
            }
        ],
    },
    {
        "folder": "layout",
        "slug": "masonry",
        "title": "Masonry Layout",
        "desc": "Multi-column masonry grid with varied card heights.",
        "idx_desc": "Multi-column masonry with varied heights.",
        "cat_id": "layout",
        "mini": '<div class="p-gal"><span></span><span></span><span></span><span></span></div>',
        "blocks": [
            {
                "id": "masonry",
                "title": "Masonry grid",
                "html": '''<div class="my-grid">
  <div class="my-card">
    <p class="my-k">Design</p>
    <p class="my-t">Token based theming</p>
    <p class="my-d">Har component CSS variables use karta hai — theme switch par sab auto update hote hain.</p>
  </div>
  <div class="my-card">
    <div class="my-media"></div>
    <p class="my-t">Media card</p>
    <p class="my-d">Gradients se bane media blocks.</p>
  </div>
  <div class="my-card">
    <p class="my-t">Short note</p>
    <p class="my-d">Chhota sa card.</p>
  </div>
  <div class="my-card">
    <p class="my-k">Ship</p>
    <p class="my-t">Copy paste ready</p>
    <p class="my-d">HTML, CSS aur JS tabs se code copy karke apne project me directly use karein. Koi build step nahi, koi dependency nahi.</p>
    <span class="my-tag">Popular</span>
  </div>
  <div class="my-card">
    <p class="my-t">Keyboard friendly</p>
    <p class="my-d">Tabs, menus aur dialogs sab keyboard accessible hain with visible focus rings.</p>
  </div>
  <div class="my-card">
    <div class="my-media my-media-2"></div>
    <p class="my-t">Gradient tile</p>
  </div>
  <div class="my-card">
    <p class="my-t">Responsive</p>
    <p class="my-d">Columns kam hote jate hain — 3 se 2, phir 1.</p>
  </div>
  <div class="my-card">
    <p class="my-k">New</p>
    <p class="my-t">120+ blocks</p>
    <p class="my-d">Har category me useful variants.</p>
  </div>
</div>''',
                "css": '''.my-grid { columns: 3; column-gap: 14px; }
.my-card {
  break-inside: avoid;
  margin-bottom: 14px;
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 14px;
  box-shadow: var(--shadow);
}
.my-k { margin: 0 0 4px; font-size: 0.66rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: var(--accent); }
.my-t { margin: 0 0 4px; font-size: 0.92rem; font-weight: 700; }
.my-d { margin: 0; font-size: 0.8rem; color: var(--muted); line-height: 1.5; }
.my-media { height: 90px; border-radius: 5px; background: linear-gradient(135deg, var(--accent-soft), transparent), var(--bg); border: 1px solid var(--border); margin-bottom: 10px; }
.my-media-2 { background: linear-gradient(135deg, var(--accent), #8b5cf6); }
.my-tag {
  display: inline-block;
  margin-top: 8px;
  font-size: 0.66rem;
  font-weight: 700;
  color: var(--accent);
  background: var(--accent-soft);
  padding: 3px 8px;
  border-radius: 999px;
}
@media (max-width: 768px) { .my-grid { columns: 2; } }
@media (max-width: 480px) { .my-grid { columns: 1; } }''',
            }
        ],
    },
    {
        "folder": "layout",
        "slug": "infinite-scroll",
        "title": "Infinite Scroll",
        "desc": "Feed that loads more items near the end of the list.",
        "idx_desc": "Auto-loading feed with sentinel and reset.",
        "cat_id": "layout",
        "mini": '<div class="p-listrow"><span class="p-avatar"></span><span class="p-line" style="width: 60px;"></span></div>',
        "blocks": [
            {
                "id": "infinite-scroll",
                "title": "Infinite scroll feed",
                "note": "Neeche scroll karein — items auto load honge.",
                "html": '''<div class="is-wrap">
  <div class="is-list" id="isList"></div>
  <div class="is-sent" id="isSent" aria-hidden="true"></div>
  <div class="is-load" id="isLoad" hidden><span class="is-spin" aria-hidden="true"></span> Loading more…</div>
  <p class="is-end" id="isEnd" hidden>You're all caught up.</p>
  <button class="is-reset" type="button" id="isReset">Reset demo</button>
</div>''',
                "css": '''.is-wrap { max-width: 420px; margin: 0 auto; position: relative; }
.is-list { display: flex; flex-direction: column; gap: 10px; }
.is-item {
  display: flex;
  gap: 10px;
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 12px;
}
.is-av {
  width: 34px;
  height: 34px;
  border-radius: 999px;
  background: var(--accent-soft);
  color: var(--accent);
  font-size: 0.72rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  flex: 0 0 auto;
}
.is-body { min-width: 0; }
.is-name { margin: 0; font-size: 0.82rem; font-weight: 600; }
.is-text { margin: 2px 0 0; font-size: 0.78rem; color: var(--muted); line-height: 1.45; }
.is-sent { height: 1px; }
.is-load {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 14px;
  font-size: 0.8rem;
  color: var(--muted);
}
.is-spin {
  width: 15px;
  height: 15px;
  border: 2px solid var(--border);
  border-top-color: var(--accent);
  border-radius: 999px;
  animation: is-spin 0.8s linear infinite;
}
@keyframes is-spin { to { transform: rotate(360deg); } }
.is-end { text-align: center; font-size: 0.8rem; color: var(--muted); padding: 14px; margin: 0; }
.is-reset {
  display: block;
  margin: 12px auto 0;
  font: inherit;
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--accent);
  background: transparent;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 8px 14px;
  cursor: pointer;
}
.is-reset:hover { border-color: var(--accent); }
.is-reset:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
@media (prefers-reduced-motion: reduce) {
  .is-spin { animation: none; }
}''',
                "js": '''(function () {
  var list = document.getElementById("isList");
  var sent = document.getElementById("isSent");
  var load = document.getElementById("isLoad");
  var end = document.getElementById("isEnd");
  var reset = document.getElementById("isReset");
  var names = ["Aman Kumar", "Riya Sharma", "Vikram Singh", "Neha Gupta", "Arjun Mehta", "Sara Khan", "Dev Patel", "Isha Rao", "Kabir Joshi", "Meera Nair"];
  var texts = ["Naya component library use kar raha hoon.", "Dashboard layout bahut clean bana hai.", "Copy button se code uthana super easy.", "Dark mode bhi perfect lag raha hai.", "Mobile preview toggle kaam karta hai.", "Accordion smooth animate ho raha hai.", "Table mobile pe cards ban jata hai.", "Stepper ke controls working hain.", "Toast notifications useful hain.", "Tokens sab jagah consistent rakhte hain."];
  var idx = 0;
  var batches = 0;
  var MAX = 3;
  var busy = false;

  function makeItem() {
    var i = idx % names.length;
    var div = document.createElement("div");
    div.className = "is-item";
    var av = document.createElement("span");
    av.className = "is-av";
    av.textContent = names[i].split(" ").map(function (w) { return w[0]; }).join("").slice(0, 2);
    var body = document.createElement("div");
    body.className = "is-body";
    var name = document.createElement("p");
    name.className = "is-name";
    name.textContent = names[i];
    var text = document.createElement("p");
    text.className = "is-text";
    text.textContent = texts[i % texts.length];
    body.appendChild(name);
    body.appendChild(text);
    div.appendChild(av);
    div.appendChild(body);
    idx++;
    return div;
  }

  function appendBatch(n) {
    var frag = document.createDocumentFragment();
    for (var i = 0; i < n; i++) frag.appendChild(makeItem());
    list.appendChild(frag);
  }

  function finish() {
    load.hidden = true;
    end.hidden = false;
    busy = false;
  }

  function loadMore() {
    if (busy || !end.hidden) return;
    busy = true;
    load.hidden = false;
    setTimeout(function () {
      appendBatch(3);
      batches++;
      load.hidden = true;
      busy = false;
      if (batches >= MAX) end.hidden = false;
    }, 600);
  }

  function start() {
    list.textContent = "";
    idx = 0;
    batches = 0;
    busy = false;
    end.hidden = true;
    load.hidden = true;
    appendBatch(4);
  }

  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      if (entries.some(function (e) { return e.isIntersecting; })) loadMore();
    }, { rootMargin: "120px" });
    io.observe(sent);
  } else {
    appendBatch(3);
  }

  reset.addEventListener("click", start);
  start();
})();''',
            }
        ],
    },
]
