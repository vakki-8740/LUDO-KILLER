CAT = "Forms & Inputs"
CAT_ID = "forms"

PAGES = [
 {
  "folder": "forms", "slug": "search-bar", "title": "Search Bar",
  "desc": "Pill search with icon, clear button and live suggestions.",
  "idx_desc": "Pill search with live suggestions and clear.",
  "mini": '<div class="p-search" style="width: 60px;"></div>',
  "blocks": [{
   "id": "search-bar", "title": "Search with suggestions",
   "html": '''<div class="sb-wrap">
  <div class="sb-bar">
    <svg class="sb-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>
    <input class="sb-input" id="sbInput" type="search" placeholder="Search components..." aria-label="Search components" autocomplete="off">
    <button class="sb-clear" type="button" id="sbClear" aria-label="Clear search" hidden>&times;</button>
    <span class="sb-key" aria-hidden="true">/</span>
  </div>
  <ul class="sb-list" id="sbList" role="listbox" aria-label="Suggestions"></ul>
  <p class="sb-hint" id="sbHint">Try “toast”, “table” or “login”.</p>
</div>''',
   "css": '''.sb-wrap { max-width: 420px; }
.sb-bar { display: flex; align-items: center; gap: 8px; border: 1px solid var(--border); background: var(--card); border-radius: 999px; padding: 6px 10px 6px 14px; transition: border-color 0.2s, box-shadow 0.2s; }
.sb-bar:focus-within { border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-soft); }
.sb-ic { width: 17px; height: 17px; color: var(--muted); flex: 0 0 auto; }
.sb-input { flex: 1; min-width: 0; border: 0; background: transparent; color: var(--text); font: inherit; font-size: 0.86rem; padding: 4px 0; outline: none; }
.sb-input::placeholder { color: var(--muted); }
.sb-clear { border: 0; background: var(--bg); color: var(--muted); width: 20px; height: 20px; border-radius: 999px; cursor: pointer; font-size: 0.9rem; line-height: 1; display: flex; align-items: center; justify-content: center; }
.sb-clear:hover { color: var(--text); }
.sb-clear:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.sb-key { font-size: 0.68rem; font-weight: 700; color: var(--muted); border: 1px solid var(--border); border-radius: 4px; padding: 1px 6px; }
.sb-list { list-style: none; margin: 8px 0 0; padding: 4px; background: var(--card); border: 1px solid var(--border); border-radius: var(--radius); box-shadow: var(--shadow); max-height: 190px; overflow: auto; }
.sb-list:empty { display: none; }
.sb-opt { display: flex; align-items: center; gap: 8px; width: 100%; border: 0; background: transparent; color: var(--text); font: inherit; font-size: 0.81rem; text-align: left; padding: 8px; border-radius: 4px; cursor: pointer; }
.sb-opt:hover, .sb-opt:focus-visible { background: var(--accent-soft); color: var(--accent); outline: none; }
.sb-opt mark { background: transparent; color: var(--accent); font-weight: 700; }
.sb-hint { margin: 8px 2px 0; font-size: 0.74rem; color: var(--muted); }''',
   "js": '''(function () {
  var items = ["Toast notifications", "Data table", "Login form", "Modal dialog", "Tabs", "Tooltip", "Pagination", "Accordion", "Color palette", "OTP input"];
  var input = document.getElementById("sbInput");
  var list = document.getElementById("sbList");
  var clear = document.getElementById("sbClear");
  var hint = document.getElementById("sbHint");

  function highlight(text, q) {
    if (!q) return text;
    var i = text.toLowerCase().indexOf(q.toLowerCase());
    if (i < 0) return text;
    return text.slice(0, i) + "<mark>" + text.slice(i, i + q.length) + "</mark>" + text.slice(i + q.length);
  }

  function render(q) {
    list.innerHTML = "";
    clear.hidden = !q;
    if (!q) { hint.textContent = "Try “toast”, “table” or “login”."; return; }
    var hits = items.filter(function (t) { return t.toLowerCase().indexOf(q.toLowerCase()) > -1; });
    if (!hits.length) { hint.textContent = "No matches for “" + q + "”."; return; }
    hint.textContent = hits.length + " result" + (hits.length > 1 ? "s" : "");
    hits.forEach(function (t) {
      var li = document.createElement("li");
      var b = document.createElement("button");
      b.type = "button";
      b.className = "sb-opt";
      b.setAttribute("role", "option");
      b.innerHTML = highlight(t, q);
      b.addEventListener("click", function () { input.value = t; render(t); input.focus(); });
      li.appendChild(b);
      list.appendChild(li);
    });
  }

  input.addEventListener("input", function () { render(input.value.trim()); });
  clear.addEventListener("click", function () { input.value = ""; render(""); input.focus(); });
  document.addEventListener("keydown", function (e) {
    if (e.key === "/" && document.activeElement !== input) { e.preventDefault(); input.focus(); }
  });
})();''',
  }],
 },
 {
  "folder": "forms", "slug": "email-phone", "title": "Email & Phone Input",
  "desc": "Toggle between email and phone with inline validation.",
  "idx_desc": "Email/phone toggle with inline validation.",
  "mini": '<div class="p-page" style="height: 46px;"><span class="p-line" style="width: 52px;"></span></div>',
  "blocks": [{
   "id": "email-phone", "title": "Contact input",
   "html": '''<div class="ep-card">
  <div class="ep-tabs" role="tablist" aria-label="Contact method">
    <button class="ep-tab is-on" type="button" role="tab" aria-selected="true" id="epTabEmail">Email</button>
    <button class="ep-tab" type="button" role="tab" aria-selected="false" id="epTabPhone">Phone</button>
  </div>
  <label class="ep-lbl" for="epField" id="epLabel">Email address</label>
  <div class="ep-field" id="epFieldWrap">
    <svg class="ep-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3.5 6.5L12 13l8.5-6.5"/></svg>
    <input class="ep-input" id="epField" type="email" placeholder="you@example.com" autocomplete="email">
  </div>
  <p class="ep-err" id="epErr" role="alert"></p>
  <button class="ep-btn" type="button" id="epSend">Continue</button>
  <p class="ep-ok" id="epOk" role="status"></p>
</div>''',
   "css": '''.ep-card { max-width: 380px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 16px; }
.ep-tabs { display: flex; gap: 4px; background: var(--bg); border-radius: var(--radius); padding: 3px; margin-bottom: 14px; }
.ep-tab { flex: 1; border: 0; background: transparent; color: var(--muted); font: inherit; font-size: 0.8rem; font-weight: 600; padding: 7px; border-radius: 4px; cursor: pointer; }
.ep-tab.is-on { background: var(--card); color: var(--text); box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08); }
.ep-tab:focus-visible { outline: 2px solid var(--accent); outline-offset: 1px; }
.ep-lbl { display: block; margin-bottom: 6px; font-size: 0.76rem; font-weight: 600; color: var(--muted); }
.ep-field { display: flex; align-items: center; gap: 8px; border: 1px solid var(--border); border-radius: var(--radius); padding: 0 10px; background: var(--bg); transition: border-color 0.2s, box-shadow 0.2s; }
.ep-field:focus-within { border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-soft); }
.ep-field.is-bad { border-color: var(--no); }
.ep-ic { width: 16px; height: 16px; color: var(--muted); flex: 0 0 auto; }
.ep-input { flex: 1; min-width: 0; border: 0; background: transparent; color: var(--text); font: inherit; font-size: 0.86rem; padding: 10px 0; outline: none; }
.ep-err { margin: 6px 0 0; min-height: 1em; font-size: 0.73rem; color: var(--no); }
.ep-btn { width: 100%; margin-top: 8px; border: 0; background: var(--accent); color: #fff; font: inherit; font-size: 0.84rem; font-weight: 600; padding: 10px; border-radius: var(--radius); cursor: pointer; }
.ep-btn:hover { opacity: 0.92; }
.ep-btn:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.ep-ok { margin: 8px 0 0; min-height: 1em; font-size: 0.76rem; color: var(--yes); }''',
   "js": '''(function () {
  var mode = "email";
  var field = document.getElementById("epField");
  var label = document.getElementById("epLabel");
  var icon = document.querySelector(".ep-ic");
  var err = document.getElementById("epErr");
  var ok = document.getElementById("epOk");
  var wrap = document.getElementById("epFieldWrap");

  function setMode(m) {
    mode = m;
    document.getElementById("epTabEmail").classList.toggle("is-on", m === "email");
    document.getElementById("epTabPhone").classList.toggle("is-on", m === "phone");
    document.getElementById("epTabEmail").setAttribute("aria-selected", String(m === "email"));
    document.getElementById("epTabPhone").setAttribute("aria-selected", String(m === "phone"));
    field.value = "";
    err.textContent = "";
    ok.textContent = "";
    wrap.classList.remove("is-bad");
    if (m === "email") {
      label.textContent = "Email address";
      field.type = "email";
      field.placeholder = "you@example.com";
      field.setAttribute("autocomplete", "email");
      icon.innerHTML = '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3.5 6.5L12 13l8.5-6.5"/>';
    } else {
      label.textContent = "Phone number";
      field.type = "tel";
      field.placeholder = "+91 98765 43210";
      field.setAttribute("autocomplete", "tel");
      icon.innerHTML = '<path d="M5 3h4l2 5-3 2a12 12 0 0 0 6 6l2-3 5 2v4a2 2 0 0 1-2 2A17 17 0 0 1 3 5a2 2 0 0 1 2-2z"/>';
    }
    field.focus();
  }

  document.getElementById("epTabEmail").addEventListener("click", function () { setMode("email"); });
  document.getElementById("epTabPhone").addEventListener("click", function () { setMode("phone"); });

  document.getElementById("epSend").addEventListener("click", function () {
    var v = field.value.trim();
    var valid = mode === "email"
      ? /^[^\\s@]+@[^\\s@]+\\.[^\\s@]{2,}$/.test(v)
      : /^\\+?[0-9][0-9\\s-]{6,15}$/.test(v);
    wrap.classList.toggle("is-bad", !valid);
    err.textContent = valid ? "" : (v ? "That " + mode + " does not look right." : "Please enter your " + mode + ".");
    ok.textContent = valid ? "Verification code sent to " + v + "." : "";
  });
})();''',
  }],
 },
 {
  "folder": "forms", "slug": "otp-input", "title": "OTP Input",
  "desc": "Six-box one-time code with auto-advance and paste.",
  "idx_desc": "Six-digit OTP with auto-advance and paste.",
  "mini": '<div class="p-row-tight"><span class="p-box"></span><span class="p-box"></span><span class="p-box"></span><span class="p-box"></span></div>',
  "blocks": [{
   "id": "otp-input", "title": "One-time code",
   "html": '''<div class="ot-card">
  <p class="ot-title">Enter verification code</p>
  <p class="ot-sub">We sent a 6-digit code to +91 98765 43210.</p>
  <div class="ot-row" id="otRow" role="group" aria-label="Verification code">
    <input class="ot-cell" type="text" inputmode="numeric" maxlength="1" aria-label="Digit 1" autocomplete="one-time-code">
    <input class="ot-cell" type="text" inputmode="numeric" maxlength="1" aria-label="Digit 2">
    <input class="ot-cell" type="text" inputmode="numeric" maxlength="1" aria-label="Digit 3">
    <input class="ot-cell" type="text" inputmode="numeric" maxlength="1" aria-label="Digit 4">
    <input class="ot-cell" type="text" inputmode="numeric" maxlength="1" aria-label="Digit 5">
    <input class="ot-cell" type="text" inputmode="numeric" maxlength="1" aria-label="Digit 6">
  </div>
  <p class="ot-msg" id="otMsg" role="status"></p>
  <button class="ot-btn" type="button" id="otVerify">Verify code</button>
  <button class="ot-resend" type="button" id="otResend">Resend code (30s)</button>
</div>''',
   "css": '''.ot-card { max-width: 380px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 20px; }
.ot-title { margin: 0 0 3px; font-size: 0.95rem; font-weight: 700; }
.ot-sub { margin: 0 0 16px; font-size: 0.78rem; color: var(--muted); }
.ot-row { display: flex; gap: 7px; margin-bottom: 10px; }
.ot-cell { width: 100%; min-width: 0; aspect-ratio: 1; text-align: center; font: inherit; font-size: 1.05rem; font-weight: 700; color: var(--text); background: var(--bg); border: 1px solid var(--border); border-radius: var(--radius); outline: none; transition: border-color 0.15s, box-shadow 0.15s; }
.ot-cell:focus { border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-soft); }
.ot-cell.is-full { border-color: var(--accent); }
.ot-msg { min-height: 1.1em; margin: 0 0 8px; font-size: 0.74rem; color: var(--no); }
.ot-msg.is-ok { color: var(--yes); }
.ot-btn { width: 100%; border: 0; background: var(--accent); color: #fff; font: inherit; font-size: 0.84rem; font-weight: 600; padding: 10px; border-radius: var(--radius); cursor: pointer; }
.ot-btn:hover { opacity: 0.92; }
.ot-btn:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.ot-resend { display: block; margin: 10px auto 0; border: 0; background: transparent; color: var(--accent); font: inherit; font-size: 0.75rem; font-weight: 600; cursor: pointer; }
.ot-resend[disabled] { color: var(--muted); cursor: default; }
.ot-resend:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; border-radius: 3px; }''',
   "js": '''(function () {
  var cells = Array.prototype.slice.call(document.querySelectorAll(".ot-cell"));
  var msg = document.getElementById("otMsg");
  var resend = document.getElementById("otResend");
  var left = 30;
  var timer;

  function value() { return cells.map(function (c) { return c.value; }).join(""); }
  function sync() {
    cells.forEach(function (c) { c.classList.toggle("is-full", !!c.value); });
  }

  cells.forEach(function (cell, i) {
    cell.addEventListener("input", function () {
      cell.value = cell.value.replace(/[^0-9]/g, "").slice(0, 1);
      sync();
      if (cell.value && i < cells.length - 1) cells[i + 1].focus();
    });
    cell.addEventListener("keydown", function (e) {
      if (e.key === "Backspace" && !cell.value && i > 0) {
        cells[i - 1].value = "";
        cells[i - 1].focus();
        sync();
      }
      if (e.key === "ArrowLeft" && i > 0) { e.preventDefault(); cells[i - 1].focus(); }
      if (e.key === "ArrowRight" && i < cells.length - 1) { e.preventDefault(); cells[i + 1].focus(); }
    });
    cell.addEventListener("paste", function (e) {
      var text = (e.clipboardData || window.clipboardData).getData("text").replace(/[^0-9]/g, "").slice(0, 6);
      if (!text) return;
      e.preventDefault();
      text.split("").forEach(function (ch, k) { if (cells[k]) cells[k].value = ch; });
      sync();
      cells[Math.min(text.length, cells.length - 1)].focus();
    });
  });

  document.getElementById("otVerify").addEventListener("click", function () {
    var v = value();
    if (v.length < 6) {
      msg.textContent = "Please enter all 6 digits.";
      msg.classList.remove("is-ok");
      return;
    }
    if (v === "123456") {
      msg.textContent = "Code verified. Redirecting...";
      msg.classList.add("is-ok");
    } else {
      msg.textContent = "Incorrect code. Demo code is 123456.";
      msg.classList.remove("is-ok");
    }
  });

  function tick() {
    left -= 1;
    if (left <= 0) {
      clearInterval(timer);
      resend.disabled = false;
      resend.textContent = "Resend code";
    } else {
      resend.textContent = "Resend code (" + left + "s)";
    }
  }

  resend.disabled = true;
  timer = setInterval(tick, 1000);
  resend.addEventListener("click", function () {
    if (resend.disabled) return;
    left = 30;
    resend.disabled = true;
    resend.textContent = "Resend code (30s)";
    timer = setInterval(tick, 1000);
    msg.textContent = "A new code was sent.";
    msg.classList.add("is-ok");
  });
})();''',
  }],
 },
 {
  "folder": "forms", "slug": "file-upload", "title": "File Upload",
  "desc": "Drag-and-drop zone with a selected file list.",
  "idx_desc": "Drag-and-drop upload with file list.",
  "mini": '<div class="p-drop" style="width: 58px; padding: 6px;"><span class="p-line" style="width: 30px;"></span></div>',
  "blocks": [{
   "id": "file-upload", "title": "Upload files",
   "html": '''<div class="fu-wrap">
  <label class="fu-drop" id="fuDrop" for="fuInput">
    <svg class="fu-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 16V4"/><path d="M7 9l5-5 5 5"/><path d="M4 15v3a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-3"/></svg>
    <span class="fu-strong">Drop files here or <span class="fu-link">browse</span></span>
    <span class="fu-hint">PDF, PNG or ZIP up to 10 MB</span>
    <input class="fu-input" id="fuInput" type="file" multiple>
  </label>
  <ul class="fu-list" id="fuList" aria-live="polite"></ul>
</div>''',
   "css": '''.fu-wrap { max-width: 420px; }
.fu-drop { display: flex; flex-direction: column; align-items: center; gap: 6px; text-align: center; border: 1.5px dashed var(--border); border-radius: var(--radius); background: var(--bg); padding: 26px 18px; cursor: pointer; transition: border-color 0.2s, background 0.2s; }
.fu-drop:hover, .fu-drop.is-over { border-color: var(--accent); background: var(--accent-soft); }
.fu-ic { width: 26px; height: 26px; color: var(--accent); }
.fu-strong { font-size: 0.84rem; font-weight: 600; }
.fu-link { color: var(--accent); text-decoration: underline; }
.fu-hint { font-size: 0.72rem; color: var(--muted); }
.fu-input { position: absolute; width: 1px; height: 1px; opacity: 0; pointer-events: none; }
.fu-list { list-style: none; margin: 10px 0 0; padding: 0; display: flex; flex-direction: column; gap: 6px; }
.fu-item { display: flex; align-items: center; gap: 8px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 7px 9px; }
.fu-doc { width: 26px; height: 30px; flex: 0 0 auto; color: var(--accent); }
.fu-doc svg { width: 100%; height: 100%; }
.fu-meta { flex: 1; min-width: 0; }
.fu-name { display: block; font-size: 0.78rem; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.fu-size { display: block; font-size: 0.7rem; color: var(--muted); }
.fu-x { border: 0; background: transparent; color: var(--muted); font-size: 1rem; cursor: pointer; padding: 2px 5px; border-radius: 3px; }
.fu-x:hover { color: var(--no); background: rgba(229, 72, 77, 0.08); }
.fu-x:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.fu-drop:focus-within { outline: 2px solid var(--accent); outline-offset: 3px; }''',
   "js": '''(function () {
  var drop = document.getElementById("fuDrop");
  var input = document.getElementById("fuInput");
  var list = document.getElementById("fuList");

  function size(n) {
    if (n < 1024) return n + " B";
    if (n < 1048576) return (n / 1024).toFixed(1) + " KB";
    return (n / 1048576).toFixed(1) + " MB";
  }

  function add(files) {
    Array.prototype.slice.call(files).forEach(function (f) {
      var li = document.createElement("li");
      li.className = "fu-item";
      li.innerHTML = '<span class="fu-doc"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4"/></svg></span>' +
        '<span class="fu-meta"><span class="fu-name"></span><span class="fu-size">' + size(f.size) + '</span></span>' +
        '<button class="fu-x" type="button" aria-label="Remove file">&times;</button>';
      li.querySelector(".fu-name").textContent = f.name;
      li.querySelector(".fu-x").addEventListener("click", function () { li.remove(); });
      list.appendChild(li);
    });
  }

  input.addEventListener("change", function () { add(input.files); input.value = ""; });
  ["dragenter", "dragover"].forEach(function (ev) {
    drop.addEventListener(ev, function (e) { e.preventDefault(); drop.classList.add("is-over"); });
  });
  ["dragleave", "drop"].forEach(function (ev) {
    drop.addEventListener(ev, function (e) { e.preventDefault(); drop.classList.remove("is-over"); });
  });
  drop.addEventListener("drop", function (e) {
    if (e.dataTransfer && e.dataTransfer.files) add(e.dataTransfer.files);
  });
})();''',
  }],
 },
 {
  "folder": "forms", "slug": "image-upload", "title": "Image Upload",
  "desc": "Avatar uploader with instant local preview.",
  "idx_desc": "Avatar uploader with local image preview.",
  "mini": '<div class="p-av" style="width: 28px; height: 28px;"></div><div class="p-dot" style="position: static;"></div>',
  "blocks": [{
   "id": "image-upload", "title": "Profile photo",
   "html": '''<div class="iu-card">
  <div class="iu-preview" id="iuPreview">
    <span class="iu-initial" id="iuInitial">A</span>
  </div>
  <label class="iu-btn" for="iuInput">Choose photo</label>
  <input class="iu-input" id="iuInput" type="file" accept="image/*">
  <button class="iu-remove" type="button" id="iuRemove" hidden>Remove</button>
  <p class="iu-note">JPG or PNG, at least 200 × 200 px.</p>
</div>''',
   "css": '''.iu-card { display: flex; flex-direction: column; align-items: center; gap: 9px; max-width: 280px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 24px 18px; }
.iu-preview { width: 92px; height: 92px; border-radius: 999px; background: var(--accent-soft); color: var(--accent); display: flex; align-items: center; justify-content: center; overflow: hidden; border: 2px solid var(--border); }
.iu-preview img { width: 100%; height: 100%; object-fit: cover; }
.iu-initial { font-size: 2rem; font-weight: 700; }
.iu-btn { border: 1px solid var(--border); background: var(--bg); color: var(--text); font: inherit; font-size: 0.8rem; font-weight: 600; padding: 8px 15px; border-radius: var(--radius); cursor: pointer; }
.iu-btn:hover { border-color: var(--accent); color: var(--accent); }
.iu-input { position: absolute; width: 1px; height: 1px; opacity: 0; }
.iu-input:focus-visible + .iu-remove { outline: 2px solid var(--accent); }
.iu-btn:focus-within, .iu-btn:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.iu-remove { border: 0; background: transparent; color: var(--no); font: inherit; font-size: 0.74rem; font-weight: 600; cursor: pointer; padding: 2px 6px; border-radius: 3px; }
.iu-remove:hover { background: rgba(229, 72, 77, 0.08); }
.iu-remove:focus-visible { outline: 2px solid var(--no); outline-offset: 2px; }
.iu-note { margin: 2px 0 0; font-size: 0.7rem; color: var(--muted); text-align: center; }''',
   "js": '''(function () {
  var input = document.getElementById("iuInput");
  var preview = document.getElementById("iuPreview");
  var initial = document.getElementById("iuInitial");
  var remove = document.getElementById("iuRemove");

  function reset() {
    preview.innerHTML = '<span class="iu-initial" id="iuInitial">A</span>';
    initial = document.getElementById("iuInitial");
    remove.hidden = true;
    input.value = "";
  }

  input.addEventListener("change", function () {
    var file = input.files && input.files[0];
    if (!file) return;
    if (!/^image\\//.test(file.type)) return;
    var reader = new FileReader();
    reader.onload = function () {
      preview.innerHTML = "";
      var img = document.createElement("img");
      img.alt = "Selected profile photo";
      img.src = String(reader.result);
      preview.appendChild(img);
      remove.hidden = false;
    };
    reader.readAsDataURL(file);
  });

  remove.addEventListener("click", function () { reset(); input.focus(); });
})();''',
  }],
 },
 {
  "folder": "forms", "slug": "date-picker", "title": "Date Picker",
  "desc": "Month calendar with prev/next and selected date display.",
  "idx_desc": "Month calendar with navigation and selection.",
  "mini": '<div class="p-cal"><span></span><span></span></div>',
  "blocks": [{
   "id": "date-picker", "title": "Calendar",
   "html": '''<div class="dt-card">
  <div class="dt-top">
    <button class="dt-nav" type="button" id="dtPrev" aria-label="Previous month">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 6l-6 6 6 6"/></svg>
    </button>
    <span class="dt-month" id="dtMonth" aria-live="polite"></span>
    <button class="dt-nav" type="button" id="dtNext" aria-label="Next month">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg>
    </button>
  </div>
  <div class="dt-week" aria-hidden="true">
    <span class="dt-wd">Su</span><span class="dt-wd">Mo</span><span class="dt-wd">Tu</span><span class="dt-wd">We</span><span class="dt-wd">Th</span><span class="dt-wd">Fr</span><span class="dt-wd">Sa</span>
  </div>
  <div class="dt-grid" id="dtGrid" role="grid" aria-label="Calendar"></div>
  <p class="dt-picked">Selected: <strong id="dtPicked">none</strong></p>
</div>''',
   "css": '''.dt-card { max-width: 320px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 12px; }
.dt-top { display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px; }
.dt-month { font-size: 0.84rem; font-weight: 700; }
.dt-nav { width: 28px; height: 28px; display: flex; align-items: center; justify-content: center; border: 1px solid var(--border); border-radius: 4px; background: transparent; color: var(--muted); cursor: pointer; }
.dt-nav svg { width: 15px; height: 15px; }
.dt-nav:hover { border-color: var(--accent); color: var(--accent); }
.dt-nav:focus-visible { outline: 2px solid var(--accent); outline-offset: 1px; }
.dt-week { display: grid; grid-template-columns: repeat(7, 1fr); gap: 2px; margin-bottom: 4px; }
.dt-wd { text-align: center; font-size: 0.64rem; font-weight: 700; text-transform: uppercase; color: var(--muted); padding: 3px 0; }
.dt-grid { display: grid; grid-template-columns: repeat(7, 1fr); gap: 2px; }
.dt-day { aspect-ratio: 1; border: 0; background: transparent; color: var(--text); font: inherit; font-size: 0.74rem; border-radius: 4px; cursor: pointer; }
.dt-day:hover { background: var(--bg); }
.dt-day:focus-visible { outline: 2px solid var(--accent); outline-offset: -1px; }
.dt-day.is-today { color: var(--accent); font-weight: 700; box-shadow: inset 0 0 0 1px var(--accent); }
.dt-day.is-sel { background: var(--accent); color: #fff; font-weight: 700; }
.dt-day.is-empty { visibility: hidden; }
.dt-picked { margin: 10px 0 0; font-size: 0.74rem; color: var(--muted); text-align: center; }''',
   "js": '''(function () {
  var grid = document.getElementById("dtGrid");
  var monthEl = document.getElementById("dtMonth");
  var picked = document.getElementById("dtPicked");
  var view = new Date();
  view.setDate(1);
  var selected = null;
  var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

  function sameDay(a, b) {
    return a.getFullYear() === b.getFullYear() && a.getMonth() === b.getMonth() && a.getDate() === b.getDate();
  }

  function render() {
    monthEl.textContent = months[view.getMonth()] + " " + view.getFullYear();
    grid.innerHTML = "";
    var first = new Date(view.getFullYear(), view.getMonth(), 1).getDay();
    var days = new Date(view.getFullYear(), view.getMonth() + 1, 0).getDate();
    var today = new Date();
    for (var i = 0; i < first; i++) {
      var pad = document.createElement("button");
      pad.type = "button";
      pad.className = "dt-day is-empty";
      pad.tabIndex = -1;
      pad.setAttribute("aria-hidden", "true");
      grid.appendChild(pad);
    }
    for (var d = 1; d <= days; d++) {
      var b = document.createElement("button");
      b.type = "button";
      b.className = "dt-day";
      b.textContent = d;
      var date = new Date(view.getFullYear(), view.getMonth(), d);
      if (sameDay(date, today)) b.classList.add("is-today");
      if (selected && sameDay(date, selected)) b.classList.add("is-sel");
      b.addEventListener("click", function (day) {
        return function () {
          selected = new Date(view.getFullYear(), view.getMonth(), day);
          picked.textContent = selected.toDateString();
          render();
        };
      }(d));
      grid.appendChild(b);
    }
  }

  document.getElementById("dtPrev").addEventListener("click", function () {
    view.setMonth(view.getMonth() - 1);
    render();
  });
  document.getElementById("dtNext").addEventListener("click", function () {
    view.setMonth(view.getMonth() + 1);
    render();
  });

  render();
})();''',
  }],
 },
 {
  "folder": "forms", "slug": "time-picker", "title": "Time Picker",
  "desc": "Scrollable hour, minute and period columns.",
  "idx_desc": "Scrollable hour, minute and period columns.",
  "mini": '<div class="p-row-tight"><span class="p-box"></span><span class="p-box"></span><span class="p-box"></span></div>',
  "blocks": [{
   "id": "time-picker", "title": "Pick a time",
   "html": '''<div class="tm-card">
  <p class="tm-lbl">Select reminder time</p>
  <div class="tm-cols">
    <div class="tm-col" role="group" aria-label="Hour">
      <button class="tm-opt is-on" type="button">09</button>
      <button class="tm-opt" type="button">10</button>
      <button class="tm-opt" type="button">11</button>
      <button class="tm-opt" type="button">12</button>
      <button class="tm-opt" type="button">01</button>
    </div>
    <div class="tm-col" role="group" aria-label="Minute">
      <button class="tm-opt is-on" type="button">00</button>
      <button class="tm-opt" type="button">15</button>
      <button class="tm-opt" type="button">30</button>
      <button class="tm-opt" type="button">45</button>
    </div>
    <div class="tm-col" role="group" aria-label="Period">
      <button class="tm-opt is-on" type="button">AM</button>
      <button class="tm-opt" type="button">PM</button>
    </div>
  </div>
  <div class="tm-out">
    <span class="tm-val" id="tmVal">09:00 AM</span>
    <button class="tm-now" type="button" id="tmNow">Use current time</button>
  </div>
</div>''',
   "css": '''.tm-card { max-width: 300px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 14px; }
.tm-lbl { margin: 0 0 10px; font-size: 0.76rem; font-weight: 600; color: var(--muted); }
.tm-cols { display: grid; grid-template-columns: 1fr 1fr 0.8fr; gap: 6px; }
.tm-col { height: 112px; overflow: auto; border: 1px solid var(--border); border-radius: var(--radius); padding: 4px; display: flex; flex-direction: column; gap: 2px; background: var(--bg); }
.tm-opt { border: 0; background: transparent; color: var(--text); font: inherit; font-size: 0.78rem; padding: 7px 4px; border-radius: 4px; cursor: pointer; flex: 0 0 auto; }
.tm-opt:hover { background: var(--accent-soft); color: var(--accent); }
.tm-opt.is-on { background: var(--accent); color: #fff; font-weight: 700; }
.tm-opt:focus-visible { outline: 2px solid var(--accent); outline-offset: -2px; }
.tm-out { display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-top: 10px; flex-wrap: wrap; }
.tm-val { font-size: 0.9rem; font-weight: 700; color: var(--accent); }
.tm-now { border: 1px solid var(--border); background: transparent; color: var(--muted); font: inherit; font-size: 0.7rem; font-weight: 600; padding: 5px 9px; border-radius: 4px; cursor: pointer; }
.tm-now:hover { border-color: var(--accent); color: var(--accent); }
.tm-now:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }''',
   "js": '''(function () {
  var cols = Array.prototype.slice.call(document.querySelectorAll(".tm-col"));
  var val = document.getElementById("tmVal");
  var state = { 0: "09", 1: "00", 2: "AM" };

  function render() {
    val.textContent = state[0] + ":" + state[1] + " " + state[2];
  }

  cols.forEach(function (col, ci) {
    var opts = Array.prototype.slice.call(col.querySelectorAll(".tm-opt"));
    opts.forEach(function (opt) {
      opt.addEventListener("click", function () {
        opts.forEach(function (o) { o.classList.remove("is-on"); });
        opt.classList.add("is-on");
        state[ci] = opt.textContent;
        render();
      });
    });
  });

  document.getElementById("tmNow").addEventListener("click", function () {
    var d = new Date();
    var h = d.getHours();
    var period = h >= 12 ? "PM" : "AM";
    h = h % 12 || 12;
    var m = Math.floor(d.getMinutes() / 15) * 15;
    state[0] = String(h).padStart(2, "0");
    state[1] = String(m).padStart(2, "0");
    state[2] = period;
    cols.forEach(function (col, ci) {
      col.querySelectorAll(".tm-opt").forEach(function (o) {
        o.classList.toggle("is-on", o.textContent === state[ci]);
      });
    });
    render();
  });

  render();
})();''',
  }],
 },
 {
  "folder": "forms", "slug": "color-picker", "title": "Color Picker",
  "desc": "Swatch palette with native picker and hex value.",
  "idx_desc": "Swatch palette with hex value field.",
  "mini": '<div class="p-row-tight"><span class="p-dot" style="position: static; background: #4f6bed;"></span><span class="p-dot" style="position: static; background: #22a06b;"></span><span class="p-dot" style="position: static; background: #e5484d;"></span></div>',
  "blocks": [{
   "id": "color-picker", "title": "Pick a color",
   "html": '''<div class="cl-card">
  <div class="cl-top">
    <span class="cl-swatch is-on" id="clSwatch"></span>
    <div>
      <p class="cl-name" id="clName">Indigo</p>
      <p class="cl-hex" id="clHex">#4F6BED</p>
    </div>
  </div>
  <div class="cl-row" id="clRow">
    <button class="cl-dot" type="button" data-color="#4f6bed" data-name="Indigo" aria-label="Indigo" style="background: #4f6bed;"></button>
    <button class="cl-dot" type="button" data-color="#8b5cf6" data-name="Violet" aria-label="Violet" style="background: #8b5cf6;"></button>
    <button class="cl-dot" type="button" data-color="#22a06b" data-name="Green" aria-label="Green" style="background: #22a06b;"></button>
    <button class="cl-dot" type="button" data-color="#e5484d" data-name="Red" aria-label="Red" style="background: #e5484d;"></button>
    <button class="cl-dot" type="button" data-color="#f0b543" data-name="Amber" aria-label="Amber" style="background: #f0b543;"></button>
    <label class="cl-custom" aria-label="Custom color">
      <input class="cl-input" id="clInput" type="color" value="#4f6bed">
    </label>
  </div>
  <label class="cl-lbl" for="clText">Hex value</label>
  <input class="cl-text" id="clText" type="text" value="#4F6BED" maxlength="7" spellcheck="false">
</div>''',
   "css": '''.cl-card { max-width: 300px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 14px; }
.cl-top { display: flex; align-items: center; gap: 10px; margin-bottom: 12px; }
.cl-swatch { width: 40px; height: 40px; border-radius: var(--radius); background: #4f6bed; box-shadow: inset 0 0 0 1px rgba(0, 0, 0, 0.12); }
.cl-name { margin: 0; font-size: 0.84rem; font-weight: 700; }
.cl-hex { margin: 1px 0 0; font-size: 0.74rem; color: var(--muted); font-family: ui-monospace, Menlo, Consolas, monospace; }
.cl-row { display: flex; align-items: center; gap: 7px; flex-wrap: wrap; margin-bottom: 12px; }
.cl-dot { width: 24px; height: 24px; border-radius: 999px; border: 2px solid var(--card); box-shadow: 0 0 0 1px var(--border); cursor: pointer; padding: 0; }
.cl-dot.is-on { box-shadow: 0 0 0 2px var(--accent); }
.cl-dot:hover { transform: scale(1.1); }
.cl-dot:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.cl-custom { width: 26px; height: 26px; border-radius: 999px; border: 1px dashed var(--muted); overflow: hidden; cursor: pointer; display: flex; align-items: center; justify-content: center; }
.cl-input { width: 34px; height: 34px; border: 0; background: transparent; padding: 0; cursor: pointer; }
.cl-lbl { display: block; margin-bottom: 4px; font-size: 0.72rem; font-weight: 600; color: var(--muted); }
.cl-text { width: 100%; border: 1px solid var(--border); border-radius: var(--radius); background: var(--bg); color: var(--text); font: inherit; font-size: 0.8rem; font-family: ui-monospace, Menlo, Consolas, monospace; padding: 8px 10px; outline: none; }
.cl-text:focus { border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-soft); }''',
   "js": '''(function () {
  var swatch = document.getElementById("clSwatch");
  var name = document.getElementById("clName");
  var hex = document.getElementById("clHex");
  var text = document.getElementById("clText");
  var input = document.getElementById("clInput");
  var dots = Array.prototype.slice.call(document.querySelectorAll(".cl-dot"));

  function apply(color, label) {
    swatch.style.background = color;
    hex.textContent = color.toUpperCase();
    text.value = color.toUpperCase();
    input.value = color;
    name.textContent = label || "Custom";
    dots.forEach(function (d) { d.classList.toggle("is-on", d.getAttribute("data-color") === color.toLowerCase()); });
  }

  dots.forEach(function (d) {
    d.addEventListener("click", function () { apply(d.getAttribute("data-color"), d.getAttribute("data-name")); });
  });

  input.addEventListener("input", function () { apply(input.value, "Custom"); });

  text.addEventListener("change", function () {
    var v = text.value.trim();
    if (/^#[0-9a-fA-F]{6}$/.test(v)) apply(v.toLowerCase(), "Custom");
    else text.value = hex.textContent;
  });
})();''',
  }],
 },
 {
  "folder": "forms", "slug": "range-slider", "title": "Range Slider",
  "desc": "Styled range input with live value and presets.",
  "idx_desc": "Styled range input with live value.",
  "mini": '<div class="p-line" style="width: 48px; border-color: var(--accent);"></div><div class="p-dot" style="position: static; background: var(--accent);"></div>',
  "blocks": [{
   "id": "range-slider", "title": "Budget range",
   "html": '''<div class="rg-card">
  <div class="rg-top">
    <label class="rg-lbl" for="rgInput">Monthly budget</label>
    <output class="rg-out" id="rgOut" for="rgInput">$250</output>
  </div>
  <input class="rg-input" id="rgInput" type="range" min="0" max="1000" step="10" value="250" aria-valuetext="$250">
  <div class="rg-scale" aria-hidden="true"><span class="rg-t">$0</span><span class="rg-t">$500</span><span class="rg-t">$1000</span></div>
  <div class="rg-presets" role="group" aria-label="Presets">
    <button class="rg-pre" type="button" data-v="100">$100</button>
    <button class="rg-pre" type="button" data-v="250">$250</button>
    <button class="rg-pre" type="button" data-v="500">$500</button>
    <button class="rg-pre" type="button" data-v="800">$800</button>
  </div>
</div>''',
   "css": '''.rg-card { max-width: 340px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 16px; }
.rg-top { display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-bottom: 10px; }
.rg-lbl { font-size: 0.76rem; font-weight: 600; color: var(--muted); }
.rg-out { font-size: 0.88rem; font-weight: 700; color: var(--accent); }
.rg-input { width: 100%; accent-color: var(--accent); cursor: pointer; height: 22px; }
.rg-input:focus-visible { outline: 2px solid var(--accent); outline-offset: 3px; border-radius: 4px; }
.rg-scale { display: flex; justify-content: space-between; margin-top: 2px; }
.rg-t { font-size: 0.68rem; color: var(--muted); }
.rg-presets { display: flex; gap: 6px; flex-wrap: wrap; margin-top: 12px; }
.rg-pre { border: 1px solid var(--border); background: var(--bg); color: var(--text); font: inherit; font-size: 0.72rem; font-weight: 600; padding: 5px 10px; border-radius: 999px; cursor: pointer; }
.rg-pre:hover { border-color: var(--accent); color: var(--accent); }
.rg-pre.is-on { background: var(--accent); border-color: var(--accent); color: #fff; }
.rg-pre:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }''',
   "js": '''(function () {
  var input = document.getElementById("rgInput");
  var out = document.getElementById("rgOut");
  var pres = Array.prototype.slice.call(document.querySelectorAll(".rg-pre"));

  function paint() {
    var v = Number(input.value);
    out.textContent = "$" + v;
    input.setAttribute("aria-valuetext", "$" + v);
    pres.forEach(function (p) { p.classList.toggle("is-on", Number(p.getAttribute("data-v")) === v); });
  }

  input.addEventListener("input", paint);
  pres.forEach(function (p) {
    p.addEventListener("click", function () {
      input.value = p.getAttribute("data-v");
      paint();
    });
  });
  paint();
})();''',
  }],
 },
 {
  "folder": "forms", "slug": "rating-input", "title": "Rating Input",
  "desc": "Interactive star rating with label and reset.",
  "idx_desc": "Interactive star rating with reset.",
  "mini": '<div class="p-row-tight"><span class="p-star">★</span><span class="p-star">★</span><span class="p-star">★</span></div>',
  "blocks": [{
   "id": "rating-input", "title": "Rate this page",
   "html": '''<div class="rt-card">
  <p class="rt-q">How was this component?</p>
  <div class="rt-stars" id="rtStars" role="group" aria-label="Rating from 1 to 5">
    <button class="rt-star" type="button" data-v="1" aria-label="1 star" aria-pressed="false">
      <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2.5l2.9 6 6.6.9-4.8 4.6 1.2 6.5L12 17.4 6.1 20.5l1.2-6.5L2.5 9.4l6.6-.9z"/></svg>
    </button>
    <button class="rt-star" type="button" data-v="2" aria-label="2 stars" aria-pressed="false">
      <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2.5l2.9 6 6.6.9-4.8 4.6 1.2 6.5L12 17.4 6.1 20.5l1.2-6.5L2.5 9.4l6.6-.9z"/></svg>
    </button>
    <button class="rt-star" type="button" data-v="3" aria-label="3 stars" aria-pressed="false">
      <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2.5l2.9 6 6.6.9-4.8 4.6 1.2 6.5L12 17.4 6.1 20.5l1.2-6.5L2.5 9.4l6.6-.9z"/></svg>
    </button>
    <button class="rt-star" type="button" data-v="4" aria-label="4 stars" aria-pressed="false">
      <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2.5l2.9 6 6.6.9-4.8 4.6 1.2 6.5L12 17.4 6.1 20.5l1.2-6.5L2.5 9.4l6.6-.9z"/></svg>
    </button>
    <button class="rt-star" type="button" data-v="5" aria-label="5 stars" aria-pressed="false">
      <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2.5l2.9 6 6.6.9-4.8 4.6 1.2 6.5L12 17.4 6.1 20.5l1.2-6.5L2.5 9.4l6.6-.9z"/></svg>
    </button>
  </div>
  <p class="rt-msg" id="rtMsg" aria-live="polite">Tap a star to rate.</p>
  <button class="rt-reset" type="button" id="rtReset">Reset rating</button>
</div>''',
   "css": '''.rt-card { max-width: 320px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 18px; text-align: center; }
.rt-q { margin: 0 0 10px; font-size: 0.86rem; font-weight: 700; }
.rt-stars { display: flex; justify-content: center; gap: 3px; margin-bottom: 8px; }
.rt-star { border: 0; background: transparent; color: var(--border); padding: 2px; cursor: pointer; transition: transform 0.12s, color 0.12s; }
.rt-star svg { width: 28px; height: 28px; }
.rt-star:hover { transform: scale(1.12); }
.rt-star.is-on { color: #f0b543; }
.rt-star:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; border-radius: 4px; }
.rt-msg { min-height: 1.1em; margin: 0 0 10px; font-size: 0.76rem; color: var(--muted); }
.rt-reset { border: 1px solid var(--border); background: transparent; color: var(--muted); font: inherit; font-size: 0.72rem; font-weight: 600; padding: 5px 10px; border-radius: 4px; cursor: pointer; }
.rt-reset:hover { border-color: var(--accent); color: var(--accent); }
.rt-reset:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }''',
   "js": '''(function () {
  var stars = Array.prototype.slice.call(document.querySelectorAll(".rt-star"));
  var msg = document.getElementById("rtMsg");
  var labels = ["", "Poor", "Fair", "Good", "Great", "Excellent"];

  function set(v) {
    stars.forEach(function (s) {
      var on = Number(s.getAttribute("data-v")) <= v;
      s.classList.toggle("is-on", on);
      s.setAttribute("aria-pressed", String(on));
    });
    msg.textContent = v ? v + " of 5 — " + labels[v] : "Tap a star to rate.";
  }

  stars.forEach(function (s) {
    s.addEventListener("click", function () { set(Number(s.getAttribute("data-v"))); });
  });

  document.getElementById("rtReset").addEventListener("click", function () { set(0); });
})();''',
  }],
 },
 {
  "folder": "forms", "slug": "multi-select", "title": "Multi Select",
  "desc": "Dropdown with checkboxes and removable chips.",
  "idx_desc": "Dropdown checkboxes with removable chips.",
  "mini": '<div class="p-row-tight"><span class="p-tag">A</span><span class="p-tag">B</span></div>',
  "blocks": [{
   "id": "multi-select", "title": "Choose tags",
   "html": '''<div class="ms-wrap">
  <label class="ms-lbl" id="msLabel">Topics</label>
  <div class="ms-box" id="msBox">
    <div class="ms-chips" id="msChips"></div>
    <button class="ms-toggle" type="button" id="msToggle" aria-expanded="false" aria-haspopup="listbox" aria-labelledby="msLabel" aria-controls="msMenu">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
    </button>
  </div>
  <div class="ms-menu" id="msMenu" role="listbox" aria-multiselectable="true" hidden>
    <label class="ms-opt"><input class="ms-check" type="checkbox" value="Design"> <span class="ms-text">Design</span></label>
    <label class="ms-opt"><input class="ms-check" type="checkbox" value="Development"> <span class="ms-text">Development</span></label>
    <label class="ms-opt"><input class="ms-check" type="checkbox" value="Marketing"> <span class="ms-text">Marketing</span></label>
    <label class="ms-opt"><input class="ms-check" type="checkbox" value="Research"> <span class="ms-text">Research</span></label>
  </div>
  <p class="ms-count" id="msCount">0 selected</p>
</div>''',
   "css": '''.ms-wrap { position: relative; max-width: 340px; }
.ms-lbl { display: block; margin-bottom: 6px; font-size: 0.74rem; font-weight: 600; color: var(--muted); }
.ms-box { display: flex; align-items: center; gap: 6px; flex-wrap: wrap; border: 1px solid var(--border); border-radius: var(--radius); background: var(--bg); padding: 6px 8px; min-height: 42px; }
.ms-box:focus-within, .ms-box.is-open { border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-soft); }
.ms-chips { display: flex; gap: 5px; flex-wrap: wrap; flex: 1; }
.ms-chip { display: inline-flex; align-items: center; gap: 4px; background: var(--accent-soft); color: var(--accent); border-radius: 999px; font-size: 0.72rem; font-weight: 600; padding: 3px 4px 3px 9px; }
.ms-chip button { border: 0; background: transparent; color: inherit; cursor: pointer; font-size: 0.85rem; line-height: 1; padding: 1px 4px; border-radius: 999px; }
.ms-chip button:hover { background: rgba(79, 107, 237, 0.18); }
.ms-chip button:focus-visible { outline: 2px solid var(--accent); outline-offset: 1px; }
.ms-toggle { border: 0; background: transparent; color: var(--muted); cursor: pointer; padding: 5px; border-radius: 4px; display: flex; }
.ms-toggle svg { width: 15px; height: 15px; }
.ms-toggle:hover { color: var(--accent); }
.ms-toggle:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.ms-menu { position: absolute; top: calc(100% + 6px); left: 0; right: 0; background: var(--card); border: 1px solid var(--border); border-radius: var(--radius); box-shadow: var(--shadow); padding: 5px; z-index: 20; }
.ms-opt { display: flex; align-items: center; gap: 8px; padding: 8px 9px; border-radius: 4px; font-size: 0.8rem; cursor: pointer; }
.ms-opt:hover { background: var(--bg); }
.ms-check { accent-color: var(--accent); width: 15px; height: 15px; }
.ms-text { flex: 1; }
.ms-count { margin: 6px 2px 0; font-size: 0.72rem; color: var(--muted); }''',
   "js": '''(function () {
  var box = document.getElementById("msBox");
  var toggle = document.getElementById("msToggle");
  var menu = document.getElementById("msMenu");
  var chips = document.getElementById("msChips");
  var count = document.getElementById("msCount");
  var checks = Array.prototype.slice.call(document.querySelectorAll(".ms-check"));

  function selected() { return checks.filter(function (c) { return c.checked; }).map(function (c) { return c.value; }); }

  function render() {
    var vals = selected();
    chips.innerHTML = "";
    vals.forEach(function (v) {
      var chip = document.createElement("span");
      chip.className = "ms-chip";
      chip.textContent = v;
      var x = document.createElement("button");
      x.type = "button";
      x.setAttribute("aria-label", "Remove " + v);
      x.innerHTML = "&times;";
      x.addEventListener("click", function () {
        checks.forEach(function (c) { if (c.value === v) c.checked = false; });
        render();
      });
      chip.appendChild(x);
      chips.appendChild(chip);
    });
    count.textContent = vals.length + " selected";
  }

  function set(open) {
    menu.hidden = !open;
    toggle.setAttribute("aria-expanded", String(open));
    box.classList.toggle("is-open", open);
  }

  toggle.addEventListener("click", function (e) { e.stopPropagation(); set(menu.hidden); });

  document.addEventListener("click", function (e) {
    if (!menu.hidden && !box.contains(e.target)) set(false);
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && !menu.hidden) { set(false); toggle.focus(); }
  });

  checks.forEach(function (c) { c.addEventListener("change", render); });
  render();
})();''',
  }],
 },
 {
  "folder": "forms", "slug": "autocomplete", "title": "Autocomplete",
  "desc": "Filtered suggestion list with keyboard navigation.",
  "idx_desc": "Filtered suggestions with arrow-key navigation.",
  "mini": '<div class="p-drop" style="width: 60px; padding: 5px;"><span class="p-line" style="width: 38px;"></span><span class="p-line" style="width: 30px;"></span></div>',
  "blocks": [{
   "id": "autocomplete", "title": "City autocomplete",
   "html": '''<div class="ac-wrap">
  <label class="ac-lbl" for="acInput">Destination</label>
  <div class="ac-field">
    <svg class="ac-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>
    <input class="ac-input" id="acInput" type="text" placeholder="Start typing a city" autocomplete="off" role="combobox" aria-expanded="false" aria-controls="acList" aria-autocomplete="list">
  </div>
  <ul class="ac-list" id="acList" role="listbox" aria-label="Cities" hidden></ul>
  <p class="ac-hint" id="acHint">Use arrow keys to move, Enter to select.</p>
</div>''',
   "css": '''.ac-wrap { position: relative; max-width: 340px; }
.ac-lbl { display: block; margin-bottom: 6px; font-size: 0.74rem; font-weight: 600; color: var(--muted); }
.ac-field { display: flex; align-items: center; gap: 8px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--bg); padding: 0 11px; }
.ac-field:focus-within { border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-soft); }
.ac-ic { width: 16px; height: 16px; color: var(--muted); flex: 0 0 auto; }
.ac-input { flex: 1; min-width: 0; border: 0; background: transparent; color: var(--text); font: inherit; font-size: 0.85rem; padding: 10px 0; outline: none; }
.ac-list { position: absolute; top: calc(100% + 6px); left: 0; right: 0; list-style: none; margin: 0; padding: 4px; background: var(--card); border: 1px solid var(--border); border-radius: var(--radius); box-shadow: var(--shadow); max-height: 190px; overflow: auto; z-index: 20; }
.ac-opt { display: flex; align-items: center; justify-content: space-between; gap: 8px; width: 100%; border: 0; background: transparent; color: var(--text); font: inherit; font-size: 0.81rem; text-align: left; padding: 8px 9px; border-radius: 4px; cursor: pointer; }
.ac-opt:hover, .ac-opt.is-active { background: var(--accent-soft); color: var(--accent); }
.ac-opt:focus-visible { outline: 2px solid var(--accent); outline-offset: -2px; }
.ac-country { font-size: 0.68rem; color: var(--muted); }
.ac-hint { margin: 6px 2px 0; font-size: 0.72rem; color: var(--muted); }''',
   "js": '''(function () {
  var cities = [
    ["Mumbai", "India"], ["Delhi", "India"], ["Bengaluru", "India"], ["Pune", "India"],
    ["Tokyo", "Japan"], ["Osaka", "Japan"], ["Paris", "France"], ["Lyon", "France"],
    ["Berlin", "Germany"], ["Munich", "Germany"], ["London", "UK"], ["Toronto", "Canada"]
  ];
  var input = document.getElementById("acInput");
  var list = document.getElementById("acList");
  var hint = document.getElementById("acHint");
  var active = -1;
  var shown = [];

  function close() {
    list.hidden = true;
    list.innerHTML = "";
    input.setAttribute("aria-expanded", "false");
    active = -1;
  }

  function choose(name) {
    input.value = name;
    close();
    hint.textContent = "Selected " + name + ".";
  }

  function render(q) {
    list.innerHTML = "";
    active = -1;
    if (!q) { close(); return; }
    shown = cities.filter(function (c) { return c[0].toLowerCase().indexOf(q.toLowerCase()) === 0; }).slice(0, 6);
    if (!shown.length) { close(); hint.textContent = "No city matches “" + q + "”."; return; }
    shown.forEach(function (c) {
      var li = document.createElement("li");
      li.setAttribute("role", "option");
      var b = document.createElement("button");
      b.type = "button";
      b.className = "ac-opt";
      b.innerHTML = "<span>" + c[0] + "</span><span class=\\"ac-country\\">" + c[1] + "</span>";
      b.addEventListener("click", function () { choose(c[0]); });
      li.appendChild(b);
      list.appendChild(li);
    });
    list.hidden = false;
    input.setAttribute("aria-expanded", "true");
    hint.textContent = shown.length + " suggestion" + (shown.length > 1 ? "s" : "") + ".";
  }

  input.addEventListener("input", function () { render(input.value.trim()); });

  input.addEventListener("keydown", function (e) {
    var opts = Array.prototype.slice.call(list.querySelectorAll(".ac-opt"));
    if (list.hidden || !opts.length) return;
    if (e.key === "ArrowDown") {
      e.preventDefault();
      active = (active + 1) % opts.length;
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      active = (active - 1 + opts.length) % opts.length;
    } else if (e.key === "Enter" && active > -1) {
      e.preventDefault();
      choose(shown[active][0]);
      return;
    } else if (e.key === "Escape") {
      close();
      return;
    } else {
      return;
    }
    opts.forEach(function (o, i) { o.classList.toggle("is-active", i === active); });
    opts[active].scrollIntoView({ block: "nearest" });
  });

  document.addEventListener("click", function (e) {
    if (!list.hidden && !list.contains(e.target) && e.target !== input) close();
  });
})();''',
  }],
 },
]
