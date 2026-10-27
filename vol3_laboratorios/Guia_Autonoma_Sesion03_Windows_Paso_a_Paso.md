# Sesión 3 — De Google Forms a Python: registrar y leer una consulta
## Guía autónoma paso a paso · Windows 10/11 · 120 minutos

**Objetivo:** crear un formulario de consultas ficticias, almacenar sus respuestas en Google Sheets, publicar un servicio de consulta con Apps Script y utilizar Python para **leer**, sin modificarla, una solicitud pendiente.

**Al terminar:** una solicitud de prueba debe aparecer en Sheets con **Estado = PENDIENTE**; la consulta debe poder leerse desde el navegador y desde PowerShell mediante Python. **En esta sesión no se generan respuestas con IA, no se cambia el estado y no se envían correos.** Eso corresponde a la sesión 4.

> **Cómo trabajar:** siga cada paso en orden. Cada etapa indica qué hacer y qué resultado comprobar. No necesita consultar otros manuales para descubrir instrucciones obligatorias. Guarde una bitácora y utilice solamente nombres y consultas ficticias. La interfaz de Google puede variar ligeramente según el idioma y las actualizaciones.
>
> **Seguridad:** este ejercicio utiliza una Web App accesible sin inicio de sesión individual, que podría exponer las consultas a quien conozca su URL. **No use datos personales, institucionales, contraseñas ni preguntas reales de estudiantes.** No comparta la URL de su Web App en repositorios, capturas públicas o mensajes grupales. Si las políticas de su institución impiden el despliegue público, deténgase y consulte al docente o a TI. Este prototipo no es un sistema seguro para uso productivo.

## Antes de empezar: cinco componentes y sus funciones

| Componente | Para qué sirve | Qué hará hoy |
|---|---|---|
| **Google Forms** | Recibe preguntas mediante un formulario web. | Enviar una consulta ficticia. |
| **Google Sheets** | Guarda las respuestas en filas y columnas. | Verificar el estado `PENDIENTE`. |
| **Google Apps Script** | Ejecuta código dentro de los servicios de Google. | Crear el formulario y publicar un servicio que lee la hoja. |
| **Web App** | Ofrece una dirección web a la que otro programa puede consultar. | Devolver una solicitud en formato JSON. |
| **Python** | Permite automatizar la comunicación entre sistemas. | Leer la solicitud desde PowerShell con `--modo lectura`. |

**Distinción esencial:** crearemos **dos proyectos de Apps Script diferentes**. El primero configura Forms y Sheets. El segundo, vinculado a la hoja, publica el servicio Web App. No mezcle sus códigos.

## Etapa 1 — Preparar los archivos y comprobar Python (20 minutos)

**Paso 1.** Abra **Chrome** o **Edge**. Haga clic en la barra superior, escriba `https://github.com/juliopez/ia-local-integracion` y presione **Enter**.

**Paso 2.** En GitHub, localice el botón verde **Code** y seleccione **Download ZIP**. Espere la descarga.

**Paso 3.** Presione **Windows + E** para abrir el Explorador de archivos. Abra **Descargas**, localice el ZIP, haga clic derecho → **Extraer todo... → Extraer**. Entre en la carpeta **`ia-local-integracion-main`** y compruebe que existe **`scripts`**.

**Paso 4.** Dentro de `scripts`, localice estos tres archivos y **no modifique los originales del repositorio** hasta que la guía lo indique:

- `crear_formulario_taller.gs`: crea un formulario, una hoja y un activador.
- `Code.gs`: se publicará como servicio de consulta.
- `puente_local.py`: conecta Python con el servicio publicado.

**Paso 5.** Compruebe Python. Presione la tecla **Windows**, escriba **PowerShell**, haga clic en **Windows PowerShell** (no necesita permisos de administrador) y escriba:

```powershell
py --version
```

Presione **Enter**. Debería aparecer una versión de Python. Si no funciona, pruebe:

```powershell
python --version
```

**Paso 6 (solo si Python no está instalado).** Abra `https://www.python.org/downloads/windows/`, descargue el instalador oficial de Python para Windows compatible con el script (Python 3.10 o posterior), ábralo y siga el asistente. Cuando el instalador ofrezca agregar Python al `PATH`, habilite esa opción si aparece. Termine la instalación, **cierre y vuelva a abrir PowerShell** y repita el paso 5. Si la política del equipo impide instalarlo, solicite apoyo a TI.

**Paso 7.** Compruebe que puede instalar la biblioteca que utiliza el puente. En PowerShell escriba:

```powershell
py -m pip --version
```

Si utiliza `python` en lugar de `py`, también úselo en los comandos siguientes.

**Comprobación A:** tiene la carpeta `scripts` y PowerShell muestra la versión de Python. **No continúe con Python sin haberlo comprobado.**

## Etapa 2 — Crear Forms y Sheets con Apps Script (20 minutos)

**¿Por qué?** Google Forms captura la información y Google Sheets la almacena. Un **activador** ejecuta una función automáticamente cuando llega una respuesta; en este ejemplo escribe `PENDIENTE`.

**Paso 8.** En otra pestaña del navegador escriba `https://script.google.com` y presione **Enter**. Inicie sesión con una cuenta propia de Google si es necesario.

**Paso 9.** Pulse **Nuevo proyecto**. Cuando se abra el editor, haga clic en el nombre del proyecto, escriba **Creación Formulario IA Local** y confirme.

**Paso 10.** Vuelva a la carpeta `scripts` del Explorador. Haga clic derecho en **`crear_formulario_taller.gs`** → **Abrir con → Bloc de notas**. Presione **Ctrl + A** para seleccionar todo y **Ctrl + C** para copiar.

**Paso 11.** Regrese al editor de Apps Script. Abra el archivo de código que aparece por defecto (habitualmente **Código.gs** o **Code.gs**). Haga clic dentro, presione **Ctrl + A** y luego **Ctrl + V**. Esto reemplaza el ejemplo inicial por el código del formulario. Presione **Ctrl + S** para guardar.

**Paso 12.** Sobre el editor localice el desplegable de **funciones**. Seleccione **`crearFormularioTaller`**. Haga clic en **Ejecutar**.

**Paso 13.** Si Google solicita autorización, revise el proyecto, la cuenta utilizada y los permisos que solicita. Apruebe únicamente si corresponden a su cuenta de pruebas y a las funciones del ejercicio. No conceda permisos si no comprende la solicitud; consulte al docente.

**Paso 14.** Abra **Registro de ejecución**. Busque tres direcciones: **Formulario (edición)**, **Formulario (para responder)** y **Hoja de cálculo**. Cópielas en su bitácora **privada**; no las publique. La función está diseñada para reutilizar los identificadores dentro del mismo proyecto si vuelve a ejecutarse, pero un proyecto nuevo puede crear otros archivos.

**Comprobación B:** el registro presenta enlaces al formulario y a la hoja de respuestas. **No intente ejecutar manualmente `registrarSolicitudTaller`**: esa función se activa al enviar el formulario.

## Etapa 3 — Enviar una consulta ficticia y comprobar Sheets (15 minutos)

**Paso 15.** Abra el enlace **Formulario (para responder)** que aparece en el registro anterior.

**Paso 16.** Complete exactamente los campos siguientes:

| Campo de Forms | Valor de ejemplo |
|---|---|
| Nombre | Estudiante de prueba |
| Tipo de consulta | Evaluaciones |
| Consulta | ¿Cuál es el plazo para solicitar la revisión de una evaluación? |
| Correo electrónico | Un correo propio autorizado para el ejercicio |

**Paso 17.** Presione **Enviar**. Vuelva al registro de Apps Script y abra el enlace de **Hoja de cálculo**.

**Paso 18.** En Google Sheets, abra la pestaña **Respuestas de formulario 1**. Busque la nueva fila y confirme que contiene las respuestas enviadas. Es posible que deba actualizar la página.

**Paso 19.** Revise las columnas. La estructura prevista por los scripts es:

| Columna | Encabezado | Contenido de esta etapa |
|---|---|---|
| A | Marca temporal | Fecha/hora de recepción |
| B | Nombre | Estudiante de prueba |
| C | Tipo de consulta | Evaluaciones |
| D | Consulta | Pregunta del ejercicio |
| E | Correo electrónico | Dirección utilizada |
| F | Estado | **PENDIENTE** |
| G | Respuesta IA | Vacía |
| H | Fecha de procesamiento | Vacía |

**Comprobación C:** se ha creado una fila y la columna F muestra **PENDIENTE**. Si no ocurre, vuelva al primer proyecto de Apps Script, abra **Activadores** (icono de reloj) y compruebe que está configurada la función `registrarSolicitudTaller` para **Al enviar formulario** en la hoja. Revise **Ejecuciones** por si aparece un error. No edite los datos a ciegas.

## Etapa 4 — Crear el servicio Web App desde la hoja (25 minutos)

**¿Por qué?** El formulario ya captura la consulta. Ahora necesitamos que Python pueda **consultar** esa información. Para ello publicaremos una segunda aplicación de Apps Script. La respuesta se entrega en **JSON**, un formato de texto que organiza valores como `disponible`, `nombre` y `consulta`.

**Paso 20.** En la **hoja de respuestas** de Google Sheets, haga clic en **Extensiones → Apps Script**. Se abrirá un **nuevo proyecto vinculado a esta hoja**. Es distinto de **Creación Formulario IA Local**.

**Paso 21.** Cambie el nombre de este proyecto a **IA Local - Servicio de Consultas**.

**Paso 22.** Abra el archivo **`scripts/Code.gs`** desde la carpeta descomprimida con el Bloc de notas. Presione **Ctrl + A** y **Ctrl + C**.

**Paso 23.** En el nuevo editor Apps Script, abra su **Código.gs** o **Code.gs**, seleccione todo el código de ejemplo y pegue **Ctrl + V**. Presione **Ctrl + S**.

**Paso 24.** En el código identifique la expresión `getSheetByName("Respuestas de formulario 1")`. Compruebe que coincide exactamente con el nombre de la pestaña de Google Sheets. **Si no coincide**, ajuste el nombre en las llamadas correspondientes del archivo y guarde. No cambie otros nombres de campos.

**Paso 25.** Haga clic en **Implementar → Nueva implementación**. Seleccione el tipo **Aplicación web** (icono de engranaje, si aparece).

**Paso 26.** Complete la configuración: **Descripción:** `Servicio IA Local - Sesión 3`; **Ejecutar como:** `Yo`; **Quién tiene acceso:** `Cualquier usuario` solamente para este ensayo ficticio y si la política de su cuenta lo permite. Este despliegue puede hacer que las consultas sean accesibles sin autenticación individual; no es apropiado para datos reales.

**Paso 27.** Pulse **Implementar** y complete las autorizaciones que correspondan. Copie la **URL de la aplicación web**, que suele terminar en **`/exec`**, en una nota privada. **No confunda esta URL con la del formulario o con la de la hoja.**

**Comprobación D:** tiene una URL `/exec` de la Web App. Si modifica posteriormente `Code.gs`, recuerde que debe ir a **Implementar → Gestionar implementaciones → Editar → Nueva versión → Implementar**; guardar el código no actualiza una versión ya publicada.

## Etapa 5 — Probar la lectura desde el navegador (10 minutos)

**Paso 28.** Abra otra pestaña de Chrome o Edge, pegue **su URL privada `/exec`** en la barra de direcciones y presione **Enter**.

**Paso 29.** Observe el texto que devuelve la página. Debe contener información similar a:

```json
{"disponible":true,"fila":2,"nombre":"Estudiante de prueba","tipo":"Evaluaciones","consulta":"¿Cuál es el plazo para solicitar la revisión de una evaluación?","correo":"correo-de-prueba"}
```

El número de fila puede ser distinto si existen registros previos. Si no existen solicitudes pendientes, aparecerá `"disponible":false`. **No publique capturas que muestren su URL completa o direcciones de correo.**

**Paso 30.** Regrese a Google Sheets. Compruebe que la misma fila sigue con **F = PENDIENTE** y que **G y H están vacías**.

**Comprobación E:** la URL `/exec` muestra la consulta ficticia y **no ha cambiado la hoja**. Eso demuestra una lectura; todavía no estamos enviando respuestas.

## Etapa 6 — Ejecutar la lectura desde PowerShell con Python (20 minutos)

**¿Por qué?** Python actuará como puente: solicitará a Apps Script una consulta pendiente. En esta sesión usamos **solo lectura**, por lo que no contactaremos al modelo para generar una respuesta y no enviaremos Gmail.

**Paso 31.** Vuelva al **Explorador de archivos**. Abra la carpeta **`ia-local-integracion-main`**, aquella que **contiene** la subcarpeta `scripts` (no entre en `scripts` todavía).

**Paso 32.** Haga clic en la **barra de direcciones** del Explorador, escriba **`powershell`** y presione **Enter**. Se abrirá PowerShell en esa carpeta. Confirme que ve una ruta terminada en `ia-local-integracion-main>`.

**Paso 33.** Abra **`scripts/puente_local.py`** en Bloc de notas. En la parte inicial busque la variable `URL_APPS_SCRIPT`. **Este archivo contiene una URL de ejemplo: reemplácela en su copia local por la URL `/exec` que obtuvo en el paso 27.** Mantenga las comillas dobles y no agregue espacios ni cambie otras líneas. Presione **Ctrl + S**. No suba esa copia modificada a un repositorio público.

**Paso 34.** Vuelva a PowerShell y ejecute:

```powershell
py -m pip install requests
```

Presione **Enter** y espere el resultado. La biblioteca `requests` permite a Python realizar consultas web. Si `py` no está disponible, reemplace `py` por `python`.

**Paso 35.** Para comprobar las opciones del script escriba:

```powershell
py scripts/puente_local.py --help
```

Presione **Enter**. Busque la opción `--modo` y los valores `lectura`, `prueba` y `completo`. **No ejecute los otros modos hoy.**

**Paso 36.** Ejecute solamente:

```powershell
py scripts/puente_local.py --modo lectura
```

Presione **Enter**. El programa debe mostrar la consulta ficticia recuperada de Sheets. Si muestra `disponible: false`, revise primero si la fila está realmente en estado `PENDIENTE` y si configuró la URL correcta.

**Paso 37.** Abra nuevamente Sheets y compruebe: **F = PENDIENTE; G y H vacías**. No debe haberse enviado ningún correo electrónico.

**Comprobación F:** Python puede leer la misma solicitud que vio en el navegador, pero la fila no cambia y no se envía Gmail. **Este es el resultado final de la sesión 3.**

## Si aparece un error

| Qué observa | Qué comprobar | Cómo continuar |
|---|---|---|
| `py` no se reconoce | `python --version` | Use `python` en todos los comandos o complete la instalación de Python. |
| `No module named requests` | Python activo | Ejecute `py -m pip install requests` con el mismo intérprete. |
| Forms no muestra enlaces | Primer proyecto, `crearFormularioTaller`, Registro de ejecución | Verifique función seleccionada, autorizaciones y errores. |
| El formulario crea duplicados | Proyectos de Apps Script distintos | Reutilice el proyecto original y sus enlaces. |
| F no muestra `PENDIENTE` | Activadores y Ejecuciones del primer proyecto | Compruebe `registrarSolicitudTaller`, no la ejecute manualmente. |
| No existe la pestaña de Sheets | Nombre de pestaña frente a `getSheetByName` | Haga coincidir los nombres en `Code.gs`. |
| `/exec` muestra error | Despliegue y autorizaciones | Revise acceso y versión publicada; no divulgue la URL. |
| `disponible:false` | Primera fila con estado `PENDIENTE` | Compruebe que existe una consulta pendiente. |
| Python lee otra consulta | Varias filas `PENDIENTE` | El script selecciona la primera pendiente; revise la hoja. |
| Un comando modificó la hoja | Modo ejecutado | Deténgase y confirme que usó únicamente `--modo lectura`. |

**Nota de validación:** la lectura integral fue probada con Ubuntu y datos ficticios. Los pasos de Windows están documentados, pero **la ejecución completa en un equipo Windows independiente aún debe comprobarse**.

## 1. Comprobación final de la sesión

- [ ] Descargué el repositorio y identifiqué los tres archivos.
- [ ] Confirmé que Python funciona y ejecuté comandos en PowerShell.
- [ ] Creé Forms y Sheets mediante el primer proyecto de Apps Script.
- [ ] Envié una consulta ficticia y comprobé **PENDIENTE**.
- [ ] Publiqué la Web App desde un segundo proyecto vinculado a Sheets.
- [ ] Comprobé la respuesta JSON desde el navegador.
- [ ] Ejecuté `py scripts/puente_local.py --modo lectura`.
- [ ] Volví a Sheets: **PENDIENTE**, sin respuesta IA ni fecha de procesamiento.
- [ ] Registré dificultades y resultados sin publicar URLs o correos.

## 2. Material complementario (opcional)

Estos recursos amplían el aprendizaje; no son necesarios para realizar el recorrido principal.

- [Laboratorio 4](Lab04.md): ampliación de la actividad.
- [Manual Técnico — capítulo 7](../vol2_manual_tecnico/cap07_mt.md): Forms y Sheets.
- [Manual Técnico — capítulo 8](../vol2_manual_tecnico/cap08_mt.md): Apps Script y Python.

## 3. Cierre y siguiente sesión

**Sesión 3 completada:** recuperó una consulta ficticia desde Python sin cambiar su estado **PENDIENTE** ni enviar un correo.

**Siguiente sesión:** [guía paso a paso de la sesión 4](Guia_Autonoma_Sesion04_Windows_Paso_a_Paso.md): procesamiento con Ollama, registro en Sheets y comprobación de Gmail. No ejecute el modo completo antes de esa actividad.
