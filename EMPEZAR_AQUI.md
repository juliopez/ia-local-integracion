# Empieza aquí · IA local e integración

**Cinco sesiones de 120 minutos · 10 horas.** Este itinerario permite aprender a ejecutar un modelo local, diseñar un asistente, conectar Google Workspace y evaluar sus resultados.

**Si es su primera vez:** comience por la **guía paso a paso de la sesión 1**. Cada guía indica dónde ingresar, qué hacer, qué escribir y qué comprobar. **No necesita leer los cinco volúmenes antes de comenzar.** Las lecturas técnicas son materiales de apoyo, no requisitos para encontrar instrucciones esenciales.

[**Abrir la ruta visual en GitHub Pages**](https://juliopez.github.io/ia-local-integracion/aprendizaje.html)

## 1. Elija su sistema operativo

| Entorno | Cómo comenzar | Alcance |
|---|---|---|
| **Windows 10/11** | [Sesión 1 — instalación paso a paso](vol3_laboratorios/Guia_Autonoma_Sesion01_Windows_Paso_a_Paso.md) | Ruta operativa principal de las cinco sesiones. |
| **Ubuntu** | [Instalación, validación e incidencias — sesión 1](vol3_laboratorios/Guia_Ubuntu_Sesion01_Validacion_2026.md) · [Knowledge y Skills — sesión 2](vol3_laboratorios/Guia_Sesion02_Knowledge_Skills_Windows_Ubuntu.md) | Documentación específica y complementaria; los procedimientos Windows de sesiones posteriores requieren adaptar comandos y rutas. |
| **macOS u otros** | [Manual Técnico](vol2_manual_tecnico/) y documentación oficial de las herramientas | La obra aporta conceptos y actividades, pero no una guía autónoma verificada para todos los sistemas. |

En equipos institucionales, compruebe los permisos antes de instalar programas. No desactive antivirus ni controles administrativos. **No utilice datos reales o personales** en los ejercicios de integración.

## 2. Siga las cinco sesiones en orden

La columna **Guía paso a paso** es el punto de entrada de cada jornada. Los laboratorios y capítulos técnicos permiten profundizar cuando lo necesite.

| Sesión y objetivo | Guía paso a paso — empezar aquí | Laboratorio original | Manual Técnico de apoyo | Resultado verificable |
|---|---|---|---|---|
| **1 · Entorno de IA local** | [Sesión 1 — LLMFit, Ollama y Open WebUI](vol3_laboratorios/Guia_Autonoma_Sesion01_Windows_Paso_a_Paso.md) | [Lab01](vol3_laboratorios/Lab01.md) | [Cap. 1](vol2_manual_tecnico/cap01_mt.md), [2](vol2_manual_tecnico/cap02_mt.md), [3](vol2_manual_tecnico/cap03_mt.md) y [4](vol2_manual_tecnico/cap04_mt.md) | Modelo descargado; conversación en PowerShell y Open WebUI. |
| **2 · Asistente académico** | [Sesión 2 — System Prompt, Knowledge, Notes y Skills](vol3_laboratorios/Guia_Autonoma_Sesion02_Windows_Paso_a_Paso.md) | [Lab02](vol3_laboratorios/Lab02.md) | [Cap. 5](vol2_manual_tecnico/cap05_mt.md) | Asistente guardado, documento asociado, pruebas, bitácora y Skill asociada. |
| **3 · Captura de consultas** | [Sesión 3 — Forms, Sheets, Apps Script y Python](vol3_laboratorios/Guia_Autonoma_Sesion03_Windows_Paso_a_Paso.md) | [Lab04 — primera etapa](vol3_laboratorios/Lab04.md) | [Cap. 7](vol2_manual_tecnico/cap07_mt.md) y [8](vol2_manual_tecnico/cap08_mt.md) | Solicitud ficticia visible desde Python, con estado **PENDIENTE** sin cambios. |
| **4 · Automatización de respuestas** | [Sesión 4 — Ollama, Sheets y Gmail](vol3_laboratorios/Guia_Autonoma_Sesion04_Windows_Paso_a_Paso.md) | [Lab04 — segunda etapa](vol3_laboratorios/Lab04.md) | [Cap. 8](vol2_manual_tecnico/cap08_mt.md) | Respuesta almacenada, estado **ENVIADA** y correo de prueba recibido. |
| **5 · Mejora y evaluación** | [Sesión 5 — comparar, mejorar y evaluar](vol3_laboratorios/Guia_Autonoma_Sesion05_Windows_Paso_a_Paso.md) | [Lab03](vol3_laboratorios/Lab03.md) | [Cap. 6](vol2_manual_tecnico/cap06_mt.md) y [10](vol2_manual_tecnico/cap10_mt.md) | Dos mejoras justificadas, tres casos comparados y conclusiones documentadas. |

**El orden del taller no es el orden numérico de los laboratorios.** La ruta intensiva utiliza Lab01 → Lab02 → Lab04 (dos sesiones) → Lab03. Los [laboratorios 5](vol3_laboratorios/Lab05.md) y [6](vol3_laboratorios/Lab06.md) se conservan como actividades de profundización.

## 3. Compruebe el resultado antes de avanzar

- **Sesión 1:** Ollama reconoce el modelo y Open WebUI permite una conversación. Si no funciona, consulte los errores frecuentes en la [guía de sesión 1](vol3_laboratorios/Guia_Autonoma_Sesion01_Windows_Paso_a_Paso.md).
- **Sesión 2:** el asistente está guardado y su documento, bitácora y Skill están configurados. Compare las respuestas con la normativa ficticia; una fuente visible no garantiza exactitud.
- **Sesión 3:** una consulta de prueba figura como **PENDIENTE** en Sheets y Python puede leerla sin modificarla ni enviar correo.
- **Sesión 4:** antes de ejecutar el modo completo compruebe que el destinatario es una cuenta propia autorizada. Confirme **ENVIADA** en Sheets y recepción del correo. No repita el procesamiento automáticamente si aparece un error.
- **Sesión 5:** conserve las mismas tres preguntas antes y después de las mejoras. Documente también resultados desfavorables o inciertos.

**Evidencias del portafolio:** guarde capturas o registros del resultado de cada sesión, configuración utilizada, problemas encontrados y una breve reflexión. No incluya contraseñas, enlaces privados de Apps Script, correos personales ni datos académicos reales. Las instrucciones y criterios institucionales de evaluación tienen precedencia sobre las pautas de ejemplo del taller.

## 4. Si algo falla

1. **Localice la etapa:** instalación, modelo local, asistente, servicios de Google o puente Python.
2. **Registre el error exacto** y el paso en que ocurrió, sin exponer información privada.
3. **Consulte la sección de problemas de la guía de esa sesión**, que presenta las comprobaciones iniciales.
4. Cambie **una condición a la vez** y vuelva a verificar. Si hay bloqueos institucionales, consulte soporte TI. En la sesión 4, **no repita un envío** sin comprobar antes el estado de Sheets y Gmail.

Las guías originales y los registros de incidencias permanecen disponibles para consultas avanzadas; no es necesario seguirlos paralelamente al tutorial principal.

## 5. Materiales para profundizar

| Colección | ¿Para qué sirve? |
|---|---|
| [Volumen 1 — Manual del Participante](vol1_manual_participante/) | Conceptos, fundamentos y contexto de las actividades. |
| [Volumen 2 — Manual Técnico](vol2_manual_tecnico/) | Explicaciones técnicas, procedimientos y capturas originales. |
| [Volumen 3 — Laboratorios](vol3_laboratorios/) | Seis laboratorios originales y guías autónomas. |
| [Volumen 4 — Proyecto Integrador](vol4_proyecto_integrador/) | Documentación y evidencias del proyecto de aprendizaje. |
| [Volumen 5 — Manual de Referencia Técnica](vol5_manual_referencia/) | Código, comandos, solución de problemas, glosario y versiones. |
| [Recursos interactivos y actividades de apoyo](RECURSOS_INTERACTIVOS.md) | Tokenización, visualizaciones didácticas y actividades para explorar conceptos. |
| [Scripts y archivos del puente local](scripts/GUIA_CONTEXTO_SKILLS.md) | Código y archivos empleados en las sesiones de integración. |

**Comience por la [guía paso a paso de la sesión 1](vol3_laboratorios/Guia_Autonoma_Sesion01_Windows_Paso_a_Paso.md) y avance cuando pueda comprobar su resultado.**
