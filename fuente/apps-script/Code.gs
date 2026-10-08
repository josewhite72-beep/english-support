/**
 * English Support · Registro de mini-tests (Google Apps Script)
 * C.E.B.G. Barrigón · José White · PanaMentorLabs
 *
 * Esta hoja es PRIVADA. Guarda:
 *   - "Estudiantes": Nombre | Grado | PIN   (la lista; nunca se publica en el sitio)
 *   - "Grado K", "Grado 1" ... "Grado 6": un renglón por cada resultado enviado
 *
 * El sitio (english-support-six.vercel.app) solo puede:
 *   - login:    mandar un PIN y recibir el nombre de ESE estudiante
 *   - progress: recibir el mejor puntaje de ese estudiante en cada mini-test
 *   - submit:   guardar un resultado (el nombre y el grado salen de la lista, no del navegador)
 *
 * Instalación: ver INSTRUCCIONES.md
 */

const SHEET_STUDENTS = "Estudiantes";
const GRADES = ["K", "1", "2", "3", "4", "5", "6"];
const RESULT_HEADER = ["Fecha", "Estudiante", "Tema", "Título del tema", "Destreza", "Puntaje", "Total", "Nota (1-5)", "Intento", "Detalle", "PIN", "ID"];

// ---------------------------------------------------------------- web app ----
function doPost(e) {
  let data = {};
  try { data = JSON.parse(e.postData.contents || "{}"); } catch (err) { return out_({ ok: false, error: "datos inválidos" }); }
  try {
    if (data.action === "login") return out_(login_(data));
    if (data.action === "progress") return out_(progress_(data));
    if (data.action === "submit") return out_(submit_(data));
    return out_({ ok: false, error: "acción desconocida" });
  } catch (err) {
    return out_({ ok: false, error: String(err.message || err) });
  }
}

function doGet() {
  return out_({ ok: true, service: "English Support", time: new Date().toISOString() });
}

function out_(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}

// --------------------------------------------------------------- acciones ----
function login_(d) {
  const st = findStudent_(d.pin);
  if (!st) { Utilities.sleep(1500); return { ok: false, error: "PIN no encontrado" }; }  // la espera frena a quien prueba PIN al azar
  if (d.grado && st.grade !== String(d.grado)) {
    return { ok: false, error: "grado", grado_correcto: st.grade, nombre: firstName_(st.name) };
  }
  return { ok: true, nombre: st.name, grado: st.grade };
}

function progress_(d) {
  const st = findStudent_(d.pin);
  if (!st) { Utilities.sleep(1500); return { ok: false, error: "PIN no encontrado" }; }
  const sh = SpreadsheetApp.getActive().getSheetByName("Grado " + st.grade);
  const best = {};
  if (sh && sh.getLastRow() > 1) {
    const rows = sh.getRange(2, 1, sh.getLastRow() - 1, RESULT_HEADER.length).getValues();
    rows.forEach(r => {
      if (pin4_(r[10]) !== st.pin) return;
      const key = r[2] + "/" + r[4];               // "5.1/Listening"
      const b = best[key] || { best: 0, total: r[6], veces: 0 };
      b.best = Math.max(b.best, Number(r[5]) || 0); b.veces++;
      best[key] = b;
    });
  }
  return { ok: true, progreso: best };
}

function submit_(d) {
  const st = findStudent_(d.pin);
  if (!st) { Utilities.sleep(1500); return { ok: false, error: "PIN no encontrado" }; }
  const lock = LockService.getScriptLock();
  lock.waitLock(20000);
  try {
    const sh = gradeSheet_(st.grade);
    ensureIdColumn_(sh);
    let attempt = 1;
    if (sh.getLastRow() > 1) {
      const rows = sh.getRange(2, 1, sh.getLastRow() - 1, RESULT_HEADER.length).getValues();
      // el mismo resultado enviado dos veces (se cortó la respuesta y el estudiante volvió a tocar Enviar): no se duplica
      const dup = d.id ? rows.find(r => String(r[11]) === String(d.id)) : null;
      if (dup) return { ok: true, intento: dup[8], nombre: st.name, repetido: true };
      attempt += rows.filter(r => pin4_(r[10]) === st.pin && String(r[2]) === String(d.tema) && String(r[4]) === String(d.destreza)).length;
    }
    const total = Number(d.total) || 0, pts = Math.max(0, Math.min(Number(d.puntaje) || 0, total));
    const nota = total ? Math.round((1 + 4 * pts / total) * 10) / 10 : "";
    // el apóstrofo guarda "5.1" y el PIN como texto (si no, la hoja los convierte en números)
    sh.appendRow([new Date(), st.name, "'" + String(d.tema || ""), String(d.tema_titulo || ""), String(d.destreza || ""),
                  pts, total, nota, attempt, String(d.detalle || "").slice(0, 45000), "'" + st.pin, String(d.id || "")]);
    return { ok: true, intento: attempt, nombre: st.name };
  } finally {
    lock.releaseLock();
  }
}

// ---------------------------------------------------------------- ayudas ----
function students_() {
  const cache = CacheService.getScriptCache();
  const hit = cache.get("students");
  if (hit) return JSON.parse(hit);
  const sh = SpreadsheetApp.getActive().getSheetByName(SHEET_STUDENTS);
  if (!sh || sh.getLastRow() < 2) return [];
  const list = sh.getRange(2, 1, sh.getLastRow() - 1, 3).getValues()
    .filter(r => r[0] && r[2])
    .map(r => ({ name: String(r[0]).trim(), grade: normGrade_(r[1]), pin: pin4_(r[2]) }));
  cache.put("students", JSON.stringify(list), 300);  // 5 minutos
  return list;
}

function findStudent_(pin) {
  pin = String(pin || "").replace(/\D/g, "");
  if (pin.length !== 4) return null;
  return students_().find(s => s.pin === pin) || null;
}

function normGrade_(g) {
  g = String(g || "").trim().toLowerCase();
  if (g.startsWith("k") || g.includes("kinder") || g.includes("kínder") || g.includes("pre")) return "K";
  const m = g.match(/\d/);
  return m ? m[0] : g;
}

function pin4_(v) { return String(v == null ? "" : v).replace(/^'/, "").trim().padStart(4, "0"); }

function firstName_(n) { return String(n).split(" ")[0]; }

function gradeSheet_(grade) {
  const ss = SpreadsheetApp.getActive();
  const name = "Grado " + grade;
  let sh = ss.getSheetByName(name);
  if (!sh) {
    sh = ss.insertSheet(name);
    sh.appendRow(RESULT_HEADER);
    sh.getRange(1, 1, 1, RESULT_HEADER.length).setFontWeight("bold");
    sh.setFrozenRows(1);
    sh.setColumnWidth(10, 420);
    sh.hideColumns(11, 2);                    // PIN e ID: ocultos, solo para el progreso y evitar duplicados
  }
  return sh;
}

// Las pestañas creadas con la versión anterior tenían 11 columnas: se agrega la columna ID (oculta)
function ensureIdColumn_(sh) {
  if (sh.getMaxColumns() < 12) sh.insertColumnsAfter(sh.getMaxColumns(), 12 - sh.getMaxColumns());
  if (String(sh.getRange(1, 12).getValue()) !== "ID") { sh.getRange(1, 12).setValue("ID"); sh.hideColumns(12); }
}

// ------------------------------------------------- menú de la hoja (maestro) ----
function onOpen() {
  SpreadsheetApp.getUi().createMenu("English Support")
    .addItem("Agregar estudiante (genera PIN)", "menuAddStudent")
    .addItem("Revisar la lista (PIN repetidos o vacíos)", "menuCheckList")
    .addItem("Preparar pestañas de resultados", "menuSetup")
    .addToUi();
}

function menuAddStudent() {
  const ui = SpreadsheetApp.getUi();
  const n = ui.prompt("Agregar estudiante", "Nombre y apellidos:", ui.ButtonSet.OK_CANCEL);
  if (n.getSelectedButton() !== ui.Button.OK || !n.getResponseText().trim()) return;
  const g = ui.prompt("Agregar estudiante", "Grado (K, 1, 2, 3, 4, 5 o 6):", ui.ButtonSet.OK_CANCEL);
  if (g.getSelectedButton() !== ui.Button.OK) return;
  const grade = normGrade_(g.getResponseText());
  if (GRADES.indexOf(grade) < 0) { ui.alert("Grado no válido: " + g.getResponseText()); return; }
  const used = new Set(studentsFresh_().map(s => s.pin));
  let pin;
  do { pin = String(1000 + Math.floor(Math.random() * 9000)); } while (used.has(pin));
  const sh = SpreadsheetApp.getActive().getSheetByName(SHEET_STUDENTS);
  sh.appendRow([n.getResponseText().trim(), grade === "K" ? "Kinder" : grade + "° Grado", pin]);
  CacheService.getScriptCache().remove("students");
  ui.alert("Estudiante agregado.\n\n" + n.getResponseText().trim() + "\nPIN: " + pin);
}

function menuCheckList() {
  const list = studentsFresh_(), seen = {}, rep = [], bad = [];
  list.forEach(s => {
    if (!/^\d{4}$/.test(s.pin)) bad.push(s.name + " (" + s.pin + ")");
    if (GRADES.indexOf(s.grade) < 0) bad.push(s.name + ": grado \"" + s.grade + "\"");
    if (seen[s.pin]) rep.push(s.pin + ": " + seen[s.pin] + " y " + s.name); else seen[s.pin] = s.name;
  });
  CacheService.getScriptCache().remove("students");
  SpreadsheetApp.getUi().alert(list.length + " estudiantes.\n\n" +
    (rep.length ? "PIN repetidos:\n" + rep.join("\n") + "\n\n" : "No hay PIN repetidos.\n\n") +
    (bad.length ? "Revisar:\n" + bad.join("\n") : "Todos los grados y PIN están bien."));
}

function menuSetup() {
  GRADES.forEach(g => ensureIdColumn_(gradeSheet_(g)));
  SpreadsheetApp.getUi().alert("Listo: pestañas Grado K a Grado 6.");
}

function studentsFresh_() {
  CacheService.getScriptCache().remove("students");
  return students_();
}
