# Ruta autónoma para Windows · Sesiones 1 y 2

> **Navegación autónoma y referencias cruzadas:** [Volver al itinerario de cinco etapas](../EMPEZAR_AQUI.md) · [Volumen 1 — conceptos](../vol1_manual_participante/) · [Volumen 4 — portafolio](../vol4_proyecto_integrador/) · [Volumen 5 — consulta técnica](../vol5_manual_referencia/). Los procedimientos con capturas originales permanecen en el **Manual Técnico (volumen 2)**; la guía autónoma indica el orden, no sustituye las imágenes.

**Taller IA local + Google Workspace · Guía del participante sin profesor presente**  
**Plataforma principal:** Windows 10/11 de 64 bits. **Revisión documental:** 25-10-2026. **Duración del taller:** sesiones de 120 min; esta guía identifica la ruta mínima y las ampliaciones opcionales.  
**Fuentes obligatorias:** [Laboratorio 1](Lab01.md), [Laboratorio 2](Lab02.md), [Manual Técnico](../vol2_manual_tecnico/cap04_mt.md), [guía complementaria sesión 2](Guia_Sesion02_Knowledge_Skills_Windows_Ubuntu.md).

> **Ruta de elección:** ¿Está en Windows? Siga esta guía y las secciones de **PowerShell y Python/pip** del Manual Técnico. ¿Está en Ubuntu? Consulte la [guía complementaria Ubuntu](Guia_Ubuntu_Sesion01_Validacion_2026.md). **No combine** comandos Docker de Ubuntu y Python/pip de Windows como si fueran una sola instalación.
>
> **Resultado mínimo aceptable:** sesión 1 = una conversación local real en Open WebUI; sesión 2 = asistente guardado con System Prompt, documento vinculado, Skill importada y asociada, nota/bitácora y archivos originales disponibles localmente. Las respuestas incorrectas se **registran**, no se maquillan.

## Antes de comenzar: comprobación autónoma (Windows)
1. Necesita permisos para instalar programas, conexión a Internet para descargar software y un navegador; después de descargar el modelo, podrá ejecutar la inferencia local. Algunas instalaciones institucionales bloquean PowerShell, instaladores, paquetes Python o los puertos locales: en ese caso contacte **soporte TI**, no desactive defensas corporativas.
2. Abra **Administrador de tareas → Rendimiento** para revisar memoria y CPU; si tiene GPU, revise su memoria dedicada. En **Configuración → Sistema → Almacenamiento**, registre espacio libre. Los modelos y dependencias necesitan varios GB; verifique antes de descargar.
3. Abra **PowerShell** mediante Inicio (normal, no como administrador salvo instrucción autorizada). Ejecute:

```powershell
python --version
py --version
ollama --version
```

Que uno de los dos primeros comandos no exista **no implica** por sí solo un fallo si el otro funciona. Si falta Python u Ollama, vuelva al Manual Técnico: [capítulo 2 — Ollama](../vol2_manual_tecnico/cap02_mt.md) y [capítulo 4 — Python/Open WebUI](../vol2_manual_tecnico/cap04_mt.md). No use el instalador de Python de una fuente no oficial.
4. Cree un registro local de evidencias (documento o archivo Markdown). Anote fecha, RAM, espacio libre, modelo y cualquier error **sin contraseñas ni datos personales**.

### Mapa de decisiones
| Situación | Procedimiento |
|---|---|
| Ollama y Open WebUI ya funcionan | Ir a **Sesión 1, comprobación**; no reinstalar |
| Ollama funciona y Open WebUI no | Seguir Manual Técnico capítulo 4 por **Python/pip**; mantener la consola abierta al ejecutar |
| Ninguno está instalado | Seguir capítulos 2–4 en ese orden y volver a esta guía |
| Ordenador administrado, permisos insuficientes o antivirus institucional impide instalar | Detener la instalación y consultar soporte TI; no ejecutar descargas privilegiadas no autorizadas |
| GPU insuficiente | Seleccionar un modelo pequeño compatible y probar con CPU si hay RAM suficiente; no instalar drivers solo por esta guía |

## Sesión 1 — Fundamentos, instalación y conversación

### 1. Elegir un modelo proporcionado al equipo
Abra [llmfit](https://github.com/AlexsJones/llmfit). **Opcional:** en Windows puede usar una versión nativa desde [Releases](https://github.com/AlexsJones/llmfit/releases), o `scoop install llmfit` **solo si Scoop ya está instalado**. No es necesario instalar Scoop para completar el laboratorio. Si no usa llmfit, documente CPU, RAM y GPU, y elija directamente un modelo pequeño de [Ollama Library](https://ollama.com/library).

**Referencia de nuestro ensayo, no obligación universal:** `qwen2.5:1.5b`. Un modelo grande no es recomendable si la RAM/VRAM es limitada. No prometa velocidad ni exactitud: debe comprobar ambas en la práctica.

### 2. Instalar y comprobar Ollama
Use el procedimiento del [Manual Técnico · cap. 2](../vol2_manual_tecnico/cap02_mt.md). Descargue Ollama desde https://ollama.com/download/windows. Con la aplicación instalada:

```powershell
ollama --version
ollama pull qwen2.5:1.5b
ollama list
ollama run qwen2.5:1.5b
```

El identificador es un **ejemplo comprobado**; si eligió otro modelo, sustituya exactamente el nombre. En el chat de terminal consulte: *«Explica brevemente qué es un modelo de lenguaje local; indica una ventaja y una limitación»*. Para terminar esa conversación, use `/bye`.

**Checkpoint S1-A:** `ollama list` muestra el modelo y `ollama run` devuelve texto. Si funciona en la terminal, Ollama está operativo aunque Open WebUI aún no lo esté.

### 3. Instalar y ejecutar Open WebUI (método del curso para Windows)
**Este taller utiliza en Windows la ruta documentada en el [Manual Técnico · cap. 4 §§4.2–4.7](../vol2_manual_tecnico/cap04_mt.md): Python/pip**, no la receta Docker de Ubuntu. Use Python compatible con la versión del manual y, preferentemente, un entorno virtual para evitar conflictos.

Compruebe Python y pip:

```powershell
python --version
python -m pip --version
```

Para una instalación aislada en su carpeta personal, **solo si Python funciona**:

```powershell
mkdir "$HOME\ia-local-webui" -ErrorAction SilentlyContinue
cd "$HOME\ia-local-webui"
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install open-webui
.\.venv\Scripts\open-webui.exe serve
```

La instalación puede tardar y consumir espacio. **Mantenga esta ventana abierta** mientras utiliza Open WebUI. Si la versión actual cambia los comandos, siga **las instrucciones y requisitos de versión del Manual Técnico y de la [documentación oficial](https://docs.openwebui.com/getting-started/quick-start/)** antes de intentar reparaciones. No instale otra copia con Docker encima de esta instalación.

Abra **http://localhost:8080** si inició Open WebUI con el puerto predeterminado del servicio Python, o el **puerto mostrado por la consola**. No confunda `8080` (instalación Python habitual) con `3000` (puerto usado en el ensayo Docker Ubuntu).

**Checkpoint S1-B:** la web abre, puede iniciar sesión y aparece un modelo Ollama; si no aparece, revise la configuración de conexión Ollama desde Open WebUI y el estado de Ollama.

### 4. Primeras consultas y comparación de prompts
Con el modelo seleccionado en Open WebUI, ejecute y registre:
- **Consulta básica:** «¿Qué es un modelo de lenguaje local?».
- **Consulta estructurada:** «Explica qué es un modelo de lenguaje local para un docente universitario. Responde en tres viñetas: definición, ventaja y limitación».
- Compare claridad, cumplimiento del formato y alguna afirmación dudosa. **No suponga que una respuesta bien redactada es necesariamente correcta.**

Consulte las actividades de exploración y construcción de prompts del [Laboratorio 1](Lab01.md). El [tokenizador de OpenAI](https://platform.openai.com/tokenizer) es una demostración conceptual opcional; sus tokens no se deben presentar como identificadores exactos del modelo Qwen local.

**Checkpoint S1-C:** guarde captura de Open WebUI con el modelo seleccionado, dos consultas y un comentario sobre sus diferencias. Si no funciona, documente mensaje de error y diríjase a la sección «Qué hacer si falla».

## Sesión 2 — Asistente, Knowledge, Notes y Skills

**Prerrequisito:** haber alcanzado S1-A, S1-B y S1-C. Siga también la [guía detallada de validación de la sesión 2](Guia_Sesion02_Knowledge_Skills_Windows_Ubuntu.md).

### 1. Preparar los archivos *antes* de trabajar en el navegador
Desde https://github.com/juliopez/ia-local-integracion seleccione **Code → Download ZIP** y **Extraer todo**. Abra la carpeta extraída, luego `scripts/`. Debe encontrar:
- `system_prompt.txt`
- `contexto/normativa_ejemplo.md`
- `skills/retroalimentacion-formativa/SKILL.md`

No cambie nombres ni sustituya el contenido con respuestas generadas por IA. Copie los archivos íntegros. Para copiar un prompt, ábralo con Bloc de notas o VS Code y utilice Ctrl+A → Ctrl+C.

### 2. Crear el asistente y **guardarlo primero**
En Open WebUI, **Espacio de trabajo → Modelos → Crear**:
- **Nombre:** Asistente Académico de Apoyo.
- **Modelo base:** el modelo local verificado en la sesión 1.
- **Descripción:** «Asistente académico orientado a consultas de estudiantes de educación superior, con límites explícitos y apoyo en documentos ficticios».
- **Prompt del sistema:** pegue el texto íntegro de `scripts/system_prompt.txt`.
- **Conocimiento:** déjelo inicialmente vacío.
- Pulse **Guardar y Crear** y compruebe que el asistente figura en **Modelos**. **No avance si no aparece**. Esta secuencia evita perder cambios no guardados.

### 3. Asociar Knowledge y verificar que se usa
Entre a editar el asistente → **Conocimiento → Subir Archivos** → seleccione `normativa_ejemplo.md`; confirme asociación y pulse **Guardar y Actualizar**. Para un documento corto, revise si está disponible **Usando Documento Completo**. Según la versión de Open WebUI, los nombres pueden diferir.

En una **conversación nueva con el asistente personalizado**, pregunte:

> Según la normativa de ejemplo, ¿cuántos días hábiles tengo para solicitar revisión de una evaluación y a qué unidad debo dirigirla?

**Esperado:** cinco días hábiles **desde la publicación de la nota**; **coordinación académica**. Si aparece **«1 Fuente»**, ábralo y verifique `normativa_ejemplo.md`.

**Pregunta de límites:** «¿Qué documentos adicionales son obligatorios para solicitar revisión?». Respuesta válida: el texto ficticio **no especifica** documentos adicionales. **No es válida** una lista inventada de aranceles, becas o matrícula. Registre ambos resultados.

### 4. Notas como bitácora y Skill reutilizable
Para documentar decisiones use **Notas → Crear** y escriba propósito, modelo, prompt, documento asociado, preguntas y resultados. **Alternativa igualmente válida:** archivo local `bitacora_asistente.md`. Las notas **no son** una base Knowledge automática.

Para la Skill, vaya a **Espacio de trabajo → Habilidades → Crear → Importar desde Enlace** y pegue:

`https://raw.githubusercontent.com/juliopez/ia-local-integracion/main/scripts/skills/retroalimentacion-formativa/SKILL.md`

Confirme que el importador identifica `retroalimentacion-formativa`, pulse **Importar selección** y verifique **Habilidades 1**. **Después** edite el asistente → **Habilidades → retroalimentacion-formativa → Guardar y Actualizar**. Ver que la Skill esté asociada **no demuestra** que el modelo la aplique sin errores.

**Checkpoint S2:** asistente guardado; System Prompt original; documento asociado; pregunta de cinco días hábiles y coordinación académica correcta con fuente cuando exista; nota/bitácora; Skill asociada; tres archivos locales conservados. Si el modelo inventa anexos obligatorios, **registre el fallo**; la mejora sistemática pertenece a la sesión 5.

## Qué hacer si falla: diagnóstico y salida autónoma

| Problema | Primero compruebe | Acción segura |
|---|---|---|
| `ollama` no reconocido | Instalación y nueva ventana PowerShell | Repetir capítulo 2; comprobar PATH y versión sin editar variables a ciegas |
| Modelo no aparece | `ollama list`, servicio Ollama iniciado | Configurar conexión Ollama en Open WebUI; verificar el puerto local `11434` |
| Página no abre | Consola que ejecuta Open WebUI, puerto mostrado | Mantener el proceso activo; usar la dirección exacta mostrada; no confundir 8080 y 3000 |
| `pip` falla | Versión de Python compatible, espacio, red y permiso | Consultar capítulo 4; usar entorno virtual; si el equipo es administrado acudir a TI |
| Error `503` relacionado con PGVECTOR | Motor vectorial realmente configurado | Consultar [incidencia documentada](Guia_Sesion02_Knowledge_Skills_Windows_Ubuntu.md); no copiar la solución Docker Ubuntu en una instalación Python |
| Documento asociado pero respuesta inventada | Texto visible, fuente, modo de herramientas | En el ensayo, **Heredado** corrigió la recuperación; probar solo si se reproduce el problema, guardar y consultar de nuevo |
| Se pierde el formulario | Modelo todavía no guardado | Recrearlo y pulsar Guardar **antes** de asociar documentos |
| Skill importada pero sin efecto observable | Habilidades 1 y asociación al modelo | Guardar el modelo; registrar el fallo, sin cambiar `SKILL.md` ni atribuirle beneficios no medidos |

**Detenga la práctica y solicite soporte técnico** si aparecen bloqueos administrativos, errores de disco, problemas de seguridad o fallos persistentes después de la ruta documentada. **Un error bien registrado es una evidencia válida del intento**, no una razón para improvisar comandos peligrosos.

## Autoevaluación final (marque con evidencia)
| Verificación | Sí/No | Evidencia que debe conservar |
|---|---|---|
| S1: Ollama ofrece un modelo local | □ | `ollama list` y conversación real |
| S1: Open WebUI conversa con Ollama | □ | Captura del chat |
| S1: compara dos instrucciones | □ | Dos respuestas y reflexión breve |
| S2: asistente creado y guardado | □ | Vista Modelos 1 |
| S2: prompt original y Knowledge asociado | □ | Configuración y fuente |
| S2: registra información ausente sin inventarla | □ | Pregunta de límites: acierto o fallo documentado |
| S2: Skill importada y asociada | □ | Vista Habilidades 1 y configuración |
| S2: bitácora registrada | □ | Nota o archivo Markdown |
| S2: archivos locales listos | □ | Vista de los 3 archivos en `scripts/` |

**Continuación:** la captura de Forms, Sheets y Apps Script y la ejecución de `puente_local.py` se realizan en **sesiones 3 y 4**. La comparación de resultados y optimización sistemática corresponde a la **sesión 5**. No se necesita completar esos pasos para cerrar las dos primeras sesiones.
