# Registro de mini-tests en Google Sheets (una sola vez)

Hazlo desde una **computadora** (en el celular, Apps Script no funciona bien).

## 1. Crear la hoja
1. Sube `English Support - Registro de mini-tests.xlsx` a tu Google Drive.
2. Ábrelo y elige **Archivo → Guardar como Hojas de cálculo de Google**. Trabaja siempre en esa copia.
3. Borra el .xlsx de Drive: tiene la lista con los PIN.

## 2. Pegar el script
1. En la hoja: **Extensiones → Apps Script**.
2. Borra lo que aparece y pega todo el contenido de `Code.gs`.
3. Toca **Guardar** (el ícono del disquete).

## 3. Publicarlo como aplicación web
1. **Implementar → Nueva implementación**.
2. En el engranaje, elige **Aplicación web**.
3. **Ejecutar como:** Yo. **Quién tiene acceso:** Cualquier persona.
   (Los estudiantes no tienen cuenta de Google. El script solo devuelve el nombre del PIN que se escribe, nunca la lista.)
4. **Implementar** → **Autorizar acceso** → elige tu cuenta → **Configuración avanzada → Ir a … (no seguro)** → **Permitir**.
   (El aviso sale porque el script es tuyo y no está verificado por Google.)
5. Copia la **URL de la aplicación web** (termina en `/exec`) y envíamela.

## 4. Uso diario
- **Ver resultados:** pestañas *Grado K* a *Grado 6*. Una fila por cada envío, con la nota de 1 a 5 y el número de intento.
- **Agregar un estudiante:** menú **English Support → Agregar estudiante** (crea un PIN que no se repite).
- **Cambiar un nombre o eliminar un estudiante:** edita o borra su fila en la pestaña *Estudiantes*. El cambio vale en 5 minutos como máximo.
- **Revisar la lista:** menú **English Support → Revisar la lista**: avisa si hay PIN repetidos o grados mal escritos.
- **Si cambias el script:** Implementar → Gestionar implementaciones → editar (lápiz) → Versión: *Nueva versión*. La URL no cambia.

## 5. Notas finales (página del docente)
Para la evaluación de emergencia del III Trimestre: 4 notas por estudiante (temas 5-1, 5-2, 6-1, 6-2),
cada una = promedio de Listening, Reading y Writing (cada destreza = promedio del 1.º y el último intento).

**Instalar (una vez, desde una computadora):**
1. En Apps Script: **+ → Secuencia de comandos**, nómbrala `Notas` y pega el contenido de `Notas.gs`.
2. Reemplaza también `Code.gs` por la versión nueva (tiene la acción `notas` y el menú).
3. **Implementar → Gestionar implementaciones → lápiz → Versión: Nueva versión → Implementar.** La URL no cambia.
4. Recarga la hoja y usa **English Support → Definir clave del docente**. Elige una clave que solo tú sepas.

**Usar (desde cualquier dispositivo):**
- Abre **english-support-six.vercel.app/docente**, escribe la clave y toca **Notas**.
- Se descarga un Excel calculado en ese momento, con una hoja por grado.
- La página no está enlazada en el sitio y sin la clave no devuelve nada.

**En la hoja:** English Support → *Calcular notas finales (pestañas)* crea las pestañas "Notas Grado X".
