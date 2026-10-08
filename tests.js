/* Mini-tests en línea — English Support (por grado)
   Datos: window.TESTS (tests-data.js), generado desde fuente/content/tests_*.py
   Funciona en línea (Vercel) y sin internet (carpeta descargada, file://). */
(function () {
  "use strict";
  const DATA = window.TESTS || {};
  const META = window.META || { grade: "", name: "", trimester: "", title: "English Support", zip: "" };
  const BRAND = `${META.title} · ${META.name}`;
  const SK = ["listening", "reading", "writing", "speaking", "mediation"];
  const SKN = { listening: "Listening", reading: "Reading", writing: "Writing", speaking: "Speaking", mediation: "Mediation" };
  const SKES = { listening: "Escuchar", reading: "Leer", writing: "Escribir", speaking: "Hablar", mediation: "Ayudar a otros a entender" };
  const app = document.getElementById("app");
  // ---------- estudiante: entra con su PIN (la lista está en la hoja privada del maestro) ----------
  // En el laboratorio varias personas usan la misma computadora: cada estudiante guarda lo suyo aparte
  // y "Salir" no borra nada. Sin ES_SEND_URL (config.js) el sitio funciona como antes, sin entrar.
  const SEND_URL = window.ES_SEND_URL || "";
  const SESSION_MS = 3 * 60 * 60 * 1000;   // la sesión se cierra sola tras 3 horas sin uso
  const hashPin = p => { let h = 5381; for (const c of String(p)) h = ((h << 5) + h + c.charCodeAt(0)) >>> 0; return h.toString(36); };
  const student = {
    get() {
      try {
        const st = JSON.parse(localStorage.getItem("es-student"));
        if (!st || st.grade !== META.grade) return null;
        if (Date.now() - (st.at || 0) > SESSION_MS) { localStorage.removeItem("es-student"); return null; }
        return st;
      } catch (e) { return null; }
    },
    set(v) { try { localStorage.setItem("es-student", JSON.stringify(Object.assign(v, { at: Date.now() }))); } catch (e) {} },
    touch() { const st = student.get(); if (st) student.set(st); },
    logout() { try { localStorage.removeItem("es-student"); sessionStorage.removeItem("es-guest"); } catch (e) {} },
    guest() { try { return sessionStorage.getItem("es-guest") === "1"; } catch (e) { return false; } },
    setGuest() { try { sessionStorage.setItem("es-guest", "1"); } catch (e) {} },
  };
  const PFX = () => { const st = SEND_URL ? student.get() : null; return "es" + META.grade + ":" + (st ? "p" + hashPin(st.pin) + ":" : ""); };
  const store = {
    get(k, d) { try { const v = localStorage.getItem(PFX() + k); return v ? JSON.parse(v) : d; } catch (e) { return d; } },
    set(k, v) { try { localStorage.setItem(PFX() + k, JSON.stringify(v)); } catch (e) {} },
    del(k) { try { localStorage.removeItem(PFX() + k); } catch (e) {} },
  };
  async function api(action, data) {
    const res = await fetch(SEND_URL, { method: "POST", body: JSON.stringify(Object.assign({ action }, data)) });
    return res.json();
  }
  // resultados que no se pudieron enviar (sin internet): se reintentan solos
  const queue = {
    all() { try { return JSON.parse(localStorage.getItem("es-queue")) || []; } catch (e) { return []; } },
    save(q) { try { localStorage.setItem("es-queue", JSON.stringify(q)); } catch (e) {} },
    add(item) { const q = queue.all(); q.push(item); queue.save(q); },
    async flush() {
      if (!SEND_URL) return;
      let q = queue.all(); if (!q.length) return;
      const left = [];
      for (const item of q) { try { const j = await api("submit", item); if (!j.ok) left.push(item); } catch (e) { left.push(item); } }
      queue.save(left);
    },
  };
  window.addEventListener("online", () => queue.flush());

  let progress = null; // mejor puntaje enviado, por "5.1/Listening" (de la hoja del maestro)
  async function loadProgress(onDone) {
    const st = student.get(); if (!st) return;
    try { const j = await api("progress", { pin: st.pin }); if (j.ok) { progress = j.progreso || {}; onDone(); } } catch (e) {}
  }

  function studentBar(onChange) {
    const bar = el("div", "student");
    if (!SEND_URL) return bar;
    const st = student.get();
    if (st) {
      student.touch();
      bar.innerHTML = `<span>Hola, <b>${esc(st.name)}</b> · ${esc(META.name)}</span>`;
      const out = el("button", "link", "Salir"); out.type = "button";
      out.onclick = () => { student.logout(); progress = null; onChange(); };
      bar.append(out);
      return bar;
    }
    if (student.guest()) {
      bar.innerHTML = `<span>Estás practicando <b>sin registrarte</b>: tus resultados no se envían al maestro.</span>`;
      const go = el("button", "link", "Entrar con mi PIN"); go.type = "button";
      go.onclick = () => { student.logout(); onChange(); };
      bar.append(go);
      return bar;
    }
    bar.classList.add("ask");
    bar.innerHTML = `<b>Escribe tu PIN de 4 números</b>
      <div class="sfields"><input type="password" class="spin" inputmode="numeric" pattern="[0-9]*" maxlength="4" autocomplete="off" placeholder="• • • •" aria-label="PIN">
      <button type="button" class="btn">Entrar</button></div><p class="smsg"></p>
      <button type="button" class="link sguest">Practicar sin registrarme</button>`;
    const inp = bar.querySelector(".spin"), go = bar.querySelector(".btn"), msg = bar.querySelector(".smsg");
    inp.oninput = () => { inp.value = inp.value.replace(/\D/g, "").slice(0, 4); };
    inp.onkeydown = e => { if (e.key === "Enter") go.click(); };
    bar.querySelector(".sguest").onclick = () => { student.setGuest(); onChange(); };
    go.onclick = async () => {
      const pin = inp.value;
      if (pin.length !== 4) { msg.textContent = "El PIN tiene 4 números."; inp.focus(); return; }
      go.disabled = true; go.textContent = "Buscando…"; msg.textContent = "";
      try {
        const j = await api("login", { pin, grado: META.grade });
        if (j.ok) {
          const sf = bar.querySelector(".sfields"); sf.innerHTML = "";
          bar.querySelector("b").textContent = "Confirma que eres tú"; sf.before(msg);
          msg.innerHTML = `¿Eres <b>${esc(j.nombre)}</b>?`;
          const yes = el("button", "btn", "Sí, soy yo"), no = el("button", "btn ghost", "No");
          yes.type = no.type = "button";
          yes.onclick = () => { student.set({ pin, name: j.nombre, grade: META.grade }); onChange(); queue.flush(); };
          no.onclick = () => onChange();
          sf.append(yes, no); yes.focus();
          return;
        }
        if (j.error === "grado") msg.innerHTML = `Ese PIN es de <b>${j.grado_correcto === "K" ? "Kínder" : j.grado_correcto + ".° grado"}</b>. <a href="../${esc(j.grado_correcto)}/tests">Ir a sus mini-tests</a>`;
        else msg.textContent = "No encontramos ese PIN. Revísalo y vuelve a intentarlo.";
      } catch (e) {
        msg.textContent = "No hay conexión con internet. Puedes practicar sin registrarte, pero no se enviará tu resultado.";
      }
      go.disabled = false; go.textContent = "Entrar"; inp.value = ""; inp.focus();
    };
    setTimeout(() => inp.focus(), 0);
    return bar;
  }

  // ---------- utilidades ----------
  const plain = s => String(s || "").replace(/\*\*/g, "").replace(/\*/g, "");
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  function md(s) {
    return esc(s).replace(/\*\*(.+?)\*\*/g, "<b>$1</b>").replace(/\*(.+?)\*/g, "<i>$1</i>");
  }
  const norm = s => String(s).toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "")
    .replace(/[’`´]/g, "'").replace(/'/g, "").replace(/[^a-z0-9 ]+/g, " ").replace(/\s+/g, " ").trim();
  function accepts(answer, list) {
    const a = norm(answer);
    if (!a) return false;
    return list.some(x => x.startsWith("~") ? x.slice(1).split(" ").every(k => a.includes(norm(k))) : a === norm(x));
  }
  const LET = "abcdef";
  // opciones con dibujo: "@nombre" o "@nombre|texto" → img/nombre.png
  const isPic = o => typeof o === "string" && o[0] === "@";
  const picName = o => o.slice(1).split("|")[0];
  const picCap = o => o.slice(1).split("|")[1] || "";
  const picHTML = (o, letter) => `<img src="img/${esc(picName(o))}.png" alt="${esc(picCap(o) || letter)}"><span class="cap">${letter})${picCap(o) ? " " + esc(picCap(o)) : ""}</span>`;
  const el = (tag, cls, html) => { const e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; };
  const themeLabel = id => id.replace("-", ".");

  // ---------- índice ----------
  function renderIndex() {
    document.title = `Mini-tests en línea · ${BRAND}`;
    app.innerHTML = "";
    app.append(el("p", "kicker", `${BRAND} · ${META.trimester}`));
    app.append(studentBar(() => { progress = null; renderIndex(); }));
    if (SEND_URL && student.get() && progress === null) { progress = {}; loadProgress(renderIndex); }
    app.append(el("h1", null, "Mini-tests en línea"));
    app.append(el("p", "lead", "Los mismos mini-tests del libro, pero <b>se corrigen solos</b> y te explican cada respuesta. " + (SEND_URL ? "Cuando termines, toca <b>Enviar a mi maestro</b>." : "Tu progreso se guarda en este dispositivo.")));
    Object.keys(DATA).sort().forEach(tid => {
      const th = DATA[tid];
      const sec = el("section", "theme");
      sec.append(el("h2", null, `<span class="tnum">Tema ${themeLabel(tid)}</span> ${esc(th.title)}`));
      sec.append(el("p", "scen", esc(th.scenario)));
      const grid = el("div", "cards");
      SK.forEach(sk => {
        const t = th.tests[sk]; if (!t) return;
        const sent = progress && progress[`${themeLabel(tid)}/${SKN[sk]}`];
        const local = store.get(`best:${tid}/${sk}`, null);
        const best = sent ? Math.max(sent.best, local || 0) : local;
        const a = el("a", "card");
        a.href = `#${tid}/${sk}`;
        a.innerHTML = `<span class="sk">${SKN[sk]}</span><span class="skes">${SKES[sk]}</span>` +
          (best != null ? `<span class="best ${best / t.total >= 0.8 ? "ok" : best / t.total >= 0.5 ? "mid" : "low"}">Mejor: ${best} / ${t.total}</span>` : `<span class="best none">Sin intentar</span>`) +
          (sent ? `<span class="sentlbl">✓ Enviado ${sent.veces === 1 ? "1 vez" : sent.veces + " veces"}</span>` : "");
        grid.append(a);
      });
      sec.append(grid);
      app.append(sec);
    });
    const off = el("section", "offline");
    off.innerHTML = `<h2>Usar sin internet</h2><p>Descarga una vez la carpeta con los audios y los mini-tests. Descomprímela y abre el archivo <b>index.html</b>: funciona sin conexión en una laptop.</p><p><a class="btn" href="${META.zip}" download>Descargar (zip)</a> <a class="btn ghost" href="index.html">Ver los audios</a></p>`;
    app.append(off);
    window.scrollTo(0, 0);
  }

  // ---------- reproductor ----------
  function player(theme, n) {
    const box = el("div", "player");
    const a = new Audio(); a.preload = "metadata";
    const srcs = { normal: `audio/${theme}/${n}.mp3`, slow: `audio/${theme}/${n}-slow.mp3` };
    let mode = "normal", plays = 0; a.src = srcs.normal;
    box.innerHTML = `<div class="prow"><button class="play" type="button">▶ Reproducir</button><div class="pinfo"><div class="bar"><i></i></div><span class="tm">0:00</span></div></div>
      <div class="prow2"><label><input type="checkbox" class="slow"> Velocidad lenta</label><span class="plays"></span></div>`;
    const btn = box.querySelector(".play"), bar = box.querySelector(".bar i"), tm = box.querySelector(".tm"), pl = box.querySelector(".plays");
    const fmt = s => isFinite(s) ? Math.floor(s / 60) + ":" + String(Math.floor(s % 60)).padStart(2, "0") : "0:00";
    const lab = () => btn.textContent = a.paused ? "▶ Reproducir" : "❚❚ Pausa";
    btn.onclick = () => a.paused ? a.play() : a.pause();
    a.onplay = () => { if (a.currentTime < 0.5) { plays++; pl.textContent = `Escuchado ${plays} ${plays === 1 ? "vez" : "veces"}`; } lab(); };
    a.onpause = a.onended = lab;
    a.ontimeupdate = a.onloadedmetadata = () => { bar.style.width = (a.currentTime / a.duration * 100 || 0) + "%"; tm.textContent = fmt(a.currentTime) + " / " + fmt(a.duration); };
    box.querySelector(".slow").onchange = e => { mode = e.target.checked ? "slow" : "normal"; const was = !a.paused; a.src = srcs[mode]; a.load(); if (was) a.play(); };
    box.querySelector(".bar").onclick = e => { if (isFinite(a.duration)) { const r = e.currentTarget.getBoundingClientRect(); a.currentTime = (e.clientX - r.left) / r.width * a.duration; } };
    return box;
  }

  // ---------- grabadora ----------
  function recorder() {
    const box = el("div", "rec");
    if (!(navigator.mediaDevices && window.MediaRecorder)) {
      box.innerHTML = `<p class="muted">Este navegador no permite grabar. Usa la grabadora de tu celular o laptop.</p>`;
      return box;
    }
    box.innerHTML = `<button type="button" class="recbtn">● Grabar mi respuesta</button><span class="recst"></span><div class="takes"></div>`;
    const b = box.querySelector(".recbtn"), st = box.querySelector(".recst"), takes = box.querySelector(".takes");
    let mr = null, chunks = [], t0 = 0, timer = null;
    b.onclick = async () => {
      if (mr && mr.state === "recording") { mr.stop(); return; }
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mr = new MediaRecorder(stream); chunks = [];
        mr.ondataavailable = e => chunks.push(e.data);
        mr.onstop = () => {
          stream.getTracks().forEach(t => t.stop()); clearInterval(timer);
          const url = URL.createObjectURL(new Blob(chunks, { type: mr.mimeType }));
          const row = el("div", "take", `<span>Grabación ${takes.children.length + 1}</span>`);
          const au = document.createElement("audio"); au.controls = true; au.src = url; row.append(au);
          takes.prepend(row); b.textContent = "● Grabar otra vez"; b.classList.remove("on"); st.textContent = "";
        };
        mr.start(); t0 = Date.now(); b.textContent = "■ Detener"; b.classList.add("on");
        timer = setInterval(() => st.textContent = "Grabando… " + Math.floor((Date.now() - t0) / 1000) + " s", 250);
      } catch (e) { st.textContent = "No se pudo usar el micrófono. Revisa el permiso del navegador."; }
    };
    return box;
  }

  // ---------- ayudas para textos abiertos ----------
  function sentences(text) { return text.split(/(?<=[.!?])\s+|\n+/).map(s => s.trim()).filter(s => /[a-z]/i.test(s)); }
  function capsOk(text) { const ss = sentences(text); return ss.length > 0 && ss.every(s => /^[^a-z]*[A-Z0-9¡¿"*(]/.test(s) && /[.!?)"*]$/.test(s)); }
  function autoHint(rule, text) {
    if (!rule || !text.trim()) return null;
    if (rule === "caps") return capsOk(text);
    try { return new RegExp(rule, "is").test(text.toLowerCase()) || new RegExp(rule, "ism").test(text.toLowerCase()); } catch (e) { return null; }
  }

  // ---------- un mini-test ----------
  function renderTest(tid, sk) {
    const th = DATA[tid], t = th && th.tests[sk];
    if (!t) { renderIndex(); return; }
    document.title = `${SKN[sk]} · Tema ${themeLabel(tid)} · ${BRAND}`;
    const key = `ans:${tid}/${sk}`, saved = store.get(key, {});
    const save = () => store.set(key, saved);
    app.innerHTML = "";
    const top = el("div", "crumbs", `<a href="#">← Todos los mini-tests</a>`);
    app.append(top);
    const sbar = studentBar(() => renderTest(tid, sk)); app.append(sbar);
    app.append(el("p", "kicker", `${esc(th.scenario)} · Tema ${themeLabel(tid)}: ${esc(th.title)}`));
    app.append(el("h1", null, `Mini-test de ${SKN[sk]}${sk === "speaking" ? " (examen oral)" : ""}`));
    const tip = el("div", "tip"); tip.innerHTML = `<b>Consejo para la prueba</b>` + t.tip.map(x => `<p>${md(x)}</p>`).join(""); app.append(tip);

    const graders = []; // funciones que devuelven puntos
    let details = [];   // detalle para enviar y para la imagen: {n, q, given, correct, ok} o {open, text, checks, pts}
    let qn = 0;
    t.parts.forEach((part, pi) => {
      const sec = el("section", "part" + (part.reading ? " has-reading" : ""));
      const left = el("div", "pleft"), right = el("div", "pright");
      if (part.intro) left.append(el("p", "intro", md(part.intro)));
      if (part.audio) left.append(player(tid, part.audio));
      if (part.reading) {
        const r = el("div", "reading"); r.innerHTML = `<h3>${esc(part.reading.title)}</h3>` + part.reading.paras.map(p => `<p>${md(p)}</p>`).join("");
        left.append(r);
      }
      if (part.pics) left.append(el("div", "pstrip", part.pics.map(([img, cap]) => `<figure><img src="img/${esc(img)}.png" alt=""><figcaption>${md(cap)}</figcaption></figure>`).join("")));
      if (part.note) { const n = el("div", "note"); n.innerHTML = `<b>${esc(part.note[0])}</b>` + part.note.slice(1).map(x => `<p>${md(x)}</p>`).join(""); left.append(n); }
      (part.qs || []).forEach(q => {
        qn++; const id = `q${qn}`;
        const box = el("div", "q"); box.dataset.id = id;
        const fb = el("div", "fb");
        if (q.t === "mc" || q.t === "tf") {
          const pics = q.t === "mc" && q.opts.every(isPic);
          const opts = q.t === "mc" ? q.opts.map((o, i) => [i, pics ? picHTML(o, LET[i]) : esc(`${LET[i]}) ${o}`)]) : [[true, "True"], [false, "False"]];
          if (q.img) box.append(el("div", "qimg", `<img src="img/${esc(q.img)}.png" alt="">`));
          box.append(el("p", "qt", `<span class="n">${qn}.</span> ${md(q.q)}`));
          const row = el("div", "opts" + (q.t === "tf" ? " tf" : "") + (pics ? " pics" : ""));
          opts.forEach(([val, label]) => {
            const b = el("button", "opt", label); b.type = "button";
            if (saved[id] === val) b.classList.add("sel");
            b.onclick = () => { if (box.classList.contains("done")) return; saved[id] = val; save(); row.querySelectorAll(".opt").forEach(x => x.classList.toggle("sel", x === b)); };
            b.dataset.val = String(val); row.append(b);
          });
          box.append(row);
          graders.push(() => {
            const ok = saved[id] === q.a;
            row.querySelectorAll(".opt").forEach(x => { if (x.dataset.val === String(q.a)) x.classList.add("right"); else if (x.classList.contains("sel")) x.classList.add("wrong"); });
            return ok;
          });
        } else if (q.t === "short") {
          if (q.img) box.append(el("div", "qimg", `<img src="img/${esc(q.img)}.png" alt="">`));
          const parts = q.q.split(/_{3,}/); const p = el("p", "qt");
          p.innerHTML = `<span class="n">${qn}.</span> `;
          const inputs = [];
          parts.forEach((txt, i) => {
            p.append(Object.assign(document.createElement("span"), { innerHTML: md(txt) }));
            if (i < parts.length - 1) {
              const inp = el("input", "blank"); inp.type = "text"; inp.autocomplete = "off"; inp.spellcheck = false;
              inp.value = (saved[id] || [])[i] || ""; inp.setAttribute("aria-label", "Respuesta " + qn);
              inp.oninput = () => { const v = saved[id] || []; v[i] = inp.value; saved[id] = v; save(); };
              inputs.push(inp); p.append(inp);
            }
          });
          box.append(p);
          graders.push(() => { const ok = inputs.every((inp, i) => accepts(inp.value, q.accept[i] || q.accept[0])); inputs.forEach(x => x.classList.add(ok ? "right" : "wrong")); return ok; });
        } else if (q.t === "fix") {
          box.append(el("p", "qt", `<span class="n">${qn}.</span> <span class="wrongs">${md(q.q)}</span>`));
          const inp = el("input", "fixin"); inp.type = "text"; inp.placeholder = "Escribe la oración corregida"; inp.autocomplete = "off"; inp.spellcheck = false;
          inp.value = saved[id] || ""; inp.oninput = () => { saved[id] = inp.value; save(); };
          box.append(inp);
          graders.push(() => { const ok = accepts(inp.value, q.accept); inp.classList.add(ok ? "right" : "wrong"); return ok; });
        }
        box.append(fb);
        const g = graders.pop();
        graders.push(() => {
          const v = saved[id], blank = v == null || v === "" || (Array.isArray(v) && !v.some(x => x && String(x).trim()));
          const ok = g();
          box.classList.add("done", ok ? "is-right" : "is-wrong");
          const ans = q.t === "mc" ? (isPic(q.opts[q.a]) ? `${LET[q.a]}) ${picCap(q.opts[q.a]) || q.pic_answer || picName(q.opts[q.a])}` : `${LET[q.a]}) ${q.opts[q.a]}`) : q.t === "tf" ? (q.a ? "True" : "False") : q.show.replace(/\*\*/g, "");
          fb.innerHTML = (ok ? `<b class="ok">✓ ¡Correcto!</b>` : `<b class="no">${blank ? "Sin responder." : "✗"} Respuesta correcta:</b> ${md(q.t === "fix" || q.t === "short" ? q.show : ans)}`) +
            (q.exp ? `<p>${md(q.exp)}</p>` : "");
          box.querySelectorAll("input").forEach(x => x.readOnly = true);
          const optLabel = i => isPic(q.opts[i]) ? `${LET[i]}) ${picCap(q.opts[i]) || q.pic_answer || picName(q.opts[i])}` : `${LET[i]}) ${q.opts[i]}`;
          const given = blank ? "" : q.t === "mc" ? optLabel(v) : q.t === "tf" ? (v ? "True" : "False") : Array.isArray(v) ? v.join(" / ") : String(v);
          details.push({ n: details.filter(d => d.n).length + 1, q: plain(q.q), given, correct: plain(q.t === "fix" || q.t === "short" ? q.show : ans), ok });
          return ok ? 1 : 0;
        });
        right.append(box);
      });
      const op = part.open;
      if (op) {
        const ob = el("div", "open");
        if (op.record) ob.append(recorder());
        let ta = null;
        if (op.lines) {
          ta = el("textarea", "wr"); ta.rows = Math.max(4, op.lines + 1); ta.placeholder = "Escribe aquí tu respuesta en inglés…";
          ta.value = saved[`o${pi}`] || ""; ta.spellcheck = false;
          const cnt = el("div", "cnt");
          const upd = () => {
            const n = sentences(ta.value).length;
            cnt.textContent = `${n} ${n === 1 ? "oración" : "oraciones"}` + (op.min_sent ? ` · se piden ${op.min_sent === op.max_sent ? op.min_sent : op.min_sent + " a " + op.max_sent}` : "");
            cnt.className = "cnt" + (op.min_sent && n >= op.min_sent && n <= op.max_sent ? " good" : "");
            ob.querySelectorAll(".chk").forEach(c => {
              const h = autoHint(c.dataset.auto, ta.value), hint = c.querySelector(".hint");
              hint.textContent = h == null ? "" : h ? "parece que sí" : "no lo encuentro"; hint.className = "hint " + (h == null ? "" : h ? "yes" : "nope");
            });
          };
          ta.oninput = () => { saved[`o${pi}`] = ta.value; save(); upd(); };
          ob.append(ta, cnt); setTimeout(upd, 0);
        }
        ob.append(el("p", "chkintro", md(op.check_intro || "Marca un punto por cada casilla:")));
        const list = el("div", "checks");
        op.checklist.forEach((c, ci) => {
          const lab = el("label", "chk"); lab.dataset.auto = c.auto || "";
          const cb = el("input"); cb.type = "checkbox"; cb.checked = !!(saved[`c${pi}`] || [])[ci];
          cb.onchange = () => { const v = saved[`c${pi}`] || []; v[ci] = cb.checked; saved[`c${pi}`] = v; save(); };
          lab.append(cb, el("span", "ct", md(c.text)), el("span", "hint"));
          list.append(lab);
        });
        ob.append(list);
        if (op.sample) {
          const d = el("details", "sample"); d.innerHTML = `<summary>Ver un ejemplo de respuesta (solo después de escribir la tuya)</summary><p><i>${esc(op.sample)}</i></p>`;
          ob.append(d);
        }
        right.append(ob);
        graders.push(() => {
          list.querySelectorAll("input").forEach(x => x.disabled = true); if (ta) ta.readOnly = true;
          const checks = op.checklist.map((c, ci) => ({ text: plain(c.text), on: list.querySelectorAll("input")[ci].checked }));
          const pts = checks.filter(c => c.on).length;
          details.push({ open: true, intro: plain(part.intro || ""), text: ta ? ta.value.trim() : "", checks, pts });
          return pts;
        });
      }
      sec.append(left, right);
      app.append(sec);
    });

    const actions = el("div", "actions");
    const check = el("button", "btn big", "Revisar mis respuestas"); check.type = "button";
    const result = el("div", "result");
    actions.append(check);
    app.append(result, actions);
    check.onclick = () => {
      if (SEND_URL && !student.get() && !student.guest()) { alert("Primero escribe tu PIN (arriba) o elige «Practicar sin registrarme»."); sbar.scrollIntoView({ behavior: "smooth" }); sbar.querySelector("input")?.focus(); return; }
      const unanswered = qn - Object.keys(saved).filter(k => /^q\d+$/.test(k) && (Array.isArray(saved[k]) ? saved[k].some(Boolean) : saved[k] !== "" && saved[k] != null)).length;
      if (unanswered > 0 && !confirm(`Te faltan ${unanswered} pregunta(s) por responder. ¿Revisar de todos modos?`)) return;
      details = [];
      const pts = graders.reduce((s, g) => s + g(), 0);
      const pct = pts / t.total;
      const best = store.get(`best:${tid}/${sk}`, null);
      if (best == null || pts > best) store.set(`best:${tid}/${sk}`, pts);
      store.set(`last:${tid}/${sk}`, { pts, at: Date.now() });
      const msg = pct >= 0.8 ? "¡Estás listo para la prueba!" : pct >= 0.5 ? "Vas bien. Lee las explicaciones de lo que fallaste y vuelve a intentarlo." : "Necesitas repasar un poco antes de la prueba.";
      result.className = "result show " + (pct >= 0.8 ? "ok" : pct >= 0.5 ? "mid" : "low");
      result.innerHTML = `<div class="score">${pts} / ${t.total}</div><p class="msg">${msg}</p>` +
        (pct < 0.8 ? `<p><b>Qué repasar en tu libro (Tema ${themeLabel(tid)}):</b> ${md(t.review)}</p>` : "") +
        `<p class="small">Las respuestas abiertas cuentan según las casillas que marcaste. Sé honesto contigo mismo.</p>`;
      actions.innerHTML = "";
      const rec = { st: student.get(), tid, sk, th, t, pts, nota: nota(pts, t.total), at: new Date(), details };
      const share = el("div", "share");
      if (SEND_URL && rec.st) share.append(sendButton(rec));
      const img = el("button", "btn ghost", "Guardar imagen del resultado"); img.type = "button";
      img.onclick = () => saveImage(rec, img);
      share.append(img);
      result.append(share);
      const again = el("button", "btn", "Intentar de nuevo"); again.type = "button";
      again.onclick = () => { store.del(key); renderTest(tid, sk); window.scrollTo(0, 0); };
      const back = el("a", "btn ghost", "Todos los mini-tests"); back.href = "#";
      actions.append(again, back);
      result.scrollIntoView({ behavior: "smooth", block: "center" });
    };
    window.scrollTo(0, 0);
  }

  // ---------- nota (escala 1.0 a 5.0) ----------
  const nota = (pts, total) => Math.round((1 + 4 * pts / total) * 10) / 10;
  const fmtDate = d => d.toLocaleDateString("es-PA", { day: "2-digit", month: "2-digit", year: "numeric" }) + " " + d.toLocaleTimeString("es-PA", { hour: "2-digit", minute: "2-digit" });
  const detailText = r => r.details.map(d => d.open
      ? `[Abierta${d.text ? ": " + d.text : ""}] ${d.checks.map(c => (c.on ? "☑ " : "☐ ") + c.text).join("; ")}`
      : `${d.n}. ${d.ok ? "✓" : "✗"}${d.ok ? "" : ` (respondió: ${d.given || "—"}; correcta: ${d.correct})`}`).join(" | ");

  // ---------- enviar al maestro (Google Sheets por Apps Script) ----------
  function sendButton(r) {
    const wrap = el("span", "sendwrap");
    const b = el("button", "btn", "Enviar a mi maestro"); b.type = "button";
    const msg = el("span", "sendmsg");
    b.onclick = async () => {
      b.disabled = true; b.textContent = "Enviando…"; msg.textContent = "";
      const data = { pin: r.st.pin, tema: themeLabel(r.tid), tema_titulo: r.th.title, destreza: SKN[r.sk],
        puntaje: r.pts, total: r.t.total, detalle: detailText(r) };
      try {
        const j = await api("submit", data);
        if (!j.ok) throw new Error(j.error || "error");
        b.textContent = "✓ Enviado"; b.classList.add("sent");
        msg.textContent = `Tu maestro ya recibió tu resultado (intento ${j.intento}).`;
        if (progress) { const k = `${data.tema}/${data.destreza}`, p = progress[k] || { best: 0, total: data.total, veces: 0 }; p.best = Math.max(p.best, data.puntaje); p.veces++; progress[k] = p; }
      } catch (e) {
        if (navigator.onLine === false || e instanceof TypeError) {
          queue.add(data); b.textContent = "En espera"; b.classList.add("sent");
          msg.textContent = "No hay internet. Tu resultado se enviará solo cuando vuelva la conexión.";
        } else {
          b.disabled = false; b.textContent = "Enviar a mi maestro";
          msg.textContent = "No se pudo enviar. Vuelve a intentarlo.";
        }
      }
    };
    wrap.append(b, msg);
    return wrap;
  }

  // ---------- guardar imagen del resultado corregido ----------
  function loadH2C() {
    return window.html2canvas ? Promise.resolve() : new Promise((ok, no) => {
      const sc = document.createElement("script"); sc.src = "../html2canvas.min.js"; sc.onload = ok; sc.onerror = no; document.head.append(sc);
    });
  }
  async function saveImage(r, btn) {
    btn.disabled = true; const label = btn.textContent; btn.textContent = "Preparando…";
    const card = el("div", "rcard");
    const rows = r.details.map(d => d.open
      ? `<div class="rq open"><b>Respuesta abierta (${d.pts} ${d.pts === 1 ? "punto" : "puntos"})</b>${d.text ? `<p class="rtext">${esc(d.text)}</p>` : ""}${d.checks.map(c => `<div>${c.on ? "☑" : "☐"} ${esc(c.text)}</div>`).join("")}</div>`
      : `<div class="rq ${d.ok ? "ok" : "no"}"><span class="mk">${d.ok ? "✓" : "✗"}</span><div><b>${d.n}.</b> ${esc(d.q || "")}<div>Mi respuesta: <b>${esc(d.given || "—")}</b>${d.ok ? "" : ` · Correcta: <b>${esc(d.correct)}</b>`}</div></div></div>`).join("");
    card.innerHTML = `<div class="rhead"><div><div class="rk">${esc(META.title)} · ${esc(META.name)} · ${esc(META.trimester)}</div>
      <h2>Mini-test de ${SKN[r.sk]} · Tema ${themeLabel(r.tid)}</h2><div>${esc(r.th.title)}</div></div>
      <div class="rscore">${r.pts} / ${r.t.total}<small>Nota ${r.nota.toFixed(1)}</small></div></div>
      <div class="rwho">${r.st ? `<b>${esc(r.st.name)}</b> · ` : ""}${esc(META.name)} · ${fmtDate(r.at)}</div>${rows}`;
    document.body.append(card);
    try {
      await loadH2C();
      const canvas = await window.html2canvas(card, { backgroundColor: "#ffffff", scale: 2 });
      const a = document.createElement("a");
      const safe = s => s.normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/[^\w]+/g, "-").replace(/^-|-$/g, "");
      a.download = `resultado-${r.st ? safe(r.st.name) + "-" : ""}${META.grade}-${r.tid}-${r.sk}.png`;
      a.href = canvas.toDataURL("image/png"); document.body.append(a); a.click(); a.remove();
      btn.textContent = "✓ Imagen guardada";
    } catch (e) {
      btn.textContent = label; alert("No se pudo crear la imagen en este navegador.");
    } finally { card.remove(); btn.disabled = false; }
  }

  function route() {
    const h = decodeURIComponent(location.hash.replace(/^#\/?/, ""));
    const m = h.match(/^(\d-\d)\/(\w+)$/);
    if (m) renderTest(m[1], m[2]); else renderIndex();
  }
  window.addEventListener("hashchange", route);
  queue.flush();
  route();
})();
