# Puente local: documentos de contexto y skills

## Ejecución por modos — versión de taller

El puente dispone de tres modos, seleccionados mediante argumentos en la terminal:

```bash
python scripts/puente_local.py --modo lectura
python scripts/puente_local.py --modo prueba
python scripts/puente_local.py --modo completo --una-vez
```

- **Lectura (sesión 3):** GET a Apps Script, muestra una consulta pendiente y **no cambia estados ni envía mensajes**.
- **Prueba (preparación sesión 4):** consulta local ficticia a Ollama, cargando `system_prompt.txt`, `contexto/` y `SKILL.md`; no accede a Apps Script.
- **Completo (sesión 4):** reserva por POST (`accion=reclamar`), genera con Ollama y devuelve mediante POST (`accion=completar`). Apps Script registra en Sheets y envía Gmail. Sin `--una-vez` el puente consulta periódicamente.

**Requisito obligatorio:** actualizar y volver a desplegar el Web App desde el código vigente de [Code.gs](../../scripts/Code.gs) (ajuste la ruta del enlace según el documento). Una implementación antigua sigue cambiando el estado al ejecutar GET y no es compatible con `accion=reclamar`. No ejecute modo completo contra una instalación antigua.

**Límites conocidos:** la reserva y el envío de Gmail no son transacciones atómicas. Una falla podría dejar filas `PROCESANDO` o `ERROR`, y el envío podría haberse realizado aun cuando no se confirme la operación. No reintente manualmente sin revisar el estado y la bandeja de envíos. El modelo es un prototipo docente, no una solución de producción.

---

## Objetivo
Extender el puente original de Google Apps Script → Ollama sin sustituir sus interfaces de entrada y salida. Las respuestas se siguen registrando mediante `Code.gs`, que también gestiona el envío de correo electrónico.

## Archivos
- `system_prompt.txt`: instrucciones permanentes generales (obligatorio).
- `contexto/*.md` o `contexto/*.txt`: fuentes breves de referencia (opcional).
- `skills/retroalimentacion-formativa/SKILL.md`: procedimiento de respuesta (opcional).
- `puente_local.py`: lee estos archivos junto al código y los envía a la API `/api/chat` de Ollama.

**Importante:** son archivos locales. Las bases **Knowledge**, las **Notes** y las **Skills** guardadas únicamente en Open WebUI **no se sincronizan automáticamente** con este puente. Si modifica una skill en Open WebUI, exporte o copie de forma controlada su contenido al archivo local del taller. Si carga documentos en Knowledge, copie solo los documentos autorizados a `contexto/`. Esta modalidad utiliza contexto completo con límites de caracteres: **no implementa recuperación vectorial (RAG)**.

## Inicio rápido
1. Mantenga en `scripts/` el código, el prompt y las carpetas de ejemplo.
2. Instale `requests` en su entorno Python: `python -m pip install requests`.
3. En `puente_local.py`, ajuste `MODELO_OLLAMA` al nombre de un modelo instalado y `URL_APPS_SCRIPT` a su propio despliegue autorizado.
4. Pruebe Ollama y Apps Script por separado; utilice únicamente consultas ficticias.
5. Ejecute `python scripts/puente_local.py` desde la raíz del repositorio.
6. Envíe una solicitud ficticia mediante Forms y revise su resultado en Sheets y el correo de prueba.

## Evidencias mínimas
- Pregunta cubierta por `normativa_ejemplo.md`: respuesta sustentada.
- Pregunta por información ausente: reconocimiento de falta de datos.
- Repetición con la skill activada y desactivada: comparación de formato y precisión.
- Registro final en Sheets y envío mediante Gmail.

## Advertencias operativas
- Los archivos se cargan del disco en cada consulta, mientras que el System Prompt original se lee al iniciar el proceso: reinicie el puente para aplicar cambios en `system_prompt.txt`.
- No cargue archivos reservados, información personal, contraseñas ni tokens.
- El texto de los documentos es información no confiable y no debe prevalecer sobre las instrucciones del sistema; esto requiere además validación humana.
- Los límites por archivo y totales son deliberados para un laboratorio. No garantizan encaje en todas las ventanas de contexto; reduzca contenido o seleccione un modelo adecuado.
- La arquitectura actual marca una fila como `PROCESANDO` al leerla. Una interrupción o error puede dejar filas sin reintento automático; antes del uso real añada recuperación de estados, autenticación, control de duplicados y autorización de destinatarios.
- **No usar en producción sin asegurar el Web App**, sus permisos de acceso y los envíos de Gmail. 
