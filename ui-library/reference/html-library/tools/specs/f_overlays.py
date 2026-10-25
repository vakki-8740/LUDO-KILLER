CAT = "Overlays"
CAT_ID = "overlays"

PAGES = [
 {
  "folder": "overlays", "slug": "drawer", "title": "Drawer",
  "desc": "Slide-in side panel with overlay and left/right sides.",
  "idx_desc": "Slide-in side panel with left and right sides.",
  "mini": '<div class="p-page" style="height: 44px;"><span class="p-line" style="width: 20px;"></span><span style="margin-left: auto; width: 20px; background: var(--accent-soft); border-radius: 3px;"></span></div>',
  "blocks": [{
   "id": "drawer", "title": "Side drawer",
   "note": "Right ya Left button se drawer kholein. Escape se band hota hai.",
   "html": '''<div class="dr-demo">
  <div class="dr-btns">
    <button class="dr-open" type="button" data-side="right">Open right drawer</button>
    <button class="dr-open" type="button" data-side="left">Open left drawer</button>
  </div>
  <div class="dr-scrim" id="drScrim" hidden></div>
  <aside class="dr-panel" id="drPanel" role="dialog" aria-modal="true" aria-labelledby="drTitle" aria-hidden="true">
    <div class="dr-head">
      <span class="dr-title" id="drTitle">Filters</span>
      <button class="dr-x" type="button" id="drClose" aria-label="Close drawer">&times;</button>
    </div>
    <div class="dr-body">
      <label class="dr-lbl" for="drRange">Price range</label>
      <input class="dr-range" id="drRange" type="range" min="0" max="100" value="60">
      <p class="dr-note">Up to $600</p>
      <div class="dr-tags">
        <button class="dr-chip is-on" type="button">In stock</button>
        <button class="dr-chip" type="button">On sale</button>
        <button class="dr-chip" type="button">New</button>
      </div>
    </div>
    <div class="dr-foot">
      <button class="dr-reset" type="button">Reset</button>
      <button class="dr-apply" type="button" id="drApply">Apply</button>
    </div>
  </aside>
</div>''',
   "css": '''.dr-demo { position: relative; height: 300px; border: 1px dashed var(--border); border-radius: var(--radius); overflow: hidden; padding: 14px; }
.dr-btns { display: flex; gap: 8px; flex-wrap: wrap; }
.dr-open { border: 1px solid var(--border); background: var(--card); color: var(--text); font: inherit; font-size: 0.78rem; font-weight: 600; padding: 8px 12px; border-radius: var(--radius); cursor: pointer; }
.dr-open:hover { border-color: var(--accent); color: var(--accent); }
.dr-open:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.dr-scrim { position: absolute; inset: 0; background: rgba(10, 12, 18, 0.45); z-index: 10; }
.dr-panel {
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  width: min(240px, 78%);
  background: var(--card);
  border-left: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  z-index: 11;
  transform: translateX(105%);
  transition: transform 0.25s ease;
}
.dr-panel.is-left { right: auto; left: 0; border-left: 0; border-right: 1px solid var(--border); transform: translateX(-105%); }
.dr-panel.is-open { transform: translateX(0); }
.dr-head { display: flex; align-items: center; justify-content: space-between; padding: 10px 12px; border-bottom: 1px solid var(--border); }
.dr-title { font-size: 0.84rem; font-weight: 700; }
.dr-x { border: 0; background: transparent; color: var(--muted); font-size: 1.1rem; cursor: pointer; padding: 0 3px; border-radius: 3px; }
.dr-x:hover { color: var(--text); }
.dr-x:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.dr-body { flex: 1; padding: 12px; overflow: auto; }
.dr-lbl { display: block; font-size: 0.72rem; font-weight: 600; color: var(--muted); margin-bottom: 4px; }
.dr-range { width: 100%; accent-color: var(--accent); }
.dr-note { margin: 4px 0 12px; font-size: 0.7rem; color: var(--muted); }
.dr-tags { display: flex; gap: 5px; flex-wrap: wrap; }
.dr-chip { border: 1px solid var(--border); background: var(--bg); color: var(--text); font: inherit; font-size: 0.7rem; font-weight: 600; padding: 4px 9px; border-radius: 999px; cursor: pointer; }
.dr-chip.is-on { background: var(--accent-soft); border-color: var(--accent); color: var(--accent); }
.dr-chip:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.dr-foot { display: flex; gap: 7px; padding: 10px 12px; border-top: 1px solid var(--border); }
.dr-reset { flex: 1; border: 1px solid var(--border); background: transparent; color: var(--muted); font: inherit; font-size: 0.75rem; font-weight: 600; padding: 7px; border-radius: var(--radius); cursor: pointer; }
.dr-apply { flex: 1; border: 0; background: var(--accent); color: #fff; font: inherit; font-size: 0.75rem; font-weight: 600; padding: 7px; border-radius: var(--radius); cursor: pointer; }
.dr-reset:focus-visible, .dr-apply:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
@media (prefers-reduced-motion: reduce) { .dr-panel { transition: none; } }''',
   "js": '''(function () {
  var panel = document.getElementById("drPanel");
  var scrim = document.getElementById("drScrim");
  var close = document.getElementById("drClose");
  var last = null;

  function open(side, trigger) {
    panel.classList.remove("is-left");
    if (side === "left") panel.classList.add("is-left");
    panel.classList.add("is-open");
    panel.setAttribute("aria-hidden", "false");
    scrim.hidden = false;
    last = trigger;
    close.focus();
  }

  function hide() {
    panel.classList.remove("is-open");
    panel.setAttribute("aria-hidden", "true");
    scrim.hidden = true;
    if (last) last.focus();
  }

  document.querySelectorAll(".dr-open").forEach(function (b) {
    b.addEventListener("click", function () { open(b.getAttribute("data-side"), b); });
  });

  scrim.addEventListener("click", hide);
  close.addEventListener("click", hide);
  document.getElementById("drApply").addEventListener("click", hide);
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && panel.classList.contains("is-open")) hide();
  });
  document.querySelectorAll(".dr-chip").forEach(function (c) {
    c.addEventListener("click", function () { c.classList.toggle("is-on"); });
  });
})();''',
  }],
 },
 {
  "folder": "overlays", "slug": "bottom-sheet", "title": "Bottom Sheet",
  "desc": "Mobile-style sheet that slides up from the bottom.",
  "idx_desc": "Sheet sliding up from the bottom with actions.",
  "mini": '<div class="p-page" style="height: 44px;"><span class="p-line" style="width: 26px; margin: auto;"></span><span class="p-line" style="width: 40px; margin: auto;"></span></div>',
  "blocks": [{
   "id": "bottom-sheet", "title": "Action sheet",
   "note": "Share button se sheet khulegi.",
   "html": '''<div class="bs-demo">
  <div class="bs-page">
    <p class="bs-context">Article preview</p>
    <button class="bs-open" type="button" id="bsOpen">Share article</button>
  </div>
  <div class="bs-scrim" id="bsScrim" hidden></div>
  <div class="bs-sheet" id="bsSheet" role="dialog" aria-modal="true" aria-labelledby="bsTitle" aria-hidden="true">
    <span class="bs-grip" aria-hidden="true"></span>
    <p class="bs-title" id="bsTitle">Share article</p>
    <div class="bs-actions">
      <button class="bs-act" type="button"><span class="bs-ai" aria-hidden="true">WA</span>WhatsApp</button>
      <button class="bs-act" type="button"><span class="bs-ai" aria-hidden="true">X</span>Post on X</button>
      <button class="bs-act" type="button"><span class="bs-ai" aria-hidden="true">@</span>Email</button>
      <button class="bs-act" type="button"><span class="bs-ai" aria-hidden="true">&#128279;</span>Copy link</button>
    </div>
    <button class="bs-cancel" type="button" id="bsClose">Cancel</button>
  </div>
</div>''',
   "css": '''.bs-demo { position: relative; height: 320px; border: 1px dashed var(--border); border-radius: var(--radius); overflow: hidden; }
.bs-page { padding: 18px; }
.bs-context { margin: 0 0 10px; font-size: 0.8rem; color: var(--muted); }
.bs-open { border: 0; background: var(--accent); color: #fff; font: inherit; font-size: 0.8rem; font-weight: 600; padding: 9px 14px; border-radius: var(--radius); cursor: pointer; }
.bs-open:hover { opacity: 0.92; }
.bs-open:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.bs-scrim { position: absolute; inset: 0; background: rgba(10, 12, 18, 0.45); z-index: 10; }
.bs-sheet {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  background: var(--card);
  border-radius: 12px 12px 0 0;
  padding: 8px 14px 14px;
  z-index: 11;
  transform: translateY(105%);
  transition: transform 0.26s ease;
  box-shadow: 0 -8px 24px rgba(0, 0, 0, 0.14);
}
.bs-sheet.is-open { transform: translateY(0); }
.bs-grip { display: block; width: 36px; height: 4px; border-radius: 999px; background: var(--border); margin: 0 auto 10px; }
.bs-title { margin: 0 0 10px; font-size: 0.84rem; font-weight: 700; text-align: center; }
.bs-actions { display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px; }
.bs-act { display: flex; flex-direction: column; align-items: center; gap: 5px; border: 0; background: transparent; color: var(--text); font: inherit; font-size: 0.66rem; font-weight: 600; padding: 6px 2px; border-radius: var(--radius); cursor: pointer; }
.bs-act:hover { background: var(--bg); }
.bs-act:focus-visible { outline: 2px solid var(--accent); outline-offset: 1px; }
.bs-ai { width: 32px; height: 32px; border-radius: 999px; background: var(--accent-soft); color: var(--accent); display: flex; align-items: center; justify-content: center; font-size: 0.68rem; font-weight: 700; }
.bs-cancel { width: 100%; margin-top: 10px; border: 1px solid var(--border); background: transparent; color: var(--muted); font: inherit; font-size: 0.78rem; font-weight: 600; padding: 8px; border-radius: var(--radius); cursor: pointer; }
.bs-cancel:hover { border-color: var(--muted); }
.bs-cancel:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
@media (prefers-reduced-motion: reduce) { .bs-sheet { transition: none; } }''',
   "js": '''(function () {
  var sheet = document.getElementById("bsSheet");
  var scrim = document.getElementById("bsScrim");
  var openBtn = document.getElementById("bsOpen");
  var closeBtn = document.getElementById("bsClose");

  function set(open) {
    sheet.classList.toggle("is-open", open);
    sheet.setAttribute("aria-hidden", String(!open));
    scrim.hidden = !open;
    if (open) closeBtn.focus();
    else openBtn.focus();
  }

  openBtn.addEventListener("click", function () { set(true); });
  closeBtn.addEventListener("click", function () { set(false); });
  scrim.addEventListener("click", function () { set(false); });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && sheet.classList.contains("is-open")) set(false);
  });
})();''',
  }],
 },
 {
  "folder": "overlays", "slug": "popover", "title": "Popover",
  "desc": "Anchored popover card with close on outside click.",
  "idx_desc": "Anchored popover card with outside-click close.",
  "mini": '<div class="p-drop" style="width: 52px; padding: 5px;"><span class="p-line" style="width: 34px;"></span></div>',
  "blocks": [{
   "id": "popover", "title": "Filter popover",
   "html": '''<div class="po-wrap">
  <button class="po-trigger" type="button" id="poTrigger" aria-expanded="false" aria-haspopup="dialog" aria-controls="poPanel">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 6h16M7 12h10M10 18h4"/></svg>
    Filters
  </button>
  <div class="po-panel" id="poPanel" role="dialog" aria-label="Filters" hidden>
    <span class="po-arrow" aria-hidden="true"></span>
    <p class="po-title">Filter results</p>
    <label class="po-opt"><input class="po-check" type="checkbox" checked> <span class="po-text">Available now</span></label>
    <label class="po-opt"><input class="po-check" type="checkbox"> <span class="po-text">Free shipping</span></label>
    <label class="po-opt"><input class="po-check" type="checkbox"> <span class="po-text">Top rated</span></label>
    <div class="po-foot">
      <button class="po-clear" type="button" id="poClear">Clear</button>
      <button class="po-done" type="button" id="poDone">Apply</button>
    </div>
  </div>
</div>''',
   "css": '''.po-wrap { position: relative; display: inline-block; }
.po-trigger { display: inline-flex; align-items: center; gap: 6px; border: 1px solid var(--border); background: var(--card); color: var(--text); font: inherit; font-size: 0.8rem; font-weight: 600; padding: 8px 13px; border-radius: var(--radius); cursor: pointer; }
.po-trigger svg { width: 15px; height: 15px; color: var(--muted); }
.po-trigger:hover { border-color: var(--accent); color: var(--accent); }
.po-trigger:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.po-panel { position: absolute; top: calc(100% + 9px); left: 0; width: 210px; background: var(--card); border: 1px solid var(--border); border-radius: var(--radius); box-shadow: var(--shadow); padding: 10px; z-index: 20; }
.po-arrow { position: absolute; top: -5px; left: 20px; width: 9px; height: 9px; background: var(--card); border-left: 1px solid var(--border); border-top: 1px solid var(--border); transform: rotate(45deg); }
.po-title { margin: 0 0 7px; font-size: 0.74rem; font-weight: 700; color: var(--muted); text-transform: uppercase; letter-spacing: 0.05em; }
.po-opt { display: flex; align-items: center; gap: 7px; padding: 6px 6px; border-radius: 4px; font-size: 0.78rem; cursor: pointer; }
.po-opt:hover { background: var(--bg); }
.po-check { accent-color: var(--accent); width: 14px; height: 14px; }
.po-text { flex: 1; }
.po-foot { display: flex; gap: 6px; margin-top: 8px; padding-top: 8px; border-top: 1px solid var(--border); }
.po-clear { flex: 1; border: 1px solid var(--border); background: transparent; color: var(--muted); font: inherit; font-size: 0.72rem; font-weight: 600; padding: 6px; border-radius: 4px; cursor: pointer; }
.po-done { flex: 1; border: 0; background: var(--accent); color: #fff; font: inherit; font-size: 0.72rem; font-weight: 600; padding: 6px; border-radius: 4px; cursor: pointer; }
.po-clear:focus-visible, .po-done:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }''',
   "js": '''(function () {
  var trigger = document.getElementById("poTrigger");
  var panel = document.getElementById("poPanel");

  function set(open) {
    panel.hidden = !open;
    trigger.setAttribute("aria-expanded", String(open));
  }

  trigger.addEventListener("click", function (e) {
    e.stopPropagation();
    set(panel.hidden);
  });

  document.addEventListener("click", function (e) {
    if (!panel.hidden && !panel.contains(e.target) && e.target !== trigger) set(false);
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && !panel.hidden) { set(false); trigger.focus(); }
  });

  document.getElementById("poDone").addEventListener("click", function () { set(false); trigger.focus(); });
  document.getElementById("poClear").addEventListener("click", function () {
    document.querySelectorAll(".po-check").forEach(function (c) { c.checked = false; });
  });
})();''',
  }],
 },
 {
  "folder": "overlays", "slug": "context-menu", "title": "Context Menu",
  "desc": "Right-click menu positioned inside a demo surface.",
  "idx_desc": "Right-click or long-press style context menu.",
  "mini": '<div class="p-drop" style="width: 50px; padding: 5px;"><span class="p-line" style="width: 28px;"></span><span class="p-line" style="width: 34px;"></span></div>',
  "blocks": [{
   "id": "context-menu", "title": "Right-click area",
   "note": "Demo area par right-click karein, ya button se menu kholein.",
   "html": '''<div class="ct-demo" id="ctArea">
  <p class="ct-hint">Right-click anywhere in this area</p>
  <div class="ct-file">
    <span class="ct-ic" aria-hidden="true">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4"/></svg>
    </span>
    <span class="ct-name">project-brief.pdf</span>
  </div>
  <button class="ct-btn" type="button" id="ctBtn">Open menu</button>
  <div class="ct-menu" id="ctMenu" role="menu" aria-label="File actions" hidden>
    <button class="ct-item" type="button" role="menuitem">Open</button>
    <button class="ct-item" type="button" role="menuitem">Rename</button>
    <button class="ct-item" type="button" role="menuitem">Duplicate</button>
    <span class="ct-sep" aria-hidden="true"></span>
    <button class="ct-item ct-danger" type="button" role="menuitem">Delete</button>
  </div>
  <p class="ct-msg" id="ctMsg" aria-live="polite"></p>
</div>''',
   "css": '''.ct-demo { position: relative; height: 280px; border: 1px dashed var(--border); border-radius: var(--radius); padding: 14px; overflow: hidden; }
.ct-hint { margin: 0 0 10px; font-size: 0.74rem; color: var(--muted); }
.ct-file { display: inline-flex; align-items: center; gap: 8px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 8px 11px; }
.ct-ic { width: 22px; height: 26px; color: var(--accent); }
.ct-ic svg { width: 100%; height: 100%; }
.ct-name { font-size: 0.78rem; font-weight: 600; }
.ct-btn { display: block; margin-top: 10px; border: 1px solid var(--border); background: transparent; color: var(--accent); font: inherit; font-size: 0.74rem; font-weight: 600; padding: 6px 11px; border-radius: var(--radius); cursor: pointer; }
.ct-btn:hover { border-color: var(--accent); }
.ct-btn:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.ct-menu { position: absolute; width: 158px; background: var(--card); border: 1px solid var(--border); border-radius: var(--radius); box-shadow: var(--shadow); padding: 4px; z-index: 20; }
.ct-item { display: block; width: 100%; text-align: left; border: 0; background: transparent; color: var(--text); font: inherit; font-size: 0.78rem; padding: 7px 9px; border-radius: 4px; cursor: pointer; }
.ct-item:hover, .ct-item:focus-visible { background: var(--bg); outline: none; }
.ct-danger { color: var(--no); }
.ct-sep { display: block; height: 1px; background: var(--border); margin: 4px 2px; }
.ct-msg { position: absolute; left: 14px; bottom: 10px; margin: 0; font-size: 0.72rem; color: var(--yes); }''',
   "js": '''(function () {
  var area = document.getElementById("ctArea");
  var menu = document.getElementById("ctMenu");
  var btn = document.getElementById("ctBtn");
  var msg = document.getElementById("ctMsg");

  function open(x, y) {
    var rect = area.getBoundingClientRect();
    var w = menu.offsetWidth || 158;
    var h = menu.offsetHeight || 150;
    var left = Math.max(6, Math.min(x, rect.width - w - 6));
    var top = Math.max(6, Math.min(y, rect.height - h - 6));
    menu.style.left = left + "px";
    menu.style.top = top + "px";
    menu.hidden = false;
  }

  function hide() { menu.hidden = true; }

  area.addEventListener("contextmenu", function (e) {
    e.preventDefault();
    var rect = area.getBoundingClientRect();
    open(e.clientX - rect.left, e.clientY - rect.top);
  });

  btn.addEventListener("click", function (e) {
    e.stopPropagation();
    if (!menu.hidden) { hide(); return; }
    var rect = btn.getBoundingClientRect();
    var arect = area.getBoundingClientRect();
    var y = rect.bottom - arect.top + 6;
    var x = rect.left - arect.left;
    if (y + 150 > arect.height) y = rect.top - arect.top - 152;
    open(x, y);
  });

  menu.querySelectorAll(".ct-item").forEach(function (item) {
    item.addEventListener("click", function () {
      msg.textContent = item.textContent + " selected.";
      hide();
    });
  });

  document.addEventListener("click", function (e) {
    if (!menu.hidden && !menu.contains(e.target) && e.target !== btn) hide();
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && !menu.hidden) { hide(); btn.focus(); }
  });
})();''',
  }],
 },
 {
  "folder": "overlays", "slug": "command-palette", "title": "Command Palette",
  "desc": "Searchable command list with keyboard navigation.",
  "idx_desc": "Cmd+K style palette with fuzzy search.",
  "mini": '<div class="p-drop" style="width: 64px; padding: 6px;"><span class="p-line" style="width: 44px;"></span><span class="p-line" style="width: 32px;"></span></div>',
  "blocks": [{
   "id": "command-palette", "title": "Quick actions",
   "note": "Open dabaiye ya Ctrl/Cmd + K try karein.",
   "html": '''<div class="cp-demo">
  <div class="cp-hintbar">
    <span class="cp-shortcut">Ctrl / Cmd + K</span>
    <button class="cp-open" type="button" id="cpOpen">Open command palette</button>
  </div>
  <div class="cp-scrim" id="cpScrim" hidden></div>
  <div class="cp-box" id="cpBox" role="dialog" aria-modal="true" aria-label="Command palette" hidden>
    <div class="cp-searchrow">
      <svg class="cp-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>
      <input class="cp-input" id="cpInput" type="text" placeholder="Type a command..." aria-label="Search commands" autocomplete="off">
      <span class="cp-esc">Esc</span>
    </div>
    <ul class="cp-list" id="cpList" role="listbox" aria-label="Commands"></ul>
    <p class="cp-empty" id="cpEmpty" hidden>No matching commands.</p>
    <div class="cp-foot"><span>&#8593; &#8595; to navigate</span><span>&#8629; to select</span></div>
  </div>
</div>''',
   "css": '''.cp-demo { position: relative; height: 300px; border: 1px dashed var(--border); border-radius: var(--radius); padding: 14px; overflow: hidden; }
.cp-hintbar { display: flex; align-items: center; gap: 9px; flex-wrap: wrap; }
.cp-shortcut { font-size: 0.68rem; font-weight: 700; color: var(--muted); border: 1px solid var(--border); border-radius: 4px; padding: 2px 7px; }
.cp-open { border: 1px solid var(--border); background: var(--card); color: var(--text); font: inherit; font-size: 0.76rem; font-weight: 600; padding: 7px 11px; border-radius: var(--radius); cursor: pointer; }
.cp-open:hover { border-color: var(--accent); color: var(--accent); }
.cp-open:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.cp-scrim { position: absolute; inset: 0; background: rgba(10, 12, 18, 0.45); z-index: 10; }
.cp-box { position: absolute; top: 34px; left: 16px; right: 16px; max-width: 330px; margin: 0 auto; background: var(--card); border: 1px solid var(--border); border-radius: 8px; box-shadow: var(--shadow); z-index: 11; overflow: hidden; }
.cp-searchrow { display: flex; align-items: center; gap: 8px; padding: 10px 12px; border-bottom: 1px solid var(--border); }
.cp-ic { width: 16px; height: 16px; color: var(--muted); flex: 0 0 auto; }
.cp-input { flex: 1; min-width: 0; border: 0; background: transparent; color: var(--text); font: inherit; font-size: 0.84rem; outline: none; padding: 2px 0; }
.cp-esc { font-size: 0.62rem; font-weight: 700; color: var(--muted); border: 1px solid var(--border); border-radius: 3px; padding: 1px 5px; }
.cp-list { list-style: none; margin: 0; padding: 4px; max-height: 190px; overflow: auto; }
.cp-item { display: flex; align-items: center; gap: 8px; width: 100%; border: 0; background: transparent; color: var(--text); font: inherit; font-size: 0.79rem; text-align: left; padding: 8px 9px; border-radius: 4px; cursor: pointer; }
.cp-item:hover, .cp-item.is-active { background: var(--accent-soft); color: var(--accent); }
.cp-item:focus-visible { outline: 2px solid var(--accent); outline-offset: -2px; }
.cp-kbd { margin-left: auto; font-size: 0.62rem; color: var(--muted); border: 1px solid var(--border); border-radius: 3px; padding: 1px 4px; }
.cp-empty { margin: 0; padding: 14px; font-size: 0.76rem; color: var(--muted); text-align: center; }
.cp-foot { display: flex; justify-content: space-between; gap: 8px; padding: 7px 12px; border-top: 1px solid var(--border); font-size: 0.64rem; color: var(--muted); }
.cp-msg { margin: 8px 0 0; }''',
   "js": '''(function () {
  var box = document.getElementById("cpBox");
  var scrim = document.getElementById("cpScrim");
  var input = document.getElementById("cpInput");
  var list = document.getElementById("cpList");
  var empty = document.getElementById("cpEmpty");
  var openBtn = document.getElementById("cpOpen");
  var items = [
    ["New project", "P"], ["Open settings", "S"], ["Invite teammate", "I"],
    ["Export data", "E"], ["Toggle theme", "T"], ["View shortcuts", "?"]
  ];
  var active = 0;
  var shown = items.slice();

  function draw() {
    list.innerHTML = "";
    empty.hidden = shown.length > 0;
    shown.forEach(function (it, i) {
      var li = document.createElement("li");
      li.setAttribute("role", "option");
      var b = document.createElement("button");
      b.type = "button";
      b.className = "cp-item" + (i === active ? " is-active" : "");
      b.innerHTML = "<span>" + it[0] + "</span><span class=\\"cp-kbd\\">" + it[1] + "</span>";
      b.addEventListener("click", function () { pick(it[0]); });
      li.appendChild(b);
      list.appendChild(li);
    });
  }

  function pick(name) {
    hide();
    openBtn.textContent = name + " selected";
    setTimeout(function () { openBtn.textContent = "Open command palette"; }, 1800);
  }

  function filter(q) {
    shown = items.filter(function (it) { return it[0].toLowerCase().indexOf(q.toLowerCase()) > -1; });
    active = 0;
    draw();
  }

  function show() {
    box.hidden = false;
    scrim.hidden = false;
    input.value = "";
    filter("");
    input.focus();
  }

  function hide() {
    box.hidden = true;
    scrim.hidden = true;
    openBtn.focus();
  }

  openBtn.addEventListener("click", show);
  scrim.addEventListener("click", hide);
  input.addEventListener("input", function () { filter(input.value.trim()); });

  input.addEventListener("keydown", function (e) {
    if (e.key === "ArrowDown") { e.preventDefault(); active = Math.min(active + 1, shown.length - 1); draw(); }
    else if (e.key === "ArrowUp") { e.preventDefault(); active = Math.max(active - 1, 0); draw(); }
    else if (e.key === "Enter" && shown[active]) { e.preventDefault(); pick(shown[active][0]); }
    else if (e.key === "Escape") { hide(); }
  });

  document.addEventListener("keydown", function (e) {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") { e.preventDefault(); show(); }
  });
})();''',
  }],
 },
 {
  "folder": "overlays", "slug": "fullscreen-modal", "title": "Fullscreen Modal",
  "desc": "Immersive overlay that fills the demo surface.",
  "idx_desc": "Immersive overlay filling the demo surface.",
  "mini": '<div class="p-page" style="height: 44px;"><span class="p-line" style="width: 30px; margin: auto;"></span></div>',
  "blocks": [{
   "id": "fullscreen-modal", "title": "Immersive modal",
   "html": '''<div class="fm-demo">
  <div class="fm-base">
    <p class="fm-baseT">Media workspace</p>
    <p class="fm-baseD">Open the immersive editor to focus on one asset.</p>
    <button class="fm-open" type="button" id="fmOpen">Open immersive view</button>
  </div>
  <div class="fm-layer" id="fmLayer" role="dialog" aria-modal="true" aria-labelledby="fmTitle" hidden>
    <div class="fm-bar">
      <span class="fm-title" id="fmTitle">Editing: hero-banner.jpg</span>
      <button class="fm-close" type="button" id="fmClose" aria-label="Close immersive view">&times;</button>
    </div>
    <div class="fm-canvas">
      <div class="fm-art" aria-hidden="true">
        <span class="fm-shape fm-s1"></span>
        <span class="fm-shape fm-s2"></span>
        <span class="fm-shape fm-s3"></span>
      </div>
    </div>
    <div class="fm-tools">
      <button class="fm-tool is-on" type="button" aria-pressed="true">Crop</button>
      <button class="fm-tool" type="button" aria-pressed="false">Adjust</button>
      <button class="fm-tool" type="button" aria-pressed="false">Filter</button>
      <button class="fm-save" type="button">Save</button>
    </div>
  </div>
</div>''',
   "css": '''.fm-demo { position: relative; height: 330px; border: 1px dashed var(--border); border-radius: var(--radius); overflow: hidden; }
.fm-base { padding: 20px; }
.fm-baseT { margin: 0 0 4px; font-size: 0.95rem; font-weight: 700; }
.fm-baseD { margin: 0 0 12px; font-size: 0.78rem; color: var(--muted); max-width: 280px; line-height: 1.5; }
.fm-open { border: 0; background: var(--accent); color: #fff; font: inherit; font-size: 0.78rem; font-weight: 600; padding: 8px 13px; border-radius: var(--radius); cursor: pointer; }
.fm-open:hover { opacity: 0.92; }
.fm-open:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.fm-layer { position: absolute; inset: 0; background: var(--card); z-index: 20; display: flex; flex-direction: column; }
.fm-bar { display: flex; align-items: center; justify-content: space-between; gap: 8px; padding: 9px 12px; border-bottom: 1px solid var(--border); }
.fm-title { font-size: 0.76rem; font-weight: 700; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.fm-close { width: 26px; height: 26px; border: 0; border-radius: 999px; background: var(--bg); color: var(--muted); font-size: 1rem; cursor: pointer; line-height: 1; flex: 0 0 auto; }
.fm-close:hover { color: var(--text); }
.fm-close:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.fm-canvas { flex: 1; display: flex; align-items: center; justify-content: center; padding: 10px; background: var(--bg); overflow: hidden; }
.fm-art { position: relative; width: 100%; height: 100%; border-radius: var(--radius); background: linear-gradient(140deg, #1f2a4a, #4f6bed 60%, #8b5cf6); overflow: hidden; }
.fm-shape { position: absolute; border-radius: 999px; }
.fm-s1 { width: 90px; height: 90px; background: rgba(255, 255, 255, 0.16); top: 18%; left: 16%; }
.fm-s2 { width: 46px; height: 46px; background: rgba(255, 255, 255, 0.24); bottom: 22%; right: 20%; }
.fm-s3 { width: 130px; height: 130px; border: 2px solid rgba(255, 255, 255, 0.3); bottom: -40px; left: 34%; }
.fm-tools { display: flex; align-items: center; gap: 6px; padding: 8px 12px; border-top: 1px solid var(--border); flex-wrap: wrap; }
.fm-tool { border: 1px solid var(--border); background: transparent; color: var(--muted); font: inherit; font-size: 0.72rem; font-weight: 600; padding: 5px 10px; border-radius: 999px; cursor: pointer; }
.fm-tool.is-on { background: var(--accent-soft); border-color: var(--accent); color: var(--accent); }
.fm-tool:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.fm-save { margin-left: auto; border: 0; background: var(--accent); color: #fff; font: inherit; font-size: 0.72rem; font-weight: 600; padding: 6px 13px; border-radius: 4px; cursor: pointer; }
.fm-save:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }''',
   "js": '''(function () {
  var layer = document.getElementById("fmLayer");
  var openBtn = document.getElementById("fmOpen");
  var closeBtn = document.getElementById("fmClose");

  function set(open) {
    layer.hidden = !open;
    if (open) closeBtn.focus();
    else openBtn.focus();
  }

  openBtn.addEventListener("click", function () { set(true); });
  closeBtn.addEventListener("click", function () { set(false); });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && !layer.hidden) set(false);
  });

  document.querySelectorAll(".fm-tool").forEach(function (t) {
    t.addEventListener("click", function () {
      document.querySelectorAll(".fm-tool").forEach(function (x) {
        x.classList.remove("is-on");
        x.setAttribute("aria-pressed", "false");
      });
      t.classList.add("is-on");
      t.setAttribute("aria-pressed", "true");
    });
  });
})();''',
  }],
 },
 {
  "folder": "overlays", "slug": "image-zoom", "title": "Image Zoom",
  "desc": "Hover magnifier lens over a product image.",
  "idx_desc": "Hover magnifier lens over a product image.",
  "mini": '<div class="p-gal" style="grid-template-columns: 1fr;"><span style="height: 30px;"></span></div>',
  "blocks": [{
   "id": "image-zoom", "title": "Magnifier",
   "note": "Image par pointer move karein — lens follow karega.",
   "html": '''<div class="iz-wrap">
  <div class="iz-stage" id="izStage">
    <span class="iz-art" aria-hidden="true"></span>
    <span class="iz-lens" id="izLens" hidden></span>
    <span class="iz-badge">2x zoom</span>
  </div>
  <p class="iz-hint">Hover to inspect the texture</p>
</div>''',
   "css": '''.iz-wrap { max-width: 340px; }
.iz-stage { position: relative; height: 200px; border-radius: var(--radius); overflow: hidden; cursor: crosshair; border: 1px solid var(--border); }
.iz-art { position: absolute; inset: 0; background: radial-gradient(circle at 28% 32%, #a9b9ff 0 8%, transparent 9%), radial-gradient(circle at 70% 66%, #c8b4ff 0 11%, transparent 12%), linear-gradient(140deg, #1f2a4a, #4f6bed 58%, #8b5cf6); }
.iz-lens { position: absolute; width: 84px; height: 84px; border-radius: 999px; border: 2px solid #fff; box-shadow: 0 4px 14px rgba(0, 0, 0, 0.3); background-image: radial-gradient(circle at 28% 32%, #a9b9ff 0 8%, transparent 9%), radial-gradient(circle at 70% 66%, #c8b4ff 0 11%, transparent 12%), linear-gradient(140deg, #1f2a4a, #4f6bed 58%, #8b5cf6); background-size: 200% 200%; pointer-events: none; transform: translate(-50%, -50%); }
.iz-badge { position: absolute; top: 8px; left: 8px; font-size: 0.62rem; font-weight: 700; color: #fff; background: rgba(10, 12, 18, 0.45); border-radius: 999px; padding: 3px 8px; }
.iz-hint { margin: 7px 0 0; font-size: 0.72rem; color: var(--muted); }''',
   "js": '''(function () {
  var stage = document.getElementById("izStage");
  var lens = document.getElementById("izLens");

  stage.addEventListener("pointerenter", function () { lens.hidden = false; });
  stage.addEventListener("pointerleave", function () { lens.hidden = true; });
  stage.addEventListener("pointermove", function (e) {
    var r = stage.getBoundingClientRect();
    if (!r.width || !r.height) return;
    var x = e.clientX - r.left;
    var y = e.clientY - r.top;
    var px = Math.max(0, Math.min(100, (x / r.width) * 100));
    var py = Math.max(0, Math.min(100, (y / r.height) * 100));
    lens.style.left = x + "px";
    lens.style.top = y + "px";
    lens.style.backgroundPosition = px + "% " + py + "%";
  });
})();''',
  }],
 },
 {
  "folder": "overlays", "slug": "video-player", "title": "Video Player",
  "desc": "Custom player chrome with progress and mute toggle.",
  "idx_desc": "Custom player chrome with progress and mute.",
  "mini": '<div class="p-gal" style="grid-template-columns: 1fr;"><span style="height: 26px; display: flex; align-items: center; justify-content: center; color: white;">▶</span></div>',
  "blocks": [{
   "id": "video-player", "title": "Player controls",
   "html": '''<div class="vp-wrap">
  <div class="vp-stage" id="vpStage">
    <span class="vp-art" aria-hidden="true"></span>
    <button class="vp-big" type="button" id="vpBig" aria-label="Play video">
      <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>
    </button>
    <div class="vp-controls">
      <button class="vp-play" type="button" id="vpPlay" aria-label="Play">
        <svg id="vpIcon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>
      </button>
      <span class="vp-time" id="vpTime">0:00 / 2:34</span>
      <div class="vp-track" id="vpTrack" role="slider" tabindex="0" aria-label="Seek" aria-valuemin="0" aria-valuemax="154" aria-valuenow="0">
        <span class="vp-fill" id="vpFill"></span>
      </div>
      <button class="vp-mute" type="button" id="vpMute" aria-label="Mute">
        <svg id="vpMuteIcon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M11 5L6 9H3v6h3l5 4z"/><path d="M16 9a4 4 0 0 1 0 6"/><path d="M19 6a8 8 0 0 1 0 12"/></svg>
      </button>
    </div>
  </div>
</div>''',
   "css": '''.vp-wrap { max-width: 380px; }
.vp-stage { position: relative; height: 210px; border-radius: var(--radius); overflow: hidden; background: #12141a; }
.vp-art { position: absolute; inset: 0; background: radial-gradient(circle at 75% 20%, rgba(139, 92, 246, 0.6), transparent 42%), radial-gradient(circle at 22% 78%, rgba(14, 165, 233, 0.45), transparent 40%), linear-gradient(140deg, #1a1f33, #2a2350); }
.vp-big { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 48px; height: 48px; border-radius: 999px; border: 0; background: rgba(255, 255, 255, 0.92); color: #1f2430; display: flex; align-items: center; justify-content: center; cursor: pointer; transition: opacity 0.2s; }
.vp-big svg { width: 22px; height: 22px; margin-left: 2px; }
.vp-big:hover { background: #fff; }
.vp-big:focus-visible { outline: 2px solid #fff; outline-offset: 2px; }
.vp-stage.is-playing .vp-big { opacity: 0; pointer-events: none; }
.vp-controls { position: absolute; left: 0; right: 0; bottom: 0; display: flex; align-items: center; gap: 8px; padding: 8px 10px; background: linear-gradient(180deg, transparent, rgba(0, 0, 0, 0.68)); }
.vp-play, .vp-mute { border: 0; background: transparent; color: #fff; padding: 2px; cursor: pointer; display: flex; }
.vp-play svg, .vp-mute svg { width: 17px; height: 17px; }
.vp-play:focus-visible, .vp-mute:focus-visible { outline: 2px solid #fff; outline-offset: 2px; }
.vp-time { font-size: 0.64rem; color: rgba(255, 255, 255, 0.85); white-space: nowrap; font-variant-numeric: tabular-nums; }
.vp-track { flex: 1; height: 4px; border-radius: 999px; background: rgba(255, 255, 255, 0.25); cursor: pointer; min-width: 40px; }
.vp-track:focus-visible { outline: 2px solid #fff; outline-offset: 3px; }
.vp-fill { display: block; height: 100%; width: 0; border-radius: 999px; background: var(--accent); }
.vp-wrap.is-muted .vp-mute { color: var(--warn); }''',
   "js": '''(function () {
  var stage = document.getElementById("vpStage");
  var play = document.getElementById("vpPlay");
  var big = document.getElementById("vpBig");
  var icon = document.getElementById("vpIcon");
  var fill = document.getElementById("vpFill");
  var time = document.getElementById("vpTime");
  var track = document.getElementById("vpTrack");
  var total = 154;
  var pos = 0;
  var timer = null;

  function fmt(s) {
    var m = Math.floor(s / 60);
    var r = Math.floor(s % 60);
    return m + ":" + (r < 10 ? "0" : "") + r;
  }

  function paint() {
    fill.style.width = (pos / total) * 100 + "%";
    time.textContent = fmt(pos) + " / " + fmt(total);
    track.setAttribute("aria-valuenow", String(Math.round(pos)));
  }

  function setPlaying(on) {
    stage.classList.toggle("is-playing", on);
    play.setAttribute("aria-label", on ? "Pause" : "Play");
    icon.innerHTML = on
      ? '<path d="M7 5h4v14H7zM13 5h4v14h-4z"/>'
      : '<path d="M8 5v14l11-7z"/>';
    if (on) {
      if (pos >= total) pos = 0;
      timer = setInterval(function () {
        pos = Math.min(total, pos + 1);
        paint();
        if (pos >= total) { clearInterval(timer); timer = null; setPlaying(false); }
      }, 400);
    } else if (timer) {
      clearInterval(timer);
      timer = null;
    }
  }

  play.addEventListener("click", function () { setPlaying(!timer); });
  big.addEventListener("click", function () { setPlaying(true); });

  function seek(x) {
    var r = track.getBoundingClientRect();
    if (!r.width) return;
    pos = Math.max(0, Math.min(total, ((x - r.left) / r.width) * total));
    paint();
  }

  track.addEventListener("click", function (e) { seek(e.clientX); });
  track.addEventListener("keydown", function (e) {
    if (e.key === "ArrowRight") { e.preventDefault(); pos = Math.min(total, pos + 5); paint(); }
    if (e.key === "ArrowLeft") { e.preventDefault(); pos = Math.max(0, pos - 5); paint(); }
  });

  document.getElementById("vpMute").addEventListener("click", function () {
    var muted = this.parentNode.parentNode.parentNode.classList.toggle("is-muted");
    this.setAttribute("aria-label", muted ? "Unmute" : "Mute");
    document.getElementById("vpMuteIcon").innerHTML = muted
      ? '<path d="M11 5L6 9H3v6h3l5 4z"/><path d="M22 9l-6 6M16 9l6 6"/>'
      : '<path d="M11 5L6 9H3v6h3l5 4z"/><path d="M16 9a4 4 0 0 1 0 6"/><path d="M19 6a8 8 0 0 1 0 12"/>';
  });

  stage.classList.add("vp-wrap");
  paint();
})();''',
  }],
 },
 {
  "folder": "overlays", "slug": "dropdown-menu", "title": "Dropdown Menu",
  "desc": "Keyboard-friendly menu with groups and selection.",
  "idx_desc": "Keyboard-friendly dropdown with selectable items.",
  "mini": '<div class="p-drop" style="width: 54px; padding: 5px;"><span class="p-line" style="width: 36px;"></span><span class="p-line" style="width: 26px;"></span></div>',
  "blocks": [{
   "id": "dropdown-menu", "title": "Account menu",
   "html": '''<div class="dd-wrap">
  <button class="dd-trigger" type="button" id="ddTrigger" aria-expanded="false" aria-haspopup="menu" aria-controls="ddMenu">
    <span class="dd-av" aria-hidden="true">AK</span>
    <span class="dd-meta"><span class="dd-name">Ayesha Khan</span><span class="dd-role">Product designer</span></span>
    <svg class="dd-caret" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
  </button>
  <div class="dd-menu" id="ddMenu" role="menu" aria-labelledby="ddTrigger" hidden>
    <span class="dd-group" role="presentation">Account</span>
    <button class="dd-item is-sel" type="button" role="menuitemradio" aria-checked="true"><span class="dd-dot" aria-hidden="true"></span>Profile</button>
    <button class="dd-item" type="button" role="menuitemradio" aria-checked="false"><span class="dd-dot" aria-hidden="true"></span>Preferences</button>
    <span class="dd-sep" role="separator"></span>
    <span class="dd-group" role="presentation">Team</span>
    <button class="dd-item" type="button" role="menuitem">Invite member</button>
    <button class="dd-item" type="button" role="menuitem">Manage billing</button>
    <span class="dd-sep" role="separator"></span>
    <button class="dd-item dd-danger" type="button" role="menuitem">Sign out</button>
  </div>
</div>''',
   "css": '''.dd-wrap { position: relative; display: inline-block; }
.dd-trigger { display: flex; align-items: center; gap: 8px; border: 1px solid var(--border); background: var(--card); padding: 6px 10px; border-radius: var(--radius); cursor: pointer; font: inherit; color: var(--text); }
.dd-trigger:hover { border-color: var(--accent); }
.dd-trigger:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.dd-av { width: 28px; height: 28px; border-radius: 999px; background: linear-gradient(135deg, #4f6bed, #8b5cf6); color: #fff; font-size: 0.64rem; font-weight: 700; display: flex; align-items: center; justify-content: center; flex: 0 0 auto; }
.dd-meta { display: flex; flex-direction: column; text-align: left; }
.dd-name { font-size: 0.76rem; font-weight: 700; line-height: 1.2; }
.dd-role { font-size: 0.62rem; color: var(--muted); }
.dd-caret { width: 14px; height: 14px; color: var(--muted); }
.dd-menu { position: absolute; top: calc(100% + 7px); left: 0; width: 200px; background: var(--card); border: 1px solid var(--border); border-radius: var(--radius); box-shadow: var(--shadow); padding: 5px; z-index: 20; }
.dd-group { display: block; padding: 5px 8px 3px; font-size: 0.62rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.07em; color: var(--muted); }
.dd-item { display: flex; align-items: center; gap: 7px; width: 100%; border: 0; background: transparent; color: var(--text); font: inherit; font-size: 0.78rem; text-align: left; padding: 7px 8px; border-radius: 4px; cursor: pointer; }
.dd-item:hover, .dd-item:focus-visible { background: var(--bg); outline: none; }
.dd-item.is-sel { color: var(--accent); font-weight: 600; }
.dd-dot { width: 6px; height: 6px; border-radius: 999px; background: transparent; }
.dd-item.is-sel .dd-dot { background: var(--accent); }
.dd-sep { display: block; height: 1px; background: var(--border); margin: 4px 2px; }
.dd-danger { color: var(--no); }''',
   "js": '''(function () {
  var trigger = document.getElementById("ddTrigger");
  var menu = document.getElementById("ddMenu");
  var items = Array.prototype.slice.call(menu.querySelectorAll(".dd-item"));

  function set(open) {
    menu.hidden = !open;
    trigger.setAttribute("aria-expanded", String(open));
    if (open && items[0]) items[0].focus();
  }

  trigger.addEventListener("click", function (e) {
    e.stopPropagation();
    set(menu.hidden);
  });

  trigger.addEventListener("keydown", function (e) {
    if (e.key === "ArrowDown") { e.preventDefault(); set(true); }
  });

  items.forEach(function (it, i) {
    it.addEventListener("click", function () {
      if (it.getAttribute("role") === "menuitemradio") {
        items.forEach(function (x) {
          if (x.getAttribute("role") === "menuitemradio") {
            x.classList.remove("is-sel");
            x.setAttribute("aria-checked", "false");
          }
        });
        it.classList.add("is-sel");
        it.setAttribute("aria-checked", "true");
      }
      set(false);
      trigger.focus();
    });
    it.addEventListener("keydown", function (e) {
      if (e.key === "ArrowDown") { e.preventDefault(); items[(i + 1) % items.length].focus(); }
      if (e.key === "ArrowUp") { e.preventDefault(); items[(i - 1 + items.length) % items.length].focus(); }
      if (e.key === "Escape") { set(false); trigger.focus(); }
    });
  });

  document.addEventListener("click", function (e) {
    if (!menu.hidden && !menu.contains(e.target) && !trigger.contains(e.target)) set(false);
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && !menu.hidden) { set(false); trigger.focus(); }
  });
})();''',
  }],
 },
]
