# Sesión 3 · Ruta autónoma Windows: Google Forms → Sheets → Apps Script → Python

> **Navegación autónoma y referencias cruzadas:** [Volver al itinerario de cinco etapas](../EMPEZAR_AQUI.md) · [Volumen 1 — conceptos](../vol1_manual_participante/) · [Volumen 4 — portafolio](../vol4_proyecto_integrador/) · [Volumen 5 — consulta técnica](../vol5_manual_referencia/). Los procedimientos con capturas originales permanecen en el **Manual Técnico (volumen 2)**; la guía autónoma indica el orden, no sustituye las imágenes.


**Objetivo:** capturar una consulta ficticia, guardarla en Sheets y leerla desde Python **sin modificar su estado ni enviar correos**. Esta guía es el recorrido principal para el participante; [Laboratorio 4](Lab04.md), [Manual Técnico cap. 7](../vol2_manual_tecnico/cap07_mt.md) y [cap. 8](../vol2_manual_tecnico/cap08_mt.md) amplían conceptos y procedimientos.

**Sistema de referencia:** Windows 10/11, PowerShell, Python y Ollama instalados en la sesión 1. Ubuntu se utilizó para validar la lectura final del ensayo docente; en Windows las etapas Google son idénticas y el comando se ejecuta con `py` o `python`. La ejecución integral en Windows aún no se ha comprobado en un equipo independiente.

## Antes de comenzar (5 minutos)
- Inicie sesión en su propia cuenta de Google; disponga de permisos para crear Forms, Sheets y proyectos Apps Script.
- Descargue o actualice el repositorio: https://github.com/juliopez/ia-local-integracion → **Code → Download ZIP → Extraer todo**. Use siempre archivos de **la misma versión**. No utilice datos académicos reales.
- Identifique los originales: [`scripts/crear_formulario_taller.gs`](../scripts/crear_formulario_taller.gs), [`scripts/Code.gs`](../scripts/Code.gs), [`scripts/puente_local.py`](../scripts/puente_local.py).
- Prepare una bitácora: fecha, sistema operativo, acciones, resultado, error (si aparece) y evidencia sin credenciales.
- **No pegue la URL de su Web App en documentos públicos o capturas**: las aplicaciones publicadas para acceso abierto exponen las consultas ficticias. No utilice este prototipo para datos sensibles.

## Paso 1. Crear Forms y Sheets automáticamente (15 minutos)
1. Abra https://script.google.com → **Proyecto nuevo**. Asigne el nombre **Creación Formulario IA Local**.
2. Abra [`crear_formulario_taller.gs`](../scripts/crear_formulario_taller.gs) desde GitHub; copie **todo** su contenido, y reemplace el código de ejemplo de este proyecto nuevo. Guarde con Ctrl+S.
3. Seleccione la función `crearFormularioTaller` y pulse **Ejecutar**. Autorice Google Forms, Sheets y Apps Script cuando Google lo solicite. Revise las autorizaciones antes de concederlas.
4. Consulte **Registro de ejecución**: encontrará los enlaces al formulario de edición, al formulario para responder y a la hoja de cálculo. Guarde los enlaces privadamente.
5. **Importante:** esta acción crea un formulario **nuevo**. El formulario en blanco que pudiera tener abierto previamente no se edita. La función guarda identificadores en propiedades del proyecto: ejecutarla otra vez en **el mismo proyecto** devuelve los enlaces, pero copiarla en un proyecto nuevo puede crear duplicados.

**Campos obligatorios (orden crítico):**

| Pregunta | Tipo | Opciones |
|---|---|---|
| Nombre | Respuesta corta | — |
| Tipo de consulta | Lista desplegable | Evaluaciones; Asignaturas; Matrícula; Otro |
| Consulta | Párrafo | — |
| Correo electrónico | Respuesta corta, validación de correo | — |

**Decisión de arquitectura:** el [Manual Técnico cap. 7](../vol2_manual_tecnico/cap07_mt.md) y [`Code.gs`](../scripts/Code.gs) coinciden en esos campos. Una sección narrativa anterior del Lab04 menciona «Prioridad»; **no la use en este caso**, porque desalinearía las columnas del puente.

## Paso 2. Enviar una consulta ficticia y validar Sheets (10 minutos)
1. Desde el registro abra el enlace **Formulario (para responder)**. Complete: **Nombre** = `Estudiante de prueba`, **Tipo de consulta** = `Evaluaciones`, **Consulta** = `¿Cuál es el plazo para solicitar la revisión de una evaluación?` y **Correo electrónico** = una dirección propia autorizada para pruebas.
2. Pulse **Enviar** y abra el enlace de la hoja de cálculo.
3. En la pestaña **Respuestas de formulario 1** deberá observar una fila nueva con las cinco columnas originales y el estado automático.

| Columna | Encabezado | Primera fila de prueba |
|---|---|---|
| A | Marca temporal | Fecha/hora del envío |
| B | Nombre | Estudiante de prueba |
| C | Tipo de consulta | Evaluaciones |
| D | Consulta | Texto enviado |
| E | Correo electrónico | Correo de prueba |
| F | Estado | **PENDIENTE** |
| G | Respuesta IA | **Vacía** |
| H | Fecha de procesamiento | **Vacía** |

**Si F no muestra PENDIENTE:** compruebe que ejecutó `crearFormularioTaller` y autorizó su creación del activador para envío del formulario. En Apps Script → Activadores debe existir `registrarSolicitudTaller`, vinculado al spreadsheet. Revise Ejecuciones para identificar un posible error; no cambie celdas ni borre respuestas indiscriminadamente.

**Checkpoint 1:** Forms recibe una respuesta y Sheets registra `PENDIENTE`.

## Paso 3. Implementar el Web App en la hoja de respuestas (20 minutos)
1. Abra la hoja vinculada y seleccione **Extensiones → Apps Script**. Este proyecto es **distinto** del proyecto de creación del formulario.
2. Nómbrelo **IA Local - Servicio de Consultas** y reemplace el código de ejemplo por el contenido íntegro de [`scripts/Code.gs`](../scripts/Code.gs). Guarde con Ctrl+S.
3. Compruebe que ambas funciones `leerSolicitud` y `doPost` seleccionan explícitamente la pestaña `Respuestas de formulario 1` mediante `getSheetByName("Respuestas de formulario 1")`. El archivo de GitHub ya incorpora esta corrección; **si su pestaña tiene otro nombre, ajuste el nombre en ambos lugares**.
4. Pulse **Implementar → Nueva implementación → Aplicación web**; descripción: `Servicio IA Local - Sesión 3`; **Ejecutar como: Yo**; **Quién tiene acceso: Cualquier usuario** para la prueba del puente local. Esta opción publica un endpoint **sin autenticación por usuario**: empléelo únicamente con **consultas ficticias** y sin datos privados. El Web App de este material es un prototipo didáctico, **no un servicio institucional seguro**. Si las políticas de su organización impiden esa publicación, deténgase y consulte a TI.
5. Pulse **Implementar**, autorice si corresponde, y copie la URL que termina en `/exec` a un lugar **privado**.

**Checkpoint 2:** el Web App tiene una URL `/exec` válida. Nunca publique esta URL en repositorios.

## Paso 4. Probar que Apps Script solo lee (5 minutos)
1. Abra la URL `/exec` **en su propio navegador**.
2. Debe obtener una respuesta JSON con `"disponible":true`, `"fila":2` (si es la primera respuesta), `"nombre":"Estudiante de prueba"`, `"tipo":"Evaluaciones"` y la consulta ficticia.
3. Vuelva a Sheets: **F = PENDIENTE**, **G y H vacías**.

Si el JSON indica `disponible:false`, compruebe que la columna F dice `PENDIENTE` y que `Code.gs` usa la pestaña correcta. Si modifica `Code.gs` **después** de publicar, actualice la implementación: **Implementar → Gestionar implementaciones → Editar → Nueva versión → Implementar**. Guardar código no reemplaza automáticamente una versión publicada.

**Checkpoint 3:** respuesta JSON correcta y hoja inalterada.

## Paso 5. Configurar y ejecutar el puente en Windows (20 minutos)
1. Abra `scripts/puente_local.py` extraído del ZIP. En la configuración inicial, cambie **solamente** `URL_APPS_SCRIPT` por su URL privada `/exec`; conserve las comillas. **No copie su URL a GitHub**. En el ensayo docente, la URL se editó en un clon local.
2. Abra **PowerShell** en la carpeta raíz del repositorio extraído (puede usar «Abrir en Terminal» desde el Explorador de archivos).
3. Compruebe la ayuda:

```powershell
py scripts/puente_local.py --help
```

Si `py` no funciona, utilice `python`. Si aparece `ModuleNotFoundError: requests`, instale **solo esa dependencia** en su entorno Python activo: `py -m pip install requests` (o `python -m pip install requests`). No ejecute `pip` con privilegios administrativos sin motivo.
4. Ejecute **solo lectura**:

```powershell
py scripts/puente_local.py --modo lectura
```

Si recibe `disponible: true` y los datos ficticios, **no** ejecute `--modo completo` durante esta sesión.
5. Regrese a Sheets: compruebe **F = PENDIENTE**, **G y H vacías**.

**Checkpoint 4 (salida de sesión 3):** Python muestra la misma consulta que Forms; ninguna celda de estado o respuesta cambia y **no se envía ningún correo**.

## Resolución de problemas sin docente
| Problema | Qué revisar | Acción prudente |
|---|---|---|
| «Ya existe una instalación» | Registro de ejecución contiene las URLs | Utilice los enlaces anteriores; no cree otro proyecto |
| No aparece «PENDIENTE» | Activador `registrarSolicitudTaller`, hoja y registro de errores | Reautorice el proyecto si el registro evidencia falta de permisos |
| `disponible:false` o hoja vacía | Pestaña, estado F, código publicado | Corrija la fuente; cree **nueva versión** de implementación si cambió código |
| Error al abrir `/exec` | Permisos y configuración del Web App | Revise implementación y autorizaciones; no pegue URL públicamente |
| `py` no reconocido | Instalación y PATH de Python | Pruebe `python --version`; recurra al Manual Técnico cap. 4 |
| `requests` no instalado | Error en PowerShell | Instale dependencia en el mismo intérprete que ejecuta el puente |
| Lectura muestra otra solicitud | Filas anteriores en estado `PENDIENTE` | El puente toma la primera pendiente; use una hoja de ensayo limpia o examine sus filas |
| El puente modifica una fila | Se ejecutó otro modo o código obsoleto | Detenga la ejecución; confirme comando `--modo lectura` y versión de los archivos |

## Evidencia mínima en la bitácora
- Identificador o título del formulario, fecha de ejecución, cuatro preguntas.
- Nombre de la hoja vinculada y **una fila ficticia con estado PENDIENTE**.
- Confirmación de JSON desde `doGet`, sin mostrar la URL secreta.
- Salida de `--modo lectura` y comprobación final F/G/H.
- Si algo falla: error literal, momento, corrección y nueva comprobación.

## Validación docente (25 de octubre de 2026)
Se creó un formulario desde `crear_formulario_taller.gs`; Google registró los enlaces de Forms y Sheets. Se envió la consulta ficticia; Sheets registró la fila y el activador colocó `PENDIENTE`. Se configuró `Code.gs` en un proyecto vinculado a Sheets, se implementó Web App, el navegador mostró JSON de solicitud disponible, y la consulta desde Ubuntu mediante `python3 scripts/puente_local.py --modo lectura` recuperó la misma solicitud. **Después de ambas lecturas, la columna F seguía PENDIENTE, G y H vacías.** La ruta **PowerShell en Windows** está documentada, pero **no ha sido ejecutada de extremo a extremo en Windows**.

**Continuación:** [Laboratorio 4, sesión 4](Lab04.md) para `--modo prueba` y `--modo completo --una-vez`. No se han probado aún esos modos como parte de este ensayo.