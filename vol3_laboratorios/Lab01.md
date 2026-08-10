# Cuaderno de Laboratorios

# Laboratorio 1

# Instalación de Ollama y Open WebUI, exploración de un LLM y primeros prompts

**Capítulo asociado:** Capítulo 1. Introducción a la Inteligencia Artificial Generativa Local

**Duración estimada:** 100 minutos

**Proyecto Integrador:** Documento 1. Definición del problema y alcance del Proyecto Integrador

---

# Índice

1. Presentación del laboratorio
2. Información general
3. Antes de comenzar

> **Nota:** El desarrollo del laboratorio, el Proyecto Integrador y el cierre se incorporarán en las siguientes entregas.

---

# 1. Presentación del laboratorio

## ¿Qué aprenderá en este laboratorio?

Bienvenido al primer laboratorio del taller **Diseño e implementación de un asistente inteligente local para el apoyo al análisis y la toma de decisiones**.

Este primer laboratorio tiene un propósito fundamental: preparar el entorno de trabajo que será utilizado durante todo el taller e iniciar el Proyecto Integrador que se desarrollará progresivamente a lo largo de los laboratorios.

A diferencia de otros cursos donde la Inteligencia Artificial se utiliza únicamente mediante servicios disponibles en Internet, en este taller trabajará con un entorno de **Inteligencia Artificial Generativa Local**. Esto significa que el modelo de lenguaje será ejecutado directamente en su computador mediante **Ollama**, mientras que **Open WebUI** proporcionará una interfaz gráfica para interactuar con dicho modelo.

Trabajar con modelos locales presenta múltiples ventajas para organizaciones e instituciones. Entre ellas destacan el mayor control sobre la información procesada, la posibilidad de mantener determinados datos dentro de la infraestructura utilizada y la capacidad de interactuar con los modelos sin depender permanentemente de servicios externos.

Sin embargo, disponer de un entorno operativo constituye sólo el primer paso.

El propósito principal del taller no consiste en aprender a instalar herramientas, sino en desarrollar la capacidad para diseñar soluciones que aporten valor a procesos reales mediante el uso de Inteligencia Artificial Generativa.

Por esta razón, durante este mismo laboratorio comenzará el desarrollo del **Proyecto Integrador**, seleccionando un problema perteneciente a su propio contexto profesional que será abordado progresivamente durante el resto del taller.

En los próximos laboratorios ese problema evolucionará mediante distintas etapas:

- diseño del asistente inteligente;
- validación y optimización;
- integración con herramientas del ecosistema Google Workspace mediante Google Apps Script;
- consolidación de la solución;
- presentación profesional del proyecto.

Al finalizar este laboratorio usted dispondrá de un entorno local completamente operativo y habrá definido el punto de partida de su Proyecto Integrador.

Este trabajo constituirá la base sobre la cual se desarrollarán todas las actividades prácticas de los laboratorio siguientes.

---

# 2. Información general

## 2.1 Propósito

Instalar, verificar y configurar el entorno de trabajo basado en Ollama y Open WebUI para ejecutar modelos de lenguaje de manera local, explorar las primeras interacciones mediante prompts y comenzar el Proyecto Integrador identificando un problema susceptible de ser apoyado mediante Inteligencia Artificial Generativa.

---

## 2.2 Competencias

Al desarrollar este laboratorio fortalecerá las siguientes competencias:

- Instalar y verificar un entorno local de Inteligencia Artificial Generativa.
- Interactuar con modelos de lenguaje mediante prompts.
- Analizar las posibilidades de aplicación de la IA en procesos organizacionales.
- Identificar oportunidades de mejora dentro de su contexto profesional.
- Definir el problema que dará origen al Proyecto Integrador.
- Documentar técnicamente el alcance inicial de una solución basada en IA.

---

## 2.3 Resultados de aprendizaje

Al finalizar este laboratorio, será capaz de:

- Verificar el correcto funcionamiento de un entorno local basado en Ollama y Open WebUI.
- Ejecutar consultas básicas utilizando un modelo de lenguaje.
- Reconocer la influencia del prompt sobre la calidad de las respuestas obtenidas.
- Identificar un problema real susceptible de ser apoyado mediante Inteligencia Artificial.
- Definir el alcance inicial del Proyecto Integrador.
- Elaborar el primer documento que formará parte del Portafolio del Proyecto Integrador.

---

## 2.4 Relación con el Manual del Participante

Este laboratorio aplica los contenidos desarrollados en el **Capítulo 1** del Manual del Participante.

Durante dicho capítulo se revisaron los conceptos fundamentales relacionados con la Inteligencia Artificial Generativa Local, los modelos de lenguaje, los prompts y el enfoque metodológico del taller.

En este laboratorio esos conocimientos se trasladan a un contexto práctico mediante la instalación del entorno de trabajo, la interacción inicial con un modelo de lenguaje y el comienzo del Proyecto Integrador.

No se pretende profundizar nuevamente en los aspectos conceptuales, sino ponerlos en práctica mediante actividades guiadas que servirán de base para el resto del curso.

---

## 2.5 Tiempo estimado

Duración total del laboratorio:

**100 minutos**

Distribución sugerida:

| Actividad | Tiempo aproximado |
|-----------|------------------:|
| Presentación del laboratorio | 10 minutos |
| Verificación del entorno | 20 minutos |
| Exploración del modelo | 20 minutos |
| Primeros prompts | 20 minutos |
| Inicio del Proyecto Integrador | 25 minutos |
| Reflexión y cierre | 5 minutos |

La distribución podrá ajustarse de acuerdo con el ritmo de trabajo de los participantes.

---

## 2.6 Recursos necesarios

### Hardware

- Computador personal con sistema operativo Windows 10 u 11.
- Procesador compatible con la ejecución de modelos locales.
- Memoria RAM suficiente para ejecutar el modelo seleccionado.
- Espacio disponible en disco para almacenar modelos de lenguaje.

### Software

- Navegador web actualizado.
- Permisos suficientes para instalar aplicaciones en el computador.
- Acceso al Manual Técnico para realizar la instalación y configuración de Ollama y Open WebUI.

### Archivos

Durante este laboratorio no se requiere documentación adicional.

Todos los documentos del Proyecto Integrador serán elaborados progresivamente durante el taller.

### Accesos requeridos

- Acceso local al computador.
- Conexión a Internet únicamente cuando sea necesaria la descarga inicial de modelos o actualizaciones.

---

## 2.7 Conocimientos previos

Antes de comenzar este laboratorio se espera que el participante:

- haya revisado el Capítulo 1 del Manual del Participante;
- comprenda el concepto general de Inteligencia Artificial Generativa;
- conozca el propósito de un modelo de lenguaje;
- comprenda qué es un prompt;
- posea conocimientos básicos sobre navegación web y administración de archivos en Windows.

No se requiere experiencia previa en programación ni en el desarrollo de asistentes inteligentes.

---

# 3. Antes de comenzar

## Lista de verificación

Antes de iniciar las actividades del laboratorio confirme que dispone de los siguientes elementos.

| Verificación                                                                | Estado |
| --------------------------------------------------------------------------- | :----: |
| Computador operativo                                                        |   □    |
| Conexión a Internet disponible para las instalaciones y descargas iniciales |   □    |
| Espacio disponible en disco                                                 |   □    |
| Permisos para instalar aplicaciones                                         |   □    |
| Navegador actualizado                                                       |   □    |
| Acceso al Manual Técnico                                                    |   □    |

En caso de que alguno de estos elementos no se encuentre disponible, solicite apoyo al docente antes de continuar.

---

## 💡 Consejo del instructor

Durante este primer laboratorio no intente construir el asistente definitivo.

El objetivo consiste en comprender cómo interactúan los modelos de lenguaje y comenzar a identificar oportunidades de aplicación dentro de su propio contexto profesional.

Un buen Proyecto Integrador comienza con una correcta definición del problema y no con la selección de una herramienta tecnológica.

---

## ⚠️ Error frecuente

Uno de los errores más habituales consiste en dedicar la mayor parte del tiempo a experimentar con el modelo de lenguaje y postergar la definición del problema que será abordado durante el Proyecto Integrador.

Recuerde que el asistente inteligente será diseñado para resolver un problema específico.

Mientras más clara sea la definición inicial del problema, más sencillo resultará construir una solución útil durante los laboratorios siguientes.

---

## Objetivo del laboratorio

**Preparar un entorno local de Inteligencia Artificial completamente operativo e identificar el problema que dará origen al Proyecto Integrador, estableciendo las bases para el desarrollo del asistente inteligente durante el resto del taller.**

---

### 📁 Producto que comenzará a construirse

Al finalizar este laboratorio comenzará la elaboración del:

**Documento 1. Definición del problema y alcance del Proyecto Integrador**

Este documento será el primer componente del Portafolio que se desarrollará progresivamente durante los laboratorios.

---

**Fin de la Parte 1 del Laboratorio 1**

> La **Parte 2** desarrollará el inicio del laboratorio guiado, incluyendo las primeras actividades prácticas: verificación del entorno, exploración del modelo de lenguaje y construcción de los primeros prompts, siguiendo la estructura metodológica aprobada para el Cuaderno de Laboratorios.

# 4. Desarrollo del laboratorio guiado

En esta sección comenzará el trabajo práctico del laboratorio.

El objetivo consiste en verificar que el entorno local de Inteligencia Artificial funciona correctamente, comprender el comportamiento inicial del modelo de lenguaje y experimentar con distintos tipos de *prompts*.

A diferencia de otros talleres donde las actividades consisten únicamente en seguir una secuencia de instrucciones, en este laboratorio se espera que observe cuidadosamente el comportamiento del modelo, registre sus resultados y analice las diferencias obtenidas en cada interacción.

Recuerde que el propósito no consiste únicamente en "hacer funcionar" una herramienta.

El verdadero objetivo es comenzar a comprender cómo los modelos de lenguaje interpretan instrucciones y cómo esa interacción influirá posteriormente en el diseño del asistente inteligente del Proyecto Integrador.

---

# Actividad 1
# Verificación del entorno de trabajo

## Objetivo

Instalar y comprobar el funcionamiento de Ollama, Open WebUI y el modelo de lenguaje que será utilizado durante el taller.

---

## Contexto

Antes de construir cualquier solución basada en Inteligencia Artificial resulta indispensable asegurar que el entorno de trabajo se encuentra completamente operativo.

En proyectos reales, una gran cantidad de problemas se origina por configuraciones incompletas, servicios detenidos o modelos incorrectamente instalados.

Por ello, esta primera actividad tiene como finalidad validar el funcionamiento del entorno antes de desarrollar nuevas tareas.

Esta práctica reduce significativamente los problemas posteriores y permite concentrar el trabajo en el diseño de soluciones y no en la resolución de dificultades técnicas.

---

## Procedimiento

### Paso 0. Instalar y configurar el entorno

Utilizando el **Manual Técnico**, realice los procedimientos correspondientes a:

- instalación y verificación de Ollama;
- descarga del modelo recomendado para el taller;
- instalación y primera ejecución de Open WebUI;
- conexión de Open WebUI con Ollama.

Una vez completados estos procedimientos, continúe con la verificación funcional descrita a continuación.

### Paso 1

Inicie el servicio de Ollama.

Espere algunos segundos hasta que el servicio quede completamente disponible.

Si el servicio ya se encuentra en ejecución, verifique que continúa operativo.

---

### Paso 2

Abra Open WebUI desde el navegador.

Confirme que la interfaz gráfica carga correctamente.

Verifique que el modelo de lenguaje previamente instalado aparece disponible para ser utilizado.

---

### Paso 3

Seleccione el modelo correspondiente.

Envíe un mensaje simple como el siguiente:

> Hola. ¿Puedes confirmar que estás funcionando correctamente?

Espere la respuesta del modelo.

---

### Paso 4

Realice una segunda consulta.

Por ejemplo:

> Resume en tres líneas qué es la Inteligencia Artificial Generativa.

Observe:

- velocidad de respuesta;
- claridad;
- formato de salida;
- idioma utilizado.

---

### Paso 5

Compruebe que puede iniciar nuevas conversaciones sin inconvenientes.

---

## Evidencias

Al finalizar esta actividad conserve las siguientes evidencias:

- captura de pantalla de Open WebUI funcionando;
- nombre del modelo utilizado;
- fecha y hora de la verificación.

Estas evidencias podrán incorporarse posteriormente al Portafolio del Proyecto Integrador.

---

## 📝 Registro del participante

**Modelo utilizado**

______________________________________________________

**Versión (si está disponible)**

______________________________________________________

**Tiempo aproximado de respuesta**

______________________________________________________

**Observaciones**

______________________________________________________

______________________________________________________

______________________________________________________

---

## ✅ Checkpoint

Antes de continuar verifique que:

- □ Ollama se encuentra operativo.
- □ Open WebUI responde correctamente.
- □ El modelo genera respuestas.
- □ Puede iniciar nuevas conversaciones.
- □ Las evidencias fueron registradas.

Si alguno de estos elementos no se cumple, solicite apoyo al docente antes de continuar.

---

## 🔍 Deténgase y analice

Responda brevemente.

1. ¿Qué diferencia observa entre utilizar un modelo local y utilizar un servicio disponible en Internet?

______________________________________________________

______________________________________________________

2. ¿Qué ventajas podría ofrecer un modelo local dentro de una organización?

______________________________________________________

______________________________________________________

---

# Actividad 2
# Exploración del modelo de lenguaje

## Objetivo

Reconocer las capacidades generales de un modelo de lenguaje mediante consultas abiertas relacionadas con distintos ámbitos del conocimiento.

---

## Contexto

Antes de diseñar un asistente inteligente resulta conveniente conocer cómo responde un modelo de lenguaje frente a distintos tipos de preguntas.

Esta exploración permitirá comprender que los modelos pueden generar textos, resumir información, organizar ideas, proponer alternativas y apoyar múltiples procesos organizacionales.

Sin embargo, también permitirá observar que la calidad de las respuestas depende en gran medida de la forma en que se plantea cada consulta.

---

## Procedimiento

Realice las siguientes consultas.

Después de cada respuesta, léala cuidadosamente antes de continuar.

---

### Consulta 1

> ¿Qué es la Inteligencia Artificial Generativa?

---

### Consulta 2

> Explique qué es un modelo de lenguaje utilizando un ejemplo sencillo.

---

### Consulta 3

> Indique tres aplicaciones de la Inteligencia Artificial dentro de mi disciplina profesional.

Si el modelo necesita mayor contexto, especifique brevemente su área de trabajo.

---

### Consulta 4

> ¿Qué tareas repetitivas podrían automatizarse mediante Inteligencia Artificial dentro de una organización?

---

### Consulta 5

Realice una consulta libre relacionada con su actividad profesional.

---

## Evidencias

Registre:

- la consulta realizada;
- la respuesta obtenida;
- observaciones relevantes.

---

## 📝 Registro del participante

| Consulta | ¿La respuesta fue útil? | Observaciones |
|-----------|------------------------|---------------|
| 1 | □ Sí □ Parcial □ No | |
| 2 | □ Sí □ Parcial □ No | |
| 3 | □ Sí □ Parcial □ No | |
| 4 | □ Sí □ Parcial □ No | |
| 5 | □ Sí □ Parcial □ No | |

---

## 💡 Consejo del instructor

No evalúe únicamente si la respuesta es correcta.

Observe también:

- el nivel de detalle;
- la estructura del texto;
- la claridad de la explicación;
- si el modelo solicita información adicional.

Estas observaciones serán muy útiles cuando comience a diseñar su propio asistente inteligente.

---

## ⚠️ Error frecuente

Muchos usuarios interpretan la primera respuesta del modelo como definitiva.

En realidad, los modelos de lenguaje permiten refinar progresivamente las respuestas mediante nuevas instrucciones o proporcionando contexto adicional.

Aprender a dialogar con el modelo constituye una de las competencias más importantes que desarrollará durante este taller.

---

## ✅ Checkpoint

Antes de continuar asegúrese de haber:

- □ realizado todas las consultas propuestas;
- □ registrado las respuestas;
- □ identificado fortalezas del modelo;
- □ identificado limitaciones iniciales.

---

## 🔍 Reflexión breve

1. ¿Cuál de las respuestas obtuvo mejores resultados?

______________________________________________________

2. ¿Cuál considera que fue menos útil?

______________________________________________________

3. ¿Qué información adicional habría permitido mejorar las respuestas obtenidas?

______________________________________________________

______________________________________________________

---

### 📁 Portafolio

Aunque esta actividad no genera un documento formal para el Proyecto Integrador, las observaciones registradas permitirán fundamentar posteriormente las decisiones adoptadas durante el diseño del asistente inteligente.

---

**Fin de la Parte 2 del Laboratorio 1**

> La **Parte 3** continuará con las actividades de construcción y comparación de *prompts*, donde el participante analizará cómo pequeñas modificaciones en las instrucciones influyen en la calidad, precisión y utilidad de las respuestas generadas por el modelo de lenguaje. Esta etapa servirá como puente entre la exploración inicial y el diseño del asistente inteligente que comenzará en el Proyecto Integrador.

# Actividad 3
# Construcción y evaluación de prompts

## Objetivo

Comprender cómo la calidad de las respuestas generadas por un modelo de lenguaje depende directamente de la forma en que se redactan las instrucciones entregadas al sistema.

---

## Contexto

Una de las competencias más importantes en el desarrollo de soluciones basadas en Inteligencia Artificial Generativa consiste en formular instrucciones claras, específicas y contextualizadas.

Estas instrucciones reciben el nombre de **prompts**.

Aunque un modelo de lenguaje posee una gran capacidad para generar información, la calidad de sus respuestas depende, en gran medida, de la información que recibe como entrada.

Un prompt bien construido puede producir respuestas claras, pertinentes y útiles.

Por el contrario, un prompt ambiguo o incompleto suele generar respuestas demasiado generales, poco precisas o alejadas del objetivo buscado.

Durante esta actividad experimentará con distintos tipos de prompts para observar cómo pequeñas modificaciones en las instrucciones producen cambios importantes en la calidad de las respuestas.

---

## Procedimiento

Trabajará utilizando un mismo tema, pero modificando progresivamente la forma de formular las instrucciones.

Después de cada consulta compare los resultados obtenidos.

---

# Caso de estudio

Utilizará como tema de referencia:

**La Inteligencia Artificial aplicada al apoyo de procesos organizacionales.**

---

## Prompt 1
### Prompt abierto

Ingrese la siguiente instrucción.

> Explique cómo puede utilizarse la Inteligencia Artificial en una organización.

Lea cuidadosamente la respuesta obtenida.

---

## Prompt 2
### Prompt específico

Ingrese ahora la siguiente instrucción.

> Explique cómo la Inteligencia Artificial puede apoyar la gestión de solicitudes internas en una institución educativa. Limite su respuesta a un máximo de 200 palabras.

Compare la respuesta con la obtenida anteriormente.

---

## Prompt 3
### Prompt con rol

Ingrese ahora:

> Actúe como consultor especializado en transformación digital y proponga tres formas de utilizar Inteligencia Artificial para mejorar la atención de estudiantes en una institución de educación superior.

Observe cómo cambia el estilo de la respuesta.

---

## Prompt 4
### Prompt con formato definido

Ingrese:

> Actúe como consultor especializado en transformación digital.
>
> Explique tres aplicaciones de la Inteligencia Artificial para mejorar la atención de estudiantes.
>
> Presente la respuesta utilizando una tabla con las columnas:
>
> • Problema
>
> • Solución propuesta
>
> • Beneficio esperado

Observe la estructura generada.

---

## Prompt 5
### Prompt contextualizado

Finalmente, construya un prompt relacionado con el problema que desea abordar en su Proyecto Integrador.

Incluya información como:

- contexto;
- organización;
- usuarios;
- objetivo;
- resultado esperado.

No se preocupe si el prompt aún no es perfecto.

Será optimizado durante los próximos laboratorios.

> ¿Qué diferencias observa entre el Prompt 1 y el Prompt 5?

---

## Evidencias

Conserve las respuestas correspondientes a los cinco prompts.

Estas evidencias permitirán observar la evolución de su capacidad para interactuar con modelos de lenguaje.

---

## 📝 Registro del participante

### Prompt 1

**¿Qué aspectos positivos observa?**

______________________________________________________

______________________________________________________

**¿Qué podría mejorarse?**

______________________________________________________

______________________________________________________

---

### Prompt 2

**¿Qué diferencias observa respecto al Prompt 1?**

______________________________________________________

______________________________________________________

---

### Prompt 3

**¿Cómo influyó el rol asignado al modelo?**

______________________________________________________

______________________________________________________

---

### Prompt 4

**¿Qué ventajas ofrece solicitar un formato específico?**

______________________________________________________

______________________________________________________

---

### Prompt 5

**Escriba aquí el primer borrador del prompt asociado a su Proyecto Integrador.**

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

---

## 💡 Consejo del instructor

Los mejores prompts no buscan impresionar al modelo.

Buscan reducir la ambigüedad.

Mientras más contexto proporcione, mayor será la probabilidad de obtener respuestas útiles y consistentes.

Piense que está entregando instrucciones a un colaborador que desconoce completamente su organización.

---

## ⚠️ Error frecuente

Muchos usuarios creen que existe un único prompt perfecto.

En realidad, el diseño de prompts constituye un proceso iterativo.

Es completamente normal modificar un mismo prompt varias veces hasta obtener una respuesta satisfactoria.

Durante el resto del taller continuará refinando los prompts utilizados por su asistente inteligente.

---

## ✅ Checkpoint

Antes de continuar asegúrese de que:

- □ construyó los cinco prompts;
- □ comparó las respuestas;
- □ registró sus observaciones;
- □ redactó el primer borrador del prompt del Proyecto Integrador.

---

## 🔍 Deténgase y analice

Reflexione sobre las siguientes preguntas.

### 1.

¿Cuál de los cinco prompts produjo la respuesta más útil?

¿Por qué?

______________________________________________________

______________________________________________________

______________________________________________________

---

### 2.

¿Qué información adicional habría permitido mejorar aún más las respuestas?

______________________________________________________

______________________________________________________

______________________________________________________

---

### 3.

¿Considera que un modelo de lenguaje necesita conocer el contexto del problema para entregar mejores resultados?

Fundamente.

______________________________________________________

______________________________________________________

______________________________________________________

---

# Actividad 4
# Análisis de los resultados obtenidos

## Objetivo

Reflexionar sobre el comportamiento observado durante las primeras interacciones con el modelo de lenguaje e identificar aprendizajes que serán utilizados durante el diseño del asistente inteligente.

---

## Contexto

El propósito de este laboratorio nunca fue aprender a formular prompts aislados.

Lo realmente importante consiste en comprender que la interacción entre una persona y un modelo de lenguaje constituye un proceso de comunicación.

Así como ocurre entre personas, la calidad de la comunicación depende de la claridad de las instrucciones, del contexto proporcionado y de la precisión con que se expresa el objetivo buscado.

Las observaciones realizadas durante esta actividad servirán como base para diseñar posteriormente el prompt principal del asistente inteligente del Proyecto Integrador.

---

## Actividad

Complete la siguiente tabla.

| Aspecto analizado | Observaciones |
|-------------------|---------------|
| ¿Qué tipo de prompt obtuvo mejores resultados? | |
| ¿Qué tipo de prompt produjo respuestas demasiado generales? | |
| ¿Qué información adicional mejoró las respuestas? | |
| ¿Qué dificultades encontró durante la interacción? | |
| ¿Qué aprendió sobre el funcionamiento del modelo? | |

---

## 📁 Portafolio

Conserve las observaciones realizadas durante esta actividad.

Aunque todavía no forman parte de un documento formal del Proyecto Integrador, constituirán un importante insumo para justificar posteriormente las decisiones adoptadas durante el diseño del asistente inteligente.

---

## 💡 Consejo del instructor

No intente memorizar prompts.

Procure comprender los principios que permiten construir instrucciones claras y contextualizadas.

Las herramientas cambiarán con el tiempo.

La capacidad para comunicarse eficazmente con un modelo de lenguaje seguirá siendo una competencia valiosa independientemente de la tecnología utilizada.

---

## ✅ Checkpoint

Antes de finalizar la parte guiada del laboratorio verifique que:

- □ exploró el comportamiento del modelo;
- □ comparó distintos tipos de prompts;
- □ redactó un primer prompt relacionado con su proyecto;
- □ registró todas sus observaciones.

Con estas actividades concluye la etapa de exploración del entorno local de Inteligencia Artificial.

En la siguiente parte del laboratorio comenzará formalmente el **Proyecto Integrador**, definiendo el problema y el alcance de la solución que desarrollará durante el resto del taller.

---

**Fin de la Parte 3 del Laboratorio 1**

# 5. Proyecto Integrador

Hasta este momento del laboratorio ha explorado el funcionamiento de un modelo de lenguaje, ha comprobado que el entorno local se encuentra operativo y ha experimentado con distintos tipos de *prompts*.

A partir de esta sección comenzará formalmente el desarrollo del **Proyecto Integrador**, actividad que acompañará todo el taller y que culminará con la presentación de una solución basada en Inteligencia Artificial Generativa con ejecución local del modelo, integrada con herramientas del ecosistema Google Workspace.

El éxito del proyecto dependerá, en gran medida, de la calidad de la definición inicial del problema.

Por esta razón, durante este laboratorio no se diseñará todavía el asistente inteligente.

Primero se definirá con precisión el problema que se desea resolver.

---

# 5.1 Objetivo

Identificar y documentar un problema real perteneciente al contexto profesional del participante, definiendo su alcance, sus usuarios y el valor esperado de una solución basada en Inteligencia Artificial Generativa.

---

# ¿Por qué comenzar por el problema?

Existe una tendencia natural a pensar primero en la tecnología.

Sin embargo, los proyectos exitosos comienzan exactamente al revés.

Primero se comprende una necesidad.

Luego se analiza el proceso.

Posteriormente se identifican oportunidades de mejora.

Recién entonces se diseña una solución tecnológica.

Este taller seguirá exactamente esa metodología.

Durante todos los laboratorios posteriores, cada decisión técnica dependerá de la definición realizada hoy.

Por ello, dedicar tiempo a comprender correctamente el problema constituye una de las inversiones más importantes de todo el Proyecto Integrador.

---

## 💡 Consejo del instructor

No intente buscar un problema complejo.

En la mayoría de los casos, las mejores soluciones nacen de procesos cotidianos que consumen tiempo, requieren análisis de información o presentan tareas repetitivas susceptibles de ser apoyadas mediante Inteligencia Artificial.

---

# 5.2 Desarrollo

## Actividad 1
### Identificación del problema

Piense en su contexto profesional.

Puede tratarse de una empresa, institución pública, establecimiento educacional, centro de salud o cualquier otra organización donde exista un proceso que pueda beneficiarse mediante el uso de Inteligencia Artificial.

Al seleccionar el problema considere los siguientes criterios.

### El problema debería:

- presentarse con cierta frecuencia;
- requerir análisis de información;
- consumir tiempo significativo;
- involucrar tareas repetitivas;
- requerir apoyo para la toma de decisiones;
- generar valor si parte del proceso pudiera automatizarse.

---

### Algunos ejemplos

**Educación**

- Clasificación de consultas estudiantiles.
- Apoyo a la retroalimentación académica.
- Organización de solicitudes administrativas.

---

**Salud**

- Clasificación preliminar de solicitudes.
- Organización documental.
- Apoyo administrativo.

---

**Industria**

- Clasificación de reportes.
- Resumen de incidencias.
- Organización de registros.

---

**Administración pública**

- Respuesta a consultas frecuentes.
- Clasificación de documentos.
- Apoyo a la gestión interna.

Estos ejemplos son únicamente referenciales.

El Proyecto Integrador debe responder preferentemente a una necesidad perteneciente al propio contexto laboral del participante.

---

## 📝 Registro del participante

### Nombre del problema

______________________________________________________

---

### Organización

______________________________________________________

---

### Área donde ocurre

______________________________________________________

---

### Personas involucradas

______________________________________________________

______________________________________________________

---

### Describa brevemente el problema

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

---

# Actividad 2
# Análisis del proceso actual

## Objetivo

Comprender cómo se desarrolla actualmente el proceso antes de proponer cualquier solución tecnológica.

---

## Contexto

Una de las causas más frecuentes del fracaso de proyectos tecnológicos consiste en intentar automatizar procesos que nunca fueron comprendidos completamente.

Antes de diseñar un asistente inteligente resulta indispensable conocer cómo trabajan actualmente las personas involucradas.

---

## Actividad

Complete la siguiente tabla.

| Pregunta | Respuesta |
|----------|-----------|
| ¿Cómo comienza el proceso? | |
| ¿Qué información recibe? | |
| ¿Quién participa? | |
| ¿Qué decisiones deben tomarse? | |
| ¿Qué dificultades aparecen? | |
| ¿Qué tareas consumen más tiempo? | |
| ¿Cómo finaliza el proceso? | |

---

## 🔍 Deténgase y analice

Responda.

¿Está intentando resolver un problema real o simplemente utilizar Inteligencia Artificial porque la tecnología está disponible?

______________________________________________________

______________________________________________________

______________________________________________________

---

# Actividad 3
# Definición del alcance

## Objetivo

Delimitar claramente lo que el Proyecto Integrador resolverá y aquello que permanecerá fuera de su alcance.

---

## Contexto

Uno de los errores más frecuentes durante el desarrollo de proyectos consiste en intentar resolver demasiados problemas simultáneamente.

Para evitar esta situación, todo proyecto debe definir claramente sus límites.

---

## Actividad

Complete la siguiente ficha.

| Elemento | Descripción |
|----------|-------------|
| Problema que resolverá el asistente | |
| Usuarios principales | |
| Información que utilizará | |
| Resultado esperado | |
| Beneficio esperado | |
| Actividades que NO realizará el asistente | |

---

## ⚠️ Error frecuente

Un asistente inteligente no necesita resolver todo un proceso organizacional.

En la mayoría de los casos resulta mucho más efectivo automatizar correctamente una única actividad que intentar reemplazar completamente el trabajo de las personas.

---

# Actividad 4
# Justificación del proyecto

Explique brevemente por qué considera que la Inteligencia Artificial puede aportar valor al problema seleccionado.

Considere aspectos como:

- reducción de tiempos;
- apoyo al análisis;
- organización de información;
- mejora en la calidad de las respuestas;
- disminución de tareas repetitivas.

---

## 📝 Registro del participante

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

---

# 5.3 Documento generado

Al finalizar este laboratorio deberá disponer del primer documento oficial del Proyecto Integrador.

---

# Documento 1

## Definición del problema y alcance

El documento deberá contener como mínimo:

- nombre del proyecto;
- organización;
- descripción del problema;
- usuarios involucrados;
- análisis del proceso actual;
- alcance de la solución;
- beneficios esperados;
- justificación del proyecto.

Este documento constituirá la base para el diseño del asistente inteligente durante el Laboratorio 2.

---

## 📁 Portafolio

Conserve este documento.

Será incorporado directamente al **Portafolio del Proyecto Integrador**.

No deberá volver a elaborarlo.

En los próximos laboratorio únicamente será complementado con nuevos documentos.

---

# 5.4 Espacio de trabajo

Utilice las siguientes páginas para desarrollar el Documento 1.

---

## Nombre del Proyecto Integrador

______________________________________________________

---

## Problema

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

---

## Objetivo del asistente inteligente

______________________________________________________

______________________________________________________

______________________________________________________

---

## Usuarios

______________________________________________________

______________________________________________________

---

## Beneficios esperados

______________________________________________________

______________________________________________________

______________________________________________________

---

## Alcance

______________________________________________________

______________________________________________________

______________________________________________________

---

## Limitaciones identificadas

______________________________________________________

______________________________________________________

______________________________________________________

---

# 5.5 Autoevaluación del Proyecto

Antes de finalizar esta sección verifique que:

| Aspecto | Sí | Parcial | No |
|----------|:--:|:--------:|:--:|
| El problema corresponde a una situación real | □ | □ | □ |
| El problema fue descrito claramente | □ | □ | □ |
| Se identificaron los usuarios | □ | □ | □ |
| El alcance quedó definido | □ | □ | □ |
| Se justificó el uso de IA | □ | □ | □ |
| El Documento 1 quedó iniciado | □ | □ | □ |

---

## 💡 Consejo del instructor

No busque un problema "perfecto".

Durante los próximos laboratorios tendrá múltiples oportunidades para mejorar esta definición.

Lo importante es que el problema sea auténtico, tenga sentido dentro de su contexto profesional y permita construir una solución que aporte valor a la organización.

---

**Fin de la Parte 4 del Laboratorio 1**

> En la **Parte 5** se desarrollará el cierre del laboratorio, incluyendo la síntesis de los aprendizajes, la autoevaluación, los entregables, la preparación para el Laboratorio 2 y la vinculación con la siguiente etapa del Proyecto Integrador.

# 6. Cierre del laboratorio

Ha finalizado el primer laboratorio del taller.

Durante este laboratorio no sólo preparó el entorno tecnológico que utilizará durante el resto del curso, sino que también inició el desarrollo del Proyecto Integrador que lo acompañará durante los laboratorios.

Aunque gran parte del trabajo realizado estuvo relacionado con la exploración de un modelo de lenguaje, el principal resultado de este laboratorio no corresponde a la instalación de Ollama o Open WebUI.

El aprendizaje más importante consiste en haber comprendido que una solución basada en Inteligencia Artificial siempre debe comenzar por una adecuada definición del problema que se desea resolver.

En los próximos laboratorios el entorno tecnológico permanecerá prácticamente sin modificaciones.

Lo que evolucionará será el Proyecto Integrador.

Cada laboratorio agregará nuevos componentes hasta construir una solución completa basada en Inteligencia Artificial Generativa Local integrada con herramientas del ecosistema Google Workspace.

---

# 6.1 Síntesis

Durante este laboratorio desarrolló las siguientes actividades:

- verificó el funcionamiento del entorno local de Inteligencia Artificial;
- exploró las capacidades generales de un modelo de lenguaje;
- experimentó con distintos tipos de prompts;
- analizó cómo la formulación de las instrucciones, el contexto, el rol y el formato solicitado influyen en las respuestas generadas;
- identificó un problema perteneciente a su contexto profesional;
- definió el alcance inicial del Proyecto Integrador;
- comenzó la elaboración del Documento 1 del Portafolio.

Observe que la mayor parte del trabajo realizado no estuvo orientado a la tecnología.

El énfasis se centró en comprender un problema organizacional y analizar de qué manera la Inteligencia Artificial puede transformarse en una herramienta de apoyo para su resolución.

Este enfoque acompañará todas las actividades del taller.

---

# 6.2 ¿Qué aprendí hoy?

Dedique algunos minutos a responder las siguientes preguntas.

No existen respuestas correctas o incorrectas.

El objetivo consiste en reflexionar sobre el proceso de aprendizaje desarrollado durante este primer laboratorio.

---

## ¿Qué fue lo más importante que aprendió hoy?

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

---

## ¿Qué actividad le resultó más desafiante?

______________________________________________________

______________________________________________________

______________________________________________________

---

## ¿Qué aspecto le gustaría profundizar durante los próximos laboratorios?

______________________________________________________

______________________________________________________

______________________________________________________

---

## ¿Cómo cree que la Inteligencia Artificial podría aportar valor dentro de su organización?

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

---

# 6.3 Autoevaluación

Evalúe el nivel de logro alcanzado durante este laboratorio.

| Criterio | Logrado | Parcial | Pendiente |
|----------|:-------:|:--------:|:---------:|
| Verifiqué correctamente el entorno de trabajo. | □ | □ | □ |
| Comprendí el funcionamiento básico de un modelo de lenguaje. | □ | □ | □ |
| Construí distintos tipos de prompts. | □ | □ | □ |
| Analicé las diferencias entre las respuestas obtenidas. | □ | □ | □ |
| Seleccioné un problema para el Proyecto Integrador. | □ | □ | □ |
| Definí el alcance inicial del proyecto. | □ | □ | □ |
| Inicié el Documento 1 del Portafolio. | □ | □ | □ |

---

## 🔍 Reflexión profesional

Después de esta primera experiencia, responda la siguiente pregunta.

> **¿Considera que la Inteligencia Artificial debería reemplazar completamente las tareas desarrolladas por las personas dentro de una organización?**

Fundamente su respuesta.

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

Esta reflexión será retomada durante el Laboratorio 6, cuando se analicen aspectos relacionados con el uso responsable de la Inteligencia Artificial.

---

# 6.4 Lista de entregables

Al finalizar este laboratorio deberá entregar o conservar los siguientes productos.

| Producto | Estado |
|----------|:------:|
| Evidencia del funcionamiento de Ollama y Open WebUI | □ |
| Registro de observaciones sobre el comportamiento del modelo | □ |
| Comparación de los distintos prompts utilizados | □ |
| Primer borrador del prompt asociado al Proyecto Integrador | □ |
| Documento 1. Definición del problema y alcance | □ |

Todos estos elementos deberán conservarse, ya que serán utilizados durante los siguientes laboratorios.

---

# 📁 Portafolio

Después de finalizar este laboratorio, el Portafolio del Proyecto Integrador debería contener el siguiente documento.

## Documento 1

**Definición del problema y alcance del Proyecto Integrador**

Este documento constituye el punto de partida de todo el trabajo que desarrollará durante el taller.

No deberá volver a elaborarlo.

En los próximos laboratorios será complementado mediante nuevos documentos que describirán el diseño, validación, integración y consolidación de la solución.

---

# 6.5 Preparación del Laboratorio 2

Antes de asistir al siguiente laboratorio asegúrese de que:

- el entorno local continúa funcionando correctamente;
- conserva el Documento 1 del Proyecto Integrador;
- dispone del modelo de lenguaje instalado;
- tiene disponible el primer borrador del prompt elaborado durante este laboratorio;
- ha revisado el Capítulo 2 del Manual del Participante.

Durante el siguiente laboratorio comenzará el diseño del asistente inteligente especializado.

Toda la información desarrollada en este laboratorio será utilizada nuevamente.

---

## 💡 Recomendación del instructor

Si durante los próximos días identifica nuevas ideas relacionadas con el problema seleccionado, incorpórelas al Documento 1.

Es completamente normal que la definición inicial evolucione antes de comenzar el diseño del asistente.

La mejora continua constituye una práctica habitual durante el desarrollo de proyectos tecnológicos.

---

# 6.6 Vinculación con el Laboratorio 2

El trabajo realizado durante este primer laboratorio constituye el punto de partida del Proyecto Integrador.

En el Laboratorio 2 utilizará el problema definido hoy para comenzar el diseño del asistente inteligente especializado.

Durante ese laboratorio aprenderá a:

- definir el propósito del asistente;
- establecer su rol;
- delimitar su contexto de actuación;
- definir restricciones;
- construir el **System Prompt**;
- construir y probar una configuración inicial del asistente.

Observe que ninguna de estas actividades sería posible sin haber definido previamente el problema que el asistente intentará resolver.

Por esta razón, el Documento 1 elaborado durante este laboratorio representa uno de los componentes más importantes del Portafolio del Proyecto Integrador.

---

# Mensaje final

Ha completado el primer paso del recorrido formativo.

Aunque todavía no ha construido un asistente inteligente, ya dispone de dos elementos fundamentales para continuar:

- un entorno local de Inteligencia Artificial completamente operativo;
- un problema real que servirá como base para el Proyecto Integrador.

A partir del próximo laboratorio comenzará el diseño de una solución basada en Inteligencia Artificial Generativa Local que evolucionará progresivamente hasta convertirse en un asistente inteligente integrado con herramientas del ecosistema Google Workspace.

Cada laboratorio agregará un nuevo componente al Proyecto Integrador y un nuevo documento al Portafolio.

Al finalizar el taller dispondrá no sólo de una solución funcional, sino también de la evidencia completa del proceso seguido para diseñarla, validarla, integrarla y presentarla profesionalmente.

---

# Fin del Laboratorio 1

## Producto obtenido para el Portafolio

**Documento 1. Definición del problema y alcance del Proyecto Integrador**

## Próximo laboratorio

**Laboratorio 2. Diseño de un asistente inteligente utilizando un caso guiado**

**Proyecto Integrador**

**Documento 2. Diseño del asistente inteligente especializado**

---

