CAT = "Buttons & Actions"
CAT_ID = "interactive"

PAGES = [
 {
  "folder": "buttons", "slug": "gradient", "title": "Gradient Buttons",
  "desc": "Accent gradients, soft gradient, multi-stop and shine hover.",
  "idx_desc": "Four gradient button styles with hover shine.",
  "mini": '<div class="p-row" style="gap: 6px;"><span class="p-btn accent" style="width: 38px; background: linear-gradient(135deg, #4f6bed, #8b5cf6);"></span><span class="p-btn" style="width: 38px; background: linear-gradient(135deg, #22a06b, #0ea5e9);"></span></div>',
  "blocks": [{
   "id": "gradient-buttons", "title": "Gradient button set",
   "html": '''<div class="gr-set">
  <button class="gr-btn gr-primary" type="button">Get started</button>
  <button class="gr-btn gr-soft" type="button">Soft gradient</button>
  <button class="gr-btn gr-green" type="button">Upgrade plan</button>
  <button class="gr-btn gr-shine" type="button">Shine on hover</button>
</div>
<div class="gr-sizes">
  <button class="gr-btn gr-primary gr-sm" type="button">Small</button>
  <button class="gr-btn gr-primary" type="button">Medium</button>
  <button class="gr-btn gr-primary gr-lg" type="button">Large</button>
</div>
<button class="gr-btn gr-primary gr-full" type="button">Continue to dashboard</button>''',
   "css": '''.gr-set { display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 14px; }
.gr-sizes { display: flex; gap: 10px; flex-wrap: wrap; align-items: center; margin-bottom: 14px; }
.gr-btn {
  position: relative;
  overflow: hidden;
  border: 0;
  border-radius: var(--radius);
  color: #fff;
  font: inherit;
  font-size: 0.9rem;
  font-weight: 600;
  padding: 10px 18px;
  cursor: pointer;
  transition: transform 0.15s, opacity 0.2s;
}
.gr-btn:hover { transform: translateY(-2px); opacity: 0.94; }
.gr-btn:active { transform: translateY(0); }
.gr-btn:focus-visible { outline: 2px solid var(--accent); outline-offset: 3px; }
.gr-primary { background: linear-gradient(135deg, #4f6bed, #8b5cf6); }
.gr-soft { background: var(--accent-soft); color: var(--accent); border: 1px solid rgba(79, 107, 237, 0.35); }
.gr-green { background: linear-gradient(135deg, #22a06b, #0ea5e9); }
.gr-shine::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(110deg, transparent 30%, rgba(255, 255, 255, 0.45) 50%, transparent 70%);
  transform: translateX(-120%);
  transition: transform 0.6s;
}
.gr-shine:hover::after { transform: translateX(120%); }
.gr-sm { font-size: 0.78rem; padding: 7px 13px; }
.gr-lg { font-size: 1rem; padding: 13px 24px; }
.gr-full { display: block; width: 100%; }
@media (prefers-reduced-motion: reduce) {
  .gr-btn, .gr-shine::after { transition: none; }
  .gr-btn:hover { transform: none; }
}''',
  }],
 },
 {
  "folder": "buttons", "slug": "button-groups", "title": "Button Groups",
  "desc": "Segmented controls, icon toolbars and vertical groups.",
  "idx_desc": "Segmented, toolbar and vertical grouped buttons.",
  "mini": '<div class="p-row-tight"><span class="p-btn accent" style="width: 26px;"></span><span class="p-btn" style="width: 26px;"></span><span class="p-btn" style="width: 26px;"></span></div>',
  "blocks": [{
   "id": "button-groups", "title": "Grouped controls",
   "html": '''<div class="bg-block">
  <p class="bg-lb">Segmented</p>
  <div class="bg-seg" role="group" aria-label="Range">
    <button class="bg-sbtn is-on" type="button" aria-pressed="true">Day</button>
    <button class="bg-sbtn" type="button" aria-pressed="false">Week</button>
    <button class="bg-sbtn" type="button" aria-pressed="false">Month</button>
  </div>
</div>
<div class="bg-block">
  <p class="bg-lb">Toolbar</p>
  <div class="bg-tool" role="toolbar" aria-label="Formatting">
    <button class="bg-ico" type="button" aria-label="Bold"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M7 4h6a4 4 0 0 1 0 8H7zM7 12h7a4 4 0 0 1 0 8H7z"/></svg></button>
    <button class="bg-ico" type="button" aria-label="Italic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M10 4h8M6 20h8M14 4l-4 16"/></svg></button>
    <button class="bg-ico" type="button" aria-label="Underline"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M7 4v7a5 5 0 0 0 10 0V4M5 21h14"/></svg></button>
    <span class="bg-div" aria-hidden="true"></span>
    <button class="bg-ico" type="button" aria-label="Link"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M10 14a5 5 0 0 0 7 0l2-2a5 5 0 0 0-7-7l-1 1"/><path d="M14 10a5 5 0 0 0-7 0l-2 2a5 5 0 0 0 7 7l1-1"/></svg></button>
  </div>
</div>
<div class="bg-block">
  <p class="bg-lb">Vertical</p>
  <div class="bg-vert" role="group" aria-label="View">
    <button class="bg-vbtn is-on" type="button" aria-pressed="true">Grid view</button>
    <button class="bg-vbtn" type="button" aria-pressed="false">List view</button>
    <button class="bg-vbtn" type="button" aria-pressed="false">Board view</button>
  </div>
</div>''',
   "css": '''.bg-block { margin-bottom: 18px; }
.bg-lb { margin: 0 0 8px; font-size: 0.7rem; font-weight: 700; letter-spacing: 0.07em; text-transform: uppercase; color: var(--muted); }
.bg-seg { display: inline-flex; border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; }
.bg-sbtn {
  border: 0;
  background: var(--card);
  color: var(--text);
  font: inherit;
  font-size: 0.83rem;
  font-weight: 600;
  padding: 8px 16px;
  cursor: pointer;
}
.bg-sbtn + .bg-sbtn { border-left: 1px solid var(--border); }
.bg-sbtn:hover { color: var(--accent); }
.bg-sbtn.is-on { background: var(--accent); color: #fff; }
.bg-sbtn:focus-visible { outline: 2px solid var(--accent); outline-offset: -2px; }
.bg-tool { display: inline-flex; align-items: center; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); }
.bg-ico {
  border: 0;
  background: transparent;
  color: var(--muted);
  padding: 8px 10px;
  cursor: pointer;
  display: flex;
  align-items: center;
}
.bg-ico svg { width: 17px; height: 17px; }
.bg-ico:hover { color: var(--accent); background: var(--bg); }
.bg-ico:focus-visible { outline: 2px solid var(--accent); outline-offset: -2px; }
.bg-div { width: 1px; height: 20px; background: var(--border); }
.bg-vert { display: inline-flex; flex-direction: column; border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; min-width: 150px; }
.bg-vbtn {
  border: 0;
  background: var(--card);
  color: var(--text);
  font: inherit;
  font-size: 0.83rem;
  font-weight: 600;
  text-align: left;
  padding: 10px 14px;
  cursor: pointer;
}
.bg-vbtn + .bg-vbtn { border-top: 1px solid var(--border); }
.bg-vbtn:hover { color: var(--accent); }
.bg-vbtn.is-on { background: var(--accent-soft); color: var(--accent); }
.bg-vbtn:focus-visible { outline: 2px solid var(--accent); outline-offset: -2px; }''',
   "js": '''document.querySelectorAll(".bg-seg").forEach(function (g) {
  var b = Array.prototype.slice.call(g.querySelectorAll(".bg-sbtn"));
  b.forEach(function (x) {
    x.addEventListener("click", function () {
      b.forEach(function (y) { y.classList.remove("is-on"); y.setAttribute("aria-pressed", "false"); });
      x.classList.add("is-on");
      x.setAttribute("aria-pressed", "true");
    });
  });
});
document.querySelectorAll(".bg-vert").forEach(function (g) {
  var b = Array.prototype.slice.call(g.querySelectorAll(".bg-vbtn"));
  b.forEach(function (x) {
    x.addEventListener("click", function () {
      b.forEach(function (y) { y.classList.remove("is-on"); y.setAttribute("aria-pressed", "false"); });
      x.classList.add("is-on");
      x.setAttribute("aria-pressed", "true");
    });
  });
});''',
  }],
 },
 {
  "folder": "buttons", "slug": "split-button", "title": "Split Button",
  "desc": "Primary action with an attached dropdown menu.",
  "idx_desc": "Primary action plus attached action menu.",
  "mini": '<div class="p-row-tight"><span class="p-btn accent" style="width: 40px;"></span><span class="p-btn accent" style="width: 16px;"></span></div>',
  "blocks": [{
   "id": "split-button", "title": "Split button",
   "html": '''<div class="sp-wrap">
  <div class="sp-group">
    <button class="sp-main" type="button">Publish</button>
    <button class="sp-arrow" type="button" id="spToggle" aria-expanded="false" aria-haspopup="menu" aria-controls="spMenu" aria-label="More publish options">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
    </button>
    <div class="sp-menu" id="spMenu" role="menu" aria-labelledby="spToggle" hidden>
      <button class="sp-item" type="button" role="menuitem">Publish and copy link</button>
      <button class="sp-item" type="button" role="menuitem">Schedule for later</button>
      <button class="sp-item" type="button" role="menuitem">Save as draft</button>
      <button class="sp-item sp-danger" type="button" role="menuitem">Discard changes</button>
    </div>
  </div>
  <div class="sp-group sp-outline">
    <button class="sp-main" type="button">Preview</button>
    <button class="sp-arrow" type="button" aria-label="Preview options">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
    </button>
  </div>
  <p class="sp-msg" id="spMsg" aria-live="polite"></p>
</div>''',
   "css": '''.sp-wrap { display: flex; align-items: center; gap: 10px; flex-wrap: wrap; }
.sp-group { position: relative; display: inline-flex; }
.sp-main {
  border: 1px solid var(--accent);
  border-right: 0;
  background: var(--accent);
  color: #fff;
  font: inherit;
  font-size: 0.86rem;
  font-weight: 600;
  padding: 9px 16px;
  border-radius: var(--radius) 0 0 var(--radius);
  cursor: pointer;
}
.sp-arrow {
  border: 1px solid var(--accent);
  background: var(--accent);
  color: #fff;
  padding: 0 9px;
  border-radius: 0 var(--radius) var(--radius) 0;
  cursor: pointer;
  display: flex;
  align-items: center;
}
.sp-arrow svg { width: 15px; height: 15px; }
.sp-main:hover, .sp-arrow:hover { opacity: 0.92; }
.sp-main:focus-visible, .sp-arrow:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.sp-outline .sp-main { background: var(--card); border-color: var(--border); color: var(--text); }
.sp-outline .sp-arrow { background: var(--card); border-color: var(--border); color: var(--text); }
.sp-outline .sp-main:hover, .sp-outline .sp-arrow:hover { border-color: var(--accent); color: var(--accent); opacity: 1; }
.sp-menu {
  position: absolute;
  top: calc(100% + 6px);
  right: 0;
  min-width: 210px;
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: 5px;
  z-index: 20;
}
.sp-item {
  display: block;
  width: 100%;
  text-align: left;
  border: 0;
  background: transparent;
  color: var(--text);
  font: inherit;
  font-size: 0.82rem;
  padding: 8px 10px;
  border-radius: 4px;
  cursor: pointer;
}
.sp-item:hover, .sp-item:focus-visible { background: var(--bg); outline: none; }
.sp-danger { color: var(--no); }
.sp-msg { width: 100%; margin: 6px 0 0; font-size: 0.78rem; color: var(--yes); min-height: 1.1em; }''',
   "js": '''(function () {
  var toggle = document.getElementById("spToggle");
  var menu = document.getElementById("spMenu");
  var msg = document.getElementById("spMsg");

  function set(open) {
    menu.hidden = !open;
    toggle.setAttribute("aria-expanded", String(open));
  }

  toggle.addEventListener("click", function (e) {
    e.stopPropagation();
    set(menu.hidden);
  });

  menu.querySelectorAll(".sp-item").forEach(function (item) {
    item.addEventListener("click", function () {
      msg.textContent = item.textContent + " selected.";
      set(false);
      toggle.focus();
    });
  });

  document.addEventListener("click", function (e) {
    if (!menu.hidden && !menu.contains(e.target) && e.target !== toggle) set(false);
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && !menu.hidden) { set(false); toggle.focus(); }
  });
})();''',
  }],
 },
 {
  "folder": "buttons", "slug": "social-login", "title": "Social Login Buttons",
  "desc": "Google, GitHub and Microsoft sign-in buttons.",
  "idx_desc": "Google, GitHub and Microsoft sign-in buttons.",
  "mini": '<div class="p-row" style="gap: 5px;"><span class="p-btn" style="width: 22px;"></span><span class="p-btn" style="width: 22px; background: #1f2430;"></span><span class="p-btn" style="width: 22px;"></span></div>',
  "blocks": [{
   "id": "social-login", "title": "Social sign-in",
   "html": '''<div class="so-stack">
  <button class="so-btn" type="button">
    <svg class="so-ic" viewBox="0 0 24 24" aria-hidden="true"><path fill="#4285F4" d="M21.6 12.2c0-.7-.1-1.4-.2-2H12v3.9h5.4a4.6 4.6 0 0 1-2 3v2.5h3.2c1.9-1.7 3-4.3 3-7.4z"/><path fill="#34A853" d="M12 22c2.7 0 5-1 6.6-2.5l-3.2-2.5c-.9.6-2 1-3.4 1-2.6 0-4.8-1.8-5.6-4.1H3.1v2.6A10 10 0 0 0 12 22z"/><path fill="#FBBC05" d="M6.4 13.9a6 6 0 0 1 0-3.8V7.5H3.1a10 10 0 0 0 0 9l3.3-2.6z"/><path fill="#EA4335" d="M12 5.9c1.5 0 2.8.5 3.8 1.5l2.8-2.8A10 10 0 0 0 3.1 7.5l3.3 2.6C7.2 7.8 9.4 5.9 12 5.9z"/></svg>
    Continue with Google
  </button>
  <button class="so-btn so-dark" type="button">
    <svg class="so-ic" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2C6.5 2 2 6.6 2 12.3c0 4.5 2.9 8.4 6.8 9.7.5.1.7-.2.7-.5v-1.7c-2.8.6-3.4-1.4-3.4-1.4-.5-1.2-1.1-1.5-1.1-1.5-.9-.6.1-.6.1-.6 1 .1 1.5 1 1.5 1 .9 1.6 2.4 1.1 3 .9.1-.7.4-1.1.6-1.4-2.2-.3-4.6-1.1-4.6-5.1 0-1.1.4-2 1-2.7-.1-.3-.4-1.3.1-2.7 0 0 .8-.3 2.7 1a9 9 0 0 1 5 0c1.9-1.3 2.7-1 2.7-1 .5 1.4.2 2.4.1 2.7.6.7 1 1.6 1 2.7 0 4-2.4 4.8-4.6 5.1.4.3.7.9.7 1.9v2.8c0 .3.2.6.7.5A10.3 10.3 0 0 0 22 12.3C22 6.6 17.5 2 12 2z"/></svg>
    Continue with GitHub
  </button>
  <button class="so-btn" type="button">
    <svg class="so-ic" viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="8" height="8" fill="#F25022"/><rect x="13" y="3" width="8" height="8" fill="#7FBA00"/><rect x="3" y="13" width="8" height="8" fill="#00A4EF"/><rect x="13" y="13" width="8" height="8" fill="#FFB900"/></svg>
    Continue with Microsoft
  </button>
</div>
<p class="so-or"><span>or sign in with email</span></p>
<div class="so-row">
  <button class="so-mini" type="button" aria-label="Sign in with Google">
    <svg class="so-ic" viewBox="0 0 24 24" aria-hidden="true"><path fill="#4285F4" d="M21.6 12.2c0-.7-.1-1.4-.2-2H12v3.9h5.4a4.6 4.6 0 0 1-2 3v2.5h3.2c1.9-1.7 3-4.3 3-7.4z"/><path fill="#34A853" d="M12 22c2.7 0 5-1 6.6-2.5l-3.2-2.5c-.9.6-2 1-3.4 1-2.6 0-4.8-1.8-5.6-4.1H3.1v2.6A10 10 0 0 0 12 22z"/><path fill="#FBBC05" d="M6.4 13.9a6 6 0 0 1 0-3.8V7.5H3.1a10 10 0 0 0 0 9l3.3-2.6z"/><path fill="#EA4335" d="M12 5.9c1.5 0 2.8.5 3.8 1.5l2.8-2.8A10 10 0 0 0 3.1 7.5l3.3 2.6C7.2 7.8 9.4 5.9 12 5.9z"/></svg>
  </button>
  <button class="so-mini" type="button" aria-label="Sign in with GitHub">
    <svg class="so-ic" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2C6.5 2 2 6.6 2 12.3c0 4.5 2.9 8.4 6.8 9.7.5.1.7-.2.7-.5v-1.7c-2.8.6-3.4-1.4-3.4-1.4-.5-1.2-1.1-1.5-1.1-1.5-.9-.6.1-.6.1-.6 1 .1 1.5 1 1.5 1 .9 1.6 2.4 1.1 3 .9.1-.7.4-1.1.6-1.4-2.2-.3-4.6-1.1-4.6-5.1 0-1.1.4-2 1-2.7-.1-.3-.4-1.3.1-2.7 0 0 .8-.3 2.7 1a9 9 0 0 1 5 0c1.9-1.3 2.7-1 2.7-1 .5 1.4.2 2.4.1 2.7.6.7 1 1.6 1 2.7 0 4-2.4 4.8-4.6 5.1.4.3.7.9.7 1.9v2.8c0 .3.2.6.7.5A10.3 10.3 0 0 0 22 12.3C22 6.6 17.5 2 12 2z"/></svg>
  </button>
  <button class="so-mini" type="button" aria-label="Sign in with Microsoft">
    <svg class="so-ic" viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="8" height="8" fill="#F25022"/><rect x="13" y="3" width="8" height="8" fill="#7FBA00"/><rect x="3" y="13" width="8" height="8" fill="#00A4EF"/><rect x="13" y="13" width="8" height="8" fill="#FFB900"/></svg>
  </button>
</div>''',
   "css": '''.so-stack { display: flex; flex-direction: column; gap: 10px; max-width: 360px; }
.so-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  height: 42px;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  background: var(--card);
  color: var(--text);
  font: inherit;
  font-size: 0.87rem;
  font-weight: 600;
  cursor: pointer;
  transition: border-color 0.2s, transform 0.15s;
}
.so-btn:hover { border-color: var(--accent); transform: translateY(-1px); }
.so-btn:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.so-ic { width: 18px; height: 18px; flex: 0 0 auto; }
.so-dark { background: #1f2430; border-color: #1f2430; color: #fff; }
.so-dark:hover { border-color: #1f2430; opacity: 0.92; }
.so-or { display: flex; align-items: center; gap: 10px; max-width: 360px; margin: 16px 0; color: var(--muted); font-size: 0.74rem; }
.so-or::before, .so-or::after { content: ""; flex: 1; height: 1px; background: var(--border); }
.so-row { display: flex; gap: 10px; }
.so-mini {
  flex: 1;
  height: 42px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  background: var(--card);
  cursor: pointer;
}
.so-mini:hover { border-color: var(--accent); }
.so-mini:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }''',
  }],
 },
 {
  "folder": "buttons", "slug": "copy-button", "title": "Copy Button",
  "desc": "Copy-to-clipboard buttons with success feedback.",
  "idx_desc": "Clipboard buttons with copied feedback.",
  "mini": '<div class="p-row" style="gap: 6px;"><span class="p-btn accent" style="width: 44px;"></span><span class="p-line" style="width: 40px;"></span></div>',
  "blocks": [{
   "id": "copy-button", "title": "Copy actions",
   "html": '''<div class="cp-row">
  <button class="cp-btn" type="button" id="cpMain">Copy install command</button>
  <span class="cp-status" id="cpStatus" aria-live="polite"></span>
</div>
<div class="cp-line">
  <code class="cp-code" id="cpCode">npm i own-library</code>
  <button class="cp-ghost" type="button" id="cpIcon" aria-label="Copy code">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15V5a2 2 0 0 1 2-2h10"/></svg>
  </button>
</div>
<div class="cp-row">
  <button class="cp-link" type="button" id="cpLink">Copy share link</button>
</div>''',
   "css": '''.cp-row { display: flex; align-items: center; gap: 10px; flex-wrap: wrap; margin-bottom: 12px; }
.cp-btn {
  border: 0;
  background: var(--accent);
  color: #fff;
  font: inherit;
  font-size: 0.86rem;
  font-weight: 600;
  padding: 9px 16px;
  border-radius: var(--radius);
  cursor: pointer;
}
.cp-btn:hover { opacity: 0.92; }
.cp-btn:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.cp-status { font-size: 0.78rem; color: var(--yes); min-height: 1.1em; }
.cp-line { display: flex; align-items: center; gap: 8px; background: var(--bg); border: 1px solid var(--border); border-radius: var(--radius); padding: 8px 10px 8px 12px; margin-bottom: 12px; max-width: 340px; }
.cp-code { flex: 1; font-family: ui-monospace, Menlo, Consolas, monospace; font-size: 0.8rem; color: var(--text); overflow-x: auto; white-space: nowrap; }
.cp-ghost {
  border: 0;
  background: transparent;
  color: var(--muted);
  padding: 4px;
  border-radius: 4px;
  cursor: pointer;
  display: flex;
}
.cp-ghost svg { width: 16px; height: 16px; }
.cp-ghost:hover { color: var(--accent); }
.cp-ghost:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.cp-link {
  border: 1px solid var(--border);
  background: transparent;
  color: var(--accent);
  font: inherit;
  font-size: 0.82rem;
  font-weight: 600;
  padding: 8px 14px;
  border-radius: var(--radius);
  cursor: pointer;
}
.cp-link:hover { border-color: var(--accent); }
.cp-link:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }''',
   "js": '''function cpCopy(text) {
  if (navigator.clipboard && window.isSecureContext) return navigator.clipboard.writeText(text);
  return new Promise(function (resolve, reject) {
    var ta = document.createElement("textarea");
    ta.value = text;
    ta.setAttribute("readonly", "");
    ta.style.position = "fixed";
    ta.style.opacity = "0";
    document.body.appendChild(ta);
    ta.select();
    var ok = false;
    try { ok = document.execCommand("copy"); } catch (e) { ok = false; }
    document.body.removeChild(ta);
    ok ? resolve() : reject(new Error("copy failed"));
  });
}

function cpFlash(btn, label) {
  var old = btn.textContent;
  btn.textContent = label;
  btn.disabled = true;
  setTimeout(function () { btn.textContent = old; btn.disabled = false; }, 1600);
}

var cpStatus = document.getElementById("cpStatus");

document.getElementById("cpMain").addEventListener("click", function () {
  var btn = this;
  cpCopy("npm i own-library").then(function () {
    cpFlash(btn, "Copied!");
    cpStatus.textContent = "Command copied.";
  }).catch(function () { cpStatus.textContent = "Copy failed — select manually."; });
});

document.getElementById("cpIcon").addEventListener("click", function () {
  var btn = this;
  cpCopy(document.getElementById("cpCode").textContent).then(function () {
    cpStatus.textContent = "Code copied.";
    btn.setAttribute("aria-label", "Copied");
    setTimeout(function () { btn.setAttribute("aria-label", "Copy code"); }, 1600);
  }).catch(function () { cpStatus.textContent = "Copy failed."; });
});

document.getElementById("cpLink").addEventListener("click", function () {
  var btn = this;
  cpCopy("https://own-library.dev/components").then(function () {
    cpFlash(btn, "Link copied!");
    cpStatus.textContent = "Share link copied.";
  }).catch(function () { cpStatus.textContent = "Copy failed."; });
});''',
  }],
 },
 {
  "folder": "buttons", "slug": "share-button", "title": "Share Button",
  "desc": "Share sheet with copy link, native share and social icons.",
  "idx_desc": "Share sheet with copy and social options.",
  "mini": '<div class="p-row" style="gap: 6px;"><span class="p-iconbtn soft"><span class="p-glyph"></span></span><span class="p-drop"><span></span></span></div>',
  "blocks": [{
   "id": "share-button", "title": "Share sheet",
   "html": '''<div class="shr-wrap">
  <button class="shr-btn" type="button" id="shrToggle" aria-expanded="false" aria-haspopup="dialog" aria-controls="shrSheet">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="M8.6 10.6l6.8-3.9M8.6 13.4l6.8 3.9"/></svg>
    Share
  </button>
  <div class="shr-sheet" id="shrSheet" role="dialog" aria-label="Share this page" hidden>
    <p class="shr-h">Share this page</p>
    <button class="shr-opt" type="button" id="shrCopy">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15V5a2 2 0 0 1 2-2h10"/></svg>
      Copy link
    </button>
    <button class="shr-opt" type="button" id="shrNative">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v12"/><path d="M7 10l5-5 5 5"/><path d="M5 15v4a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-4"/></svg>
      Share via device
    </button>
    <div class="shr-social">
      <a class="shr-soc" href="#" aria-label="Share on WhatsApp">WA</a>
      <a class="shr-soc" href="#" aria-label="Share on X">X</a>
      <a class="shr-soc" href="#" aria-label="Share by email">@</a>
    </div>
    <p class="shr-msg" id="shrMsg" aria-live="polite"></p>
  </div>
</div>''',
   "css": '''.shr-wrap { position: relative; display: inline-block; }
.shr-btn {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  border: 1px solid var(--border);
  background: var(--card);
  color: var(--text);
  font: inherit;
  font-size: 0.86rem;
  font-weight: 600;
  padding: 9px 15px;
  border-radius: var(--radius);
  cursor: pointer;
}
.shr-btn svg { width: 16px; height: 16px; }
.shr-btn:hover { border-color: var(--accent); color: var(--accent); }
.shr-btn:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.shr-sheet {
  position: absolute;
  top: calc(100% + 8px);
  left: 0;
  width: 240px;
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: 12px;
  z-index: 30;
}
.shr-h { margin: 0 0 8px; font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.07em; color: var(--muted); }
.shr-opt {
  display: flex;
  align-items: center;
  gap: 8px;
  width: 100%;
  border: 0;
  background: transparent;
  color: var(--text);
  font: inherit;
  font-size: 0.83rem;
  text-align: left;
  padding: 8px;
  border-radius: 4px;
  cursor: pointer;
}
.shr-opt svg { width: 16px; height: 16px; color: var(--accent); }
.shr-opt:hover { background: var(--bg); }
.shr-opt:focus-visible { outline: 2px solid var(--accent); outline-offset: -2px; }
.shr-social { display: flex; gap: 8px; margin-top: 8px; padding-top: 10px; border-top: 1px solid var(--border); }
.shr-soc {
  width: 32px;
  height: 32px;
  border-radius: 999px;
  border: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.72rem;
  font-weight: 700;
  color: var(--muted);
  text-decoration: none;
}
.shr-soc:hover { border-color: var(--accent); color: var(--accent); }
.shr-soc:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.shr-msg { margin: 8px 0 0; font-size: 0.74rem; color: var(--yes); min-height: 1em; }''',
   "js": '''(function () {
  var toggle = document.getElementById("shrToggle");
  var sheet = document.getElementById("shrSheet");
  var msg = document.getElementById("shrMsg");

  function set(open) {
    sheet.hidden = !open;
    toggle.setAttribute("aria-expanded", String(open));
  }

  toggle.addEventListener("click", function (e) {
    e.stopPropagation();
    set(sheet.hidden);
  });

  document.addEventListener("click", function (e) {
    if (!sheet.hidden && !sheet.contains(e.target) && e.target !== toggle) set(false);
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && !sheet.hidden) { set(false); toggle.focus(); }
  });

  function copy(text) {
    if (navigator.clipboard && window.isSecureContext) return navigator.clipboard.writeText(text);
    return new Promise(function (resolve, reject) {
      var ta = document.createElement("textarea");
      ta.value = text;
      ta.style.position = "fixed";
      ta.style.opacity = "0";
      document.body.appendChild(ta);
      ta.select();
      var ok = false;
      try { ok = document.execCommand("copy"); } catch (err) { ok = false; }
      document.body.removeChild(ta);
      ok ? resolve() : reject(new Error("fail"));
    });
  }

  document.getElementById("shrCopy").addEventListener("click", function () {
    copy("https://own-library.dev/components").then(function () {
      msg.textContent = "Link copied!";
    }).catch(function () { msg.textContent = "Copy failed."; });
  });

  document.getElementById("shrNative").addEventListener("click", function () {
    if (navigator.share) {
      navigator.share({ title: "OWN Library", url: "https://own-library.dev/components" }).then(function () {
        msg.textContent = "Shared.";
      }).catch(function () { msg.textContent = "Share cancelled."; });
    } else {
      msg.textContent = "Native share not supported — link copy karein.";
    }
  });

  sheet.querySelectorAll(".shr-soc").forEach(function (a) {
    a.addEventListener("click", function (e) {
      e.preventDefault();
      msg.textContent = a.getAttribute("aria-label") + " share demo.";
    });
  });
})();''',
  }],
 },
 {
  "folder": "buttons", "slug": "back-to-top", "title": "Back-to-Top Button",
  "desc": "Scroll-aware floating action inside a scrollable panel.",
  "idx_desc": "Scroll-aware floating back-to-top button.",
  "mini": '<div class="p-row" style="gap: 6px;"><span class="p-fab" style="width: 24px; height: 24px; font-size: 13px;">↑</span><span class="p-line" style="width: 40px;"></span></div>',
  "blocks": [{
   "id": "back-to-top", "title": "Back to top",
   "note": "Panel ke andar neeche scroll karein.",
   "html": '''<div class="bt-panel" id="btPanel">
  <section class="bt-sec"><h4 class="bt-h">Overview</h4><p class="bt-p">Panel ke andar content scroll hota hai. Neeche jaate hi button dikhega.</p></section>
  <section class="bt-sec"><h4 class="bt-h">Usage</h4><p class="bt-p">Long pages par back-to-top button user ko turant upar le jata hai.</p></section>
  <section class="bt-sec"><h4 class="bt-h">Accessibility</h4><p class="bt-p">Hidden state me button tabindex -1 aur aria-hidden hota hai.</p></section>
  <section class="bt-sec"><h4 class="bt-h">Motion</h4><p class="bt-p">prefers-reduced-motion on hone par smooth scroll off ho jata hai.</p></section>
  <button class="bt-top" type="button" id="btTop" aria-label="Back to top" aria-hidden="true" tabindex="-1">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19V5M6 11l6-6 6 6"/></svg>
  </button>
</div>''',
   "css": '''.bt-panel {
  position: relative;
  height: 340px;
  overflow: auto;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  background: var(--card);
  padding: 16px 16px 70px;
}
.bt-sec { border: 1px solid var(--border); border-radius: var(--radius); padding: 14px; margin-bottom: 12px; background: var(--bg); }
.bt-h { margin: 0 0 4px; font-size: 0.9rem; }
.bt-p { margin: 0; font-size: 0.82rem; color: var(--muted); line-height: 1.5; }
.bt-top {
  position: absolute;
  right: 14px;
  bottom: 14px;
  width: 40px;
  height: 40px;
  border-radius: 999px;
  border: 1px solid var(--border);
  background: var(--card);
  color: var(--accent);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: var(--shadow);
  opacity: 0;
  transform: translateY(8px);
  pointer-events: none;
  transition: opacity 0.2s, transform 0.2s;
}
.bt-top svg { width: 18px; height: 18px; }
.bt-top.is-vis { opacity: 1; transform: translateY(0); pointer-events: auto; }
.bt-top:hover { border-color: var(--accent); }
.bt-top:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
@media (prefers-reduced-motion: reduce) {
  .bt-top { transition: none; }
}''',
   "js": '''(function () {
  var panel = document.getElementById("btPanel");
  var btn = document.getElementById("btTop");

  function sync() {
    var show = panel.scrollTop > 120;
    btn.classList.toggle("is-vis", show);
    btn.setAttribute("aria-hidden", String(!show));
    btn.tabIndex = show ? 0 : -1;
  }

  panel.addEventListener("scroll", sync);
  btn.addEventListener("click", function () {
    var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    panel.scrollTo({ top: 0, behavior: reduce ? "auto" : "smooth" });
  });
  sync();
})();''',
  }],
 },
]
