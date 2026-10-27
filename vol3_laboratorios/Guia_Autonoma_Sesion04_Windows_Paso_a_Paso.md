# Sesión 4 — Automatizar una respuesta con Ollama, Sheets y Gmail
## Guía autónoma paso a paso · Windows 10/11 · 120 minutos

**Objetivo:** continuar el flujo de la [sesión 3](Guia_Autonoma_Sesion03_Windows_Paso_a_Paso.md), comprobar una respuesta local de Ollama y procesar **una sola consulta ficticia** de Google Forms hasta registrar su respuesta en Sheets y recibir un correo de Gmail.

**Requisitos:** haber completado la sesión 3: Google Forms y Sheets operativos, Web App publicada, `scripts/puente_local.py` disponible y `--modo lectura` funcionando. Además, Ollama y el modelo de la sesión 1 deben estar instalados.

> **Cómo utilizar esta guía:** siga los pasos uno a uno. No debe consultar otros documentos para ejecutar las acciones básicas. Utilice exclusivamente nombres, preguntas y un destinatario de prueba autorizado. **El modo completo modifica Google Sheets y envía un correo real.** No lo ejecute hasta confirmar la dirección de destino.
>
> **Seguridad:** el Web App de este taller es un prototipo didáctico sin autenticación individual para leer solicitudes. No introduzca datos reales, contraseñas ni información institucional y **no publique su URL `/exec`**. Si la política de su organización impide este uso, solicite apoyo antes de continuar.

## Antes de comenzar: ¿qué hace cada herramienta?

| Componente | Función en el ejercicio |
|---|---|
| **Google Forms** | Recibe la consulta ficticia del participante. |
| **Google Sheets** | Guarda la solicitud y su estado: `PENDIENTE`, `PROCESANDO`, `ENVIADA` o `ERROR`. |
| **Apps Script / Web App** | Permite reservar la solicitud, registrar la respuesta y enviar el correo con Gmail. |
| **Python (`puente_local.py`)** | Coordina la consulta al servicio y la generación de texto con Ollama. |
| **Ollama** | Ejecuta el modelo local que genera la respuesta. |
| **System Prompt / contexto / Skill local** | Aportan instrucciones y documentos que el puente lee desde la carpeta `scripts`. No se sincronizan automáticamente con Open WebUI. |

**Tres modos, tres resultados:** `--modo lectura` consulta la solicitud sin cambiarla; `--modo prueba` consulta **solo Ollama** con una pregunta ficticia local, sin acceder a Google; `--modo completo --una-vez` procesa **una** solicitud pendiente y puede enviar Gmail.

## Etapa 1 — Recuperar el trabajo de la sesión 3 (15 minutos)

**Paso 1.** Abra **Chrome** o **Edge**. En la barra de direcciones escriba `https://sheets.google.com` y presione **Enter**. Inicie sesión con la **misma cuenta de Google** que utilizó en la sesión 3.

**Paso 2.** Abra la hoja **IA Local — Respuestas del Asistente Académico** creada durante la sesión anterior. Si no la encuentra, abra Google Drive, busque ese nombre y seleccione la hoja.

**Paso 3.** En la parte inferior seleccione la pestaña **Respuestas de formulario 1**. Compruebe las columnas: **F Estado**, **G Respuesta IA** y **H Fecha de procesamiento**.

**Paso 4.** Busque la fila ficticia de la sesión 3 y compruebe que tiene **F = PENDIENTE** y que **G y H están vacías**. Verifique también que la columna **E** contiene **un correo propio autorizado** al que pueda acceder. **No procese filas de otras personas.** Si no existe una solicitud adecuada, abra el formulario de ensayo de la sesión 3 y envíe una nueva con su dirección autorizada.

**Paso 5.** En el Explorador de archivos de Windows (**Windows + E**), abra la carpeta descomprimida del repositorio `ia-local-integracion-main`. Verifique que dentro está la carpeta `scripts`.

**Comprobación A:** tiene una solicitud ficticia pendiente con un correo autorizado y localizó los archivos del puente. Si hay varias solicitudes pendientes, recuerde que el programa selecciona **la primera**: revise y aclare esos registros antes de continuar.

## Etapa 2 — Revisar la configuración local (20 minutos)

**¿Por qué?** El programa Python necesita conocer la URL de su Web App y el nombre exacto del modelo de Ollama que ejecutará. La URL de ejemplo del archivo descargado **no debe utilizarse como si fuera su implementación personal**.

**Paso 6.** Presione la tecla **Windows**, escriba **PowerShell** y seleccione **Windows PowerShell**.

**Paso 7.** En PowerShell escriba el siguiente comando y presione **Enter**:

```powershell
ollama list
```

Localice el modelo descargado en la sesión 1. Si usa el modelo del ejemplo, aparecerá `qwen2.5:1.5b`. Anote exactamente su nombre.

**Paso 8.** Abra la carpeta `scripts` en el Explorador. Localice `puente_local.py`, haga clic derecho → **Abrir con → Bloc de notas** (o VS Code, si lo tiene instalado).

**Paso 9.** Al comienzo de `puente_local.py`, identifique estas tres variables y compruébelas:

```python
URL_APPS_SCRIPT = "https://script.google.com/macros/s/URL_PERSONAL/exec"
URL_OLLAMA = "http://localhost:11434/api/chat"
MODELO_OLLAMA = "qwen2.5:1.5b"
```

**No copie literalmente `URL_PERSONAL`:** reemplace la URL completa por **su propia dirección `/exec`** de la sesión 3. Si utiliza otro modelo, escriba su nombre exacto en `MODELO_OLLAMA`. Mantenga `URL_OLLAMA` salvo que su instalación utilice expresamente otra dirección.

**Paso 10.** Presione **Ctrl + S** para guardar la copia local. **No suba ese archivo modificado a GitHub**: contiene la URL privada de su servicio.

**Paso 11.** Abra, sin modificarlos, los tres archivos que Python utilizará: `scripts/system_prompt.txt`, `scripts/contexto/normativa_ejemplo.md` y `scripts/skills/retroalimentacion-formativa/SKILL.md`. Compruebe que existen en las rutas indicadas. El puente leerá estos archivos locales directamente, sin consultar Knowledge ni Skills de Open WebUI.

**Comprobación B:** identificó el modelo, configuró **su** URL de Apps Script y encontró los tres archivos de apoyo. No comparta capturas que muestren la URL personal.

## Etapa 3 — Abrir PowerShell en la carpeta y probar Ollama (20 minutos)

**Paso 12.** En el Explorador de archivos, abra la carpeta principal `ia-local-integracion-main` (la carpeta **que contiene** `scripts`). Haga clic en la **barra de direcciones** del Explorador, escriba `powershell` y presione **Enter**. Se abrirá PowerShell en la ubicación correcta.

**Paso 13.** Compruebe Python. Escriba y presione **Enter**:

```powershell
py --version
```

Si Windows no reconoce `py`, pruebe `python --version` y utilice `python` en los siguientes comandos.

**Paso 14.** Compruebe las opciones del programa:

```powershell
py scripts/puente_local.py --help
```

Presione **Enter**. En la ayuda debe aparecer `--modo` con los valores `lectura`, `prueba` y `completo`. Si aparece `No module named requests`, escriba `py -m pip install requests` y repita el comando. Cuando use `python`, sustitúyalo también en esos comandos.

**Paso 15.** Ejecute una prueba **solo local**:

```powershell
py scripts/puente_local.py --modo prueba
```

Presione **Enter** y espere la respuesta del modelo Ollama. Puede tardar dependiendo del computador.

**Paso 16.** Busque el texto `Respuesta de prueba (sin cambios en Sheets):` seguido por una respuesta generada. Compare su contenido con `normativa_ejemplo.md`: el documento ficticio establece **cinco días hábiles desde la publicación de la nota** para solicitar revisión de una evaluación. Si el modelo responde de otra manera, guarde esa evidencia; no significa que deba alterar el texto original.

**Paso 17.** Regrese a Sheets. Verifique que la solicitud sigue con **F = PENDIENTE**, y que **G y H permanecen vacías**. El modo prueba **no consulta Google Workspace ni envía mensajes**.

**Comprobación C:** Ollama respondió localmente y la hoja no cambió. Si falla, compruebe que Ollama está abierto y que el nombre en `MODELO_OLLAMA` coincide con `ollama list`. **No avance al modo completo** si la prueba local no funciona.

## Etapa 4 — Preparar un único envío autorizado (15 minutos)

**Paso 18.** En Sheets identifique la **primera fila** con estado `PENDIENTE`, porque esa es la que seleccionará el puente. Compruebe que corresponde a su caso ficticio, con correo destinatario autorizado en la columna E. Si hay otras solicitudes pendientes antes, deténgase y solicite apoyo: no ejecute el envío sobre una fila ajena.

**Paso 19.** Abra su correo de prueba en Gmail en otra pestaña: escriba `https://mail.google.com` y presione **Enter**. Compruebe que tiene acceso a la bandeja del destinatario. Si el destinatario utiliza otra cuenta, abra la bandeja de ese destinatario en un navegador o sesión autorizada.

**Paso 20.** Confirme otra vez que **F = PENDIENTE**, **G está vacía** y **H está vacía**. Solo entonces continúe. Este es el último punto para detenerse antes de realizar cambios y enviar un correo.

**Comprobación D:** la fila y el destinatario son correctos, y está preparado para verificar el correo.

## Etapa 5 — Ejecutar una vez el flujo completo (20 minutos)

**¿Qué ocurrirá?** Python solicita una fila a Apps Script; la fila pasa de `PENDIENTE` a `PROCESANDO`; Ollama genera una respuesta; Apps Script la escribe en Sheets, añade una fecha, envía el mensaje mediante Gmail y finalmente marca **`ENVIADA`**.

**Paso 21.** Regrese a la ventana PowerShell abierta en la carpeta del repositorio.

**Paso 22.** Escriba este comando **exactamente** y presione **Enter**:

```powershell
py scripts/puente_local.py --modo completo --una-vez
```

Si su computador requiere `python` en lugar de `py`, utilice `python scripts/puente_local.py --modo completo --una-vez`.

**Paso 23.** Espere a que termine. Debe aparecer información semejante a:

```text
Modo COMPLETO: se procesarán solicitudes y Apps Script enviará correos.
Procesando fila 2...
Fila 2 procesada correctamente.
```

El número de fila puede variar. **No ejecute nuevamente el comando** para intentar resolver lentitud o errores: podría haber un correo enviado, aunque la actualización final de Sheets hubiera fallado.

**Comprobación E:** la ejecución finalizó o generó un error registrado. Si aparece un error, **deténgase**, consulte Sheets, los registros de Apps Script y Gmail antes de decidir cualquier reintento.

## Etapa 6 — Comprobar el resultado y guardar evidencias (30 minutos)

**Paso 24.** Regrese a Google Sheets y actualice la página si hace falta. Busque **la fila procesada** que mostró PowerShell.

**Paso 25.** Compruebe las tres columnas:

| Columna | Resultado esperado |
|---|---|
| **F · Estado** | **ENVIADA** |
| **G · Respuesta IA** | Texto generado por Ollama |
| **H · Fecha de procesamiento** | Fecha y hora registradas |

**Paso 26.** Abra Gmail del **destinatario de prueba**. Busque un mensaje cuyo asunto comienza por **«Respuesta a tu consulta académica»**. Revise también **Spam** si no lo encuentra.

**Paso 27.** Abra el correo y compruebe que contiene la respuesta generada. Compare brevemente el texto con `normativa_ejemplo.md`. El hecho de que el mensaje se haya enviado **no garantiza** que su contenido sea correcto.

**Paso 28.** Guarde capturas de la ejecución en PowerShell, la fila de Sheets y la recepción del correo. Use **Windows + Shift + S** para seleccionar la parte visible, y oculte o recorte direcciones personales y URLs privadas antes de compartirlas.

**Paso 29.** Abra la bitácora utilizada en la sesión 2, o cree un archivo nuevo en Bloc de notas. Registre: fecha, modelo, número de fila, estado final, correo recibido (sí/no), pertinencia de la respuesta y cualquier error. No incorpore credenciales ni direcciones privadas.

**Paso 30.** Verifique las evidencias del cierre. Si Sheets sigue en `PROCESANDO` o `ERROR`, **no reintente automáticamente**. Apps Script registra y envía mediante acciones separadas, de modo que es necesario comprobar primero lo que realmente ocurrió.

**Comprobación final:** la fila está marcada **ENVIADA**, Sheets conserva respuesta y fecha, Gmail muestra el mensaje y dispone de evidencias.

## Qué hacer si aparece un problema

| Problema | Acción inicial segura |
|---|---|
| `py` no funciona | Use `python` si muestra la versión correcta. |
| Falta `requests` | Ejecute `py -m pip install requests` con el mismo intérprete. |
| El modelo no responde | Compruebe que Ollama funciona y que `MODELO_OLLAMA` coincide con `ollama list`. |
| Se lee otra fila | El puente elige la **primera** solicitud `PENDIENTE`. Verifique su hoja antes de ejecutar el modo completo. |
| No hay solicitudes pendientes | Envíe una nueva consulta ficticia desde el formulario. |
| Sheets muestra `PROCESANDO` o `ERROR` | Deténgase. Revise Apps Script y Gmail antes de cualquier reintento. |
| No llega el correo | Revise la cuenta correcta, Spam y enviados de la cuenta ejecutora del Apps Script. No reprocese hasta aclarar el estado. |
| Respuesta inventada o incorrecta | Conserve la evidencia para la sesión 5, sin afirmar que el modelo está validado. |

**Nota de validación:** el flujo completo se comprobó previamente en **Ubuntu** con datos ficticios. Los procedimientos Windows están documentados, pero todavía no se han validado de extremo a extremo en un computador Windows independiente.

## 1. Comprobación final de la sesión

- [ ] Encontré una solicitud **ficticia** y el destinatario es una cuenta propia autorizada.
- [ ] Revisé la URL local de Apps Script y el nombre del modelo Ollama.
- [ ] Confirmé que existen System Prompt, normativa y Skill locales.
- [ ] Ejecuté `--modo prueba` y Ollama respondió sin modificar Sheets.
- [ ] Confirmé el estado **PENDIENTE** antes del procesamiento.
- [ ] Ejecuté `--modo completo --una-vez` **una sola vez**.
- [ ] Sheets registra **ENVIADA**, respuesta y fecha.
- [ ] El destinatario recibió el mensaje en Gmail.
- [ ] Registré aciertos, errores y limitaciones sin divulgar datos privados.

## 2. Material complementario (opcional)

Las lecturas complementan la práctica; no son necesarias para completar sus pasos.

- [Laboratorio 4](Lab04.md): fundamentos y arquitectura.
- [Manual Técnico — Capítulo 8](../vol2_manual_tecnico/cap08_mt.md): integración y procedimientos ampliados.
- [Guía original de la sesión 4](Guia_Autonoma_Sesion04_Windows.md): referencia técnica y validaciones.

## 3. Cierre y siguiente sesión

**Sesión 4 completada:** la respuesta quedó registrada con fecha y estado **ENVIADA**, y el destinatario recibió el correo de prueba. Si alguna comprobación falla, conserve la evidencia y no repita automáticamente el envío.

**Siguiente sesión:** [guía paso a paso de la sesión 5](Guia_Autonoma_Sesion05_Windows_Paso_a_Paso.md): evaluar respuestas y justificar mejoras.
