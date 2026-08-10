# Capítulo 4

# Solución de problemas (Troubleshooting)

---

## Objetivo

Proporcionar una guía de consulta rápida para identificar, diagnosticar y resolver los problemas más frecuentes que pueden presentarse durante la instalación, configuración, integración y operación de la solución desarrollada en esta colección.

El propósito de este capítulo es disminuir los tiempos de diagnóstico, facilitar la recuperación del sistema y documentar las soluciones verificadas durante el desarrollo del taller.

---

# Cómo utilizar este capítulo

Los problemas se encuentran organizados según el componente donde normalmente se producen.

Cada registro incorpora:

- síntoma observado;
- posibles causas;
- procedimiento recomendado;
- acciones preventivas.

Antes de realizar modificaciones importantes en la configuración del sistema, se recomienda verificar si el problema ya se encuentra documentado en este capítulo.

---

# Organización del capítulo

| Sección | Contenido                    |
| ------- | ---------------------------- |
| T4.1    | Ollama                       |
| T4.2    | Open WebUI                   |
| T4.3    | Python                       |
| T4.4    | Google Apps Script           |
| T4.5    | Google Forms y Google Sheets |
| T4.6    | Integración completa         |

---

# T4.1

# Problemas frecuentes en Ollama

---

## Problema 1

### Síntoma

El comando `ollama list` no muestra modelos disponibles.

### **Posibles causas**

- Todavía no se ha descargado ningún modelo.
- Los modelos esperados no se encuentran disponibles en la instalación actual.

### **Procedimiento recomendado**

1. Verificar si se ha descargado previamente algún modelo.
2. Descargar el modelo requerido mediante `ollama pull`.
3. Ejecutar nuevamente `ollama list`.

### **Prevención**  
Verificar la disponibilidad del modelo requerido antes de comenzar las actividades.

---

## Problema 2

### Síntoma

El modelo demora excesivamente en responder.

### Posibles causas

- Memoria RAM insuficiente.
- Procesador con alta carga.
- Modelo demasiado grande para el equipo.

### Procedimiento recomendado

- Cerrar aplicaciones innecesarias.
- Utilizar un modelo de menor tamaño.
- Reiniciar el equipo antes de ejecutar nuevas pruebas.

### Prevención

Seleccionar el modelo considerando las características del computador.

---

# T4.2

# Problemas frecuentes en Open WebUI

---

## Problema 1

### Síntoma

La interfaz web no carga.

### Posibles causas

- El servicio no está iniciado.
- Puerto incorrecto.
- Firewall bloqueando la conexión.

### Procedimiento recomendado

- Verificar que Open WebUI esté ejecutándose.
- Confirmar el puerto utilizado.
- Reiniciar el servicio.

### Prevención

Comprobar el funcionamiento antes de comenzar el desarrollo del asistente.

---

## Problema 2

### Síntoma

El modelo personalizado no responde correctamente.

### Posibles causas

- Ollama no está disponible.
- Modelo base no disponible o no seleccionado.
- Error de comunicación entre Open WebUI y Ollama.

### Procedimiento recomendado

- Confirmar que Ollama se encuentra operativo.
- Verificar que el modelo base utilizado se encuentre disponible.
- Revisar la configuración del modelo personalizado.

---

# T4.3

# Problemas frecuentes en Python

---

## Problema 1

### Síntoma

`puente_local.py` no inicia correctamente.

### Posibles causas

- Error de sintaxis en el script.
- Python no se encuentra disponible en el entorno.
- Biblioteca `requests` no disponible.
- Configuración incorrecta de las URL utilizadas por el puente.

### Procedimiento recomendado

- Revisar el mensaje de error mostrado en la terminal.
- Verificar la instalación de Python.
- Comprobar que la biblioteca `requests` se encuentre disponible.
- Revisar las URL configuradas en `puente_local.py`.

---

## Problema 2

### Síntoma

`puente_local.py` no obtiene una solicitud desde el Web App.

### Posibles causas

- URL del Web App incorrecta.
- Implementación del Web App desactualizada.
- No existen solicitudes con estado `PENDIENTE`.
- Error de comunicación con el Web App.

### Procedimiento recomendado

- Verificar la URL configurada en `puente_local.py`.
- Confirmar que se encuentre implementada la versión actual del Web App.
- Revisar en Google Sheets que exista una solicitud con estado `PENDIENTE`.
- Ejecutar nuevamente `puente_local.py` y revisar el mensaje mostrado en la terminal.

---

# T4.4

# Problemas frecuentes en Google Apps Script

---

## Problema 1

### Síntoma

El script finaliza con error de autorización.

### Posibles causas

- Permisos pendientes.
- Servicios de Google sin autorización.

### Procedimiento recomendado

- Ejecutar nuevamente el script.
- Aceptar todos los permisos solicitados.
- Verificar la cuenta utilizada.

---

## Problema 2

### Síntoma

No se registra la respuesta en Google Sheets.

### Posibles causas

- Error en la escritura.
- Cambio en la estructura de la hoja.
- Columna inexistente.

### Procedimiento recomendado

- Revisar los nombres de las columnas.
- Confirmar la hoja utilizada.
- Ejecutar nuevamente la prueba.

---

## Problema 3

### Síntoma

La solicitud aparece con estado `ERROR` en Google Sheets.

### Posibles causas

- La respuesta recibida está vacía.
- El número de fila recibido no es válido.
- Se produjo un error durante el registro o envío del correo.

### Procedimiento recomendado

- Revisar las ejecuciones de Google Apps Script.
- Verificar los datos de la fila correspondiente.
- Comprobar que exista una dirección de correo válida.
- Corregir el problema y ejecutar nuevamente una solicitud de prueba.

---

# T4.5

# Problemas frecuentes en Google Forms y Google Sheets

---

## Problema 1

### Síntoma

Las respuestas no aparecen en Google Sheets.

### Posibles causas

- Formulario sin vinculación.
- Hoja incorrecta.

### Procedimiento recomendado

- Revisar la configuración del formulario.
- Confirmar la hoja asociada.

---

## Problema 2

### Síntoma

Los datos aparecen incompletos.

### Posibles causas

- Campos obligatorios mal configurados.
- Error durante el envío.

### Procedimiento recomendado

- Revisar el formulario.
- Ejecutar una nueva prueba.

---

# T4.6

# Problemas de integración

---

## Problema 1

### Síntoma

El flujo completo no finaliza correctamente.

### Posibles causas

- Error en alguno de los componentes.
- Comunicación interrumpida.
- Configuración inconsistente.

### Procedimiento recomendado

Verificar secuencialmente:

1. Google Forms.
2. Registro de la solicitud en Google Sheets.
3. Google Apps Script / Web App.
4. `puente_local.py`.
5. Ollama y modelo de lenguaje.
6. Devolución de la respuesta al Web App.
7. Registro de la respuesta en Google Sheets.
8. Envío mediante Gmail.

---

## Problema 2

### Síntoma

El usuario no recibe el correo electrónico.

### Posibles causas

- Error durante el envío.
- Dirección incorrecta.
- Restricciones del servicio Gmail.

### Procedimiento recomendado

- Revisar los registros de Apps Script.
- Confirmar la dirección de correo.
- Ejecutar una prueba manual.

---

# Árbol de diagnóstico rápido

Utilice el siguiente procedimiento cuando se presente un problema durante la operación.

```text
¿El usuario envió el formulario?
        │
        ▼
¿La solicitud llegó a Google Sheets?
        │
        ▼
¿Existe una solicitud con estado PENDIENTE?
        │
        ▼
¿El Web App permite obtener la solicitud?
        │
        ▼
¿puente_local.py obtuvo la solicitud?
        │
        ▼
¿Ollama generó una respuesta?
        │
        ▼
¿puente_local.py devolvió la respuesta al Web App?
        │
        ▼
¿La respuesta quedó registrada en Google Sheets?
        │
        ▼
¿Gmail envió el correo?
        │
        ▼
Flujo completado
```

---

# Recomendaciones generales

- Realizar pruebas parciales antes de ejecutar el flujo completo.
- Registrar los errores detectados durante el desarrollo.
- Mantener respaldos del código fuente.
- Documentar cualquier modificación relevante.
- Validar el funcionamiento después de cada cambio importante.

---

# Relación con la colección

| Documento | Relación |
|------------|----------|
| Libro del Participante | Identificación de componentes del sistema. |
| Manual Técnico | Procedimientos de instalación, configuración y validación. |
| Manual del Proyecto Integrador | Evidencias de pruebas y validación. |
| Cuaderno de Laboratorios | Resolución de problemas durante las actividades prácticas. |

---

# Cierre del capítulo

La resolución sistemática de problemas constituye una competencia fundamental durante la implementación de soluciones organizacionales basadas en Inteligencia Artificial.

Los procedimientos descritos en este capítulo permiten abordar de forma ordenada los incidentes más habituales, facilitando el diagnóstico, reduciendo los tiempos de recuperación y contribuyendo a mantener la estabilidad de la solución desarrollada durante el taller.

--- 
