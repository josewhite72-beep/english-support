/**
 * English Support · Notas finales del III Trimestre (evaluación de emergencia post-terremoto)
 * C.E.B.G. Barrigón · José White · PanaMentorLabs
 *
 * Reglas:
 *   - 4 notas por estudiante: una por tema (5-1, 5-2, 6-1, 6-2) = 2 por scenario.
 *   - Cada nota = promedio de Listening, Reading y Writing de ese tema.
 *     (Speaking y Mediation NO se toman en cuenta.)
 *   - Nota de cada destreza = promedio del PRIMER y el ÚLTIMO intento.
 *     Si hizo un solo intento, cuenta ese.
 *   - Si le falta una destreza, se promedian solo las que hizo.
 *   - Si no hizo ninguna destreza del tema, la nota queda vacía.
 *   - Escala 1.0 a 5.0, un decimal.
 *
 * Dos formas de usarlo:
 *   1. Página del docente (english-support-six.vercel.app/docente): botón "Notas" → descarga un Excel
 *      calculado en ese momento. Necesita la clave del docente (ver definirClaveDocente).
 *   2. En la hoja: función calcularNotasFinales → crea pestañas "Notas Grado X".
 */

const NF_TEMAS = ["5-1", "5-2", "6-1", "6-2"];
const NF_DESTREZAS = ["listening", "reading", "writing"];
const NF_ABREV = { listening: "L", reading: "R", writing: "W" };
const NF_PROP_CLAVE = "CLAVE_DOCENTE";

// ------------------------------------------------------------- cálculo ----
// Devuelve [{ grade, filas: [{ nombre, notas: [4], detalle: [12] }] }] (vacío = "")
function datosNotas_() {
  const ss = SpreadsheetApp.getActive();
  const alumnos = studentsFresh_();
  const salida = [];

  GRADES.forEach(grade => {
    const sh = ss.getSheetByName("Grado " + grade);
    const lista = alumnos.filter(s => s.grade === grade);

    const datos = {};     // pin -> tema -> destreza -> [{intento, fecha, nota}]
    const nombres = {};   // pin -> nombre en la hoja (por si ya no está en la lista)
    if (sh && sh.getLastRow() > 1) {
      sh.getRange(2, 1, sh.getLastRow() - 1, 11).getValues().forEach(r => {
        const pin = pin4_(r[10]);
        const tema = String(r[2]).replace(/^'/, "").trim();
        const destreza = String(r[4]).trim().toLowerCase();
        if (!pin || NF_TEMAS.indexOf(tema) < 0 || NF_DESTREZAS.indexOf(destreza) < 0) return;
        let nota = Number(r[7]);
        if (!nota) {
          const pts = Number(r[5]) || 0, total = Number(r[6]) || 0;
          if (!total) return;
          nota = 1 + 4 * pts / total;
        }
        nombres[pin] = nombres[pin] || String(r[1]);
        datos[pin] = datos[pin] || {};
        datos[pin][tema] = datos[pin][tema] || {};
        (datos[pin][tema][destreza] = datos[pin][tema][destreza] || [])
          .push({ intento: Number(r[8]) || 0, fecha: new Date(r[0]).getTime() || 0, nota: nota });
      });
    }

    const pines = lista.map(s => s.pin);
    Object.keys(datos).forEach(p => { if (pines.indexOf(p) < 0) pines.push(p); });
    if (!pines.length) return;
    const nombreDe = p => (lista.find(s => s.pin === p) || {}).name || nombres[p] || p;
    pines.sort((a, b) => nombreDe(a).localeCompare(nombreDe(b), "es"));

    const filas = pines.map(pin => {
      const notas = [], detalle = [];
      NF_TEMAS.forEach(tema => {
        const porDestreza = NF_DESTREZAS.map(d => notaDestreza_(((datos[pin] || {})[tema] || {})[d]));
        porDestreza.forEach(n => detalle.push(n === null ? "" : n));
        const hechas = porDestreza.filter(n => n !== null);
        notas.push(hechas.length ? redondear_(hechas.reduce((a, b) => a + b, 0) / hechas.length) : "");
      });
      return { nombre: nombreDe(pin), notas: notas, detalle: detalle };
    });
    salida.push({ grade: grade, filas: filas });
  });
  return salida;
}

// Promedio del primer y el último intento (o el único). null si no hizo la destreza.
function notaDestreza_(intentos) {
  if (!intentos || !intentos.length) return null;
  const orden = intentos.slice().sort((a, b) => (a.intento - b.intento) || (a.fecha - b.fecha));
  const primero = orden[0].nota, ultimo = orden[orden.length - 1].nota;
  return redondear_(orden.length === 1 ? primero : (primero + ultimo) / 2);
}

function redondear_(n) { return Math.round(n * 10 + 1e-9) / 10; }

// ------------------------------------------ acción web: página del docente ----
function notas_(d) {
  const clave = PropertiesService.getScriptProperties().getProperty(NF_PROP_CLAVE);
  if (!clave) return { ok: false, error: "Falta definir la clave del docente en la hoja." };
  if (String(d.clave || "") !== clave) { Utilities.sleep(2000); return { ok: false, error: "Clave incorrecta" }; }
  return {
    ok: true,
    generado: new Date().toISOString(),
    temas: NF_TEMAS,
    destrezas: NF_DESTREZAS.map(x => NF_ABREV[x]),
    grados: datosNotas_()
  };
}

// Pide la clave en la hoja (menú English Support → Definir clave del docente)
function definirClaveDocente() {
  const ui = SpreadsheetApp.getUi();
  const r = ui.prompt("Clave del docente",
    "Escribe la clave para la página del docente (mínimo 6 caracteres).\nSolo tú debes conocerla.",
    ui.ButtonSet.OK_CANCEL);
  if (r.getSelectedButton() !== ui.Button.OK) return;
  const clave = r.getResponseText().trim();
  if (clave.length < 6) { ui.alert("La clave debe tener al menos 6 caracteres."); return; }
  PropertiesService.getScriptProperties().setProperty(NF_PROP_CLAVE, clave);
  ui.alert("Clave guardada. Úsala en english-support-six.vercel.app/docente");
}

// ------------------------------------------- pestañas "Notas Grado X" en la hoja ----
function calcularNotasFinales() {
  const ss = SpreadsheetApp.getActive();
  const resumen = [];
  datosNotas_().forEach(({ grade, filas }) => {
    const enc1 = ["Estudiante", "Nota 1", "Nota 2", "Nota 3", "Nota 4", ""];
    const enc2 = ["", "Scenario 5 · Tema 5-1", "Scenario 5 · Tema 5-2", "Scenario 6 · Tema 6-1", "Scenario 6 · Tema 6-2", ""];
    NF_TEMAS.forEach(t => NF_DESTREZAS.forEach(d => { enc1.push(t + " " + NF_ABREV[d]); enc2.push(""); }));
    enc2[6] = "Detalle por destreza (promedio 1.º y último intento)";
    const valores = filas.map(f => [f.nombre].concat(f.notas, [""], f.detalle));
    const ancho = enc1.length;

    const nombreHoja = "Notas Grado " + grade;
    let out = ss.getSheetByName(nombreHoja);
    if (out) out.clear(); else out = ss.insertSheet(nombreHoja);
    out.getRange(1, 1, 1, ancho).setValues([enc1]).setFontWeight("bold");
    out.getRange(2, 1, 1, ancho).setValues([enc2]).setFontStyle("italic");
    out.getRange(3, 1, valores.length, ancho).setValues(valores);

    [out.getRange(1, 1, valores.length + 2, 5), out.getRange(1, 7, valores.length + 2, ancho - 6)].forEach(rg => rg
      .setBackground("#ffffff").setFontColor("#000000")
      .setBorder(true, true, true, true, true, true, "#000000", SpreadsheetApp.BorderStyle.SOLID));
    out.getRange(3, 2, valores.length, ancho - 1).setNumberFormat("0.0").setHorizontalAlignment("center");
    out.getRange(1, 2, 2, ancho - 1).setHorizontalAlignment("center").setWrap(true);
    out.setFrozenRows(2);
    out.setFrozenColumns(1);
    out.autoResizeColumn(1);
    out.setColumnWidths(2, 4, 110);
    out.setColumnWidth(6, 20);
    out.setColumnWidths(7, ancho - 6, 60);
    resumen.push(nombreHoja + ": " + valores.length + " estudiantes");
  });
  const msg = resumen.length ? "Notas calculadas:\n\n" + resumen.join("\n") : "No se encontraron resultados.";
  try { SpreadsheetApp.getUi().alert(msg); } catch (e) { Logger.log(msg); }
}
