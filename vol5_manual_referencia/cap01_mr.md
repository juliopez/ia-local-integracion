# MANUAL DE REFERENCIA TÉCNICA

## Desarrollo de Soluciones Organizacionales mediante Inteligencia Artificial Local

### Recursos técnicos, código fuente y documentación de apoyo

---

**Autor**

**Dr. Julio López-Núñez**

---

# Presentación

El presente **Manual de Referencia Técnica** reúne todos los recursos complementarios utilizados durante el desarrollo del taller **Desarrollo de Soluciones Organizacionales mediante Inteligencia Artificial Local**.

Mientras que el **Libro del Participante** explica los fundamentos conceptuales, el **Manual Técnico** guía la implementación paso a paso, el **Cuaderno de Laboratorios** permite aplicar los conocimientos adquiridos y el **Manual del Proyecto Integrador** documenta formalmente el desarrollo de la solución, este volumen actúa como un repositorio técnico de consulta permanente.

Aquí se concentran los elementos que, por su extensión o naturaleza especializada, no forman parte del cuerpo principal de la colección, pero sirven como apoyo para implementar, mantener y evolucionar la solución desarrollada.

Entre estos recursos se incluyen diagramas de arquitectura, código fuente completo, comandos de uso frecuente, procedimientos de solución de problemas, glosario técnico y documentación complementaria.

Este manual ha sido concebido como una herramienta de consulta. No requiere una lectura secuencial y puede utilizarse de forma independiente cada vez que alguno de los demás volúmenes haga referencia a uno de sus contenidos.

---

# Cómo utilizar este manual

Cada capítulo del presente volumen puede consultarse de manera independiente.

Durante la lectura de cualquiera de los otros documentos de la colección aparecerán referencias similares a las siguientes:

> Revise el **Capítulo 4 del Manual de Referencia Técnica** para identificar posibles soluciones al problema detectado.

o

> Revise el **Capítulo 2 del Manual de Referencia Técnica** para identificar posibles soluciones al problema detectado.

Estas referencias permiten mantener una estructura editorial limpia, evitando incorporar extensos bloques de código o información altamente técnica dentro de los documentos principales.

---

# Organización del Manual

El Manual de Referencia Técnica se organiza en siete capítulos.

| Capítulo   | Contenido                               |
| ---------- | --------------------------------------- |
| Capítulo 1 | Diagramas de arquitectura               |
| Capítulo 2 | Código fuente completo                  |
| Capítulo 3 | Guía rápida de comandos                 |
| Capítulo 4 | Solución de problemas (Troubleshooting) |
| Capítulo 5 | Glosario técnico                        |
| Capítulo 6 | Recursos complementarios                |
| Capítulo 7 | Versiones de software utilizadas        |

Cada capítulo puede utilizarse de manera independiente según las necesidades del lector.

---

# Convenciones utilizadas

Para facilitar la consulta del manual se utilizarán las siguientes convenciones editoriales.

| Convención | Significado |
|------------|-------------|
| Código | Fragmentos listos para utilizar. |
| Nota técnica | Información complementaria. |
| Buena práctica | Recomendación derivada de la experiencia profesional. |
| Advertencia | Situación que puede provocar errores durante la implementación. |
| Importante | Aspecto que requiere especial atención. |
| Referencia cruzada | Relación con alguno de los demás volúmenes de la colección. |

---

# Relación con la colección

El siguiente esquema resume el papel del Manual de Referencia Técnica dentro de la colección.

```text
Libro del Participante
        │
        ▼
Manual Técnico
        │
        ▼
Cuaderno de Laboratorios
        │
        ▼
Manual del Proyecto Integrador
        │
        ▼
Manual de Referencia Técnica
```

El presente volumen constituye el repositorio oficial de apoyo técnico para toda la colección.

---

# Antes de comenzar

Los recursos incluidos en este manual han sido seleccionados con el propósito de facilitar la implementación y el mantenimiento de soluciones organizacionales basadas en Inteligencia Artificial Local.

Siempre que sea posible, se recomienda consultar previamente el **Libro del Participante**, el **Manual Técnico** y el **Manual del Proyecto Integrador**, utilizando este volumen únicamente como apoyo durante la ejecución de actividades específicas.

# Capítulo 1

# Diagramas de Arquitectura

---

## Objetivo

Reunir los diagramas oficiales utilizados durante el desarrollo del proyecto, proporcionando una representación gráfica de la arquitectura técnica, el flujo de información y la interacción entre los distintos componentes que conforman la solución.

Los diagramas incluidos en este capítulo constituyen la referencia oficial para comprender la estructura general del sistema y deberán utilizarse como apoyo durante la implementación, la documentación y la presentación del Proyecto Integrador.

---

# Cómo utilizar este capítulo

Cada diagrama representa una vista diferente de la solución desarrollada.

Algunos muestran la arquitectura completa del sistema, mientras que otros describen procesos específicos o la interacción entre componentes particulares.

Se recomienda consultar estos diagramas antes de realizar modificaciones importantes en la arquitectura o durante la elaboración de la documentación técnica del proyecto.

---

# Organización del capítulo

Este capítulo contiene los siguientes diagramas.

| Diagrama | Descripción |
|-----------|-------------|
| D1 | Arquitectura general de la solución |
| D2 | Arquitectura de Ollama |
| D3 | Arquitectura de Open WebUI |
| D4 | Flujo Google Forms → Google Sheets |
| D5 | Flujo Apps Script → Python |
| D6 | Flujo completo de procesamiento |
| D7 | Arquitectura de producción |
| D8 | Arquitectura del Proyecto Integrador |

---

# D1

# Arquitectura general de la solución

## Objetivo

Representar la arquitectura completa del sistema desarrollado durante el taller, mostrando la interacción entre el usuario, los servicios de Google Workspace, el puente local implementado en Python y el modelo de lenguaje ejecutado mediante Ollama.

---

## Descripción

El flujo comienza cuando un usuario registra una solicitud mediante un formulario de Google Forms.

La información es almacenada automáticamente en Google Sheets.

Posteriormente, Google Apps Script, publicado como Web App, permite acceder a las solicitudes pendientes registradas en Google Sheets.

El puente local `puente_local.py` consulta el Web App, obtiene una solicitud pendiente y la remite a Ollama para su procesamiento mediante el modelo de lenguaje configurado.

Finalmente, la respuesta generada es registrada nuevamente en Google Sheets y enviada automáticamente al usuario mediante correo electrónico.

---

## Diagrama

```text
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

---

## Componentes

| Componente | Función |
|------------|---------|
| Usuario | Registra la solicitud. |
| Google Forms | Captura la información. |
| Google Sheets | Almacena las solicitudes y respuestas. |
| Apps Script | Coordina el flujo del proceso. |
| Python | Establece la comunicación con Ollama. |
| Ollama | Ejecuta el modelo de lenguaje local. |
| Gmail | Entrega la respuesta al usuario. |

---

## Consideraciones

- El procesamiento se realiza completamente en el computador local.
- No se utilizan servicios comerciales de IA generativa.
- El modelo permanece bajo control de la organización.
- El procesamiento mediante el modelo de lenguaje se realiza localmente a través de Ollama, mientras que la captura, registro y envío de información utilizan los servicios de Google Workspace definidos en la solución.
- La arquitectura puede adaptarse para incorporar nuevos modelos de lenguaje.

---

## Relación con la colección

| Documento | Relación |
|------------|----------|
| Libro del Participante | Capítulos sobre arquitectura general. |
| Manual Técnico | Capítulos 7 y 8. |
| Manual del Proyecto Integrador | Plantillas A.4 y A.5. |
| Cuaderno de Laboratorios | Laboratorios 4 y 5. |

---

## Buenas prácticas

- Mantener actualizado este diagrama cuando cambie la arquitectura.
- Utilizar la misma nomenclatura en toda la documentación.
- Incorporar fecha y versión en futuras modificaciones.
- Conservar una copia editable del diagrama.

---

## Referencia técnica

Este diagrama constituye la representación oficial de la arquitectura utilizada durante el taller.

Todas las implementaciones descritas en la colección deberán mantener coherencia con esta representación o documentar explícitamente las modificaciones realizadas.

---

# D2

# Arquitectura de Ollama

---

## Objetivo

Describir la arquitectura funcional de Ollama dentro de la solución desarrollada durante el taller, identificando los componentes involucrados en la ejecución de modelos de lenguaje locales, el flujo de procesamiento de solicitudes y la interacción con el puente desarrollado en Python.

Este diagrama permite comprender cómo Ollama administra los modelos instalados y cómo responde a las solicitudes generadas desde el sistema.

---

# Descripción

Ollama actúa como el motor de inferencia del proyecto.

Recibe solicitudes desde el puente local implementado en Python, procesa el prompt utilizando el modelo de lenguaje previamente cargado y devuelve una respuesta al proceso solicitante.

La inferencia mediante Ollama y el modelo de lenguaje se realiza localmente, sin utilizar servicios externos de Inteligencia Artificial generativa.

---

# Diagrama

```text
                 Puente Python
                        │
                        ▼
                API Local Ollama
                        │
                        ▼
              Administrador Ollama
                        │
        ┌───────────────┴───────────────┐
        │                               │
        ▼                               ▼
 Modelo de Lenguaje              Gestión de Modelos
        │                               │
        └───────────────┬───────────────┘
                        ▼
               Motor de Inferencia
                        │
                        ▼
             Generación de Respuesta
                        │
                        ▼
                 Puente Python
```

---

# Componentes

| Componente | Función |
|------------|---------|
| API Local | Recibe solicitudes desde aplicaciones externas. |
| Administrador Ollama | Gestiona la ejecución de los modelos instalados. |
| Modelo de Lenguaje | Procesa el prompt recibido y genera la respuesta. |
| Motor de Inferencia | Ejecuta el proceso de generación de texto. |
| Puente Python | Envía solicitudes y recibe las respuestas generadas. |

---

# Flujo de procesamiento

El procesamiento interno de Ollama puede resumirse de la siguiente forma.

1. El puente local envía un prompt.
2. Ollama identifica el modelo solicitado.
3. El modelo es cargado en memoria (si corresponde).
4. Se ejecuta el proceso de inferencia.
5. Se genera la respuesta.
6. La respuesta es devuelta al puente local.

---

# Recursos utilizados

Durante la ejecución, Ollama utiliza principalmente los siguientes recursos del computador.

| Recurso | Utilización |
|----------|-------------|
| Memoria RAM | Almacenamiento temporal del modelo durante la inferencia. |
| Procesador (CPU) | Coordinación del proceso y ejecución del modelo cuando no existe aceleración adicional. |
| Disco | Almacenamiento permanente de los modelos descargados. |

---

# Tabla de decisión rápida

La siguiente tabla proporciona una orientación general para seleccionar modelos según la memoria RAM disponible en el equipo.

| Memoria RAM disponible | Tamaño recomendado del modelo |
|------------------------|-------------------------------|
| Hasta 8 GB | Modelos pequeños (≈3B parámetros). |
| 16 GB | Modelos medianos (≈7B parámetros). |
| 32 GB o más | Modelos de mayor tamaño (≈13B o superiores, según disponibilidad de recursos). |

> **Importante:** Esta tabla corresponde únicamente a una referencia orientativa. El rendimiento efectivo dependerá también del procesador, del sistema operativo y de los demás procesos que se encuentren ejecutándose en el computador.

---

# Consideraciones

- Ollama trabaja completamente en el computador local.
- Los modelos permanecen almacenados localmente.
- No es necesario enviar información a servicios externos para generar respuestas.
- Es posible instalar distintos modelos según las necesidades del proyecto.
- El cambio de modelo no requiere modificar la arquitectura general de la solución.

---

# Buenas prácticas

- Mantener únicamente los modelos realmente necesarios.
- Eliminar versiones que ya no se utilicen.
- Verificar periódicamente el espacio disponible en disco.
- Confirmar que exista memoria RAM suficiente antes de utilizar modelos de mayor tamaño.
- Registrar en la documentación del proyecto el modelo utilizado durante las pruebas y la operación.

---

# Relación con la colección

| Documento | Relación |
|------------|----------|
| Libro del Participante | Capítulo dedicado a Ollama y modelos de lenguaje locales. |
| Manual Técnico | Capítulos 2 y 8. |
| Manual del Proyecto Integrador | Plantillas A.2 y A.4. |
| Cuaderno de Laboratorios | Laboratorios 2, 3 y 4. |

---

# Referencia técnica

Este diagrama representa la arquitectura funcional de Ollama utilizada como referencia durante el desarrollo del taller.

En caso de incorporar nuevos modelos o modificar la configuración de ejecución, se recomienda actualizar esta representación para mantener la consistencia de la documentación técnica.

---

# D3

# Arquitectura de Open WebUI

---

## Objetivo

Describir la arquitectura funcional de Open WebUI dentro de la solución desarrollada durante el taller, identificando los componentes que intervienen en la interacción entre el usuario y los modelos de lenguaje ejecutados mediante Ollama.

Este diagrama permite comprender el papel que desempeña Open WebUI como interfaz de usuario para la administración, configuración y utilización de asistentes inteligentes locales.

---

# Descripción

Open WebUI proporciona una interfaz web que permite interactuar con los modelos de lenguaje instalados en Ollama sin necesidad de utilizar la línea de comandos.

A través de esta plataforma es posible:

- configurar modelos personalizados a partir de modelos disponibles;
- administrar conversaciones;
- configurar instrucciones del sistema (_System Prompt_);
- probar distintos modelos;
- validar respuestas;
- gestionar configuraciones básicas.

Durante el desarrollo del Proyecto Integrador, Open WebUI constituye el entorno principal para el diseño, prueba y validación inicial del asistente inteligente.

---

# Diagrama

```text
                    Usuario
                        │
                        ▼
                Navegador Web
                        │
                        ▼
                 Open WebUI
                        │
        ┌───────────────┼────────────────┐
        │               │                │
        ▼               ▼                ▼
 Conversaciones   Configuración   Gestión de Modelos
        │               │                │
        └───────────────┼────────────────┘
                        ▼
                 API de Ollama
                        │
                        ▼
              Modelo de Lenguaje
                        │
                        ▼
                  Respuesta IA
                        │
                        ▼
                   Open WebUI
                        │
                        ▼
                    Usuario
```

---

# Componentes

| Componente | Función |
|------------|---------|
| Navegador Web | Acceso a la interfaz gráfica. |
| Open WebUI | Plataforma para administrar asistentes y conversaciones. |
| Conversaciones | Historial de interacción con el modelo. |
| Configuración | Administración de parámetros y asistentes. |
| Gestión de Modelos | Selección del modelo disponible en Ollama. |
| API de Ollama | Comunicación entre Open WebUI y el motor de inferencia. |
| Modelo de Lenguaje | Generación de respuestas. |

---

# Funcionalidades principales

Durante el taller se utilizarán principalmente las siguientes funciones de Open WebUI.

| Funcionalidad                           | Utilización                                                               |
| --------------------------------------- | ------------------------------------------------------------------------- |
| Configuración de modelos personalizados | Definir el comportamiento especializado a partir de un modelo disponible. |
| Configuración del System Prompt         | Personalizar el comportamiento del modelo.                                |
| Gestión de conversaciones               | Registrar sesiones de prueba.                                             |
| Selección de modelos                    | Cambiar entre modelos disponibles.                                        |
| Validación de respuestas                | Evaluar el comportamiento del asistente.                                  |

---

# Flujo de interacción

El funcionamiento general puede resumirse mediante la siguiente secuencia.

1. El usuario accede mediante un navegador web.
2. Open WebUI presenta la interfaz de conversación.
3. El usuario envía una consulta.
4. Open WebUI remite la solicitud a Ollama.
5. Ollama ejecuta el modelo seleccionado.
6. La respuesta retorna a Open WebUI.
7. El usuario visualiza el resultado.

---

# Ventajas de utilizar Open WebUI

| Ventaja | Descripción |
|----------|-------------|
| Facilidad de uso | Evita utilizar comandos durante las pruebas iniciales. |
| Organización | Mantiene el historial de conversaciones. |
| Configuración | Permite administrar asistentes personalizados. |
| Productividad | Facilita la experimentación con distintos modelos. |
| Validación | Simplifica las pruebas funcionales del asistente. |

---

# Consideraciones

- Open WebUI constituye únicamente una interfaz de usuario.
- No ejecuta modelos de lenguaje directamente.
- Depende del correcto funcionamiento de Ollama.
- Puede administrar múltiples asistentes dentro de un mismo entorno.
- Las conversaciones pueden utilizarse como evidencia durante el proceso de validación.

---

# Buenas prácticas

- Definir nombres descriptivos para cada asistente.
- Mantener actualizado el System Prompt.
- Eliminar conversaciones de prueba que ya no sean necesarias.
- Registrar la versión del asistente antes de realizar modificaciones importantes.
- Utilizar conversaciones independientes para distintos escenarios de prueba.

---

# Relación con la colección

| Documento | Relación |
|------------|----------|
| Libro del Participante | Capítulo dedicado a Open WebUI. |
| Manual Técnico | Capítulos 3 y 4. |
| Manual del Proyecto Integrador | Plantillas A.2 y A.3. |
| Cuaderno de Laboratorios | Laboratorios 2 y 3. |

---

# Referencia técnica

Este diagrama representa la arquitectura funcional de Open WebUI utilizada durante el taller.

En futuras versiones del proyecto, cualquier modificación relacionada con la administración de asistentes, la organización de conversaciones o la configuración del entorno deberá actualizarse en esta representación para mantener la coherencia documental.

---

# D4

# Flujo de captura de información mediante Google Forms y Google Sheets

---

## Objetivo

Describir el proceso de captura, almacenamiento y disponibilidad inicial de la información dentro de la solución desarrollada durante el Proyecto Integrador.

Este diagrama representa el inicio del flujo operativo del sistema, mostrando cómo una solicitud realizada por un usuario es registrada y almacenada antes de ser procesada por el asistente inteligente.

---

# Descripción

El proceso comienza cuando un usuario completa un formulario diseñado en Google Forms.

Cada respuesta enviada es almacenada automáticamente en una hoja de cálculo de Google Sheets, la cual actúa como repositorio temporal de información para el resto de la solución.

Google Apps Script utilizará posteriormente esta información para iniciar el procesamiento automático de la solicitud.

---

# Diagrama

```text
                Usuario
                    │
                    ▼
            Google Forms
                    │
          Completa formulario
                    │
                    ▼
         Envío de respuestas
                    │
                    ▼
          Google Sheets
                    │
      Registro automático
                    │
                    ▼
      Solicitud disponible
      para procesamiento
```

---

# Componentes

| Componente | Función |
|------------|---------|
| Usuario | Completa el formulario. |
| Google Forms | Captura la información ingresada. |
| Google Sheets | Almacena automáticamente cada respuesta recibida. |

---

# Flujo del proceso

El funcionamiento puede resumirse mediante la siguiente secuencia.

1. El usuario accede al formulario.
2. Completa los campos requeridos.
3. Envía la información.
4. Google Forms valida el envío.
5. Las respuestas se almacenan automáticamente en Google Sheets.
6. La solicitud queda disponible para el procesamiento automático.

---

# Información almacenada

Dependiendo del proyecto desarrollado, Google Sheets podrá registrar información como:

| Tipo de información | Ejemplo |
|----------------------|---------|
| Fecha y hora | Momento del envío. |
| Usuario | Nombre o identificador. |
| Solicitud | Consulta realizada. |
| Estado | Pendiente, procesada o finalizada. |
| Respuesta | Resultado generado posteriormente por la IA. |

---

# Ventajas del enfoque

| Ventaja | Descripción |
|----------|-------------|
| Automatización | El registro es completamente automático. |
| Trazabilidad | Todas las solicitudes quedan almacenadas. |
| Escalabilidad | Es posible incorporar nuevos campos sin modificar la arquitectura general. |
| Integración | Google Apps Script puede acceder directamente a la información registrada. |

---

# Consideraciones

- Google Forms actúa únicamente como mecanismo de captura.
- Google Sheets constituye la fuente oficial de datos del proceso.
- No existe procesamiento mediante IA en esta etapa.
- Toda modificación realizada en el formulario debe reflejarse en la estructura de la hoja de cálculo.

---

# Buenas prácticas

- Diseñar formularios simples y claros.
- Evitar solicitar información innecesaria.
- Validar los tipos de datos antes de utilizar la información.
- Mantener nombres consistentes para las columnas de Google Sheets.
- Documentar cualquier cambio estructural realizado al formulario.

---

# Relación con la colección

| Documento | Relación |
|------------|----------|
| Libro del Participante | Unidad dedicada a Google Workspace y captura de información. |
| Manual Técnico | Capítulos 5 y 7. |
| Manual del Proyecto Integrador | Plantillas A.4 y A.5. |
| Cuaderno de Laboratorios | Laboratorio 4. |

---

# Referencia técnica

Este diagrama representa la primera etapa del flujo operativo de la solución.

Toda implementación desarrollada durante el taller deberá iniciar el procesamiento únicamente una vez que la información haya sido correctamente almacenada en Google Sheets.

En caso de modificar el formulario o la estructura de la hoja de cálculo, se recomienda actualizar esta documentación para mantener la coherencia entre la arquitectura y la implementación.

---

# D5

# Flujo de comunicación entre el Web App y `puente_local.py`

---

## Objetivo

Describir el proceso de comunicación entre Google Apps Script, publicado como Web App, y el puente local desarrollado en Python, permitiendo que las solicitudes registradas en Google Sheets sean procesadas por el modelo de Inteligencia Artificial ejecutado mediante Ollama.

Este diagrama representa el punto de integración entre los servicios en la nube de Google Workspace y la infraestructura local donde se ejecuta el modelo de lenguaje.

---

# Descripción

Una vez registrada una solicitud en Google Sheets, Google Apps Script, publicado como Web App, permite consultar las solicitudes pendientes.

`puente_local.py` consulta periódicamente el Web App mediante una solicitud HTTP, obtiene una solicitud pendiente y la envía a Ollama para generar una respuesta.

Una vez obtenida la respuesta, `puente_local.py` la devuelve al Web App mediante una nueva solicitud HTTP. Google Apps Script registra la respuesta en Google Sheets y realiza el envío correspondiente mediante Gmail.

---

# Diagrama

```text
Google Sheets
      │
      ▼
Google Apps Script / Web App
      │
      │ GET
      ▼
puente_local.py
      │
      ▼
Ollama
      │
      ▼
Modelo de Lenguaje
      │
      ▼
puente_local.py
      │
      │ POST
      ▼
Google Apps Script / Web App
      │
      ├──────────────► Google Sheets
      │
      └──────────────► Gmail
```

---

# Componentes

| Componente                   | Función                                                                                   |
| ---------------------------- | ----------------------------------------------------------------------------------------- |
| Google Sheets                | Almacena la solicitud pendiente de procesamiento.                                         |
| Google Apps Script           | Coordina el flujo de comunicación.                                                        |
| Solicitud HTTP               | Permite el intercambio de información entre `puente_local.py` y el Web App                |
| puente_local.py              | Consulta solicitudes pendientes, las envía a Ollama y devuelve las respuestas al Web App. |
| API de Ollama                | Permite la comunicación con el modelo seleccionado.                                       |
| Modelo de Lenguaje           | Genera la respuesta.                                                                      |
| Google Apps Script / Web App | Entrega solicitudes pendientes y recibe las respuestas procesadas.                        |

---

# Flujo del proceso

El proceso completo se desarrolla de la siguiente manera.

- `puente_local.py` consulta periódicamente el Web App mediante una solicitud HTTP GET.
- Google Apps Script consulta Google Sheets e identifica una solicitud pendiente.
- El Web App devuelve la solicitud pendiente a `puente_local.py`.
- `puente_local.py` envía la consulta a Ollama.
- Ollama ejecuta el modelo de lenguaje configurado.
- `puente_local.py` recibe la respuesta generada.
- `puente_local.py` envía la respuesta al Web App mediante una solicitud HTTP POST.
- Google Apps Script recibe la respuesta.
- Google Sheets actualiza el registro correspondiente.
- Gmail envía la respuesta al usuario.

---

# Información intercambiada

## Solicitud

Ejemplo de información enviada.

| Campo | Descripción |
|--------|-------------|
| prompt | Consulta enviada al modelo. |
| usuario | Identificador del solicitante. |
| fecha | Momento del envío. |
| contexto | Información adicional utilizada por el asistente. |

---

## Respuesta

Información devuelta al flujo.

| Campo | Descripción |
|--------|-------------|
| respuesta | Texto generado por el modelo. |
| estado | Resultado del procesamiento. |
| fecha_respuesta | Fecha y hora de finalización. |

---

# Posibles puntos de falla

| Situación                  | Consecuencia                                     |
| -------------------------- | ------------------------------------------------ |
| `puente_local.py` detenido | Las solicitudes pendientes no son procesadas.    |
| Ollama no disponible       | No puede generarse la respuesta.                 |
| Error en la solicitud HTTP | El procesamiento se interrumpe.                  |
| Error JSON                 | Apps Script no puede interpretar la respuesta.   |
| Tiempo de espera excedido  | La solicitud puede no completarse correctamente. |

---

# Recomendaciones

- Verificar previamente que `puente_local.py` se encuentre en ejecución.
- Confirmar que Ollama esté disponible antes de iniciar las pruebas.
- Registrar los errores de comunicación para facilitar el diagnóstico.
- Validar la estructura del objeto JSON antes de procesar la respuesta.
- Utilizar mensajes de error descriptivos durante el desarrollo.

---

# Buenas prácticas

- Separar claramente la lógica de comunicación y la lógica de procesamiento.
- Mantener una estructura uniforme para las solicitudes y respuestas.
- Evitar modificar el formato JSON durante el proyecto.
- Registrar tiempos de respuesta cuando se realicen pruebas de rendimiento.
- Documentar cualquier cambio realizado en la interfaz entre Google Apps Script y Python.

---

# Relación con la colección

| Documento | Relación |
|------------|----------|
| Libro del Participante | Unidad dedicada a la integración de herramientas. |
| Manual Técnico | Capítulos 7 y 8. |
| Manual del Proyecto Integrador | Plantilla A.4. |
| Cuaderno de Laboratorios | Laboratorio 4. |

---

# Referencia técnica

Este diagrama representa el mecanismo oficial de comunicación entre Google Workspace y el entorno local utilizado durante el taller.

Cualquier modificación en el protocolo de intercambio de información, en la estructura del objeto JSON o en `puente_local.py` deberá quedar documentada para mantener la consistencia de la arquitectura y facilitar el mantenimiento futuro.

---

# D6

# Flujo completo de procesamiento de una solicitud

---

## Objetivo

Representar de manera integral el recorrido que sigue una solicitud desde que es registrada por un usuario hasta que la respuesta generada por el modelo de Inteligencia Artificial es entregada nuevamente al solicitante.

Este diagrama constituye la representación oficial del flujo operativo de la solución desarrollada durante el taller y resume la interacción entre todos los componentes tecnológicos involucrados.

---

# Descripción

El procesamiento comienza cuando un usuario registra una solicitud mediante Google Forms.

La información es almacenada automáticamente en Google Sheets y queda disponible para su procesamiento.

El puente local `puente_local.py` consulta el Web App de Google Apps Script, obtiene una solicitud pendiente y la envía a Ollama para su procesamiento mediante el modelo de lenguaje seleccionado.

Una vez generada la respuesta, ésta retorna al flujo de automatización, se almacena nuevamente en Google Sheets y finalmente es enviada al usuario mediante correo electrónico.

---

# Componentes involucrados

| Etapa | Componente | Función |
|--------|------------|---------|
| 1 | Usuario | Registra la solicitud. |
| 2 | Google Forms | Captura la información. |
| 3 | Google Sheets | Almacena los datos. |
| 4 | Apps Script | Coordina el flujo automático. |
| 5 | Python | Actúa como puente hacia Ollama. |
| 6 | Ollama | Ejecuta el modelo de IA. |
| 7 | Google Sheets | Registra la respuesta obtenida. |
| 8 | Gmail | Envía la respuesta al usuario. |

---

# Secuencia detallada

| Paso | Acción                                                                 |
| ---- | ---------------------------------------------------------------------- |
| 1    | El usuario completa el formulario.                                     |
| 2    | Google Forms almacena la información.                                  |
| 3    | Google Sheets registra una nueva fila.                                 |
| 4    | Apps Script detecta una solicitud pendiente.                           |
| 5    | `puente_local.py` consulta el Web App.<br>                             |
| 6    | Apps Script identifica una solicitud pendiente en Google Sheets.       |
| 7    | El Web App devuelve la solicitud a `puente_local.py`.<br>              |
| 8    | `puente_local.py` consulta a Ollama.<br>                               |
| 9    | Ollama ejecuta el modelo de lenguaje.<br>                              |
| 10   | `puente_local.py` recibe la respuesta.<br>                             |
| 11   | `puente_local.py` devuelve la respuesta al Web App.<br>                |
| 12   | Apps Script actualiza Google Sheets y realiza el envío mediante Gmail. |
| 13   | El proceso queda registrado para futuras consultas.                    |

---

# Entradas del proceso

| Entrada                | Origen                                                                    |
| ---------------------- | ------------------------------------------------------------------------- |
| Consulta del usuario   | Google Forms                                                              |
| Contexto del asistente | Google Sheets                                                             |
| System Prompt          | Configuración del asistente / archivo utilizado por el flujo automatizado |
| Modelo de IA           | Ollama                                                                    |

---

# Salidas del proceso

| Salida | Destino |
|---------|---------|
| Respuesta generada | Google Sheets |
| Correo electrónico | Usuario |
| Registro histórico | Google Sheets |

---

# Puntos de control

Durante el procesamiento se recomienda verificar los siguientes aspectos.

| Punto de control          | Objetivo                                                        |
| ------------------------- | --------------------------------------------------------------- |
| Formulario recibido       | Confirmar que la información esté completa.                     |
| Comunicación HTTP         | Verificar la comunicación entre el Web App y `puente_local.py`. |
| Estado de Ollama          | Confirmar disponibilidad del modelo.                            |
| Registro en Google Sheets | Validar el almacenamiento de la respuesta.                      |
| Envío de correo           | Confirmar la entrega del resultado al usuario.                  |

---

# Riesgos del proceso

| Riesgo                   | Impacto | Mitigación                                                                   |
| ------------------------ | ------- | ---------------------------------------------------------------------------- |
| Error de conexión        | Alto    | Verificar la ejecución de `puente_local.py` y la disponibilidad del Web App. |
| Modelo no disponible     | Alto    | Confirmar la instalación de Ollama.                                          |
| Error en Apps Script     | Medio   | Revisar los registros de ejecución.                                          |
| Error en Google Forms    | Bajo    | Validar el formulario antes de su publicación.                               |
| Error de envío por Gmail | Medio   | Verificar permisos y cuotas del servicio.                                    |

---

# Indicadores sugeridos

| Indicador | Objetivo |
|------------|----------|
| Tiempo promedio de respuesta | Medir el rendimiento del sistema. |
| Solicitudes procesadas | Evaluar el nivel de utilización. |
| Solicitudes con error | Detectar fallas recurrentes. |
| Tiempo de disponibilidad | Monitorear la estabilidad del servicio. |

---

# Buenas prácticas

- Mantener una única versión del flujo de procesamiento.
- Documentar cualquier modificación realizada al proceso.
- Validar cada componente antes de realizar pruebas integrales.
- Supervisar periódicamente el rendimiento del modelo de lenguaje.
- Registrar los cambios importantes mediante control de versiones.

---

# Relación con la colección

| Documento | Relación |
|------------|----------|
| Libro del Participante | Arquitectura general del proyecto. |
| Manual Técnico | Capítulos 7, 8, 9 y 10. |
| Manual del Proyecto Integrador | Plantillas A.4, A.5 y A.6. |
| Cuaderno de Laboratorios | Laboratorios 4, 5 y 6. |

---

# Referencia técnica

El presente diagrama constituye la representación oficial del flujo operativo completo de la solución desarrollada durante el taller.

Toda adaptación futura del sistema deberá mantener este flujo como referencia o documentar explícitamente las modificaciones introducidas, asegurando la trazabilidad y la coherencia entre la arquitectura, la implementación y la documentación técnica.

---

# D7

# Arquitectura de referencia para una eventual implementación

---

## Objetivo

Presentar una arquitectura de referencia para una eventual evolución del prototipo hacia un entorno de operación organizacional, identificando componentes y aspectos que deberían considerarse antes de su implementación.

Este diagrama representa una arquitectura de referencia para una eventual implementación de la solución en un entorno organizacional.

---

# Descripción

En una eventual evolución del prototipo hacia un entorno de operación organizacional, los distintos componentes podrían interactuar de forma automatizada para recibir solicitudes, procesarlas mediante Inteligencia Artificial Local y entregar respuestas a los usuarios.

El flujo operativo mantendría la arquitectura utilizada durante el desarrollo, incorporando actividades de monitoreo, mantenimiento y actualización del sistema.

El flujo operativo mantiene la misma arquitectura utilizada durante el desarrollo, incorporando ahora actividades de monitoreo, mantenimiento y actualización del sistema.

---

# Diagrama

```text
                     Usuarios
                         │
                         ▼
                  Google Forms
                         │
                         ▼
                 Google Sheets
                         │
                         ▼
              Google Apps Script
                         │
                         ▼
                 puente_local.py
                         │
                         ▼
                     Ollama
                         │
                         ▼
               Modelo de Lenguaje
                         │
                         ▼
              Google Apps Script
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
      Google Sheets            Gmail
              │                     │
              └──────────┬──────────┘
                         ▼
                      Usuarios

--------------------------------------------------------

        Administración y mantenimiento

     Monitoreo • Actualizaciones • Respaldos
```

---

# Componentes

| Componente         | Función                                           |
| ------------------ | ------------------------------------------------- |
| Usuarios           | Utilizan la solución durante la operación normal. |
| Google Forms       | Punto de entrada de las solicitudes.              |
| Google Sheets      | Repositorio operativo de información.             |
| Google Apps Script | Automatización del proceso.                       |
| Ollama             | Ejecución local del modelo de IA.                 |
| Gmail              | Entrega automática de respuestas.                 |

---

# Procesos de soporte

Durante la operación normal deberán realizarse periódicamente las siguientes actividades.

| Actividad                     | Frecuencia sugerida |
| ----------------------------- | ------------------- |
| Respaldo de Google Sheets     | Semanal             |
| Actualización de modelos      | Según necesidad     |
| Revisión de registros         | Semanal             |
| Validación del flujo completo | Mensual             |

---

# Disponibilidad esperada

Para asegurar un funcionamiento estable se recomienda verificar regularmente los siguientes aspectos.

| Elemento                    | Verificación |
| --------------------------- | ------------ |
| Espacio disponible en disco | Adecuado     |
| Memoria RAM disponible      | Adecuada     |
| Estado de Ollama            | Operativo    |
| Estado de Apps Script       | Operativo    |

---

# Riesgos operacionales

| Riesgo                           | Acción recomendada                          |
| -------------------------------- | ------------------------------------------- |
| Detención de `puente_local.py`   | Reiniciar la ejecución del puente local.    |
| Modelo eliminado accidentalmente | Restaurar desde respaldo.                   |
| Cambios en Google Forms          | Verificar compatibilidad con Google Sheets. |
| Cambios en Apps Script           | Ejecutar pruebas de integración.            |
| Saturación de memoria RAM        | Utilizar modelos de menor tamaño.           |

---

# Buenas prácticas

- Mantener respaldos periódicos de la documentación y del código fuente.
- Registrar todas las modificaciones importantes.
- Documentar las versiones utilizadas.
- Supervisar el funcionamiento del sistema antes de realizar actualizaciones.
- Conservar un ambiente de pruebas independiente del ambiente de operación.

---

# Relación con la colección

| Documento | Relación |
|------------|----------|
| Libro del Participante | Arquitectura general. |
| Manual Técnico | Capítulos 8, 9 y 10. |
| Manual del Proyecto Integrador | Plantillas A.4, A.5 y A.6. |
| Cuaderno de Laboratorios | Laboratorios 5 y 6. |

---

# Referencia técnica

La arquitectura presentada corresponde al escenario recomendado para la operación de la solución desarrollada durante el taller.

En implementaciones futuras podrán incorporarse nuevos componentes, siempre que se mantenga la coherencia general de la arquitectura y se documente cualquier modificación relevante.

---

# D8

# Arquitectura metodológica del Proyecto Integrador

---

## Objetivo

Representar la secuencia metodológica utilizada durante el desarrollo del Proyecto Integrador, mostrando la evolución progresiva del trabajo realizado por el estudiante desde la identificación del problema hasta la presentación profesional de la solución desarrollada.

Este diagrama resume la metodología de trabajo utilizada durante todo el taller y constituye la referencia oficial para comprender la relación existente entre los distintos documentos generados durante el proyecto.

---

# Descripción

El Proyecto Integrador se desarrolla mediante una secuencia progresiva de actividades.

Cada etapa utiliza como punto de partida el resultado obtenido en la etapa anterior, permitiendo construir gradualmente una solución organizacional basada en Inteligencia Artificial Local.

La metodología utilizada privilegia la construcción incremental, la validación continua y la documentación permanente del proyecto.

---

# Diagrama

```text
                 Problema
                     │
                     ▼
        Definición del problema
              (Plantilla A.1)
                     │
                     ▼
       Diseño del asistente IA
              (Plantilla A.2)
                     │
                     ▼
     Validación y optimización
              (Plantilla A.3)
                     │
                     ▼
 Integración con herramientas
        digitales (Plantilla A.4)
                     │
                     ▼
 Diseño del proceso organizacional
              (Plantilla A.5)
                     │
                     ▼
 Informe Ejecutivo y
 Presentación Profesional
      (Plantilla A.6)
```

---

# Etapas del proyecto

| Etapa | Resultado obtenido |
|--------|--------------------|
| Definición del problema | Problema claramente delimitado. |
| Diseño del asistente | Especificación funcional del asistente. |
| Validación | Asistente optimizado mediante pruebas. |
| Integración | Solución conectada con herramientas digitales. |
| Proceso organizacional | Solución contextualizada dentro de la organización. |
| Presentación profesional | Proyecto consolidado y documentado. |

---

# Productos generados

Durante el desarrollo del Proyecto Integrador se construyen los siguientes documentos.

|Documento|Plantilla|Producto|
|---|---|---|
|Documento 1|A.1|Definición del problema y alcance|
|Documento 2|A.2|Diseño del asistente inteligente|
|Documento 3|A.3|Validación y optimización|
|Documento 4|A.4|Integración con herramientas digitales|
|Documento 5|A.5|Diseño del proceso organizacional|
|Documento 6|A.6|Informe ejecutivo y presentación profesional|

En conjunto, estos documentos conforman el expediente técnico del proyecto.

---

# Competencias desarrolladas

Cada etapa incorpora nuevas competencias profesionales.

| Etapa | Competencia principal |
|--------|-----------------------|
| A.1 | Análisis de problemas. |
| A.2 | Diseño de soluciones basadas en IA. |
| A.3 | Validación y mejora continua. |
| A.4 | Integración tecnológica. |
| A.5 | Diseño de procesos organizacionales. |
| A.6 | Comunicación profesional y documentación técnica. |

---

# Principios metodológicos

La metodología del Proyecto Integrador se sustenta en los siguientes principios.

- Construcción incremental.
- Validación permanente.
- Documentación continua.
- Trazabilidad de las decisiones.
- Integración progresiva.
- Mejora continua.
- Enfoque centrado en la organización.
- Uso responsable de la Inteligencia Artificial.

---

# Factores críticos de éxito

| Factor | Descripción |
|----------|-------------|
| Coherencia | Mantener alineadas todas las etapas del proyecto. |
| Evidencia | Documentar cada decisión relevante. |
| Validación | Evaluar continuamente el comportamiento del asistente. |
| Integración | Garantizar la comunicación entre todos los componentes. |
| Comunicación | Presentar claramente la solución desarrollada. |

---

# Buenas prácticas

- Construir el proyecto de manera secuencial.
- Evitar comenzar una etapa sin haber finalizado la anterior.
- Mantener actualizado el expediente técnico.
- Registrar todas las mejoras implementadas.
- Respaldar periódicamente la documentación del proyecto.
- Conservar la trazabilidad entre las distintas versiones.

---

# Relación con la colección

| Documento | Relación |
|------------|----------|
| Libro del Participante | Proporciona los fundamentos conceptuales de cada etapa. |
| Manual Técnico | Explica la implementación de los componentes técnicos. |
| Cuaderno de Laboratorios | Permite desarrollar progresivamente el proyecto. |
| Manual del Proyecto Integrador | Contiene toda la documentación generada durante el proceso. |

---

# Referencia técnica

El presente diagrama representa la metodología oficial utilizada durante el desarrollo del taller.

Más que una secuencia de actividades, constituye una guía para la construcción de soluciones organizacionales apoyadas por Inteligencia Artificial Local, integrando aspectos técnicos, metodológicos y documentales dentro de un único proceso de trabajo.

---

# Cierre del Capítulo

Los ocho diagramas presentados en este capítulo constituyen la representación gráfica oficial de la solución desarrollada durante el taller.

En conjunto describen:

- la arquitectura general del sistema;
- los principales componentes tecnológicos;
- los flujos de información;
- la arquitectura de operación;
- la metodología utilizada para desarrollar el Proyecto Integrador.

Se recomienda utilizar estos diagramas como referencia durante futuras implementaciones, adaptaciones o actividades de mantenimiento de la solución.


