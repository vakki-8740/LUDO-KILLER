CAT = "Feedback"
CAT_ID = "feedback"

PAGES = [
 {
  "folder": "feedback", "slug": "toast", "title": "Toast Notifications",
  "desc": "Stacked toasts with variants, auto-dismiss and close buttons.",
  "idx_desc": "Stacked toasts with variants and auto-dismiss.",
  "mini": '<div class="p-drop" style="width: 64px; padding: 6px;"><span class="p-line" style="width: 40px;"></span><span class="p-line" style="width: 30px;"></span></div>',
  "blocks": [{
   "id": "toasts", "title": "Toast stack",
   "note": "Buttons se toast trigger karein — right side stack me aayenge.",
   "html": '''<div class="ts-demo">
  <div class="ts-btns">
    <button class="ts-trig" type="button" data-variant="success">Success toast</button>
    <button class="ts-trig" type="button" data-variant="error">Error toast</button>
    <button class="ts-trig" type="button" data-variant="warning">Warning toast</button>
    <button class="ts-trig" type="button" data-variant="info">Info toast</button>
  </div>
  <div class="ts-stack" id="tsStack" aria-live="polite" aria-atomic="false"></div>
</div>''',
   "css": '''.ts-demo { position: relative; min-height: 280px; border: 1px dashed var(--border); border-radius: var(--radius); padding: 14px; overflow: hidden; }
.ts-btns { display: flex; flex-wrap: wrap; gap: 8px; align-content: flex-start; max-width: 55%; }
.ts-trig {
  border: 1px solid var(--border);
  background: var(--card);
  color: var(--text);
  font: inherit;
  font-size: 0.8rem;
  font-weight: 600;
  padding: 8px 12px;
  border-radius: var(--radius);
  cursor: pointer;
}
.ts-trig:hover { border-color: var(--accent); color: var(--accent); }
.ts-trig:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.ts-stack { position: absolute; top: 14px; right: 14px; display: flex; flex-direction: column; gap: 8px; width: min(270px, 60%); }
.ts-pill {
  display: flex;
  align-items: flex-start;
  gap: 8px;
  background: var(--card);
  border: 1px solid var(--border);
  border-left: 3px solid var(--accent);
  border-radius: var(--radius);
  padding: 10px 10px 12px;
  box-shadow: var(--shadow);
  animation: tsIn 0.22s ease-out;
  position: relative;
  overflow: hidden;
}
.ts-pill.is-success { border-left-color: var(--yes); }
.ts-pill.is-error { border-left-color: var(--no); }
.ts-pill.is-warning { border-left-color: var(--warn); }
.ts-pill.is-info { border-left-color: var(--accent); }
.ts-ic { width: 17px; height: 17px; flex: 0 0 auto; margin-top: 1px; }
.ts-pill.is-success .ts-ic { color: var(--yes); }
.ts-pill.is-error .ts-ic { color: var(--no); }
.ts-pill.is-warning .ts-ic { color: var(--warn); }
.ts-pill.is-info .ts-ic { color: var(--accent); }
.ts-txt { flex: 1; }
.ts-t { display: block; font-size: 0.8rem; font-weight: 700; margin-bottom: 1px; }
.ts-m { display: block; font-size: 0.74rem; color: var(--muted); line-height: 1.35; }
.ts-x { border: 0; background: transparent; color: var(--muted); cursor: pointer; padding: 0 2px; font-size: 1rem; line-height: 1; }
.ts-x:hover { color: var(--text); }
.ts-bar { position: absolute; left: 0; bottom: 0; height: 2px; width: 100%; background: currentColor; opacity: 0.35; transform-origin: left; animation: tsCountdown 3.4s linear forwards; }
@keyframes tsIn { from { opacity: 0; transform: translateX(14px); } to { opacity: 1; transform: translateX(0); } }
@keyframes tsCountdown { from { transform: scaleX(1); } to { transform: scaleX(0); } }
@media (prefers-reduced-motion: reduce) {
  .ts-pill, .ts-bar { animation: none; }
}''',
   "js": '''(function () {
  var stack = document.getElementById("tsStack");
  var data = {
    success: ["Saved", "Your changes were saved.", '<svg class="ts-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg>'],
    error: ["Something went wrong", "Please try again in a moment.", '<svg class="ts-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8v5M12 16.5v.5"/></svg>'],
    warning: ["Check your input", "Two fields need attention.", '<svg class="ts-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 4l9 16H3z"/><path d="M12 10v4M12 17v.5"/></svg>'],
    info: ["Heads up", "A new version is available.", '<svg class="ts-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 7.5v.5"/></svg>']
  };

  function remove(el) {
    el.style.opacity = "0";
    setTimeout(function () { if (el.parentNode) el.parentNode.removeChild(el); }, 180);
  }

  document.querySelectorAll(".ts-trig").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var v = btn.getAttribute("data-variant");
      var d = data[v];
      while (stack.children.length >= 3) stack.removeChild(stack.firstChild);
      var el = document.createElement("div");
      el.className = "ts-pill is-" + v;
      el.innerHTML = d[2] + '<div class="ts-txt"><span class="ts-t">' + d[0] + '</span><span class="ts-m">' + d[1] + '</span></div><button class="ts-x" type="button" aria-label="Dismiss">&times;</button><span class="ts-bar"></span>';
      el.querySelector(".ts-x").addEventListener("click", function () { remove(el); });
      stack.appendChild(el);
      setTimeout(function () { remove(el); }, 3400);
    });
  });
})();''',
  }],
 },
 {
  "folder": "feedback", "slug": "snackbar", "title": "Snackbar",
  "desc": "Bottom snackbar with an undo action.",
  "idx_desc": "Bottom snackbar with undo action.",
  "mini": '<div class="p-line" style="width: 56px;"></div><div class="p-line" style="width: 34px; border-color: var(--yes);"></div>',
  "blocks": [{
   "id": "snackbar", "title": "Snackbar with undo",
   "note": "Delete dabaiye — snackbar me Undo milega.",
   "html": '''<div class="sn-demo">
  <div class="sn-body">
    <p class="sn-count">Items: <strong id="snCount">3</strong></p>
    <button class="sn-del" type="button" id="snDel">Delete item</button>
  </div>
  <div class="sn-bar" id="snBar" role="status" hidden>
    <span class="sn-msg" id="snMsg">Item deleted.</span>
    <button class="sn-undo" type="button" id="snUndo">Undo</button>
  </div>
</div>''',
   "css": '''.sn-demo { position: relative; min-height: 220px; border: 1px dashed var(--border); border-radius: var(--radius); padding: 16px; overflow: hidden; }
.sn-count { margin: 0 0 10px; font-size: 0.9rem; }
.sn-del {
  border: 1px solid rgba(229, 72, 77, 0.4);
  background: rgba(229, 72, 77, 0.08);
  color: var(--no);
  font: inherit;
  font-size: 0.82rem;
  font-weight: 600;
  padding: 8px 14px;
  border-radius: var(--radius);
  cursor: pointer;
}
.sn-del:hover { border-color: var(--no); }
.sn-del:focus-visible { outline: 2px solid var(--no); outline-offset: 2px; }
.sn-bar {
  position: absolute;
  left: 16px;
  right: 16px;
  bottom: 16px;
  display: flex;
  align-items: center;
  gap: 10px;
  background: #242833;
  color: #f3f4f8;
  border-radius: var(--radius);
  padding: 10px 12px;
  box-shadow: var(--shadow);
  animation: snUp 0.22s ease-out;
}
.sn-msg { flex: 1; font-size: 0.8rem; }
.sn-undo {
  border: 0;
  background: transparent;
  color: #9db0ff;
  font: inherit;
  font-size: 0.8rem;
  font-weight: 700;
  cursor: pointer;
  padding: 4px 6px;
  border-radius: 3px;
}
.sn-undo:hover { background: rgba(157, 176, 255, 0.14); }
.sn-undo:focus-visible { outline: 2px solid #9db0ff; outline-offset: 2px; }
@keyframes snUp { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
@media (prefers-reduced-motion: reduce) { .sn-bar { animation: none; } }''',
   "js": '''(function () {
  var count = 3;
  var countEl = document.getElementById("snCount");
  var bar = document.getElementById("snBar");
  var msg = document.getElementById("snMsg");
  var timer = null;

  function hide() {
    bar.hidden = true;
    if (timer) { clearTimeout(timer); timer = null; }
  }

  document.getElementById("snDel").addEventListener("click", function () {
    if (count <= 0) { msg.textContent = "Nothing left to delete."; bar.hidden = false; return; }
    count -= 1;
    countEl.textContent = count;
    msg.textContent = "Item deleted.";
    bar.hidden = false;
    if (timer) clearTimeout(timer);
    timer = setTimeout(hide, 4200);
  });

  document.getElementById("snUndo").addEventListener("click", function () {
    count += 1;
    countEl.textContent = count;
    msg.textContent = "Item restored.";
    if (timer) clearTimeout(timer);
    timer = setTimeout(hide, 2200);
  });
})();''',
  }],
 },
 {
  "folder": "feedback", "slug": "empty-state", "title": "Empty States",
  "desc": "Illustrated empty states for inbox, search and files.",
  "idx_desc": "Illustrated empty states with clear actions.",
  "mini": '<div class="p-page" style="height: 48px;"><span class="p-line" style="width: 34px;"></span><span class="p-line" style="width: 24px;"></span></div>',
  "blocks": [
   {"id": "empty-inbox", "title": "Inbox", "html": '''<div class="em-card">
  <div class="em-art">
    <svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 22h48v28a4 4 0 0 1-4 4H12a4 4 0 0 1-4-4z"/><path d="M8 22l10-12h28l10 12"/><path d="M8 22l16 12h16l16-12"/></svg>
  </div>
  <h4 class="em-t">Inbox zero</h4>
  <p class="em-d">No new messages right now. You are all caught up.</p>
  <button class="em-btn" type="button">Compose message</button>
</div>''', "css": '''.em-card { text-align: center; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 34px 20px; }
.em-art { width: 64px; height: 64px; margin: 0 auto 14px; color: var(--accent); opacity: 0.85; }
.em-art svg { width: 100%; height: 100%; }
.em-t { margin: 0 0 4px; font-size: 1rem; }
.em-d { margin: 0 auto 16px; max-width: 280px; font-size: 0.82rem; color: var(--muted); line-height: 1.5; }
.em-btn { border: 0; background: var(--accent); color: #fff; font: inherit; font-size: 0.82rem; font-weight: 600; padding: 9px 16px; border-radius: var(--radius); cursor: pointer; }
.em-btn:hover { opacity: 0.92; }
.em-btn:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }'''},
   {"id": "empty-search", "title": "Search", "html": '''<div class="em-card">
  <div class="em-art em-warn">
    <svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="28" cy="28" r="16"/><path d="M40 40l14 14M22 24h12M22 31h8"/></svg>
  </div>
  <h4 class="em-t">No results found</h4>
  <p class="em-d">Try a shorter keyword or remove filters to widen the search.</p>
  <button class="em-btn em-ghost" type="button">Clear filters</button>
</div>''', "css": '''.em-card { text-align: center; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 34px 20px; }
.em-art { width: 64px; height: 64px; margin: 0 auto 14px; color: var(--accent); opacity: 0.85; }
.em-art svg { width: 100%; height: 100%; }
.em-warn { color: var(--warn); }
.em-t { margin: 0 0 4px; font-size: 1rem; }
.em-d { margin: 0 auto 16px; max-width: 280px; font-size: 0.82rem; color: var(--muted); line-height: 1.5; }
.em-btn { border: 0; background: var(--accent); color: #fff; font: inherit; font-size: 0.82rem; font-weight: 600; padding: 9px 16px; border-radius: var(--radius); cursor: pointer; }
.em-btn:hover { opacity: 0.92; }
.em-btn:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.em-ghost { background: transparent; color: var(--accent); border: 1px solid var(--border); }
.em-ghost:hover { border-color: var(--accent); opacity: 1; }'''},
   {"id": "empty-files", "title": "Files", "html": '''<div class="em-card">
  <div class="em-art">
    <svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 16a4 4 0 0 1 4-4h12l6 8h14a4 4 0 0 1 4 4v26a4 4 0 0 1-4 4H16a4 4 0 0 1-4-4z"/><path d="M32 34v12M26 40l6-6 6 6"/></svg>
  </div>
  <h4 class="em-t">This folder is empty</h4>
  <p class="em-d">Upload your first file to get started. You can drag and drop too.</p>
  <button class="em-btn" type="button">Upload files</button>
</div>''', "css": '''.em-card { text-align: center; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 34px 20px; }
.em-art { width: 64px; height: 64px; margin: 0 auto 14px; color: var(--accent); opacity: 0.85; }
.em-art svg { width: 100%; height: 100%; }
.em-t { margin: 0 0 4px; font-size: 1rem; }
.em-d { margin: 0 auto 16px; max-width: 280px; font-size: 0.82rem; color: var(--muted); line-height: 1.5; }
.em-btn { border: 0; background: var(--accent); color: #fff; font: inherit; font-size: 0.82rem; font-weight: 600; padding: 9px 16px; border-radius: var(--radius); cursor: pointer; }
.em-btn:hover { opacity: 0.92; }
.em-btn:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }'''},
  ],
 },
 {
  "folder": "feedback", "slug": "error-state", "title": "Error States",
  "desc": "Inline retry block and a friendly 404 page.",
  "idx_desc": "Inline retry error and friendly 404 state.",
  "mini": '<div class="p-page" style="height: 48px;"><span class="p-line" style="width: 20px;"></span><span class="p-line" style="width: 34px;"></span></div>',
  "blocks": [
   {"id": "error-inline", "title": "Inline retry", "note": "Retry dabaiye — pehle load hoga, phir error wapas aayega.", "html": '''<div class="er-box" id="erBox">
  <span class="er-ic" aria-hidden="true">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10.3 4.3a2 2 0 0 1 3.4 0l7.2 12.4a2 2 0 0 1-1.7 3H4.8a2 2 0 0 1-1.7-3z"/><path d="M12 9v4M12 16.5v.5"/></svg>
  </span>
  <div class="er-txt">
    <p class="er-t">Could not load activity</p>
    <p class="er-d" id="erDesc">The server did not respond. Check your connection and retry.</p>
  </div>
  <button class="er-btn" type="button" id="erBtn">Retry</button>
</div>''', "css": '''.er-box { display: flex; align-items: flex-start; gap: 12px; flex-wrap: wrap; border: 1px solid rgba(229, 72, 77, 0.35); background: rgba(229, 72, 77, 0.06); border-radius: var(--radius); padding: 14px; }
.er-ic { width: 22px; height: 22px; color: var(--no); flex: 0 0 auto; }
.er-ic svg { width: 100%; height: 100%; }
.er-txt { flex: 1; min-width: 180px; }
.er-t { margin: 0 0 2px; font-size: 0.86rem; font-weight: 700; }
.er-d { margin: 0; font-size: 0.79rem; color: var(--muted); line-height: 1.45; }
.er-btn { border: 1px solid rgba(229, 72, 77, 0.4); background: var(--card); color: var(--no); font: inherit; font-size: 0.78rem; font-weight: 600; padding: 7px 12px; border-radius: var(--radius); cursor: pointer; }
.er-btn:hover { border-color: var(--no); }
.er-btn:focus-visible { outline: 2px solid var(--no); outline-offset: 2px; }
.er-btn[disabled] { opacity: 0.6; cursor: progress; }''', "js": '''(function () {
  var btn = document.getElementById("erBtn");
  var desc = document.getElementById("erDesc");
  btn.addEventListener("click", function () {
    btn.disabled = true;
    btn.textContent = "Retrying...";
    desc.textContent = "Contacting the server...";
    setTimeout(function () {
      btn.disabled = false;
      btn.textContent = "Retry";
      desc.textContent = "Still offline. The demo error returns on purpose.";
    }, 1400);
  });
})();'''},
   {"id": "error-404", "title": "Not found", "html": '''<div class="er-p404">
  <p class="er-code">404</p>
  <h4 class="er-404t">This page took a wrong turn</h4>
  <p class="er-404d">The link may be broken, or the page was moved. Let us get you back on track.</p>
  <div class="er-actions">
    <button class="er-home" type="button">Back to dashboard</button>
    <button class="er-plain" type="button">Contact support</button>
  </div>
</div>''', "css": '''.er-p404 { text-align: center; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 36px 20px; }
.er-code { margin: 0; font-size: 2.6rem; font-weight: 800; letter-spacing: 0.06em; color: var(--accent); line-height: 1; }
.er-404t { margin: 10px 0 4px; font-size: 1.05rem; }
.er-404d { margin: 0 auto 18px; max-width: 300px; font-size: 0.83rem; color: var(--muted); line-height: 1.5; }
.er-actions { display: flex; justify-content: center; gap: 8px; flex-wrap: wrap; }
.er-home { border: 0; background: var(--accent); color: #fff; font: inherit; font-size: 0.82rem; font-weight: 600; padding: 9px 16px; border-radius: var(--radius); cursor: pointer; }
.er-home:hover { opacity: 0.92; }
.er-home:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.er-plain { border: 1px solid var(--border); background: transparent; color: var(--text); font: inherit; font-size: 0.82rem; font-weight: 600; padding: 9px 16px; border-radius: var(--radius); cursor: pointer; }
.er-plain:hover { border-color: var(--accent); color: var(--accent); }
.er-plain:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }'''},
  ],
 },
 {
  "folder": "feedback", "slug": "offline-indicator", "title": "Offline Indicator",
  "desc": "Connection banner that reacts to real online/offline events.",
  "idx_desc": "Connection banner driven by online/offline events.",
  "mini": '<div class="p-line" style="width: 56px; border-color: var(--warn);"></div><div class="p-line" style="width: 36px;"></div>',
  "blocks": [{
   "id": "offline-indicator", "title": "Connection banner",
   "note": "Simulate buttons se banner test karein. Wapas online hote hi auto-hide.",
   "html": '''<div class="of-demo">
  <div class="of-banner" id="ofBanner" role="status" aria-live="polite" hidden>
    <span class="of-dot" aria-hidden="true"></span>
    <span class="of-txt" id="ofTxt">You are offline. Changes will sync when you reconnect.</span>
    <button class="of-retry" type="button" id="ofRetry">Retry</button>
  </div>
  <div class="of-body">
    <p class="of-state">Status: <strong id="ofState">Online</strong></p>
    <div class="of-actions">
      <button class="of-sim" type="button" id="ofOff">Simulate offline</button>
      <button class="of-sim of-on" type="button" id="ofOn">Simulate online</button>
    </div>
  </div>
</div>''',
   "css": '''.of-demo { border: 1px dashed var(--border); border-radius: var(--radius); padding: 14px; min-height: 180px; }
.of-banner {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
  background: rgba(194, 116, 10, 0.12);
  border: 1px solid rgba(194, 116, 10, 0.4);
  color: var(--warn);
  border-radius: var(--radius);
  padding: 9px 12px;
  margin-bottom: 14px;
  font-size: 0.8rem;
  font-weight: 600;
}
.of-dot { width: 8px; height: 8px; border-radius: 999px; background: currentColor; flex: 0 0 auto; animation: ofPulse 1.4s ease-in-out infinite; }
.of-txt { flex: 1; min-width: 150px; }
.of-retry { border: 1px solid currentColor; background: transparent; color: inherit; font: inherit; font-size: 0.74rem; font-weight: 700; padding: 4px 9px; border-radius: 3px; cursor: pointer; }
.of-retry:hover { background: rgba(194, 116, 10, 0.12); }
.of-retry:focus-visible { outline: 2px solid var(--warn); outline-offset: 2px; }
.of-state { margin: 0 0 10px; font-size: 0.85rem; }
.of-actions { display: flex; gap: 8px; flex-wrap: wrap; }
.of-sim { border: 1px solid var(--border); background: var(--card); color: var(--text); font: inherit; font-size: 0.78rem; font-weight: 600; padding: 7px 12px; border-radius: var(--radius); cursor: pointer; }
.of-sim:hover { border-color: var(--accent); color: var(--accent); }
.of-sim:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.of-on { border-color: rgba(34, 160, 107, 0.4); color: var(--yes); }
@keyframes ofPulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.35; } }
@media (prefers-reduced-motion: reduce) { .of-dot { animation: none; } }''',
   "js": '''(function () {
  var banner = document.getElementById("ofBanner");
  var txt = document.getElementById("ofTxt");
  var state = document.getElementById("ofState");
  var online = true;

  function render() {
    banner.hidden = online;
    state.textContent = online ? "Online" : "Offline";
    state.style.color = online ? "var(--yes)" : "var(--no)";
    if (!online) txt.textContent = "You are offline. Changes will sync when you reconnect.";
  }

  document.getElementById("ofOff").addEventListener("click", function () { online = false; render(); });
  document.getElementById("ofOn").addEventListener("click", function () { online = true; render(); });
  document.getElementById("ofRetry").addEventListener("click", function () {
    txt.textContent = "Reconnecting...";
    setTimeout(function () { online = true; render(); }, 900);
  });

  window.addEventListener("online", function () { online = true; render(); });
  window.addEventListener("offline", function () { online = false; render(); });
  render();
})();''',
  }],
 },
 {
  "folder": "feedback", "slug": "notification-center", "title": "Notification Center",
  "desc": "Bell trigger with unread count and a notification panel.",
  "idx_desc": "Bell, unread count and notification panel.",
  "mini": '<div class="p-drop" style="width: 62px; padding: 6px;"><span class="p-row" style="gap: 4px;"><span class="p-dot" style="background: var(--accent);"></span><span class="p-line" style="width: 28px;"></span></span><span class="p-line" style="width: 40px;"></span></div>',
  "blocks": [{
   "id": "notification-center", "title": "Notifications",
   "note": "Bell par click karein — unread badge aur mark-all-read dekhein.",
   "html": '''<div class="nc-wrap">
  <button class="nc-bell" type="button" id="ncBell" aria-expanded="false" aria-haspopup="dialog" aria-controls="ncPanel" aria-label="Notifications">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 8a6 6 0 0 0-12 0c0 7-3 7-3 9h18c0-2-3-2-3-9"/><path d="M10.3 21a2 2 0 0 0 3.4 0"/></svg>
    <span class="nc-badge" id="ncBadge">3</span>
  </button>
  <div class="nc-panel" id="ncPanel" role="dialog" aria-label="Notifications" hidden>
    <div class="nc-head">
      <span class="nc-title">Notifications</span>
      <button class="nc-mark" type="button" id="ncMark">Mark all read</button>
    </div>
    <ul class="nc-list" id="ncList">
      <li class="nc-item is-unread"><span class="nc-dot" aria-hidden="true"></span><div><p class="nc-t">New comment on your post</p><p class="nc-m">Ayesha replied 4 minutes ago.</p></div></li>
      <li class="nc-item is-unread"><span class="nc-dot" aria-hidden="true"></span><div><p class="nc-t">Invoice paid</p><p class="nc-m">Payment of $48.00 was received.</p></div></li>
      <li class="nc-item is-unread"><span class="nc-dot" aria-hidden="true"></span><div><p class="nc-t">Backup complete</p><p class="nc-m">All files were synced last night.</p></div></li>
      <li class="nc-item"><span class="nc-dot" aria-hidden="true"></span><div><p class="nc-t">Weekly report ready</p><p class="nc-m">Your analytics summary is available.</p></div></li>
    </ul>
    <a class="nc-all" href="#">View all notifications</a>
  </div>
</div>''',
   "css": '''.nc-wrap { position: relative; display: inline-block; }
.nc-bell {
  position: relative;
  width: 42px;
  height: 42px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  background: var(--card);
  color: var(--text);
  cursor: pointer;
}
.nc-bell svg { width: 19px; height: 19px; }
.nc-bell:hover { border-color: var(--accent); color: var(--accent); }
.nc-bell:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.nc-badge {
  position: absolute;
  top: -5px;
  right: -5px;
  min-width: 17px;
  height: 17px;
  padding: 0 4px;
  border-radius: 999px;
  background: var(--no);
  color: #fff;
  font-size: 0.66rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
}
.nc-badge.is-zero { display: none; }
.nc-panel {
  position: absolute;
  top: calc(100% + 8px);
  right: 0;
  width: 290px;
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  z-index: 30;
  overflow: hidden;
}
.nc-head { display: flex; align-items: center; justify-content: space-between; gap: 8px; padding: 10px 12px; border-bottom: 1px solid var(--border); }
.nc-title { font-size: 0.82rem; font-weight: 700; }
.nc-mark { border: 0; background: transparent; color: var(--accent); font: inherit; font-size: 0.72rem; font-weight: 700; cursor: pointer; padding: 2px 4px; border-radius: 3px; }
.nc-mark:hover { text-decoration: underline; }
.nc-mark:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.nc-list { list-style: none; margin: 0; padding: 4px; max-height: 240px; overflow: auto; }
.nc-item { display: flex; gap: 8px; padding: 8px; border-radius: 4px; }
.nc-item:hover { background: var(--bg); }
.nc-dot { width: 7px; height: 7px; border-radius: 999px; background: transparent; margin-top: 5px; flex: 0 0 auto; }
.nc-item.is-unread .nc-dot { background: var(--accent); }
.nc-t { margin: 0; font-size: 0.78rem; font-weight: 600; }
.nc-m { margin: 2px 0 0; font-size: 0.73rem; color: var(--muted); line-height: 1.4; }
.nc-all { display: block; text-align: center; padding: 9px; border-top: 1px solid var(--border); color: var(--accent); font-size: 0.75rem; font-weight: 700; text-decoration: none; }
.nc-all:hover { background: var(--bg); }
.nc-all:focus-visible { outline: 2px solid var(--accent); outline-offset: -2px; }''',
   "js": '''(function () {
  var bell = document.getElementById("ncBell");
  var panel = document.getElementById("ncPanel");
  var badge = document.getElementById("ncBadge");
  var list = document.getElementById("ncList");

  function countUnread() { return list.querySelectorAll(".is-unread").length; }

  function syncBadge() {
    var n = countUnread();
    badge.textContent = n;
    badge.classList.toggle("is-zero", n === 0);
  }

  function set(open) {
    panel.hidden = !open;
    bell.setAttribute("aria-expanded", String(open));
  }

  bell.addEventListener("click", function (e) {
    e.stopPropagation();
    set(panel.hidden);
  });

  document.addEventListener("click", function (e) {
    if (!panel.hidden && !panel.contains(e.target) && !bell.contains(e.target)) set(false);
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && !panel.hidden) { set(false); bell.focus(); }
  });

  document.getElementById("ncMark").addEventListener("click", function () {
    list.querySelectorAll(".is-unread").forEach(function (li) { li.classList.remove("is-unread"); });
    syncBadge();
  });

  list.querySelectorAll(".nc-item").forEach(function (li) {
    li.addEventListener("click", function () {
      li.classList.remove("is-unread");
      syncBadge();
    });
  });

  syncBadge();
})();''',
  }],
 },
]
