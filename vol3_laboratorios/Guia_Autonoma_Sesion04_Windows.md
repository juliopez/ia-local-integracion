# Sesión 4 · Automatización de respuestas con IA local

**Recorrido de aprendizaje para Windows 10/11** · Esta guía continúa la [sesión 3](Guia_Autonoma_Sesion03_Windows.md), donde se creó el formulario, se vinculó con Sheets y se comprobó que Python lee una solicitud sin modificarla.

> **Orientación:** [Itinerario completo](../EMPEZAR_AQUI.md) · [Laboratorio 4](Lab04.md) · [Manual Técnico, capítulo 8](../vol2_manual_tecnico/cap08_mt.md) (explicaciones e imágenes) · [Manual del Participante](../vol1_manual_participante/) · [Proyecto Integrador](../vol4_proyecto_integrador/) · [Referencia Técnica](../vol5_manual_referencia/).

## Resultado esperado
Una consulta ficticia enviada mediante Google Forms se registra en Google Sheets, Python la obtiene a través de Apps Script, Ollama genera una respuesta y Apps Script la escribe en la hoja y la envía mediante Gmail. **El estado final del código vigente es `ENVIADA`**, no `PROCESADO`.

**Utilice exclusivamente datos de prueba y un correo propio autorizado.** El Web App de este ejercicio admite acceso mediante enlace y no tiene los controles necesarios para gestionar antecedentes reales de estudiantes. No publique su URL.

## Preparación

Compruebe que completó la [sesión 3](Guia_Autonoma_Sesion03_Windows.md): existe una hoja llamada `Respuestas de formulario 1` con columnas A–H, una solicitud en estado `PENDIENTE`, el Web App `/exec` devuelve JSON con `disponible: true`, y Python ejecuta `--modo lectura` sin modificar nada.

Utilice las **versiones vigentes** de [`scripts/Code.gs`](../scripts/Code.gs), [`scripts/puente_local.py`](../scripts/puente_local.py), [`scripts/system_prompt.txt`](../scripts/system_prompt.txt), [`scripts/contexto/normativa_ejemplo.md`](../scripts/contexto/normativa_ejemplo.md) y [`scripts/skills/retroalimentacion-formativa/SKILL.md`](../scripts/skills/retroalimentacion-formativa/SKILL.md). Los tres últimos archivos se leen **localmente** por Python: no se importan automáticamente desde Open WebUI.

Si su hoja tiene otro nombre, cambie las **dos apariciones** de `getSheetByName("Respuestas de formulario 1")` en `Code.gs`, guarde y publique una **nueva versión** de su Web App. No basta con guardar el script si la URL `/exec` apunta a una versión anterior.

## Actividad 1. Configurar Python (10 min)

Desde el Explorador de Windows, abra la carpeta local del repositorio y edite `scripts/puente_local.py` con un editor de texto.

Verifique estas líneas (sustituya únicamente los valores de su propia instalación):

```python
URL_APPS_SCRIPT = "https://script.google.com/macros/s/URL_DE_SU_WEB_APP/exec"
URL_OLLAMA = "http://localhost:11434/api/chat"
MODELO_OLLAMA = "qwen2.5:1.5b"
```

`qwen2.5:1.5b` es el modelo utilizado en el ejemplo; si completó la sesión 1 con otro modelo, use el **identificador exacto** que muestra `ollama list`. **Nunca publique la URL personal del Web App en el repositorio.**

En PowerShell, situado en la raíz del repositorio, ejecute:

```powershell
py scripts/puente_local.py --help
```

Si Windows no reconoce `py`, utilice `python`. Si aparece `No module named requests`, instale la dependencia en ese mismo entorno: `py -m pip install requests`.

**Compruebe:** aparece la ayuda con los modos `lectura`, `prueba` y `completo`.

## Actividad 2. Validar respuesta local, sin enviar mensajes (15 min)

Ejecute:

```powershell
py scripts/puente_local.py --modo prueba
```

Esta acción utiliza una **consulta ficticia local** y pide una respuesta a Ollama. **No lee, modifica ni envía datos a Google Workspace.** Una salida esperada comienza con `Respuesta de prueba (sin cambios en Sheets):` y contiene texto generado por el modelo. Compruebe que el texto alude a los **cinco días hábiles desde la publicación de la nota** definidos en el documento ficticio.

Si Ollama no responde, compruebe que está iniciado, que `ollama list` reconoce el modelo y que el identificador de `MODELO_OLLAMA` coincide. La calidad lingüística puede variar: registre respuestas incorrectas para la actividad de optimización de la sesión 5.

**Compruebe:** la hoja sigue con la solicitud `PENDIENTE`; no hay un correo nuevo generado por esta prueba.

## Actividad 3. Ejecutar un ciclo completo (15 min)

Antes de continuar, **confirme** que la fila de ensayo contiene una dirección de correo propia autorizada y que las columnas G y H están vacías. El procedimiento siguiente **modifica Sheets y envía un correo real**.

Ejecute **una sola vez**:

```powershell
py scripts/puente_local.py --modo completo --una-vez
```

La salida esperada es similar a:

```text
Modo COMPLETO: se procesarán solicitudes y Apps Script enviará correos.
Procesando fila 2...
Fila 2 procesada correctamente.
```

El número de fila puede ser distinto si ya envió otras solicitudes.

**Qué sucede:** Apps Script reserva la solicitud (`PENDIENTE` → `PROCESANDO`), Python genera una respuesta mediante Ollama, Apps Script registra texto y fecha, envía por Gmail y marca la fila como `ENVIADA`.

**No repita el comando automáticamente ante un error**: el envío de correo y la actualización de Sheets **no son una transacción atómica**. Una fila con `PROCESANDO` o `ERROR` requiere revisión del registro y de Gmail antes de cualquier reintento.

## Actividad 4. Verificar el resultado (15 min)

En Google Sheets, hoja `Respuestas de formulario 1`, compruebe:

| Columna | Resultado esperado |
|---|---|
| F · Estado | **ENVIADA** |
| G · Respuesta IA | Texto completo generado por Ollama |
| H · Fecha de procesamiento | Fecha y hora registradas |

Abra Gmail del destinatario de prueba. Busque un mensaje con asunto que comienza por **«Respuesta a tu consulta académica»** y compruebe que su cuerpo contiene la respuesta generada. Puede revisar Spam si no lo encuentra.

**La sesión termina cuando ambas verificaciones son satisfactorias.** Una ejecución sin errores en la terminal no sustituye comprobar Sheets y Gmail.

## Si algo falla

| Síntoma | Comprobación | Siguiente acción |
|---|---|---|
| `--modo prueba` falla | Ollama activo, modelo exacto, puerto 11434 | Corregir configuración local y repetir **solo** el modo prueba |
| `No module named requests` | Python usado para ejecutar el script | Instalar `requests` con ese intérprete |
| No existe solicitud pendiente | Estado en columna F | Enviar un formulario de ensayo nuevo; no modificar una fila `ENVIADA` |
| `--modo completo` muestra error | Filas `PENDIENTE`, `PROCESANDO`, `ERROR` o `ENVIADA`; correo enviado | **No reintentar hasta determinar qué ocurrió** |
| La fila no cambia o cambió a `ERROR` | Registro de Apps Script, versión de Web App, permisos Gmail | Corregir el error según el registro; revisar envío previo |
| Gmail no muestra correo | Destinatario y carpetas, estado de fila, enviados del titular del Apps Script | No repetir el envío hasta aclarar si se entregó |
| Respuesta poco pertinente | Pregunta de entrada, prompt y contexto | Guardar el caso como evidencia para la sesión 5 |

## Evidencias para el portafolio
- Consulta ficticia y estado original `PENDIENTE`.
- Ejecución de `--modo prueba` con respuesta local.
- Salida de `--modo completo --una-vez`.
- Hoja con estado `ENVIADA`, texto y fecha de procesamiento.
- Confirmación de correo recibido (oculte direcciones personales).
- Breve observación crítica sobre exactitud y límites de la respuesta.

## Comprobación de aprendizaje

Marque: ☐ Puedo distinguir lectura, prueba y procesamiento completo. ☐ Compruebo el estado antes de ejecutar. ☐ Reconozco `ENVIADA` como estado final. ☐ Confirmé el correo. ☐ Sé que la calidad de la respuesta debe evaluarse por separado.

**Siguiente etapa:** [mejora y evaluación del asistente](Lab03.md) y [Manual Técnico, capítulos 6 y 10](../vol2_manual_tecnico/).

---

**Alcance de la comprobación del ejemplo:** se ejecutó el flujo completo con Ubuntu, Qwen 2.5 1.5B, Forms, Sheets, Apps Script y Gmail. Se observó una respuesta local, ejecución completa sin error, fila final `ENVIADA` y recepción confirmada del correo. **El procedimiento de PowerShell está documentado, pero no se ha probado integralmente en un equipo Windows independiente.**
