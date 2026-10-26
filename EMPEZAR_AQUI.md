# Empieza aquí · IA local e integración
**Aprendizaje paso a paso:** cinco etapas para diseñar, integrar y evaluar un asistente de IA local. Duración de referencia: 10 horas, con actividades de profundización opcionales.

> **Comience aquí.** Elija su sistema operativo, siga cada etapa en orden y compruebe el resultado antes de continuar.

## Seleccione su entorno

- **Windows 10/11 (ruta prioritaria):** [Ruta paso a paso para sesiones 1 y 2](vol3_laboratorios/Guia_Autonoma_Windows_Sesiones01_02.md). Consulte PowerShell, Python y pip en el Manual Técnico. **No ejecute comandos de Ubuntu.**
- **Ubuntu:** [Instrucciones para Ubuntu](vol3_laboratorios/Guia_Ubuntu_Sesion01_Validacion_2026.md); los pasos de interfaz de sesiones 2–5 son similares, pero la instalación y el acceso local pueden diferir.
- **macOS u otros entornos:** siga los requisitos oficiales de Ollama/Open WebUI y adapte solo la instalación; las actividades de diseño y verificación siguen siendo aplicables.
- **Equipo institucional restringido:** revise permisos y capacidades antes de instalar; pida autorización o soporte TI cuando corresponda. No desactive políticas de seguridad para completar una práctica.


## Material de consulta: cinco volúmenes

Cada etapa del itinerario combina recursos con funciones distintas. Utilice cada volumen según las necesidades de la actividad, sin necesidad de leerlos completos antes de comenzar.

| Recurso | Función en la ruta autónoma | Acceso |
|---|---|---|
| **Volumen 1 — Manual del Participante** | Conceptos y fundamentos antes de la práctica | [Capítulos y materiales](vol1_manual_participante/) |
| **Volumen 2 — Manual Técnico** | Procedimientos, comandos y capturas de pantalla | [Capítulos técnicos](vol2_manual_tecnico/) |
| **Volumen 3 — Laboratorios** | Actividades, checkpoints y evidencias | [Laboratorios](vol3_laboratorios/) |
| **Volumen 4 — Proyecto Integrador** | Documentar progresivamente el producto de cada etapa | [Manual del Proyecto Integrador](vol4_proyecto_integrador/) |
| **Volumen 5 — Manual de Referencia Técnica** | Resolver dudas sobre arquitectura y componentes | [Manual de Referencia](vol5_manual_referencia/) |

**Lecturas y recursos de las cinco sesiones:**

| Etapa | Practique aquí | Amplíe aquí | Registre aquí |
|---|---|---|---|
| **1** | [Guía Windows sesiones 1–2](vol3_laboratorios/Guia_Autonoma_Windows_Sesiones01_02.md) y [Lab01](vol3_laboratorios/Lab01.md) | [Manual Técnico cap. 4 — imágenes de instalación](vol2_manual_tecnico/cap04_mt.md); [Manual del Participante](vol1_manual_participante/) | [Proyecto Integrador](vol4_proyecto_integrador/) |
| **2** | [Guía Windows sesiones 1–2](vol3_laboratorios/Guia_Autonoma_Windows_Sesiones01_02.md) y [Lab02](vol3_laboratorios/Lab02.md) | [Manual Técnico cap. 5 — imágenes de configuración](vol2_manual_tecnico/cap05_mt.md); [Referencia Técnica](vol5_manual_referencia/) | [Proyecto Integrador](vol4_proyecto_integrador/) |
| **3** | [Guía autónoma Windows sesión 3](vol3_laboratorios/Guia_Autonoma_Sesion03_Windows.md) y [Lab04](vol3_laboratorios/Lab04.md) | [Manual Técnico cap. 7 — imágenes de Forms](vol2_manual_tecnico/cap07_mt.md); [cap. 8](vol2_manual_tecnico/cap08_mt.md); [Referencia Técnica](vol5_manual_referencia/) | [Proyecto Integrador](vol4_proyecto_integrador/) |
| **4** | [Guía Windows sesión 4](vol3_laboratorios/Guia_Autonoma_Sesion04_Windows.md) y [Lab04](vol3_laboratorios/Lab04.md) | [Manual Técnico cap. 8](vol2_manual_tecnico/cap08_mt.md); [Referencia Técnica](vol5_manual_referencia/) | [Proyecto Integrador](vol4_proyecto_integrador/) |
| **5** | [Guía Windows sesión 5](vol3_laboratorios/Guia_Autonoma_Sesion05_Windows.md) y [Lab03](vol3_laboratorios/Lab03.md) | [Manual Técnico cap. 6](vol2_manual_tecnico/cap06_mt.md) y [cap. 10](vol2_manual_tecnico/cap10_mt.md) | [Proyecto Integrador](vol4_proyecto_integrador/) |

**Apoyo visual:** consulte las capturas de pantalla disponibles en los capítulos del Manual Técnico cuando necesite identificar una opción de la interfaz.

**Sesión 5 — optimización y evaluación:** [Guía autónoma con explicación, mejoras a elegir, procedimiento y comprobación](vol3_laboratorios/Guia_Autonoma_Sesion05_Windows.md). El laboratorio conserva las tres consultas iniciales para comparar resultados antes/después. La pauta de evidencias no sustituye al instrumento institucional de evaluación.

## Cómo seguir la ruta
Cada etapa tiene **lectura → actividad → evidencia → comprobación → solución de dificultades**. Puede detenerse y volver a empezar usando sus evidencias y archivos locales. No pase a la siguiente etapa solo porque una pantalla abre: compruebe el producto esperado.

| Etapa | Qué conseguiré | Qué debo seguir, en orden | Salida verificable |
|---|---|---|---|
| **0 — Preparación** | Elegir sistema, revisar hardware y descargar materiales | Esta página → [guía de Windows](vol3_laboratorios/Guia_Autonoma_Windows_Sesiones01_02.md) (o alternativa para su SO) → [recursos de trabajo](scripts/GUIA_CONTEXTO_SKILLS.md) | Conocer SO, RAM, espacio libre, permisos y carpeta de trabajo |
| **1 — IA local** | Ejecutar un LLM en mi computador | [Ruta autónoma Windows, sesión 1](vol3_laboratorios/Guia_Autonoma_Windows_Sesiones01_02.md#sesión-1--fundamentos-instalación-y-conversación) → [Lab01](vol3_laboratorios/Lab01.md) → [Manual Técnico cap. 2](vol2_manual_tecnico/cap02_mt.md) y [cap. 4](vol2_manual_tecnico/cap04_mt.md) para detalles | Ollama lista el modelo; Open WebUI responde; comparar 2 prompts |
| **2 — Asistente** | Diseñar un asistente con contexto e instrucciones | [Ruta autónoma Windows, sesión 2](vol3_laboratorios/Guia_Autonoma_Windows_Sesiones01_02.md#sesión-2--asistente-knowledge-notes-y-skills) → [Lab02](vol3_laboratorios/Lab02.md) → [solución de problemas](vol3_laboratorios/Guia_Sesion02_Knowledge_Skills_Windows_Ubuntu.md) | Asistente guardado; Knowledge asociado y probado; Skill asociada; registro de trabajo y archivos del asistente |
| **3 — Captura de consultas** | Captar y leer una consulta sin procesarla aún | [Guía autónoma para Windows, sesión 3](vol3_laboratorios/Guia_Autonoma_Sesion03_Windows.md) → [Lab04 — captura de consultas](vol3_laboratorios/Lab04.md) → [Manual Técnico cap. 7](vol2_manual_tecnico/cap07_mt.md) y [cap. 8](vol2_manual_tecnico/cap08_mt.md) → [archivos de integración](scripts/GUIA_CONTEXTO_SKILLS.md) | Formulario vinculado a Sheets; consulta disponible en Python y registrada como **PENDIENTE** |
| **4 — Automatización** | Procesar una consulta y generar una respuesta | [Guía autónoma Windows, sesión 4](vol3_laboratorios/Guia_Autonoma_Sesion04_Windows.md) → [Lab04 — automatización de respuestas](vol3_laboratorios/Lab04.md) → [Manual Técnico cap. 8](vol2_manual_tecnico/cap08_mt.md) → [scripts](scripts/) | Consulta procesada en una prueba controlada; resultado registrado y correo de prueba enviado |
| **5 — Mejorar y evaluar** | Identificar errores y validar la solución | [Lab03](vol3_laboratorios/Lab03.md) → [Manual Técnico cap. 6](vol2_manual_tecnico/cap06_mt.md) y [cap. 10](vol2_manual_tecnico/cap10_mt.md) → [proyecto](docs/proyecto.html) | Comparación antes/después y evidencia de funcionamiento y límites del asistente |

**Tiempo:** cada etapa toma como referencia una sesión de 120 minutos. Puede distribuir el trabajo en más de una jornada según su ritmo.

## Producto de cada sesión y puntos de control

### Etapa 1 · No avance si...
- `ollama list` no muestra un modelo o no consigue generar una respuesta.
- Open WebUI no muestra el modelo o no responde.
- No ha registrado una consulta abierta y otra estructurada.
- **Cómo resolverlo:** [guía autónoma, diagnóstico](vol3_laboratorios/Guia_Autonoma_Windows_Sesiones01_02.md#qué-hacer-si-falla-diagnóstico-y-salida-autónoma). En caso de falta de permisos o de recursos del equipo, contacte al soporte que corresponda.

### Etapa 2 · No avance si...
- El modelo personalizado no quedó guardado.
- No comprobó que `normativa_ejemplo.md` permita responder «cinco días hábiles desde la publicación de la nota» y «coordinación académica».
- No importó y asoció `retroalimentacion-formativa`, o no conservó los archivos originales en `scripts/`.
- **Qué registrar, incluso si falla:** la consulta sobre **documentos adicionales obligatorios**. La normativa ficticia **no establece anexos**; si el LLM inventa alguno, consigne el error para la etapa 5 en vez de darlo por válido.

### Etapas 3–5 · Evidencia y continuidad
- **Etapa 3:** capturar y leer sin modificar el estado de la solicitud.
- **Etapa 4:** distinguir ejecución de prueba y ejecución completa; utilizar datos ficticios, revisar la bitácora y comprobar entrega.
- **Etapa 5:** probar una pregunta dentro y otra fuera del dominio; documentar limitaciones y mejoras. Si participa en una evaluación formal, siga además los criterios establecidos para su curso.

## ¿Cuándo consultar cada material?

| Material | ¿Para qué lo utilizo? |
|---|---|
| [Ruta de aprendizaje del portal](https://juliopez.github.io/ia-local-integracion/aprendizaje.html) | Orientarme y acceder rápidamente a las cinco etapas |
| [Laboratorios](vol3_laboratorios/) | Ejecutar actividades, registrar evidencia y construir productos |
| [Manual del Participante](vol1_manual_participante/) | Comprender conceptos y sentido de cada tarea |
| [Manual Técnico](vol2_manual_tecnico/) | Ejecutar procedimientos y resolver detalles de configuración |
| [Scripts](scripts/) | Conservar los archivos reproducibles; la configuración de Open WebUI no se sincroniza automáticamente con Python |
| [Laboratorios 5 y 6](vol3_laboratorios/) | Profundización opcional, no prerrequisito para terminar las cinco etapas |

## Recuperación ante errores
1. **Identifique el componente**: equipo/instalador, Ollama, Open WebUI, Knowledge/Skill, Google Workspace o puente Python.
2. **Registre evidencia concreta**: qué intentó, mensaje completo de error, sistema operativo y resultado esperado. Nunca publique contraseñas, secretos, correos privados ni tokens.
3. **Consulte la ayuda de esa etapa**, no las guías de otro SO: [Windows 1–2](vol3_laboratorios/Guia_Autonoma_Windows_Sesiones01_02.md), [Knowledge/Skills](vol3_laboratorios/Guia_Sesion02_Knowledge_Skills_Windows_Ubuntu.md) y los apartados «Problemas frecuentes» del Manual Técnico.
4. **No reinicie desde cero ni cambie cinco configuraciones a la vez**. Compruebe una hipótesis por vez. Si debe volver a crear un contenedor o instalación, conserve primero los datos.
5. **Si requiere permisos institucionales o intervención del sistema operativo**, detenga los intentos y acuda al soporte técnico. La autonomía didáctica no supone evadir restricciones administrativas.

## Evidencia final del itinerario
Al terminar, su portafolio debe contener: verificación de modelo local; asistente y prueba de Knowledge; copia local de `system_prompt.txt`, documento y `SKILL.md`; formulario y hoja de cálculo de prueba; ejecución del puente y respuesta ficticia; comparación y reflexión final. Organice cada evidencia con el nombre de la etapa, fecha y resultado.

**¿Listo para comenzar?** Si usa Windows, vaya a la [primera comprobación de la ruta autónoma](vol3_laboratorios/Guia_Autonoma_Windows_Sesiones01_02.md#antes-de-comenzar-comprobación-autónoma-windows).


## Laboratorios complementarios y continuidad de la obra

La ruta intensiva conserva los **seis laboratorios** del cuaderno original. Su secuencia de ejecución de cinco sesiones es: [Lab01](vol3_laboratorios/Lab01.md) → [Lab02](vol3_laboratorios/Lab02.md) → [Lab04, parte 1](vol3_laboratorios/Lab04.md) → [Lab04, parte 2](vol3_laboratorios/Lab04.md) → [Lab03](vol3_laboratorios/Lab03.md). Después puede ampliar la experiencia con [Lab05 — consolidación](vol3_laboratorios/Lab05.md) y [Lab06 — presentación y uso responsable](vol3_laboratorios/Lab06.md). La ruta intensiva no sustituye los contenidos de profundización.
