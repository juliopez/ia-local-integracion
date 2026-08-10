# Cuaderno de Laboratorios

# Laboratorio 3

# Validación y optimización del asistente inteligente mediante casos de prueba

**Capítulo asociado:** Capítulo 3. Validación y optimización de asistentes inteligentes

**Duración estimada:** 100 minutos

**Proyecto Integrador:** Documento 3. Validación y optimización del asistente inteligente

---

# Índice

1. Presentación del laboratorio
2. Información general
3. Antes de comenzar

> **Nota:** El desarrollo del laboratorio, el Proyecto Integrador y el cierre se incorporarán en las siguientes entregas.

---

# 1. Presentación del laboratorio

## ¿Qué aprenderá en este laboratorio?

Hasta este momento del taller ha construido y configurado un asistente inteligente especializado.

Sin embargo, diseñar un asistente no garantiza que sus respuestas sean correctas, consistentes o útiles para los usuarios.

Al igual que cualquier otra solución tecnológica, un asistente basado en Inteligencia Artificial debe ser sometido a un proceso sistemático de validación antes de ser utilizado en un contexto real.

Durante este laboratorio aprenderá a evaluar críticamente el comportamiento de su asistente mediante casos de prueba diseñados específicamente para comprobar si cumple el propósito para el cual fue creado.

Más que buscar respuestas "correctas", el objetivo será analizar aspectos como:

- coherencia de las respuestas;
- precisión de la información generada;
- cumplimiento del propósito definido;
- respeto por las restricciones establecidas;
- necesidad de mejorar el System Prompt.

Esta etapa constituye una práctica habitual en el desarrollo profesional de soluciones basadas en Inteligencia Artificial.

Los asistentes inteligentes rara vez alcanzan un comportamiento óptimo desde su configuración inicial.

Normalmente requieren múltiples ciclos de prueba, análisis y optimización antes de alcanzar un comportamiento estable.

Por esta razón, durante este laboratorio aprenderá una metodología de validación que posteriormente podrá aplicar en cualquier proyecto basado en modelos de lenguaje.

Inicialmente trabajará sobre un caso guiado, donde todos los participantes evaluarán un mismo asistente utilizando una pauta común.

Posteriormente aplicará esa misma metodología a su propio Proyecto Integrador, validando el asistente diseñado durante el Laboratorio 2.

Al finalizar este laboratorio dispondrá de un asistente optimizado y de un registro documentado de las modificaciones realizadas.

---

# 2. Información general

## 2.1 Propósito

Validar y optimizar un asistente inteligente mediante una metodología basada en casos de prueba, identificando fortalezas, debilidades y oportunidades de mejora para incrementar la calidad de sus respuestas.

---

## 2.2 Competencias

Durante este laboratorio desarrollará las siguientes competencias:

- Diseñar casos de prueba para asistentes inteligentes.
- Evaluar críticamente las respuestas generadas por un modelo de lenguaje.
- Detectar inconsistencias y oportunidades de mejora.
- Optimizar prompts mediante procesos iterativos.
- Documentar técnicamente las modificaciones realizadas durante la validación.
- Justificar las decisiones adoptadas durante la optimización del asistente.

---

## 2.3 Resultados de aprendizaje

Al finalizar este laboratorio será capaz de:

- Diseñar un conjunto de casos de prueba representativos.
- Aplicar criterios objetivos para evaluar el desempeño de un asistente inteligente.
- Identificar problemas asociados al diseño y comportamiento del asistente.
- Optimizar el comportamiento del asistente mediante ajustes sucesivos.
- Elaborar el Documento 3 del Portafolio del Proyecto Integrador.

---

## 2.4 Relación con el Manual del Participante

Este laboratorio pone en práctica los contenidos desarrollados en el **Capítulo 3** del Manual del Participante.

Durante dicho capítulo se revisó el proceso de validación y optimización de asistentes inteligentes, destacando la importancia de construir casos de prueba, analizar las respuestas obtenidas y documentar sistemáticamente las mejoras implementadas.

En este laboratorio esos conceptos serán aplicados mediante la evaluación de un caso guiado y, posteriormente, mediante la validación del asistente desarrollado en el Proyecto Integrador.

---

## 2.5 Tiempo estimado

**Duración total:** 100 minutos

Distribución sugerida:

| Actividad | Tiempo aproximado |
|-----------|------------------:|
| Presentación del laboratorio | 10 minutos |
| Caso guiado de validación | 30 minutos |
| Optimización del prompt | 20 minutos |
| Proyecto Integrador | 35 minutos |
| Reflexión y cierre | 5 minutos |

La distribución podrá ajustarse según el ritmo de trabajo del grupo.

---

## 2.6 Recursos necesarios

### Hardware

- Computador personal.

### Software

- Ollama operativo.
- Open WebUI.
- Modelo de lenguaje instalado.

### Archivos

- Documento 2 del Proyecto Integrador.
- Manual del Participante (Capítulo 3).

### Accesos requeridos

No se requiere conexión permanente a Internet.

Todo el trabajo se desarrollará utilizando el entorno local configurado en los laboratorios anteriores.

---

## 2.7 Conocimientos previos

Antes de comenzar este laboratorio se espera que el participante:

- haya completado el Laboratorio 2;
- disponga del Documento 2 del Proyecto Integrador;
- comprenda la estructura de un asistente inteligente;
- conozca el funcionamiento básico de Ollama y Open WebUI;
- haya revisado el Capítulo 3 del Manual del Participante.

---

# 3. Antes de comenzar

## Lista de verificación

Antes de iniciar confirme que dispone de los siguientes elementos.

| Verificación                         | Estado |
|--------------|:------:|
| Ollama operativo                     | □ |
| Open WebUI funcionando               | □ |
| Modelo disponible                    | □ |
| Documento 2 del Proyecto Integrador  | □ |
| System Prompt del asistente          | □ |
| Manual del Participante (Capítulo 3) | □ |

---

## 💡 Consejo del instructor

Evite evaluar su asistente con una única pregunta.

La calidad de un asistente se determina observando su comportamiento frente a múltiples situaciones y distintos tipos de consultas.

Incorporar casos de prueba variados y representativos permite obtener una evaluación más completa del comportamiento del asistente.

---

## ⚠️ Error frecuente

Muchos desarrolladores modifican inmediatamente el prompt después de observar una respuesta incorrecta.

Antes de realizar cambios, procure identificar la causa del problema.

No todos los errores se solucionan agregando nuevas instrucciones.

En ocasiones basta con mejorar el contexto, redefinir una restricción o ajustar el propósito del asistente.

---

## Objetivo del laboratorio

**Validar sistemáticamente el comportamiento del asistente inteligente mediante casos de prueba representativos, identificando oportunidades de mejora y documentando las optimizaciones realizadas antes de avanzar hacia la etapa de integración.**

---

### 📁 Producto que comenzará a construirse

Al finalizar este laboratorio elaborará el:

**Documento 3. Validación y optimización del asistente inteligente**

Este documento registrará los casos de prueba ejecutados, los resultados obtenidos, las mejoras implementadas y el **System Prompt optimizado**.

---

### 📈 Progreso del Proyecto Integrador

```
Documento 1  ██████████  ✔
Documento 2  ██████████  ✔
Documento 3  ███░░░░░░░  En desarrollo
Documento 4  ░░░░░░░░░░
Documento 5  ░░░░░░░░░░
Documento 6  ░░░░░░░░░░
```

---

**Fin de la Parte 1 del Laboratorio 3**

> La **Parte 2** desarrollará un caso guiado de validación donde todos los participantes aprenderán a construir casos de prueba, evaluar objetivamente las respuestas del asistente e identificar oportunidades de optimización antes de aplicar la metodología a su propio Proyecto Integrador.

# 4. Desarrollo del laboratorio guiado

En este laboratorio aprenderá una metodología sistemática para validar asistentes inteligentes.

Hasta el momento ha diseñado una solución basada en Inteligencia Artificial. Sin embargo, todavía no sabe si realmente responde de la forma esperada.

En proyectos reales, antes de incorporar un asistente a un proceso operativo resulta recomendable someterlo a pruebas que permitan evaluar su comportamiento en distintos escenarios.

Una configuración funcional no implica que la solución se encuentre suficientemente validada para su utilización en un contexto real.

Durante esta primera parte del laboratorio trabajará con un caso común para todos los participantes.

El propósito no consiste en comprobar si el modelo "sabe responder", sino en aprender cómo evaluar objetivamente un asistente inteligente.

Una vez comprendida la metodología, aplicará exactamente el mismo procedimiento al asistente desarrollado en su Proyecto Integrador.

---

# Caso guiado

## Asistente Académico

Utilizará el mismo asistente diseñado durante el Laboratorio 2.

Recuerde que dicho asistente fue construido para:

- responder consultas académicas;
- orientar a estudiantes;
- entregar información clara;
- respetar restricciones previamente definidas.

Durante este laboratorio evaluaremos si realmente cumple esas condiciones.

---

# Actividad 1

# Diseño de casos de prueba

## Objetivo

Construir un conjunto de casos de prueba representativos que permitan evaluar objetivamente el comportamiento del asistente inteligente.

---

## Contexto

Una validación adecuada requiere planificar previamente qué situaciones serán evaluadas.

Si solamente se realizan preguntas al azar, resulta muy difícil determinar si el asistente realmente cumple su propósito.

Por esta razón, los casos de prueba deben representar situaciones que los usuarios enfrentarían en un contexto real.

Cada caso debe responder a una pregunta sencilla:

> **¿Qué comportamiento espero observar en el asistente frente a esta situación?**

---

## Procedimiento

Analice el propósito del asistente académico y diseñe cinco consultas representativas.

Considere diferentes niveles de dificultad.

Por ejemplo:

- preguntas frecuentes;
- consultas incompletas;
- solicitudes ambiguas;
- preguntas fuera del contexto del asistente;
- situaciones donde el asistente debería reconocer que no dispone de información suficiente.

---

## 📝 Registro del participante

| Caso | Consulta | ¿Qué espera que responda el asistente? |
|------|----------|-----------------------------------------|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |

---

## 💡 Consejo del instructor

Un buen caso de prueba no busca "hacer fallar" al asistente.

Busca comprobar si el comportamiento observado coincide con el comportamiento esperado.

---

## ⚠️ Error frecuente

Diseñar únicamente consultas fáciles.

En proyectos reales también deben evaluarse situaciones poco habituales o ambiguas.

Estas pruebas suelen entregar la información más valiosa para optimizar posteriormente el asistente.

---

## ✅ Checkpoint

Antes de continuar confirme que:

- □ diseñó cinco casos de prueba;
- □ representan situaciones diferentes;
- □ cada uno posee un resultado esperado claramente definido.

---

# Actividad 2

# Ejecución de los casos de prueba

## Objetivo

Evaluar el comportamiento del asistente frente a los casos definidos anteriormente.

---

## Contexto

Ahora el asistente será sometido a las pruebas diseñadas.

Durante esta actividad no se realizarán modificaciones al prompt.

El objetivo consiste únicamente en observar el comportamiento del modelo y registrar los resultados obtenidos.

Recuerde actuar como un evaluador.

Evite corregir inmediatamente los errores detectados.

---

## Procedimiento

Ejecute uno por uno los cinco casos de prueba.

Después de cada consulta registre cuidadosamente los resultados.

---

## 📝 Registro del participante

| Caso | ¿La respuesta fue adecuada? | Observaciones |
|------|:---------------------------:|---------------|
| 1 | □ Sí □ Parcial □ No | |
| 2 | □ Sí □ Parcial □ No | |
| 3 | □ Sí □ Parcial □ No | |
| 4 | □ Sí □ Parcial □ No | |
| 5 | □ Sí □ Parcial □ No | |

---

## Aspectos que debería observar

Durante la evaluación considere aspectos como:

- precisión;
- coherencia;
- claridad;
- organización;
- cumplimiento del propósito;
- respeto por las restricciones definidas;
- reconocimiento de incertidumbre cuando corresponda.

---

## 🔍 Deténgase y analice

No piense todavía en modificar el prompt.

Responda primero.

¿Qué patrones observa en las respuestas?

¿Existe algún tipo de consulta donde el asistente obtiene sistemáticamente mejores resultados?

______________________________________________________

______________________________________________________

______________________________________________________

---

## 💡 Consejo del instructor

No evalúe únicamente si la respuesta "parece correcta".

Pregúntese también:

> **¿Es la respuesta que realmente necesita el usuario?**

Esta diferencia resulta fundamental durante el diseño de soluciones basadas en Inteligencia Artificial.

---

## ✅ Checkpoint

Antes de continuar confirme que:

- □ ejecutó todos los casos de prueba;
- □ registró los resultados;
- □ identificó patrones de comportamiento.

---

# Actividad 3

# Identificación de oportunidades de mejora

## Objetivo

Analizar los resultados obtenidos durante las pruebas e identificar los aspectos del asistente que requieren optimización.

---

## Contexto

La validación no termina cuando se detectan errores.

El verdadero propósito consiste en comprender por qué esos errores ocurrieron.

En esta etapa comenzará el análisis de las posibles causas.

Más adelante esas observaciones permitirán optimizar el System Prompt.

---

## Procedimiento

Revise nuevamente todas las respuestas obtenidas.

Complete la siguiente tabla.

---

## 📝 Registro del participante

| Aspecto evaluado | Observaciones |
|------------------|---------------|
| Respuestas demasiado generales | |
| Respuestas incompletas | |
| Información poco clara | |
| Problemas de formato | |
| Incumplimiento de restricciones | |
| Otros aspectos relevantes | |

---

## 🔍 Reflexión breve

Responda.

¿Considera que los problemas detectados se deben principalmente a:

- una definición poco clara del propósito;
- un contexto insuficiente;
- restricciones poco precisas;
- instrucciones ambiguas;
- otro factor?

Fundamente.

______________________________________________________

______________________________________________________

______________________________________________________

---

## 📁 Portafolio

Las observaciones registradas durante esta actividad constituirán la base para justificar las modificaciones que realizará posteriormente al System Prompt.

No elimine esta información.

Será incorporada al Documento 3 del Proyecto Integrador.

---

## 💡 Consejo del instructor

Una buena optimización no consiste en agregar más instrucciones.

Consiste en identificar exactamente cuál es la causa del comportamiento observado.

Mientras más preciso sea el diagnóstico, más sencilla será la mejora del asistente.

---

## ✅ Checkpoint general

Antes de finalizar esta sección confirme que:

- □ diseñó casos de prueba representativos;
- □ ejecutó todas las pruebas;
- □ registró sistemáticamente los resultados;
- □ identificó oportunidades concretas de mejora.

Con estas actividades concluye la primera etapa del proceso de validación.

En la siguiente sección comenzará la optimización del asistente mediante la modificación controlada del prompt y la comparación entre la versión inicial y la versión mejorada.

---

**Fin de la Parte 2 del Laboratorio 3**

# Actividad 4

# Optimización del System Prompt

## Objetivo

Modificar de manera controlada el prompt del asistente inteligente utilizando la información obtenida durante la etapa de validación.

---

## Contexto

Después de ejecutar los casos de prueba ya dispone de información suficiente para comenzar la optimización del asistente.

Es importante comprender que esta actividad no consiste en escribir un prompt completamente nuevo.

La optimización busca introducir mejoras puntuales, justificadas y medibles.

En proyectos reales, las modificaciones realizadas sobre un asistente deben responder siempre a evidencia obtenida durante las pruebas.

Modificar el prompt "porque parece mejor" dificulta posteriormente comprender qué cambios realmente mejoraron el comportamiento del modelo.

Por ello, durante esta actividad cada modificación deberá estar respaldada por un problema identificado durante la validación.

---

## Procedimiento

Revise las observaciones registradas durante la actividad anterior.

Seleccione las tres oportunidades de mejora más importantes.

Posteriormente modifique el prompt únicamente en aquellos aspectos que considere necesarios.

No agregue instrucciones innecesarias.

Procure mantener un diseño claro, consistente y fácil de comprender.

---

## 📝 Registro del participante

### Problema identificado Nº1

______________________________________________________

### Modificación realizada

______________________________________________________

### Justificación

______________________________________________________

---

### Problema identificado Nº2

______________________________________________________

### Modificación realizada

______________________________________________________

### Justificación

______________________________________________________

---

### Problema identificado Nº3

______________________________________________________

### Modificación realizada

______________________________________________________

### Justificación

______________________________________________________

---

## 💡 Consejo del instructor

Realice pocos cambios cada vez.

Cuando se modifican demasiados elementos simultáneamente resulta difícil identificar cuál de ellos produjo una mejora real.

La optimización incremental constituye una práctica ampliamente utilizada en proyectos de desarrollo de software e Inteligencia Artificial.

---

## ⚠️ Error frecuente

Agregar numerosas restricciones pensando que ello mejorará automáticamente las respuestas.

En muchos casos ocurre exactamente lo contrario.

Prompts excesivamente largos pueden producir respuestas más rígidas, repetitivas o contradictorias.

---

## ✅ Checkpoint

Antes de continuar confirme que:

- □ identificó los principales problemas;
- □ cada modificación posee una justificación;
- □ evitó incorporar instrucciones innecesarias.

---

# Actividad 5

# Comparación de resultados

## Objetivo

Comparar el comportamiento del asistente antes y después de las modificaciones realizadas.

---

## Contexto

Una optimización solamente puede considerarse exitosa cuando produce una mejora observable.

Por ello resulta indispensable comparar el comportamiento del asistente antes y después de las modificaciones.

De esta manera será posible determinar objetivamente si las modificaciones realmente incrementaron la calidad de las respuestas.

---

## Procedimiento

Ejecute nuevamente los cinco casos de prueba utilizando el prompt optimizado.

Posteriormente compare ambas versiones.

---

## 📝 Registro del participante

| Caso | Resultado inicial | Resultado posterior al ajuste | ¿Mejoró?  |
| ---- | ----------------- | ----------------------------- | :-------: |
| 1    |                   |                               | □ Sí □ No |
| 2    |                   |                               | □ Sí □ No |
| 3    |                   |                               | □ Sí □ No |
| 4    |                   |                               | □ Sí □ No |
| 5    |                   |                               | □ Sí □ No |

---

## Aspectos para comparar

Durante la comparación considere:

- precisión de las respuestas;
- coherencia;
- claridad;
- cumplimiento del propósito;
- respeto por las restricciones;
- facilidad de comprensión para el usuario.

---

## 🔍 Deténgase y analice

Responda.

¿Cuáles modificaciones produjeron una mejora evidente?

______________________________________________________

______________________________________________________

______________________________________________________

---

¿Existe alguna modificación que no haya generado el resultado esperado?

______________________________________________________

______________________________________________________

______________________________________________________

---

## 💡 Consejo del instructor

La optimización no siempre produce mejoras inmediatas.

Es completamente normal realizar varias iteraciones antes de obtener un comportamiento estable.

---

## ✅ Checkpoint

Antes de continuar confirme que:

- □ ejecutó nuevamente todos los casos de prueba;
- □ comparó los resultados antes y después de los ajustes;
- □ identificó mejoras concretas.

---

# Actividad 6

# Reflexión sobre el proceso de validación

## Objetivo

Analizar críticamente el proceso de validación y reconocer la importancia de las pruebas sistemáticas durante el desarrollo de asistentes inteligentes.

---

## Contexto

Una de las principales diferencias entre un usuario ocasional de Inteligencia Artificial y un profesional que desarrolla soluciones basadas en IA consiste en la manera en que evalúa los resultados.

Mientras un usuario suele aceptar la primera respuesta generada por el modelo, un desarrollador valida, compara, analiza y mejora sistemáticamente el comportamiento del asistente.

Este enfoque permite construir soluciones considerablemente más confiables y útiles para las organizaciones.

---

## Actividad

Responda las siguientes preguntas.

### ¿Qué aprendizaje considera más importante obtenido durante este proceso de validación?

______________________________________________________

______________________________________________________

______________________________________________________

---

### ¿Qué aspecto del asistente requirió mayores ajustes?

______________________________________________________

______________________________________________________

______________________________________________________

---

### ¿Considera que la validación debería formar parte de todos los proyectos basados en Inteligencia Artificial?

¿Por qué?

______________________________________________________

______________________________________________________

______________________________________________________

---

## 📁 Portafolio

Las respuestas registradas durante esta actividad permitirán fundamentar posteriormente las decisiones adoptadas durante la optimización del asistente.

Conserve esta información.

Será incorporada al Documento 3 del Proyecto Integrador.

---

## 💡 Consejo del instructor

Documente siempre las modificaciones realizadas.

En proyectos reales resulta tan importante conocer el estado final del asistente como comprender el proceso seguido para llegar a él.

La documentación constituye una evidencia fundamental del trabajo profesional.

---

## 📊 Resumen de la validación

Complete la siguiente síntesis.

| Aspecto | Resultado |
|----------|-----------|
| Casos de prueba ejecutados | |
| Problemas detectados | |
| Mejoras implementadas | |
| Casos donde el desempeño mejoró | |
| Aspectos pendientes de optimización | |

---

## ✅ Checkpoint general

Antes de finalizar la etapa guiada confirme que:

- □ optimizó el System Prompt;
- □ comparó los resultados obtenidos antes y después de las modificaciones;
- □ documentó todas las modificaciones;
- □ registró los resultados de la validación;
- □ identificó aspectos pendientes de mejora.

Con estas actividades concluye el **caso guiado de validación y optimización**.

En la siguiente parte del laboratorio aplicará exactamente la misma metodología a su **Proyecto Integrador**, validando y optimizando el asistente inteligente diseñado durante el Laboratorio 2.

---

**Fin de la Parte 3 del Laboratorio 3**

# 5. Proyecto Integrador

Durante el caso guiado aprendió una metodología para validar y optimizar asistentes inteligentes utilizando casos de prueba.

Ahora aplicará exactamente el mismo procedimiento al asistente desarrollado para su Proyecto Integrador.

A diferencia de los laboratorios anteriores, este laboratorio representa el primer proceso formal de aseguramiento de la calidad de la solución.

No se trata únicamente de comprobar si el asistente responde.

El propósito consiste en verificar si responde correctamente, de manera consistente y alineada con el problema que pretende resolver.

Al finalizar esta sección habrá optimizado su asistente y documentado las mejoras implementadas.

Ese registro constituirá el **Documento 3 del Portafolio del Proyecto Integrador**.

---

# 5.1 Objetivo

Validar y optimizar el asistente inteligente diseñado durante el Laboratorio 2 mediante una metodología basada en casos de prueba, documentando sistemáticamente los resultados obtenidos y las mejoras implementadas.

---

# Antes de comenzar

Recupere el siguiente material elaborado durante los laboratorios anteriores:

- Documento 1. Definición del problema.
- Documento 2. Diseño del asistente inteligente.
- System Prompt inicial.

Revise cuidadosamente la definición del problema.

Recuerde que todos los casos de prueba deberán construirse considerando el propósito original del asistente.

---

## 💡 Consejo del instructor

No modifique todavía el Documento 2.

Primero valide el comportamiento del asistente.

Las modificaciones deberán realizarse únicamente después de disponer de evidencia suficiente.

---

# Actividad 1

# Diseño de casos de prueba

## Objetivo

Diseñar un conjunto de pruebas que permitan comprobar objetivamente el comportamiento del asistente inteligente.

---

## Actividad

Diseñe al menos cinco consultas representativas para su asistente.

Procure incorporar distintos tipos de situaciones.

Por ejemplo:

- consultas frecuentes;
- consultas incompletas;
- solicitudes ambiguas;
- preguntas fuera del contexto;
- situaciones donde el asistente debería reconocer que no posee información suficiente.

---

## 📝 Registro del participante

| Caso | Consulta | Resultado esperado |
|------|----------|-------------------|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |

---

## 🔍 Deténgase y analice

Antes de ejecutar las pruebas pregúntese:

> Si el asistente respondiera exactamente como espero,

¿qué características debería presentar esa respuesta?

Anote sus observaciones.

______________________________________________________

______________________________________________________

______________________________________________________

---

# Actividad 2

# Ejecución de las pruebas

## Objetivo

Evaluar el comportamiento del asistente frente a los casos definidos anteriormente.

---

## Actividad

Ejecute cada consulta utilizando el System Prompt elaborado durante el Laboratorio 2.

Después de cada interacción registre cuidadosamente los resultados.

---

## 📝 Registro del participante

| Caso | ¿Respuesta adecuada? | Observaciones |
|------|:--------------------:|---------------|
| 1 | □ Sí □ Parcial □ No | |
| 2 | □ Sí □ Parcial □ No | |
| 3 | □ Sí □ Parcial □ No | |
| 4 | □ Sí □ Parcial □ No | |
| 5 | □ Sí □ Parcial □ No | |

---

## Aspectos que deberían evaluarse

Considere aspectos como:

- cumplimiento del propósito;
- claridad;
- precisión;
- organización;
- consistencia;
- respeto por las restricciones;
- reconocimiento de incertidumbre cuando corresponda.

---

## 📁 Evidencias

Conserve:

- capturas de pantalla relevantes;
- respuestas representativas;
- observaciones realizadas durante la evaluación.

Estas evidencias podrán incorporarse posteriormente al Portafolio.

---

# Actividad 3

# Diagnóstico del asistente

## Objetivo

Identificar las principales fortalezas y debilidades observadas durante la validación.

---

## Actividad

Complete la siguiente matriz.

| Aspecto | Observaciones |
|----------|---------------|
| Fortalezas observadas | |
| Debilidades detectadas | |
| Respuestas inconsistentes | |
| Restricciones incumplidas | |
| Aspectos que requieren optimización | |

---

## 🔍 Reflexión

¿Cuál considera que fue el principal problema observado durante la validación?

______________________________________________________

______________________________________________________

______________________________________________________

---

# Actividad 4

# Optimización del prompt

## Objetivo

Implementar mejoras controladas sobre el System Prompt.

---

## Actividad

Revise nuevamente el prompt.

Realice únicamente aquellas modificaciones que estén justificadas por los resultados obtenidos durante las pruebas.

Registre cuidadosamente cada cambio.

---

## 📝 Registro del participante

| Modificación | Motivo | Resultado esperado |
|--------------|--------|-------------------|
| | | |
| | | |
| | | |

---

## 💡 Consejo del instructor

Evite realizar demasiados cambios simultáneamente.

Cada modificación debería responder a un problema claramente identificado durante la validación.

---

# Actividad 5

# Segunda ejecución de pruebas

## Objetivo

Comprobar si las modificaciones implementadas mejoraron el comportamiento del asistente.

---

## Actividad

Ejecute nuevamente los mismos cinco casos de prueba.

Posteriormente compare los resultados obtenidos antes y después de las modificaciones.

---

## 📝 Registro del participante

| Caso | Antes | Después | ¿Mejoró? |
|------|--------|----------|:---------:|
| 1 | | | □ Sí □ No |
| 2 | | | □ Sí □ No |
| 3 | | | □ Sí □ No |
| 4 | | | □ Sí □ No |
| 5 | | | □ Sí □ No |

---

## 🔍 Deténgase y analice

¿Qué modificación produjo la mejora más importante?

______________________________________________________

______________________________________________________

______________________________________________________

---

¿Existe algún aspecto que todavía requiere optimización?

______________________________________________________

______________________________________________________

______________________________________________________

---

# Actividad 6

# Reflexión sobre el proceso de mejora

## Objetivo

Analizar el proceso de optimización realizado.

---

## Actividad

Responda.

### ¿Qué aprendió sobre el comportamiento de su asistente?

______________________________________________________

______________________________________________________

______________________________________________________

---

### ¿Qué cambios considera necesarios como parte de una mejora futura?

______________________________________________________

______________________________________________________

______________________________________________________

---

### ¿Cómo justificaría técnicamente las modificaciones realizadas?

______________________________________________________

______________________________________________________

______________________________________________________

---

# 5.2 Documento generado

Al finalizar este laboratorio deberá disponer del siguiente documento.

---

# Documento 3

## Validación y optimización del asistente inteligente

Este documento deberá contener, como mínimo:

- descripción de los casos de prueba;
- resultados obtenidos;
- problemas detectados;
- modificaciones realizadas;
- comparación de resultados antes y después de las modificaciones;
- conclusiones del proceso de validación.

Este documento servirá como respaldo técnico para demostrar que el asistente fue sometido a un proceso sistemático de mejora antes de ser integrado con otras herramientas.

---

## 📁 Portafolio

Incorpore el Documento 3 al Portafolio del Proyecto Integrador.

Al finalizar este laboratorio su Portafolio deberá contener:

- Documento 1. Definición del problema.
- Documento 2. Diseño del asistente.
- Documento 3. Validación y optimización.

---

# 5.3 Autoevaluación del Proyecto

Antes de continuar confirme que:

| Aspecto | Sí | Parcial | No |
|----------|:--:|:--------:|:--:|
| Diseñé casos de prueba representativos. | □ | □ | □ |
| Ejecuté sistemáticamente todas las pruebas. | □ | □ | □ |
| Registré los resultados obtenidos. | □ | □ | □ |
| Identifiqué oportunidades de mejora. | □ | □ | □ |
| Optimicé el prompt utilizando evidencia. | □ | □ | □ |
| Comparé ambas versiones del asistente. | □ | □ | □ |
| Incorporé el Documento 3 al Portafolio. | □ | □ | □ |

---

## 💡 Consejo final

La validación no representa el final del proceso de mejora.

En proyectos reales, los asistentes inteligentes evolucionan continuamente mediante nuevas pruebas, retroalimentación de los usuarios y ajustes sucesivos.

Lo importante es desarrollar una metodología que permita mejorar la solución de forma sistemática y fundamentada.

---

### 📈 Progreso del Proyecto Integrador

```
Documento 1  ██████████  ✔
Documento 2  ██████████  ✔
Documento 3  ██████████  ✔
Documento 4  ░░░░░░░░░░
Documento 5  ░░░░░░░░░░
Documento 6  ░░░░░░░░░░
```

---

**Fin de la Parte 4 del Laboratorio 3**

> En la **Parte 5** realizará el cierre del laboratorio, sintetizará los principales aprendizajes obtenidos durante el proceso de validación, verificará los productos incorporados al Portafolio y preparará el trabajo que desarrollará en el **Laboratorio 4**, donde el asistente inteligente será integrado con herramientas del ecosistema Google Workspace mediante Google Apps Script.

# 6. Cierre del laboratorio

Durante este laboratorio completó la primera etapa formal de aseguramiento de la calidad de su asistente inteligente.

Hasta el laboratorio anterior disponía de un diseño metodológico y de un primer prompt funcional.

A partir de las actividades desarrolladas hoy, ese diseño fue sometido a un proceso sistemático de validación, permitiéndole identificar fortalezas, detectar debilidades y realizar mejoras fundamentadas en evidencia.

Este enfoque constituye una diferencia importante respecto del uso cotidiano de herramientas de Inteligencia Artificial.

Mientras un usuario ocasional suele aceptar la primera respuesta obtenida, un desarrollador de soluciones basadas en IA analiza críticamente el comportamiento del sistema, documenta los resultados y mejora progresivamente el asistente mediante procesos iterativos.

Ésta es precisamente la metodología que ha comenzado a desarrollar durante este laboratorio.

---

# 6.1 Síntesis

Durante este laboratorio desarrolló las siguientes actividades:

- diseñó casos de prueba representativos;
- ejecutó pruebas sobre el asistente inteligente;
- analizó objetivamente los resultados obtenidos;
- identificó fortalezas y debilidades;
- optimizó el System Prompt;
- comparó distintas versiones del asistente;
- documentó el proceso de mejora;
- elaboró el Documento 3 del Proyecto Integrador.

Más allá de la optimización del prompt, el principal aprendizaje consiste en comprender que la calidad de un asistente inteligente depende de un proceso permanente de evaluación y mejora continua.

La validación deja de ser una actividad puntual para transformarse en una práctica habitual dentro del desarrollo de soluciones basadas en Inteligencia Artificial.

---

# 6.2 ¿Qué aprendí hoy?

Dedique algunos minutos a reflexionar sobre el proceso desarrollado.

---

## ¿Qué aspecto del proceso de validación considera más importante?

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

---

## ¿Qué tipo de prueba permitió detectar los problemas más relevantes?

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

---

## ¿Qué modificación produjo la mejora más significativa en su asistente?

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

---

## ¿Qué nuevas mejoras le gustaría implementar en el futuro?

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

---

# 6.3 Autoevaluación

Evalúe el nivel de logro alcanzado durante este laboratorio.

| Criterio | Logrado | Parcial | Pendiente |
|----------|:-------:|:--------:|:---------:|
| Diseñé casos de prueba representativos. | □ | □ | □ |
| Evalué objetivamente el comportamiento del asistente. | □ | □ | □ |
| Registré sistemáticamente los resultados obtenidos. | □ | □ | □ |
| Identifiqué oportunidades de mejora. | □ | □ | □ |
| Optimicé el prompt utilizando evidencia. | □ | □ | □ |
| Comparé ambas versiones del asistente. | □ | □ | □ |
| Documenté el proceso de validación. | □ | □ | □ |
| Completé el Documento 3 del Proyecto Integrador. | □ | □ | □ |

---

## 🔍 Reflexión profesional

Responda la siguiente pregunta.

> **¿Por qué considera que un asistente inteligente debería ser validado antes de integrarse a un proceso organizacional?**

En su respuesta considere aspectos relacionados con:

- confiabilidad;
- calidad;
- riesgos;
- experiencia del usuario;
- mejora continua.

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

---

## 🌐 Uso responsable de la Inteligencia Artificial

Durante este laboratorio comprobó que un modelo de lenguaje puede generar respuestas muy útiles, pero también cometer errores, interpretar incorrectamente una consulta o responder con un nivel de certeza mayor al que realmente posee.

Por esta razón, antes de incorporar un asistente inteligente a un proceso organizacional resulta indispensable considerar aspectos relacionados con el uso responsable de la Inteligencia Artificial.

Reflexione sobre las siguientes preguntas.

### ¿Qué consecuencias podría generar una respuesta incorrecta de su asistente?

______________________________________________________

______________________________________________________

______________________________________________________

---

### ¿Qué tipo de decisiones deberían seguir siendo supervisadas por una persona?

______________________________________________________

______________________________________________________

______________________________________________________

---

### ¿Qué mecanismos podrían implementarse para reducir errores o sesgos durante el uso del asistente?

______________________________________________________

______________________________________________________

______________________________________________________

---

> **Importante**
>
> Un asistente inteligente debe entenderse como una herramienta de apoyo para el análisis y la toma de decisiones. En aquellos procesos donde las respuestas puedan afectar a personas, organizaciones o derechos, siempre será necesaria la supervisión y el juicio profesional de un responsable humano.

---

# 6.4 Lista de entregables

Al finalizar este laboratorio deberá disponer de los siguientes productos.

| Producto                            | Estado |
| ----------------------------------- | :----: |
| Casos de prueba diseñados           |   □    |
| Registro de resultados              |   □    |
| Diagnóstico del asistente           |   □    |
| System Prompt optimizado            |   □    |
| Comparación entre versiones         |   □    |
| Documento 3 del Proyecto Integrador |   □    |

Conserve toda la documentación generada.

Será utilizada durante el proceso de integración del Laboratorio 4.

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

Observe que su proyecto ya cuenta con tres componentes fundamentales:

1. El problema identificado.
2. El diseño metodológico del asistente.
3. La evidencia de su proceso de validación y mejora.

Estos documentos serán la base para la siguiente etapa del taller: la integración del asistente con herramientas del ecosistema Google Workspace.

---

# 6.5 Preparación del Laboratorio 4

Antes de asistir al siguiente laboratorio asegúrese de que:

- conserva los Documentos 1, 2 y 3 del Proyecto Integrador;
- mantiene operativo el entorno local de IA;
- dispone del system prompt optimizado;
- ha revisado el Capítulo 4 del Manual del Participante.

En el próximo laboratorio el asistente dejará de funcionar como una herramienta aislada y comenzará a formar parte de un flujo integrado con herramientas del ecosistema Google Workspace.

Para ello se utilizarán Google Apps Script y un Web App para gestionar el intercambio de información, mientras que `puente_local.py` permitirá conectar este flujo con el modelo ejecutado localmente mediante Ollama.

---

## 💡 Recomendación del instructor

Antes del próximo laboratorio piense en cómo le gustaría que el asistente recibiera información y entregara sus respuestas.

Por ejemplo:

- mediante un formulario;
- a partir de una hoja de cálculo;
- utilizando el contenido de un correo electrónico;
- procesando un documento;
- apoyando un flujo de trabajo específico.

No será necesario implementar estas ideas todavía.

Sin embargo, comenzar a visualizar la integración facilitará el trabajo que desarrollará durante el siguiente laboratorio.

---

# 6.6 Vinculación con el Laboratorio 4

Hasta ahora el asistente ha funcionado de manera independiente.

Durante el Laboratorio 4 aprenderá a integrarlo con un proceso digital sencillo utilizando herramientas del ecosistema Google Workspace.

El objetivo no será aprender programación avanzada.

La finalidad consistirá en comprender cómo un asistente inteligente puede formar parte de un flujo de trabajo organizacional.

Durante ese laboratorio aprenderá a:

- capturar información mediante herramientas del ecosistema Google Workspace;
- estructurar la información necesaria para su posterior procesamiento;
- preparar los componentes necesarios para integrar el asistente con el flujo digital;
- comprender el papel de Google Apps Script dentro de la solución;
- analizar las ventajas y limitaciones de este tipo de integración.

Con ello, el Proyecto Integrador comenzará a transformarse en una solución funcional que interactúa con aplicaciones utilizadas habitualmente en organizaciones.

---

# Mensaje final

El desarrollo de soluciones basadas en Inteligencia Artificial no termina cuando un asistente responde correctamente a una consulta.

La verdadera calidad de una solución se demuestra cuando ha sido sometida a un proceso sistemático de validación, mejora y documentación.

Durante este laboratorio ha dado ese paso.

A partir de ahora su asistente no es solamente una idea bien diseñada.

Es una solución que ha comenzado a ser evaluada y perfeccionada mediante criterios objetivos.

En el siguiente laboratorio iniciará una nueva etapa: integrar esa solución con herramientas digitales utilizadas en procesos reales, acercando el Proyecto Integrador a un escenario de aplicación profesional.

---

# Fin del Laboratorio 3

## Producto obtenido para el Portafolio

**Documento 3. Validación y optimización del asistente inteligente**

## Próximo laboratorio

**Laboratorio 4. Integración del asistente inteligente con Google Workspace mediante Google Apps Script**

**Proyecto Integrador**

**Documento 4. Integración del asistente con un proceso digital**

---

### 📈 Progreso del Proyecto Integrador

```
Documento 1  ██████████  ✔
Documento 2  ██████████  ✔
Documento 3  ██████████  ✔
Documento 4  ███░░░░░░░  Próximo laboratorio
Documento 5  ░░░░░░░░░░
Documento 6  ░░░░░░░░░░
```


