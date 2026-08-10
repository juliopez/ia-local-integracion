# Capítulo 5

# Glosario técnico

---

## Objetivo

Presentar las definiciones de los principales conceptos técnicos utilizados a lo largo de esta colección, proporcionando un lenguaje común que facilite la comprensión de los contenidos desarrollados en el Libro del Participante, el Manual Técnico, el Cuaderno de Laboratorios y el Manual del Proyecto Integrador.

El presente glosario no pretende reemplazar la documentación oficial de cada tecnología, sino entregar definiciones prácticas y contextualizadas al alcance del lector.

---

# Cómo utilizar este capítulo

Los términos se encuentran organizados en orden alfabético.

Cada definición incluye:

- concepto;
- definición;
- contexto de utilización dentro del taller.

Cuando un término aparezca por primera vez en cualquiera de los demás volúmenes, el lector podrá consultar este capítulo para ampliar su significado.

---

# Glosario

---

## API

**Definición**

Conjunto de reglas y mecanismos que permiten la comunicación entre aplicaciones o servicios.

**Contexto**

Durante el taller, `puente_local.py` utiliza solicitudes HTTP para comunicarse con el Web App de Google Apps Script y con la API local de Ollama.

---

## Apps Script

**Definición**

Plataforma de desarrollo de Google utilizada para automatizar tareas dentro de Google Workspace.

**Contexto**

Publicado como Web App, permite consultar solicitudes pendientes, recibir las respuestas generadas y coordinar su registro en Google Sheets y envío mediante Gmail.

---

## Asistente Inteligente

**Definición**

Sistema basado en un modelo de lenguaje diseñado para ejecutar tareas específicas siguiendo instrucciones previamente definidas.

**Contexto**

Es el elemento central desarrollado durante el Proyecto Integrador.

---

## Contexto

**Definición**

Información adicional utilizada por el modelo de lenguaje para interpretar correctamente una solicitud.

**Contexto**

Puede incorporarse mediante el System Prompt o directamente en la consulta enviada al modelo.

---

## Flujo de trabajo

**Definición**

Secuencia organizada de actividades necesarias para ejecutar un proceso.

**Contexto**

La solución desarrollada automatiza un flujo organizacional completo.

---

## Google Forms

**Definición**

Herramienta de Google Workspace utilizada para capturar información mediante formularios electrónicos.

**Contexto**

Constituye el punto de entrada de las solicitudes del usuario.

---

## Google Sheets

**Definición**

Hoja de cálculo utilizada para almacenar y administrar la información del proyecto.

**Contexto**

Registra solicitudes, respuestas y estados del proceso.

---

## Inteligencia Artificial Local

**Definición**

Enfoque en el que los modelos de Inteligencia Artificial se ejecutan en infraestructura local, sin depender de servicios externos de IA generativa para realizar la inferencia.

**Contexto**

Durante el taller, la inferencia del modelo de lenguaje se realiza localmente mediante Ollama.

---

## JSON

**Definición**

Formato de intercambio de información ampliamente utilizado entre aplicaciones.

**Contexto**

Las respuestas entre Python y Google Apps Script se intercambian utilizando este formato.

---

## Modelo de Lenguaje

**Definición**

Modelo de Inteligencia Artificial entrenado para comprender y generar lenguaje natural.

**Contexto**

Es ejecutado localmente mediante Ollama.

---

## Ollama

**Definición**

Aplicación que permite descargar, administrar y ejecutar modelos de lenguaje directamente desde un computador personal.

**Contexto**

Constituye el motor de inferencia utilizado durante el proyecto.

---

## Open WebUI

**Definición**

Interfaz gráfica basada en navegador que facilita la interacción con modelos de lenguaje ejecutados mediante Ollama.

**Contexto**

Se utiliza para configurar modelos personalizados, definir instrucciones mediante el _System Prompt_ y realizar pruebas de funcionamiento.

---

## Portafolio

**Definición**

Conjunto organizado de documentos que evidencian el desarrollo del Proyecto Integrador.

**Contexto**

Se construye progresivamente mediante las Plantillas A.1 a A.6.

---

## Prompt

**Definición**

Instrucción enviada a un modelo de lenguaje para solicitar una respuesta.

**Contexto**

Puede corresponder a una consulta realizada por un usuario o a una instrucción generada automáticamente por el sistema.

---

## Proyecto Integrador

**Definición**

Actividad central del taller donde el estudiante desarrolla una solución organizacional basada en Inteligencia Artificial Local.

**Contexto**

Integra los conocimientos adquiridos durante todo el proceso formativo.

---

## Python

**Definición**

Lenguaje de programación utilizado para desarrollar `puente_local.py`, componente encargado de comunicar el Web App de Google Apps Script con Ollama.

**Contexto**

Consulta solicitudes pendientes, las envía a Ollama y devuelve las respuestas generadas al Web App.

---

## Respuesta

**Definición**

Resultado generado por el modelo de lenguaje como consecuencia del procesamiento de una solicitud.

**Contexto**

Es registrada en Google Sheets y posteriormente enviada al usuario.

---

## System Prompt

**Definición**

Conjunto de instrucciones que definen el comportamiento general de un asistente inteligente mientras se encuentran configuradas.

**Contexto**

Determina el rol, las restricciones y el estilo de respuesta del modelo.

---

## Trazabilidad

**Definición**

Capacidad para reconstruir la evolución de un proyecto mediante el registro de sus distintas versiones y evidencias.

**Contexto**

Es uno de los principios metodológicos del Proyecto Integrador.

---

## Validación

**Definición**

Proceso destinado a verificar que el asistente inteligente cumple los objetivos definidos durante su diseño.

**Contexto**

Se desarrolla principalmente mediante la Plantilla A.3 del Manual del Proyecto Integrador.

---

# Recomendaciones

- Consultar este glosario cuando aparezcan términos desconocidos.
- Mantener actualizadas las definiciones si se incorporan nuevas herramientas al proyecto.
- Utilizar la terminología de forma consistente en toda la documentación.

---

# Relación con la colección

| Documento | Relación                                                     |
|------------|----------|
| Libro del Participante | Definición de conceptos fundamentales.                       |
| Manual Técnico | Apoyo durante la configuración técnica de la solución.       |
| Manual del Proyecto Integrador | Terminología utilizada en las plantillas.                    |
| Cuaderno de Laboratorios | Consulta durante el desarrollo de las actividades prácticas. |

---

# Cierre del capítulo

El dominio de la terminología técnica constituye un elemento fundamental para comprender la arquitectura, la implementación y la documentación de soluciones basadas en Inteligencia Artificial Local.

Las definiciones incluidas en este capítulo establecen un vocabulario común para toda la colección, favoreciendo la comunicación técnica y la correcta interpretación de los distintos procedimientos descritos en los demás volúmenes.

---
