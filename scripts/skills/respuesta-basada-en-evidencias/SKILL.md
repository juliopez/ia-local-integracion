---
name: respuesta-basada-en-evidencias
description: >
  Utilizar cuando el usuario pregunte por normas, requisitos, plazos o
  procedimientos institucionales que deban sustentarse en documentos.
  No reemplaza la recuperación del contexto documental.
---

# Respuestas fundamentadas en evidencia documental

## Propósito

Responder preguntas institucionales **solo cuando los documentos de referencia efectivamente disponibles** permitan respaldar las afirmaciones. Si el contexto es insuficiente, explicitar el límite. Una Skill no lee por sí misma archivos ni busca en Knowledge.

## Cuándo utilizar

Cuando se soliciten reglas, plazos, requisitos, responsables o procedimientos de una institución. No es una instrucción para inventar requisitos o extrapolar desde conocimientos generales.

## Exclusión de otros procedimientos

Para consultas sobre plazos, normas, requisitos y revisión formal de evaluaciones, utilice esta Skill y no el formato de retroalimentación formativa. Una pregunta sobre revisión de calificaciones no pide evaluar un trabajo.

## Procedimiento

1. Identifique la pregunta y las afirmaciones documentales que exige.
2. Compruebe que existe texto documental relevante **dentro del contexto recibido**. No suponga que un archivo fue consultado solo porque figura asociado en una interfaz.
3. Localice el fragmento que respalda cada afirmación sustantiva. Antes de declarar insuficiencia, compruebe también apartados de preguntas frecuentes y menciones equivalentes dentro del contexto recibido.
4. Formule la respuesta sin agregar plazos, requisitos ni responsabilidades que no estén sustentados.
5. Distinga entre información no regulada (el documento indica expresamente que no la especifica) y ausencia real de evidencia. Si el documento indica que no establece un requisito, responda que no lo establece; no clasifique esa pregunta como fuera de alcance. Solo si no existe información pertinente, responda: «No encuentro antecedentes suficientes en los documentos proporcionados para confirmar esa información».
6. Identifique el nombre de archivo o sección **solo si consta realmente en el contexto**; no invente números de página, citas ni referencias.
7. Distinga lo documentado de cualquier recomendación general; ante preguntas estrictamente documentales, omita recomendaciones no solicitadas.

## Formato de respuesta

Responda directamente en una o dos frases, sin encabezados, repeticiones, apartados técnicos ni recomendaciones innecesarias. Mencione el documento solo cuando aporte claridad.

## Comprobación antes de responder

- [ ] Cada norma, plazo y obligación tiene respaldo documental identificable.
- [ ] No se presenta como obligatoria una condición ausente de las fuentes.
- [ ] No se atribuye consulta a fuentes que el modelo no recibió.
- [ ] Si el contexto no permite responder, se reconoce expresamente.

**Alcance técnico:** estas instrucciones son Markdown, no herramientas ejecutables. En Open WebUI debe estar asociada la Knowledge correspondiente y funcionar su recuperación; en el puente Python los documentos se leen de `scripts/contexto/`. No sustituye controles técnicos ni garantiza ausencia de alucinaciones.