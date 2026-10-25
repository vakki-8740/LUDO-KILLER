CAT = "Authentication"
CAT_ID = "auth"

PAGES = [
 {
  "folder": "auth", "slug": "login", "title": "Login Form",
  "desc": "Email and password sign-in with visibility toggle.",
  "idx_desc": "Email and password sign-in with show/hide.",
  "mini": '<div class="p-page" style="height: 48px;"><span class="p-line" style="width: 40px;"></span><span class="p-line" style="width: 32px;"></span></div>',
  "blocks": [{
   "id": "login-form", "title": "Sign in",
   "html": '''<div class="lg-card">
  <h4 class="lg-t">Welcome back</h4>
  <p class="lg-s">Sign in to continue to your workspace.</p>
  <label class="lg-lbl" for="lgEmail">Email</label>
  <input class="lg-input" id="lgEmail" type="email" placeholder="you@example.com" autocomplete="email">
  <label class="lg-lbl" for="lgPass">Password</label>
  <div class="lg-passwrap">
    <input class="lg-input lg-pass" id="lgPass" type="password" placeholder="Enter password" autocomplete="current-password">
    <button class="lg-eye" type="button" id="lgEye" aria-label="Show password" aria-pressed="false">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7-10-7-10-7z"/><circle cx="12" cy="12" r="3"/></svg>
    </button>
  </div>
  <div class="lg-row">
    <label class="lg-remember"><input class="lg-check" type="checkbox"> Remember me</label>
    <button class="lg-forgot" type="button">Forgot password?</button>
  </div>
  <button class="lg-submit" type="button" id="lgSubmit">Sign in</button>
  <p class="lg-msg" id="lgMsg" role="status"></p>
  <p class="lg-or"><span>or continue with</span></p>
  <div class="lg-social">
    <button class="lg-soc" type="button">Google</button>
    <button class="lg-soc" type="button">GitHub</button>
  </div>
</div>''',
   "css": '''.lg-card { max-width: 340px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 20px; }
.lg-t { margin: 0 0 3px; font-size: 1.05rem; }
.lg-s { margin: 0 0 16px; font-size: 0.78rem; color: var(--muted); }
.lg-lbl { display: block; margin: 0 0 4px; font-size: 0.72rem; font-weight: 600; color: var(--muted); }
.lg-input { width: 100%; border: 1px solid var(--border); border-radius: var(--radius); background: var(--bg); color: var(--text); font: inherit; font-size: 0.83rem; padding: 9px 11px; outline: none; margin-bottom: 10px; }
.lg-input:focus { border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-soft); }
.lg-passwrap { position: relative; }
.lg-pass { padding-right: 36px; }
.lg-eye { position: absolute; right: 4px; top: 4px; width: 30px; height: 30px; border: 0; background: transparent; color: var(--muted); cursor: pointer; border-radius: 4px; display: flex; align-items: center; justify-content: center; }
.lg-eye svg { width: 16px; height: 16px; }
.lg-eye:hover { color: var(--accent); }
.lg-eye:focus-visible { outline: 2px solid var(--accent); outline-offset: 1px; }
.lg-row { display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-bottom: 12px; flex-wrap: wrap; }
.lg-remember { display: inline-flex; align-items: center; gap: 5px; font-size: 0.72rem; color: var(--muted); cursor: pointer; }
.lg-check { accent-color: var(--accent); width: 13px; height: 13px; }
.lg-forgot { border: 0; background: transparent; color: var(--accent); font: inherit; font-size: 0.72rem; font-weight: 600; cursor: pointer; padding: 2px; border-radius: 3px; }
.lg-forgot:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.lg-submit { width: 100%; border: 0; background: var(--accent); color: #fff; font: inherit; font-size: 0.84rem; font-weight: 600; padding: 10px; border-radius: var(--radius); cursor: pointer; }
.lg-submit:hover { opacity: 0.92; }
.lg-submit:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.lg-msg { min-height: 1em; margin: 8px 0 0; font-size: 0.74rem; color: var(--no); }
.lg-msg.is-ok { color: var(--yes); }
.lg-or { display: flex; align-items: center; gap: 8px; margin: 12px 0; font-size: 0.68rem; color: var(--muted); }
.lg-or::before, .lg-or::after { content: ""; flex: 1; height: 1px; background: var(--border); }
.lg-social { display: flex; gap: 7px; }
.lg-soc { flex: 1; border: 1px solid var(--border); background: transparent; color: var(--text); font: inherit; font-size: 0.74rem; font-weight: 600; padding: 8px; border-radius: var(--radius); cursor: pointer; }
.lg-soc:hover { border-color: var(--accent); color: var(--accent); }
.lg-soc:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }''',
   "js": '''(function () {
  var pass = document.getElementById("lgPass");
  var eye = document.getElementById("lgEye");
  var msg = document.getElementById("lgMsg");

  eye.addEventListener("click", function () {
    var show = pass.type === "password";
    pass.type = show ? "text" : "password";
    eye.setAttribute("aria-label", show ? "Hide password" : "Show password");
    eye.setAttribute("aria-pressed", String(show));
  });

  document.getElementById("lgSubmit").addEventListener("click", function () {
    var email = document.getElementById("lgEmail").value.trim();
    if (!/^[^\\s@]+@[^\\s@]+\\.[^\\s@]{2,}$/.test(email)) {
      msg.textContent = "Enter a valid email address.";
      msg.classList.remove("is-ok");
      return;
    }
    if (pass.value.length < 6) {
      msg.textContent = "Password must be at least 6 characters.";
      msg.classList.remove("is-ok");
      return;
    }
    msg.textContent = "Signed in successfully (demo).";
    msg.classList.add("is-ok");
  });
})();''',
  }],
 },
 {
  "folder": "auth", "slug": "signup", "title": "Signup Form",
  "desc": "Account creation with live password strength.",
  "idx_desc": "Signup form with live password strength.",
  "mini": '<div class="p-page" style="height: 48px;"><span class="p-line" style="width: 34px;"></span><span class="p-line" style="width: 40px;"></span></div>',
  "blocks": [{
   "id": "signup-form", "title": "Create account",
   "html": '''<div class="sg-card">
  <h4 class="sg-t">Create your account</h4>
  <p class="sg-s">Free for personal projects.</p>
  <label class="sg-lbl" for="sgName">Full name</label>
  <input class="sg-input" id="sgName" type="text" placeholder="Ayesha Khan" autocomplete="name">
  <label class="sg-lbl" for="sgEmail">Email</label>
  <input class="sg-input" id="sgEmail" type="email" placeholder="you@example.com" autocomplete="email">
  <label class="sg-lbl" for="sgPass">Password</label>
  <input class="sg-input" id="sgPass" type="password" placeholder="At least 8 characters" autocomplete="new-password">
  <div class="sg-meter" aria-hidden="true">
    <span class="sg-seg" id="sgSeg1"></span><span class="sg-seg" id="sgSeg2"></span><span class="sg-seg" id="sgSeg3"></span>
  </div>
  <p class="sg-hint" id="sgHint">Use 8+ characters with a number and a symbol.</p>
  <label class="sg-terms"><input class="sg-check" id="sgTerms" type="checkbox"> I agree to the terms of service</label>
  <button class="sg-submit" type="button" id="sgSubmit">Create account</button>
  <p class="sg-msg" id="sgMsg" role="status"></p>
</div>''',
   "css": '''.sg-card { max-width: 350px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 20px; }
.sg-t { margin: 0 0 3px; font-size: 1.02rem; }
.sg-s { margin: 0 0 14px; font-size: 0.76rem; color: var(--muted); }
.sg-lbl { display: block; margin: 0 0 4px; font-size: 0.71rem; font-weight: 600; color: var(--muted); }
.sg-input { width: 100%; border: 1px solid var(--border); border-radius: var(--radius); background: var(--bg); color: var(--text); font: inherit; font-size: 0.82rem; padding: 8px 10px; margin-bottom: 9px; outline: none; }
.sg-input:focus { border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-soft); }
.sg-input.is-bad { border-color: var(--no); }
.sg-meter { display: flex; gap: 4px; margin-bottom: 4px; }
.sg-seg { flex: 1; height: 4px; border-radius: 999px; background: var(--border); transition: background 0.2s; }
.sg-hint { margin: 0 0 10px; font-size: 0.68rem; color: var(--muted); min-height: 1em; }
.sg-terms { display: flex; align-items: flex-start; gap: 6px; font-size: 0.72rem; color: var(--muted); margin-bottom: 12px; line-height: 1.4; }
.sg-check { accent-color: var(--accent); width: 13px; height: 13px; margin-top: 1px; }
.sg-submit { width: 100%; border: 0; background: var(--accent); color: #fff; font: inherit; font-size: 0.83rem; font-weight: 600; padding: 9px; border-radius: var(--radius); cursor: pointer; }
.sg-submit:hover { opacity: 0.92; }
.sg-submit:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.sg-msg { min-height: 1em; margin: 8px 0 0; font-size: 0.73rem; color: var(--no); }
.sg-msg.is-ok { color: var(--yes); }''',
   "js": '''(function () {
  var pass = document.getElementById("sgPass");
  var hint = document.getElementById("sgHint");
  var segs = [document.getElementById("sgSeg1"), document.getElementById("sgSeg2"), document.getElementById("sgSeg3")];
  var msg = document.getElementById("sgMsg");

  function strength(v) {
    var score = 0;
    if (v.length >= 8) score += 1;
    if (/[0-9]/.test(v)) score += 1;
    if (/[^A-Za-z0-9]/.test(v)) score += 1;
    return score;
  }

  pass.addEventListener("input", function () {
    var s = strength(pass.value);
    var colors = ["", "var(--no)", "var(--warn)", "var(--yes)"];
    segs.forEach(function (seg, i) { seg.style.background = i < s ? colors[s] : "var(--border)"; });
    hint.textContent = pass.value
      ? (s === 3 ? "Strong password." : s === 2 ? "Almost there — add a symbol." : "Weak — add numbers and symbols.")
      : "Use 8+ characters with a number and a symbol.";
  });

  document.getElementById("sgSubmit").addEventListener("click", function () {
    var name = document.getElementById("sgName");
    var email = document.getElementById("sgEmail");
    name.classList.toggle("is-bad", !name.value.trim());
    email.classList.toggle("is-bad", !/^[^\\s@]+@[^\\s@]+\\.[^\\s@]{2,}$/.test(email.value.trim()));
    if (!name.value.trim()) { msg.textContent = "Please enter your name."; msg.classList.remove("is-ok"); return; }
    if (!/^[^\\s@]+@[^\\s@]+\\.[^\\s@]{2,}$/.test(email.value.trim())) { msg.textContent = "Enter a valid email."; msg.classList.remove("is-ok"); return; }
    if (strength(pass.value) < 2) { msg.textContent = "Please choose a stronger password."; msg.classList.remove("is-ok"); return; }
    if (!document.getElementById("sgTerms").checked) { msg.textContent = "Please accept the terms to continue."; msg.classList.remove("is-ok"); return; }
    msg.textContent = "Account created (demo).";
    msg.classList.add("is-ok");
  });
})();''',
  }],
 },
 {
  "folder": "auth", "slug": "forgot-password", "title": "Forgot Password",
  "desc": "Reset request with a confirmation state.",
  "idx_desc": "Reset request form with sent confirmation.",
  "mini": '<div class="p-page" style="height: 46px;"><span class="p-line" style="width: 44px;"></span></div>',
  "blocks": [{
   "id": "forgot-password", "title": "Reset request",
   "html": '''<div class="fp-card">
  <span class="fp-ic" aria-hidden="true">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3.5 6.5L12 13l8.5-6.5"/></svg>
  </span>
  <h4 class="fp-t" id="fpTitle">Forgot your password?</h4>
  <p class="fp-s" id="fpSub">Enter your email and we will send a reset link.</p>
  <div id="fpForm">
    <label class="fp-lbl" for="fpEmail">Email address</label>
    <input class="fp-input" id="fpEmail" type="email" placeholder="you@example.com" autocomplete="email">
    <button class="fp-submit" type="button" id="fpSend">Send reset link</button>
    <button class="fp-back" type="button">Back to sign in</button>
    <p class="fp-msg" id="fpMsg" role="status"></p>
  </div>
  <div id="fpDone" hidden>
    <p class="fp-done" id="fpDoneText"></p>
    <button class="fp-open" type="button">Open email app</button>
    <button class="fp-again" type="button" id="fpAgain">Use another email</button>
  </div>
</div>''',
   "css": '''.fp-card { max-width: 340px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 22px; text-align: center; }
.fp-ic { display: inline-flex; width: 44px; height: 44px; border-radius: 999px; background: var(--accent-soft); color: var(--accent); align-items: center; justify-content: center; margin-bottom: 10px; }
.fp-ic svg { width: 22px; height: 22px; }
.fp-t { margin: 0 0 4px; font-size: 1rem; }
.fp-s { margin: 0 0 16px; font-size: 0.76rem; color: var(--muted); line-height: 1.45; }
.fp-lbl { display: block; text-align: left; margin-bottom: 4px; font-size: 0.71rem; font-weight: 600; color: var(--muted); }
.fp-input { width: 100%; border: 1px solid var(--border); border-radius: var(--radius); background: var(--bg); color: var(--text); font: inherit; font-size: 0.82rem; padding: 9px 10px; margin-bottom: 10px; outline: none; }
.fp-input:focus { border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-soft); }
.fp-submit { width: 100%; border: 0; background: var(--accent); color: #fff; font: inherit; font-size: 0.82rem; font-weight: 600; padding: 9px; border-radius: var(--radius); cursor: pointer; }
.fp-submit:hover { opacity: 0.92; }
.fp-submit:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.fp-back { display: block; margin: 10px auto 0; border: 0; background: transparent; color: var(--muted); font: inherit; font-size: 0.72rem; font-weight: 600; cursor: pointer; }
.fp-back:hover { color: var(--accent); }
.fp-back:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; border-radius: 3px; }
.fp-msg { min-height: 1em; margin: 8px 0 0; font-size: 0.72rem; color: var(--no); text-align: left; }
.fp-done { margin: 0 0 14px; font-size: 0.78rem; line-height: 1.5; color: var(--text); }
.fp-open { width: 100%; border: 0; background: var(--accent); color: #fff; font: inherit; font-size: 0.82rem; font-weight: 600; padding: 9px; border-radius: var(--radius); cursor: pointer; margin-bottom: 8px; }
.fp-again { border: 0; background: transparent; color: var(--accent); font: inherit; font-size: 0.73rem; font-weight: 600; cursor: pointer; }
.fp-open:focus-visible, .fp-again:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }''',
   "js": '''(function () {
  var msg = document.getElementById("fpMsg");
  var email = document.getElementById("fpEmail");
  var done = document.getElementById("fpDone");
  var form = document.getElementById("fpForm");

  document.getElementById("fpSend").addEventListener("click", function () {
    var v = email.value.trim();
    if (!/^[^\\s@]+@[^\\s@]+\\.[^\\s@]{2,}$/.test(v)) {
      msg.textContent = "Enter a valid email address.";
      return;
    }
    form.hidden = true;
    done.hidden = false;
    document.getElementById("fpTitle").textContent = "Check your inbox";
    document.getElementById("fpSub").textContent = "We sent a reset link to " + v + ".";
    document.getElementById("fpDoneText").textContent = "The link expires in 30 minutes. Check spam if you do not see it.";
  });

  document.getElementById("fpAgain").addEventListener("click", function () {
    done.hidden = true;
    form.hidden = false;
    document.getElementById("fpTitle").textContent = "Forgot your password?";
    document.getElementById("fpSub").textContent = "Enter your email and we will send a reset link.";
    email.value = "";
    msg.textContent = "";
    email.focus();
  });
})();''',
  }],
 },
 {
  "folder": "auth", "slug": "reset-password", "title": "Reset Password",
  "desc": "New password form with live rule checklist.",
  "idx_desc": "New password form with live rule checklist.",
  "mini": '<div class="p-page" style="height: 46px;"><span class="p-line" style="width: 38px;"></span><span class="p-line" style="width: 26px;"></span></div>',
  "blocks": [{
   "id": "reset-password", "title": "Choose a new password",
   "html": '''<div class="rp-card">
  <h4 class="rp-t">Set a new password</h4>
  <p class="rp-s">Use a password you have not used before.</p>
  <label class="rp-lbl" for="rpNew">New password</label>
  <input class="rp-input" id="rpNew" type="password" autocomplete="new-password" placeholder="New password">
  <label class="rp-lbl" for="rpConfirm">Confirm password</label>
  <input class="rp-input" id="rpConfirm" type="password" autocomplete="new-password" placeholder="Repeat password">
  <ul class="rp-rules">
    <li class="rp-rule" id="rpRule1"><span class="rp-b" aria-hidden="true"></span>At least 8 characters</li>
    <li class="rp-rule" id="rpRule2"><span class="rp-b" aria-hidden="true"></span>Contains a number</li>
    <li class="rp-rule" id="rpRule3"><span class="rp-b" aria-hidden="true"></span>Matches the confirmation</li>
  </ul>
  <button class="rp-submit" type="button" id="rpSubmit">Update password</button>
  <p class="rp-msg" id="rpMsg" role="status"></p>
</div>''',
   "css": '''.rp-card { max-width: 340px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 20px; }
.rp-t { margin: 0 0 3px; font-size: 1rem; }
.rp-s { margin: 0 0 14px; font-size: 0.76rem; color: var(--muted); }
.rp-lbl { display: block; margin-bottom: 4px; font-size: 0.71rem; font-weight: 600; color: var(--muted); }
.rp-input { width: 100%; border: 1px solid var(--border); border-radius: var(--radius); background: var(--bg); color: var(--text); font: inherit; font-size: 0.82rem; padding: 9px 10px; margin-bottom: 9px; outline: none; }
.rp-input:focus { border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-soft); }
.rp-rules { list-style: none; margin: 2px 0 12px; padding: 0; display: flex; flex-direction: column; gap: 4px; }
.rp-rule { display: flex; align-items: center; gap: 6px; font-size: 0.71rem; color: var(--muted); }
.rp-b { width: 12px; height: 12px; border-radius: 999px; border: 1px solid var(--border); flex: 0 0 auto; position: relative; }
.rp-rule.is-ok { color: var(--yes); }
.rp-rule.is-ok .rp-b { background: var(--yes); border-color: var(--yes); }
.rp-rule.is-ok .rp-b::after { content: ""; position: absolute; left: 3px; top: 1px; width: 3px; height: 6px; border: solid #fff; border-width: 0 1.5px 1.5px 0; transform: rotate(45deg); }
.rp-submit { width: 100%; border: 0; background: var(--accent); color: #fff; font: inherit; font-size: 0.83rem; font-weight: 600; padding: 9px; border-radius: var(--radius); cursor: pointer; }
.rp-submit:hover { opacity: 0.92; }
.rp-submit:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.rp-msg { min-height: 1em; margin: 8px 0 0; font-size: 0.73rem; color: var(--no); }
.rp-msg.is-ok { color: var(--yes); }''',
   "js": '''(function () {
  var pass = document.getElementById("rpNew");
  var confirm = document.getElementById("rpConfirm");
  var r1 = document.getElementById("rpRule1");
  var r2 = document.getElementById("rpRule2");
  var r3 = document.getElementById("rpRule3");
  var msg = document.getElementById("rpMsg");

  function check() {
    var a = pass.value;
    var b = confirm.value;
    var ok1 = a.length >= 8;
    var ok2 = /[0-9]/.test(a);
    var ok3 = a.length > 0 && a === b;
    r1.classList.toggle("is-ok", ok1);
    r2.classList.toggle("is-ok", ok2);
    r3.classList.toggle("is-ok", ok3);
    return ok1 && ok2 && ok3;
  }

  [pass, confirm].forEach(function (el) {
    el.addEventListener("input", function () {
      check();
      msg.textContent = "";
    });
  });

  document.getElementById("rpSubmit").addEventListener("click", function () {
    if (!check()) {
      msg.textContent = "Please satisfy all three rules.";
      msg.classList.remove("is-ok");
      return;
    }
    msg.textContent = "Password updated. You can sign in now.";
    msg.classList.add("is-ok");
  });
})();''',
  }],
 },
 {
  "folder": "auth", "slug": "email-verify", "title": "Email Verification",
  "desc": "Verification notice with resend countdown.",
  "idx_desc": "Verification notice with resend countdown.",
  "mini": '<div class="p-page" style="height: 46px;"><span class="p-dot" style="position: static; background: var(--accent);"></span><span class="p-line" style="width: 38px;"></span></div>',
  "blocks": [{
   "id": "email-verify", "title": "Verify your email",
   "html": '''<div class="ev-card">
  <span class="ev-ic" aria-hidden="true">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3.5 6.5L12 13l8.5-6.5"/><path d="M8 20l4-3 4 3"/></svg>
  </span>
  <h4 class="ev-t">Confirm your email</h4>
  <p class="ev-s">We sent a verification link to <strong id="evEmail">ayesha@example.com</strong>.</p>
  <button class="ev-open" type="button">Open email app</button>
  <button class="ev-resend" type="button" id="evResend" disabled>Resend in 30s</button>
  <button class="ev-change" type="button" id="evChange">Change email address</button>
  <p class="ev-msg" id="evMsg" role="status"></p>
</div>''',
   "css": '''.ev-card { max-width: 340px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 22px; text-align: center; }
.ev-ic { display: inline-flex; width: 46px; height: 46px; border-radius: 999px; background: var(--accent-soft); color: var(--accent); align-items: center; justify-content: center; margin-bottom: 10px; }
.ev-ic svg { width: 23px; height: 23px; }
.ev-t { margin: 0 0 4px; font-size: 1rem; }
.ev-s { margin: 0 0 16px; font-size: 0.77rem; color: var(--muted); line-height: 1.5; }
.ev-s strong { color: var(--text); }
.ev-open { width: 100%; border: 0; background: var(--accent); color: #fff; font: inherit; font-size: 0.82rem; font-weight: 600; padding: 9px; border-radius: var(--radius); cursor: pointer; margin-bottom: 7px; }
.ev-open:hover { opacity: 0.92; }
.ev-open:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.ev-resend { width: 100%; border: 1px solid var(--border); background: transparent; color: var(--accent); font: inherit; font-size: 0.77rem; font-weight: 600; padding: 8px; border-radius: var(--radius); cursor: pointer; margin-bottom: 7px; }
.ev-resend[disabled] { color: var(--muted); cursor: default; }
.ev-resend:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.ev-change { border: 0; background: transparent; color: var(--muted); font: inherit; font-size: 0.72rem; font-weight: 600; cursor: pointer; padding: 3px; border-radius: 3px; }
.ev-change:hover { color: var(--accent); }
.ev-change:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.ev-msg { min-height: 1em; margin: 8px 0 0; font-size: 0.72rem; color: var(--yes); }''',
   "js": '''(function () {
  var resend = document.getElementById("evResend");
  var msg = document.getElementById("evMsg");
  var left = 30;
  var timer = setInterval(function () {
    left -= 1;
    if (left <= 0) {
      clearInterval(timer);
      resend.disabled = false;
      resend.textContent = "Resend verification email";
    } else {
      resend.textContent = "Resend in " + left + "s";
    }
  }, 1000);

  resend.addEventListener("click", function () {
    if (resend.disabled) return;
    msg.textContent = "A new verification email was sent.";
    left = 30;
    resend.disabled = true;
    resend.textContent = "Resend in 30s";
    timer = setInterval(function () {
      left -= 1;
      if (left <= 0) {
        clearInterval(timer);
        resend.disabled = false;
        resend.textContent = "Resend verification email";
      } else {
        resend.textContent = "Resend in " + left + "s";
      }
    }, 1000);
  });

  document.getElementById("evChange").addEventListener("click", function () {
    msg.textContent = "Change flow is demo-only here.";
  });
})();''',
  }],
 },
 {
  "folder": "auth", "slug": "otp-verify", "title": "OTP Verification",
  "desc": "Four-digit code entry with verify feedback.",
  "idx_desc": "Four-digit OTP entry with verify feedback.",
  "mini": '<div class="p-row-tight"><span class="p-box"></span><span class="p-box"></span><span class="p-box"></span><span class="p-box"></span></div>',
  "blocks": [{
   "id": "otp-verify", "title": "Verify your number",
   "html": '''<div class="ov-card">
  <h4 class="ov-t">Check your phone</h4>
  <p class="ov-s">Enter the 4-digit code sent to +91 98765 43210.</p>
  <div class="ov-row" id="ovRow" role="group" aria-label="Verification code">
    <input class="ov-cell" type="text" inputmode="numeric" maxlength="1" aria-label="Digit 1" autocomplete="one-time-code">
    <input class="ov-cell" type="text" inputmode="numeric" maxlength="1" aria-label="Digit 2">
    <input class="ov-cell" type="text" inputmode="numeric" maxlength="1" aria-label="Digit 3">
    <input class="ov-cell" type="text" inputmode="numeric" maxlength="1" aria-label="Digit 4">
  </div>
  <button class="ov-submit" type="button" id="ovSubmit">Verify</button>
  <p class="ov-msg" id="ovMsg" role="status"></p>
  <div class="ov-foot">
    <button class="ov-resend" type="button" id="ovResend">Resend code</button>
    <button class="ov-help" type="button">Need help?</button>
  </div>
</div>''',
   "css": '''.ov-card { max-width: 330px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 22px; text-align: center; }
.ov-t { margin: 0 0 4px; font-size: 0.98rem; }
.ov-s { margin: 0 0 14px; font-size: 0.76rem; color: var(--muted); line-height: 1.45; }
.ov-row { display: flex; gap: 8px; justify-content: center; margin-bottom: 12px; }
.ov-cell { width: 44px; height: 48px; text-align: center; font: inherit; font-size: 1.1rem; font-weight: 700; color: var(--text); background: var(--bg); border: 1px solid var(--border); border-radius: var(--radius); outline: none; }
.ov-cell:focus { border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-soft); }
.ov-cell.is-full { border-color: var(--accent); }
.ov-submit { width: 100%; border: 0; background: var(--accent); color: #fff; font: inherit; font-size: 0.82rem; font-weight: 600; padding: 9px; border-radius: var(--radius); cursor: pointer; }
.ov-submit:hover { opacity: 0.92; }
.ov-submit:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.ov-msg { min-height: 1em; margin: 8px 0 0; font-size: 0.73rem; color: var(--no); }
.ov-msg.is-ok { color: var(--yes); }
.ov-foot { display: flex; justify-content: space-between; gap: 8px; margin-top: 8px; }
.ov-resend, .ov-help { border: 0; background: transparent; color: var(--muted); font: inherit; font-size: 0.71rem; font-weight: 600; cursor: pointer; padding: 2px; border-radius: 3px; }
.ov-resend:hover, .ov-help:hover { color: var(--accent); }
.ov-resend:focus-visible, .ov-help:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }''',
   "js": '''(function () {
  var cells = Array.prototype.slice.call(document.querySelectorAll(".ov-cell"));
  var msg = document.getElementById("ovMsg");

  cells.forEach(function (c, i) {
    c.addEventListener("input", function () {
      c.value = c.value.replace(/[^0-9]/g, "").slice(0, 1);
      c.classList.toggle("is-full", !!c.value);
      if (c.value && i < cells.length - 1) cells[i + 1].focus();
    });
    c.addEventListener("keydown", function (e) {
      if (e.key === "Backspace" && !c.value && i > 0) {
        cells[i - 1].value = "";
        cells[i - 1].focus();
        cells[i - 1].classList.remove("is-full");
      }
    });
  });

  document.getElementById("ovSubmit").addEventListener("click", function () {
    var v = cells.map(function (c) { return c.value; }).join("");
    if (v.length < 4) { msg.textContent = "Enter all 4 digits."; msg.classList.remove("is-ok"); return; }
    if (v === "1234") { msg.textContent = "Verified. Welcome back!"; msg.classList.add("is-ok"); }
    else { msg.textContent = "Wrong code. Demo code is 1234."; msg.classList.remove("is-ok"); }
  });

  document.getElementById("ovResend").addEventListener("click", function () {
    msg.textContent = "A new code was sent.";
    msg.classList.add("is-ok");
  });
})();''',
  }],
 },
 {
  "folder": "auth", "slug": "two-factor", "title": "Two-Factor Auth",
  "desc": "Method picker with authenticator code entry.",
  "idx_desc": "2FA method picker with code entry.",
  "mini": '<div class="p-row-tight"><span class="p-box"></span><span class="p-box"></span><span class="p-box"></span></div>',
  "blocks": [{
   "id": "two-factor", "title": "Two-step verification",
   "html": '''<div class="tf-card">
  <div class="tf-head">
    <span class="tf-lock" aria-hidden="true">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="10" width="16" height="10" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/></svg>
    </span>
    <div><p class="tf-t">Two-factor authentication</p><p class="tf-s" id="tfSub">Enter the 6-digit code from your authenticator app.</p></div>
  </div>
  <div class="tf-tabs" role="tablist" aria-label="2FA method">
    <button class="tf-tab is-on" type="button" role="tab" aria-selected="true" data-m="app">Authenticator</button>
    <button class="tf-tab" type="button" role="tab" aria-selected="false" data-m="sms">SMS</button>
  </div>
  <label class="tf-lbl" for="tfCode">Verification code</label>
  <input class="tf-input" id="tfCode" type="text" inputmode="numeric" maxlength="6" placeholder="000000" autocomplete="one-time-code">
  <label class="tf-remember"><input class="tf-check" type="checkbox"> Trust this device for 30 days</label>
  <button class="tf-submit" type="button" id="tfSubmit">Verify and continue</button>
  <p class="tf-msg" id="tfMsg" role="status"></p>
  <button class="tf-recover" type="button">Use a recovery code instead</button>
</div>''',
   "css": '''.tf-card { max-width: 350px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 18px; }
.tf-head { display: flex; gap: 10px; margin-bottom: 12px; }
.tf-lock { width: 38px; height: 38px; flex: 0 0 auto; border-radius: 999px; background: var(--accent-soft); color: var(--accent); display: flex; align-items: center; justify-content: center; }
.tf-lock svg { width: 19px; height: 19px; }
.tf-t { margin: 0 0 2px; font-size: 0.88rem; font-weight: 700; }
.tf-s { margin: 0; font-size: 0.72rem; color: var(--muted); line-height: 1.4; }
.tf-tabs { display: flex; gap: 3px; background: var(--bg); border-radius: var(--radius); padding: 3px; margin-bottom: 10px; }
.tf-tab { flex: 1; border: 0; background: transparent; color: var(--muted); font: inherit; font-size: 0.72rem; font-weight: 600; padding: 6px; border-radius: 4px; cursor: pointer; }
.tf-tab.is-on { background: var(--card); color: var(--text); box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08); }
.tf-tab:focus-visible { outline: 2px solid var(--accent); outline-offset: 1px; }
.tf-lbl { display: block; margin-bottom: 4px; font-size: 0.71rem; font-weight: 600; color: var(--muted); }
.tf-input { width: 100%; border: 1px solid var(--border); border-radius: var(--radius); background: var(--bg); color: var(--text); font: inherit; font-size: 1rem; font-weight: 700; letter-spacing: 0.35em; padding: 9px 10px; outline: none; margin-bottom: 8px; text-align: center; }
.tf-input:focus { border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-soft); }
.tf-remember { display: flex; align-items: center; gap: 6px; font-size: 0.71rem; color: var(--muted); margin-bottom: 10px; cursor: pointer; }
.tf-check { accent-color: var(--accent); width: 13px; height: 13px; }
.tf-submit { width: 100%; border: 0; background: var(--accent); color: #fff; font: inherit; font-size: 0.82rem; font-weight: 600; padding: 9px; border-radius: var(--radius); cursor: pointer; }
.tf-submit:hover { opacity: 0.92; }
.tf-submit:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.tf-msg { min-height: 1em; margin: 8px 0 0; font-size: 0.72rem; color: var(--no); text-align: center; }
.tf-msg.is-ok { color: var(--yes); }
.tf-recover { display: block; margin: 4px auto 0; border: 0; background: transparent; color: var(--muted); font: inherit; font-size: 0.71rem; font-weight: 600; cursor: pointer; }
.tf-recover:hover { color: var(--accent); }
.tf-recover:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; border-radius: 3px; }''',
   "js": '''(function () {
  var code = document.getElementById("tfCode");
  var msg = document.getElementById("tfMsg");
  var sub = document.getElementById("tfSub");

  document.querySelectorAll(".tf-tab").forEach(function (t) {
    t.addEventListener("click", function () {
      document.querySelectorAll(".tf-tab").forEach(function (x) {
        x.classList.remove("is-on");
        x.setAttribute("aria-selected", "false");
      });
      t.classList.add("is-on");
      t.setAttribute("aria-selected", "true");
      sub.textContent = t.getAttribute("data-m") === "app"
        ? "Enter the 6-digit code from your authenticator app."
        : "Enter the 6-digit code we texted to +91 98765 43210.";
      msg.textContent = "";
    });
  });

  document.getElementById("tfSubmit").addEventListener("click", function () {
    var v = code.value.replace(/[^0-9]/g, "");
    if (v.length !== 6) { msg.textContent = "Enter the full 6-digit code."; msg.classList.remove("is-ok"); return; }
    if (v === "123456") { msg.textContent = "Verified. Redirecting to your account."; msg.classList.add("is-ok"); }
    else { msg.textContent = "Invalid code. Demo code is 123456."; msg.classList.remove("is-ok"); }
  });

  document.querySelector(".tf-recover").addEventListener("click", function () {
    msg.textContent = "Recovery code flow is demo-only.";
    msg.classList.remove("is-ok");
  });
})();''',
  }],
 },
 {
  "folder": "auth", "slug": "profile-settings", "title": "Profile Settings",
  "desc": "Editable profile form with save feedback.",
  "idx_desc": "Editable profile form with save feedback.",
  "mini": '<div class="p-row-tight"><span class="p-av" style="width: 20px; height: 20px;"></span><span class="p-line" style="width: 36px;"></span></div>',
  "blocks": [{
   "id": "profile-settings", "title": "Profile details",
   "html": '''<div class="ps-card">
  <div class="ps-head">
    <span class="ps-av" aria-hidden="true">AK</span>
    <div><p class="ps-name">Ayesha Khan</p><button class="ps-photo" type="button">Change photo</button></div>
  </div>
  <div class="ps-grid">
    <div class="ps-field">
      <label class="ps-lbl" for="psFirst">First name</label>
      <input class="ps-input" id="psFirst" type="text" value="Ayesha">
    </div>
    <div class="ps-field">
      <label class="ps-lbl" for="psLast">Last name</label>
      <input class="ps-input" id="psLast" type="text" value="Khan">
    </div>
  </div>
  <label class="ps-lbl" for="psEmail">Email</label>
  <input class="ps-input" id="psEmail" type="email" value="ayesha@example.com">
  <label class="ps-lbl" for="psBio">Bio</label>
  <textarea class="ps-area" id="psBio" rows="3">Product designer focused on calm, accessible interfaces.</textarea>
  <div class="ps-foot">
    <button class="ps-cancel" type="button" id="psCancel">Cancel</button>
    <button class="ps-save" type="button" id="psSave">Save changes</button>
  </div>
  <p class="ps-msg" id="psMsg" role="status"></p>
</div>''',
   "css": '''.ps-card { max-width: 400px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 16px; }
.ps-head { display: flex; align-items: center; gap: 10px; margin-bottom: 14px; }
.ps-av { width: 48px; height: 48px; border-radius: 999px; background: linear-gradient(135deg, #4f6bed, #8b5cf6); color: #fff; font-weight: 700; display: flex; align-items: center; justify-content: center; flex: 0 0 auto; }
.ps-name { margin: 0 0 2px; font-size: 0.88rem; font-weight: 700; }
.ps-photo { border: 0; background: transparent; color: var(--accent); font: inherit; font-size: 0.72rem; font-weight: 600; cursor: pointer; padding: 1px; border-radius: 3px; }
.ps-photo:hover { text-decoration: underline; }
.ps-photo:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.ps-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
.ps-field { min-width: 0; }
.ps-lbl { display: block; margin: 0 0 4px; font-size: 0.7rem; font-weight: 600; color: var(--muted); }
.ps-input { width: 100%; border: 1px solid var(--border); border-radius: var(--radius); background: var(--bg); color: var(--text); font: inherit; font-size: 0.8rem; padding: 8px 9px; margin-bottom: 9px; outline: none; }
.ps-area { width: 100%; border: 1px solid var(--border); border-radius: var(--radius); background: var(--bg); color: var(--text); font: inherit; font-size: 0.8rem; padding: 8px 9px; outline: none; resize: vertical; margin-bottom: 10px; }
.ps-input:focus, .ps-area:focus { border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-soft); }
.ps-foot { display: flex; justify-content: flex-end; gap: 7px; }
.ps-cancel { border: 1px solid var(--border); background: transparent; color: var(--muted); font: inherit; font-size: 0.76rem; font-weight: 600; padding: 7px 13px; border-radius: var(--radius); cursor: pointer; }
.ps-save { border: 0; background: var(--accent); color: #fff; font: inherit; font-size: 0.76rem; font-weight: 600; padding: 7px 13px; border-radius: var(--radius); cursor: pointer; }
.ps-cancel:hover { border-color: var(--muted); }
.ps-save:hover { opacity: 0.92; }
.ps-cancel:focus-visible, .ps-save:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.ps-msg { min-height: 1em; margin: 8px 0 0; font-size: 0.72rem; color: var(--yes); text-align: right; }''',
   "js": '''(function () {
  var first = document.getElementById("psFirst");
  var last = document.getElementById("psLast");
  var email = document.getElementById("psEmail");
  var msg = document.getElementById("psMsg");
  var initial = { first: first.value, last: last.value, email: email.value };

  document.getElementById("psSave").addEventListener("click", function () {
    if (!first.value.trim() || !last.value.trim()) {
      msg.textContent = "Name fields cannot be empty.";
      msg.style.color = "var(--no)";
      return;
    }
    if (!/^[^\\s@]+@[^\\s@]+\\.[^\\s@]{2,}$/.test(email.value.trim())) {
      msg.textContent = "Enter a valid email address.";
      msg.style.color = "var(--no)";
      return;
    }
    msg.textContent = "Profile saved.";
    msg.style.color = "var(--yes)";
  });

  document.getElementById("psCancel").addEventListener("click", function () {
    first.value = initial.first;
    last.value = initial.last;
    email.value = initial.email;
    msg.textContent = "";
  });
})();''',
  }],
 },
 {
  "folder": "auth", "slug": "change-password", "title": "Change Password",
  "desc": "Current and new password with strength feedback.",
  "idx_desc": "Password change form with strength meter.",
  "mini": '<div class="p-page" style="height: 46px;"><span class="p-line" style="width: 40px;"></span><span class="p-line" style="width: 30px;"></span></div>',
  "blocks": [{
   "id": "change-password", "title": "Update password",
   "html": '''<div class="cw-card">
  <h4 class="cw-t">Change password</h4>
  <p class="cw-s">Choose a strong password you do not use elsewhere.</p>
  <label class="cw-lbl" for="cwCurrent">Current password</label>
  <input class="cw-input" id="cwCurrent" type="password" autocomplete="current-password" placeholder="Current password">
  <label class="cw-lbl" for="cwNew">New password</label>
  <input class="cw-input" id="cwNew" type="password" autocomplete="new-password" placeholder="New password">
  <div class="cw-meter"><span class="cw-seg" id="cwS1"></span><span class="cw-seg" id="cwS2"></span><span class="cw-seg" id="cwS3"></span></div>
  <p class="cw-hint" id="cwHint">8+ characters, one number, one symbol.</p>
  <label class="cw-lbl" for="cwConfirm">Confirm new password</label>
  <input class="cw-input" id="cwConfirm" type="password" autocomplete="new-password" placeholder="Repeat new password">
  <button class="cw-submit" type="button" id="cwSubmit">Update password</button>
  <p class="cw-msg" id="cwMsg" role="status"></p>
</div>''',
   "css": '''.cw-card { max-width: 340px; border: 1px solid var(--border); border-radius: var(--radius); background: var(--card); padding: 18px; }
.cw-t { margin: 0 0 3px; font-size: 0.95rem; }
.cw-s { margin: 0 0 12px; font-size: 0.74rem; color: var(--muted); }
.cw-lbl { display: block; margin-bottom: 4px; font-size: 0.7rem; font-weight: 600; color: var(--muted); }
.cw-input { width: 100%; border: 1px solid var(--border); border-radius: var(--radius); background: var(--bg); color: var(--text); font: inherit; font-size: 0.8rem; padding: 8px 9px; margin-bottom: 8px; outline: none; }
.cw-input:focus { border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-soft); }
.cw-meter { display: flex; gap: 4px; margin-bottom: 4px; }
.cw-seg { flex: 1; height: 4px; border-radius: 999px; background: var(--border); }
.cw-hint { margin: 0 0 10px; font-size: 0.68rem; color: var(--muted); min-height: 1em; }
.cw-submit { width: 100%; border: 0; background: var(--accent); color: #fff; font: inherit; font-size: 0.8rem; font-weight: 600; padding: 9px; border-radius: var(--radius); cursor: pointer; }
.cw-submit:hover { opacity: 0.92; }
.cw-submit:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.cw-msg { min-height: 1em; margin: 8px 0 0; font-size: 0.72rem; color: var(--no); }
.cw-msg.is-ok { color: var(--yes); }''',
   "js": '''(function () {
  var current = document.getElementById("cwCurrent");
  var np = document.getElementById("cwNew");
  var confirm = document.getElementById("cwConfirm");
  var msg = document.getElementById("cwMsg");
  var hint = document.getElementById("cwHint");
  var segs = [document.getElementById("cwS1"), document.getElementById("cwS2"), document.getElementById("cwS3")];

  function score(v) {
    var s = 0;
    if (v.length >= 8) s += 1;
    if (/[0-9]/.test(v)) s += 1;
    if (/[^A-Za-z0-9]/.test(v)) s += 1;
    return s;
  }

  np.addEventListener("input", function () {
    var s = score(np.value);
    var colors = ["", "var(--no)", "var(--warn)", "var(--yes)"];
    segs.forEach(function (seg, i) { seg.style.background = i < s ? colors[s] : "var(--border)"; });
    hint.textContent = np.value ? (s === 3 ? "Strong password." : "Keep going — " + (3 - s) + " rule(s) left.") : "8+ characters, one number, one symbol.";
  });

  document.getElementById("cwSubmit").addEventListener("click", function () {
    if (!current.value) { msg.textContent = "Enter your current password."; msg.classList.remove("is-ok"); return; }
    if (score(np.value) < 3) { msg.textContent = "New password is not strong enough."; msg.classList.remove("is-ok"); return; }
    if (np.value !== confirm.value) { msg.textContent = "Passwords do not match."; msg.classList.remove("is-ok"); return; }
    msg.textContent = "Password changed successfully.";
    msg.classList.add("is-ok");
  });
})();''',
  }],
 },
]
