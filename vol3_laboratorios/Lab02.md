# Cuaderno de Laboratorios

# Laboratorio 2

# Diseño de un asistente inteligente utilizando un caso guiado

**Capítulo asociado:** Capítulo 2. Diseño de asistentes inteligentes

**Duración estimada:** 100 minutos

**Proyecto Integrador:** Documento 2. Diseño del asistente inteligente especializado

---

# Índice

1. Presentación del laboratorio
2. Información general
3. Antes de comenzar

> **Nota:** El desarrollo del laboratorio, el Proyecto Integrador y el cierre se incorporarán en las siguientes entregas.

---

# 1. Presentación del laboratorio

## ¿Qué aprenderá en este laboratorio?

Durante el laboratorio anterior preparó el entorno local de Inteligencia Artificial y definió el problema que será abordado mediante el Proyecto Integrador.

A partir de este laboratorio comenzará el diseño del asistente inteligente que utilizará durante el resto del taller.

Esta etapa representa uno de los momentos más importantes del proceso de desarrollo, ya que las decisiones adoptadas aquí influirán directamente en el comportamiento del asistente durante las etapas de validación, integración y consolidación.

Diseñar un asistente inteligente implica mucho más que redactar un prompt.

Significa definir con claridad:

- el propósito del asistente;
- el problema que resolverá;
- el tipo de usuarios para quienes fue diseñado;
- el contexto donde operará;
- las restricciones que deberá respetar;
- el tipo de respuestas que deberá generar.

En otras palabras, durante este laboratorio transformará una idea inicial en una especificación funcional que servirá como base para el resto del Proyecto Integrador.

Para facilitar este proceso, el laboratorio comenzará con un caso guiado donde todos los participantes construirán un asistente sencillo siguiendo una metodología común.

Posteriormente, aplicarán la misma metodología al problema definido durante el Laboratorio 1, desarrollando su propio asistente inteligente.

Al finalizar este laboratorio dispondrá de una especificación completa del asistente y de una configuración inicial del **System Prompt** que orientará su comportamiento durante las siguientes etapas del taller.

---

# 2. Información general

## 2.1 Propósito

Diseñar un asistente inteligente especializado mediante una metodología estructurada, definiendo su propósito, contexto, usuarios, restricciones y comportamiento esperado, para posteriormente aplicarlo al Proyecto Integrador.

---

## 2.2 Competencias

Durante este laboratorio desarrollará las siguientes competencias:

- Diseñar asistentes inteligentes orientados a un problema específico.
- Definir el rol y propósito de un asistente basado en IA.
- Establecer el contexto operativo de una solución basada en modelos de lenguaje.
- Elaborar prompts estructurados para asistentes especializados.
- Traducir una necesidad organizacional en una especificación funcional.
- Documentar técnicamente el diseño inicial de un asistente inteligente.

---

## 2.3 Resultados de aprendizaje

Al finalizar este laboratorio será capaz de:

- Explicar los componentes fundamentales de un asistente inteligente.
- Diseñar un asistente utilizando una metodología estructurada.
- Redactar el primer **System Prompt** del asistente.
- Justificar las decisiones adoptadas durante el diseño.
- Elaborar el Documento 2 del Portafolio del Proyecto Integrador.

---

## 2.4 Relación con el Manual del Participante

Este laboratorio pone en práctica los contenidos desarrollados en el **Capítulo 2** del Manual del Participante.

Durante dicho capítulo se revisó la metodología para diseñar asistentes inteligentes, identificando los elementos que determinan su comportamiento, tales como el rol, los objetivos, el contexto, las restricciones y los criterios de funcionamiento.

En este laboratorio esos conceptos serán aplicados mediante el diseño de un asistente guiado y, posteriormente, mediante el desarrollo del asistente correspondiente al Proyecto Integrador.

---

## 2.5 Tiempo estimado

**Duración total:** 100 minutos

Distribución sugerida:

| Actividad                           | Tiempo aproximado |
|-----------|------------------:|
| Presentación del laboratorio        | 10 minutos |
| Caso guiado: diseño de un asistente | 30 minutos |
| Construcción del **System Prompt**  | 20 minutos |
| Proyecto Integrador                 | 35 minutos |
| Reflexión y cierre                  | 5 minutos |

La distribución podrá modificarse según el ritmo de trabajo del grupo.

---

## 2.6 Recursos necesarios

### Hardware

- Computador personal.
- Conexión eléctrica.

### Software

- Ollama operativo.
- Open WebUI.
- Modelo de lenguaje instalado.

### Archivos

- Documento 1 del Proyecto Integrador.
- Manual del Participante (Capítulo 2).

### Accesos requeridos

No se requiere conexión permanente a Internet.

Todo el trabajo se desarrollará utilizando el entorno local preparado durante el laboratorio anterior.

---

## 2.7 Conocimientos previos

Antes de iniciar este laboratorio se espera que el participante:

- haya completado el Laboratorio 1;
- disponga del Documento 1 del Proyecto Integrador;
- comprenda el concepto de prompt;
- conozca el funcionamiento básico de Ollama y Open WebUI;
- haya revisado el Capítulo 2 del Manual del Participante.

---

# 3. Antes de comenzar

## Lista de verificación

Antes de iniciar el laboratorio confirme que dispone de los siguientes elementos.

| Verificación | Estado |
|--------------|:------:|
| Ollama operativo | □ |
| Open WebUI funcionando | □ |
| Modelo disponible | □ |
| Documento 1 del Proyecto Integrador | □ |
| Manual del Participante (Capítulo 2) | □ |

---

## 💡 Consejo del instructor

No intente construir un asistente perfecto durante este laboratorio.

El diseño de asistentes inteligentes es un proceso iterativo.

Durante los próximos laboratorios dispondrá de múltiples oportunidades para validar, ajustar y optimizar el comportamiento del asistente.

Lo importante hoy es construir una primera versión coherente y bien fundamentada.

---

## ⚠️ Error frecuente

Uno de los errores más habituales consiste en diseñar asistentes demasiado generales.

Mientras más específico sea el problema que intenta resolver el asistente, más consistentes y útiles serán las respuestas generadas por el modelo.

Evite crear asistentes cuyo propósito sea "responder cualquier consulta".

Defina claramente su dominio de trabajo.

---

## Objetivo del laboratorio

**Diseñar un asistente inteligente especializado, definiendo su propósito, contexto, restricciones y comportamiento esperado, para iniciar formalmente la construcción de la solución que será desarrollada durante el Proyecto Integrador.**

---

### 📁 Producto que comenzará a construirse

Al finalizar este laboratorio elaborará el:

**Documento 2. Diseño del asistente inteligente especializado**

Este documento describirá las características fundamentales del asistente y constituirá la base para las actividades de validación y optimización que se desarrollarán en el Laboratorio 3.

---

**Fin de la Parte 1 del Laboratorio 2**

> La **Parte 2** desarrollará el caso guiado para el diseño de un asistente inteligente, donde todos los participantes construirán una primera solución utilizando una metodología común antes de aplicar el proceso a su propio Proyecto Integrador.

# 4. Desarrollo del laboratorio guiado

En este laboratorio comenzará el diseño de un asistente inteligente especializado.

Hasta este momento ha identificado el problema que desea resolver. Sin embargo, todavía no existe una solución.

El objetivo de las siguientes actividades consiste en transformar esa necesidad en una especificación funcional capaz de orientar el comportamiento del modelo de lenguaje.

Para ello trabajará inicialmente con un **caso guiado**, común para todos los participantes.

La finalidad de este caso no es construir el asistente definitivo, sino aprender una metodología de diseño que posteriormente aplicará a su propio Proyecto Integrador.

Una vez comprendida la metodología, cada participante diseñará un asistente adaptado a su realidad profesional.

---

# Caso guiado

Durante las siguientes actividades todos los participantes desarrollarán un mismo asistente.

## Asistente para apoyo a consultas académicas

El asistente tendrá como finalidad responder consultas frecuentes relacionadas con procesos académicos de una institución de educación superior.

El asistente deberá:

- responder utilizando lenguaje claro;
- mantener un tono profesional;
- entregar información organizada;
- reconocer cuando no dispone de antecedentes suficientes;
- evitar generar información que no haya sido proporcionada.

Este ejemplo será utilizado únicamente como ejercicio metodológico.

Posteriormente, cada participante diseñará su propio asistente.

---

# Actividad 1

# Definición del propósito del asistente

## Objetivo

Definir claramente cuál será la finalidad del asistente inteligente antes de comenzar su construcción.

---

## Contexto

Todo asistente inteligente existe para cumplir un propósito específico.

Si dicho propósito no se encuentra claramente definido, el modelo tenderá a generar respuestas inconsistentes o demasiado generales.

Por esta razón, el primer paso consiste en responder una pregunta muy sencilla:

> **¿Para qué fue creado este asistente?**

Observe que la pregunta no hace referencia a la tecnología utilizada.

Hace referencia al problema que el asistente ayudará a resolver.

---

## Procedimiento

Lea la siguiente descripción.

> "Una institución recibe diariamente consultas relacionadas con procesos académicos. Muchas de ellas corresponden a preguntas repetitivas que consumen tiempo del personal administrativo."

Ahora responda.

### ¿Cuál debería ser el propósito del asistente?

No piense todavía en el prompt.

Concéntrese únicamente en la finalidad de la solución.

---

## 📝 Registro del participante

**Propósito propuesto**

______________________________________________________

______________________________________________________

______________________________________________________

---

## Discusión guiada

Compare su propuesta con otros participantes.

Reflexione sobre las siguientes preguntas.

- ¿El propósito describe una necesidad real?
- ¿Está claramente delimitado?
- ¿Puede entenderse sin conocer la tecnología utilizada?

---

## 💡 Consejo del instructor

El propósito siempre debería comenzar utilizando un verbo de acción.

Por ejemplo:

- apoyar;
- clasificar;
- organizar;
- orientar;
- resumir;
- analizar.

Evite expresiones demasiado amplias como:

- ayudar en todo;
- responder cualquier consulta;
- resolver cualquier problema.

---

## ⚠️ Error frecuente

Confundir el propósito del asistente con las funcionalidades que ofrecerá.

El propósito responde a la pregunta:

> **¿Para qué existe el asistente?**

Las funcionalidades responderán posteriormente a la pregunta:

> **¿Qué hará el asistente para cumplir ese propósito?**

---

## ✅ Checkpoint

Antes de continuar confirme que:

- □ el propósito se encuentra claramente definido;
- □ describe una necesidad concreta;
- □ puede comprenderse sin conocer detalles técnicos.

---

# Actividad 2

# Definición del rol

## Objetivo

Establecer el rol profesional que asumirá el asistente durante sus interacciones con los usuarios.

---

## Contexto

Los modelos de lenguaje modifican significativamente el estilo de sus respuestas cuando reciben instrucciones relacionadas con el rol que deben desempeñar.

Un mismo modelo puede actuar como:

- docente;
- analista;
- consultor;
- abogado;
- médico;
- especialista técnico.

El rol permite establecer el tipo de lenguaje, el nivel de profundidad y la perspectiva desde la cual responderá el asistente.

---

## Procedimiento

Para el caso guiado considere el siguiente escenario.

El asistente responderá consultas académicas dirigidas a estudiantes.

¿Qué rol debería asumir?

Algunas posibilidades son:

- asistente académico;
- orientador institucional;
- analista de información académica;
- especialista en apoyo estudiantil.

Seleccione la alternativa que considere más adecuada.

Explique su decisión.

---

## 📝 Registro del participante

**Rol seleccionado**

______________________________________________________

---

**Justificación**

______________________________________________________

______________________________________________________

______________________________________________________

---

## 🔍 Deténgase y analice

¿Cambiarían las respuestas del modelo si el rol fuera "Secretario Académico" en lugar de "Asistente Académico"?

¿Por qué?

______________________________________________________

______________________________________________________

______________________________________________________

---

## 💡 Consejo del instructor

El rol no debe definirse pensando únicamente en un cargo.

También puede representar una función.

Por ejemplo:

- facilitador;
- analista;
- orientador;
- evaluador;
- asesor.

Lo importante es que ese rol sea coherente con el propósito del asistente.

---

## ✅ Checkpoint

Antes de continuar confirme que:

- □ definió el rol del asistente;
- □ justificó la elección;
- □ verificó que el rol es coherente con el propósito definido anteriormente.

---

# Actividad 3

# Definición de los usuarios

## Objetivo

Identificar quiénes utilizarán el asistente y cuáles serán sus principales necesidades de información.

---

## Contexto

Todo asistente inteligente debe diseñarse pensando en las personas que interactuarán con él.

Conocer a los usuarios permitirá definir posteriormente:

- el lenguaje que utilizará el asistente;
- el nivel de detalle de las respuestas;
- el tipo de ejemplos que podrá entregar;
- las restricciones que deberá respetar.

---

## Procedimiento

Para el caso guiado identifique:

### Usuarios principales

______________________________________________________

### Necesidades más frecuentes

______________________________________________________

______________________________________________________

______________________________________________________

---

## 📝 Registro del participante

| Usuario | Necesidad principal |
|----------|---------------------|
| | |
| | |
| | |

---

## 💡 Consejo del instructor

No piense únicamente en quién hará preguntas.

Piense también en quién utilizará posteriormente la información generada por el asistente.

---

## 📁 Portafolio

Las decisiones adoptadas durante estas tres primeras actividades servirán como modelo para el desarrollo del Documento 2 del Proyecto Integrador.

En este momento todavía no está construyendo su propio asistente.

Está aprendiendo la metodología que aplicará durante la segunda parte del laboratorio.

---

## ✅ Checkpoint general

Antes de finalizar esta sección verifique que:

- □ comprendió la diferencia entre propósito y funcionalidades;
- □ definió un rol coherente;
- □ identificó los usuarios del asistente;
- □ registró todas las decisiones adoptadas.

Con estas actividades concluye la primera parte del caso guiado.

En la siguiente sección continuará definiendo el contexto operativo, las restricciones, los criterios de funcionamiento y la estructura del **System Prompt**, completando así el diseño metodológico del asistente inteligente.

---

**Fin de la Parte 2 del Laboratorio 2**

# Actividad 4

# Definición del contexto de actuación

## Objetivo

Definir el contexto organizacional dentro del cual operará el asistente inteligente, estableciendo los límites del dominio de conocimiento que utilizará para responder las consultas de los usuarios.

---

## Contexto

Hasta este momento ha definido:

- el propósito del asistente;
- el rol que desempeñará;
- los usuarios a quienes estará dirigido.

Sin embargo, aún falta responder una pregunta fundamental:

> **¿En qué contexto trabajará el asistente?**

El contexto constituye uno de los componentes importantes del diseño.

Junto con las instrucciones y restricciones definidas en el _System Prompt_, permite delimitar el ámbito dentro del cual se espera que opere el asistente y reducir la probabilidad de que genere respuestas fuera del dominio establecido.

Una definición clara del contexto facilita obtener respuestas más pertinentes y consistentes con el propósito del asistente.

---

## Procedimiento

Para el caso guiado considere la siguiente situación.

El asistente trabajará exclusivamente apoyando consultas relacionadas con procesos académicos de una institución de educación superior.

No responderá consultas relacionadas con:

- salud;
- aspectos legales;
- soporte informático;
- orientación psicológica;
- temas financieros.

Su ámbito de acción será únicamente el académico.

Ahora complete la siguiente ficha.

---

## 📝 Registro del participante

### Contexto donde operará el asistente

______________________________________________________

______________________________________________________

______________________________________________________

---

### Información o fuentes que estarán disponibles para apoyar sus respuestas
>**Importante:** indicar una fuente de información en el _System Prompt_ no proporciona automáticamente acceso a ella. Para utilizar documentos, reglamentos u otros antecedentes específicos, dicha información deberá estar efectivamente disponible para el asistente durante la interacción o mediante los mecanismos de integración correspondientes.
______________________________________________________

______________________________________________________

______________________________________________________

---

### Temas que quedan fuera de su alcance

______________________________________________________

______________________________________________________

______________________________________________________

---

## 💡 Consejo del instructor

Definir claramente aquello que el asistente **no hará** resulta tan importante como definir aquello que sí hará.

Los asistentes inteligentes funcionan mejor cuando poseen límites claramente establecidos.

---

## ⚠️ Error frecuente

Muchos asistentes son diseñados como "expertos en todo".

Como consecuencia, comienzan a responder preguntas fuera del dominio para el cual fueron concebidos.

Esto reduce considerablemente la confiabilidad de la solución.

---

## ✅ Checkpoint

Antes de continuar confirme que:

- □ definió el contexto del asistente;
- □ delimitó claramente el dominio de conocimiento;
- □ identificó los temas que quedan fuera de su alcance.

---

# Actividad 5

# Definición de restricciones

## Objetivo

Establecer las reglas que deberán orientar el comportamiento del asistente durante todas sus interacciones.

---

## Contexto

Un asistente inteligente no solamente necesita saber qué hacer.

También debe conocer las restricciones que orientarán su comportamiento.

Estas restricciones permiten mantener la coherencia de las respuestas y disminuir la posibilidad de generar información incorrecta o poco apropiada.

En proyectos profesionales, estas reglas constituyen uno de los componentes más importantes del diseño del asistente.

---

## Procedimiento

Para el caso guiado considere las siguientes restricciones.

El asistente deberá:

- utilizar un lenguaje respetuoso;
- responder únicamente cuando disponga de información suficiente;
- reconocer explícitamente cuando desconozca una respuesta;
- evitar inventar información;
- responder utilizando lenguaje claro;
- organizar la información mediante listas cuando sea conveniente.

Ahora complete la siguiente tabla.

---

## 📝 Registro del participante

| Restricción | ¿Por qué es importante? |
|-------------|-------------------------|
| | |
| | |
| | |
| | |
| | |

---

## 🔍 Deténgase y analice

Imagine que el asistente entrega una respuesta incorrecta sobre un proceso académico.

¿Qué consecuencias podría generar?

______________________________________________________

______________________________________________________

______________________________________________________

---

## 💡 Consejo del instructor

Las restricciones constituyen una herramienta para aumentar la calidad de las respuestas.

No limitan al modelo.

Lo orientan.

---

## ✅ Checkpoint

Antes de continuar verifique que:

- □ definió las principales restricciones;
- □ justificó su importancia;
- □ analizó las consecuencias de no establecerlas.

---


# Actividad 6
# Construcción del primer prompt

## Objetivo

Integrar todos los componentes definidos anteriormente en un primer borrador del **System Prompt** del asistente.

---

## Contexto

Hasta este momento el asistente dispone de:

- un propósito;
- un rol;
- usuarios definidos;
- un contexto;
- restricciones.

Ahora esos elementos deberán integrarse en un único prompt.

Este prompt no será definitivo.

Durante el Laboratorio 3 será validado y optimizado.

Sin embargo, constituye el punto de partida para el comportamiento del asistente.

---

## Procedimiento

Utilizando los elementos desarrollados durante las actividades anteriores, redacte el primer borrador del prompt.

Puede utilizar la siguiente estructura como referencia.

---

### Plantilla sugerida

> Actúa como ____________________________.
>
> Tu propósito consiste en ____________________________.
>
> Tus usuarios principales son ____________________________.
>
> Debes responder únicamente consultas relacionadas con ____________________________.
>
> No debes responder consultas relacionadas con ____________________________.
>
> Cuando no dispongas de información suficiente, indícalo explícitamente.
>
> Utiliza un lenguaje ____________________________.
>
> Organiza las respuestas utilizando ____________________________.

---

## 📝 Registro del participante

### Primer borrador del prompt

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

---

## 💡 Consejo del instructor

No intente escribir un prompt extenso.

Procure que cada instrucción aporte información relevante.

La claridad siempre resulta más importante que la cantidad de texto.

---

## ⚠️ Error frecuente

Agregar instrucciones repetidas o contradictorias.

Antes de finalizar revise cuidadosamente el prompt y elimine aquellas frases que no aporten información nueva.

---

## 📁 Portafolio

Conserve este primer borrador.

Durante el Laboratorio 3 será sometido a distintas pruebas de validación y posteriormente optimizado.

La evolución del prompt formará parte de la evidencia del Proyecto Integrador.

---

# Actividad 7
### Configuración inicial del asistente en Open WebUI

**Objetivo**
 
Implementar en Open WebUI la primera versión del asistente diseñado durante las actividades anteriores.

**Procedimiento**

Utilizando las instrucciones correspondientes del **Manual Técnico**:

1. Acceda a Open WebUI.
2. Cree la configuración del asistente a partir del modelo definido para el taller.
3. Asigne un nombre que permita identificarlo.
4. Incorpore el **System Prompt** elaborado durante este laboratorio.
5. Guarde la configuración.
6. Inicie una conversación utilizando el asistente configurado.

7. Realice una consulta sencilla relacionada con su propósito y compruebe que genera una respuesta.

**Checkpoint:**

□ El asistente fue configurado en Open WebUI.
□ Se incorporó el System Prompt.
□ El modelo responde correctamente.
□ Se realizó una primera prueba funcional.


---

## ✅ Checkpoint general

Antes de finalizar la etapa guiada del laboratorio confirme que:

- □ definió el contexto del asistente;
- □ estableció restricciones de funcionamiento;
- □ redactó el primer borrador del prompt;
- □ registró todas las observaciones realizadas.

Con estas actividades concluye el **caso guiado**.

En la siguiente parte del laboratorio aplicará exactamente la misma metodología al problema definido en su **Proyecto Integrador**, diseñando la primera versión de su propio asistente inteligente especializado.

---

**Fin de la Parte 3 del Laboratorio 2**

# 5. Proyecto Integrador

Durante el caso guiado desarrolló un asistente inteligente siguiendo una metodología estructurada.

Ahora aplicará exactamente ese mismo procedimiento al problema definido en el Laboratorio 1.

A diferencia de las actividades anteriores, en esta sección no existe una única respuesta correcta.

Cada participante diseñará un asistente distinto, ya que responderá a necesidades, organizaciones y contextos profesionales diferentes.

Sin embargo, todos los proyectos compartirán la misma metodología de diseño.

Al finalizar esta sección habrá construido y documentado su asistente inteligente especializado y generado el **Documento 2** del Portafolio del Proyecto Integrador.

---

# 5.1 Objetivo

Diseñar el asistente inteligente asociado al Proyecto Integrador, definiendo su propósito, rol, usuarios, contexto, restricciones y **System Prompt**.

---

# Antes de comenzar

Recupere el **Documento 1. Definición del problema y alcance**, elaborado durante el Laboratorio 1.

Toda la información registrada en ese documento será utilizada para desarrollar el asistente.

Si durante la revisión identifica aspectos que requieren ajustes o mayor precisión, puede realizar las modificaciones necesarias antes de continuar.

Recuerde que el Proyecto Integrador evoluciona progresivamente durante el taller.

Es completamente normal perfeccionar documentos desarrollados en laboratorios anteriores.

---

## 💡 Consejo del instructor

No copie el caso guiado.

Utilícelo únicamente como referencia metodológica.

Su asistente debe responder al problema específico que identificó en su propio contexto profesional.

---

# Actividad 1

# Definición del propósito del asistente

## Objetivo

Establecer claramente la finalidad del asistente inteligente.

---

## Actividad

Complete la siguiente ficha.

### Nombre del asistente

______________________________________________________

---

### Problema que ayudará a resolver

______________________________________________________

______________________________________________________

______________________________________________________

---

### Propósito principal

______________________________________________________

______________________________________________________

______________________________________________________

---

### Valor esperado para la organización

______________________________________________________

______________________________________________________

______________________________________________________

---

## 🔍 Deténgase y analice

Si una persona leyera únicamente el propósito del asistente,

¿comprendería inmediatamente para qué fue diseñado?

Si la respuesta es negativa, reformule la descripción.

---

# Actividad 2

# Definición del rol y de los usuarios

## Objetivo

Precisar el perfil profesional que asumirá el asistente y las características de quienes interactuarán con él.

---

## Actividad

Complete la siguiente tabla.

| Elemento | Descripción |
|----------|-------------|
| Rol del asistente | |
| Usuarios principales | |
| Nivel de conocimiento de los usuarios | |
| Tipo de consultas esperadas | |

---

## 💡 Consejo del instructor

Procure que el rol represente una función claramente identificable dentro de la organización.

Por ejemplo:

- Analista documental.
- Asistente de procesos.
- Orientador académico.
- Consultor interno.
- Especialista en apoyo administrativo.

---

# Actividad 3

# Definición del contexto operativo

## Objetivo

Especificar el entorno donde funcionará el asistente.

---

## Actividad

Complete la siguiente ficha.

### Organización

______________________________________________________

---

### Área donde operará

______________________________________________________

---

### Tipo de información que utilizará

______________________________________________________

______________________________________________________

______________________________________________________

---

### Información que no deberá utilizar

______________________________________________________

______________________________________________________

______________________________________________________

---

### Alcance del asistente

______________________________________________________

______________________________________________________

______________________________________________________

---

## ⚠️ Error frecuente

Definir un contexto demasiado amplio.

Mientras más específico sea el dominio de conocimiento, mejores resultados obtendrá posteriormente durante la validación del asistente.

---

# Actividad 4

# Definición de restricciones

## Objetivo

Establecer las reglas que orientarán el comportamiento del asistente durante todas sus interacciones.

---

## Actividad

Complete la siguiente tabla.

| Restricción | Justificación |
|-------------|---------------|
| | |
| | |
| | |
| | |
| | |

Algunas preguntas que pueden orientar su trabajo son:

- ¿Debe reconocer cuando desconoce una respuesta?
- ¿Puede generar recomendaciones?
- ¿Debe solicitar información adicional antes de responder?
- ¿Puede responder utilizando información no proporcionada por el usuario?
- ¿Debe mantener un lenguaje formal o cercano?

---

## 🔍 Reflexión

Piense en una situación donde el asistente entregue una respuesta incorrecta.

¿Qué impacto podría generar dentro de su organización?

______________________________________________________

______________________________________________________

______________________________________________________

---

# Actividad 5

# Diseño del **System Prompt**

## Objetivo

Construir una configuración inicial del **System Prompt** que utilizará el asistente inteligente.

---

## Procedimiento

Integre toda la información desarrollada durante las actividades anteriores.

Puede utilizar la siguiente estructura como guía.

---

### Plantilla de referencia

> Actúa como _________________________________.
>
> Tu propósito consiste en _________________________________.
>
> Ayudarás principalmente a _________________________________.
>
> Trabajarás únicamente dentro del contexto de _________________________________.
>
> No responderás consultas relacionadas con _________________________________.
>
> Cuando no dispongas de información suficiente deberás _________________________________.
>
> Tus respuestas deberán caracterizarse por _________________________________.

---

## 📝 Espacio de trabajo

### Primer borrador del prompt

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

---

## 💡 Consejo del instructor

Considere este prompt como la configuración inicial de su asistente.

Durante el Laboratorio 3 será sometido a múltiples pruebas de funcionamiento.

No busque la perfección.

Busque coherencia.

---

# Actividad 6

# Revisión del diseño

Antes de finalizar, revise nuevamente todo el diseño del asistente.

Pregúntese:

- ¿El propósito coincide con el problema identificado?
- ¿El rol es coherente?
- ¿Los usuarios fueron correctamente identificados?
- ¿El contexto está claramente delimitado?
- ¿Las restricciones son suficientes?
- ¿El prompt integra todos los elementos anteriores?

Realice los ajustes que considere necesarios.

---

# 5.2 Documento generado

Al finalizar este laboratorio deberá disponer del siguiente documento.

---

# Documento 2

## Diseño del asistente inteligente especializado

El documento deberá incluir, como mínimo:

- Nombre del asistente.
- Problema que resolverá.
- Propósito.
- Rol.
- Usuarios.
- Contexto operativo.
- Restricciones.
- **System Prompt** inicial.
- ¿Qué componente considera más importante para que el asistente entregue respuestas de calidad?

Este documento será utilizado durante el Laboratorio 3 para validar y optimizar el comportamiento del asistente.

---

## 📁 Portafolio

Incorpore el Documento 2 al Portafolio del Proyecto Integrador.

Al finalizar este laboratorio su Portafolio deberá contener:

- Documento 1. Definición del problema y alcance.
- Documento 2. Diseño del asistente inteligente especializado.

---

# 5.3 Autoevaluación del Proyecto

Antes de continuar confirme que:

| Aspecto | Sí | Parcial | No |
|----------|:--:|:--------:|:--:|
| Definí claramente el propósito del asistente. | □ | □ | □ |
| El rol representa adecuadamente su función. | □ | □ | □ |
| Identifiqué correctamente los usuarios. | □ | □ | □ |
| Delimité el contexto de trabajo. | □ | □ | □ |
| Definí restricciones coherentes. | □ | □ | □ |
| Elaboré el primer prompt completo. | □ | □ | □ |
| Incorporé el Documento 2 al Portafolio. | □ | □ | □ |

---

## 💡 Consejo final

No considere este documento como un producto terminado.

Piense en él como el plano de construcción del asistente inteligente.

Así como los proyectos de ingeniería evolucionan mediante pruebas y mejoras sucesivas, su asistente también será perfeccionado en los próximos laboratorios.

Lo importante es que la estructura metodológica ya se encuentra definida.

---

**Fin de la Parte 4 del Laboratorio 2**

> En la **Parte 5** realizará el cierre del laboratorio, reflexionará sobre las decisiones adoptadas durante el diseño del asistente, verificará los productos obtenidos y preparará el trabajo que desarrollará en el **Laboratorio 3**, donde comenzará la validación y optimización del asistente inteligente mediante casos de prueba.

# 6. Cierre del laboratorio

Durante este laboratorio dio un paso decisivo en el desarrollo del Proyecto Integrador.

Mientras que en el laboratorio anterior definió el problema que deseaba resolver, en esta oportunidad transformó esa necesidad en el diseño de una solución concreta basada en Inteligencia Artificial Generativa Local.

Observe que aún no ha comenzado la etapa de validación.

Eso ocurrirá durante el próximo laboratorio.

Sin embargo, a partir de este momento ya dispone de un asistente inteligente con una identidad claramente definida:

- sabe cuál es su propósito;
- conoce el rol que desempeñará;
- identifica a sus usuarios;
- comprende el contexto donde trabajará;
- posee restricciones de funcionamiento;
- dispone de un primer prompt estructurado.

Estos elementos constituyen la base sobre la cual evolucionará el asistente durante el resto del taller.

---

# 6.1 Síntesis

Durante este laboratorio desarrolló las siguientes actividades:

- analizó la metodología para diseñar asistentes inteligentes;
- participó en el desarrollo de un caso guiado;
- definió el propósito del asistente;
- estableció el rol que desempeñará;
- identificó a los usuarios;
- delimitó el contexto operativo;
- definió restricciones de funcionamiento;
- elaboró el primer borrador del **System Prompt**;
- desarrolló el Documento 2 del Proyecto Integrador.

Más allá de la construcción del prompt, el principal aprendizaje de este laboratorio consiste en comprender que el comportamiento de un asistente inteligente depende principalmente de las decisiones de diseño adoptadas antes de comenzar su implementación.

Una buena arquitectura metodológica facilita enormemente las etapas posteriores de validación y optimización.

---

# 6.2 ¿Qué aprendí hoy?

Dedique algunos minutos a reflexionar sobre su experiencia.

No existen respuestas únicas.

El propósito consiste en reconocer los principales aprendizajes obtenidos durante este laboratorio.

---

## ¿Cuál fue la decisión de diseño más importante que tomó durante este laboratorio?

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

---

## ¿Qué aspecto del diseño le resultó más complejo?

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

---

## ¿Qué cambios cree que deberá realizar posteriormente en el asistente?

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

---

## ¿Qué diferencia observa entre escribir un prompt y diseñar un asistente inteligente?

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

---

# 6.3 Autoevaluación

Evalúe el nivel de logro alcanzado durante este laboratorio.

| Criterio | Logrado | Parcial | Pendiente |
|----------|:-------:|:--------:|:---------:|
| Comprendí la metodología para diseñar asistentes inteligentes. | □ | □ | □ |
| Definí claramente el propósito del asistente. | □ | □ | □ |
| Seleccioné un rol coherente con el problema. | □ | □ | □ |
| Delimité adecuadamente el contexto de trabajo. | □ | □ | □ |
| Establecí restricciones apropiadas. | □ | □ | □ |
| Elaboré el primer prompt del asistente. | □ | □ | □ |
| Completé el Documento 2 del Proyecto Integrador. | □ | □ | □ |

---

## 🔍 Reflexión profesional

Responda la siguiente pregunta.

> **¿Por qué considera que dos asistentes construidos sobre el mismo modelo de lenguaje pueden entregar respuestas completamente distintas?**

Fundamente utilizando los conceptos desarrollados durante este laboratorio.

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

______________________________________________________

Esta reflexión será retomada durante el Laboratorio 3, cuando el comportamiento del asistente sea sometido a pruebas de validación.

---

# 6.4 Lista de entregables

Al finalizar este laboratorio deberá disponer de los siguientes productos.

| Producto                              | Estado |
| ------------------------------------- | :----: |
| Caso guiado desarrollado              | □ |
| Ficha de diseño del asistente         | □ |
| Definición del propósito              | □ |
| Definición del rol                    | □ |
| Contexto operativo                    | □ |
| Restricciones del asistente           | □ |
| Primer borrador del **System Prompt** | □ |
| Documento 2 del Proyecto Integrador   | □ |

Conserve todos estos documentos.

Serán utilizados durante el Laboratorio 3.

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

Observe que el Portafolio comienza a reflejar la evolución del proyecto.

Hasta ahora dispone de:

1. El problema que desea resolver.
2. El diseño de la solución que utilizará para resolverlo.

Durante los siguientes laboratorios el Portafolio continuará creciendo mediante nuevos documentos.

---

# 6.5 Preparación del Laboratorio 3

Antes de asistir al próximo laboratorio asegúrese de que:

- conserva el Documento 2 del Proyecto Integrador;
- mantiene operativo el entorno local de IA;
- dispone del primer prompt elaborado durante este laboratorio;
- ha revisado el Capítulo 3 del Manual del Participante.

En el siguiente laboratorio comenzará una nueva etapa del proyecto:

**la validación y optimización del asistente inteligente.**

Ya no diseñará nuevas funcionalidades.

Ahora comprobará si el asistente realmente responde como fue concebido.

---

## 💡 Recomendación del instructor

Antes del próximo laboratorio converse con su asistente utilizando distintas preguntas relacionadas con el problema definido.

No busque todavía mejorar el prompt.

Simplemente observe:

- cómo responde;
- qué hace correctamente;
- qué dificultades aparecen;
- qué aspectos considera necesario modificar.

Estas observaciones facilitarán enormemente las actividades de validación que desarrollará durante el siguiente laboratorio.

---

# 6.6 Vinculación con el Laboratorio 3

Hasta este momento ha diseñado y configurado su asistente inteligente.

Durante el Laboratorio 3 el asistente será sometido a un proceso sistemático de validación mediante distintos casos de prueba.

Aprenderá a:

- diseñar casos de prueba;
- validar la calidad de las respuestas;
- identificar errores;
- detectar inconsistencias;
- optimizar el **System Prompt**;
- documentar las mejoras realizadas.

En otras palabras, el asistente avanzará desde una configuración inicial hacia una solución progresivamente validada y optimizada.

Esta etapa constituye una práctica habitual en el desarrollo profesional de soluciones basadas en Inteligencia Artificial.

---

# Mensaje final

Diseñar un asistente inteligente no consiste únicamente en redactar instrucciones para un modelo de lenguaje.

Implica comprender un problema, definir un propósito claro, establecer límites de actuación y traducir esas decisiones en una arquitectura coherente que permita al modelo comportarse de manera consistente.

Durante este laboratorio ha construido esa arquitectura.

En los próximos laboratorios comprobará que un buen diseño facilita enormemente la validación, la integración con otros sistemas y la evolución futura del asistente.

El Proyecto Integrador continúa avanzando.

Cada nuevo documento incorporado al Portafolio representa una evidencia del proceso de diseño seguido para construir una solución basada en Inteligencia Artificial Generativa Local.

---

# Fin del Laboratorio 2

## Producto obtenido para el Portafolio

**Documento 2. Diseño del asistente inteligente especializado**

## Próximo laboratorio

**Laboratorio 3. Validación y optimización del asistente inteligente mediante casos de prueba**

**Proyecto Integrador**

**Documento 3. Validación y optimización del asistente inteligente**

---

