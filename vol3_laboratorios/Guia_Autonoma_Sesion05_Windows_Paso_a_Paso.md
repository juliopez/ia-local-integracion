# Sesión 5 — Mejorar y evaluar un asistente de IA local
## Guía autónoma paso a paso · Windows 10/11 · 120 minutos

**Objetivo:** identificar problemas reales en las respuestas de su asistente, aplicar **al menos dos mejoras justificadas**, repetir las mismas preguntas y comparar los resultados con evidencia. No necesita instalar otro modelo.

**Antes de comenzar:** tenga funcionando Ollama y Open WebUI, y conserve el **Asistente Académico de Apoyo** creado en la [sesión 2](Guia_Autonoma_Sesion02_Windows_Paso_a_Paso.md), junto con `normativa_ejemplo.md` y su bitácora. Para esta actividad utilice **Open WebUI**, no el envío automatizado de correos de la sesión 4.

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

**Paso 1.** En Windows, presione la tecla **Windows**, escriba **Ollama** y ábralo si no está ejecutándose. Abra también **Open WebUI** desde Inicio.

**Paso 2.** Abra Chrome o Edge, escriba `http://localhost:8080` en la barra de direcciones y presione **Enter**. Si Open WebUI Desktop utiliza otro puerto, consulte el indicado en la aplicación. Inicie sesión si se solicita.

**Paso 3.** Abra **Espacio de trabajo → Modelos** y confirme que sigue disponible **Asistente Académico de Apoyo**. Compruebe que conserva el documento ficticio de Knowledge. No cambie aún el System Prompt ni los archivos.

**Paso 4.** Abra la carpeta del repositorio de la sesión 2 en el **Explorador de archivos** (teclas **Windows + E**). Localice `scripts/contexto/normativa_ejemplo.md`, haga clic derecho → **Abrir con → Bloc de notas** y léalo. Anote qué plazos o requisitos establece y qué asuntos **no** regula.

**Paso 5.** Abra su bitácora de la sesión 2. Escriba como objetivo de hoy: «Evaluar el asistente con tres preguntas, implementar dos mejoras y comparar las respuestas antes y después». Guarde el documento.

**Comprobación A:** puede abrir el asistente y el texto normativo. Comprende que una respuesta bien redactada puede contener información inventada.

## Bloque 2 — Diagnosticar y mejorar el asistente (60 minutos)

### Etapa 1. Registrar tres respuestas iniciales (15 minutos)

**Paso 6.** Abra una **conversación nueva** en Open WebUI y seleccione **Asistente Académico de Apoyo**, no solo el modelo base de Ollama.

**Paso 7.** Copie y envíe esta pregunta, basada en información del ejercicio:

> Según la normativa de ejemplo, ¿cuántos días hábiles tengo para solicitar la revisión de una evaluación y a quién debo dirigir la solicitud?

**Paso 8.** Guarde la respuesta íntegra en su bitácora bajo el título **Caso 1 — Antes**. Compare con la normativa ficticia; la referencia utilizada en el taller establece **cinco días hábiles desde la publicación de la nota** y **coordinación académica**. Si hay una cita o una indicación de fuente, ábrala y compruebe que respalda el contenido.

**Paso 9.** Abra otra **conversación nueva** con el mismo asistente y envíe:

> ¿Qué documentos adicionales son obligatorios para solicitar la revisión de una evaluación?

**Paso 10.** Copie la respuesta como **Caso 2 — Antes**. Compruebe si afirma la existencia de certificados, aranceles o anexos que **no aparecen** en el documento. En ese caso, anote «requisito no respaldado», no «respuesta correcta».

**Paso 11.** Inicie una tercera conversación nueva y pregunte:

> Soy estudiante y no entiendo cómo solicitar la revisión de una evaluación. ¿Puedes orientarme con pasos claros, distinguiendo los requisitos documentados de las recomendaciones generales?

**Paso 12.** Guarde la respuesta como **Caso 3 — Antes**. Observe si el asistente diferencia reglas documentadas, consejos generales e información que no conoce.

**Comprobación B:** tiene **tres preguntas literales**, tres respuestas originales y notas sobre exactitud, claridad y respaldo documental. Conserve exactamente las mismas preguntas para el resto de la práctica.

### Etapa 2. Elegir y justificar dos mejoras (10 minutos)

**Paso 13.** Revise las tres respuestas y anote **al menos dos problemas concretos**. Ejemplos: inventar un requisito, no reconocer límites, contestar sin consultar la fuente, entregar una respuesta confusa.

**Paso 14.** Para cada problema elija **una intervención**: ajustar el **System Prompt**, revisar la asociación de **Knowledge**, corregir una copia autorizada de la normativa ficticia, mejorar la estructura de respuesta o comprobar la **Skill** asociada. No modifique todo simultáneamente.

**Paso 15.** Complete esta tabla en su bitácora:

| Problema observado | Componente que modificaré | Cambio previsto | Resultado que espero |
|---|---|---|---|
| [Escriba un problema real] | [System Prompt/Knowledge/etc.] | [Una modificación concreta] | [Un resultado comprobable] |
| [Escriba otro problema] | [Componente] | [Segunda modificación] | [Un resultado comprobable] |

**Comprobación C:** puede explicar por qué cada cambio está relacionado con una dificultad observada. No se exige cambiar una Skill solo para completar una lista.

### Etapa 3. Aplicar las mejoras y guardar versiones (25 minutos)

**Paso 16.** Vuelva a **Espacio de trabajo → Modelos → Asistente Académico de Apoyo → Editar**. **Antes de cambiar nada**, copie el texto actual del System Prompt a su bitácora o a un archivo de respaldo; registre también los documentos asociados y, si modifica parámetros, sus valores originales.

**Paso 17.** Aplique **solo la primera mejora** seleccionada. Ejemplo, si el problema es inventar obligaciones, agregue en el System Prompt una instrucción específica:

> Cuando el usuario pregunte por un requisito obligatorio, menciona solamente los que estén expresamente indicados en el documento disponible. Si no hay información suficiente, dilo claramente y no inventes requisitos.

Este texto es **un ejemplo**: adáptelo al problema real diagnosticado, sin alterar la normativa original.

**Paso 18.** Haga clic en **Guardar y Actualizar** (o el botón equivalente de su versión). Vuelva a editar el asistente y compruebe que se conservó el cambio.

**Paso 19.** Abra una **conversación nueva**, seleccione el asistente y repita **la pregunta original relacionada con la primera mejora**, exactamente con el mismo texto del paso 7, 9 u 11. Copie el resultado como **Después de mejora 1** y contraste con la fuente.

**Paso 20.** Aplique **la segunda mejora**, relacionada con el otro problema. Por ejemplo, verifique el documento que está asociado en **Conocimiento/Knowledge** y vuelva a guardarlo si la asociación faltaba, o ajuste una instrucción de formato. Si modifica el documento, trabaje sobre una copia autorizada y evite mantener dos versiones contradictorias.

**Paso 21.** Haga clic en **Guardar y Actualizar**. Compruebe el cambio y registre exactamente qué se modificó. Si toca la Skill, verifique tanto su disponibilidad como su **asociación** al asistente; una Skill visible no prueba que haya sido utilizada efectivamente.

**Paso 22.** Inicie un chat nuevo y repita **la pregunta original relacionada con la segunda mejora**. Guarde el resultado como **Después de mejora 2**. Indique si mejoró, empeoró o no cambió. Si el resultado es peor, documente la posibilidad de revertir el cambio, pero no oculte la evidencia.

**Comprobación D:** tiene dos cambios identificados y guardados, sus configuraciones anteriores y posteriores, y al menos una prueba por intervención. Cuando sea posible, modifique **una variable por vez**.

### Etapa 4. Comparar resultados con las mismas preguntas (10 minutos)

**Paso 23.** Con la configuración final del asistente, abra **tres conversaciones nuevas** (una por cada pregunta). Repita exactamente las preguntas de los pasos **7, 9 y 11**, sin agregar pistas o respuestas esperadas en los mensajes.

**Paso 24.** Copie las tres respuestas finales y complete:

| Caso | Resultado antes | Resultado después | Evidencia que lo respalda | Evaluación |
|---|---|---|---|---|
| 1. Plazo y responsable | [Resumen] | [Resumen] | [Texto/fuente] | Mejoró / igual / empeoró |
| 2. Requisitos no especificados | [Resumen] | [Resumen] | [Texto/fuente] | Mejoró / igual / empeoró |
| 3. Orientación al estudiante | [Resumen] | [Resumen] | [Texto/fuente] | Mejoró / igual / empeoró |

**Paso 25.** Escriba dos o tres frases: ¿qué problema se redujo?, ¿qué problema continúa?, ¿qué evidencia respalda su conclusión? **Una única respuesta correcta no demuestra fiabilidad general.**

**Comprobación E:** compara tres casos antes y después con la **misma redacción** y distingue observaciones de suposiciones.

## Bloque 3 — Evaluación y documentación del trabajo (45 minutos)

**Nota:** este bloque sirve para organizar evidencias académicas. **No sustituye una pauta de evaluación institucional**, si su curso dispone de una.

### Etapa 5. Preparar evidencias (20 minutos)

**Paso 26.** Abra su bitácora en Bloc de notas, Word o el editor utilizado. Cree estos apartados: **Propósito del asistente**, **Preguntas y respuestas iniciales**, **Problemas detectados**, **Dos mejoras**, **Resultados finales** y **Conclusión**.

**Paso 27.** Incorpore las tres preguntas originales y las seis respuestas (tres antes y tres después). Incluya la tabla de comparación del paso 24 y su valoración.

**Paso 28.** Agregue una descripción de cada intervención: nombre del componente, estado anterior, cambio realizado y justificación. **No presente únicamente una captura del botón Guardar:** documente el efecto observado.

**Paso 29.** Tome las capturas necesarias con **Windows + Shift + S**. Seleccione únicamente la región relevante; guarde las evidencias en su carpeta del taller. Oculte direcciones personales, cuentas y cualquier dato no ficticio.

**Comprobación F:** otro participante podría reconocer qué preguntas utilizó, qué modificó y cómo determinó el resultado.

### Etapa 6. Concluir y revisar la calidad de la evidencia (25 minutos)

**Paso 30.** Escriba una conclusión crítica en un párrafo: qué mejoró, qué limitaciones persisten y qué se debería probar antes de utilizar el asistente en un proceso real.

**Paso 31.** Compruebe que las afirmaciones sobre reglas académicas están respaldadas por `normativa_ejemplo.md`. Si el asistente inventó requisitos, **consérvelos como evidencia del problema**; no presente la respuesta como si fuera válida.

**Paso 32.** Verifique que no mezcló cambios de Open WebUI con los archivos locales de Python. **Knowledge, Notes y Skills configurados en Open WebUI no se sincronizan automáticamente con `scripts/`**. Si decide llevar mejoras al puente, debe planificar una actualización local independiente.

**Paso 33.** Realice una autoevaluación: ¿diagnosticó al menos dos problemas?, ¿justificó dos intervenciones?, ¿repitió las tres preguntas originales?, ¿comparó con documentos?, ¿registró errores y limitaciones?

**Paso 34.** Guarde el documento y las capturas en la carpeta de trabajo. Si el docente solicita entrega, utilice el mecanismo y formato oficialmente indicados; esta guía **no establece una nueva fecha, rúbrica ni plataforma de evaluación**.

**Comprobación final:** dispone de evidencia para explicar no solo qué cambió, sino **si realmente mejoró y con qué límites**.

## Si aparece un problema

| Situación | Qué hacer |
|---|---|
| Open WebUI no abre | Compruebe que la aplicación está iniciada y verifique el puerto local indicado. |
| No aparece el asistente | Entre a **Espacio de trabajo → Modelos** y confirme el nombre y la cuenta local. |
| El documento no aparece | Revise la asociación en **Knowledge** y guarde los cambios. |
| La respuesta cita una fuente pero inventa algo | Abra el documento y contraste cada afirmación. Registre el error. |
| El modelo repite el error después del cambio | Mantenga la pregunta igual; registre el resultado y revise si la intervención era pertinente. |
| Una Skill está importada pero no asociada | Verifique la asociación al asistente y guarde. No dé por probada su aplicación. |
| No puede demostrar una mejora | Describa con precisión la ausencia de cambio o el empeoramiento; también es evidencia válida. |

## 1. Comprobación final de la sesión

- [ ] Seleccioné mi asistente original, no únicamente el modelo base.
- [ ] Consulté el texto de la normativa ficticia.
- [ ] Conservé las tres preguntas y sus tres respuestas iniciales.
- [ ] Registré **dos problemas** respaldados por evidencia.
- [ ] Apliqué y guardé **dos mejoras pertinentes**.
- [ ] Repetí las **mismas tres preguntas** con la configuración final.
- [ ] Comparé las respuestas con la documentación, no solo con su apariencia.
- [ ] Registré resultados favorables, desfavorables e inciertos.
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
