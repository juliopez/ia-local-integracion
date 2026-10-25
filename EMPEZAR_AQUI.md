# Empieza aquí · IA local e integración
**Itinerario de autoaprendizaje del repositorio** · 5 etapas / 10 horas de práctica guiada y evaluación, con profundización opcional. **No requiere profesor presente para seguir los materiales**, aunque los bloqueos de instalación en equipos administrados pueden requerir soporte TI.

> **Si no sabe por dónde comenzar, este es el único punto de entrada.** No empiece leyendo los cinco volúmenes de forma lineal. Trabaje por etapas, siga los enlaces en orden y avance solo cuando cumpla el criterio de salida.

## Seleccione su entorno

- **Windows 10/11 (ruta prioritaria):** [Ruta paso a paso para sesiones 1 y 2](vol3_laboratorios/Guia_Autonoma_Windows_Sesiones01_02.md). Consulte PowerShell, Python y pip en el Manual Técnico. **No ejecute comandos de Ubuntu.**
- **Ubuntu:** [Validación de la sesión 1](vol3_laboratorios/Guia_Ubuntu_Sesion01_Validacion_2026.md); los pasos de interfaz de sesiones 2–5 son similares, pero la instalación y el acceso local pueden diferir.
- **macOS u otros entornos:** siga los requisitos oficiales de Ollama/Open WebUI y adapte solo la instalación; las actividades de diseño y verificación siguen siendo aplicables.
- **Equipo institucional restringido:** revise permisos y capacidades antes de instalar; pida autorización o soporte TI cuando corresponda. No desactive políticas de seguridad para completar una práctica.


## Mapa de referencias cruzadas — cinco volúmenes

Cada etapa del itinerario combina recursos con funciones distintas. **Regrese siempre a este índice para cambiar de etapa**, no lea necesariamente los cinco volúmenes de principio a fin.

| Recurso | Función en la ruta autónoma | Acceso |
|---|---|---|
| **Volumen 1 — Manual del Participante** | Conceptos y fundamentos antes de la práctica | [Capítulos y materiales](vol1_manual_participante/) |
| **Volumen 2 — Manual Técnico** | Procedimientos, comandos y **capturas de referencia conservadas** | [Capítulos técnicos](vol2_manual_tecnico/) |
| **Volumen 3 — Laboratorios** | Actividades, checkpoints y evidencias | [Laboratorios](vol3_laboratorios/) |
| **Volumen 4 — Proyecto Integrador** | Documentar progresivamente el producto de cada etapa | [Manual del Proyecto Integrador](vol4_proyecto_integrador/) |
| **Volumen 5 — Manual de Referencia Técnica** | Resolver dudas sobre arquitectura y componentes | [Manual de Referencia](vol5_manual_referencia/) |

**Correspondencia para las primeras etapas:**

| Etapa | Practique aquí | Amplíe aquí | Registre aquí |
|---|---|---|---|
| **1** | [Guía Windows sesiones 1–2](vol3_laboratorios/Guia_Autonoma_Windows_Sesiones01_02.md) y [Lab01](vol3_laboratorios/Lab01.md) | [Manual Técnico cap. 4 — imágenes de instalación](vol2_manual_tecnico/cap04_mt.md); [Manual del Participante](vol1_manual_participante/) | [Proyecto Integrador](vol4_proyecto_integrador/) |
| **2** | [Guía Windows sesiones 1–2](vol3_laboratorios/Guia_Autonoma_Windows_Sesiones01_02.md) y [Lab02](vol3_laboratorios/Lab02.md) | [Manual Técnico cap. 5 — imágenes de configuración](vol2_manual_tecnico/cap05_mt.md); [Referencia Técnica](vol5_manual_referencia/) | [Proyecto Integrador](vol4_proyecto_integrador/) |
| **3** | [Guía autónoma Windows sesión 3](vol3_laboratorios/Guia_Autonoma_Sesion03_Windows.md) y [Lab04](vol3_laboratorios/Lab04.md) | [Manual Técnico cap. 7 — imágenes de Forms](vol2_manual_tecnico/cap07_mt.md); [cap. 8](vol2_manual_tecnico/cap08_mt.md); [Referencia Técnica](vol5_manual_referencia/) | [Proyecto Integrador](vol4_proyecto_integrador/) |

**Sobre las imágenes:** están dentro de los manuales correspondientes, vinculadas a archivos originales de `images/`. Las nuevas guías no reemplazan esas imágenes; enlazan al capítulo donde se explica y representa visualmente el procedimiento.

## Cómo estudiar sin profesor
Cada etapa tiene **lectura imprescindible → actividad reproducible → evidencia → comprobación → qué hacer si falla**. Puede detenerse y volver a empezar usando sus evidencias y archivos locales. No pase a la siguiente etapa solo porque una pantalla abre: compruebe el producto esperado.

| Etapa | Qué conseguiré | Qué debo seguir, en orden | Salida verificable |
|---|---|---|---|
| **0 — Preparación** | Elegir sistema, revisar hardware y descargar materiales | Esta página → [guía de Windows](vol3_laboratorios/Guia_Autonoma_Windows_Sesiones01_02.md) (o alternativa para su SO) → [recursos de trabajo](scripts/GUIA_CONTEXTO_SKILLS.md) | Conocer SO, RAM, espacio libre, permisos y carpeta de trabajo |
| **1 — IA local** | Ejecutar un LLM en mi computador | [Ruta autónoma Windows, sesión 1](vol3_laboratorios/Guia_Autonoma_Windows_Sesiones01_02.md#sesión-1--fundamentos-instalación-y-conversación) → [Lab01](vol3_laboratorios/Lab01.md) → [Manual Técnico cap. 2](vol2_manual_tecnico/cap02_mt.md) y [cap. 4](vol2_manual_tecnico/cap04_mt.md) para detalles | Ollama lista el modelo; Open WebUI responde; comparar 2 prompts |
| **2 — Asistente** | Diseñar un asistente con contexto e instrucciones | [Ruta autónoma Windows, sesión 2](vol3_laboratorios/Guia_Autonoma_Windows_Sesiones01_02.md#sesión-2--asistente-knowledge-notes-y-skills) → [Lab02](vol3_laboratorios/Lab02.md) → [incidencias comprobadas](vol3_laboratorios/Guia_Sesion02_Knowledge_Skills_Windows_Ubuntu.md) | Asistente guardado; Knowledge asociado y probado; Skill asociada; bitácora y tres archivos locales |
| **3 — Captura de consultas** | Captar y leer una consulta sin procesarla aún | [Guía autónoma para Windows, sesión 3](vol3_laboratorios/Guia_Autonoma_Sesion03_Windows.md) → [Lab04, primera etapa](vol3_laboratorios/Lab04.md) → [Manual Técnico cap. 7](vol2_manual_tecnico/cap07_mt.md) y [cap. 8](vol2_manual_tecnico/cap08_mt.md) → [archivos del puente](scripts/GUIA_CONTEXTO_SKILLS.md) | Forms → Sheets → Apps Script → Python lectura; fila sigue **PENDIENTE** |
| **4 — Automatización** | Procesar una consulta y generar una respuesta | [Lab04, segunda etapa](vol3_laboratorios/Lab04.md) → [Manual Técnico cap. 8](vol2_manual_tecnico/cap08_mt.md) → [scripts](scripts/) | `--modo prueba` funciona localmente; `--modo completo --una-vez` actualiza estado y entrega correo en un ensayo ficticio |
| **5 — Mejorar y evaluar** | Identificar errores y validar la solución | [Lab03](vol3_laboratorios/Lab03.md) → [Manual Técnico cap. 6](vol2_manual_tecnico/cap06_mt.md) y [cap. 10](vol2_manual_tecnico/cap10_mt.md) → [proyecto](docs/proyecto.html) | Comparación antes/después y evidencia de funcionamiento y límites del asistente |

**Tiempo:** cada sesión del taller equivale a 120 minutos, pero quien estudia por cuenta propia puede invertir más. Los tiempos intensivos sirven de orientación, **no son un límite de estudio**.

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
- **Etapa 5:** probar una pregunta dentro y otra fuera del dominio; documentar limitaciones y mejoras. El examen académico con calificación corresponde al contexto del taller dirigido y no impide estudiar autónomamente.

## Materiales y su función: no son itinerarios competidores

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
