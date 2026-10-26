# Sesión 5 · Mejorar, comprobar y evaluar un asistente de IA local

**Guía autónoma, con prioridad para Windows · 120 minutos.** Continúe con el asistente creado en [sesiones 1–2](Guia_Autonoma_Windows_Sesiones01_02.md) y, si corresponde, el flujo automatizado de [sesiones 3](Guia_Autonoma_Sesion03_Windows.md) y [4](Guia_Autonoma_Sesion04_Windows.md).

**Ruta:** [EMPEZAR AQUÍ](../EMPEZAR_AQUI.md) · [Laboratorio 3](Lab03.md) · [Manual Técnico cap. 6](../vol2_manual_tecnico/cap06_mt.md) y [cap. 10](../vol2_manual_tecnico/cap10_mt.md) · [Proyecto Integrador](../vol4_proyecto_integrador/) · [Referencia Técnica](../vol5_manual_referencia/).

## Qué logrará

Revisará críticamente las respuestas de **su propio asistente**, elegirá las mejoras que necesita, las aplicará en Open WebUI y comprobará si realmente mejoraron los resultados. **No necesita instalar ni descargar otro modelo.** Si ya realizó alguna mejora en sesiones anteriores, elija otras pertinentes; no repita cambios solo para cumplir una lista.

| Bloque | Tiempo | Producto |
|---|---:|---|
| Introducción: por qué evaluar | 15 min | Criterios de calidad comprendidos |
| Laboratorio de optimización | **60 min** | Diagnóstico, intervenciones y comparación |
| Evaluación final | **45 min** | Evidencias y valoración argumentada |

> **Importante:** la evaluación mide la calidad del diagnóstico, la justificación, la implementación y la comprobación; no exige que el modelo responda perfectamente. Trabaje con preguntas y normativa **ficticias**. No introduzca datos reales de estudiantes ni active el envío de correos al probar respuestas en Open WebUI.

## A. Breve explicación inicial (15 min)

**¿Por qué optimizar?** Un modelo puede contestar correctamente una pregunta explícita y, ante otra más abierta, inventar requisitos. Que Open WebUI muestre una fuente no garantiza que **todas** las afirmaciones estén respaldadas por ella. Una instrucción añadida tampoco garantiza una mejora consistente.

**Qué observar:** (1) precisión factual; (2) fidelidad a las fuentes; (3) reconocimiento de información ausente; (4) pertinencia; (5) claridad; (6) aplicación de las habilidades o formato requerido.

**Regla del experimento:** conserve la pregunta original, guarde la respuesta y cambie **un componente por vez** cuando sea posible. No confunda una respuesta más larga con una respuesta mejor.

### Qué es una alucinación en un modelo de lenguaje

Una **alucinación** es una respuesta que presenta información inventada, incorrecta o no respaldada como si fuera válida. Puede parecer convincente e incluso citar un archivo, pero la cita no prueba que el contenido esté realmente en esa fuente.

**Ejemplo del taller:** cuando el documento no exige certificados para revisar una evaluación, el asistente puede afirmar que «debe presentar una identificación oficial». Ese requisito es una alucinación **normativa**: convierte información inexistente en una obligación. Una recomendación general como «puede consultar al docente» no constituye por sí sola una alucinación si se identifica claramente como consejo, y no como norma obligatoria.

**Por qué ocurre:** el modelo genera texto probable y no verifica automáticamente cada afirmación; influyen la formulación de la consulta, el contenido recuperado, la calidad y suficiencia de la fuente, las instrucciones y los límites del modelo. **Un documento escaso puede reducir la utilidad de las respuestas, pero no autoriza inventar lo que falta.**

**Cómo detectarla y reducir su impacto, paso a paso:**

1. Localice en la respuesta toda afirmación sobre plazos, requisitos, responsables, procedimientos o resultados garantizados.
2. Abra la fuente citada y compruebe si **cada afirmación importante** aparece explícitamente allí.
3. Clasifique: **respaldada / recomendación general / no documentada o contradictoria**.
4. Si falta información, registre el error y mejore el documento, las instrucciones o la forma de presentar incertidumbre, según corresponda.
5. Repita **la misma pregunta original** y compare; incluya otra consulta no documentada para comprobar que el modelo sigue reconociendo límites.

**No confunda corrección de una respuesta con eliminación de alucinaciones:** una sola prueba favorable no demuestra fiabilidad general.

### Ejercicio opcional: fuente breve frente a fuente ampliada

El repositorio incluye la [versión breve original](../scripts/referencias/normativa_ejemplo_version_breve.md) y la [normativa ficticia ampliada](../scripts/contexto/normativa_ejemplo.md). Si su problema es la insuficiencia del contexto, puede comparar ambas **sin cambiar el modelo ni el System Prompt**:

1. Guarde la pregunta y la respuesta utilizando su documento actual.
2. Descargue la versión ampliada desde GitHub y asóciela al asistente en **Conocimiento**, evitando conservar simultáneamente dos versiones contradictorias de la misma fuente.
3. Abra otra conversación y repita exactamente la pregunta.
4. Verifique qué afirmaciones están documentadas, cuáles son recomendaciones y cuáles son invenciones.

**Nota:** esta comparación cambia deliberadamente el *contenido documental*; si también modifica el prompt, ya no podrá atribuir con claridad la diferencia a la ampliación del documento. La versión actualizada del repositorio **no reemplaza automáticamente** el archivo o conocimiento ya cargado en Open WebUI, ni la copia local instalada en cada equipo.

## B. Laboratorio de optimización (60 min)

### Paso 1 · Diagnosticar su asistente (10 min)

1. Abra Open WebUI y seleccione **su asistente existente**.
2. Prepare tres preguntas acordes con su propósito:
   - **Información disponible:** una respuesta explícita en su documento de contexto.
   - **Información ausente:** una pregunta cuya respuesta **no esté establecida** en sus fuentes.
   - **Orientación abierta:** una pregunta donde se espere ayuda pertinente, sin inventar normas.
3. Realice cada pregunta en una **conversación nueva**. Guarde las respuestas iniciales y, cuando corresponda, la fuente mostrada.
4. Identifique **dos problemas concretos**. Ejemplos: datos inventados, respuestas vagas, citas defectuosas, formato poco útil, falta de referencia al contexto, Skill no aplicada.

**Comprobación:** tiene las tres preguntas exactas, tres respuestas de partida y al menos dos observaciones fundamentadas.

### Paso 2 · Seleccionar mejoras (15 min)

**¿Qué puede mejorar?** Revise esta tabla. Seleccione **al menos dos intervenciones pertinentes y factibles**, preferiblemente en componentes distintos. Las mejoras ya incorporadas previamente no se tienen que repetir.

| Área | Para qué sirve | Cómo intervenir en esta sesión |
|---|---|---|
| **System Prompt** | Fijar función, límites y criterios de respuesta | Edite las instrucciones del asistente; indique qué hacer cuando falta información |
| **Conocimiento** | Proveer hechos comprobables | Verifique asociación de documentos; corrija ambigüedades, errores o contenido innecesario en **copias autorizadas**, y vuelva a cargar si corresponde |
| **Uso de fuentes** | Evitar citas que no respaldan afirmaciones | Pida distinguir hechos documentados de recomendaciones generales y compruébelo en las respuestas |
| **Skill** | Orientar un procedimiento o formato específico | Revise que esté asociada; ajuste instrucciones en su contenido editable o copia de trabajo y compruebe si se aplica |
| **Estructura de respuesta** | Hacer la orientación más comprensible | Defina brevedad, pasos, distinción entre norma y sugerencia, lenguaje claro |
| **Reconocimiento de límites** | Reducir invenciones | Indique que debe declarar cuándo un requisito no figura en las fuentes |
| **Parámetros** | Explorar variaciones de generación | Si está disponible, registre el valor anterior de temperatura; cambie un parámetro y pruebe |
| **Diseño de consultas** | Obtener entradas menos ambiguas | Reformule una consulta **adicional** para diagnóstico, pero mantenga las tres originales para comparar el asistente |
| **Asociación de recursos** | Garantizar disponibilidad de documentos y habilidades | Compruebe en la configuración del modelo «Conocimiento» y «Habilidades»; no confunda contadores globales con recursos asociados |
| **Pruebas sistemáticas** | Comprobar consistencia | Repita exactamente los casos y evalúe también las respuestas incorrectas |

**Comprobación:** para cada mejora seleccionada puede explicar el problema que aborda y qué resultado espera observar.

### Paso 3 · Implementar mejoras (25 min)

Trabaje en la configuración de **su propio asistente** en Open WebUI:

1. **Registre o copie el estado original** (instrucciones, recursos y parámetros que piensa cambiar).
2. **Aplique la primera mejora** escogida. Guarde y compruebe la configuración.
3. Formule la pregunta relacionada en una **conversación nueva**. Registre la salida y compare con la respuesta original.
4. **Aplique la segunda mejora** y repita la comprobación. Si ambas mejoras inciden sobre la misma consulta, anote qué cambió entre cada prueba.
5. Si una intervención empeora la respuesta, **registre el resultado** y explique si decide revertirla o conservarla para una prueba adicional.

**Precauciones:** una Skill asociada no demuestra por sí sola que fue ejecutada. La información presentada como fuente puede contener afirmaciones no respaldadas. El System Prompt de Open WebUI **no se sincroniza automáticamente** con `scripts/system_prompt.txt`: registre las mejoras aceptadas para replicarlas más adelante en el puente Python. No modifique Google Sheets ni Gmail en esta actividad.

**Comprobación:** mantiene al menos dos intervenciones con registro del antes y del después, incluyendo resultados no satisfactorios.

### Paso 4 · Verificar y concluir (10 min)

1. Repita **las mismas tres preguntas originales** (preferiblemente cada una en conversación nueva).
2. Compare los resultados mediante la pauta siguiente.
3. Clasifique cada intervención: **mejoró / no cambió / empeoró / resultado incierto**.
4. Escriba una conclusión breve: ¿qué mejoró?, ¿qué problema persiste?, ¿qué podría revisar después?

| Caso | Exactitud | Fuente o límites | Pertinencia | Cambio observado |
|---|---|---|---|---|
| 1 · Dato documentado | Antes → después | Antes → después | Antes → después | |
| 2 · Información ausente | Antes → después | Antes → después | Antes → después | |
| 3 · Orientación abierta | Antes → después | Antes → después | Antes → después | |

**Comprobación:** tiene evidencia comparativa. Una respuesta correcta obtenida por anticipar la solución en la pregunta **no sustituye** la prueba con el enunciado original.

## C. Evaluación final (45 min)

La evaluación comienza **después** del laboratorio de mejora. El instrumento institucional específico puede establecer exigencias adicionales; la siguiente pauta es una estructura de evidencia para preparar y valorar el trabajo, **no una rúbrica institucional aprobada**.

1. **10 min — Organice evidencias:** tres preguntas originales y resultados iniciales; capturas o transcripciones sin información personal.
2. **15 min — Describa las intervenciones:** al menos dos problemas, dos mejoras, sus configuraciones inicial y final, y por qué las seleccionó.
3. **10 min — Contraste resultados:** respuestas finales para las mismas tres preguntas y explicación de cambios y errores persistentes.
4. **10 min — Concluya y entregue:** valoración crítica sobre precisión, fuentes, limitaciones y utilidad del asistente; incorpore al [Proyecto Integrador](../vol4_proyecto_integrador/), según las instrucciones de su curso.

**Criterios sugeridos para la revisión docente:** diagnóstico fundamentado, pertinencia de las intervenciones, reproducibilidad y evidencia de comparación, y juicio crítico sobre resultados. No se califica como éxito automático modificar un prompt o mostrar una cita: hay que demostrar qué pasó.

### Plantilla breve para el registro individual

| Campo | Qué registrar |
|---|---|
| Propósito del asistente | A quién ayuda y para qué |
| Tres preguntas iniciales | Copia literal de cada consulta |
| Problemas encontrados | Dos observaciones con evidencia |
| Mejoras implementadas | Componente, valor antes/después y justificación |
| Resultados | Comparación usando las mismas preguntas |
| Conclusión | Mejoras, limitaciones y acciones futuras |

## Ejemplo didáctico (no copiar como respuesta propia)

En un asistente académico con normativa ficticia, la pregunta «¿qué documentos adicionales son obligatorios para revisar una evaluación?» produjo requisitos inventados, pese a mostrar el archivo de normativa como fuente. Una pregunta mucho más restrictiva obtuvo la respuesta correcta. **Eso indica que la formulación puede afectar el resultado, pero no demuestra que el asistente haya mejorado para consultas reales abiertas.**

## Cierre de la jornada

Al finalizar, usted debería poder **diagnosticar, ajustar, comprobar y comunicar** el desempeño de un asistente local, distinguiendo una mejora verificada de una mejora supuesta. Si usa el puente Python de la sesión 4, recuerde que sus instrucciones y documentos locales son independientes de la configuración de Open WebUI.

**Estado de esta guía:** secuencia didáctica preparada a partir de las pruebas realizadas en Ubuntu. Las optimizaciones demostraron resultados mixtos; la actividad completa de 60 + 45 minutos todavía requiere aplicación con participantes y definición institucional del instrumento evaluativo final.
