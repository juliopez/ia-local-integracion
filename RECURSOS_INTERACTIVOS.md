# Recursos interactivos y actividades de apoyo

Esta colección transversal acompaña el aprendizaje de la IA local en distintos capítulos y laboratorios. Para cada recurso se indica dónde incorporarlo, qué observar y qué limitaciones considerar. Es complementaria a los cinco volúmenes y no sustituye las prácticas con Ollama.

Este índice complementa los capítulos del Manual del Participante y las prácticas del Cuaderno de Laboratorios. Los enlaces externos son **demostrativos** y no sustituyen el funcionamiento ni las especificaciones de los modelos ejecutados localmente.

| Recurso | Ubicación formativa | Qué observar | Precaución |
|---|---|---|---|
| [Tokenizador interactivo de OpenAI](https://platform.openai.com/tokenizer) | [Capítulo 1](vol1_manual_participante/cap01.md) y [Laboratorio 1](vol3_laboratorios/Lab01.md) | Diferencia entre palabras y tokens, fragmentación y efectos de instrucciones extensas | Los modelos de Ollama pueden usar otros tokenizadores |
| [Transformer Explainer](https://poloclub.github.io/transformer-explainer/) | [Capítulo 1, §4.3](vol1_manual_participante/cap01.md) | Tokens, contexto, atención y predicción del siguiente token | Es una representación didáctica de una arquitectura/modelo concreto |
| Comparación en Open WebUI | [Capítulo 2, §4.6](vol1_manual_participante/cap02.md) | Efectos del *System Prompt* manteniendo el modelo y la consulta | Una respuesta aislada no prueba mejoras estables |
| Casos de prueba contrastados | [Capítulo 3, §4.3](vol1_manual_participante/cap03.md) | Exactitud, información ausente y cumplimiento de restricciones | Contrastar con evidencia ficticia preparada previamente |
| Diagrama del flujo de integración | [Capítulo 4, §4.2](vol1_manual_participante/cap04.md) | Responsabilidades y recorrido de datos entre Google Workspace y Ollama | Diagrama conceptual, no guía de despliegue |

**Secuencia pedagógica:** comprender cómo se procesa el lenguaje → diseñar instrucciones → contrastar respuestas con evidencia → integrar componentes. Evite incorporar datos institucionales confidenciales o identificables en servicios demostrativos externos.


[Volver al inicio](README.md) · [Recursos del sitio](https://juliopez.github.io/ia-local-integracion/recursos.html)
