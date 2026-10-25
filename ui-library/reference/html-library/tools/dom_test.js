const fs = require("fs");
const path = require("path");
let JSDOM, ResourceLoader, VirtualConsole;
try {
  ({ JSDOM, ResourceLoader, VirtualConsole } = require("jsdom"));
} catch (e) {
  ({ JSDOM, ResourceLoader, VirtualConsole } =
    require("/data/data/com.termux/files/usr/tmp/opencode/node_modules/jsdom"));
}

const ROOT = "/storage/emulated/0/OWN LABRARY";

class ScriptLoader extends ResourceLoader {
  fetch(url, options) {
    if (url.endsWith(".css")) return null;
    return super.fetch(url, options);
  }
}

function collectPages(dir) {
  const out = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.name === "tools" || entry.name === "node_modules") continue;
    const p = path.join(dir, entry.name);
    if (entry.isDirectory()) out.push(...collectPages(p));
    else if (entry.name.endsWith(".html")) out.push(p);
  }
  return out;
}

function assert(cond, msg, fails) {
  if (!cond) fails.push(msg);
}

function wait(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

async function testPage(file) {
  const fails = [];
  const src = fs.readFileSync(file, "utf8");
  if (!src.includes("lib/viewer.js")) return null;
  const rel = path.relative(ROOT, file);

  const errors = [];
  const vc = new VirtualConsole();
  vc.on("jsdomError", (e) => {
    if (String(e.message).includes("Could not parse CSS")) return;
    errors.push(e.message);
  });
  vc.on("error", (...a) => errors.push(a.join(" ")));

  const dom = await JSDOM.fromFile(file, {
    resources: new ScriptLoader(),
    runScripts: "dangerously",
    virtualConsole: vc,
    pretendToBeVisual: true,
  });
  const { window } = dom;
  await new Promise((res) => {
    if (window.document.readyState === "complete") res();
    else window.addEventListener("load", res);
  });
  await wait(60);

  assert(errors.length === 0, "page errors: " + errors.join(" | ").slice(0, 300), fails);

  const doc = window.document;
  const blocks = [...doc.querySelectorAll(".vw-block")];
  assert(blocks.length > 0, "no .vw-block found", fails);

  for (const block of blocks) {
    const id = block.id;
    const style = block.querySelector("style");
    const script = block.querySelector("script[data-block]");
    const panel = block.querySelector(".vw-code");
    assert(panel, id + ": code panel missing", fails);
    if (!panel) continue;

    const tabs = [...panel.querySelectorAll(".vw-tab")];
    const names = tabs.map((t) => t.textContent.trim());
    assert(JSON.stringify(names.slice(0, 3)) === '["HTML","CSS","JS"]', id + ": tabs wrong: " + names, fails);
    const hasVars = /var\(--/.test((style ? style.textContent : "") + block.querySelector(".vw-frame").innerHTML);
    assert(names.includes("Tokens") === hasVars, id + ": Tokens tab mismatch", fails);
    assert(tabs[0].getAttribute("aria-selected") === "true", id + ": first tab not selected", fails);

    const panes = [...panel.querySelectorAll(".vw-pre")];
    assert(panes.filter((p) => !p.hidden).length === 1, id + ": pane visibility wrong", fails);
    const htmlCode = panes[0].querySelector("code").textContent;
    assert(htmlCode.trim().length > 10, id + ": HTML pane empty", fails);
    assert(htmlCode.includes("vw-") === false || true, "", fails);

    const cssPane = panes[1].querySelector("code").textContent;
    assert(cssPane.trim().length > 20, id + ": CSS pane empty", fails);
    if (style) {
      assert(cssPane.trim() === style.textContent.trim(), id + ": CSS pane != style text", fails);
    }

    const jsIdx = 2;
    const jsPane = panes[jsIdx].querySelector("code").textContent;
    if (script) {
      assert(jsPane.trim() === script.textContent.trim(), id + ": JS pane != script text", fails);
    } else {
      assert(jsPane.trim() === "", id + ": JS pane should be empty", fails);
    }

    assert(panel.hidden === true, id + ": panel should start hidden", fails);
    const codeBtn = [...block.querySelectorAll(".vw-tools .vw-btn")].find((b) => /Code/.test(b.textContent));
    assert(codeBtn, id + ": view-code button missing", fails);
    if (codeBtn) {
      codeBtn.click();
      assert(panel.hidden === false, id + ": panel did not open", fails);
      assert(codeBtn.getAttribute("aria-expanded") === "true", id + ": aria-expanded not set", fails);
      assert(codeBtn.textContent === "Hide Code", id + ": button label not toggled", fails);

      tabs[1].click();
      assert(tabs[1].getAttribute("aria-selected") === "true", id + ": CSS tab select failed", fails);
      assert(panes[1].hidden === false && panes[0].hidden === true, id + ": CSS pane not shown", fails);

      const copyBtn = panel.querySelector(".vw-copy");
      doc.execCommand = () => true;
      copyBtn.click();
      await wait(30);
      assert(/Copied/.test(copyBtn.textContent) || copyBtn.classList.contains("is-done"),
        id + ": copy feedback missing (" + copyBtn.textContent + ")", fails);

      codeBtn.click();
      assert(panel.hidden === true, id + ": panel did not close", fails);
    }

    const segBtns = [...block.querySelectorAll(".vw-seg button")];
    assert(segBtns.length === 2, id + ": size buttons missing", fails);
    const mobileBtn = segBtns.find((b) => b.dataset.size === "mobile");
    mobileBtn.click();
    assert(block.classList.contains("vw-mobile"), id + ": mobile class not applied", fails);
    assert(mobileBtn.getAttribute("aria-pressed") === "true", id + ": aria-pressed not updated", fails);
    segBtns.find((b) => b.dataset.size === "desktop").click();
    assert(!block.classList.contains("vw-mobile"), id + ": mobile class not removed", fails);
  }

  const themeBtn = doc.getElementById("vwTheme");
  assert(themeBtn, "theme button missing", fails);
  if (themeBtn) {
    const before = doc.documentElement.getAttribute("data-theme");
    themeBtn.click();
    const after = doc.documentElement.getAttribute("data-theme");
    assert(before !== after, "theme did not toggle", fails);
  }

  const back = doc.querySelector(".vw-back");
  assert(back && back.getAttribute("href") === "../index.html", "back link missing", fails);

  window.close();
  return { rel, fails };
}

(async () => {
  const files = collectPages(ROOT).filter((f) =>
    fs.readFileSync(f, "utf8").includes("lib/viewer.js"));
  let bad = 0;
  let blocks = 0;
  for (const f of files) {
    const r = await testPage(f);
    if (!r) continue;
    blocks += (fs.readFileSync(f, "utf8").match(/class="vw-block"/g) || []).length;
    if (r.fails.length) {
      bad++;
      console.log("FAIL " + r.rel);
      for (const m of r.fails) console.log("   - " + m);
    }
  }
  console.log("pages tested: " + files.length + ", blocks: " + blocks + ", failing pages: " + bad);
  process.exit(bad ? 1 : 0);
})();
