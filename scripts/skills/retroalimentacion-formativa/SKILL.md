---
name: retroalimentacion-formativa
description: Procedimiento didáctico para analizar trabajos académicos ficticios y entregar retroalimentación basada en evidencias, con fortalezas, mejoras y próximos pasos.
---

# Retroalimentación formativa

## Propósito

Orientar la mejora de un desempeño o producto académico mediante observaciones concretas, respetuosas y verificables. Esta habilidad complementa las instrucciones generales del asistente (**System Prompt**) y los documentos de referencia (**Knowledge**); no los sustituye.

## Cuándo utilizar

Utilice este procedimiento cuando el usuario solicite **retroalimentación sobre un trabajo, respuesta, explicación, actividad o desempeño**, y proporcione suficiente material para analizarlo.

**No lo aplique automáticamente** a preguntas administrativas sobre plazos, requisitos, matrícula o procedimientos. Para esas consultas, responda con la normativa disponible y reconozca lo que no esté documentado.

Si el usuario solicita retroalimentación pero no comparte el trabajo o criterios necesarios, pida únicamente el antecedente imprescindible. No simule haber revisado material inexistente.

## Procedimiento

1. **Identificar la tarea:** determine qué producto o desempeño se evalúa, su propósito y los criterios proporcionados por el usuario. No invente una rúbrica.
2. **Examinar evidencias:** identifique fragmentos o características observables del material entregado. Distinga observación de interpretación.
3. **Reconocer fortalezas:** señale una o dos decisiones logradas y explique **por qué** son pertinentes, utilizando evidencia disponible.
4. **Identificar oportunidades de mejora:** seleccione uno o dos aspectos prioritarios, describa la dificultad y su efecto sobre el trabajo. Evite juicios personales sobre el estudiante.
5. **Recomendar acciones realizables:** proponga cambios específicos que el estudiante pueda ejecutar y verificar; priorice el siguiente paso.
6. **Reconocer límites:** si falta información o un criterio no puede comprobarse, declárelo. Sustente las afirmaciones institucionales únicamente en el contexto documental proporcionado. No invente normas, plazos, calificaciones ni datos personales.
7. **Comprobar coherencia:** asegure que cada fortaleza y recomendación esté relacionada con una evidencia o un criterio conocido; no prometa que un cambio garantiza una determinada nota.

## Formato de respuesta

Adapte la extensión a la solicitud. Cuando exista evidencia suficiente, utilice esta estructura:

**Fortaleza identificada:** [observación concreta y evidencia].

**Aspecto por mejorar:** [dificultad prioritaria y por qué importa].

**Recomendación concreta:** [acción específica y realizable].

**Siguiente paso:** [qué modificar o probar y cómo comprobar la mejora].

Si el trabajo cumple adecuadamente los criterios, no invente debilidades para completar el formato. Si no hay evidencia para alguna sección, indíquelo brevemente.

## Ejemplo didáctico (trabajo ficticio)

**Solicitud:** «Retroalimenta esta explicación: “Ollama permite ejecutar un modelo local sin enviar cada consulta a un proveedor remoto”. El objetivo es explicar las ventajas y limitaciones de la IA local».

**Fortaleza identificada:** la explicación reconoce correctamente la ejecución local y distingue esa modalidad de la consulta a un servicio remoto.

**Aspecto por mejorar:** no aborda las limitaciones de hardware, que forman parte del objetivo indicado.

**Recomendación concreta:** agregue una oración sobre memoria RAM, capacidad de procesamiento y cómo estos recursos condicionan qué modelos pueden utilizarse.

**Siguiente paso:** revise la explicación y compruebe que presenta al menos una ventaja y una limitación explícitas, sin afirmar que todo uso de herramientas locales garantiza privacidad absoluta.

## Criterios de comprobación

Antes de entregar la respuesta, verifique:

- [ ] La retroalimentación se refiere al **trabajo realmente proporcionado**.
- [ ] Las fortalezas y las mejoras se sustentan en **evidencia observable**.
- [ ] Las recomendaciones son **específicas, viables y pertinentes**.
- [ ] Se distinguen hechos documentados, inferencias y límites de información.
- [ ] No se inventan criterios institucionales, calificaciones, normas ni requisitos.
- [ ] El tono es respetuoso y orientado al aprendizaje.

**Alcance técnico:** esta Skill contiene instrucciones de texto. No ejecuta código, no lee automáticamente archivos externos y no envía mensajes ni modifica sistemas. Su importación o asociación al asistente no demuestra por sí sola que haya sido aplicada correctamente.
