# Sesión 5 — Mejorar y evaluar un asistente de IA local
## Guía autónoma paso a paso · Windows 10/11 · 120 minutos

**Objetivo:** identificar problemas reales en las respuestas de su asistente, aplicar **al menos dos mejoras justificadas**, repetir las mismas preguntas y comparar los resultados con evidencia. No necesita instalar otro modelo.

**Antes de comenzar:** utilice el modelo local elegido para su equipo, con Ollama y el puente Python configurados durante las sesiones 3 y 4. Conserve `scripts/system_prompt.txt`, `scripts/contexto/normativa_ejemplo.md`, las Skills y su bitácora. Open WebUI fue explorado en la sesión 2, pero **no es el entorno de ejecución de esta práctica**. Todas las pruebas se realizan mediante `--modo prueba`: no se envían correos ni se modifica Sheets. Compare siempre con el mismo modelo y la misma configuración, salvo el cambio deliberado que está evaluando.

> **Cómo seguir la guía:** ejecute cada paso y compruebe el resultado antes de continuar. Puede apoyarse en los manuales al terminar, pero no necesita cambiar de documento para descubrir los pasos de la práctica. **Use solamente normativa y consultas ficticias.** No pruebe el envío de Gmail ni modifique datos reales.

## ¿Qué significa mejorar un asistente?

**Mejorar no significa conseguir una respuesta más larga o más convincente.** Significa detectar un problema, cambiar algo concreto y comprobar si las nuevas respuestas son más precisas, pertinentes o fieles a los documentos.

| Concepto | Significado en la práctica |
|---|---|
| **Exactitud** | Las afirmaciones coinciden con los antecedentes disponibles. |
| **Fidelidad a las fuentes** | Los plazos y requisitos mencionados realmente aparecen en el documento. |
| **Reconocimiento de límites** | El asistente admite cuando no tiene antecedentes suficientes. |
| **Claridad** | La respuesta resulta comprensible para sus usuarios. |
| **Alucinación** | El asistente presenta una afirmación inventada o no sustentada como si fuera verdadera. |
| **Comparación antes/después** | Se repite la **misma pregunta** antes y después de modificar el asistente. |

**Ejemplo:** si `normativa_ejemplo.md` no exige certificados adicionales, responder «debe adjuntar un certificado de matrícula» sería una afirmación no respaldada. Que Open WebUI muestre una fuente **no convierte automáticamente la respuesta en correcta**.

## Bloque 1 — Comprender qué vamos a evaluar (15 minutos)

**Paso 1.** Confirme que Ollama está ejecutándose y que su modelo local elegido está instalado. No necesita abrir Open WebUI.

**Paso 2.** Abra la carpeta del repositorio en el Explorador de archivos de Windows y localice `scripts/puente_local.py`.

**Paso 3.** Abra PowerShell en la raíz del repositorio y ejecute `py scripts/puente_local.py --help`. Compruebe que aparece la opción `--pregunta`. Si utiliza Ubuntu, sustituya `py` por `python3`.

**Paso 4.** Abra `scripts/contexto/normativa_ejemplo.md` y compruebe qué plazos y requisitos establece y qué información no especifica.

**Paso 5.** Abra su bitácora de trabajo y anote el objetivo: «Evaluar el asistente con tres preguntas, implementar dos mejoras y comparar las respuestas antes y después».

**Comprobación A:** puede abrir el asistente y el texto normativo. Comprende que una respuesta bien redactada puede contener información inventada.

## Bloque 2 — Diagnosticar y mejorar el asistente (60 minutos)

### Etapa 1. Registrar tres respuestas iniciales (15 minutos)

**Paso 6.** En PowerShell, desde la raíz del repositorio, ejecute para cada pregunta `py scripts/puente_local.py --modo prueba --pregunta "TEXTO DE LA PREGUNTA"`, sustituyendo el texto entre comillas por las preguntas de los pasos 7, 9 y 11. En Ubuntu use `python3` en lugar de `py`. El modo prueba consulta Ollama y archivos locales; no modifica Sheets ni envía Gmail.

**Paso 7.** Copie y envíe esta pregunta, basada en información del ejercicio:

> Según la normativa de ejemplo, ¿cuántos días hábiles tengo para solicitar la revisión de una evaluación y a quién debo dirigir la solicitud?

**Paso 8.** Guarde la respuesta íntegra en su bitácora bajo el título **Caso 1 — Antes**. Compare con la normativa ficticia; la referencia utilizada en el taller establece **cinco días hábiles desde la publicación de la nota** y **coordinación académica**. Si hay una cita o una indicación de fuente, ábrala y compruebe que respalda el contenido.

**Paso 9.** Ejecute otra vez el modo prueba con la siguiente pregunta:

> ¿Qué documentos adicionales son obligatorios para solicitar la revisión de una evaluación?

**Paso 10.** Copie la respuesta como **Caso 2 — Antes**. Compruebe si afirma la existencia de certificados, aranceles o anexos que **no aparecen** en el documento. En ese caso, anote «requisito no respaldado», no «respuesta correcta».

**Paso 11.** Ejecute el modo prueba con la tercera pregunta:

> Soy estudiante y no entiendo cómo solicitar la revisión de una evaluación. ¿Puedes orientarme con pasos claros, distinguiendo los requisitos documentados de las recomendaciones generales?

**Paso 12.** Guarde la respuesta como **Caso 3 — Antes**. Observe si el asistente diferencia reglas documentadas, consejos generales e información que no conoce.

**Comprobación B:** tiene **tres preguntas literales**, tres respuestas originales y notas sobre exactitud, claridad y respaldo documental. Conserve exactamente las mismas preguntas para el resto de la práctica.

### Etapa 2. Elegir y justificar dos mejoras (10 minutos)

**Paso 13.** Revise las tres respuestas y anote **al menos dos problemas concretos**. Ejemplos: inventar un requisito, no reconocer límites, contestar sin consultar la fuente, entregar una respuesta confusa o contradictoria. **Diagnóstico orientativo:** si el dato no existe en Knowledge, el problema es falta de evidencia; si el dato sí está, compruebe que llega al modelo y que las instrucciones no se contradicen; si la respuesta mezcla procedimientos, revise qué Skills recibe.

**Paso 14.** Para cada problema elija **una intervención**: ajustar el **System Prompt**, revisar la asociación de **Knowledge**, corregir una copia autorizada de la normativa ficticia, mejorar la estructura de respuesta o comprobar la **Skill** asociada. **Pista importante:** un prompt más largo no siempre es mejor; elimine instrucciones duplicadas antes de añadir otras. Una Skill no sustituye Knowledge, y cargar Skills ajenas a la pregunta puede confundir a algunos modelos. No modifique todo simultáneamente.

**Paso 15.** Complete esta tabla en su bitácora:

| Problema observado | Componente que modificaré | Cambio previsto | Resultado que espero |
|---|---|---|---|
| [Escriba un problema real] | [System Prompt/Knowledge/etc.] | [Una modificación concreta] | [Un resultado comprobable] |
| [Escriba otro problema] | [Componente] | [Segunda modificación] | [Un resultado comprobable] |

**Comprobación C:** puede explicar por qué cada cambio está relacionado con una dificultad observada. No se exige cambiar una Skill solo para completar una lista.

### Etapa 3. Aplicar las mejoras y guardar versiones (25 minutos)

**Paso 16.** Abra `scripts/system_prompt.txt`, `scripts/contexto/` y `scripts/skills/` en el Explorador. Antes de modificar archivos, guarde una copia de las instrucciones y registre el nombre del modelo, los documentos y la Skill implicada. No modifique el código Python para esta actividad.

**Paso 17.** Aplique **solo la primera mejora** seleccionada. Ejemplo, si el problema es inventar obligaciones, agregue en el System Prompt una instrucción específica:

> Cuando el usuario pregunte por un requisito obligatorio, menciona solamente los que estén expresamente indicados en el documento disponible. Si no hay información suficiente, dilo claramente y no inventes requisitos.

Este texto es **un ejemplo**: adáptelo al problema real diagnosticado, sin alterar la normativa original.

**Paso 18.** Guarde `scripts/system_prompt.txt` con **Ctrl + S** y compruebe que el cambio se conservó. No publique datos privados ni URLs de Apps Script.

**Paso 19.** Repita `--modo prueba --pregunta "…"` con la misma pregunta literal del caso elegido. Guarde el resultado como **Después de mejora 1** y contrástelo con el documento.

**Paso 20.** Aplique **la segunda mejora**, relacionada con el otro problema. Por ejemplo, verifique el documento que está asociado en **Conocimiento/Knowledge** y vuelva a guardarlo si la asociación faltaba, o ajuste una instrucción de formato. Si modifica el documento, trabaje sobre una copia autorizada y evite mantener dos versiones contradictorias.

**Paso 21.** Guarde el `SKILL.md` o documento modificado y vuelva a ejecutar el modo prueba. El puente selecciona como máximo una Skill reconocida mediante expresiones de la consulta; añadir una carpeta nueva no la activa automáticamente. Registre exactamente qué cambió.

**Paso 22.** Repita la pregunta original relacionada con la segunda mejora mediante `--modo prueba --pregunta "…"`. Guarde el resultado como **Después de mejora 2** e indique si mejoró, empeoró o no cambió. Si empeora, registre la evidencia y considere revertir el cambio.

**Comprobación D:** tiene dos cambios identificados y guardados, sus configuraciones anteriores y posteriores, y al menos una prueba por intervención. Cuando sea posible, modifique **una variable por vez**.

**Pistas de optimización para cualquier modelo:** (1) formule una regla clara en vez de repetirla en tres lugares; (2) entregue únicamente documentos pertinentes y verifique que el modelo los recibe; (3) use una Skill adecuada al tipo de tarea, no todas por defecto; (4) pida reconocer información ausente, sin inventarla; (5) si la respuesta es confusa, ensaye una instrucción breve de formato. El tamaño del contexto y los resultados pueden variar según el modelo y el equipo. **No se exige cambiar de modelo, instalar herramientas ni modificar Python.**

### Etapa 4. Comparar resultados con las mismas preguntas (10 minutos)

**Paso 23.** Con la configuración final, ejecute el modo prueba tres veces y repita exactamente las preguntas de los pasos **7, 9 y 11**, sin añadir pistas ni respuestas esperadas.

**Paso 24.** Copie las tres respuestas finales y complete:

| Caso | Resultado antes | Resultado después | Evidencia que lo respalda | Evaluación |
|---|---|---|---|---|
| 1. Plazo y responsable | [Resumen] | [Resumen] | [Texto/fuente] | Mejoró / igual / empeoró |
| 2. Requisitos no especificados | [Resumen] | [Resumen] | [Texto/fuente] | Mejoró / igual / empeoró |
| 3. Orientación al estudiante | [Resumen] | [Resumen] | [Texto/fuente] | Mejoró / igual / empeoró |

**Prueba de generalización (pregunta nueva).** Sin modificar nuevamente el asistente, ejecute una cuarta consulta que **no haya utilizado durante las mejoras**:

> ¿Es obligatorio presentar un certificado digital para solicitar la revisión de una evaluación?

Contraste la respuesta con `normativa_ejemplo.md`. Compruebe si distingue correctamente entre requisitos exigidos y requisitos que el documento no establece. Registre el resultado. Esta prueba complementa las tres comparaciones anteriores.

**Paso 25.** Escriba dos o tres frases: ¿qué problema se redujo?, ¿qué problema continúa?, ¿qué evidencia respalda su conclusión? **Una única respuesta correcta no demuestra fiabilidad general.**

**Comprobación E:** compara tres casos antes y después con la **misma redacción** y distingue observaciones de suposiciones.

## Taller guiado — System Prompt, Skills y Knowledge en el puente local

**Propósito.** Reconocer tres componentes que influyen en la respuesta: **System Prompt** (reglas generales), **Knowledge** (información documental) y **Skill** (procedimiento aplicable a la consulta). En esta sesión se utiliza exclusivamente **Python + Ollama**. Open WebUI fue presentado en la sesión 2, pero no se requiere aquí.

### Reconocer los archivos utilizados

**Paso B1.** Abra la carpeta `scripts/` del repositorio. Identifique `puente_local.py`, `system_prompt.txt`, `contexto/normativa_ejemplo.md` y las subcarpetas de `skills/`. El puente consulta directamente la API de Ollama y no recupera automáticamente configuraciones guardadas en Open WebUI.

**Paso B2.** Abra las Skills `respuesta-basada-en-evidencias/SKILL.md` y `retroalimentacion-formativa/SKILL.md`. Compare sus propósitos: una orienta respuestas sobre normas y requisitos documentados; la otra sirve para retroalimentar un trabajo proporcionado. **No se necesitan ambas para la misma pregunta.**

**Paso B3.** El puente utiliza `seleccionar_skill()` para elegir como máximo una Skill reconocida mediante expresiones presentes en la consulta. Este selector es sencillo y no equivale a comprender semánticamente todas las preguntas. Copiar un `SKILL.md` adicional no garantiza que el puente lo active.

**Paso B4.** Compruebe que `normativa_ejemplo.md` contiene las reglas necesarias para responder. El puente lee archivos `.md` y `.txt` de `scripts/contexto/`; no utiliza RAG ni búsqueda vectorial.

### ¿Por qué utilizamos archivos TXT o Markdown para Knowledge?

Cuando incorporamos conocimiento a nuestro asistente, necesitamos que el modelo reciba el contenido del documento en un formato que pueda interpretar.

Los archivos `.txt` y `.md` contienen **texto plano**. Nuestro programa Python puede leerlos directamente y enviar su contenido a Ollama junto con la consulta del usuario. Markdown permite, además, organizar ese texto con títulos, listas y tablas sencillas.

Los archivos PDF y Word tienen estructuras más complejas: pueden incluir formato, tablas, imágenes y otros elementos que requieren herramientas adicionales para extraer el texto correctamente.

```text
Documento .txt o .md
         ↓
Python lee su contenido
         ↓
Ollama recibe texto + consulta
         ↓
El modelo genera una respuesta
```

**¿Significa que no podemos utilizar PDF o Word?** No. Podemos aprovechar su información después de extraer el texto y guardarlo en un formato compatible con el puente.

**¿Por qué no incorporamos esos formatos directamente?** Porque el objetivo de esta práctica es comprender cómo un asistente utiliza conocimiento externo sin agregar todavía la complejidad de procesar diferentes formatos documentales. El puente podría ampliarse posteriormente con bibliotecas de Python para extraer texto de PDF y Word, sin necesidad de cambiar el modelo.

**Importante:** esta es una decisión de implementación del **puente Python del taller**, no una incapacidad general de Ollama o de los modelos de lenguaje. Convertir un documento tampoco garantiza respuestas correctas: compruebe que el texto esté completo, sea legible y que las afirmaciones del asistente estén respaldadas por él.

### Pregunta frecuente: ¿puedo utilizar PDF o Word como Knowledge?

**Sí, como fuente de información, pero no directamente en este puente.** El puente del taller lee `.md` y `.txt`; colocar un archivo `.pdf`, `.docx` o `.doc` en `scripts/contexto/` no hará que el modelo lo lea.

**Paso B5.** Si desea utilizar información de un PDF o documento Word, abra el archivo con una herramienta apropiada, extraiga o copie su contenido textual y guarde una **copia autorizada** como `.txt` o `.md` dentro de `scripts/contexto/`. Revise encabezados, tablas, números y errores de conversión. Un PDF escaneado puede requerir OCR; copiar un archivo no equivale a extraer su texto.

**Paso B6.** Pruebe una pregunta cuya respuesta conozca y compruebe si el modelo utiliza correctamente el texto extraído. Si falla, revise primero si el documento realmente llegó al contexto antes de añadir instrucciones o cambiar de modelo.

### Pistas para optimizar las respuestas

**Paso B7.** Cuando una respuesta sea incorrecta, identifique la causa probable antes de intervenir:

| Síntoma | Qué revisar primero |
|---|---|
| Inventa una norma o un costo | ¿Existe respaldo en Knowledge? ¿El System Prompt exige reconocer información ausente? |
| Ignora una regla que sí existe | ¿El documento llegó al modelo? ¿Hay instrucciones redundantes o contradictorias? |
| Mezcla retroalimentación con normas | ¿La Skill seleccionada corresponde a la pregunta? |
| Repite o contradice sus conclusiones | ¿Se pueden simplificar las instrucciones y el formato de respuesta? |
| Responde de forma diferente entre intentos | ¿Se mantiene el mismo modelo y la misma configuración? ¿Conviene repetir un caso crítico? |

**Paso B8.** Pruebe una mejora por vez y compare siempre con la pregunta original. No se exige cambiar de modelo, instalar herramientas adicionales ni modificar el código Python. Un modelo más grande tampoco garantiza automáticamente una respuesta mejor.

**Comprobación:** puede explicar qué archivo contiene los hechos, cuál establece reglas generales, cuándo se selecciona una Skill y por qué una respuesta aparentemente convincente puede ser incorrecta.

---

### ¿Por qué mi asistente sigue cometiendo errores después de optimizarlo?

Aunque **System Prompt**, **Knowledge** y **Skills** estén alineados, sin contradicciones ni instrucciones redundantes, la calidad de las respuestas también depende del **modelo de lenguaje local**.

- **Capacidad del modelo:** distintos modelos tienen diferente habilidad para seguir instrucciones, interpretar documentos, razonar y mantener respuestas coherentes. Un modelo pequeño puede fallar incluso cuando recibe información correcta.
- **Ventana de contexto:** el modelo necesita recibir la información pertinente dentro del límite de contexto configurado. Un documento existente en la carpeta no garantiza que todo su contenido pueda procesarse eficazmente.
- **Recursos disponibles:** memoria, procesador y aceleración disponible condicionan qué modelos pueden ejecutarse y con qué velocidad.

**¿Qué hacer si persisten los errores?** Primero compruebe que el texto documental llega al modelo, que las instrucciones no se contradicen y que la Skill corresponde a la pregunta. Si el problema continúa, **considere la capacidad del modelo como una posible limitación**, sin atribuirle automáticamente todas las fallas. Un modelo más grande no garantiza mejores respuestas en todos los casos.

**Para comparar correctamente:** durante las mejoras mantenga el mismo modelo y la misma configuración. Si después decide ensayar otro modelo, realice una **comparación separada**, con las mismas preguntas, y registre calidad, tiempo de respuesta y recursos utilizados. **No es obligatorio cambiar de modelo ni instalar otro para completar esta sesión.**

**Idea clave:** optimizar las instrucciones y el conocimiento mejora las condiciones de respuesta, pero **no elimina las limitaciones del LLM**. El objetivo es obtener resultados comprobables, no prometer respuestas perfectas.

---

## Bloque 3 — Evaluación y documentación del trabajo (45 minutos)

**Nota:** este bloque sirve para organizar evidencias académicas. **No sustituye una pauta de evaluación institucional**, si su curso dispone de una.

### Etapa 5. Preparar evidencias (20 minutos)

**Paso 26.** Abra su bitácora en Bloc de notas, Word o el editor utilizado. Cree estos apartados: **Propósito del asistente**, **Preguntas y respuestas iniciales**, **Problemas detectados**, **Dos mejoras**, **Resultados finales** y **Conclusión**.

**Paso 27.** Incorpore las tres preguntas originales y las seis respuestas (tres antes y tres después), además de la cuarta pregunta de generalización y su resultado. Incluya la tabla de comparación del paso 24 y su valoración.

**Paso 28.** Agregue una descripción de cada intervención: nombre del componente, estado anterior, cambio realizado y justificación. **No presente únicamente una captura del botón Guardar:** documente el efecto observado.

**Paso 29.** Tome las capturas necesarias con **Windows + Shift + S**. Seleccione únicamente la región relevante; guarde las evidencias en su carpeta del taller. Oculte direcciones personales, cuentas y cualquier dato no ficticio.

**Comprobación F:** otro participante podría reconocer qué preguntas utilizó, qué modificó y cómo determinó el resultado.

### Etapa 6. Concluir y revisar la calidad de la evidencia (25 minutos)

**Paso 30.** Escriba una conclusión crítica en un párrafo: qué mejoró, qué limitaciones persisten y qué se debería probar antes de utilizar el asistente en un proceso real.

**Paso 31.** Compruebe que las afirmaciones sobre reglas académicas están respaldadas por `normativa_ejemplo.md`. Si el asistente inventó requisitos, **consérvelos como evidencia del problema**; no presente la respuesta como si fuera válida.

**Paso 32.** Verifique que las pruebas se realizaron mediante el puente Python + Ollama y que los archivos locales utilizados corresponden a la configuración evaluada. Knowledge y Skills configurados previamente en Open WebUI no se sincronizan automáticamente con `scripts/`. No afirme que probó ambas rutas si solo utilizó una.

**Paso 33.** Realice una autoevaluación: ¿diagnosticó al menos dos problemas?, ¿justificó dos intervenciones?, ¿repitió las tres preguntas originales?, ¿comparó con documentos?, ¿registró errores y limitaciones?

**Paso 34.** Guarde el documento y las capturas en la carpeta de trabajo. Si el docente solicita entrega, utilice el mecanismo y formato oficialmente indicados; esta guía **no establece una nueva fecha, rúbrica ni plataforma de evaluación**.

**Comprobación final:** dispone de evidencia para explicar no solo qué cambió, sino **si realmente mejoró y con qué límites**.

## Si aparece un problema

| Situación | Qué hacer |
|---|---|
| No se ejecuta el puente | Compruebe que Python y sus dependencias están instalados y que ejecuta el comando desde la raíz del repositorio. |
| Ollama no responde | Compruebe que Ollama está ejecutándose y que el modelo configurado está instalado. |
| El documento no se utiliza | Compruebe que exista como `.md` o `.txt` en `scripts/contexto/` y que contenga texto legible. |
| La respuesta cita una fuente pero inventa algo | Abra el documento y contraste cada afirmación. Registre el error. |
| El modelo repite el error después del cambio | Mantenga la pregunta igual; registre el resultado y revise si la intervención era pertinente. |
| Una Skill nueva no se utiliza | El selector actual solo reconoce las Skills previstas; copiar un archivo no activa automáticamente nuevas Skills. |
| El puente no reconoce `--pregunta` | Actualice `scripts/puente_local.py` desde el repositorio, preservando previamente su configuración privada. |
| No se recuperan documentos | Compruebe los archivos `.md` o `.txt` de `scripts/contexto/` y sus contenidos. |
| No puede demostrar una mejora | Describa con precisión la ausencia de cambio o el empeoramiento; también es evidencia válida. |

## 1. Comprobación final de la sesión

- [ ] Seleccioné mi asistente original, no únicamente el modelo base.
- [ ] Consulté el texto de la normativa ficticia.
- [ ] Conservé las tres preguntas y sus tres respuestas iniciales.
- [ ] Registré **dos problemas** respaldados por evidencia.
- [ ] Apliqué y guardé **dos mejoras pertinentes**.
- [ ] Repetí las **mismas tres preguntas** con la configuración final.
- [ ] Probé una **cuarta pregunta nueva** para evaluar si la mejora se mantiene ante otra consulta.
- [ ] Comparé las respuestas con la documentación, no solo con su apariencia.
- [ ] Registré resultados favorables, desfavorables e inciertos.
- [ ] Distinguí System Prompt, documentos Knowledge/contexto y Skills; comprobé el puente local Python + Ollama sin enviar correos reales.
- [ ] Documenté los cambios y la conclusión crítica.

## 2. Material complementario (opcional)

Estos recursos permiten ampliar el trabajo, pero no son necesarios para completar la práctica.

- [Laboratorio 3 — Validación y optimización](Lab03.md).
- [Manual Técnico — Capítulo 6](../vol2_manual_tecnico/cap06_mt.md): mejora continua.
- [Manual Técnico — Capítulo 10](../vol2_manual_tecnico/cap10_mt.md): evaluación.
- [Normativa ficticia ampliada](../scripts/contexto/normativa_ejemplo.md) y [versión breve original](../scripts/referencias/normativa_ejemplo_version_breve.md): actividad opcional de comparación documental.

## 3. Cierre y siguiente sesión

**Sesión 5 completada:** el resultado es una evaluación argumentada del desempeño, con mejoras documentadas y sus limitaciones, no la afirmación de que el asistente esté libre de errores.

**Continuación opcional:** consulte el [Proyecto Integrador](../vol4_proyecto_integrador/), el [Laboratorio 5](Lab05.md) y el [Laboratorio 6](Lab06.md) para consolidar y presentar la solución.
