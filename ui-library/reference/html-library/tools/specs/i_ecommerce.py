CAT = "E-commerce"
CAT_ID = "ecommerce"

PAGES = [
 {
  "folder": "ecommerce", "slug": "product-card", "title": "Product Card",
  "desc": "Product tile with badge, rating and add action.",
  "idx_desc": "Product tile with badge, rating and add action.",
  "mini": '<div class="p-card" style="width: 34px; height: 40px;"></div><div class="p-line" style="width: 26px;"></div>',
  "blocks": [{
   "id": "product-card", "title": "Product cards",
   "html": '''<div class="pc-grid">
  <article class="pc-card">
    <div class="pc-art pc-a"><span class="pc-badge">-20%</span><button class="pc-heart" type="button" aria-label="Save Ceramic mug" aria-pressed="false">&#9825;</button></div>
    <div class="pc-body">
      <p class="pc-cat">Home</p>
      <p class="pc-name">Ceramic mug</p>
      <p class="pc-rate"><span class="pc-star">&#9733;</span> 4.8 <span class="pc-rev">(124)</span></p>
      <div class="pc-buy"><span class="pc-price">$18.00</span><span class="pc-old">$22.50</span><button class="pc-add" type="button">Add</button></div>
    </div>
  </article>
  <article class="pc-card">
    <div class="pc-art pc-b"><span class="pc-badge is-new">New</span><button class="pc-heart" type="button" aria-label="Save Canvas tote" aria-pressed="false">&#9825;</button></div>
    <div class="pc-body">
      <p class="pc-cat">Bags</p>
      <p class="pc-name">Canvas tote</p>
      <p class="pc-rate"><span class="pc-star">&#9733;</span> 4.6 <span class="pc-rev">(89)</span></p>
      <div class="pc-buy"><span class="pc-price">$26.00</span><button class="pc-add" type="button">Add</button></div>
    </div>
  </article>
</div>
<p class="pc-msg" id="pcMsg" aria-live="polite"></p>''',
   "css": '''.pc-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; max-width: 380px; }
.pc-card { border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); overflow: hidden; }
.pc-art { position: relative; height: 110px; display: flex; align-items: center; justify-content: center; }
.pc-a { background: linear-gradient(140deg, #e8d5c4, #c98b5e 65%, #6b3d10); }
.pc-b { background: linear-gradient(140deg, #d6e4d2, #6aa87a 65%, #23503a); }
.pc-badge { position: absolute; top: 7px; left: 7px; font-size: 0.56rem; font-weight: 800; color: #fff; background: var(--no); border-radius: 999px; padding: 2px 7px; }
.pc-badge.is-new { background: var(--yes); }
.pc-heart { position: absolute; top: 6px; right: 6px; width: 24px; height: 24px; border-radius: 999px; border: 0; background: rgba(255, 255, 255, 0.88); color: #6b7280; font-size: 0.8rem; cursor: pointer; line-height: 1; }
.pc-heart.is-on { color: var(--no); }
.pc-heart:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.pc-body { padding: 8px; }
.pc-cat { margin: 0; font-size: 0.54rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; color: var(--muted); }
.pc-name { margin: 1px 0 2px; font-size: 0.76rem; font-weight: 700; }
.pc-rate { margin: 0; font-size: 0.6rem; color: var(--muted); }
.pc-star { color: #f0b543; }
.pc-rev { color: var(--muted); }
.pc-buy { display: flex; align-items: center; gap: 5px; margin-top: 6px; }
.pc-price { font-size: 0.8rem; font-weight: 800; }
.pc-old { font-size: 0.6rem; color: var(--muted); text-decoration: line-through; }
.pc-add { margin-left: auto; border: 0; background: var(--accent); color: #fff; font: inherit; font-size: 0.6rem; font-weight: 700; padding: 4px 9px; border-radius: 999px; cursor: pointer; }
.pc-add:hover { opacity: 0.92; }
.pc-add:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.pc-msg { min-height: 1em; margin: 7px 0 0; font-size: 0.66rem; color: var(--yes); }''',
   "js": '''(function () {
  var msg = document.getElementById("pcMsg");
  document.querySelectorAll(".pc-add").forEach(function (b) {
    b.addEventListener("click", function () {
      var card = b.closest(".pc-card");
      msg.textContent = card.querySelector(".pc-name").textContent + " added to cart.";
    });
  });
  document.querySelectorAll(".pc-heart").forEach(function (h) {
    h.addEventListener("click", function () {
      var on = h.classList.toggle("is-on");
      h.setAttribute("aria-pressed", String(on));
      h.innerHTML = on ? "&#9829;" : "&#9825;";
    });
  });
})();''',
  }],
 },
 {
  "folder": "ecommerce", "slug": "product-details", "title": "Product Details",
  "desc": "Gallery, color and size selectors with quantity.",
  "idx_desc": "Gallery with color, size and quantity selectors.",
  "mini": '<div class="p-gal" style="grid-template-columns: 1fr 1fr;"><span style="height: 20px;"></span><span style="height: 20px;"></span><span style="height: 20px;"></span><span style="height: 20px;"></span></div>',
  "blocks": [{
   "id": "product-details", "title": "Product page",
   "html": '''<div class="pd-wrap">
  <div class="pd-gallery">
    <div class="pd-main pd-mainA" id="pdMain" role="img" aria-label="Sneaker product photo"></div>
    <div class="pd-thumbs" role="group" aria-label="Product photos">
      <button class="pd-thumb pd-tA is-on" type="button" data-g="pd-mainA" aria-label="View photo 1"></button>
      <button class="pd-thumb pd-tB" type="button" data-g="pd-mainB" aria-label="View photo 2"></button>
      <button class="pd-thumb pd-tC" type="button" data-g="pd-mainC" aria-label="View photo 3"></button>
    </div>
  </div>
  <div class="pd-info">
    <p class="pd-brand">OWN Goods</p>
    <h4 class="pd-name">Court low sneaker</h4>
    <p class="pd-price">$86.00 <span class="pd-old">$110.00</span></p>
    <p class="pd-label">Color: <span id="pdColor">Sand</span></p>
    <div class="pd-colors" role="group" aria-label="Color">
      <button class="pd-color is-on" type="button" data-c="Sand" style="background: #d8c3a5;" aria-label="Sand"></button>
      <button class="pd-color" type="button" data-c="Ink" style="background: #2b2f3a;" aria-label="Ink"></button>
      <button class="pd-color" type="button" data-c="Sage" style="background: #8fa88b;" aria-label="Sage"></button>
    </div>
    <p class="pd-label">Size</p>
    <div class="pd-sizes" role="group" aria-label="Size">
      <button class="pd-size" type="button">7</button>
      <button class="pd-size is-on" type="button">8</button>
      <button class="pd-size" type="button">9</button>
      <button class="pd-size" type="button">10</button>
    </div>
    <div class="pd-row">
      <div class="pd-qty">
        <button class="pd-qb" type="button" id="pdMinus" aria-label="Decrease quantity">&minus;</button>
        <span class="pd-qv" id="pdQty">1</span>
        <button class="pd-qb" type="button" id="pdPlus" aria-label="Increase quantity">+</button>
      </div>
      <button class="pd-cart" type="button" id="pdCart">Add to cart</button>
    </div>
    <p class="pd-msg" id="pdMsg" role="status"></p>
  </div>
</div>''',
   "css": '''.pd-wrap { display: grid; grid-template-columns: 1fr 1.2fr; gap: 12px; max-width: 440px; }
.pd-gallery { min-width: 0; }
.pd-main { height: 150px; border-radius: var(--radius); border: 1px solid var(--border); }
.pd-mainA { background: linear-gradient(140deg, #f0e2cf, #d8c3a5 62%, #9c7b55); }
.pd-mainB { background: linear-gradient(140deg, #c9ccd6, #2b2f3a 65%, #12141a); }
.pd-mainC { background: linear-gradient(140deg, #dfe8da, #8fa88b 62%, #4c6b4f); }
.pd-thumbs { display: flex; gap: 5px; margin-top: 5px; }
.pd-thumb { flex: 1; height: 30px; border-radius: 3px; border: 1px solid var(--border); cursor: pointer; padding: 0; }
.pd-thumb.is-on { box-shadow: 0 0 0 2px var(--accent); }
.pd-thumb:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.pd-tA { background: linear-gradient(140deg, #f0e2cf, #d8c3a5); }
.pd-tB { background: linear-gradient(140deg, #c9ccd6, #2b2f3a); }
.pd-tC { background: linear-gradient(140deg, #dfe8da, #8fa88b); }
.pd-info { min-width: 0; }
.pd-brand { margin: 0; font-size: 0.54rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--muted); }
.pd-name { margin: 1px 0 2px; font-size: 0.92rem; }
.pd-price { margin: 0 0 7px; font-size: 0.82rem; font-weight: 800; color: var(--accent); }
.pd-old { font-size: 0.62rem; font-weight: 500; color: var(--muted); text-decoration: line-through; margin-left: 3px; }
.pd-label { margin: 0 0 4px; font-size: 0.6rem; font-weight: 600; color: var(--muted); }
.pd-label span { color: var(--text); }
.pd-colors { display: flex; gap: 5px; margin-bottom: 8px; }
.pd-color { width: 18px; height: 18px; border-radius: 999px; border: 2px solid var(--card); box-shadow: 0 0 0 1px var(--border); cursor: pointer; padding: 0; }
.pd-color.is-on { box-shadow: 0 0 0 2px var(--accent); }
.pd-color:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.pd-sizes { display: flex; gap: 4px; margin-bottom: 8px; }
.pd-size { width: 26px; height: 26px; border: 1px solid var(--border); border-radius: 4px; background: var(--card); color: var(--text); font: inherit; font-size: 0.62rem; font-weight: 600; cursor: pointer; }
.pd-size.is-on { background: var(--accent); border-color: var(--accent); color: #fff; }
.pd-size:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.pd-row { display: flex; gap: 6px; align-items: center; }
.pd-qty { display: flex; align-items: center; border: 1px solid var(--border); border-radius: 4px; }
.pd-qb { width: 24px; height: 28px; border: 0; background: transparent; color: var(--muted); font: inherit; font-size: 0.8rem; cursor: pointer; }
.pd-qb:hover { color: var(--accent); }
.pd-qb:focus-visible { outline: 2px solid var(--accent); outline-offset: -2px; }
.pd-qv { min-width: 18px; text-align: center; font-size: 0.68rem; font-weight: 700; }
.pd-cart { flex: 1; border: 0; background: var(--accent); color: #fff; font: inherit; font-size: 0.68rem; font-weight: 700; padding: 8px; border-radius: 4px; cursor: pointer; }
.pd-cart:hover { opacity: 0.92; }
.pd-cart:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.pd-msg { min-height: 1em; margin: 6px 0 0; font-size: 0.62rem; color: var(--yes); }
@media (max-width: 430px) { .pd-wrap { grid-template-columns: 1fr; } .pd-main { height: 120px; } }''',
   "js": '''(function () {
  var qty = 1;
  var out = document.getElementById("pdQty");
  var msg = document.getElementById("pdMsg");

  document.getElementById("pdMinus").addEventListener("click", function () {
    qty = Math.max(1, qty - 1);
    out.textContent = qty;
  });
  document.getElementById("pdPlus").addEventListener("click", function () {
    qty = Math.min(9, qty + 1);
    out.textContent = qty;
  });

  document.querySelectorAll(".pd-size").forEach(function (b) {
    b.addEventListener("click", function () {
      document.querySelectorAll(".pd-size").forEach(function (x) { x.classList.remove("is-on"); });
      b.classList.add("is-on");
    });
  });

  document.querySelectorAll(".pd-color").forEach(function (b) {
    b.addEventListener("click", function () {
      document.querySelectorAll(".pd-color").forEach(function (x) { x.classList.remove("is-on"); });
      b.classList.add("is-on");
      document.getElementById("pdColor").textContent = b.getAttribute("data-c");
    });
  });

  document.querySelectorAll(".pd-thumb").forEach(function (t) {
    t.addEventListener("click", function () {
      document.querySelectorAll(".pd-thumb").forEach(function (x) { x.classList.remove("is-on"); });
      t.classList.add("is-on");
      document.getElementById("pdMain").className = "pd-main " + t.getAttribute("data-g");
    });
  });

  document.getElementById("pdCart").addEventListener("click", function () {
    msg.textContent = qty + " item(s) added to cart.";
  });
})();''',
  }],
 },
 {
  "folder": "ecommerce", "slug": "cart", "title": "Shopping Cart",
  "desc": "Cart lines with quantity steppers and live total.",
  "idx_desc": "Cart lines with quantity steppers and live total.",
  "mini": '<div class="p-row"><span class="p-box"></span><span class="p-line" style="width: 30px;"></span></div>',
  "blocks": [{
   "id": "cart", "title": "Cart drawer content",
   "html": '''<div class="ca-card">
  <div class="ca-head"><span class="ca-t">Your cart</span><span class="ca-n" id="caCount">2 items</span></div>
  <ul class="ca-list" id="caList">
    <li class="ca-item" data-price="18">
      <span class="ca-art ca-a" aria-hidden="true"></span>
      <div class="ca-m"><p class="ca-nm">Ceramic mug</p><p class="ca-v">Sand</p></div>
      <div class="ca-qty">
        <button class="ca-q" type="button" aria-label="Decrease Ceramic mug quantity">&minus;</button>
        <span class="ca-qv">1</span>
        <button class="ca-q" type="button" aria-label="Increase Ceramic mug quantity">+</button>
      </div>
      <span class="ca-p">$18.00</span>
      <button class="ca-x" type="button" aria-label="Remove Ceramic mug">&times;</button>
    </li>
    <li class="ca-item" data-price="26">
      <span class="ca-art ca-b" aria-hidden="true"></span>
      <div class="ca-m"><p class="ca-nm">Canvas tote</p><p class="ca-v">Natural</p></div>
      <div class="ca-qty">
        <button class="ca-q" type="button" aria-label="Decrease Canvas tote quantity">&minus;</button>
        <span class="ca-qv">1</span>
        <button class="ca-q" type="button" aria-label="Increase Canvas tote quantity">+</button>
      </div>
      <span class="ca-p">$26.00</span>
      <button class="ca-x" type="button" aria-label="Remove Canvas tote">&times;</button>
    </li>
  </ul>
  <p class="ca-empty" id="caEmpty" hidden>Your cart is empty.</p>
  <div class="ca-foot">
    <div class="ca-total"><span class="ca-tl">Subtotal</span><span class="ca-tv" id="caTotal">$44.00</span></div>
    <button class="ca-checkout" type="button">Checkout</button>
  </div>
</div>''',
   "css": '''.ca-card { max-width: 380px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 12px; }
.ca-head { display: flex; align-items: center; justify-content: space-between; margin-bottom: 7px; }
.ca-t { font-size: 0.82rem; font-weight: 700; }
.ca-n { font-size: 0.62rem; color: var(--muted); }
.ca-list { list-style: none; margin: 0; padding: 0; }
.ca-item { display: flex; align-items: center; gap: 7px; padding: 8px 0; border-bottom: 1px solid var(--border); }
.ca-art { width: 34px; height: 38px; border-radius: 4px; flex: 0 0 auto; }
.ca-a { background: linear-gradient(140deg, #e8d5c4, #c98b5e 65%, #6b3d10); }
.ca-b { background: linear-gradient(140deg, #d6e4d2, #6aa87a 65%, #23503a); }
.ca-m { flex: 1; min-width: 0; }
.ca-nm { margin: 0; font-size: 0.68rem; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.ca-v { margin: 1px 0 0; font-size: 0.56rem; color: var(--muted); }
.ca-qty { display: flex; align-items: center; border: 1px solid var(--border); border-radius: 3px; }
.ca-q { width: 17px; height: 20px; border: 0; background: transparent; color: var(--muted); font-size: 0.7rem; cursor: pointer; line-height: 1; padding: 0; }
.ca-q:hover { color: var(--accent); }
.ca-q:focus-visible { outline: 2px solid var(--accent); outline-offset: -2px; }
.ca-qv { min-width: 14px; text-align: center; font-size: 0.58rem; font-weight: 700; }
.ca-p { font-size: 0.64rem; font-weight: 700; white-space: nowrap; }
.ca-x { border: 0; background: transparent; color: var(--muted); font-size: 0.8rem; cursor: pointer; padding: 1px 3px; border-radius: 2px; line-height: 1; }
.ca-x:hover { color: var(--no); }
.ca-x:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.ca-empty { margin: 10px 0; font-size: 0.7rem; color: var(--muted); text-align: center; }
.ca-foot { margin-top: 9px; }
.ca-total { display: flex; align-items: center; justify-content: space-between; margin-bottom: 7px; }
.ca-tl { font-size: 0.66rem; color: var(--muted); }
.ca-tv { font-size: 0.86rem; font-weight: 800; }
.ca-checkout { width: 100%; border: 0; background: var(--accent); color: #fff; font: inherit; font-size: 0.72rem; font-weight: 700; padding: 8px; border-radius: 4px; cursor: pointer; }
.ca-checkout:hover { opacity: 0.92; }
.ca-checkout:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }''',
   "js": '''(function () {
  var list = document.getElementById("caList");
  var totalEl = document.getElementById("caTotal");
  var countEl = document.getElementById("caCount");
  var empty = document.getElementById("caEmpty");

  function paint() {
    var items = Array.prototype.slice.call(list.querySelectorAll(".ca-item"));
    var total = 0;
    var units = 0;
    items.forEach(function (it) {
      var q = Number(it.querySelector(".ca-qv").textContent);
      var price = Number(it.getAttribute("data-price"));
      total += q * price;
      units += q;
      it.querySelector(".ca-p").textContent = "$" + (q * price).toFixed(2);
    });
    totalEl.textContent = "$" + total.toFixed(2);
    countEl.textContent = units + " item" + (units === 1 ? "" : "s");
    empty.hidden = items.length > 0;
    list.hidden = items.length === 0;
  }

  list.addEventListener("click", function (e) {
    var item = e.target.closest(".ca-item");
    if (!item) return;
    var qv = item.querySelector(".ca-qv");
    if (e.target.classList.contains("ca-q")) {
      var plus = e.target.textContent === "+";
      qv.textContent = Math.max(1, Number(qv.textContent) + (plus ? 1 : -1));
      paint();
    }
    if (e.target.classList.contains("ca-x")) {
      item.remove();
      paint();
    }
  });

  paint();
})();''',
  }],
 },
 {
  "folder": "ecommerce", "slug": "checkout", "title": "Checkout Form",
  "desc": "Shipping and payment sections with order action.",
  "idx_desc": "Shipping and payment checkout form.",
  "mini": '<div class="p-page" style="height: 46px;"><span class="p-line" style="width: 44px;"></span><span class="p-line" style="width: 30px;"></span></div>',
  "blocks": [{
   "id": "checkout-form", "title": "Checkout",
   "html": '''<div class="co-card">
  <p class="co-t">Checkout</p>
  <div class="co-sec">
    <p class="co-st"><span class="co-sn">1</span>Shipping address</p>
    <div class="co-grid">
      <input class="co-in" type="text" placeholder="First name" aria-label="First name">
      <input class="co-in" type="text" placeholder="Last name" aria-label="Last name">
    </div>
    <input class="co-in" type="text" placeholder="Street address" aria-label="Street address">
    <div class="co-grid">
      <input class="co-in" type="text" placeholder="City" aria-label="City">
      <input class="co-in" type="text" placeholder="PIN code" aria-label="PIN code">
    </div>
  </div>
  <div class="co-sec">
    <p class="co-st"><span class="co-sn">2</span>Payment</p>
    <div class="co-pay">
      <label class="co-opt"><input class="co-radio" type="radio" name="coPay" checked> Card ending 4242</label>
      <label class="co-opt"><input class="co-radio" type="radio" name="coPay"> UPI</label>
      <label class="co-opt"><input class="co-radio" type="radio" name="coPay"> Cash on delivery</label>
    </div>
  </div>
  <div class="co-total"><span class="co-tl">Total</span><span class="co-tv">$148.00</span></div>
  <button class="co-place" type="button" id="coPlace">Place order</button>
  <p class="co-msg" id="coMsg" role="status"></p>
</div>''',
   "css": '''.co-card { max-width: 380px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 14px; }
.co-t { margin: 0 0 10px; font-size: 0.88rem; font-weight: 800; }
.co-sec { margin-bottom: 12px; }
.co-st { display: flex; align-items: center; gap: 6px; margin: 0 0 7px; font-size: 0.68rem; font-weight: 700; }
.co-sn { width: 16px; height: 16px; border-radius: 999px; background: var(--accent-soft); color: var(--accent); font-size: 0.56rem; display: flex; align-items: center; justify-content: center; }
.co-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 6px; }
.co-in { width: 100%; border: 1px solid var(--border); border-radius: 4px; background: var(--bg); color: var(--text); font: inherit; font-size: 0.7rem; padding: 7px 8px; margin-bottom: 6px; outline: none; min-width: 0; }
.co-in:focus { border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-soft); }
.co-pay { display: flex; flex-direction: column; gap: 4px; }
.co-opt { display: flex; align-items: center; gap: 6px; border: 1px solid var(--border); border-radius: 4px; padding: 7px 8px; font-size: 0.68rem; cursor: pointer; }
.co-opt:hover { border-color: var(--accent); }
.co-radio { accent-color: var(--accent); width: 13px; height: 13px; }
.co-total { display: flex; align-items: center; justify-content: space-between; padding: 8px 0; border-top: 1px solid var(--border); margin-bottom: 8px; }
.co-tl { font-size: 0.68rem; color: var(--muted); }
.co-tv { font-size: 0.92rem; font-weight: 800; }
.co-place { width: 100%; border: 0; background: var(--accent); color: #fff; font: inherit; font-size: 0.76rem; font-weight: 700; padding: 9px; border-radius: 4px; cursor: pointer; }
.co-place:hover { opacity: 0.92; }
.co-place:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.co-msg { min-height: 1em; margin: 7px 0 0; font-size: 0.64rem; color: var(--yes); text-align: center; }''',
   "js": '''(function () {
  var msg = document.getElementById("coMsg");
  document.getElementById("coPlace").addEventListener("click", function () {
    var missing = false;
    document.querySelectorAll(".co-in").forEach(function (i) {
      if (!i.value.trim()) missing = true;
    });
    if (missing) {
      msg.textContent = "Please fill in every shipping field.";
      msg.style.color = "var(--no)";
      return;
    }
    msg.textContent = "Order placed (demo). Confirmation sent.";
    msg.style.color = "var(--yes)";
  });
})();''',
  }],
 },
 {
  "folder": "ecommerce", "slug": "order-summary", "title": "Order Summary",
  "desc": "Compact summary with items, shipping and total.",
  "idx_desc": "Compact summary with items, shipping and total.",
  "mini": '<div class="p-line" style="width: 40px;"></div><div class="p-line" style="width: 28px; border-color: var(--accent);"></div>',
  "blocks": [{
   "id": "order-summary", "title": "Summary card",
   "html": '''<div class="os-card">
  <p class="os-t">Order summary</p>
  <ul class="os-list">
    <li class="os-item"><span class="os-art os-a" aria-hidden="true"></span><span class="os-n">Ceramic mug <span class="os-q">x1</span></span><span class="os-p">$18.00</span></li>
    <li class="os-item"><span class="os-art os-b" aria-hidden="true"></span><span class="os-n">Canvas tote <span class="os-q">x1</span></span><span class="os-p">$26.00</span></li>
    <li class="os-item"><span class="os-art os-c" aria-hidden="true"></span><span class="os-n">Notebook set <span class="os-q">x2</span></span><span class="os-p">$24.00</span></li>
  </ul>
  <div class="os-lines">
    <div class="os-line"><span class="os-k">Subtotal</span><span class="os-v">$68.00</span></div>
    <div class="os-line"><span class="os-k">Shipping</span><span class="os-v is-free">Free</span></div>
    <div class="os-line"><span class="os-k">Tax</span><span class="os-v">$5.44</span></div>
  </div>
  <div class="os-total"><span class="os-tk">Total</span><span class="os-tv">$73.44</span></div>
  <button class="os-promo" type="button">Have a promo code?</button>
</div>''',
   "css": '''.os-card { max-width: 340px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 13px; }
.os-t { margin: 0 0 8px; font-size: 0.8rem; font-weight: 700; }
.os-list { list-style: none; margin: 0 0 9px; padding: 0; }
.os-item { display: flex; align-items: center; gap: 7px; padding: 5px 0; border-bottom: 1px solid var(--border); }
.os-art { width: 26px; height: 28px; border-radius: 3px; flex: 0 0 auto; }
.os-a { background: linear-gradient(140deg, #e8d5c4, #c98b5e); }
.os-b { background: linear-gradient(140deg, #d6e4d2, #6aa87a); }
.os-c { background: linear-gradient(140deg, #d9e2f4, #4f6bed); }
.os-n { flex: 1; font-size: 0.66rem; font-weight: 600; }
.os-q { color: var(--muted); font-weight: 500; }
.os-p { font-size: 0.64rem; font-weight: 700; }
.os-lines { padding-top: 3px; }
.os-line { display: flex; justify-content: space-between; padding: 3px 0; }
.os-k { font-size: 0.64rem; color: var(--muted); }
.os-v { font-size: 0.64rem; font-weight: 600; }
.os-v.is-free { color: var(--yes); }
.os-total { display: flex; justify-content: space-between; align-items: center; border-top: 1px solid var(--border); margin-top: 5px; padding-top: 7px; }
.os-tk { font-size: 0.72rem; font-weight: 700; }
.os-tv { font-size: 0.92rem; font-weight: 800; color: var(--accent); }
.os-promo { margin-top: 8px; border: 0; background: transparent; color: var(--accent); font: inherit; font-size: 0.62rem; font-weight: 600; cursor: pointer; padding: 2px; border-radius: 3px; }
.os-promo:hover { text-decoration: underline; }
.os-promo:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }''',
  }],
 },
 {
  "folder": "ecommerce", "slug": "payment-method", "title": "Payment Methods",
  "desc": "Selectable cards, UPI and saved wallet options.",
  "idx_desc": "Selectable cards, UPI and wallet options.",
  "mini": '<div class="p-card" style="width: 32px; height: 20px;"></div><div class="p-dot" style="position: static;"></div>',
  "blocks": [{
   "id": "payment-method", "title": "Choose payment",
   "html": '''<div class="pm-card">
  <p class="pm-t">Payment method</p>
  <div class="pm-list" role="radiogroup" aria-label="Payment method">
    <button class="pm-opt is-on" type="button" role="radio" aria-checked="true" data-pm="card">
      <span class="pm-logo pm-visa" aria-hidden="true">VISA</span>
      <span class="pm-m"><span class="pm-n">Visa ending 4242</span><span class="pm-d">Expires 09/29</span></span>
      <span class="pm-radio" aria-hidden="true"></span>
    </button>
    <button class="pm-opt" type="button" role="radio" aria-checked="false" data-pm="upi">
      <span class="pm-logo pm-upi" aria-hidden="true">UPI</span>
      <span class="pm-m"><span class="pm-n">UPI</span><span class="pm-d">Pay using any UPI app</span></span>
      <span class="pm-radio" aria-hidden="true"></span>
    </button>
    <button class="pm-opt" type="button" role="radio" aria-checked="false" data-pm="wallet">
      <span class="pm-logo pm-wallet" aria-hidden="true">$</span>
      <span class="pm-m"><span class="pm-n">OWN Wallet</span><span class="pm-d">Balance $120.40</span></span>
      <span class="pm-radio" aria-hidden="true"></span>
    </button>
  </div>
  <button class="pm-new" type="button" id="pmNew">+ Add a new card</button>
  <button class="pm-pay" type="button" id="pmPay">Pay $73.44</button>
  <p class="pm-msg" id="pmMsg" role="status"></p>
</div>''',
   "css": '''.pm-card { max-width: 350px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 13px; }
.pm-t { margin: 0 0 8px; font-size: 0.8rem; font-weight: 700; }
.pm-list { display: flex; flex-direction: column; gap: 5px; margin-bottom: 7px; }
.pm-opt { display: flex; align-items: center; gap: 8px; border: 1px solid var(--border); border-radius: 5px; background: transparent; padding: 8px; cursor: pointer; text-align: left; font: inherit; }
.pm-opt:hover { border-color: var(--accent); }
.pm-opt.is-on { border-color: var(--accent); background: var(--accent-soft); }
.pm-opt:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.pm-logo { width: 34px; height: 23px; border-radius: 3px; display: flex; align-items: center; justify-content: center; font-size: 0.5rem; font-weight: 800; flex: 0 0 auto; }
.pm-visa { background: #1a1f71; color: #fff; font-style: italic; letter-spacing: 0.04em; }
.pm-upi { background: linear-gradient(135deg, #f0b543, #e5484d); color: #fff; }
.pm-wallet { background: var(--accent-soft); color: var(--accent); font-size: 0.8rem; }
.pm-m { flex: 1; display: flex; flex-direction: column; min-width: 0; }
.pm-n { font-size: 0.68rem; font-weight: 700; }
.pm-d { font-size: 0.56rem; color: var(--muted); }
.pm-radio { width: 13px; height: 13px; border-radius: 999px; border: 1px solid var(--border); flex: 0 0 auto; position: relative; }
.pm-opt.is-on .pm-radio { border-color: var(--accent); }
.pm-opt.is-on .pm-radio::after { content: ""; position: absolute; inset: 2px; border-radius: 999px; background: var(--accent); }
.pm-new { border: 0; background: transparent; color: var(--accent); font: inherit; font-size: 0.64rem; font-weight: 700; padding: 2px; cursor: pointer; margin-bottom: 8px; border-radius: 3px; }
.pm-new:hover { text-decoration: underline; }
.pm-new:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.pm-pay { width: 100%; border: 0; background: var(--accent); color: #fff; font: inherit; font-size: 0.74rem; font-weight: 700; padding: 9px; border-radius: 4px; cursor: pointer; }
.pm-pay:hover { opacity: 0.92; }
.pm-pay:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.pm-msg { min-height: 1em; margin: 7px 0 0; font-size: 0.62rem; color: var(--yes); text-align: center; }''',
   "js": '''(function () {
  var opts = Array.prototype.slice.call(document.querySelectorAll(".pm-opt"));
  var msg = document.getElementById("pmMsg");

  opts.forEach(function (o) {
    o.addEventListener("click", function () {
      opts.forEach(function (x) {
        x.classList.remove("is-on");
        x.setAttribute("aria-checked", "false");
      });
      o.classList.add("is-on");
      o.setAttribute("aria-checked", "true");
    });
  });

  document.getElementById("pmNew").addEventListener("click", function () {
    msg.textContent = "New card form would open here.";
  });

  document.getElementById("pmPay").addEventListener("click", function () {
    var sel = document.querySelector(".pm-opt.is-on .pm-n").textContent;
    msg.textContent = "Paid with " + sel + " (demo).";
  });
})();''',
  }],
 },
 {
  "folder": "ecommerce", "slug": "coupon-code", "title": "Coupon Code",
  "desc": "Promo input with valid, invalid and applied states.",
  "idx_desc": "Promo input with valid and invalid states.",
  "mini": '<div class="p-input" style="width: 46px;"></div><div class="p-tag">10%</div>',
  "blocks": [{
   "id": "coupon-code", "title": "Apply promo",
   "html": '''<div class="cu-card">
  <p class="cu-t">Have a promo code?</p>
  <div class="cu-row">
    <input class="cu-input" id="cuInput" type="text" placeholder="Enter code" aria-label="Promo code" autocomplete="off">
    <button class="cu-apply" type="button" id="cuApply">Apply</button>
  </div>
  <p class="cu-msg" id="cuMsg" role="status"></p>
  <div class="cu-applied" id="cuApplied" hidden>
    <span class="cu-tag" id="cuTag">SAVE10</span>
    <span class="cu-saved">You save $7.34</span>
    <button class="cu-remove" type="button" id="cuRemove" aria-label="Remove promo code">&times;</button>
  </div>
  <p class="cu-sub">Available offers</p>
  <button class="cu-offer" type="button" data-code="SAVE10">SAVE10 &#8212; 10% off your order</button>
  <button class="cu-offer" type="button" data-code="FREESHIP">FREESHIP &#8212; free delivery</button>
</div>''',
   "css": '''.cu-card { max-width: 340px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 13px; }
.cu-t { margin: 0 0 7px; font-size: 0.76rem; font-weight: 700; }
.cu-row { display: flex; gap: 6px; }
.cu-input { flex: 1; min-width: 0; border: 1px solid var(--border); border-radius: 4px; background: var(--bg); color: var(--text); font: inherit; font-size: 0.72rem; padding: 7px 9px; outline: none; text-transform: uppercase; }
.cu-input:focus { border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-soft); }
.cu-apply { border: 0; background: var(--accent); color: #fff; font: inherit; font-size: 0.68rem; font-weight: 700; padding: 7px 12px; border-radius: 4px; cursor: pointer; }
.cu-apply:hover { opacity: 0.92; }
.cu-apply:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.cu-msg { min-height: 1em; margin: 5px 0 0; font-size: 0.62rem; color: var(--no); }
.cu-msg.is-ok { color: var(--yes); }
.cu-applied { display: flex; align-items: center; gap: 6px; border: 1px dashed var(--yes); background: rgba(34, 160, 107, 0.07); border-radius: 4px; padding: 6px 8px; margin-top: 6px; }
.cu-tag { font-size: 0.56rem; font-weight: 800; letter-spacing: 0.05em; color: var(--yes); border: 1px solid currentColor; border-radius: 3px; padding: 1px 4px; }
.cu-saved { flex: 1; font-size: 0.62rem; font-weight: 600; color: var(--yes); }
.cu-remove { border: 0; background: transparent; color: var(--muted); font-size: 0.8rem; cursor: pointer; padding: 1px 3px; border-radius: 2px; line-height: 1; }
.cu-remove:hover { color: var(--no); }
.cu-remove:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.cu-sub { margin: 10px 0 4px; font-size: 0.56rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; color: var(--muted); }
.cu-offer { display: block; width: 100%; text-align: left; border: 0; background: transparent; color: var(--accent); font: inherit; font-size: 0.62rem; font-weight: 600; padding: 4px 2px; cursor: pointer; border-radius: 3px; }
.cu-offer:hover { text-decoration: underline; }
.cu-offer:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }''',
   "js": '''(function () {
  var input = document.getElementById("cuInput");
  var msg = document.getElementById("cuMsg");
  var applied = document.getElementById("cuApplied");
  var tag = document.getElementById("cuTag");

  function apply(code) {
    var c = code.trim().toUpperCase();
    if (c === "SAVE10") {
      tag.textContent = "SAVE10";
      applied.hidden = false;
      msg.textContent = "Code applied — 10% off.";
      msg.classList.add("is-ok");
      input.value = "";
    } else if (c === "FREESHIP") {
      tag.textContent = "FREESHIP";
      applied.hidden = false;
      msg.textContent = "Code applied — free delivery.";
      msg.classList.add("is-ok");
      input.value = "";
    } else {
      applied.hidden = true;
      msg.textContent = c ? "That code is not valid." : "Enter a promo code first.";
      msg.classList.remove("is-ok");
    }
  }

  document.getElementById("cuApply").addEventListener("click", function () { apply(input.value); });
  input.addEventListener("keydown", function (e) {
    if (e.key === "Enter") apply(input.value);
  });
  document.querySelectorAll(".cu-offer").forEach(function (b) {
    b.addEventListener("click", function () { apply(b.getAttribute("data-code")); });
  });
  document.getElementById("cuRemove").addEventListener("click", function () {
    applied.hidden = true;
    msg.textContent = "Promo removed.";
    msg.classList.remove("is-ok");
  });
})();''',
  }],
 },
 {
  "folder": "ecommerce", "slug": "order-tracker", "title": "Order Tracker",
  "desc": "Horizontal progress steps and delivery events.",
  "idx_desc": "Horizontal order steps with delivery events.",
  "mini": '<div class="p-steps"><span></span><span></span><span></span></div>',
  "blocks": [{
   "id": "order-tracker", "title": "Track order",
   "html": '''<div class="ot-card">
  <div class="ot-head"><span class="ot-t">Order #ORD-8241</span><span class="ot-eta">Arrives Fri, 24 Oct</span></div>
  <div class="ot-steps">
    <div class="ot-step is-done"><span class="ot-dot" aria-hidden="true"></span><span class="ot-sl">Ordered</span><span class="ot-sd">18 Oct</span></div>
    <div class="ot-step is-done"><span class="ot-dot" aria-hidden="true"></span><span class="ot-sl">Packed</span><span class="ot-sd">19 Oct</span></div>
    <div class="ot-step is-now"><span class="ot-dot" aria-hidden="true"></span><span class="ot-sl">Shipped</span><span class="ot-sd">21 Oct</span></div>
    <div class="ot-step"><span class="ot-dot" aria-hidden="true"></span><span class="ot-sl">Delivered</span><span class="ot-sd">Expected</span></div>
  </div>
  <div class="ot-events">
    <div class="ot-ev"><span class="ot-ei is-now" aria-hidden="true"></span><div><p class="ot-et">Out for delivery</p><p class="ot-ed">Mumbai hub &#183; Today, 08:40</p></div></div>
    <div class="ot-ev"><span class="ot-ei" aria-hidden="true"></span><div><p class="ot-et">In transit</p><p class="ot-ed">Pune facility &#183; 21 Oct, 22:10</p></div></div>
    <div class="ot-ev"><span class="ot-ei" aria-hidden="true"></span><div><p class="ot-et">Package packed</p><p class="ot-ed">Warehouse &#183; 19 Oct, 14:02</p></div></div>
  </div>
</div>''',
   "css": '''.ot-card { max-width: 400px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 13px; }
.ot-head { display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-bottom: 12px; flex-wrap: wrap; }
.ot-t { font-size: 0.74rem; font-weight: 700; }
.ot-eta { font-size: 0.6rem; font-weight: 600; color: var(--yes); background: rgba(34, 160, 107, 0.1); padding: 2px 7px; border-radius: 999px; }
.ot-steps { display: flex; justify-content: space-between; position: relative; margin-bottom: 14px; }
.ot-steps::before { content: ""; position: absolute; top: 5px; left: 9%; right: 9%; height: 2px; background: var(--border); }
.ot-step { position: relative; z-index: 1; display: flex; flex-direction: column; align-items: center; gap: 3px; flex: 1; }
.ot-dot { width: 11px; height: 11px; border-radius: 999px; background: var(--bg); border: 2px solid var(--border); }
.ot-step.is-done .ot-dot { background: var(--yes); border-color: var(--yes); }
.ot-step.is-now .ot-dot { background: var(--accent); border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-soft); }
.ot-sl { font-size: 0.58rem; font-weight: 700; color: var(--muted); }
.ot-step.is-done .ot-sl, .ot-step.is-now .ot-sl { color: var(--text); }
.ot-sd { font-size: 0.52rem; color: var(--muted); }
.ot-events { border-top: 1px solid var(--border); padding-top: 7px; }
.ot-ev { display: flex; gap: 7px; padding: 4px 0; }
.ot-ei { width: 7px; height: 7px; border-radius: 999px; background: var(--border); margin-top: 4px; flex: 0 0 auto; }
.ot-ei.is-now { background: var(--accent); }
.ot-et { margin: 0; font-size: 0.66rem; font-weight: 600; }
.ot-ed { margin: 1px 0 0; font-size: 0.58rem; color: var(--muted); }''',
  }],
 },
 {
  "folder": "ecommerce", "slug": "price-breakdown", "title": "Price Breakdown",
  "desc": "Itemised pricing with savings, tax and total.",
  "idx_desc": "Itemised pricing with savings, tax and total.",
  "mini": '<div class="p-line" style="width: 44px;"></div><div class="p-line" style="width: 26px; border-color: var(--accent);"></div>',
  "blocks": [{
   "id": "price-breakdown", "title": "Cost breakdown",
   "html": '''<div class="pb-card">
  <p class="pb-t">Price details</p>
  <div class="pb-line"><span class="pb-k">Items (3)</span><span class="pb-v">$68.00</span></div>
  <div class="pb-line"><span class="pb-k">Discount (SAVE10)</span><span class="pb-v is-save">-$6.80</span></div>
  <div class="pb-line"><span class="pb-k">Delivery</span><span class="pb-v is-save">Free</span></div>
  <div class="pb-line"><span class="pb-k">Estimated tax</span><span class="pb-v">$5.51</span></div>
  <div class="pb-line pb-sub"><span class="pb-k">Subtotal</span><span class="pb-v">$66.71</span></div>
  <div class="pb-total"><span class="pb-tk">Total</span><span class="pb-tv">$66.71</span></div>
  <p class="pb-saved"><span class="pb-ico" aria-hidden="true">&#10003;</span> You saved $6.80 on this order</p>
  <button class="pb-help" type="button">How is tax calculated?</button>
</div>''',
   "css": '''.pb-card { max-width: 330px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 13px; }
.pb-t { margin: 0 0 8px; font-size: 0.78rem; font-weight: 700; }
.pb-line { display: flex; align-items: center; justify-content: space-between; padding: 4px 0; }
.pb-k { font-size: 0.66rem; color: var(--muted); }
.pb-v { font-size: 0.66rem; font-weight: 600; }
.pb-v.is-save { color: var(--yes); }
.pb-sub { border-top: 1px dashed var(--border); margin-top: 4px; padding-top: 6px; }
.pb-sub .pb-k, .pb-sub .pb-v { color: var(--text); font-weight: 700; }
.pb-total { display: flex; align-items: center; justify-content: space-between; border-top: 1px solid var(--border); margin-top: 4px; padding-top: 7px; }
.pb-tk { font-size: 0.74rem; font-weight: 800; }
.pb-tv { font-size: 0.98rem; font-weight: 800; color: var(--accent); }
.pb-saved { display: flex; align-items: center; gap: 4px; margin: 7px 0; font-size: 0.6rem; font-weight: 600; color: var(--yes); }
.pb-ico { width: 13px; height: 13px; border-radius: 999px; background: rgba(34, 160, 107, 0.14); display: flex; align-items: center; justify-content: center; font-size: 0.5rem; }
.pb-help { border: 0; background: transparent; color: var(--accent); font: inherit; font-size: 0.6rem; font-weight: 600; padding: 2px; cursor: pointer; border-radius: 3px; }
.pb-help:hover { text-decoration: underline; }
.pb-help:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }''',
  }],
 },
 {
  "folder": "ecommerce", "slug": "invoice", "title": "Invoice",
  "desc": "Printable invoice with billing info and line items.",
  "idx_desc": "Printable invoice with billing info and totals.",
  "mini": '<div class="p-page" style="height: 48px;"><span class="p-line" style="width: 26px;"></span><span class="p-line" style="width: 40px;"></span></div>',
  "blocks": [{
   "id": "invoice", "title": "Invoice preview",
   "html": '''<div class="iv-card">
  <div class="iv-head">
    <div><p class="iv-logo">OWN<span class="iv-logoD">studio</span></p><p class="iv-tag">Design systems &amp; components</p></div>
    <div class="iv-meta"><p class="iv-inv">Invoice #INV-2841</p><p class="iv-date">Issued 18 Oct 2026</p><p class="iv-date">Due 01 Nov 2026</p></div>
  </div>
  <div class="iv-bill">
    <div><p class="iv-lb">Billed to</p><p class="iv-bn">Ayesha Khan</p><p class="iv-bd">14 Marine Drive<br>Mumbai 400020</p></div>
    <div><p class="iv-lb">Payment</p><p class="iv-bn">Visa ending 4242</p><p class="iv-bd">Paid 18 Oct 2026</p></div>
  </div>
  <div class="iv-scroll">
    <table class="iv-table">
      <thead><tr><th class="iv-th">Item</th><th class="iv-th iv-qty">Qty</th><th class="iv-th iv-amt">Amount</th></tr></thead>
      <tbody>
        <tr class="iv-tr"><td class="iv-td">UI library license</td><td class="iv-td iv-qty">1</td><td class="iv-td iv-amt">$96.00</td></tr>
        <tr class="iv-tr"><td class="iv-td">Component audit</td><td class="iv-td iv-qty">2</td><td class="iv-td iv-amt">$40.00</td></tr>
        <tr class="iv-tr"><td class="iv-td">Priority support</td><td class="iv-td iv-qty">1</td><td class="iv-td iv-amt">$12.00</td></tr>
      </tbody>
    </table>
  </div>
  <div class="iv-totals">
    <div class="iv-line"><span class="iv-k">Subtotal</span><span class="iv-v">$148.00</span></div>
    <div class="iv-line"><span class="iv-k">Tax (8%)</span><span class="iv-v">$11.84</span></div>
    <div class="iv-grand"><span class="iv-gk">Total paid</span><span class="iv-gv">$159.84</span></div>
  </div>
  <div class="iv-foot">
    <span class="iv-thanks">Thank you for your business.</span>
    <button class="iv-print" type="button" id="ivPrint">Print invoice</button>
  </div>
  <p class="iv-msg" id="ivMsg" aria-live="polite"></p>
</div>''',
   "css": '''.iv-card { max-width: 430px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 14px; }
.iv-head { display: flex; justify-content: space-between; gap: 10px; flex-wrap: wrap; padding-bottom: 10px; border-bottom: 1px solid var(--border); }
.iv-logo { margin: 0; font-size: 0.86rem; font-weight: 800; letter-spacing: 0.02em; }
.iv-logoD { color: var(--accent); }
.iv-tag { margin: 1px 0 0; font-size: 0.56rem; color: var(--muted); }
.iv-meta { text-align: right; }
.iv-inv { margin: 0; font-size: 0.66rem; font-weight: 700; }
.iv-date { margin: 1px 0 0; font-size: 0.56rem; color: var(--muted); }
.iv-bill { display: flex; gap: 18px; flex-wrap: wrap; padding: 10px 0; }
.iv-lb { margin: 0; font-size: 0.52rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; color: var(--muted); }
.iv-bn { margin: 2px 0 0; font-size: 0.66rem; font-weight: 600; }
.iv-bd { margin: 1px 0 0; font-size: 0.56rem; color: var(--muted); line-height: 1.4; }
.iv-scroll { overflow-x: auto; }
.iv-table { width: 100%; border-collapse: collapse; min-width: 300px; }
.iv-th { text-align: left; font-size: 0.52rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--muted); padding: 5px 4px; border-bottom: 1px solid var(--border); }
.iv-td { font-size: 0.64rem; padding: 6px 4px; border-bottom: 1px solid var(--border); }
.iv-qty { text-align: center; width: 36px; }
.iv-amt { text-align: right; white-space: nowrap; }
.iv-totals { margin-left: auto; max-width: 180px; padding-top: 7px; }
.iv-line { display: flex; justify-content: space-between; padding: 2px 0; }
.iv-k { font-size: 0.6rem; color: var(--muted); }
.iv-v { font-size: 0.6rem; font-weight: 600; }
.iv-grand { display: flex; justify-content: space-between; border-top: 1px solid var(--border); margin-top: 4px; padding-top: 5px; }
.iv-gk { font-size: 0.66rem; font-weight: 800; }
.iv-gv { font-size: 0.8rem; font-weight: 800; color: var(--accent); }
.iv-foot { display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-top: 10px; padding-top: 8px; border-top: 1px solid var(--border); flex-wrap: wrap; }
.iv-thanks { font-size: 0.56rem; color: var(--muted); }
.iv-print { border: 1px solid var(--border); background: transparent; color: var(--accent); font: inherit; font-size: 0.6rem; font-weight: 700; padding: 4px 9px; border-radius: 3px; cursor: pointer; }
.iv-print:hover { border-color: var(--accent); }
.iv-print:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.iv-msg { min-height: 1em; margin: 5px 0 0; font-size: 0.58rem; color: var(--muted); }''',
   "js": '''(function () {
  document.getElementById("ivPrint").addEventListener("click", function () {
    document.getElementById("ivMsg").textContent = "Use your browser print dialog to save as PDF.";
  });
})();''',
  }],
 },
]
