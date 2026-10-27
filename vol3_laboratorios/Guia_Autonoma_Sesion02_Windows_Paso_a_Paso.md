# Sesión 2 — Crear y comprobar un asistente académico en Open WebUI
## Guía autónoma paso a paso · Windows 10/11 · 120 minutos

**Objetivo:** crear un asistente especializado, incorporar un **System Prompt**, asociar un documento ficticio mediante **Knowledge**, registrar una **Nota o bitácora** e importar y asociar una **Skill**. Después, comprobar sus respuestas y registrar tanto aciertos como errores.

**Requisito:** haber terminado la [sesión 1](Guia_Autonoma_Sesion01_Windows_Paso_a_Paso.md): Ollama instalado, modelo `qwen2.5:1.5b` disponible y Open WebUI accesible. **No hay que reinstalar nada.** Las pantallas pueden variar según la versión de Open WebUI. Cuando cambien los nombres, busque la función equivalente y conserve la evidencia de lo realizado.

> **Cómo seguirla:** realice cada paso por orden. Al finalizar una etapa, compruebe el resultado antes de continuar. Los manuales enlazados al final son para profundizar, **no son necesarios para completar esta práctica**. Use únicamente información ficticia.

## Antes de configurar: cuatro componentes, cuatro funciones

| Componente | Pregunta que responde | Uso en esta sesión |
|---|---|---|
| **System Prompt** | ¿Cómo debe comportarse el asistente? | Define su rol y sus límites generales. |
| **Knowledge** | ¿Qué documentos puede consultar? | Aporta la normativa académica ficticia. |
| **Notes** | ¿Qué observó y decidió el participante? | Conserva resultados, dificultades y decisiones. |
| **Skills** | ¿Cómo realizar una tarea especializada? | Aporta instrucciones para retroalimentación formativa. |

Estos elementos **no se sustituyen entre sí**. Configurarlos es distinto de demostrar que el modelo los utiliza correctamente; por eso la guía incluye comprobaciones y pruebas.

## Etapa 1 — Abrir Open WebUI y comprobar el modelo (10 minutos)

**Paso 1.** Encienda el computador. Presione la tecla **Windows**, escriba **Ollama** y abra la aplicación si no está funcionando.

**Paso 2.** Presione nuevamente **Windows**, escriba **Open WebUI** y abra la aplicación instalada en la sesión anterior. Espere a que inicie.

**Paso 3.** Abra **Chrome** o **Edge**. Haga clic en la barra superior de direcciones, escriba `http://localhost:8080` y presione **Enter**. Si la aplicación indica otro puerto, utilice ese puerto. Inicie sesión en su cuenta local de Open WebUI cuando corresponda.

**Paso 4.** Compruebe que el selector de modelos muestra `qwen2.5:1.5b`. Si no aparece, abra PowerShell (tecla Windows → escriba **PowerShell** → presione Enter), escriba `ollama list` y presione **Enter**. Compruebe que Ollama está funcionando y vuelva a Open WebUI.

**Comprobación A:** puede abrir Open WebUI y seleccionar el modelo descargado. Si no ocurre, registre lo que ve y solicite apoyo antes de avanzar.

## Etapa 2 — Descargar los tres archivos del ejercicio (15 minutos)

**Paso 5.** En el navegador, abra **https://github.com/juliopez/ia-local-integracion**.

**Paso 6.** Busque el botón verde **Code**, haga clic y seleccione **Download ZIP**. Espere a que termine la descarga.

**Paso 7.** Presione **Windows + E** para abrir el Explorador de archivos. Entre a **Descargas**. Haga clic derecho sobre el ZIP descargado y seleccione **Extraer todo... → Extraer**.

**Paso 8.** Abra la carpeta descomprimida `ia-local-integracion-main` y luego la carpeta `scripts`. Identifique estos tres archivos, que usaremos sin modificar:

| Archivo | Dónde encontrarlo | Para qué sirve |
|---|---|---|
| `system_prompt.txt` | `scripts/system_prompt.txt` | Define rol, propósito y restricciones del asistente |
| `normativa_ejemplo.md` | `scripts/contexto/normativa_ejemplo.md` | Contiene las reglas académicas **ficticias** de consulta |
| `SKILL.md` | `scripts/skills/retroalimentacion-formativa/SKILL.md` | Describe una habilidad reutilizable |

**Paso 9.** Mantenga esta carpeta abierta. Para leer un archivo de texto, haga clic derecho → **Abrir con → Bloc de notas**. No cambie su contenido ni lo reemplace por respuestas generadas por IA.

**Comprobación B:** encontró los tres archivos y sabe en qué carpeta están.

## Etapa 3 — Crear y guardar el asistente (25 minutos)

### ¿Qué es un System Prompt y para qué sirve?

El **System Prompt** es el conjunto de instrucciones generales que orienta el comportamiento del asistente: qué rol cumple, a quién ayuda, cómo debe expresarse y qué límites debe respetar. **No es un documento de consulta ni aporta por sí solo la normativa académica.** En esta actividad utilizaremos `system_prompt.txt` para configurar un asistente que orienta consultas de estudiantes sin inventar reglas institucionales.

**Cómo reconocer su función:** después de crear el asistente, compare su propósito y tono con las instrucciones copiadas. Que el texto aparezca guardado confirma la configuración, pero todavía no demuestra que todas sus respuestas sean correctas.


**Paso 10.** Regrese a Open WebUI en el navegador. En la navegación lateral busque **Espacio de trabajo** (*Workspace*) y haga clic.

**Paso 11.** Ingrese a **Modelos** (*Models*) y seleccione **Crear** (*Create* o el botón **+**). Según la versión, se mostrará un formulario para crear un modelo/asistente personalizado.

**Paso 12.** Complete sus campos:

- **Nombre:** `Asistente Académico de Apoyo`
- **Modelo base:** `qwen2.5:1.5b` (o el modelo Ollama validado en la sesión 1).
- **Descripción:** `Asistente académico que orienta consultas estudiantiles utilizando normativa ficticia, reconociendo límites de información.`

**Paso 13.** Localice el campo **Prompt del sistema** (*System Prompt*). Vuelva al Explorador de archivos, abra `scripts/system_prompt.txt` con Bloc de notas, presione **Ctrl + A** para seleccionar todo y **Ctrl + C** para copiar. Regrese al formulario de Open WebUI, haga clic en **System Prompt** y presione **Ctrl + V**. Compruebe que el texto quedó completo.

**Paso 14.** **Deje Knowledge vacío por ahora.** Pulse **Guardar y Crear** (*Save & Create* o el botón equivalente). Espere la confirmación.

**Paso 15.** Vuelva a **Espacio de trabajo → Modelos**. Compruebe que aparece **Asistente Académico de Apoyo**. Si no aparece, no continúe: repita los pasos 11–14 y confirme que realmente guardó.

**Comprobación C:** el asistente está en la lista de Modelos, con su modelo base y System Prompt. Guarde una captura con **Windows + Shift + S**.

## Etapa 4 — Asociar Knowledge y comprobar una respuesta con evidencia (25 minutos)

### ¿Qué es Knowledge y para qué sirve?

**Knowledge (conocimiento)** permite vincular documentos que Open WebUI puede recuperar o incorporar como contexto al responder. A diferencia del **System Prompt**, que indica **cómo comportarse**, Knowledge aporta **información sobre la cual responder**. Aquí utilizaremos `normativa_ejemplo.md`, un documento **ficticio** que establece, entre otras reglas, un plazo de cinco días hábiles para solicitar revisión de una evaluación.

**Ejemplo:** ante «¿Cuántos días tengo para pedir revisión?», el asistente debería fundamentarse en esa normativa, no inventar una fecha. **Cómo comprobarlo:** confirme que el documento está asociado, examine las fuentes si aparecen y contraste la respuesta con el texto original. Subir un archivo no garantiza que se recupere ni que el modelo lo interprete correctamente.


**Paso 16.** En **Espacio de trabajo → Modelos**, abra **Asistente Académico de Apoyo** para **Editar**.

**Paso 17.** Busque el apartado **Conocimiento** (*Knowledge*). Seleccione **Subir archivos**, **Añadir** o la opción equivalente, según la versión.

**Paso 18.** En la ventana para seleccionar archivos, abra la carpeta descomprimida del repositorio y vaya a `scripts/contexto/`. Seleccione **`normativa_ejemplo.md`**, pulse **Abrir** y espere la carga. Confirme que está asociado al asistente. Para un documento pequeño, si su versión ofrece **Usar documento completo**, puede seleccionarlo para este ejercicio.

**Paso 19.** Pulse **Guardar y Actualizar** (*Save & Update*). Verifique que el archivo continúa asociado al volver a editar el asistente. **Subir el archivo no equivale a guardar los cambios.**

**Paso 20.** Inicie un **chat nuevo**. En el selector de modelos, elija **Asistente Académico de Apoyo**, no directamente el modelo base.

**Paso 21.** Escriba y envíe esta pregunta:

> Según la normativa de ejemplo, ¿cuántos días hábiles existen para solicitar revisión de una evaluación y a qué unidad debe dirigirse la solicitud?

**Resultado esperado según la normativa ficticia utilizada en el ejercicio:** **cinco días hábiles desde la publicación de la nota** y **coordinación académica**. Si aparece una indicación de fuente, como **1 Fuente**, haga clic y compruebe si cita `normativa_ejemplo.md`.

**Paso 22.** En el mismo asistente, haga esta segunda pregunta:

> ¿Qué documentos adicionales son obligatorios para solicitar la revisión de una evaluación?

**Resultado esperado:** el documento ficticio **no especifica documentos adicionales obligatorios**. Si el asistente inventa certificados, aranceles u otros anexos, **registre ese error**. No cambie aún la normativa ni el System Prompt para forzar una respuesta correcta.

**Comprobación D:** el documento quedó asociado, formuló ambas preguntas y registró los resultados, incluidas las respuestas incorrectas. Una fuente visible es evidencia de consulta, pero **no garantiza** que toda la respuesta sea correcta.

## Etapa 5 — Registrar una nota o bitácora (15 minutos)

### ¿Qué es una Note y para qué sirve?

Una **Note (nota)** es un espacio donde puede escribir y conservar observaciones de su trabajo. En nuestro taller funcionará como **bitácora del participante**: registrará el modelo utilizado, la pregunta, la respuesta, las fuentes observadas y los posibles errores. Puede utilizar la función Notes de Open WebUI **o** guardar un archivo Markdown en su computador.

**Ejemplo:** «La primera respuesta indicó cinco días y citó el documento; la segunda inventó un requisito». **Cómo comprobarlo:** vuelva a abrir la nota o el archivo y revise que conserva el registro. **Importante:** escribir algo en Notes **no hace que el asistente lo utilice automáticamente como Knowledge**.


**Paso 23.** En Open WebUI, busque **Notas** (*Notes*) en el espacio de trabajo. Si está disponible, seleccione **Crear**. Si no aparece en su instalación, abra **Bloc de notas** desde el menú Inicio y cree un archivo local llamado `bitacora_asistente.md`.

**Paso 24.** Escriba:

```text
Sesión 2 — Bitácora de mi asistente
Nombre: Asistente Académico de Apoyo
Modelo base: qwen2.5:1.5b
System Prompt: system_prompt.txt
Documento: normativa_ejemplo.md
Prueba 1: [copiar respuesta y anotar si coincidió con el documento]
Prueba 2: [copiar respuesta y anotar si inventó información]
Observaciones: [dificultades y posibles mejoras]
```

**Paso 25.** Guarde la nota o el archivo local. Si usa Bloc de notas, en **Archivo → Guardar como**, elija la carpeta extraída del repositorio o su carpeta personal del taller; en **Tipo** seleccione **Todos los archivos** y escriba el nombre `bitacora_asistente.md` para evitar que se guarde como `.txt`.

**Comprobación E:** dispone de una bitácora que conserva decisiones y resultados. **Notas no es automáticamente una base Knowledge**.

## Etapa 6 — Importar y asociar una Skill (20 minutos)

### ¿Qué es una Skill y para qué sirve?

Una **Skill (habilidad)** reúne instrucciones reutilizables para realizar una **tarea especializada**. No es lo mismo que Knowledge: **Knowledge aporta datos o documentos**, mientras que una Skill describe **cómo abordar un tipo de trabajo**. Tampoco sustituye al System Prompt, que establece el comportamiento general del asistente.

**Ejemplo del taller:** `retroalimentacion-formativa/SKILL.md` ofrece pautas para organizar retroalimentación educativa. **Cómo comprobarlo:** revise primero que la Skill fue **importada** y luego que quedó **asociada** al asistente. Estas dos comprobaciones acreditan la configuración, **no su aplicación efectiva**; la calidad de la respuesta se evaluará posteriormente.


**¿Qué es una Skill?** Es un conjunto de instrucciones reutilizables para una tarea específica. **Importarla y asociarla no demuestra automáticamente que el modelo la utilice correctamente.**

**Paso 26.** En Open WebUI, vaya a **Espacio de trabajo → Habilidades** (*Skills*). Haga clic en **Crear** o el botón **+**.

**Paso 27.** Busque **Importar desde enlace** (*Import from URL* o función equivalente). Copie y pegue exactamente esta dirección:

```text
https://raw.githubusercontent.com/juliopez/ia-local-integracion/main/scripts/skills/retroalimentacion-formativa/SKILL.md
```

**Paso 28.** Confirme que el importador reconoce la habilidad **`retroalimentacion-formativa`**. Pulse **Importar selección**. Compruebe que aparece entre las habilidades disponibles.

**Paso 29.** Regrese a **Espacio de trabajo → Modelos**, abra **Asistente Académico de Apoyo → Editar**, busque **Habilidades** y seleccione **`retroalimentacion-formativa`**. Pulse **Guardar y Actualizar**.

**Paso 30.** Vuelva a editar el asistente: confirme que la Skill sigue asociada. Tome una captura. No es necesario demostrar mejoras atribuibles a la Skill en esta sesión: ese análisis se realizará en la **sesión 5**.

**Comprobación F:** la habilidad fue **importada y asociada**. Si la versión de Open WebUI no muestra el menú Habilidades o no admite la importación por enlace, registre una captura y conserve el archivo `SKILL.md` para seguimiento; **no improvise una instalación alternativa**.

## Cierre de la sesión — Verifique su trabajo (10 minutos)

- [ ] Puedo abrir Open WebUI y seleccionar el modelo de Ollama.
- [ ] Tengo los archivos `system_prompt.txt`, `normativa_ejemplo.md` y `SKILL.md`.
- [ ] Mi asistente **Asistente Académico de Apoyo** está guardado.
- [ ] El System Prompt está copiado íntegramente.
- [ ] Knowledge contiene el documento ficticio y guardé los cambios.
- [ ] Hice la pregunta del plazo y la pregunta sobre documentos adicionales.
- [ ] Registré aciertos, errores y fuentes, si aparecieron.
- [ ] Guardé una nota o bitácora.
- [ ] Importé **y** asocié la Skill, o documenté por qué no fue posible.

## Si aparece un problema

| Problema | Qué hacer primero |
|---|---|
| No encuentro el archivo | En el Explorador vaya a **Descargas → ia-local-integracion-main → scripts**; si sigue comprimido, use **Extraer todo** |
| No aparece mi asistente | Vuelva a **Modelos** y compruebe que pulsó **Guardar y Crear** |
| El modelo base no aparece | Compruebe Ollama y `ollama list`; revise la conexión local |
| Subí el documento, pero no está asociado | Vuelva a editar el asistente, añada Knowledge y pulse **Guardar y Actualizar** |
| El asistente no cita la normativa o inventa detalles | Confirme archivo y modelo seleccionados. Registre el resultado; no atribuya automáticamente el fallo a la Skill |
| Aparece un error de almacenamiento vectorial `503` | Registre el mensaje y consulte al docente. No aplique comandos Docker ni cambios de base de datos sin diagnóstico |
| No veo Habilidades/Skills | La interfaz depende de la versión. Registre una captura; conserve `SKILL.md` y pida orientación |
| No puedo importar la Skill | Verifique Internet y que la URL esté completa; no descargue archivos de sitios no oficiales |

**Recuerde:** Open WebUI permite diseñar y probar el asistente, pero no sincroniza automáticamente su Knowledge, sus Notes ni sus Skills con el puente Python de las sesiones 3 y 4. Por eso es importante conservar **los archivos originales**.

### Material para profundizar (opcional)

- [Laboratorio 2](Lab02.md): actividades de diseño y fundamento pedagógico.
- [Manual Técnico — capítulo 5](../vol2_manual_tecnico/cap05_mt.md): asistentes, configuración y pruebas.
- [Manual del Participante — capítulo 2](../vol1_manual_participante/cap02.md): propósito, rol y restricciones.
- [Registro de incidencias Windows y Ubuntu](Guia_Sesion02_Knowledge_Skills_Windows_Ubuntu.md): diagnóstico avanzado.

**Fin de la sesión 2.** En la sesión 3 comenzará la captura de solicitudes mediante Google Forms, Sheets y Apps Script.
