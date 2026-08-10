# Cuaderno de Laboratorios

# Laboratorio 4

# Integración del asistente inteligente con Google Workspace y un modelo de IA local

**Capítulo asociado:** Capítulo 4. Integración del asistente inteligente con herramientas de productividad

**Duración estimada:** 100 minutos

**Proyecto Integrador:** Documento 4. Integración del asistente con un proceso digital

---

# Índice

1. Presentación del laboratorio
2. Información general
3. Antes de comenzar

> **Nota:** El desarrollo del laboratorio, el Proyecto Integrador y el cierre se incorporarán en las siguientes entregas.

---

# 1. Presentación del laboratorio

## ¿Qué aprenderá en este laboratorio?

Hasta este momento del taller ha desarrollado un asistente inteligente capaz de responder consultas relacionadas con un problema específico.

Sin embargo, ese asistente continúa funcionando de forma aislada.

En un contexto organizacional, los asistentes inteligentes rara vez operan de manera independiente.

Habitualmente forman parte de procesos donde reciben información desde aplicaciones utilizadas diariamente por las personas, procesan dicha información mediante Inteligencia Artificial y generan una respuesta que posteriormente es utilizada por otros sistemas o por los propios usuarios.

Este laboratorio representa el paso desde un asistente experimental hacia una solución integrada dentro de un flujo de trabajo.

Para ello utilizará herramientas del ecosistema Google Workspace como mecanismo de captura y gestión de información.

Es importante comprender que el propósito de este laboratorio no consiste en aprender programación mediante Google Apps Script.

Google Apps Script será utilizado únicamente como un componente de integración que permitirá conectar distintas herramientas dentro de un proceso sencillo de automatización.

Durante la primera parte del laboratorio todos los participantes desarrollarán un mismo caso guiado.

Posteriormente aplicarán esa metodología para integrar el asistente correspondiente a su Proyecto Integrador.

Al finalizar este laboratorio dispondrá de un flujo funcional donde un usuario podrá ingresar información mediante una herramienta de Google Workspace, ésta será procesada por el asistente inteligente y el resultado quedará disponible para continuar el proceso de trabajo.

Esta integración constituye uno de los principales objetivos del taller, ya que demuestra cómo una solución basada en Inteligencia Artificial puede incorporarse a procesos reales sin modificar completamente la infraestructura tecnológica existente.

---

# 2. Información general

## 2.1 Propósito

Integrar un asistente inteligente con un proceso sencillo basado en Google Workspace, utilizando Google Apps Script, un Web App y un puente local para conectar las herramientas de productividad con el modelo ejecutado mediante Ollama, comprendiendo cómo la Inteligencia Artificial puede incorporarse a flujos de trabajo organizacionales.

---

## 2.2 Competencias

Durante este laboratorio desarrollará las siguientes competencias.

- Comprender el funcionamiento general de un flujo de integración.
- Integrar un asistente inteligente con herramientas del ecosistema Google Workspace.
- Utilizar Google Apps Script como mecanismo de automatización.
- Analizar procesos susceptibles de incorporar Inteligencia Artificial.
- Documentar técnicamente una integración funcional.
- Evaluar las ventajas y limitaciones de este tipo de soluciones.

---

## 2.3 Resultados de aprendizaje

Al finalizar este laboratorio será capaz de:

- Explicar el funcionamiento general de una integración basada en Google Workspace.
- Comprender el papel de Google Apps Script dentro de un flujo de automatización.
- Integrar un asistente inteligente con un proceso sencillo.
- Analizar el recorrido completo de la información dentro del flujo.
- Elaborar el Documento 4 del Portafolio del Proyecto Integrador.

---

## 2.4 Relación con el Manual del Participante

Este laboratorio pone en práctica los contenidos desarrollados en el **Capítulo 4** del Manual del Participante.

Durante dicho capítulo se revisaron los principios generales para integrar asistentes inteligentes con herramientas de productividad y automatización.

En este laboratorio esos conceptos serán aplicados mediante un caso guiado donde el asistente recibirá información desde una herramienta de Google Workspace, procesará dicha información y devolverá una respuesta que continuará formando parte del flujo de trabajo.

---

## 2.5 Tiempo estimado

**Duración total:** 100 minutos

Distribución sugerida:

| Actividad | Tiempo aproximado |
|-----------|------------------:|
| Presentación del laboratorio | 10 minutos |
| Caso guiado de integración | 35 minutos |
| Comprensión del flujo completo | 20 minutos |
| Proyecto Integrador | 30 minutos |
| Reflexión y cierre | 5 minutos |

---

## 2.6 Recursos necesarios

### Hardware

- Computador personal.

**Software**

- Ollama operativo.
- Python instalado.
- Archivo `puente_local.py`.
- Navegador web actualizado.

**Herramientas Google**

- Google Forms.
- Google Sheets.
- Google Apps Script.
- Web App de Google Apps Script.
- Gmail.

### Archivos

- Documento 3 del Proyecto Integrador.
- Manual del Participante (Capítulo 4).

---

## 2.7 Conocimientos previos

Antes de comenzar este laboratorio se espera que el participante:

- haya completado los tres laboratorios anteriores;
- disponga del Documento 3 del Proyecto Integrador;
- conozca el funcionamiento general del asistente inteligente;
- comprenda la metodología de validación desarrollada anteriormente;
- haya revisado el Capítulo 4 del Manual del Participante.

---

# 3. Antes de comenzar

## Lista de verificación

Antes de iniciar confirme que dispone de los siguientes elementos.

| Verificación | Estado |
|--------------|:------:|
| Ollama operativo | □ |
| Open WebUI funcionando | □ |
| Prompt optimizado | □ |
| Cuenta Google disponible | □ |
| Google Forms accesible | □ |
| Google Sheets accesible | □ |
| Google Apps Script disponible | □ |
| Documento 3 del Proyecto Integrador | □ |

---

## 💡 Consejo del instructor

Durante este laboratorio no se concentre en aprender la sintaxis de Google Apps Script.

Procure comprender el recorrido que realiza la información desde que un usuario la ingresa hasta que el asistente devuelve una respuesta.

Comprender el flujo resulta mucho más importante que memorizar instrucciones de programación.

---

## ⚠️ Error frecuente

Muchos participantes concentran toda su atención en el código.

Sin embargo, el verdadero objetivo consiste en comprender la arquitectura del proceso.

Si entiende cómo circula la información entre las distintas herramientas, posteriormente podrá reemplazar Google Workspace por cualquier otro ecosistema tecnológico.

---

## 📌 Importante

El propósito de este laboratorio **no es enseñar Google Apps Script**.

Google Apps Script será utilizado únicamente como una herramienta de integración que permitirá conectar un asistente inteligente con un proceso desarrollado mediante Google Workspace.

Los conceptos relacionados con programación serán explicados únicamente en la medida necesaria para comprender el funcionamiento del flujo implementado.

---

## Objetivo del laboratorio

**Integrar un asistente inteligente con un proceso sencillo basado en Google Workspace, comprendiendo el flujo completo de información entre las distintas herramientas y documentando la solución desarrollada como parte del Proyecto Integrador.**

---

### 📁 Producto que comenzará a construirse

Al finalizar este laboratorio elaborará el:

**Documento 4. Integración del asistente con un proceso digital**

Este documento describirá el flujo implementado, las herramientas utilizadas, el recorrido de la información y las principales decisiones adoptadas durante el proceso de integración.

---

### 📈 Progreso del Proyecto Integrador

```
Documento 1  ██████████ ✔
Documento 2  ██████████ ✔
Documento 3  ██████████ ✔
Documento 4  ███░░░░░░░ En desarrollo
Documento 5  ░░░░░░░░░░
Documento 6  ░░░░░░░░░░
```

---

**Fin de la Parte 1 del Laboratorio 4**

> La **Parte 2** desarrollará un caso guiado donde todos los participantes construirán un flujo completo utilizando Google Forms, Google Sheets, Google Apps Script y el asistente inteligente local, comprendiendo el recorrido de la información desde su captura hasta la generación de la respuesta.

# 4. Desarrollo del laboratorio guiado

Durante este laboratorio integrará, por primera vez, el asistente inteligente desarrollado en los laboratorios anteriores con un proceso de trabajo basado en Google Workspace.

Hasta ahora el asistente ha funcionado como una aplicación independiente donde el usuario escribe directamente una consulta y obtiene una respuesta.

En un entorno organizacional esto rara vez ocurre.

Lo habitual es que la información provenga desde formularios, hojas de cálculo, documentos, correos electrónicos u otras aplicaciones utilizadas diariamente por las personas.

Por esta razón, el objetivo del laboratorio consiste en comprender cómo un asistente inteligente puede incorporarse como un componente más dentro de un flujo de trabajo.

Para facilitar el aprendizaje, todos los participantes desarrollarán inicialmente el mismo caso guiado.

Posteriormente aplicarán la metodología al Proyecto Integrador.

---

# Caso guiado

## Clasificación automática de solicitudes mediante IA

En este caso se implementará un flujo sencillo donde un usuario enviará una solicitud mediante un formulario de Google.

La información será registrada automáticamente en una hoja de cálculo.

Posteriormente, Google Apps Script permitirá exponer las solicitudes pendientes mediante un Web App. El archivo `puente_local.py`, ejecutado en el entorno local, consultará periódicamente este servicio, enviará las solicitudes al modelo mediante Ollama y devolverá las respuestas generadas. Finalmente, Google Apps Script registrará los resultados en Google Sheets y enviará la respuesta al correo electrónico del usuario.

El flujo general será el siguiente.

```

Usuario
↓
Google Forms
↓
Google Sheets
↓
Google Apps Script / Web App
↓
puente_local.py
↓
Ollama
↓
puente_local.py
↓
Google Apps Script / Web App
↓
Google Sheets
↓
Gmail
↓
Usuario

```

Observe que el asistente no trabaja de manera aislada.

Forma parte de un proceso organizacional completo.

---

# Actividad 1

# Comprensión del flujo de integración

## Objetivo

Comprender el recorrido que seguirá la información desde su captura hasta la generación de la respuesta.

---

## Contexto

Antes de implementar cualquier integración resulta indispensable comprender cómo circula la información entre los distintos componentes.

Cuando se conoce el flujo completo resulta mucho más sencillo identificar posibles problemas, modificar procesos o incorporar nuevas herramientas.

Por ello, esta primera actividad se centrará en analizar la arquitectura general de la solución.

---

## Procedimiento

Observe cuidadosamente el siguiente flujo.

```

Usuario
↓
Google Forms
↓
Google Sheets
↓
Google Apps Script / Web App
↓
puente_local.py
↓
Ollama
↓
puente_local.py
↓
Google Apps Script / Web App
↓
Google Sheets
↓
Gmail
↓
Usuario

```

Ahora responda las preguntas propuestas.

---

## 📝 Registro del participante

###  ¿Dónde comienza el proceso?

______________________________________________________

---

### ¿Dónde queda registrada inicialmente la solicitud?

______________________________________________________

---

### ¿Qué función cumple Google Apps Script y el Web App?

______________________________________________________

---

### ¿Qué función cumple `puente_local.py`?

______________________________________________________

---

### ¿Qué componente ejecuta el modelo de lenguaje y genera la respuesta?

______________________________________________________

---


### ¿Dónde queda registrada la respuesta?

______________________________________________________

---


### ¿Cómo recibe finalmente el usuario la respuesta generada?

______________________________________________________

---

## 💡 Consejo del instructor

No memorice el flujo.

Procure comprender el propósito de cada componente.

En proyectos futuros algunas herramientas podrán cambiar, pero la lógica general de integración será muy similar.

---

## ⚠️ Error frecuente

Pensar que Google Apps Script "hace Inteligencia Artificial".

En realidad, Google Apps Script únicamente coordina el intercambio de información entre las distintas aplicaciones.

La Inteligencia Artificial continúa siendo ejecutada por el modelo local.

---

## ✅ Checkpoint

Antes de continuar confirme que comprende:

- □ dónde comienza el proceso;
- □ cómo circula la información;
- □ cuál es el papel de cada herramienta;
- □ dónde se genera la respuesta.

---

# Actividad 2

# Construcción del formulario de entrada

## Objetivo

Crear el mecanismo mediante el cual los usuarios enviarán información al asistente inteligente.

---

## Contexto

Todo proceso automatizado necesita un punto de entrada.

En este laboratorio dicho punto será un formulario de Google.

El formulario permitirá capturar la información que posteriormente será enviada al asistente.

Observe que el formulario no realiza ninguna tarea de Inteligencia Artificial.

Su función consiste únicamente en registrar información estructurada.

---

## Procedimiento

Cree un formulario con la siguiente estructura.

### Campo 1

Nombre del solicitante.

---

### Campo 2

Correo electrónico.

---

### Campo 3

Descripción de la solicitud.

---

### Campo 4

Prioridad.

- Alta
- Media
- Baja

---

Una vez creado el formulario:

- genere una respuesta de prueba;
- verifique que la información aparece correctamente en Google Sheets.

---

## 📝 Registro del participante

| Verificación | Estado |
|--------------|:------:|
| Formulario creado | □ |
| Hoja de cálculo generada | □ |
| Registro de prueba realizado | □ |
| Información almacenada correctamente | □ |

---

## 📁 Evidencias

Conserve:

- captura del formulario;
- captura de Google Sheets;
- registro de prueba.

Estas evidencias formarán parte del Documento 4.

---

## 💡 Consejo del instructor

Procure que los nombres de los campos sean claros.

Posteriormente Google Apps Script utilizará esos nombres para acceder a la información registrada.

---

## 🔍 Deténgase y analice

¿Por qué resulta conveniente utilizar un formulario como mecanismo de captura de información?

______________________________________________________

______________________________________________________

______________________________________________________

---

## ✅ Checkpoint

Antes de continuar confirme que:

- □ el formulario funciona correctamente;
- □ Google Sheets recibe las respuestas;
- □ los datos aparecen organizados.

---

# Actividad 3

# Comprensión de los componentes de integración

## Objetivo

Comprender el rol que desempeña Google Apps Script dentro del proceso de integración.

---

## Contexto

Hasta este momento el flujo termina cuando la información queda registrada en Google Sheets.

El siguiente paso consiste en permitir que las solicitudes registradas en Google Sheets puedan ser procesadas por el modelo ejecutado localmente.

Para ello se utilizarán dos componentes principales: **Google Apps Script**, que permitirá leer y actualizar las solicitudes mediante un Web App, y **`puente_local.py`**, que consultará dicho servicio y realizará la comunicación con Ollama.

De esta forma, Google Apps Script gestiona la interacción con Google Workspace, mientras que `puente_local.py` coordina el intercambio de información entre el Web App y el modelo ejecutado localmente.

Es importante destacar que Google Apps Script no reemplaza al asistente.

En este laboratorio trabajará sobre un script previamente preparado por el instructor.

El objetivo no será desarrollar una aplicación desde cero, sino comprender cómo el script participa dentro del flujo de integración.

---

## Procedimiento

Observe el script proporcionado por el instructor.

Durante la revisión identifique:

- dónde se leen los datos desde Google Sheets;
- cómo se exponen las solicitudes pendientes mediante el Web App;
- dónde se recibe la respuesta procesada;
- dónde se actualiza nuevamente la información en Google Sheets;
- dónde se realiza el envío de la respuesta mediante Gmail.

No es necesario comprender cada instrucción del código.

Lo importante es identificar el papel que desempeña cada bloque dentro del proceso.

---

## 📝 Registro del participante

Complete la siguiente tabla.

| Componente                   | Función dentro del flujo |
| ---------------------------- | ------------------------ |
| Google Forms                 |                          |
| Google Sheets                |                          |
| Google Apps Script / Web App |                          |
| `puente_local.py`            |                          |
| Ollama                       |                          |
| Gmail                        |                          |

---

## 💡 Consejo del instructor

Cuando analice un programa procure comprender primero qué hace cada bloque.

La comprensión de la arquitectura general resulta mucho más importante que memorizar instrucciones específicas.

---

## ⚠️ Error frecuente

Intentar comprender cada línea de código antes de entender el proceso completo.

Primero comprenda el flujo.

Posteriormente podrá analizar el detalle de la implementación.

---

## 📁 Portafolio

Las observaciones registradas durante estas actividades constituirán la base para documentar la arquitectura de integración utilizada posteriormente en el Proyecto Integrador.

---

## ✅ Checkpoint general

Antes de finalizar esta sección confirme que:

- □ comprende el recorrido completo de la información;
- □ construyó correctamente el formulario;
- □ verificó el almacenamiento de datos en Google Sheets;
- □ comprendió el papel de Google Apps Script dentro del proceso.

Con estas actividades concluye la primera parte del caso guiado.

En la siguiente sección completará la integración ejecutando el flujo completo, verificará el funcionamiento de la comunicación entre Google Workspace y el asistente inteligente, analizará los resultados obtenidos y comprenderá cómo pequeñas modificaciones permiten adaptar el flujo a distintos procesos organizacionales.

---

**Fin de la Parte 2 del Laboratorio 4**

# Actividad 4

# Ejecución del flujo de integración

## Objetivo

Verificar el funcionamiento completo del proceso de integración entre Google Workspace y el asistente inteligente local.

---

## Contexto

Hasta este momento ha construido los distintos componentes del flujo y ha comprendido el papel que desempeña cada uno de ellos.

Ahora ejecutará el proceso completo.

Esta actividad permitirá observar cómo una solicitud enviada por un usuario recorre las distintas herramientas hasta transformarse en una respuesta generada por el asistente inteligente.

Más que analizar el código utilizado, el objetivo consiste en comprender el comportamiento del flujo y verificar que la información llegue correctamente desde el punto de origen hasta el resultado final.

---

## Procedimiento

Complete las siguientes actividades.

### Paso 1

Abra el formulario de Google creado anteriormente.

Ingrese una nueva solicitud de prueba.

Procure utilizar una descripción suficientemente clara para facilitar posteriormente el análisis de la respuesta.

---

### Paso 2

Verifique que la información quedó registrada correctamente en Google Sheets.

Compruebe que todos los campos contienen la información esperada.

---

### Paso 3

Verifique que el Web App de Google Apps Script se encuentre correctamente implementado y que Ollama esté operativo.

A continuación, ejecute el archivo `puente_local.py` desde la terminal, siguiendo las instrucciones desarrolladas en el Manual Técnico.

Observe cómo el puente identifica las solicitudes pendientes, las envía al modelo ejecutado mediante Ollama y devuelve las respuestas al servicio de Google Apps Script.

---

### Paso 4

Espere el procesamiento de la solicitud.

Revise Google Sheets y compruebe que el estado de la solicitud fue actualizado y que la respuesta generada quedó registrada correctamente.

Finalmente, verifique que el usuario recibió la respuesta mediante correo electrónico.

---

### Paso 5

Repita el proceso utilizando nuevas solicitudes.

Procure utilizar consultas de distinta naturaleza para observar el comportamiento del flujo.

---

## 📝 Registro del participante

| Prueba | Estado |
|---------|:------:|
| Formulario enviado | □ |
| Registro en Google Sheets | □ |
| Script ejecutado | □ |
| Respuesta generada | □ |
| Respuesta almacenada | □ |

---

## 📁 Evidencias

Conserve las siguientes capturas.

- Formulario completado.
- Registro en Google Sheets.
- Ejecución de `puente_local.py`.
- Resultado generado por el asistente.

Estas evidencias serán utilizadas posteriormente en el Documento 4 del Proyecto Integrador.

---

## 💡 Consejo del instructor

Durante esta actividad observe cuidadosamente el recorrido de la información.

Pregúntese constantemente:

> ¿Qué aplicación está trabajando en este momento?

Comprender esa secuencia facilitará enormemente futuras integraciones.

---

## ⚠️ Error frecuente

Cuando el flujo no funciona correctamente, muchos usuarios comienzan inmediatamente a modificar el código.

Antes de hacerlo, verifique primero:

- que el formulario registró correctamente la información;
- que Google Sheets contiene los datos esperados;
- que el asistente se encuentra operativo;
- que el script fue ejecutado correctamente.

En la mayoría de los casos el problema se encuentra en alguno de estos elementos y no en la lógica del programa.

---

## ✅ Checkpoint

Antes de continuar confirme que:

- □ el flujo completo funciona correctamente;
- □ la respuesta llega nuevamente a Google Sheets;
- □ comprende el recorrido completo de la información.

---

# Actividad 5

# Análisis del flujo implementado

## Objetivo

Analizar críticamente la solución desarrollada e identificar oportunidades de mejora.

---

## Contexto

Todo flujo de automatización puede evolucionar.

Después de comprobar que la integración funciona correctamente resulta conveniente analizar posibles mejoras.

No todas ellas requieren programación.

Muchas veces basta con reorganizar el proceso o incorporar nuevos componentes.

---

## Procedimiento

Observe nuevamente el flujo implementado.

Complete la siguiente tabla.

---

## 📝 Registro del participante

| Pregunta | Respuesta |
|-----------|-----------|
| ¿Qué etapa consume más tiempo? | |
| ¿Qué parte del flujo podría automatizarse aún más? | |
| ¿Qué información adicional podría incorporarse? | |
| ¿Qué dificultades observó durante la integración? | |
| ¿Qué ventajas ofrece este tipo de solución? | |

---

## 🔍 Deténgase y analice

Imagine que la organización recibe cien solicitudes diarias.

¿Cómo cambiaría el trabajo de las personas utilizando este flujo automatizado?

______________________________________________________

______________________________________________________

______________________________________________________

---

## 💡 Consejo del instructor

No piense únicamente en la tecnología.

Analice también el proceso de trabajo.

La automatización resulta verdaderamente útil cuando simplifica tareas realizadas habitualmente por las personas.

---

# Actividad 6

# Adaptación del flujo a distintos escenarios

## Objetivo

Comprender que la misma arquitectura de integración puede utilizarse en diferentes contextos organizacionales.

---

## Contexto

El flujo desarrollado durante este laboratorio corresponde únicamente a un ejemplo.

La arquitectura utilizada puede adaptarse fácilmente a múltiples procesos.

Lo importante no es memorizar un caso específico.

Lo importante consiste en comprender el patrón general de integración.

---

## Actividad

Complete la siguiente tabla proponiendo posibles aplicaciones.

| Contexto | Posible aplicación |
|-----------|-------------------|
| Educación | |
| Salud | |
| Empresa privada | |
| Institución pública | |
| Organización de su interés | |

---

## 💡 Consejo del instructor

Cuando piense en nuevas aplicaciones pregúntese siempre:

- ¿Qué información ingresa?
- ¿Qué análisis realiza el asistente?
- ¿Qué información entrega?
- ¿Quién utilizará posteriormente esa respuesta?

Estas cuatro preguntas permiten diseñar una gran cantidad de soluciones basadas en Inteligencia Artificial.

---

## 🌐 Buenas prácticas de integración

Antes de implementar un flujo de trabajo basado en Inteligencia Artificial considere siempre los siguientes aspectos.

- Verifique la calidad de los datos de entrada.
- Defina claramente quién utilizará las respuestas generadas.
- Mantenga registros de las decisiones automatizadas.
- Evite automatizar procesos críticos sin supervisión humana.
- Revise periódicamente el funcionamiento del asistente.
- Documente todas las modificaciones realizadas sobre el flujo.

Estas prácticas contribuyen a desarrollar soluciones más confiables, mantenibles y alineadas con principios de uso responsable de la Inteligencia Artificial.

---

## 📁 Portafolio

Las observaciones realizadas durante esta actividad permitirán justificar posteriormente las decisiones adoptadas durante el diseño del flujo de integración del Proyecto Integrador.

---

## ✅ Checkpoint general

Antes de finalizar la etapa guiada confirme que:

- □ ejecutó correctamente el flujo completo;
- □ verificó el intercambio de información entre las herramientas;
- □ analizó críticamente el funcionamiento del proceso;
- □ identificó oportunidades de mejora;
- □ comprendió cómo adaptar la arquitectura a otros escenarios.

Con estas actividades concluye el caso guiado del Laboratorio 4.

En la siguiente parte aplicará exactamente esta metodología al **Proyecto Integrador**, construyendo el flujo de integración correspondiente a su propio asistente inteligente y documentando la arquitectura implementada.

---

**Fin de la Parte 3 del Laboratorio 4**

# 5. Proyecto Integrador

Durante el caso guiado aprendió cómo integrar un asistente inteligente con un proceso sencillo utilizando herramientas del ecosistema Google Workspace.

Ahora aplicará la misma metodología al asistente desarrollado durante los laboratorios anteriores.

En esta oportunidad no replicará exactamente el ejemplo trabajado en clase.

Su desafío consistirá en diseñar un flujo de integración coherente con el problema identificado en el Proyecto Integrador.

El objetivo no es construir una automatización compleja.

Lo importante es demostrar que el asistente puede incorporarse de manera útil a un proceso de trabajo real.

Al finalizar esta sección habrá definido la arquitectura de integración de su solución y generado el **Documento 4 del Portafolio del Proyecto Integrador**.

---

# 5.1 Objetivo

Diseñar e implementar un flujo sencillo que integre el asistente inteligente con una herramienta del ecosistema Google Workspace, documentando la arquitectura utilizada y justificando las decisiones adoptadas durante el proceso de integración.

---

# Antes de comenzar

Recupere los siguientes documentos desarrollados anteriormente.

- Documento 1. Definición del problema.
- Documento 2. Diseño del asistente inteligente.
- Documento 3. Validación y optimización.

Revise nuevamente el propósito del asistente.

Pregúntese:

> ¿En qué momento del proceso organizacional sería útil incorporar el asistente?

La respuesta a esa pregunta orientará toda la integración.

---

## 💡 Consejo del instructor

No intente automatizar un proceso completo.

Seleccione una única actividad donde el asistente pueda aportar valor de manera clara y verificable.

Las soluciones simples suelen ser más robustas y fáciles de mantener.

---

# Actividad 1

# Identificación del punto de integración

## Objetivo

Determinar el momento del proceso donde el asistente inteligente será incorporado.

---

## Actividad

Analice el proceso definido en el Documento 1.

Identifique una actividad donde la Inteligencia Artificial pueda apoyar a las personas.

---

## 📝 Registro del participante

### Nombre del proceso

______________________________________________________

---

### Etapa donde se incorporará el asistente

______________________________________________________

---

### Problema que resolverá en esa etapa

______________________________________________________

______________________________________________________

______________________________________________________

---

### Beneficio esperado

______________________________________________________

______________________________________________________

______________________________________________________

---

## 🔍 Deténgase y analice

¿Por qué seleccionó precisamente esa etapa del proceso?

______________________________________________________

______________________________________________________

______________________________________________________

---

# Actividad 2

# Diseño del flujo de integración

## Objetivo

Representar gráficamente el recorrido que realizará la información.

---

## Actividad

Complete el siguiente esquema.

```
Usuario
↓
Herramienta Google Workspace
↓
Google Apps Script / Web App
↓
puente_local.py
↓
Ollama
↓
puente_local.py
↓
Google Apps Script / Web App
↓
Herramienta Google Workspace
↓
Usuario
```

Ahora personalice el flujo reemplazando cada componente por el que corresponda a su proyecto.

---

## 📝 Registro del participante

### Flujo propuesto

```
_________________________________________________

↓

_________________________________________________

↓

_________________________________________________

↓

_________________________________________________

↓

_________________________________________________

↓

_________________________________________________

↓

_________________________________________________
```

---

## 💡 Consejo del instructor

No centre su atención únicamente en la tecnología.

Cada bloque representa una actividad del proceso.

Comprender el flujo permitirá modificar posteriormente la implementación sin alterar el funcionamiento general.

---

# Actividad 3

# Selección de herramientas

## Objetivo

Justificar las herramientas elegidas para implementar la integración.

---

## Actividad

Complete la siguiente tabla.

| Herramienta/componente             | Función dentro del flujo |
| ---------------------------------- | ------------------------ |
| Google Forms                       |                          |
| Google Sheets                      |                          |
| Google Apps Script / Web App       |                          |
| `puente_local.py`                  |                          |
| Ollama                             |                          |
| Gmail u otra herramienta de salida |                          |

---

## Reflexión

¿Por qué estas herramientas resultan adecuadas para el problema seleccionado?

______________________________________________________

______________________________________________________

______________________________________________________

---

# Actividad 4

# Implementación del flujo

## Objetivo

Construir y verificar el funcionamiento de la integración.

---

## Actividad

Implemente el flujo utilizando el ejemplo desarrollado durante el caso guiado como referencia.

Verifique que:

- la información ingresa correctamente;
- el asistente recibe la consulta;
- la respuesta es generada;
- el resultado vuelve al flujo de trabajo.

---

## 📝 Registro del participante

| Verificación | Estado |
|--------------|:------:|
| Captura de datos | □ |
| Comunicación con el asistente | □ |
| Generación de respuesta | □ |
| Registro del resultado | □ |
| Flujo completo operativo | □ |

---

## 📁 Evidencias

Conserve capturas de:

- formulario utilizado;
- hoja de cálculo;
- ejecución del flujo;
- resultado obtenido.

Estas evidencias formarán parte del Documento 4.

---

## ⚠️ Error frecuente

Si el flujo no funciona correctamente, no modifique inmediatamente el script.

Revise primero:

- la captura de datos;
- la estructura de Google Sheets;
- el funcionamiento del asistente;
- la configuración de los permisos.

En la mayoría de los casos los problemas se originan en estos elementos.

---

# Actividad 5

# Evaluación de la integración

## Objetivo

Analizar el funcionamiento del flujo implementado.

---

## Actividad

Responda las siguientes preguntas.

### ¿Qué parte del flujo funcionó correctamente?

______________________________________________________

______________________________________________________

---

### ¿Qué dificultades aparecieron?

______________________________________________________

______________________________________________________

---

### ¿Qué mejoras podrían implementarse posteriormente?

______________________________________________________

______________________________________________________

---

### ¿Cómo podría ampliarse esta solución para atender un mayor volumen de usuarios?

______________________________________________________

______________________________________________________

---

## 🌐 Uso responsable de la integración

Toda automatización basada en Inteligencia Artificial debe considerar aspectos relacionados con la protección de la información y la supervisión humana.

Reflexione sobre las siguientes preguntas.

### ¿Qué información debería evitar enviarse automáticamente al asistente?

______________________________________________________

______________________________________________________

---

### ¿Qué respuestas deberían ser revisadas por una persona antes de ser utilizadas?

______________________________________________________

______________________________________________________

---

### ¿Qué medidas permitirían proteger la privacidad de los usuarios?

______________________________________________________

______________________________________________________

---

# 5.2 Documento generado

Al finalizar este laboratorio deberá disponer del siguiente documento.

---

# Documento 4

## Integración del asistente con un proceso digital

Este documento deberá contener, como mínimo:

- descripción del proceso seleccionado;
- punto de integración;
- arquitectura del flujo;
- herramientas utilizadas;
- evidencias del funcionamiento;
- dificultades encontradas;
- mejoras propuestas.

Este documento demostrará cómo el asistente inteligente fue incorporado a un proceso de trabajo utilizando herramientas del ecosistema Google Workspace.

---

## 📁 Portafolio

Incorpore el Documento 4 al Portafolio del Proyecto Integrador.

Al finalizar este laboratorio su Portafolio deberá contener:

- Documento 1. Definición del problema.
- Documento 2. Diseño del asistente.
- Documento 3. Validación y optimización.
- Documento 4. Integración con un proceso digital.

---

# 5.3 Autoevaluación del Proyecto

Antes de continuar confirme que:

| Aspecto | Sí | Parcial | No |
|----------|:--:|:--------:|:--:|
| Identifiqué correctamente el punto de integración. | □ | □ | □ |
| Diseñé el flujo completo. | □ | □ | □ |
| Seleccioné adecuadamente las herramientas. | □ | □ | □ |
| Implementé el flujo funcional. | □ | □ | □ |
| Evalué el funcionamiento de la integración. | □ | □ | □ |
| Incorporé el Documento 4 al Portafolio. | □ | □ | □ |

---

## 💡 Consejo final

No evalúe la integración únicamente desde una perspectiva tecnológica.

Pregúntese siempre si la solución realmente facilita el trabajo de las personas.

Una integración exitosa no es aquella que utiliza más herramientas, sino aquella que aporta valor al proceso donde se implementa.

---

### 📈 Progreso del Proyecto Integrador

```
Documento 1  ██████████ ✔
Documento 2  ██████████ ✔
Documento 3  ██████████ ✔
Documento 4  ██████████ ✔
Documento 5  ░░░░░░░░░░
Documento 6  ░░░░░░░░░░
```

---

**Fin de la Parte 4 del Laboratorio 4**

> En la **Parte 5** realizará el cierre del laboratorio, reflexionará sobre la integración desarrollada, verificará los productos incorporados al Portafolio y preparará el trabajo que desarrollará en el **Laboratorio 5**, donde el asistente inteligente dejará de ser una integración aislada para convertirse en un componente de un proceso organizacional completo.

# 6. Cierre del laboratorio

Durante este laboratorio su asistente inteligente dio un paso decisivo hacia un escenario de aplicación profesional.

Hasta el laboratorio anterior el asistente funcionaba como una herramienta independiente que respondía consultas realizadas directamente por el usuario.

A partir de las actividades desarrolladas hoy, el asistente pasó a formar parte de un flujo de trabajo donde interactúa con aplicaciones del ecosistema Google Workspace.

Este cambio representa uno de los principales objetivos del taller.

En un entorno organizacional, la Inteligencia Artificial genera mayor valor cuando se integra con procesos existentes, apoyando la captura, el análisis y el tratamiento de la información sin modificar completamente la forma en que las personas trabajan.

Durante este laboratorio comprobó que una integración sencilla puede automatizar tareas repetitivas y facilitar la gestión de información, manteniendo al mismo tiempo el control humano sobre el proceso.

---

# 6.1 Síntesis

Durante este laboratorio desarrolló las siguientes actividades:

- analizó la arquitectura general de un flujo de integración;
- comprendió el papel de Google Forms, Google Sheets y Google Apps Script;
- construyó un flujo de integración guiado;
- verificó el recorrido completo de la información;
- integró el asistente inteligente con un proceso sencillo;
- documentó la arquitectura implementada;
- reflexionó sobre el uso responsable de la automatización;
- elaboró el Documento 4 del Proyecto Integrador.

Observe que el principal aprendizaje no consiste en utilizar una herramienta específica.

El aprendizaje más importante consiste en comprender cómo integrar la Inteligencia Artificial dentro de un proceso de trabajo existente.

Esta metodología podrá aplicarse posteriormente utilizando otras plataformas tecnológicas sin modificar la lógica general del proceso.

---

# 6.2 ¿Qué aprendí hoy?

Dedique algunos minutos a reflexionar sobre la experiencia desarrollada durante este laboratorio.

---

## ¿Qué fue lo más importante que aprendió acerca de la integración entre IA y Google Workspace?

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

---

## ¿Qué componente del flujo le resultó más fácil de comprender?

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

---

## ¿Qué parte del proceso considera que podría mejorarse?

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

---

## ¿Qué otras aplicaciones del ecosistema Google cree que podrían integrarse con su asistente inteligente?

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

---

# 6.3 Autoevaluación

Evalúe el nivel de logro alcanzado durante este laboratorio.

| Criterio | Logrado | Parcial | Pendiente |
|----------|:-------:|:--------:|:---------:|
| Comprendí el flujo completo de integración. | □ | □ | □ |
| Comprendí el papel de Google Apps Script. | □ | □ | □ |
| Integré correctamente el asistente con Google Workspace. | □ | □ | □ |
| Verifiqué el recorrido completo de la información. | □ | □ | □ |
| Analicé oportunidades de mejora del proceso. | □ | □ | □ |
| Documenté la arquitectura implementada. | □ | □ | □ |
| Completé el Documento 4 del Proyecto Integrador. | □ | □ | □ |

---

## 🔍 Reflexión profesional

Responda la siguiente pregunta.

> **¿Por qué considera que una organización obtiene mayor beneficio cuando la Inteligencia Artificial forma parte de un proceso de trabajo y no funciona como una herramienta aislada?**

En su respuesta considere aspectos relacionados con:

- eficiencia;
- automatización;
- calidad de la información;
- continuidad del proceso;
- apoyo a la toma de decisiones.

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

---

## 🌐 Integración responsable de la Inteligencia Artificial

La incorporación de Inteligencia Artificial dentro de procesos organizacionales también implica nuevas responsabilidades.

Antes de implementar una solución de este tipo conviene analizar aspectos relacionados con la seguridad, la privacidad y el control de las decisiones automatizadas.

Reflexione sobre las siguientes preguntas.

### ¿Qué tipo de información no debería incorporarse automáticamente al flujo?

______________________________________________________

______________________________________________________

______________________________________________________

---

### ¿Qué actividades deberían mantenerse bajo supervisión humana?

______________________________________________________

______________________________________________________

______________________________________________________

---

### ¿Qué controles implementaría para asegurar la calidad de las respuestas generadas?

______________________________________________________

______________________________________________________

______________________________________________________

---

> **Importante**
>
> Automatizar un proceso no significa eliminar la responsabilidad de las personas.
>
> La Inteligencia Artificial debe entenderse como un mecanismo de apoyo que facilita el trabajo, pero las decisiones relevantes continúan siendo responsabilidad de quienes gestionan el proceso.

---

# 6.4 Lista de entregables

Al finalizar este laboratorio deberá disponer de los siguientes productos.

| Producto | Estado |
|----------|:------:|
| Flujo de integración diseñado | □ |
| Formulario implementado | □ |
| Hoja de cálculo configurada | □ |
| Flujo ejecutado correctamente | □ |
| Evidencias del funcionamiento | □ |
| Documento 4 del Proyecto Integrador | □ |

Conserve todos estos productos.

Serán utilizados durante el Laboratorio 5.

---

# 📁 Portafolio

Al finalizar este laboratorio, el Portafolio del Proyecto Integrador debería contener:

### Documento 1

**Definición del problema y alcance**

✔ Completado.

---

### Documento 2

**Diseño del asistente inteligente especializado**

✔ Completado.

---

### Documento 3

**Validación y optimización del asistente inteligente**

✔ Completado.

---

### Documento 4

**Integración del asistente con un proceso digital**

✔ Completado.

---

Observe cómo el Proyecto Integrador ha evolucionado.

Ya no dispone únicamente de un asistente inteligente.

Ahora posee una solución capaz de interactuar con herramientas utilizadas diariamente dentro de una organización.

---

# 6.5 Preparación del Laboratorio 5

Antes de asistir al siguiente laboratorio asegúrese de que:

- conserva los cuatro documentos desarrollados hasta ahora;
- mantiene operativo el entorno local de Inteligencia Artificial;
- dispone del flujo de integración funcionando correctamente;
- ha revisado el Capítulo 5 del Manual del Participante.

En el próximo laboratorio el foco dejará de estar en la integración tecnológica.

Trabajará sobre el proceso organizacional completo.

Analizará cómo la Inteligencia Artificial puede incorporarse a un flujo de trabajo más amplio, identificando oportunidades de mejora, puntos críticos y mecanismos de seguimiento.

---

## 💡 Recomendación del instructor

Observe durante los próximos días algún proceso de trabajo perteneciente a su organización.

Pregúntese:

- ¿Dónde comienza realmente el proceso?
- ¿Qué actividades agregan valor?
- ¿Qué tareas son repetitivas?
- ¿Qué información se genera en cada etapa?
- ¿En qué otros puntos podría incorporarse la Inteligencia Artificial?

Estas observaciones enriquecerán considerablemente el desarrollo del Laboratorio 5.

---

# 6.6 Vinculación con el Laboratorio 5

Hasta ahora el Proyecto Integrador ha evolucionado de la siguiente manera:

- identificó un problema;
- diseñó un asistente inteligente;
- validó su funcionamiento;
- lo integró con un proceso digital sencillo.

Durante el Laboratorio 5 dará un nuevo paso.

Analizará el proceso organizacional completo donde se inserta el asistente.

Aprenderá a identificar:

- entradas y salidas del proceso;
- actores involucrados;
- actividades automatizadas;
- puntos de control;
- indicadores de funcionamiento;
- oportunidades de mejora.

El asistente dejará de ser una solución tecnológica aislada para transformarse en un componente integrado dentro de un proceso organizacional completo.

---

# Mensaje final

Las organizaciones no adoptan la Inteligencia Artificial únicamente por su capacidad para generar respuestas.

Lo hacen porque permite optimizar procesos, apoyar a las personas y facilitar la toma de decisiones.

Durante este laboratorio ha comprobado que el verdadero valor de un asistente inteligente aparece cuando interactúa con otras herramientas y participa activamente en un flujo de trabajo.

Ese enfoque constituye uno de los principios fundamentales de este taller y será la base sobre la cual continuará desarrollando su Proyecto Integrador durante los dos últimos laboratorios.

---

# Fin del Laboratorio 4

## Producto obtenido para el Portafolio

**Documento 4. Integración del asistente con un proceso digital**

## Próximo laboratorio

**Laboratorio 5. Integración del asistente inteligente dentro de un proceso organizacional completo**

**Proyecto Integrador**

**Documento 5. Consolidación de la solución y análisis del proceso organizacional**

---

### 📈 Progreso del Proyecto Integrador

```
Documento 1  ██████████ ✔
Documento 2  ██████████ ✔
Documento 3  ██████████ ✔
Documento 4  ██████████ ✔
Documento 5  ███░░░░░░░ Próximo laboratorio
Documento 6  ░░░░░░░░░░
```

