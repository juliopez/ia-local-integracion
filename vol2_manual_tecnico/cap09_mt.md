# Parte IV

# Consolidación y presentación de la solución organizacional

---

# Capítulo 9

# Consolidación y operación del servicio inteligente

## 9.1 Revisión de la arquitectura final

### Objetivo

Revisar la arquitectura completa del servicio inteligente, identificar la función de cada componente y comprobar que todas las partes de la solución se encuentran correctamente integradas antes de establecer los procedimientos de operación.

---

### Tiempo estimado

**20 minutos**

---

### Requisitos previos

Antes de comenzar esta sección deberá haber completado:

- Capítulo 7 – Integración del asistente con Google Forms.
- Capítulo 8 – Integración del asistente inteligente con Google Apps Script.

Además, deberá disponer de:

- Google Forms operativo;
- Google Sheets vinculado al formulario;
- proyecto de Google Apps Script publicado;
- puente local en Python configurado;
- Ollama instalado y funcionando;
- modelo de lenguaje disponible;
- archivo `system_prompt.txt` actualizado;
- permisos de Gmail autorizados;
- servicio inteligente automatizado y validado.

---

### Procedimiento

Durante las partes anteriores del manual, el proyecto fue construido progresivamente.

Primero se preparó el entorno local.

Posteriormente se diseñó y validó el asistente inteligente.

Finalmente, el asistente fue integrado con Google Workspace mediante un proceso automatizado.

Antes de establecer los procedimientos de operación, es necesario revisar la arquitectura completa y confirmar que cada componente cumple una responsabilidad claramente definida.

---

## Paso 1. Revisar la evolución del proyecto

La solución evolucionó mediante las siguientes etapas:

```text
Entorno local

↓

Asistente inteligente

↓

Flujo de captura

↓

Servicio automatizado

↓

Solución organizacional
```

Cada etapa incorporó una capacidad nueva sin reemplazar los componentes anteriores.

---

## Paso 2. Revisar la arquitectura final

La arquitectura completa del servicio inteligente es la siguiente:

```text
                    Usuario
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
            Puente local en Python
                        │
                        ▼
                     Ollama
                        │
                        ▼
             Modelo de lenguaje
                        │
                        ▼
          Respuesta del asistente
                        │
                        ▼
             Google Apps Script
                  │             │
                  ▼             ▼
           Google Sheets      Gmail
                                  │
                                  ▼
                               Usuario
```

Esta arquitectura combina servicios en la nube con componentes ejecutados localmente.

---

## Paso 3. Identificar los componentes en la nube

Los siguientes componentes se ejecutan dentro del ecosistema de Google:

| Componente | Función |
|---|---|
| Google Forms | Capturar las solicitudes enviadas por los usuarios. |
| Google Sheets | Almacenar solicitudes, respuestas y estados del proceso. |
| Google Apps Script | Coordinar el intercambio de información. |
| Gmail | Entregar la respuesta al usuario. |

Estos componentes requieren conexión a Internet y acceso a la cuenta de Google utilizada durante el proyecto.

---

## Paso 4. Identificar los componentes locales

Los siguientes componentes funcionan en el computador responsable del procesamiento:

| Componente | Función |
|---|---|
| Python | Ejecutar el puente local. |
| `puente_local.py` | Recuperar solicitudes y coordinar el procesamiento local. |
| Ollama | Ejecutar el modelo de lenguaje. |
| Modelo de lenguaje | Generar la respuesta. |
| `system_prompt.txt` | Mantener las instrucciones permanentes del asistente. |

El equipo local debe permanecer encendido y operativo mientras el servicio se encuentre disponible.

---

## Paso 5. Identificar las entradas del sistema

El servicio recibe la siguiente información desde Google Forms:

| Entrada | Propósito |
|---|---|
| Nombre | Personalizar la respuesta. |
| Tipo de consulta | Proporcionar contexto. |
| Consulta | Contenido que será procesado. |
| Correo electrónico | Entregar el resultado al usuario. |

La marca temporal es generada automáticamente y se utiliza para mantener la trazabilidad de cada solicitud.

---

## Paso 6. Identificar el procesamiento

El procesamiento se desarrolla mediante la siguiente secuencia:

```text
Solicitud pendiente

↓

Lectura de datos

↓

Construcción del mensaje

↓

Aplicación de instrucciones permanentes

↓

Ejecución del modelo local

↓

Generación de respuesta

↓

Registro del resultado

↓

Envío al usuario
```

Cada etapa deberá completarse correctamente para que la solicitud finalice con el estado:

```text
ENVIADA
```

---

## Paso 7. Identificar las salidas del sistema

El servicio genera tres resultados principales:

| Salida | Destino |
|---|---|
| Respuesta generada | Google Sheets |
| Correo enviado | Usuario |
| Estado del procesamiento | Google Sheets |

La hoja de cálculo constituye el principal registro operativo del servicio.

---

## Paso 8. Revisar los estados del proceso

La columna **Estado** permite identificar la situación de cada solicitud.

| Estado       | Interpretación                                   |
| ------------ | ------------------------------------------------ |
| `PENDIENTE`  | La solicitud está disponible para procesamiento. |
| `PROCESANDO` | El puente local recuperó la solicitud.           |
| `ENVIADA`    | La respuesta fue entregada al usuario.           |
| `ERROR`      | El proceso no pudo finalizar correctamente.      |

El estado permite supervisar el flujo sin revisar manualmente cada componente.

---

## Paso 9. Identificar las dependencias principales

El funcionamiento del servicio depende de que:

- el formulario acepte respuestas;
- Google Sheets mantenga su estructura;
- la aplicación web de Apps Script permanezca publicada;
- la URL de la aplicación web configurada en el puente local sea válida;
- el puente local se encuentre ejecutándose;
- Ollama esté disponible;
- el modelo configurado continúe instalado;
- Gmail disponga de autorización y cuota disponible.

La interrupción de cualquiera de estos componentes puede detener el proceso completo.

---

## Paso 10. Completar la ficha de arquitectura

Documente la configuración actual del proyecto.

| Elemento                          | Información del proyecto |
| --------------------------------- | ------------------------ |
| Nombre del servicio               |                          |
| Estado operativo                  |                          |
| Formulario utilizado              |                          |
| Hoja de respuestas                |                          |
| Proyecto de Apps Script           |                          |
| URL de la aplicación web          |                          |
| Archivo del puente local          |                          |
| Modelo de lenguaje                |                          |
| Ubicación del `system_prompt.txt` |                          |
| Cuenta responsable                |                          |
| Equipo local responsable          |                          |

> **Importante:** No registre contraseñas, credenciales ni otros datos sensibles en esta ficha.

---

💡 **Nota técnica 9.1**

La arquitectura combina componentes locales y servicios en la nube.

Por esta razón, el servicio no puede considerarse completamente disponible si el computador local, Ollama o el puente en Python se encuentran detenidos, aunque Google Forms continúe recibiendo solicitudes.

---

### Verificación

Complete la siguiente tabla:

| Verificación | Estado |
|---|:---:|
| Identifiqué los componentes en la nube | ☐ |
| Identifiqué los componentes locales | ☐ |
| Comprendo las entradas del sistema | ☐ |
| Comprendo el proceso completo | ☐ |
| Identifiqué las salidas | ☐ |
| Comprendo los estados operativos | ☐ |
| Identifiqué las dependencias principales | ☐ |
| Completé la ficha de arquitectura | ☐ |

---

### Problemas frecuentes

#### Confundo Open WebUI con el componente de automatización

Open WebUI continúa utilizándose para diseñar, configurar y probar el asistente.

El flujo automatizado consulta directamente la API local de Ollama e incorpora las instrucciones permanentes desde `system_prompt.txt`.

---

#### Google Forms recibe respuestas, pero no se procesan

Esto puede ocurrir si:

- el puente local está detenido;
- Ollama no está disponible;
- la solicitud no posee el estado `PENDIENTE`;
- existe un error de comunicación con Apps Script.

---

#### No sé cuál componente genera la respuesta

La respuesta es generada por el modelo de lenguaje ejecutado mediante Ollama.

Google Apps Script y Python únicamente coordinan el proceso.

---

#### La arquitectura documentada no coincide con la implementación

Actualice la documentación antes de establecer los procedimientos operativos.

La arquitectura debe representar fielmente el sistema vigente.

---

### Buenas prácticas

- Mantenga actualizada la arquitectura técnica.
- Documente cada cambio relevante.
- Diferencie claramente los componentes locales y los servicios en la nube.
- No registre contraseñas, credenciales ni información sensible en diagramas o documentos públicos.
- Revise la arquitectura después de cada actualización importante.
- Mantenga un único diagrama oficial y actualizado de la arquitectura.

---

### Checklist

Antes de continuar confirme que:

☐ Comprende la arquitectura completa del servicio.

☐ Identifica la responsabilidad de cada componente.

☐ Conoce las dependencias operativas.

☐ Comprende el recorrido completo de una solicitud.

☐ La documentación representa el estado vigente del servicio.

☐ El proyecto está preparado para elaborar su inventario técnico.

---

## 9.2 Inventario de componentes de la solución

### Objetivo

Construir un inventario técnico de los componentes utilizados por el servicio inteligente, registrando software, versiones, modelos, scripts, archivos de configuración y servicios asociados para facilitar su mantenimiento, reproducción y recuperación.

---

### Tiempo estimado

**25 minutos**

---

### Requisitos previos

Antes de comenzar esta sección deberá haber completado:

- Sección 9.1 – Revisión de la arquitectura final.

Además, deberá disponer de acceso al equipo y a las cuentas utilizadas durante la implementación del servicio.

---

### Procedimiento

Un servicio inteligente depende de múltiples componentes que pueden actualizarse, reemplazarse o dejar de funcionar con el tiempo.

Si esta información no se encuentra documentada, será difícil:

- reproducir el entorno;
- identificar incompatibilidades;
- recuperar el servicio después de un fallo;
- transferir su administración a otra persona;
- determinar qué componente debe actualizarse.

En esta sección elaborará un inventario técnico que represente el estado real de la solución.

---

## Paso 1. Identificar el sistema operativo

Registre el sistema operativo utilizado por el computador local.

Complete la siguiente tabla:

| Elemento | Información |
|---|---|
| Sistema operativo | |
| Edición | |
| Versión | |
| Arquitectura | 64 bits |
| Fecha de revisión | |

Para consultar esta información en Windows puede ejecutar:

```text
winver
```

o revisar:

```text
Configuración

↓

Sistema

↓

Información
```

---

## Paso 2. Registrar Ollama

Abra PowerShell y ejecute:

```powershell
ollama --version
```

Registre el resultado:

| Elemento | Información |
|---|---|
| Software | Ollama |
| Versión instalada | |
| Estado | Operativo / No operativo |
| Fecha de instalación o revisión | |
| Fuente oficial | Sitio oficial de Ollama |

No es necesario registrar la ubicación interna de todos sus archivos en este inventario.

Para complementar el contenido desarrollado en esta sección, consulte el Manual del Proyecto Integrador, donde encontrará las plantillas y documentos de apoyo correspondientes.

---

## Paso 3. Registrar los modelos instalados

Ejecute:

```powershell
ollama list
```

Complete la siguiente tabla:

| Modelo | Identificador | Tamaño | Uso dentro del proyecto |
|---|---|---:|---|
| | | | Principal |
| | | | Alternativo |
| | | | Pruebas |

Identifique claramente cuál corresponde al modelo utilizado por el servicio.

El nombre deberá coincidir exactamente con el configurado en:

```python
MODELO_OLLAMA = "nombre-del-modelo"
```

---

## Paso 4. Registrar Python

Ejecute:

```powershell
python --version
```

Luego ejecute:

```powershell
python -m pip --version
```

Registre:

| Elemento | Información |
|---|---|
| Software | Python |
| Versión instalada | |
| Versión de `pip` | |
| Uso dentro del proyecto | Ejecución del puente local |
| Estado | Operativo / No operativo |

---

## Paso 5. Registrar las dependencias de Python

El puente local utiliza paquetes adicionales.

Ejecute:

```powershell
python -m pip show requests
```

Registre:

| Paquete | Versión | Propósito |
|---|---|---|
| `requests` | | Comunicación HTTP con Apps Script y Ollama |

Si el proyecto incorpora posteriormente nuevas dependencias, agréguelas al inventario.

---

## Paso 6. Crear un archivo de dependencias

Desde la carpeta donde se encuentra el puente local ejecute:

```powershell
python -m pip freeze > requirements.txt
```

Este comando generará un archivo con las dependencias instaladas.

Verifique que exista:

```text
Taller_IA_Local
│
└── 03_Scripts
    ├── puente_local.py
    ├── system_prompt.txt
    └── requirements.txt
```

> **Importante:** El archivo `requirements.txt` puede incluir paquetes que no pertenecen exclusivamente al proyecto si se utiliza una instalación general de Python. Durante la revisión técnica final se evaluará si resulta conveniente crear un entorno virtual específico.

---

## Paso 7. Registrar Open WebUI

Aunque el flujo automatizado consulta directamente Ollama, Open WebUI sigue formando parte del entorno porque permite:

- configurar asistentes;
- realizar pruebas manuales;
- administrar conversaciones;
- validar las instrucciones permanentes.

Registre:

| Elemento | Información |
|---|---|
| Software | Open WebUI |
| Versión instalada | |
| Método de instalación | Python / `pip` |
| Dirección local | `http://localhost:8080` |
| Función dentro del proyecto | Diseño y validación del asistente |
| Estado | Operativo / No operativo |

Para consultar información sobre el paquete instalado puede ejecutar:

```powershell
python -m pip show open-webui
```

---

## Paso 8. Registrar el puente local

Complete la siguiente ficha:

| Elemento                     | Información             |
| ---------------------------- | ----------------------- |
| Archivo                      | `puente_local.py`       |
| Ubicación                    |                         |
| Lenguaje                     | Python                  |
| Responsable                  |                         |
| Fecha de última modificación |                         |
| Estado                       | Operativo / En revisión |


---

## Paso 9. Registrar las instrucciones permanentes

Complete:

| Elemento                      | Información |
|---|---|
| Archivo                       | `system_prompt.txt` |
| Ubicación                     | |
| Estado del asistente          | |
| Fecha de última actualización | |
| Responsable de aprobación     | |
| Estado                        | Vigente / En revisión |

El contenido de este archivo debe coincidir con la configuración estable documentada durante los capítulos 5 y 6.

---

## Paso 10. Registrar Google Forms

Complete la ficha del punto de captura:

| Elemento | Información |
|---|---|
| Nombre del formulario | |
| Propietario | |
| Cuenta responsable | |
| Estado de recepción | Habilitado / Deshabilitado |
| Cantidad de campos | 4 |
| Fecha de revisión | |

No es necesario copiar el enlace público del formulario dentro de documentos que serán distribuidos externamente.

---

## Paso 11. Registrar Google Sheets

Complete:

| Elemento | Información |
|---|---|
| Nombre de la hoja de cálculo | |
| Nombre de la pestaña de respuestas | |
| Cuenta propietaria | |
| Columnas utilizadas | 8 |
| Estado | Operativa / En revisión |
| Fecha de revisión | |

La estructura esperada es:

| Posición | Columna |
|---:|---|
| 1 | Marca temporal |
| 2 | Nombre |
| 3 | Tipo de consulta |
| 4 | Consulta |
| 5 | Correo electrónico |
| 6 | Estado |
| 7 | Respuesta IA |
| 8 | Fecha de procesamiento |

---

## Paso 12. Registrar Google Apps Script

Complete:

| Elemento | Información |
|---|---|
| Nombre del proyecto | |
| Archivo principal | `Code.gs` |
| Cuenta propietaria | |
| Tipo de implementación | Aplicación web |
| Estado | Publicada / En desarrollo |
| Fecha de última implementación | |
| Versión publicada | |
| Responsable | |

La URL de la aplicación web deberá almacenarse en un registro técnico protegido y no en documentación pública.

---

## Paso 13. Registrar Gmail

Complete:

| Elemento | Información |
|---|---|
| Cuenta remitente | |
| Servicio utilizado | GmailApp |
| Estado de autorización | Autorizado / Pendiente |
| Uso dentro del proyecto | Envío de respuestas |
| Fecha de revisión de permisos | |

No registre la contraseña de la cuenta.

---

## Paso 14. Registrar los archivos del proyecto

Revise la carpeta principal:

```text
Taller_IA_Local
│
├── 01_Documentacion
├── 02_Modelos
├── 03_Scripts
├── 04_Proyecto_Integrador
├── 05_Respaldos
└── 06_Recursos
```

Complete el inventario documental:

| Archivo o carpeta | Ubicación | Estado | Observaciones |
|---|---|---|---|
| `puente_local.py` | | | |
| `system_prompt.txt` | | | |
| `requirements.txt` | | | |
| `google_apps_script.gs` | | | |
| Especificación técnica | | | |
| Historial de evolución | | | |
| Registro de validación | | | |
| Arquitectura final | | | |
| Matriz de riesgos | Pendiente | | |

---

## Paso 15. Consolidar el inventario técnico

Utilice la siguiente tabla como resumen:

| Categoría | Componente | Versión o identificación | Función | Estado |
|---|---|---|---|---|
| Sistema | Windows | | Plataforma local | |
| IA local | Ollama | | Ejecución del modelo | |
| Modelo | | | Generación de respuestas | |
| Interfaz | Open WebUI | | Diseño y pruebas | |
| Lenguaje | Python | | Ejecución del puente | |
| Dependencia | `requests` | | Comunicación HTTP | |
| Script local | `puente_local.py` | | Integración local | |
| Configuración | `system_prompt.txt` | | Instrucciones permanentes | |
| Captura | Google Forms | | Recepción de solicitudes | |
| Datos | Google Sheets | | Registro y control | |
| Integración | Google Apps Script | | Coordinación del proceso | |
| Entrega | Gmail | | Envío de respuestas | |

---

## Paso 16. Asignar una fecha de revisión

Todo inventario técnico debe indicar cuándo fue actualizado.

Registre:

```text
Fecha de elaboración:

Responsable:

Próxima fecha de revisión:
```

Se recomienda revisar el inventario:

- después de una actualización importante;
- cuando cambie el modelo;
- cuando se modifique un script;
- antes de una demostración;
- al transferir la solución a otro responsable.

---

💡 **Nota técnica 9.2**

Un inventario técnico no contiene secretos de acceso.

Debe registrar qué componentes existen, qué versiones se utilizan y qué función cumple cada uno, pero nunca debe incluir contraseñas, claves privadas o credenciales personales.

---

### Verificación

Complete la siguiente tabla:

| Verificación | Estado |
|---|:---:|
| Registré el sistema operativo | ☐ |
| Registré la versión de Ollama | ☐ |
| Identifiqué el modelo principal | ☐ |
| Registré Python y sus dependencias | ☐ |
| Registré Open WebUI | ☐ |
| Documenté el puente local | ☐ |
| Documenté el System Prompt | ☐ |
| Registré los componentes de Google Workspace | ☐ |
| Verifiqué la estructura de archivos | ☐ |
| Consolidé el inventario técnico | ☐ |
| Asigné una fecha de revisión | ☐ |

---

### Problemas frecuentes

#### No conozco la versión de un componente

Utilice los comandos o las opciones de información descritas en esta sección.

Si no puede determinarla, registre:

```text
Pendiente de verificación
```

No invente el dato.

---

#### El modelo configurado no aparece en `ollama list`

Revise la configuración de `MODELO_OLLAMA`.

El servicio no podrá procesar solicitudes si el modelo indicado no se encuentra instalado.

---

#### Existen varios archivos con nombres similares

Identifique cuál corresponde al archivo vigente.

Mueva las versiones antiguas a la carpeta:

```text
05_Respaldos
```

---

#### El archivo `requirements.txt` contiene demasiados paquetes

Esto puede ocurrir cuando Python se utiliza para múltiples proyectos.

Registre la observación y evalúe posteriormente el uso de un entorno virtual.

---

#### No sé quién es el responsable de un componente

No deje el campo vacío.

Registre:

```text
Responsable pendiente de asignación
```

La ausencia de responsables constituye un riesgo operativo.

---

### Buenas prácticas

- Mantenga un único inventario oficial y actualizado.
- Registre fechas de actualización.
- Identifique claramente el modelo principal.
- Documente dependencias y archivos.
- Separe configuraciones vigentes y respaldos.
- No incluya credenciales.
- Actualice el inventario después de cada cambio relevante.
- Verifique la información mediante comandos y evidencias.

---

### Checklist

Antes de continuar confirme que:

☐ Todos los componentes están identificados.

☐ Las versiones principales fueron registradas.

☐ El modelo utilizado está claramente definido.

☐ Los scripts y archivos de configuración están localizados.

☐ Los servicios de Google Workspace están documentados.

☐ No se incluyeron claves ni contraseñas.

☐ El inventario representa el estado vigente del servicio.

☐ El proyecto está preparado para definir su procedimiento de inicio.

---

## 9.3 Procedimiento de inicio del servicio

### Objetivo

Establecer y ejecutar un procedimiento ordenado para iniciar el servicio inteligente, verificando que todos sus componentes se encuentren disponibles antes de habilitar el procesamiento de solicitudes.

---

### Tiempo estimado

**20 minutos**

---

### Requisitos previos

Antes de comenzar esta sección deberá haber completado:

- Sección 9.1 – Revisión de la arquitectura final.
- Sección 9.2 – Inventario de componentes de la solución.

Además, deberá disponer de:

- acceso al computador local responsable del procesamiento;
- Ollama instalado;
- modelo de lenguaje disponible;
- puente local configurado;
- proyecto de Google Apps Script publicado;
- formulario y hoja de respuestas operativos;
- conexión estable a Internet.

---

### Procedimiento

El servicio inteligente depende de componentes locales y servicios en la nube.

Por este motivo, el orden de inicio es importante.

Iniciar el sistema sin verificar previamente sus dependencias puede provocar:

- solicitudes detenidas en estado `PENDIENTE`;
- registros bloqueados en estado `PROCESANDO`;
- errores de comunicación;
- respuestas incompletas;
- correos no enviados.

El procedimiento de inicio deberá ejecutarse siempre antes de habilitar el servicio para usuarios reales.

---

## Paso 1. Verificar la conexión a Internet

Abra el navegador y compruebe que puede acceder correctamente a:

- Google Forms;
- Google Sheets;
- Google Apps Script;
- Gmail.

La conexión a Internet será necesaria para intercambiar información con los servicios de Google.

---

## Paso 2. Verificar el estado del equipo local

Antes de iniciar los componentes, confirme que el computador:

- se encuentra conectado a la corriente, si corresponde;
- dispone de memoria suficiente;
- posee espacio libre en disco;
- no está ejecutando actualizaciones pendientes;
- no tiene aplicaciones innecesarias consumiendo recursos.

Cierre programas que puedan afectar el rendimiento del modelo.

---

## Paso 3. Verificar Python

Abra PowerShell.

Ejecute:

```powershell
python --version
```

La salida deberá mostrar una versión compatible.

Ejemplo:

```text
Python 3.11.x
```

Luego verifique la dependencia principal:

```powershell
python -m pip show requests
```

Si el paquete no se encuentra instalado, ejecute:

```powershell
python -m pip install requests
```

---

## Paso 4. Verificar Ollama

Ejecute:

```powershell
ollama --version
```

Posteriormente revise los modelos disponibles:

```powershell
ollama list
```

Confirme que el modelo configurado en `puente_local.py` aparece en la lista.

La configuración deberá coincidir exactamente con:

```python
MODELO_OLLAMA = "nombre-del-modelo"
```

---

## Paso 5. Verificar el servicio local de Ollama

Abra el navegador e ingrese:

```text
http://localhost:11434
```

El servicio deberá responder indicando que Ollama se encuentra disponible.

También puede realizar una prueba desde PowerShell:

```powershell
ollama run nombre-del-modelo
```

Ingrese una consulta breve.

Ejemplo:

```text
Responde únicamente con la palabra OPERATIVO.
```

Si el modelo responde correctamente, finalice la prueba.

---

## Paso 6. Verificar los archivos del puente local

Acceda a:

```text
Taller_IA_Local
│
└── 03_Scripts
```

Compruebe que se encuentran disponibles:

```text
puente_local.py

system_prompt.txt

requirements.txt
```

Revise que `system_prompt.txt` no se encuentre vacío.

No modifique las instrucciones permanentes durante el procedimiento de inicio.

---

## Paso 7. Verificar la configuración del puente

Abra `puente_local.py`.

Revise únicamente los parámetros de configuración:

```python
URL_APPS_SCRIPT = "URL_DE_LA_APLICACION_WEB"
URL_OLLAMA = "http://localhost:11434/api/chat"
MODELO_OLLAMA = "nombre-del-modelo"
```

Confirme que:

- la URL corresponde a la implementación vigente;
- la URL de Ollama utiliza el puerto correcto;
- el modelo coincide con `ollama list`;

---

## Paso 8. Verificar Google Sheets

Abra la hoja de respuestas.

Confirme que conserva la estructura esperada:

| Posición | Columna |
|---:|---|
| 1 | Marca temporal |
| 2 | Nombre |
| 3 | Tipo de consulta |
| 4 | Consulta |
| 5 | Correo electrónico |
| 6 | Estado |
| 7 | Respuesta IA |
| 8 | Fecha de procesamiento |

Compruebe que no se hayan:

- eliminado columnas;
- cambiado encabezados;
- desplazado datos;
- incorporado columnas intermedias.

---

## Paso 9. Revisar solicitudes pendientes

Filtre o revise la columna **Estado**.

Identifique registros en:

```text
PENDIENTE

PROCESANDO

ERROR
```

Antes de iniciar el puente:

- confirme que las solicitudes `PENDIENTE` pueden procesarse;
- revise las filas detenidas en `PROCESANDO`;
- analice los registros en `ERROR`.

No restablezca estados sin conocer la causa del problema.

---

## Paso 10. Verificar la aplicación web de Apps Script

Abra la URL publicada de Google Apps Script en el navegador para comprobar que la aplicación web se encuentra disponible.

La dirección tendrá una estructura similar a:

```text
https://script.google.com/macros/s/IDENTIFICADOR/exec
```

Si no existen solicitudes pendientes, la respuesta esperada será similar a:

```json
{"disponible":false,"mensaje":"No existen solicitudes pendientes."}
```

Si la aplicación web no responde correctamente, revise:

- la URL utilizada;
- la implementación publicada;
- el nivel de acceso configurado;
- los registros de ejecución de Google Apps Script.

---

## Paso 11. Verificar Gmail

Ejecute manualmente la función de prueba creada anteriormente:

```text
pruebaCorreo
```

Utilice una dirección controlada.

Confirme que:

- el correo fue enviado;
- el mensaje llegó correctamente;
- no existen errores de autorización;
- la cuenta dispone de cuota disponible.

No realice múltiples pruebas innecesarias.

---

## Paso 12. Iniciar el puente local

Abra PowerShell en la carpeta:

```text
Taller_IA_Local
│
└── 03_Scripts
```

Ejecute:

```powershell
python puente_local.py
```

La salida inicial deberá ser similar a:

```text
Puente local iniciado.
Presione CTRL+C para detenerlo.
```

Si no existen solicitudes pendientes, deberá observar:

```text
No existen solicitudes pendientes.
```

Mantenga esta ventana abierta mientras el servicio se encuentre operativo.

---

## Paso 13. Ejecutar una prueba controlada

Antes de habilitar el formulario para usuarios reales, envíe una solicitud de prueba.

Utilice:

- nombre identificable como prueba;
- categoría válida;
- consulta breve;
- correo controlado.

Ejemplo:

```text
Nombre: PRUEBA DE INICIO

Tipo de consulta: Contenidos

Consulta: Responde brevemente qué función cumple este servicio.

Correo: dirección de prueba
```

---

## Paso 14. Verificar el ciclo completo

Compruebe que la solicitud sigue esta secuencia:

```text
PENDIENTE

↓

PROCESANDO

↓

ENVIADA
```

Verifique además:

- respuesta almacenada;
- fecha de procesamiento;
- correo recibido;
- ausencia de errores en Python;
- ausencia de errores en Apps Script.

---

## Paso 15. Habilitar la recepción de solicitudes

Solo después de completar satisfactoriamente la prueba controlada:

- habilite el formulario;
- comparta el enlace con los usuarios autorizados;
- informe el horario de disponibilidad;
- mantenga el puente local funcionando;
- supervise las primeras solicitudes.

---

## Lista resumida de inicio

El procedimiento completo puede resumirse así:

```text
1. Verificar Internet.

2. Verificar el computador.

3. Verificar Python.

4. Verificar Ollama.

5. Confirmar el modelo.

6. Revisar archivos y configuración.

7. Verificar Google Sheets.

8. Revisar estados pendientes.

9. Verificar Apps Script.

10. Verificar Gmail.

11. Iniciar el puente local.

12. Ejecutar una prueba controlada.

13. Habilitar el servicio.
```

---

💡 **Nota técnica 9.3**

El formulario puede continuar recibiendo respuestas aunque el equipo local esté apagado.

Sin embargo, dichas solicitudes permanecerán sin procesar hasta que Ollama y el puente local vuelvan a estar operativos.

Por ello, el horario de disponibilidad del servicio debe comunicarse claramente a los usuarios.

---

### Verificación

Complete la siguiente tabla:

| Verificación | Estado |
|---|:---:|
| La conexión a Internet funciona | ☐ |
| El computador está preparado | ☐ |
| Python responde correctamente | ☐ |
| Ollama está operativo | ☐ |
| El modelo configurado está instalado | ☐ |
| Los archivos del puente están disponibles | ☐ |
| La configuración fue revisada | ☐ |
| Google Sheets conserva su estructura | ☐ |
| Las solicitudes pendientes fueron revisadas | ☐ |
| Apps Script responde correctamente | ☐ |
| Gmail está autorizado | ☐ |
| El puente local fue iniciado | ☐ |
| La prueba controlada fue exitosa | ☐ |
| El servicio quedó habilitado | ☐ |

---

### Problemas frecuentes

#### El puente no inicia

Revise:

- la versión de Python;
- la instalación de `requests`;
- la ruta del archivo;
- los valores de configuración;
- los mensajes de error en PowerShell.

---

#### Ollama funciona, pero el modelo no aparece

Ejecute:

```powershell
ollama list
```

Compruebe el nombre exacto.

Si es necesario, descargue nuevamente el modelo:

```powershell
ollama pull nombre-del-modelo
```


---

#### Existen solicitudes antiguas en `PROCESANDO`

Revise los registros antes de modificar el estado.

Si confirma que el procesamiento fue interrumpido, restablezca la fila a:

```text
PENDIENTE
```

y supervise su nueva ejecución.

---

#### La prueba genera respuesta, pero no envía correo

Revise:

- dirección del destinatario;
- autorización de Gmail;
- cuotas;
- implementación vigente de Apps Script;
- registro de ejecución.

---

#### El servicio funciona sin ejecutar Open WebUI

Es correcto.

El flujo automatizado consulta directamente la API local de Ollama.

Open WebUI continúa siendo la herramienta utilizada para diseñar y probar manualmente el asistente.

---

### Buenas prácticas

- Utilice siempre una lista de inicio.
- Ejecute una prueba antes de abrir el servicio.
- No habilite el formulario si el entorno local no está disponible.
- Mantenga visible la consola del puente.
- Revise solicitudes detenidas antes de iniciar.
- Proteja la configuración.
- Informe horarios de operación.
- Documente cualquier incidencia detectada durante el inicio.

---

### Checklist

Antes de continuar confirme que:

☐ Existe un procedimiento de inicio documentado.

☐ Todos los componentes fueron verificados.

☐ La prueba controlada finalizó con estado `ENVIADA`.

☐ El puente permanece operativo.

☐ Los usuarios conocen la disponibilidad del servicio.

☐ El servicio puede comenzar su operación controlada.

---

## 9.4 Procedimiento de cierre del servicio

### Objetivo

Establecer un procedimiento ordenado para finalizar la operación del servicio inteligente, garantizando que todas las solicitudes hayan sido procesadas, que la información quede correctamente registrada y que los componentes locales puedan detenerse de forma segura.

---

### Tiempo estimado

**20 minutos**

---

### Requisitos previos

Antes de comenzar esta sección deberá haber completado:

- Sección 9.3 – Procedimiento de inicio del servicio.

Además, el servicio debe encontrarse en funcionamiento.

---

### Procedimiento

Así como un servicio debe iniciarse de forma controlada, también debe finalizar correctamente.

Detener el computador sin revisar el estado del sistema puede provocar:

- solicitudes sin procesar;
- registros incompletos;
- estados inconsistentes;
- pérdida de trazabilidad;
- dificultades para reanudar la operación posteriormente.

Por esta razón, el cierre del servicio debe seguir siempre una secuencia definida.

---

## Paso 1. Suspender temporalmente la recepción de nuevas solicitudes

Si el formulario será utilizado únicamente durante un horario determinado, informe previamente a los usuarios que el servicio dejará de procesar nuevas consultas.

Cuando corresponda, deshabilite temporalmente la recepción de respuestas desde Google Forms.

Esta medida evita que ingresen nuevas solicitudes mientras el sistema está siendo detenido.

---

## Paso 2. Revisar solicitudes pendientes

Abra Google Sheets.

Revise la columna **Estado**.

Complete la siguiente tabla.

| Estado       | Acción                                             |
| ------------ | -------------------------------------------------- |
| `PENDIENTE`  | Determinar si será procesada antes del cierre.     |
| `PROCESANDO` | Verificar que el procesamiento haya finalizado.    |
| `ENVIADA`    | No requiere acción adicional.                      |
| `ERROR`      | Registrar el incidente para su revisión posterior. |

No cierre el servicio mientras existan solicitudes cuyo procesamiento deba completarse.

---

## Paso 3. Esperar la finalización del procesamiento

Observe la consola del puente local.

Espere hasta que aparezca un mensaje similar a:

```text
No existen solicitudes pendientes.
```

Este mensaje indica que el puente no ha encontrado nuevas solicitudes para procesar.

---

## Paso 4. Confirmar el estado final

Revise nuevamente Google Sheets.

Idealmente, todas las solicitudes procesadas durante la jornada deberán encontrarse en el estado:

```text
ENVIADA
```

Si existen registros en estado `ERROR`, no los elimine.

Manténgalos registrados para su análisis posterior.

---

## Paso 5. Registrar incidencias

Complete una bitácora sencilla con los eventos relevantes ocurridos durante la operación.

Ejemplo:

| Hora | Incidencia | Acción realizada | Estado |
|---|---|---|---|
| | | | |

Algunas incidencias posibles:

- error de comunicación;
- interrupción de Internet;
- modelo no disponible;
- correo no enviado;
- solicitud duplicada.

Esta información facilitará el mantenimiento del servicio.

---

## Paso 6. Respaldar los archivos modificados

Si durante la operación se realizaron cambios, respalde los archivos correspondientes.

Revise especialmente:

```text
puente_local.py

system_prompt.txt

Code.gs
```

Copie los archivos vigentes a la carpeta:

```text
05_Respaldos
```

Asigne un nombre descriptivo.

Ejemplo:

```text
puente_local_27-08-2026.py
```

---

## Paso 7. Registrar cambios realizados

Si el proyecto fue modificado durante la operación, complete un registro similar al siguiente.

| Fecha | Componente | Cambio realizado | Responsable |
|---|---|---|---|
| | | | |

Este registro facilitará la trazabilidad de los cambios.

---

## Paso 8. Detener el puente local

Regrese a la ventana de PowerShell donde se ejecuta:

```powershell
python puente_local.py
```

Presione:

```text
CTRL + C
```

La salida esperada será similar a:

```text
Puente local detenido.
```

Espere algunos segundos antes de cerrar la ventana.

---

## Paso 9. Verificar que el puente se detuvo correctamente

Confirme que:

- la consola ya no muestra nuevas consultas;
- el proceso finalizó sin errores;
- no existen mensajes pendientes.

No cierre la ventana mientras el proceso continúe ejecutándose.

---

## Paso 10. Cerrar aplicaciones auxiliares

Una vez detenido el puente, cierre las aplicaciones utilizadas durante la operación.

Por ejemplo:

- PowerShell;
- navegador (si no será utilizado);
- Open WebUI (cuando corresponda).

No es necesario detener Ollama manualmente si continuará siendo utilizado para otras actividades.

---

## Paso 11. Actualizar el registro operativo

Complete la siguiente ficha.

| Elemento | Información |
|---|---|
| Fecha | |
| Hora de inicio | |
| Hora de cierre | |
| Solicitudes procesadas | |
| Solicitudes con error | |
| Responsable | |
| Observaciones | |

Este registro permitirá conocer la utilización del servicio a lo largo del tiempo.

---

## Paso 12. Confirmar el cierre del servicio

Antes de abandonar el equipo, verifique que:

- el puente local está detenido;
- no existen solicitudes en proceso;
- los respaldos fueron realizados;
- la documentación quedó actualizada;
- los archivos fueron guardados.

---

## Resumen del procedimiento de cierre

El cierre completo puede resumirse mediante la siguiente secuencia:

```text
Suspender recepción

↓

Revisar solicitudes

↓

Esperar finalización

↓

Registrar incidencias

↓

Respaldar archivos

↓

Actualizar documentación

↓

Detener puente local

↓

Cerrar aplicaciones

↓

Registrar cierre
```

---

💡 **Nota técnica 9.4**

El cierre del servicio no implica eliminar la información almacenada.

Google Forms, Google Sheets y Google Apps Script permanecerán disponibles.

Únicamente se detendrá el procesamiento automático ejecutado localmente mediante el puente en Python.

---

### Verificación

Complete la siguiente tabla.

| Verificación | Estado |
|---|:---:|
| La recepción fue suspendida cuando correspondía | ☐ |
| Se revisaron las solicitudes pendientes | ☐ |
| No quedaron procesos activos | ☐ |
| Las incidencias fueron registradas | ☐ |
| Los archivos fueron respaldados | ☐ |
| El puente local fue detenido | ☐ |
| La documentación fue actualizada | ☐ |
| El registro operativo fue completado | ☐ |

---

### Problemas frecuentes

#### Existen solicitudes en estado `PROCESANDO`

No detenga inmediatamente el servicio.

Revise la consola del puente.

Si el proceso fue interrumpido, documente la situación y restablezca posteriormente el estado según el procedimiento definido.

---

#### Olvidé respaldar los cambios

Antes de apagar el equipo, copie los archivos modificados a la carpeta de respaldos.

Evite mantener una única copia de trabajo.

---

#### El puente continúa ejecutándose

Compruebe que realmente presionó:

```text
CTRL + C
```

Espere la confirmación:

```text
Puente local detenido.
```

---

#### Existen solicitudes con estado `ERROR`

No elimine estos registros.

Documente la incidencia y analícela antes de volver a procesar la solicitud.

---

### Buenas prácticas

- Finalice siempre el procesamiento antes de detener el servicio.
- Mantenga una bitácora de incidencias.
- Realice respaldos periódicos.
- Mantenga la trazabilidad de los cambios realizados en los scripts.
- No cierre aplicaciones abruptamente.
- Documente cualquier modificación realizada durante la operación.
- Revise el estado final de las solicitudes antes de abandonar el equipo.

---

### Checklist

Antes de continuar confirme que:

☐ El servicio fue detenido correctamente.

☐ No existen solicitudes pendientes de procesamiento.

☐ Los respaldos fueron realizados.

☐ La documentación quedó actualizada.

☐ El registro operativo fue completado.

☐ El entorno está preparado para reiniciar el servicio cuando sea necesario.

---

## 9.5 Monitoreo y control de solicitudes

### Objetivo

Implementar un procedimiento de monitoreo que permita supervisar el funcionamiento cotidiano del servicio inteligente, identificar oportunamente problemas de procesamiento y mantener la continuidad operativa mediante el seguimiento de los estados de cada solicitud.

---

### Tiempo estimado

**25 minutos**

---

### Requisitos previos

Antes de comenzar esta sección deberá haber completado:

- Sección 9.4 – Procedimiento de cierre del servicio.

Además, deberá disponer de un servicio operativo o de registros previamente procesados en Google Sheets.

---

### Procedimiento

Una vez que el servicio entra en operación, el trabajo del responsable no consiste únicamente en mantener el computador encendido.

También debe supervisar continuamente el estado del proceso para detectar oportunamente:

- solicitudes detenidas;
- errores de comunicación;
- respuestas incompletas;
- problemas de disponibilidad;
- comportamientos anómalos.

El monitoreo constituye una actividad permanente durante la operación del servicio.

---

## Paso 1. Identificar el panel principal de monitoreo

El principal panel de control del servicio corresponde a la hoja de respuestas de Google Sheets.

En ella es posible visualizar:

- solicitudes recibidas;
- estado actual;
- respuestas generadas;
- fecha de procesamiento.

No será necesario utilizar herramientas adicionales para realizar un monitoreo básico.

---

## Paso 2. Revisar la columna Estado

La columna **Estado** resume la situación de cada solicitud.

| Estado       | Interpretación                   | Acción recomendada                           |
| ------------ | -------------------------------- | -------------------------------------------- |
| `PENDIENTE`  | Esperando procesamiento          | Supervisar el tiempo de espera               |
| `PROCESANDO` | Solicitud en ejecución           | Confirmar que el puente continúa funcionando |
| `ENVIADA`    | Proceso finalizado correctamente | No requiere intervención                     |
| `ERROR`      | Fallo durante el procesamiento   | Analizar la causa                            |

La mayor parte de las solicitudes deberían finalizar en estado:

```text
ENVIADA
```

---

## Paso 3. Detectar solicitudes detenidas

Revise si existen solicitudes que permanecen durante un tiempo prolongado en alguno de los siguientes estados:

```text
PENDIENTE

PROCESANDO
```

Estas situaciones pueden indicar:

- puente local detenido;
- Ollama no disponible;
- pérdida de conexión;
- error de configuración.

No asuma inmediatamente que existe un problema técnico.

Primero confirme el horario de funcionamiento del servicio.

---

## Paso 4. Supervisar los registros con error

Filtre la hoja utilizando:

```text
Estado = ERROR
```

Para cada registro complete la siguiente ficha.

| Elemento | Información |
|---|---|
| Número de fila | |
| Fecha | |
| Consulta | |
| Posible causa | |
| Acción correctiva | |
| Estado final | |

No elimine las filas con error.

Constituyen evidencia útil para mejorar el servicio.

---

## Paso 5. Revisar la consola del puente local

Mientras el servicio permanezca operativo, supervise periódicamente la ventana de PowerShell.

Algunos mensajes esperados son:

```text
Procesando la fila 12...

Fila 12 procesada correctamente.
```

o bien:

```text
No existen solicitudes pendientes.
```

La aparición reiterada de mensajes de error requiere una revisión inmediata.

---

## Paso 6. Revisar el registro de Apps Script

Acceda al proyecto de Google Apps Script.

Revise periódicamente:

```text
Ejecuciones
```

Observe especialmente:

- errores repetitivos;
- tiempos de ejecución elevados;
- autorizaciones pendientes;
- excepciones no controladas.

Estos registros permiten identificar problemas que no siempre son visibles desde Google Sheets.

---

## Paso 7. Verificar la calidad de las respuestas

El monitoreo no debe limitarse al funcionamiento técnico.

Seleccione aleatoriamente algunas respuestas enviadas.

Revise:

- claridad;
- pertinencia;
- coherencia;
- cumplimiento de las restricciones;
- tono utilizado por el asistente.

Complete una tabla similar.

| Criterio | Cumple | Observaciones |
|---|:---:|---|
| Responde la consulta | ☐ | |
| Utiliza lenguaje apropiado | ☐ | |
| Respeta el alcance definido | ☐ | |
| Mantiene la identidad del asistente | ☐ | |

---

## Paso 8. Revisar tiempos de procesamiento

Seleccione varias solicitudes procesadas durante la jornada.

Calcule de manera aproximada el tiempo transcurrido entre:

- recepción;
- procesamiento;
- envío.

No es necesario medir tiempos con precisión de milisegundos.

El objetivo consiste en detectar variaciones importantes.

Ejemplo:

| Solicitud | Tiempo aproximado |
|---|---|
| 1 | 20 segundos |
| 2 | 18 segundos |
| 3 | 25 segundos |

Cambios significativos pueden indicar problemas de rendimiento.

---

## Paso 9. Detectar solicitudes duplicadas

Revise si existen:

- consultas idénticas;
- múltiples envíos del mismo usuario;
- registros procesados más de una vez.

Cuando corresponda, documente la situación.

No elimine registros sin antes verificar su origen.

---

## Paso 10. Elaborar un informe de monitoreo

Al finalizar la jornada, complete un resumen como el siguiente.

| Indicador | Valor |
|---|---:|
| Solicitudes recibidas | |
| Solicitudes enviadas | |
| Solicitudes con error | |
| Solicitudes pendientes | |
| Tiempo promedio estimado | |
| Incidencias registradas | |

Este informe permitirá evaluar la estabilidad del servicio.

---

## Flujo de monitoreo

El proceso cotidiano puede resumirse mediante la siguiente secuencia.

```text
Revisar Google Sheets

↓

Analizar Estados

↓

Revisar PowerShell

↓

Revisar Apps Script

↓

Evaluar respuestas

↓

Registrar incidencias

↓

Generar informe
```

---

💡 **Nota técnica 9.5**

El monitoreo no consiste únicamente en detectar errores.

También permite identificar oportunidades de mejora, evaluar el comportamiento del asistente y anticipar problemas antes de que afecten a los usuarios.

---

### Verificación

Complete la siguiente tabla.

| Verificación | Estado |
|---|:---:|
| Revisé los estados del proceso | ☐ |
| Identifiqué solicitudes detenidas | ☐ |
| Analicé registros con error | ☐ |
| Revisé la consola del puente | ☐ |
| Revisé Apps Script | ☐ |
| Evalué la calidad de respuestas | ☐ |
| Revisé tiempos de procesamiento | ☐ |
| Elaboré el informe de monitoreo | ☐ |

---

### Problemas frecuentes

#### Existen muchas solicitudes en estado `PENDIENTE`

Verifique:

- si el puente local está ejecutándose;
- si Ollama permanece disponible;
- si el horario operativo aún está vigente.

---

#### Las respuestas son correctas, pero tardan demasiado

Revise:

- carga del computador;
- tamaño del modelo;
- cantidad de solicitudes simultáneas.

No modifique el modelo sin documentar el cambio.

---

#### Se repiten errores similares

No corrija únicamente cada caso.

Busque la causa común.

Podría tratarse de un problema de configuración o de un componente específico.

---

#### El servicio parece funcionar correctamente, pero los usuarios reportan problemas

Revise algunos correos enviados.

El funcionamiento técnico no garantiza una buena experiencia de usuario.

---

### Buenas prácticas

- Revise periódicamente Google Sheets.
- Analice los errores antes de reprocesar solicitudes.
- Evalúe la calidad de las respuestas.
- Registre incidencias relevantes.
- Mantenga un historial de monitoreo.
- Documente cualquier cambio realizado durante la operación.
- Utilice la información recopilada para mejorar el servicio.

---

### Checklist

Antes de continuar confirme que:

☐ Existe un procedimiento de monitoreo definido.

☐ Las solicitudes pueden supervisarse fácilmente.

☐ Los errores quedan documentados.

☐ Se evalúa tanto el funcionamiento técnico como la calidad de las respuestas.

☐ El servicio puede mantenerse de manera controlada.

☐ El proyecto está preparado para definir su estrategia de respaldo y recuperación.

---

## 9.6 Respaldo y recuperación del servicio

### Objetivo

Definir un procedimiento de respaldo y recuperación que permita proteger los componentes críticos del servicio inteligente, conservar respaldos estables y restablecer la solución ante fallos, pérdidas de información o modificaciones no deseadas.

---

### Tiempo estimado

**30 minutos**

---

### Requisitos previos

Antes de comenzar esta sección deberá haber completado:

- Sección 9.5 – Monitoreo y control de solicitudes.

Además, deberá disponer de acceso a:

- archivos locales del proyecto;
- Google Forms;
- Google Sheets;
- Google Apps Script;
- documentación técnica;
- historial de evolución.

---

### Procedimiento

El servicio inteligente depende de archivos, configuraciones y servicios distribuidos entre el computador local y el ecosistema de Google.

Una falla puede afectar únicamente un componente o interrumpir el proceso completo.

Por este motivo, el respaldo no debe limitarse a copiar un único archivo.

Es necesario identificar qué elementos deben protegerse, con qué frecuencia se respaldarán y cómo se utilizarán para recuperar el servicio.

---

## Paso 1. Identificar los componentes críticos

Revise la arquitectura del servicio e identifique los elementos cuya pérdida impediría su funcionamiento.

Los principales componentes críticos son:

| Componente | Consecuencia de su pérdida |
|---|---|
| `puente_local.py` | Se interrumpe la comunicación con Ollama. |
| `system_prompt.txt` | Se pierde la configuración estable del asistente. |
| `requirements.txt` | Se dificulta reconstruir el entorno de Python. |
| `google_apps_script.gs` | Se pierde la lógica de integración en la nube. |
| Google Sheets | Se pierden solicitudes, estados y respuestas. |
| Especificación técnica | Se pierde la definición funcional del asistente. |
| Historial de evolución | Se pierde la trazabilidad de los cambios. |
| Registro de validación | Se pierde evidencia del funcionamiento. |
| Inventario técnico | Se dificulta reproducir el entorno. |

---

## Paso 2. Clasificar los respaldos

Utilice tres categorías.

### Respaldo de código

Incluye:

```text
puente_local.py

Code.gs

requirements.txt
```

---

### Respaldo de configuración

Incluye:

```text
system_prompt.txt

parámetros documentados

nombre del modelo

URL de Ollama

estructura de Google Sheets
```

No incluya contraseñas, credenciales u otra información sensible en respaldos no protegidos.

---

### Respaldo documental

Incluye:

- especificación técnica;
- arquitectura;
- inventario;
- registros de validación;
- bitácora de incidencias;
- historial de evoluciones;
- fichas de liberación.

---

## Paso 3. Organizar la carpeta de respaldos

Dentro de la carpeta principal utilice:

```text
Taller_IA_Local
│
└── 05_Respaldos
```

Cree una subcarpeta por fecha de respaldo.

Ejemplo:

```text
05_Respaldos
│
├── 2026-08-03
├── 2026-08-10
└── 2026-08-20
```

Evite almacenar todos los archivos sin orden dentro de una única carpeta.

---

## Paso 4. Aplicar una nomenclatura consistente

Utilice nombres que permitan identificar:

- componente;  
- fecha;  
- estado o propósito del respaldo.

Ejemplos:

```text
puente_local_2026-08-03.py

system_prompt_2026-08-03.txt

Code_2026-08-03.gs
```

No utilice nombres ambiguos como:

```text
final.py

final_final.py

ultima_version.gs
```

---

## Paso 5. Respaldar el código local

Copie a la carpeta de respaldo:

```text
puente_local.py

system_prompt.txt

requirements.txt
```

Verifique que los archivos puedan abrirse correctamente.

No basta con confirmar que fueron copiados.

Revise su contenido.

---

## Paso 6. Respaldar Google Apps Script

Abra el proyecto de Google Apps Script.

Copie el contenido vigente del archivo:

```text
Code.gs
```

Guárdelo localmente como:

```text
google_apps_script.gs
```

Si el proyecto contiene varios archivos, respalde cada uno de ellos por separado.

Ejemplo:

```text
Code.gs

Configuracion.gs

Correo.gs
```

---

## Paso 7. Respaldar Google Sheets

Google Sheets conserva automáticamente historial de mejoras, pero también se recomienda mantener una copia controlada.

Puede realizar una copia de la hoja de cálculo y asignarle un nombre como:

```text
Respaldo_Servicio_Inteligente_28_06_2026
```

Verifique que incluya:

- estructura de columnas;
- estados;
- respuestas;
- fechas;
- registros necesarios para la trazabilidad.

No distribuya copias que contengan datos personales sin autorización.

---

## Paso 8. Respaldar Google Forms

Registre:

- nombre del formulario;
- campos utilizados;
- tipos de pregunta;
- obligatoriedad;
- vínculo con Google Sheets.

Si corresponde, cree una copia del formulario.

No es necesario duplicarlo después de cada operación, pero sí cuando se realicen cambios estructurales.

---

## Paso 9. Respaldar la documentación técnica

Copie a la carpeta de respaldo:

- arquitectura final;
- inventario técnico;
- procedimientos de inicio y cierre;
- registro operativo;
- historial de evolución;
- matriz de validación;
- bitácora de incidencias.

La documentación debe corresponder al mismo estado funcional que los scripts respaldados.

---

## Paso 10. Proteger la información sensible

Antes de copiar o compartir un respaldo, revise que no incluya:

- contraseñas;
- credenciales;
- tokens;
- información de autenticación;

Si un archivo contiene valores sensibles, reemplácelos por marcadores.

---

## Paso 11. Definir la frecuencia de respaldo

Establezca una periodicidad.

| Situación                             | Respaldo recomendado      |
| ------------------------------------- | ------------------------- |
| Antes de modificar código             | Obligatorio               |
| Después de alcanzar un estado estable | Obligatorio               |
| Después de cambiar el System Prompt   | Recomendado               |
| Antes de una demostración             | Recomendado               |
| Después de una incidencia importante  | Obligatorio               |
| Durante operación regular             | Según frecuencia definida |

Para un proyecto de laboratorio puede bastar con respaldar después de cada cambio importante.

---

## Paso 12. Definir una ubicación secundaria

No mantenga todos los respaldos en el mismo computador.

Considere una segunda ubicación autorizada, por ejemplo:

- almacenamiento institucional;
- unidad externa;
- Google Drive;
- repositorio privado.

La ubicación secundaria debe respetar las políticas de seguridad y protección de datos aplicables.

---

## Paso 13. Elaborar una ficha de respaldo

Complete:

| Elemento               | Información |
| ---------------------- | ----------- |
| Fecha                  |             |
| Estado respaldado      |             |
| Responsable            |             |
| Componentes incluidos  |             |
| Ubicación principal    |             |
| Ubicación secundaria   |             |
| Verificación realizada | Sí / No     |
| Observaciones          |             |

---

# Procedimiento de recuperación

## Paso 14. Identificar el tipo de fallo

Antes de restaurar, determine qué componente falló.

| Tipo de fallo | Acción inicial |
|---|---|
| Script local modificado | Restaurar `puente_local.py` |
| System Prompt incorrecto | Restaurar versión estable |
| Apps Script con errores | Restaurar código publicado |
| Hoja modificada | Recuperar estructura o versión |
| Dependencias perdidas | Reinstalar desde `requirements.txt` |
| Equipo nuevo | Reconstruir el entorno completo |

Evite restaurar todos los componentes si solo uno está afectado.

---

## Paso 15. Detener el servicio

Antes de recuperar una versión:

1. suspenda la recepción de solicitudes;
2. detenga el puente local;
3. registre solicitudes pendientes;
4. documente el motivo de la recuperación.

No restaure archivos mientras el proceso continúe ejecutándose.

---

## Paso 16. Seleccionar el respaldo correcto

Revise:

- fecha;
- versión;
- estado;
- observaciones.

Seleccione la última versión estable anterior al fallo.

No utilice automáticamente el archivo más reciente si no fue validado.

---

## Paso 17. Restaurar los archivos locales

Copie desde el respaldo:

```text
puente_local.py

system_prompt.txt

requirements.txt
```

Reemplace únicamente los componentes afectados.

Luego reinstale dependencias cuando sea necesario:

```powershell
python -m pip install -r requirements.txt
```

---

## Paso 18. Restaurar Google Apps Script

Abra el editor.

Reemplace el código afectado por la versión respaldada.

Guarde los cambios.

Después:

```text
Implementar

↓

Administrar implementaciones

↓

Publicar nueva versión
```

Verifique que la URL utilizada por el puente continúe vigente.

---

## Paso 19. Restaurar la estructura de Google Sheets

Si la hoja fue modificada:

- recupere una versión anterior;
- restablezca encabezados;
- confirme el orden de las columnas;
- revise estados;
- verifique que no se pierdan solicitudes.

La estructura esperada continúa siendo:

| Posición | Columna |
|---:|---|
| 1 | Marca temporal |
| 2 | Nombre |
| 3 | Tipo de consulta |
| 4 | Consulta |
| 5 | Correo electrónico |
| 6 | Estado |
| 7 | Respuesta IA |
| 8 | Fecha de procesamiento |

---

## Paso 20. Ejecutar una prueba de recuperación

Después de restaurar:

1. verifique Python;
2. verifique Ollama;
3. confirme el modelo;
4. inicie el puente;
5. envíe una solicitud de prueba;
6. confirme el correo;
7. revise el estado final.

El resultado esperado es:

```text
ENVIADA
```

No reabra el servicio a usuarios reales antes de completar esta prueba.

---

## Paso 21. Registrar la recuperación

Complete:

| Elemento | Información |
|---|---|
| Fecha | |
| Componente restaurado | |
| Versión recuperada | |
| Motivo | |
| Responsable | |
| Resultado de la prueba | |
| Observaciones | |

Este registro formará parte de la trazabilidad operativa.

---

## Flujo resumido de recuperación

```text
Detectar fallo

↓

Detener servicio

↓

Identificar componente

↓

Seleccionar respaldo estable

↓

Restaurar

↓

Verificar configuración

↓

Ejecutar prueba controlada

↓

Reabrir servicio

↓

Registrar recuperación
```

---

💡 **Nota técnica 9.6**

Un respaldo solo es útil si puede restaurarse.

Por este motivo, no basta con copiar archivos: es necesario comprobar periódicamente que los respaldos se encuentran completos, legibles y asociados a un estado conocido y documentado del servicio.

---

### Verificación

Complete la siguiente tabla:

| Verificación | Estado |
|---|:---:|
| Identifiqué los componentes críticos | ☐ |
| Organicé la carpeta de respaldos | ☐ |
| Apliqué una nomenclatura consistente | ☐ |
| Respaldé scripts y configuraciones | ☐ |
| Respaldé Apps Script | ☐ |
| Respaldé la documentación | ☐ |
| Definí una frecuencia | ☐ |
| Establecí una ubicación secundaria | ☐ |
| Documenté el procedimiento de recuperación | ☐ |
| Ejecuté una prueba de restauración | ☐ |

---

### Problemas frecuentes

#### El respaldo contiene claves o credenciales

Elimine esos valores antes de copiar o compartir el archivo.

Mantenga las credenciales en mecanismos protegidos.

---

#### No sé cuál versión restaurar

Seleccione la última versión estable y validada.

Revise el historial de evolución y la ficha de liberación.

---

#### El código fue restaurado, pero la aplicación web sigue usando una versión anterior

Actualice la implementación de Google Apps Script.

Guardar el código no siempre modifica la versión publicada.

---

#### El puente no funciona después de restaurarlo

Verifique:

- dependencias;
- URL de Apps Script;
- modelo configurado;
- disponibilidad de Ollama;
- ubicación de `system_prompt.txt`.

---

#### La hoja fue restaurada, pero los datos están desplazados

Revise el orden de las columnas y ajuste la estructura antes de reiniciar el servicio.

---

### Buenas prácticas

- Respalde antes de modificar.
- Mantenga copias en más de una ubicación.
- Utilice nombres claros.
- Proteja los datos personales.
- Separe versiones estables y versiones en desarrollo.
- Pruebe periódicamente la recuperación.
- Documente cada restauración.
- No sobrescriba respaldos antiguos sin necesidad.

---

### Checklist

Antes de continuar confirme que:

☐ Existe un respaldo completo de la versión vigente.

☐ Los archivos pueden recuperarse.

☐ La documentación y el código corresponden a la misma versión.

☐ No se almacenaron credenciales en ubicaciones inseguras.

☐ El procedimiento de recuperación fue probado.

☐ El servicio puede restablecerse después de un fallo.

---

## 9.7 Seguridad y protección de la configuración

### Objetivo

Identificar y aplicar medidas básicas de seguridad para proteger las claves, permisos, archivos, servicios locales y datos utilizados por el servicio inteligente, reduciendo el riesgo de accesos no autorizados, modificaciones accidentales o exposición de información.

---

### Tiempo estimado

**30 minutos**

---

### Requisitos previos

Antes de comenzar esta sección deberá haber completado:

- Sección 9.6 – Respaldo y recuperación del servicio.

Además, deberá disponer de acceso a:

- archivos locales del proyecto;
- configuración de Google Apps Script;
- cuenta responsable de Google Workspace;
- puente local en Python;
- documentación técnica vigente.

---

### Procedimiento

El servicio inteligente combina componentes locales y servicios en la nube.

Esta arquitectura requiere proteger distintos elementos:

- cuentas de acceso;
- archivos de configuración;
- scripts;
- datos almacenados;
- servicios locales;
- permisos de Google Workspace;
- información personal recopilada durante la operación.

El propósito de esta sección no es implementar una infraestructura avanzada de ciberseguridad.

El objetivo consiste en establecer controles básicos que reduzcan los riesgos más frecuentes durante la operación del servicio.

---

## Paso 1. Identificar los elementos sensibles

Revise la solución e identifique aquellos componentes que no deben compartirse públicamente.

| Elemento                    | Motivo de protección                                                   |
| --------------------------- | ---------------------------------------------------------------------- |
| Archivo `system_prompt.txt` | Contiene la configuración del asistente.                               |
| Código de Apps Script       | Coordina el procesamiento y envío de respuestas.                       |
| Archivo `puente_local.py`   | Contiene parámetros técnicos del servicio.                             |
| Correos de usuarios         | Corresponden a datos personales.                                       |
| Respuestas registradas      | Pueden contener información privada o sensible.                        |
| URL de la aplicación web    | Forma parte de la configuración técnica utilizada por el puente local. |
| Cuenta de Google            | Administra Forms, Sheets, Apps Script y Gmail.                         |

---

## Paso 2. Revisar la configuración del puente local

Abra `puente_local.py` y revise los parámetros utilizados para conectar los distintos componentes del servicio.

La configuración principal incluye:

```
URL_APPS_SCRIPT = "URL_DE_LA_APLICACION_WEB"
URL_OLLAMA = "http://localhost:11434/api/chat"
MODELO_OLLAMA = "nombre-del-modelo"
```

Verifique que:

- la URL de Apps Script corresponda a la implementación vigente;
- Ollama utilice la dirección y el puerto configurados;
- el modelo indicado se encuentre instalado;
- no existan contraseñas, credenciales o tokens incorporados innecesariamente dentro del código.

La configuración técnica debe mantenerse protegida y solo debe ser modificada por personas autorizadas.

---

## Paso 3. Proteger la cuenta de Google

La cuenta propietaria de los servicios debe utilizar:

- contraseña segura;
- verificación en dos pasos;
- mecanismos de recuperación actualizados;
- acceso restringido.

No comparta una cuenta personal entre múltiples responsables.

Cuando sea posible, utilice una cuenta institucional destinada al proyecto.

---

## Paso 4. Revisar los permisos de Google Workspace

Compruebe quién posee acceso a:

- Google Forms;
- Google Sheets;
- Google Apps Script;
- copias de respaldo;
- Gmail utilizado para los envíos.

Elimine accesos que ya no sean necesarios.

Aplique el principio de mínimo privilegio:

> Cada persona debe disponer únicamente de los permisos necesarios para cumplir su función.

---

## Paso 5. Revisar la implementación de Apps Script

Verifique la configuración de la aplicación web.

Documente:

| Elemento | Configuración actual |
|---|---|
| Ejecutar como | |
| Usuarios con acceso | |
| Fecha de publicación | |
| Responsable | |
| Versión | |

Evite utilizar niveles de acceso más amplios de lo necesario.

Revise periódicamente la configuración de acceso de la aplicación web y asegúrese de que corresponda a las necesidades reales del servicio.

---

## Paso 6. Proteger Google Sheets

Limite el acceso a la hoja de respuestas.

Los usuarios del formulario no necesitan acceder directamente a Google Sheets.

Revise especialmente quién puede:

- visualizar respuestas;
- modificar estados;
- editar columnas;
- eliminar registros;
- compartir la hoja.

La modificación accidental de la estructura puede interrumpir el servicio.

---

## Paso 7. Proteger el formulario

Revise la configuración del formulario.

Confirme:

- quién puede responder;
- si se recopilan correos automáticamente;
- si una persona puede enviar múltiples respuestas;
- si se permite editar respuestas;
- si el formulario permanece abierto permanentemente.

Utilice únicamente las opciones necesarias para el caso de uso.

---

## Paso 8. Proteger los archivos locales

Los archivos del proyecto deben almacenarse en una cuenta de usuario protegida.

Revise especialmente:

```text
puente_local.py

system_prompt.txt

requirements.txt

google_apps_script.gs
```

Evite almacenarlos en:

- carpetas públicas;
- computadores compartidos sin control;
- servicios de intercambio abiertos;
- repositorios públicos.

---

## Paso 9. Revisar la exposición de servicios locales

Ollama y Open WebUI se utilizan dentro del computador local.

No configure el router ni el firewall para exponer públicamente:

```text
localhost:11434

localhost:8080
```

El puente local consulta Ollama desde el mismo equipo.

No es necesario abrir esos puertos hacia Internet.

---

## Paso 10. Revisar el firewall

Compruebe que las reglas del firewall no exponen innecesariamente los servicios locales.

El objetivo es permitir el funcionamiento interno del equipo sin habilitar acceso remoto no autorizado.

No desactive completamente el firewall para solucionar problemas de conectividad.

---

## Paso 11. Minimizar los datos recopilados

El formulario utiliza únicamente:

- nombre;
- tipo de consulta;
- consulta;
- correo electrónico.

No agregue datos adicionales sin una justificación clara.

Evite solicitar:

- contraseñas;
- identificadores financieros;
- información médica;
- documentos personales;
- antecedentes confidenciales;
- datos sensibles que no sean necesarios.

---

## Paso 12. Revisar el contenido de las consultas

Informe a los usuarios que no deben ingresar información sensible o confidencial.

Aunque el modelo se ejecute localmente, los datos también se almacenan en servicios de Google.

La privacidad debe analizarse considerando todo el recorrido de la información, no únicamente el procesamiento del modelo.

---

## Paso 13. Definir un período de conservación

Determine cuánto tiempo se mantendrán:

- solicitudes;
- correos;
- respuestas;
- registros de error;
- respaldos.

Ejemplo:

| Información | Período definido |
|---|---|
| Solicitudes | |
| Respuestas generadas | |
| Correos enviados | |
| Registros de error | |
| Respaldos | |

No conserve información indefinidamente sin necesidad.

---

## Paso 14. Definir un procedimiento de eliminación

Cuando termine el período establecido:

1. verifique que la información ya no sea necesaria;
2. confirme que no exista una obligación de conservación;
3. elimine los registros correspondientes;
4. revise las copias de respaldo;
5. documente la eliminación.

No elimine datos sin autorización cuando formen parte de un proceso institucional.

---

## Paso 15. Proteger los respaldos

Los respaldos deben recibir el mismo nivel de protección que los archivos originales.

Revise que:

- no contengan claves;
- no se compartan públicamente;
- tengan acceso restringido;
- permanezcan en ubicaciones autorizadas;
- puedan eliminarse cuando dejen de ser necesarios.

---

## Paso 16. Revisar las capturas y evidencias

Antes de utilizar imágenes en una presentación o portafolio, verifique que no muestren:

- claves;
- URL privadas;
- correos personales;
- nombres completos no autorizados;
- consultas confidenciales;
- respuestas sensibles;
- datos de cuentas.

Utilice datos ficticios o anonimizados durante las demostraciones.

---

## Paso 17. Elaborar la lista de controles de seguridad

Complete:

| Control                          | Implementado | Observaciones |
| -------------------------------- | :----------: | ------------- |
| Permisos revisados               |      ☐       |               |
| Hoja de cálculo restringida      |      ☐       |               |
| Servicios locales no expuestos   |      ☐       |               |
| Datos minimizados                |      ☐       |               |
| Período de conservación definido |      ☐       |               |
| Respaldos protegidos             |      ☐       |               |
| Evidencias anonimizadas          |      ☐       |               |
| Configuración técnica protegida  |      ☐       |               |
| Acceso a Apps Script revisado    |      ☐       |               |
| Archivos locales protegidos      |      ☐       |               |
| Cuenta de Google protegida       |      ☐       |               |

---

## Paso 18. Verificar el servicio después de los cambios

Después de modificar la configuración o los permisos:

1. inicie el puente;
2. envíe una solicitud de prueba;
3. confirme el procesamiento;
4. verifique el correo;
5. revise el estado final.

El resultado esperado será:

```text
ENVIADA
```

---

💡 **Nota técnica 9.7**

El procesamiento local mediante Ollama reduce la necesidad de enviar la consulta a un proveedor externo de modelos, pero no elimina todos los riesgos de privacidad.

Los datos continúan circulando por Google Forms, Google Sheets, Google Apps Script y Gmail. Por ello, la seguridad debe evaluarse considerando la arquitectura completa.

---

### Verificación

Complete la siguiente tabla:

| Verificación                                    | Estado |
| ----------------------------------------------- | :----: |
| Identifiqué los elementos sensibles             |   ☐    |
| El código no contiene credenciales innecesarias |   ☐    |
| El acceso a Apps Script fue revisado            |   ☐    |
| La configuración local está protegida           |   ☐    |
| La cuenta de Google está protegida              |   ☐    |
| Los permisos fueron revisados                   |   ☐    |
| Google Sheets posee acceso restringido          |   ☐    |
| Los servicios locales no están expuestos        |   ☐    |
| Se minimizan los datos capturados               |   ☐    |
| Existe un período de conservación               |   ☐    |
| Los respaldos están protegidos                  |   ☐    |
| Las evidencias no revelan información privada   |   ☐    |

---

### Problemas frecuentes

#### Muchas personas tienen acceso a Google Sheets

Revise los permisos y elimine accesos innecesarios.

Los usuarios del formulario no requieren acceso a la hoja de respuestas.

---

#### El sistema requiere datos adicionales

Justifique cada nuevo campo.

No incorpore información únicamente porque podría ser útil en el futuro.

---

#### Una captura contiene información personal

Reemplace la captura por una versión anonimizada antes de incorporarla al portafolio o a una presentación.

---

#### El firewall bloquea el servicio

No desactive toda la protección.

Identifique qué componente está afectado y revise únicamente la regla necesaria.

---

### Buenas prácticas

- Evite incorporar credenciales directamente en el código.
- Utilice verificación en dos pasos.
- Aplique mínimo privilegio.
- No exponga Ollama ni Open WebUI a Internet.
- Capture únicamente datos necesarios.
- Defina períodos de conservación.
- Proteja los respaldos.
- Utilice datos ficticios en demostraciones.
- Cambie inmediatamente cualquier credencial que haya sido expuesta.
- Revise periódicamente permisos y accesos.

---

### Checklist

Antes de continuar confirme que:

☐ Las credenciales y configuraciones sensibles están protegidas.

☐ Los permisos corresponden a las responsabilidades definidas.

☐ Los archivos locales poseen acceso restringido.

☐ Los servicios locales no están expuestos.

☐ Los datos personales se limitan a lo necesario.

☐ Existe un procedimiento de conservación y eliminación.

☐ Los respaldos y evidencias están protegidos.

☐ El servicio puede operar sin revelar configuraciones sensibles.

---

## 9.8 Roles y responsabilidades operativas

### Objetivo

Definir los roles y responsabilidades necesarios para iniciar, supervisar, mantener, modificar y recuperar el servicio inteligente, asegurando que cada actividad operativa tenga una persona responsable y un nivel de autorización claramente establecido.

---

### Tiempo estimado

**25 minutos**

---

### Requisitos previos

Antes de comenzar esta sección deberá haber completado:

- Sección 9.7 – Seguridad y protección de la configuración.

Además, deberá disponer de:

- arquitectura técnica actualizada;
- inventario de componentes;
- procedimientos de inicio y cierre;
- plan de respaldo y recuperación;
- controles de seguridad documentados.

---

### Procedimiento

Un servicio inteligente no debería depender exclusivamente del conocimiento informal de una sola persona.

Para operar de manera controlada es necesario definir:

- quién puede iniciar el servicio;
- quién supervisa las solicitudes;
- quién revisa errores;
- quién modifica el código;
- quién actualiza el modelo;
- quién autoriza cambios relevantes en el servicio
- quién responde ante incidentes.

Una misma persona puede asumir varios roles en un proyecto pequeño.

Sin embargo, las responsabilidades deben permanecer explícitamente documentadas.

---

## Paso 1. Identificar las actividades operativas

Revise las principales actividades necesarias para mantener el servicio.

| Actividad                    | Descripción                                                     |
| ---------------------------- | --------------------------------------------------------------- |
| Inicio del servicio          | Verificar componentes e iniciar el puente local.                |
| Cierre del servicio          | Detener el procesamiento y revisar estados.                     |
| Monitoreo                    | Supervisar solicitudes, errores y tiempos.                      |
| Mantenimiento técnico        | Corregir scripts y configuraciones.                             |
| Administración del asistente | Actualizar instrucciones permanentes.                           |
| Gestión de modelos           | Instalar, probar o reemplazar modelos.                          |
| Seguridad                    | Administrar permisos, accesos y protección de la configuración. |
| Respaldo                     | Proteger archivos y documentación.                              |
| Recuperación                 | Restaurar componentes ante fallos.                              |
| Validación                   | Comprobar que los cambios funcionan.                            |
| Atención de incidentes       | Coordinar la respuesta frente a problemas.                      |
| Aprobación de cambios        | Autorizar la incorporación de cambios relevantes.               |

---

## Paso 2. Definir el responsable operativo

El responsable operativo administra el funcionamiento cotidiano del servicio.

Sus tareas principales son:

- ejecutar el procedimiento de inicio;
- mantener el puente local en funcionamiento;
- revisar solicitudes pendientes;
- supervisar la consola;
- ejecutar el procedimiento de cierre;
- registrar incidencias;
- informar problemas al responsable técnico.

No debería modificar código o configuraciones críticas sin autorización.

---

## Paso 3. Definir el responsable técnico

El responsable técnico administra los componentes tecnológicos.

Sus responsabilidades incluyen:

- mantener `puente_local.py`;
- revisar Google Apps Script;
- controlar dependencias;
- actualizar Ollama;
- verificar compatibilidad;
- corregir errores técnicos;
- realizar pruebas después de cambios;
- mantener el inventario actualizado.

Este rol debe poseer conocimientos suficientes sobre la arquitectura del servicio.

---

## Paso 4. Definir el responsable del asistente

Este rol administra el comportamiento funcional del asistente.

Sus responsabilidades son:

- revisar la especificación técnica;
- mantener `system_prompt.txt`;
- analizar respuestas problemáticas;
- proponer mejoras;
- actualizar restricciones;
- verificar la identidad y el tono;
- coordinar la validación del comportamiento.

No debe modificar las instrucciones permanentes sin documentar el cambio.

---

## Paso 5. Definir el responsable de seguridad y datos

Este rol supervisa:

- permisos;
- accesos;
- configuraciones sensibles;
- datos personales;

En proyectos pequeños, esta responsabilidad puede ser asumida por el responsable técnico, pero debe quedar expresamente registrada.

---

## Paso 6. Definir el responsable de aprobación

Antes de incorporar cambios relevantes al servicio, una persona autorizada deberá revisar:

- resultados de validación;
- cambios técnicos;
- impacto funcional;
- riesgos;
- documentación;
- condiciones de operación.

---

## Paso 7. Definir el responsable de atención a usuarios

El servicio debe disponer de un canal de revisión humana.

Este rol deberá:

- recibir solicitudes no resueltas;
- revisar respuestas cuestionadas;
- intervenir en casos complejos;
- corregir información;
- responder ante reclamos;
- escalar problemas técnicos o funcionales.

El asistente no debe convertirse en el único punto de contacto disponible.

---

## Paso 8. Construir la matriz de responsabilidades

Complete una matriz similar a la siguiente.

| Actividad                                     | Operativo | Técnico | Asistente | Seguridad | Aprobación |
| --------------------------------------------- | :-------: | :-----: | :-------: | :-------: | :--------: |
| Iniciar servicio                              |     R     |    A    |           |           |            |
| Cerrar servicio                               |     R     |    A    |           |           |            |
| Monitorear solicitudes                        |     R     |    A    |           |           |            |
| Corregir código                               |           |    R    |           |           |     A      |
| Modificar System Prompt                       |           |         |     R     |           |     A      |
| Cambiar modelo                                |           |    R    |     A     |           |     A      |
| Gestionar accesos y configuraciones sensibles |           |    A    |           |     R     |            |
| Respaldar archivos                            |     R     |    A    |           |     A     |            |
| Recuperar el servicio                         |           |    R    |           |     A     |            |
| Validar cambios realizados                    |     A     |    A    |     R     |     A     |            |
| Autorizar liberación                          |           |         |           |           |     R      |

Utilice la siguiente referencia:

| Código | Significado |
|---|---|
| `R` | Responsable de ejecutar la actividad. |
| `A` | Participa o apoya la actividad. |

En proyectos más avanzados podrá utilizarse una matriz RACI completa.

---

## Paso 9. Definir niveles de autorización

No todas las personas deberían poder modificar todos los componentes.

Establezca niveles básicos.

| Nivel          | Permisos                             |
| -------------- | ------------------------------------ |
| Operación      | Iniciar, detener y monitorear.       |
| Mantenimiento  | Modificar scripts y configuraciones. |
| Administración | Gestionar accesos y seguridad.       |
| Aprobación     | Autorizar  cambios mayores.          |

Evite entregar permisos de administración a personas que solo requieren supervisar solicitudes.

---

## Paso 10. Definir actividades que requieren aprobación

Las siguientes acciones deberían requerir autorización previa:

- cambiar el modelo de lenguaje;
- modificar el System Prompt;
- alterar la estructura de Google Sheets;
- modificar parámetros críticos de configuración;
- modificar permisos;
- publicar una nueva implementación;
- incorporar nuevos campos al formulario;
- cambiar el contenido de los correos;
- aprobar cambios relevantes para su operación

Documente quién aprueba cada tipo de cambio.

---

## Paso 11. Definir la sustitución de responsables

El servicio no debe depender de una única persona.

Para cada rol principal, identifique un reemplazo.

| Rol | Responsable titular | Reemplazo |
|---|---|---|
| Operativo | | |
| Técnico | | |
| Asistente | | |
| Seguridad | | |
| Aprobación | | |

El reemplazo debe conocer los procedimientos y disponer de acceso autorizado.

---

## Paso 12. Definir la transferencia de conocimiento

Cada responsable deberá disponer de la documentación necesaria.

Por ejemplo:

| Rol        | Documentación requerida                                             |
| ---------- | ------------------------------------------------------------------- |
| Operativo  | Inicio, cierre, monitoreo e incidencias.                            |
| Técnico    | Arquitectura, inventario, scripts y recuperación.                   |
| Asistente  | Especificación, System Prompt y validaciones.                       |
| Seguridad  | Permisos, respaldos, conservación y protección de la configuración. |
| Aprobación | Historial, resultados, riesgos y fichas de versión.                 |

La información no debe mantenerse únicamente en mensajes informales o memoria personal.

---

## Paso 13. Definir el tratamiento de incidentes

Cuando ocurra un incidente:

1. el responsable operativo detecta y registra;
2. el responsable técnico diagnostica;
3. el responsable de seguridad evalúa impacto;
4. el responsable del asistente revisa el comportamiento, si corresponde;
5. el responsable de aprobación decide la continuidad;
6. se documenta el resultado.

Este flujo evita respuestas improvisadas.

---

## Paso 14. Crear la ficha de responsables

Complete:

| Elemento | Información |
|---|---|
| Nombre del servicio | |
| Responsable operativo | |
| Responsable técnico | |
| Responsable del asistente | |
| Responsable de seguridad | |
| Responsable de aprobación | |
| Responsable de atención a usuarios | |
| Fecha de asignación | |
| Próxima revisión | |

Evite incorporar datos personales innecesarios en documentos públicos.

---

## Paso 15. Revisar los accesos asociados

Compruebe que los permisos reales coinciden con las responsabilidades.

Revise:

- Google Forms;
- Google Sheets;
- Apps Script;
- Gmail;
- respaldos;
- carpetas locales;
- cuentas institucionales.

Una persona no debería conservar acceso después de dejar de cumplir su rol.

---

## Paso 16. Validar la asignación de responsabilidades

Plantee un escenario de prueba.

Ejemplo:

```text
Una solicitud permanece en estado PROCESANDO
durante más de diez minutos.
```

Determine:

- quién detecta;
- quién diagnostica;
- quién autoriza el reprocesamiento;
- quién comunica al usuario;
- quién documenta.

Si no puede responder claramente, la matriz requiere ajustes.

---

💡 **Nota técnica 9.8**

Asignar responsabilidades no implica necesariamente crear nuevos cargos.

En un proyecto pequeño, una misma persona puede asumir distintos roles. Lo importante es que cada función operativa esté explícitamente asignada, documentada y respaldada por procedimientos.

---

### Verificación

Complete la siguiente tabla:

| Verificación | Estado |
|---|:---:|
| Identifiqué las actividades operativas | ☐ |
| Definí el responsable operativo | ☐ |
| Definí el responsable técnico | ☐ |
| Definí quién administra el asistente | ☐ |
| Definí responsabilidades de seguridad | ☐ |
| Definí quién aprueba nuevas versiones | ☐ |
| Existe un canal de revisión humana | ☐ |
| Construí la matriz de responsabilidades | ☐ |
| Definí reemplazos | ☐ |
| Revisé los accesos | ☐ |

---

### Problemas frecuentes

#### Una sola persona controla todo el servicio

Puede ser aceptable durante un laboratorio.

Sin embargo, documente igualmente cada rol para facilitar futuras transferencias y reducir dependencia.

---

#### Nadie está autorizado para modificar el System Prompt

Asigne formalmente un responsable funcional y un mecanismo de aprobación.

---

#### Existen personas con permisos innecesarios

Revise los accesos y aplique el principio de mínimo privilegio.

---

#### No existe reemplazo para el responsable técnico

Documente el entorno y prepare una persona de respaldo antes de utilizar el servicio en un contexto real.

---

#### Los usuarios no saben a quién acudir

Defina un canal de revisión humana y comuníquelo claramente.

---

### Buenas prácticas

- Asigne todas las actividades críticas.
- Separe operación, modificación y aprobación cuando sea posible.
- Mantenga reemplazos autorizados.
- Revise periódicamente los accesos.
- Documente el conocimiento técnico.
- Evite depender de una única persona.
- Mantenga un canal de atención humana.
- Actualice la matriz cuando cambien los responsables.

---

### Checklist

Antes de continuar confirme que:

☐ Cada actividad posee un responsable.

☐ Los permisos coinciden con las funciones asignadas.

☐ Existen responsables de reemplazo.

☐ Las modificaciones importantes requieren aprobación.

☐ Los incidentes poseen un flujo de atención.

☐ Los usuarios disponen de revisión humana.

☐ La ficha de responsables está actualizada.

☐ El servicio puede operar con responsabilidades claras.

---

## 9.9 Prueba operativa del servicio

### Objetivo

Realizar una prueba operativa integral que permita verificar el funcionamiento del servicio inteligente utilizando los procedimientos, controles y responsabilidades definidos durante este capítulo, comprobando que la solución puede operar de manera estable bajo condiciones normales.

---

### Tiempo estimado

**40 minutos**

---

### Requisitos previos

Antes de comenzar esta sección deberá haber completado:

- Sección 9.1 – Revisión de la arquitectura final.
- Sección 9.2 – Inventario de componentes.
- Sección 9.3 – Procedimiento de inicio.
- Sección 9.4 – Procedimiento de cierre.
- Sección 9.5 – Monitoreo y control.
- Sección 9.6 – Respaldo y recuperación.
- Sección 9.7 – Seguridad y protección.
- Sección 9.8 – Roles y responsabilidades.

El servicio deberá encontrarse completamente operativo.

---

### Procedimiento

Hasta este momento se han definido todos los procedimientos necesarios para operar el servicio.

Sin embargo, disponer de documentación no garantiza que el sistema funcione correctamente.

Antes de considerar la solución lista para su utilización, es necesario ejecutar una prueba integral que valide:

- la arquitectura;
- el procedimiento de inicio;
- el procesamiento;
- el monitoreo;
- la recuperación frente a errores sencillos;
- el procedimiento de cierre.

Esta prueba simulará una jornada normal de operación.

---

## Paso 1. Preparar el entorno

Ejecute el procedimiento de inicio definido en la Sección 9.3.

Confirme que:

- existe conexión a Internet;
- Python funciona correctamente;
- Ollama está operativo;
- el modelo está disponible;
- Google Apps Script responde;
- el puente local fue iniciado.

No continúe si alguno de estos elementos presenta problemas.

---

## Paso 2. Verificar el estado inicial

Abra Google Sheets.

Confirme que no existen solicitudes pendientes provenientes de pruebas anteriores.

Revise especialmente los estados:

```text
PENDIENTE

PROCESANDO

ERROR
```

Si corresponde, documente la situación antes de iniciar la prueba.

---

## Paso 3. Ejecutar el Caso de Prueba 1

Ingrese una consulta sencilla desde Google Forms.

Ejemplo:

| Campo | Valor |
|---|---|
| Nombre | Usuario de prueba |
| Tipo de consulta | Contenidos |
| Consulta | ¿Qué es un modelo de lenguaje? |
| Correo | Dirección de prueba |

---

## Paso 4. Supervisar el procesamiento

Observe simultáneamente:

- PowerShell;
- Google Sheets.

Compruebe que la solicitud sigue la secuencia:

```text
PENDIENTE

↓

PROCESANDO

↓

ENVIADA
```

---

## Paso 5. Validar el resultado

Revise:

- respuesta generada;
- fecha de procesamiento;
- correo recibido.

Complete la siguiente tabla.

| Verificación | Resultado |
|---|:---:|
| Respuesta generada | ☐ |
| Estado ENVIADA | ☐ |
| Correo recibido | ☐ |
| Sin errores en consola | ☐ |

---

## Paso 6. Ejecutar el Caso de Prueba 2

Envíe una consulta más extensa.

Ejemplo:

```text
Necesito saber cuáles son los principales contenidos
de la unidad actual y qué temas debería revisar antes
de la próxima evaluación.
```

Evalúe:

- coherencia;
- organización;
- claridad.

---

## Paso 7. Ejecutar el Caso de Prueba 3

Ingrese una consulta fuera del alcance definido.

Ejemplo:

```text
Modifica mis calificaciones finales.
```

Verifique que el asistente:

- rechaza la solicitud;
- explica sus limitaciones;
- mantiene un comportamiento adecuado.

---

## Paso 8. Ejecutar un error controlado

Para verificar el procedimiento de recuperación, provoque un error sencillo.

Por ejemplo:

detenga temporalmente el puente local.

Envíe una nueva consulta.

Observe que la solicitud permanece en:

```text
PENDIENTE
```

Inicie nuevamente el puente.

Compruebe que el procesamiento continúa normalmente.

No modifique componentes críticos ni elimine archivos durante esta prueba.

---

## Paso 9. Verificar el monitoreo

Revise:

- Google Sheets;
- consola del puente;
- Apps Script.

Confirme que todos los eventos relevantes pueden identificarse fácilmente.

---

## Paso 10. Revisar los registros

Complete una bitácora de la prueba.

| Hora | Evento | Resultado |
|---|---|---|
| | Inicio del servicio | |
| | Caso 1 | |
| | Caso 2 | |
| | Caso 3 | |
| | Error controlado | |
| | Recuperación | |
| | Cierre | |

---

## Paso 11. Evaluar el comportamiento del asistente

Seleccione las respuestas obtenidas durante la prueba.

Evalúe:

| Criterio | Cumple |
|---|:---:|
| Responde correctamente | ☐ |
| Mantiene el contexto | ☐ |
| Respeta restricciones | ☐ |
| Utiliza lenguaje claro | ☐ |
| No inventa información | ☐ |

Esta evaluación será utilizada posteriormente durante el análisis del servicio.

---

## Paso 12. Revisar la estabilidad

Determine si durante toda la prueba se observaron:

- interrupciones;
- reinicios;
- errores repetitivos;
- tiempos excesivos;
- pérdidas de información.

Registre cualquier observación.

---

## Paso 13. Ejecutar el procedimiento de cierre

Una vez terminadas las pruebas:

- revise solicitudes pendientes;
- registre incidencias;
- respalde cambios, si corresponde;
- detenga el puente;
- complete el registro operativo.

Utilice el procedimiento definido en la Sección 9.4.

---

## Paso 14. Elaborar el informe de la prueba

Complete la siguiente ficha.

| Elemento | Resultado |
|---|---|
| Fecha | |
| Responsable | |
| Casos ejecutados | |
| Casos exitosos | |
| Errores detectados | |
| Tiempo aproximado de ejecución | |
| Observaciones | |

---

## Paso 15. Registrar la conclusión

Clasifique el resultado de la prueba.

Seleccione una opción.

| Estado | Significado |
|---|---|
| Operativo | El servicio funciona correctamente. |
| Operativo con observaciones | Existen mejoras menores pendientes. |
| Requiere correcciones | Deben resolverse problemas antes de utilizarlo. |

Documente brevemente la decisión adoptada.

---

## Resumen de la prueba operativa

```text
Inicio

↓

Caso 1

↓

Caso 2

↓

Caso 3

↓

Error controlado

↓

Recuperación

↓

Monitoreo

↓

Cierre

↓

Informe
```

---

💡 **Nota técnica 9.9**

Toda modificación importante del servicio debería ir acompañada de una nueva prueba operativa.

No es recomendable incorporar cambios directamente en el servicio utilizado por usuarios sin validar previamente su funcionamiento.

---

### Verificación

Complete la siguiente tabla.

| Verificación | Estado |
|---|:---:|
| El servicio inició correctamente | ☐ |
| Se ejecutó el Caso 1 | ☐ |
| Se ejecutó el Caso 2 | ☐ |
| Se ejecutó el Caso 3 | ☐ |
| Se realizó un error controlado | ☐ |
| El servicio se recuperó correctamente | ☐ |
| El monitoreo fue satisfactorio | ☐ |
| El procedimiento de cierre fue ejecutado | ☐ |
| Se elaboró el informe final | ☐ |

---

### Problemas frecuentes

#### Todas las pruebas funcionan excepto el envío de correos

Revise la autorización de Gmail y confirme que no se alcanzó la cuota diaria de envío.

---

#### El error controlado deja solicitudes sin procesar

Revise el procedimiento de recuperación antes de continuar.

No elimine registros sin documentar la situación.

---

#### Algunas respuestas presentan menor calidad

Revise el contenido de `system_prompt.txt` y determine si requiere ajustes antes de modificar el modelo.

---

#### El servicio funciona correctamente, pero la documentación no coincide

Actualice primero la documentación.

El estado operativo del servicio y la documentación deben mantenerse sincronizados.

---

### Buenas prácticas

- Ejecute pruebas después de cada cambio importante.
- Documente todos los resultados.
- Realice pruebas utilizando consultas variadas.
- Mantenga evidencia de los errores detectados.
- Corrija un problema por vez.
- No incorpore cambios al servicio sin validación previa.
- Conserve los informes de prueba junto con la documentación del proyecto.

---

### Checklist

Antes de continuar confirme que:

☐ El servicio fue probado de extremo a extremo.

☐ Se validó el procedimiento de recuperación.

☐ Los resultados quedaron documentados.

☐ Se identificaron oportunidades de mejora.

☐ El procedimiento de operación fue validado.

☐ El servicio está preparado para consolidar su estado operativo.

---

## 9.10 Consolidación del estado operativo

### Objetivo

Consolidar el estado operativo del servicio inteligente, reunir la documentación técnica y funcional del proyecto, registrar formalmente su condición de operación y dejar preparada la solución para la evaluación integral y la presentación final.

---

### Tiempo estimado

**30 minutos**

---

### Requisitos previos

Antes de comenzar esta sección deberá haber completado:

- Sección 9.1 – Revisión de la arquitectura final.
- Sección 9.2 – Inventario de componentes.
- Sección 9.3 – Procedimiento de inicio.
- Sección 9.4 – Procedimiento de cierre.
- Sección 9.5 – Monitoreo y control.
- Sección 9.6 – Respaldo y recuperación.
- Sección 9.7 – Seguridad y protección.
- Sección 9.8 – Roles y responsabilidades.
- Sección 9.9 – Prueba operativa.

Además, deberá disponer de:

- documentación actualizada;
- resultados de la prueba operativa;
- inventario técnico vigente;
- respaldo de los componentes críticos;
- registro de incidencias;
- historial de evolución del proyecto.

---

### Procedimiento

Durante este capítulo el servicio fue revisado desde una perspectiva operativa.

Se documentaron:

- arquitectura;
- componentes;
- procedimientos;
- respaldos;
- controles de seguridad;
- responsabilidades;
- pruebas de funcionamiento.

El siguiente paso consiste en reunir toda esta información y registrar un estado operativo consolidado.

Esta versión representará el estado oficial del servicio antes de comenzar la evaluación final del proyecto.

---

## Paso 1. Revisar el resultado de la prueba operativa

Recupere el informe elaborado en la sección anterior.

Compruebe la clasificación obtenida:

```text
Operativo

Operativo con observaciones

Requiere correcciones
```

Únicamente podrá consolidarse un estado operativo cuando el servicio se encuentre:

```text
Operativo
```

o:

```text
Operativo con observaciones
```

Las observaciones pendientes deberán quedar claramente documentadas.

---

## Paso 2. Confirmar la arquitectura vigente

Revise que la documentación represente correctamente la arquitectura actual:

```text
                    Usuario
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
            Puente local en Python
                        │
                        ▼
                     Ollama
                        │
                        ▼
             Modelo de lenguaje
                        │
                        ▼
          Respuesta del asistente
                        │
                        ▼
             Google Apps Script
                  │             │
                  ▼             ▼
           Google Sheets      Gmail
                                  │
                                  ▼
                               Usuario
```

Elimine diagramas antiguos que puedan generar confusión o trasládelos a la carpeta de respaldos.

---

## Paso 3. Revisar el inventario técnico

Confirme que el inventario incluye:

- sistema operativo;
- versión de Ollama;
- modelo principal;
- versión de Python;
- dependencias;
- versión de Open WebUI;
- scripts;
- archivos de configuración;
- servicios de Google Workspace;
- responsables;
- fechas de revisión.

No deje campos críticos sin completar.

---

## Paso 4. Revisar los archivos técnicos

Compruebe que la carpeta del proyecto contiene:

```text
Taller_IA_Local
│
├── 01_Documentacion
│
├── 02_Modelos
│
├── 03_Scripts
│   ├── puente_local.py
│   ├── system_prompt.txt
│   ├── requirements.txt
│   └── google_apps_script.gs
│
├── 04_Proyecto_Integrador
│
├── 05_Respaldos
│
└── 06_Recursos
```

Verifique que cada archivo corresponde a la versión vigente.

---

## Paso 5. Revisar la documentación funcional

Compruebe que se encuentran disponibles:

- definición del problema;
- ficha de identidad;
- capacidades;
- restricciones;
- criterios de éxito;
- especificación técnica;
- instrucciones permanentes;
- historial de evolución;  
- registros de validación y estado operativo.

Estos documentos representan el diseño funcional del asistente.

---

## Paso 6. Revisar la documentación operativa

Compruebe que se encuentran disponibles:

- procedimiento de inicio;
- procedimiento de cierre;
- procedimiento de monitoreo;
- plan de respaldo;
- procedimiento de recuperación;
- controles de seguridad;
- matriz de responsabilidades;
- informe de prueba operativa;
- bitácora de incidencias.

Estos documentos representan las condiciones de operación del servicio.

---

## Paso 7. Verificar la sincronización de los componentes

Revise que los siguientes componentes correspondan a la misma versión:

| Componente                | Estado / identificación |
| ------------------------- | ----------------------- |
| `puente_local.py`         |                         |
| `system_prompt.txt`       |                         |
| `google_apps_script.gs`   |                         |
| Arquitectura              |                         |
| Inventario técnico        |                         |
| Registro de validación    |                         |
| Procedimientos operativos |                         |

No consolide una versión si existen componentes con numeraciones incompatibles o documentación desactualizada.

---

## Paso 8. Definir el estado operativo

A partir de los resultados obtenidos durante la prueba operativa, registre la condición actual del servicio.

Utilice una de las siguientes categorías:

`Operativo`

`Operativo con observaciones`

`Requiere correcciones`

---

## Paso 9. Completar la ficha de estado operativo

Complete:

| Elemento | Información |
|---|---|
| Nombre del servicio | |
| Versión operativa | |
| Fecha | |
| Responsable técnico | |
| Responsable operativo | |
| Responsable funcional | |
| Modelo utilizado | |
| Estado | Operativa |
| Resultado de prueba | |
| Observaciones pendientes | |

---

## Paso 10. Registrar las capacidades vigentes

Complete:

| Capacidad                                                     | Estado |
| ------------------------------------------------------------- | :----: |
| Captura mediante Google Forms                                 |   ✔    |
| Almacenamiento en Google Sheets                               |   ✔    |
| Procesamiento local con Ollama                                |   ✔    |
| Uso de instrucciones permanentes mediante `system_prompt.txt` |   ✔    |
| Integración mediante Apps Script                              |   ✔    |
| Puente local en Python                                        |   ✔    |
| Envío mediante Gmail                                          |   ✔    |
| Control de estados                                            |   ✔    |
| Monitoreo                                                     |   ✔    |
| Respaldo y recuperación                                       |   ✔    |
| Procedimientos operativos                                     |   ✔    |
| Responsabilidades definidas                                   |   ✔    |

---

## Paso 11. Registrar las limitaciones operativas

Documente claramente las condiciones que afectan la disponibilidad del servicio.

Por ejemplo:

| Limitación | Impacto |
|---|---|
| El computador debe permanecer encendido | Sin equipo local no existe procesamiento. |
| El puente debe ejecutarse | Las solicitudes quedan pendientes si se detiene. |
| Ollama debe estar disponible | No se generan respuestas sin el modelo. |
| Existe dependencia de Internet | Los servicios de Google requieren conectividad. |
| Gmail posee cuotas | Puede limitarse el envío de respuestas. |
| El modelo puede generar errores | Se requiere revisión y supervisión humana. |

Estas limitaciones serán analizadas con mayor profundidad en el Capítulo 10.

---

## Paso 12. Registrar observaciones pendientes

Complete:

| Prioridad | Observación | Acción futura |
|---|---|---|
| Alta | | |
| Media | | |
| Baja | | |

Una versión puede considerarse operativa con mejoras menores pendientes, siempre que no comprometan su funcionamiento principal o seguridad.

---

## Paso 13. Actualizar el historial de evolución

Agregue la nueva versión.

| Etapa          | Cambio principal                      | Estado     |
| -------------- | ------------------------------------- | ---------- |
| Construcción   | Asistente inicial                     | Completada |
| Optimización   | Ajuste y validación                   | Completada |
| Integración    | Incorporación de Google Workspace     | Completada |
| Automatización | Procesamiento automatizado            | Completada |
| Consolidación  | Procedimientos y controles operativos | Completada |


---

## Paso 14. Crear un respaldo de la versión operativa

Cree una carpeta específica:

```text
05_Respaldos
│
└── RESPALDO_OPERATIVO_AAAA-MM-DD
```

Incluya:

- scripts;
- instrucciones permanentes;
- dependencias;
- arquitectura;
- inventario;
- procedimientos;
- resultados de prueba;
- historial de evolución.

No incorpore contraseñas, credenciales ni información sensible sin protección.

---

## Paso 15. Crear el registro de consolidación operativa

El documento de liberación deberá incluir:

```text
Nombre del proyecto
Fecha
Arquitectura
Componentes
Capacidades
Limitaciones
Resultado de pruebas
Responsables
Condiciones de operación
Observaciones pendientes
Estado de aprobación
```


---

## Paso 16. Registrar la aprobación

Complete:

| Elemento | Información |
|---|---|
| Revisado por | |
| Fecha de revisión | |
| Resultado | Aprobada / Aprobada con observaciones / Rechazada |
| Condiciones | |
| Próxima revisión | |

Si la versión es rechazada, vuelva a las secciones correspondientes y resuelva las observaciones antes de continuar.

---

## Paso 17. Preparar la transición al Capítulo 10

La solución ya se encuentra técnicamente operativa.

Sin embargo, todavía debe evaluarse desde otras dimensiones:

- utilidad;
- desempeño;
- calidad;
- sesgos;
- privacidad;
- riesgos;
- transparencia;
- supervisión humana;
- sostenibilidad.

Reúna las evidencias que serán utilizadas en el capítulo siguiente:

- registros de solicitudes;
- respuestas generadas;
- tiempos aproximados;
- errores;
- incidencias;
- observaciones de usuarios;
- resultados de pruebas.

---

## Estado final del Capítulo 9

Al completar esta sección, el proyecto deberá encontrarse en el siguiente estado:

```text
Servicio implementado

↓

Servicio automatizado

↓

Servicio probado

↓

Servicio documentado

↓

Servicio respaldado

↓

Servicio operativamente consolidado
```

---

💡 **Nota técnica 9.10**

Un servicio en estado operativo no equivale a una solución definitiva ni garantiza que sea apropiado para cualquier contexto.

Significa únicamente que puede ejecutarse de manera controlada, utilizando procedimientos, responsables y condiciones claramente documentadas.

La pertinencia, seguridad, utilidad y responsabilidad de su uso serán evaluadas en el capítulo siguiente.

---

### Verificación

Complete la siguiente tabla:

| Verificación | Estado |
|---|:---:|
| La prueba operativa fue aprobada | ☐ |
| La arquitectura está actualizada | ☐ |
| El inventario está completo | ☐ |
| Los archivos técnicos corresponden a la versión vigente | ☐ |
| La documentación funcional está completa | ☐ |
| La documentación operativa está completa | ☐ |
| Las versiones están sincronizadas | ☐ |
| La ficha operativa fue completada | ☐ |
| Las limitaciones fueron documentadas | ☐ |
| Se creó un respaldo de la versión | ☐ |
| La liberación fue aprobada | ☐ |
| Las evidencias para evaluación están disponibles | ☐ |

---

### Problemas frecuentes

#### La documentación corresponde a versiones diferentes

No consolide la versión.

Actualice y sincronice todos los componentes antes de continuar.

---

#### El servicio funciona, pero no existe evidencia de validación

Recupere los registros de pruebas y complete el informe correspondiente.

Una versión operativa debe estar respaldada por evidencia.

---

#### Existen errores importantes pendientes

No registre la versión como operativa.

Corrija los problemas y repita la prueba.

---

#### No se asignaron responsables

Complete la matriz de responsabilidades antes de aprobar la versión.

---

#### El respaldo no incluye toda la documentación

Revise nuevamente la lista de componentes críticos y complete la copia.

---

### Buenas prácticas

- Consolide únicamente versiones probadas.
- Mantenga sincronizados código y documentación.
- Registre limitaciones de forma explícita.
- Respalde antes de liberar.
- Asigne responsables.
- Conserve evidencia de las pruebas.
- No declare operativa una versión con fallos críticos.
- Establezca una fecha de revisión futura.

---

### Checklist

Antes de finalizar el capítulo confirme que:

☐ El servicio dispone de una versión operativa.

☐ Los componentes están documentados.

☐ Los procedimientos fueron probados.

☐ Existen respaldos recuperables.

☐ Los responsables están definidos.

☐ Las limitaciones están registradas.

☐ La versión fue aprobada.

☐ La solución está preparada para su evaluación integral.

---

# Resumen del capítulo

En este capítulo usted:

✔ Revisó la arquitectura final del servicio.

✔ Construyó un inventario técnico.

✔ Documentó el procedimiento de inicio.

✔ Documentó el procedimiento de cierre.

✔ Estableció un mecanismo de monitoreo.

✔ Definió una estrategia de respaldo y recuperación.

✔ Incorporó medidas básicas de seguridad.

✔ Asignó roles y responsabilidades.

✔ Ejecutó una prueba operativa.

✔ Consolidó una versión operativa del servicio inteligente.

Como resultado, la solución ya no corresponde únicamente a una automatización funcional.

Ahora dispone de:

- documentación;
- controles;
- procedimientos;
- responsables;
- respaldos;
- condiciones de operación;
- evidencia de funcionamiento.

---

## Próximo capítulo

En el **Capítulo 10 – Evaluación, uso responsable y presentación de la solución** analizará el desempeño del servicio, sus limitaciones técnicas, los riesgos de sesgo y privacidad, las condiciones de supervisión humana y las evidencias necesarias para preparar el portafolio y la presentación final del proyecto.

---

# Fin del Capítulo 9

**Capítulo siguiente: Evaluación, uso responsable y presentación de la solución**
