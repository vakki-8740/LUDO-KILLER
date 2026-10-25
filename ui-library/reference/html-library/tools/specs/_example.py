CAT = "Smoke"
CAT_ID = "system"
CAT_DESC = "Smoke test section."

PAGES = [
    {
        "folder": "system",
        "slug": "smoke-test",
        "title": "Smoke Test",
        "desc": "Temporary pipeline check.",
        "idx_desc": "Temporary pipeline check.",
        "mini": '<div class="p-row" style="gap: 6px;"><span class="p-pill"></span><span class="p-pill"></span></div>',
        "blocks": [
            {
                "id": "smoke-pill",
                "title": "Pill button",
                "html": '<div class="sk-wrap"><button class="sk-pill" type="button" id="skBtn">Click me <span id="skCount">0</span></button></div>',
                "css": """.sk-wrap { display: flex; justify-content: center; }
.sk-pill {
  border: 1px solid var(--border);
  background: var(--card);
  color: var(--text);
  font: inherit;
  font-weight: 600;
  font-size: 0.9rem;
  padding: 10px 18px;
  border-radius: 999px;
  cursor: pointer;
  transition: border-color 0.2s, color 0.2s;
}
.sk-pill:hover { border-color: var(--accent); color: var(--accent); }
.sk-pill:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }""",
                "js": """var btn = document.getElementById("skBtn");
var count = document.getElementById("skCount");
var n = 0;
btn.addEventListener("click", function () {
  n += 1;
  count.textContent = String(n);
});""",
            },
        ],
    },
]
