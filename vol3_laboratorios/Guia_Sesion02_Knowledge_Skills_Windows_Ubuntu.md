# Sesión 2 · Guía de validación: Knowledge, Notes y Skills

**Fecha de ensayo:** 25 de octubre de 2026. **Plataforma principal del taller:** **Windows 10/11**; los pasos de interfaz son comunes a Windows y Ubuntu. **Ubuntu** aparece únicamente como anexo diagnóstico del equipo del docente. Este material complementa el [Laboratorio 2](Lab02.md), el [Manual Técnico · Capítulo 5](../vol2_manual_tecnico/cap05_mt.md) y la [guía de archivos locales](../scripts/GUIA_CONTEXTO_SKILLS.md).

## A. Ruta principal del participante — Windows (40 minutos)

Los estudiantes con Windows **no deben ejecutar comandos `sudo`, `systemctl` ni instalar controladores NVIDIA siguiendo el ensayo de Ubuntu**. Si Ollama y Open WebUI ya funcionan tras Lab01, continúe directamente con la interfaz web.

1. **Diseño (10 min).** Identifique propósito, rol, usuarios, límites y casos de uso (actividades 1–5 de Lab02).
2. **Asistente (10 min).** En **Espacio de trabajo → Modelos → Crear**, seleccione el modelo base disponible, configure el asistente **Asistente Académico de Apoyo** y **copie sin reformular** el contenido de [`scripts/system_prompt.txt`](../scripts/system_prompt.txt). **Guarde el modelo antes de configurar Knowledge** para evitar perder un formulario no guardado.
3. **Conocimiento y bitácora (10 min).** Asocie [`scripts/contexto/normativa_ejemplo.md`](../scripts/contexto/normativa_ejemplo.md) mediante **Conocimiento / Subir Archivos**. En **Notas** registre decisiones, errores y resultados, o mantenga una bitácora Markdown local (ambas alternativas son válidas según el Manual Técnico). La nota de Open WebUI no es una fuente documental automática.
4. **Skill y prueba (10 min).** En **Espacio de trabajo → Habilidades → Crear → Importar desde Enlace**, use el RAW de [`SKILL.md`](../scripts/skills/retroalimentacion-formativa/SKILL.md):

   `https://raw.githubusercontent.com/juliopez/ia-local-integracion/main/scripts/skills/retroalimentacion-formativa/SKILL.md`

   Confirme **Importar selección** y luego **asóciela al modelo** en su apartado Habilidades; pulse **Guardar y Actualizar**. Importar una skill no equivale a asociarla, ni asociarla prueba automáticamente que se haya ejecutado.

**Producto verificable:** carpeta local `scripts/` con `system_prompt.txt`, `contexto/normativa_ejemplo.md`, `skills/retroalimentacion-formativa/SKILL.md` y bitácora. En Windows: **GitHub → Code → Download ZIP**, extraer y conservar la carpeta; `git clone` es opcional. Open WebUI **no sincroniza automáticamente** Knowledge, Notes ni Skills con `puente_local.py`. No usar datos reales de estudiantes.

## B. Validación funcional del conocimiento

Pregunte al **asistente personalizado**, en una conversación nueva:

> Según la normativa de ejemplo disponible, ¿cuántos días hábiles existen para solicitar revisión de una evaluación y a qué unidad se dirige la solicitud?

**Resultado esperado:** **cinco días hábiles desde la publicación de la nota**, dirigido a **coordinación académica**. Expanda el indicador de fuentes si aparece y compruebe `normativa_ejemplo.md`. Un nombre de archivo visible confirma asociación; una fuente vinculada a una respuesta exacta proporciona mejor evidencia de recuperación.

**Prueba de límites:**

> ¿Qué documentos adicionales debo presentar obligatoriamente para pedir revisión?

**Resultado esperado:** la normativa ficticia **no especifica** documentos adicionales. **Respuesta fallida:** afirmar que aranceles, becas, fechas de matrícula o listas de solicitudes son anexos obligatorios. La presencia de citas no convierte en verdaderas afirmaciones inventadas.

**Registro:** anote pregunta, respuesta, fuente observada, acierto/error y cambio de configuración. La comparación sistemática con y sin Skill se aborda en **sesión 5**, no en la evaluación de instalación.

## C. Incidencias y soluciones condicionales (Windows y Ubuntu)

| Síntoma | Interpretación prudente | Acción |
|---|---|---|
| El modelo conversa, pero Knowledge devuelve `503: Configure PGVECTOR_DB_URL for remote vector storage` | La configuración actual de almacenamiento vectorial no está operativa; en el ensayo ocurrió con `main-slim` | Comprobar edición de Open WebUI y configuración de almacenamiento; para el taller se validó la imagen estándar `ghcr.io/open-webui/open-webui:main` con Chroma. **No reinstalar Ollama.** |
| El documento aparece asociado, pero responde con información inventada o genérica | Asociación no implica recuperación correcta; también influye la capacidad del modelo | Comprobar contenido visible, indexación y evidencia de fuentes; realizar prueba en chat nuevo |
| En este entorno, los modos predeterminados no produjeron respuestas documentadas | Incidencia observada, no regla universal | En el **modelo**, bajo Parámetros Avanzados → Modo de Llamada a Funciones, se seleccionó **Heredado (Legacy)**; guardar y verificar con las preguntas de la sección B. **Aplicar solo si se reproduce el fallo** |
| El texto del documento aparece en Knowledge, pero no hay respaldo en el equipo | Knowledge es una configuración de Open WebUI | Guardar los archivos en `scripts/`; importar una copia a la interfaz no reemplaza los archivos locales |
| La Skill figura como importada, pero las respuestas inventan reglas | Importación y asociación no garantizan uso eficaz | Conservar evidencia y analizar en sesión 5; no afirmar que una Skill se ejecutó solo porque aparece en el modelo |

**Advertencia técnica para Windows:** si el participante necesita instalar Open WebUI con Docker Desktop, siga **el Manual Técnico, capítulo 4**, y la guía oficial de Open WebUI para su versión. Antes de **recrear** un contenedor, identificar el volumen de datos, crear respaldo independiente y conservar credenciales/configuración. No copiar indiscriminadamente el bloque de comandos de Ubuntu. La etiqueta `:main` puede cambiar de contenido con el tiempo; para despliegues repetibles conviene registrar la versión/digest probados.

## D. Anexo: evidencias del ensayo docente en Ubuntu

**Equipo:** Ubuntu 26.04.1, Ollama, Docker y Qwen `qwen2.5:1.5b`. El entorno de Open WebUI se instaló inicialmente con `main-slim`; chat operativo, pero Knowledge devolvió error de PGVector. Se descargó y ejecutó la imagen estándar `main` con `VECTOR_DB=chroma` reutilizando el volumen existente. **Durante el ensayo se sustituyó el contenedor sin un respaldo independiente de volumen; para la guía del alumnado se recomienda hacerlo correctamente antes de cambios estructurales.**

**Logs comprobados:** `healthy`; embeddings `sentence-transformers/all-MiniLM-L6-v2`; líneas `embeddings generated 1 for 1 items` y `added 1 items to collection`. **No hubo evidencia de problema de indexación** después del cambio de imagen. La primera serie de consultas devolvió plazos inventados, destinatarios incorrectos o negativa infundada de acceso. Se seleccionó **Heredado** en Modo de Llamada a Funciones y una consulta posterior respondió correctamente con **«1 Fuente» → `normativa_ejemplo.md`**. Es una asociación temporal observada, no demostración causal exhaustiva.

Luego se importó la skill original por URL RAW; Open WebUI indicó **Habilidad importada correctamente**, se asoció y se guardó el modelo. Una consulta posterior recuperó plazo y destinatario, **pero inventó documentos obligatorios** (aranceles, becas, matrícula y una lista de solicitudes). **Resultado:** mecanismo documental verificado para la pregunta simple; calidad de respuesta y aplicación efectiva de la Skill **no validadas**. Reservar estos casos para la **sesión 5**.

La carpeta local se creó mediante `git clone` y se comprobó la existencia de los tres archivos. Esto solo acredita **presencia de archivos**, no ejecución de `puente_local.py`, que se abordará en sesiones 3–4.

## E. Lista de verificación

- [ ] El asistente personalizado está creado y **guardado**
- [ ] `system_prompt.txt` coincide con el texto del repositorio
- [ ] `normativa_ejemplo.md` está asociado y su información se verifica en una respuesta con fuente
- [ ] La bitácora está registrada en Notes **o** como Markdown local
- [ ] `retroalimentacion-formativa` se importó **y** asoció al asistente
- [ ] Se registra al menos una respuesta correcta y una prueba de límites
- [ ] Los **tres archivos originales** están en la carpeta local `scripts/`
- [ ] Los resultados imperfectos quedan documentados para la sesión 5

**Lecturas:** [Lab02](Lab02.md) · [Manual Técnico cap. 5](../vol2_manual_tecnico/cap05_mt.md) · [Guía de archivos y puente](../scripts/GUIA_CONTEXTO_SKILLS.md).