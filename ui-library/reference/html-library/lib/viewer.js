(function () {
  "use strict";

  var TOKENS = [
    ":root {",
    "  --bg: #f4f5f7;",
    "  --card: #ffffff;",
    "  --text: #1f2430;",
    "  --muted: #6b7280;",
    "  --border: #e5e7eb;",
    "  --shadow: 0 8px 30px rgba(0, 0, 0, 0.08);",
    "  --accent: #4f6bed;",
    "  --accent-soft: rgba(79, 107, 237, 0.10);",
    "  --yes: #22a06b;",
    "  --no: #e5484d;",
    "  --warn: #c2740a;",
    "  --track-off: #d8dce3;",
    "  --radius: 6px;",
    "}",
    "",
    '[data-theme="dark"] {',
    "  --bg: #12141a;",
    "  --card: #1c1f28;",
    "  --text: #eceef3;",
    "  --muted: #9aa1b2;",
    "  --border: #2a2e3a;",
    "  --shadow: 0 8px 30px rgba(0, 0, 0, 0.4);",
    "  --accent: #7b92ff;",
    "  --accent-soft: rgba(123, 146, 255, 0.14);",
    "  --warn: #f0b543;",
    "  --track-off: #3a4050;",
    "  --radius: 6px;",
    "}"
  ].join("\n");

  var ARROW_L = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5M11 18l-6-6 6-6"/></svg>';
  var CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg>';

  function clean(text) {
    return (text || "").replace(/[ \t]+$/gm, "").replace(/\s+$/, "");
  }

  function copyText(text) {
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(text);
    }
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

  function buildPanel(block) {
    var stage = block.querySelector(".vw-stage");
    var frame = block.querySelector(".vw-frame");
    var tools = block.querySelector(".vw-tools");
    if (!stage || !frame || !tools) return null;

    var styles = Array.prototype.map.call(block.querySelectorAll("style"), function (s) {
      return s.textContent;
    }).join("\n\n");
    var jsNode = block.querySelector("script[data-block]");
    var htmlCode = clean(frame.innerHTML);
    var cssCode = clean(styles);
    var jsCode = jsNode ? clean(jsNode.textContent) : "";
    var usesTokens = /var\(--/.test(htmlCode + cssCode);

    var codeBtn = document.createElement("button");
    codeBtn.type = "button";
    codeBtn.className = "vw-btn";
    codeBtn.setAttribute("aria-expanded", "false");
    codeBtn.textContent = "View Code";
    tools.appendChild(codeBtn);

    var panes = {};
    var tabDefs = [["html", "HTML"], ["css", "CSS"], ["js", "JS"]];
    if (usesTokens) tabDefs.push(["tokens", "Tokens"]);
    var texts = { html: htmlCode, css: cssCode, js: jsCode, tokens: TOKENS };

    var panel = document.createElement("div");
    panel.className = "vw-code";
    panel.hidden = true;

    var tabsBar = document.createElement("div");
    tabsBar.className = "vw-tabs";
    tabsBar.setAttribute("role", "tablist");

    var copyBtn = document.createElement("button");
    copyBtn.type = "button";
    copyBtn.className = "vw-copy";
    copyBtn.innerHTML = "Copy " + CHECK;
    copyBtn.setAttribute("aria-label", "Copy code of this component");

    var active = "html";

    tabDefs.forEach(function (def, i) {
      var key = def[0];
      var tab = document.createElement("button");
      tab.type = "button";
      tab.className = "vw-tab";
      tab.textContent = def[1];
      tab.setAttribute("role", "tab");
      tab.setAttribute("aria-selected", key === active ? "true" : "false");
      tab.tabIndex = key === active ? 0 : -1;

      var pre = document.createElement("pre");
      pre.className = "vw-pre";
      var code = document.createElement("code");
      code.textContent = texts[key];
      pre.appendChild(code);
      pre.hidden = key !== active;

      tab.addEventListener("click", function () { select(key); });
      tab.addEventListener("keydown", function (e) {
        if (e.key !== "ArrowRight" && e.key !== "ArrowLeft") return;
        e.preventDefault();
        var idx = tabDefs.findIndex(function (d) { return d[0] === active; });
        var next = (idx + (e.key === "ArrowRight" ? 1 : -1) + tabDefs.length) % tabDefs.length;
        select(tabDefs[next][0]);
        tabsBar.querySelectorAll(".vw-tab")[next].focus();
      });

      panes[key] = { tab: tab, pre: pre };
      tabsBar.appendChild(tab);
      panel.appendChild(pre);
    });

    function select(key) {
      active = key;
      tabDefs.forEach(function (def) {
        var p = panes[def[0]];
        p.tab.setAttribute("aria-selected", def[0] === key ? "true" : "false");
        p.tab.tabIndex = def[0] === key ? 0 : -1;
        p.pre.hidden = def[0] !== key;
      });
      copyBtn.classList.remove("is-done");
      copyBtn.innerHTML = "Copy " + CHECK;
    }

    tabsBar.appendChild(copyBtn);
    panel.appendChild(tabsBar);

    var tip = document.createElement("div");
    tip.className = "vw-tip";
    tip.textContent = "Copy kiya gaya code sirf is component ka hai (viewer chrome shamil nahi). Tokens tab se project ke CSS variables le lein.";
    panel.appendChild(tip);

    copyBtn.addEventListener("click", function () {
      copyText(texts[active]).then(function () {
        copyBtn.classList.add("is-done");
        copyBtn.textContent = "Copied!";
        setTimeout(function () {
          copyBtn.classList.remove("is-done");
          copyBtn.innerHTML = "Copy " + CHECK;
        }, 1600);
      }).catch(function () {
        copyBtn.textContent = "Select & copy";
        var pre = panes[active].pre;
        var range = document.createRange();
        range.selectNodeContents(pre);
        var sel = window.getSelection();
        sel.removeAllRanges();
        sel.addRange(range);
      });
    });

    codeBtn.addEventListener("click", function () {
      var open = panel.hidden;
      panel.hidden = !open;
      codeBtn.setAttribute("aria-expanded", String(open));
      codeBtn.textContent = open ? "Hide Code" : "View Code";
      codeBtn.classList.toggle("is-on", open);
      if (open) panes[active].tab.focus();
    });

    stage.insertAdjacentElement("afterend", panel);
    return panel;
  }

  function initBlock(block) {
    var tools = block.querySelector(".vw-tools");
    var stage = block.querySelector(".vw-stage");
    if (!tools || !stage) return;

    buildPanel(block);

    var seg = tools.querySelectorAll(".vw-seg button");
    seg.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var mobile = btn.dataset.size === "mobile";
        block.classList.toggle("vw-mobile", mobile);
        seg.forEach(function (b) {
          b.setAttribute("aria-pressed", String((b.dataset.size === "mobile") === mobile));
        });
      });
    });
  }

  function initTheme() {
    var btn = document.getElementById("vwTheme");
    if (!btn) return;
    btn.addEventListener("click", function () {
      var root = document.documentElement;
      var next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("theme", next); } catch (e) {}
    });
  }

  function init() {
    initTheme();
    document.querySelectorAll(".vw-block").forEach(initBlock);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
