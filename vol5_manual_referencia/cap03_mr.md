# Capítulo 3

# Guía rápida de comandos

---

## Objetivo

Reunir los principales comandos utilizados durante el desarrollo del taller, proporcionando una referencia de consulta rápida para las tareas más frecuentes relacionadas con la instalación, configuración, administración y operación de la solución.

Este capítulo no pretende reemplazar la documentación oficial de cada herramienta, sino ofrecer un resumen práctico de los comandos utilizados durante las actividades desarrolladas en esta colección.

---

# Cómo utilizar este capítulo

Los comandos se encuentran organizados por herramienta.

Cada sección incluye:

- propósito;
- comandos principales;
- descripción;
- observaciones.

Antes de ejecutar cualquier comando, verifique que se encuentra en el entorno correcto y que dispone de los permisos necesarios.

---

# Organización del capítulo

| Sección | Contenido          |
| ------- | ------------------ |
| C3.1    | Ollama             |
| C3.2    | Python             |
| C3.3    | Pip                |
| C3.4    | Open WebUI         |
| C3.5    | Google Apps Script |
| C3.6    | Sistema operativo  |

---

# C3.0

# llmfit — selección de modelos en Ubuntu, Windows y macOS

Los siguientes comandos son **alternativas**, no instrucciones consecutivas. Permiten realizar el diagnóstico de hardware antes de instalar Ollama.

**Instalación mediante script:**

```bash
curl -fsSL https://llmfit.axjns.dev/install.sh | sh
```

**Ejecución temporal con Docker y TUI:**

```bash
sudo docker run -it --rm ghcr.io/alexsjones/llmfit --tui
```

Docker debe estar instalado para la segunda opción. La ejecución en contenedor puede ofrecer una detección de hardware diferente de la instalación nativa, especialmente respecto de la GPU. Revise el script remoto antes de ejecutarlo. Consulte https://github.com/AlexsJones/llmfit para confirmar instrucciones actualizadas.

**Windows 10/11 (x86-64) — instalación nativa recomendada:**

En PowerShell, si Scoop ya está instalado:

```powershell
scoop install llmfit
llmfit
```

Si no dispone de Scoop, consulte https://scoop.sh/ para instalarlo o descargue el binario compatible desde https://github.com/AlexsJones/llmfit/releases. No es necesario instalar Ubuntu, WSL2 ni Docker para utilizar la versión nativa de Windows. Compruebe la procedencia del ejecutable y, cuando corresponda, su firma digital.

**macOS — Homebrew:**

```bash
brew install AlexsJones/llmfit/llmfit
llmfit
```

**Criterio para el taller:** llmfit es opcional. Si la instalación no resulta viable, registre RAM, CPU y GPU/VRAM (si corresponde), seleccione manualmente un modelo compatible en la biblioteca de Ollama y continúe con el laboratorio. Las estimaciones de llmfit requieren una prueba real de rendimiento.


---

# C3.0.1

# Tokenización — referencia rápida

**Herramienta interactiva:** https://platform.openai.com/tokenizer

- **Token:** unidad de texto definida por el tokenizador; no siempre coincide con una palabra.
- **Token ID:** número que identifica un token dentro de un vocabulario específico; no es una medida de significado.
- **Embedding interno:** representación vectorial aprendida del token que el modelo utiliza durante su procesamiento; no equivale automáticamente al embedding de recuperación utilizado en RAG.
- **Ventana de contexto:** límite de tokens que el modelo puede considerar, condicionado por el modelo y su configuración.

**Actividad rápida:** compare «¿Qué es el aprendizaje activo?» con una instrucción de retroalimentación formativa más extensa. Observe cantidad y segmentación de tokens.

**Advertencia:** el tokenizador de OpenAI es un ejemplo pedagógico; los modelos disponibles en Ollama pueden usar tokenizadores distintos. No ingrese información personal o académica confidencial en la herramienta web.

---

# C3.1

# Comandos de Ollama

---

## Objetivo

Presentar los comandos básicos utilizados para administrar modelos de lenguaje mediante Ollama.

---

## Listar modelos instalados

```bash
ollama list
```

Descripción

Muestra todos los modelos disponibles en el equipo.

---

## Descargar un modelo

```bash
ollama pull nombre_modelo
```

Descripción

Descarga un modelo disponible a través de Ollama. Antes de ejecutarlo, seleccione un candidato según el hardware (opcionalmente mediante llmfit), confirme su etiqueta exacta en la biblioteca oficial de Ollama y siga el Capítulo 3 del Manual Técnico. `nombre_modelo` es un marcador de posición.

---

## Ejecutar un modelo

```bash
ollama run nombre_modelo
```

Descripción

Inicia una conversación utilizando el modelo especificado.

---

## Eliminar un modelo

```bash
ollama rm nombre_modelo
```

Descripción

Elimina un modelo instalado localmente.

---

## Mostrar información de un modelo

```bash
ollama show nombre_modelo
```

Descripción

Presenta información general del modelo instalado.

---

# C3.2

# Comandos de Python

---

## Verificar instalación

```bash
python --version
```

---

## Verificar instalación mediante Python 3

```bash
python3 --version
```

---

## Ejecutar un programa

```bash
python archivo.py
```

---

## Crear entorno virtual

```bash
python -m venv nombre_entorno
```

---

## Activar entorno virtual (Windows)

```bash
nombre_entorno\Scripts\activate
```

---

## Activar entorno virtual (Linux / macOS)

```bash
source nombre_entorno/bin/activate
```

---

# C3.3

# Comandos de Pip

---

## Verificar versión

```bash
pip --version
```

---

## Instalar un paquete

```bash
pip install nombre_paquete
```


---

## Mostrar paquetes instalados

```bash
pip list
```

---

## Actualizar un paquete

```bash
pip install --upgrade nombre_paquete
```

---

## Desinstalar un paquete

```bash
pip uninstall nombre_paquete
```

---

# C3.4

# Open WebUI

La administración de Open WebUI dependerá del método de instalación utilizado. Para iniciar, detener o reiniciar el servicio, consulte el procedimiento correspondiente en el **Manual Técnico**.


---

# C3.5

# Google Apps Script

---

## Ejecutar una función

Acción realizada desde el editor de Google Apps Script.

---

## Implementar una nueva versión del Web App

Acción realizada desde **Implementar → Gestionar implementaciones**, creando una nueva versión de la implementación cuando se hayan realizado cambios en el código.

---

## Consultar registros

Acción realizada desde el menú **Ejecuciones**.

---

## Autorizar permisos

Durante la configuración inicial, Google Apps Script puede solicitar autorización para acceder a los servicios de Google Workspace utilizados por la solución.

---

# C3.6

# Comandos del sistema operativo

---

## Cambiar de directorio

```bash
cd nombre_directorio
```

---

## Mostrar contenido del directorio

```bash
dir
```

(Windows)

```bash
ls
```

(Linux / macOS)

---

## Mostrar ruta actual

```bash
cd
```

(Windows)

```bash
pwd
```

(Linux / macOS)

---

## Crear carpeta

```bash
mkdir nombre_carpeta
```

---

## Eliminar carpeta

```bash
rmdir nombre_carpeta
```

---

## Limpiar pantalla

```bash
cls
```

(Windows)

```bash
clear
```

(Linux / macOS)

---

# Buenas prácticas

- Ejecutar únicamente comandos cuyo funcionamiento se comprenda.
- Verificar el directorio de trabajo antes de modificar archivos.
- Mantener documentadas las versiones de las herramientas utilizadas.
- Registrar cualquier cambio importante realizado mediante comandos administrativos.
- Evitar ejecutar comandos con privilegios elevados cuando no sean necesarios.

---

# Relación con la colección

| Documento                      | Relación                                                  |
| ------------------------------ | --------------------------------------------------------- |
| Libro del Participante         | Referencia rápida durante el estudio de las herramientas. |
| Manual Técnico                 | Apoyo durante la instalación y configuración.             |
| Manual del Proyecto Integrador | Consulta durante el desarrollo del Proyecto Integrador.   |
| Cuaderno de Laboratorios       | Referencia práctica durante los laboratorios.             |

---

# Cierre del capítulo

La presente guía reúne los comandos utilizados con mayor frecuencia durante el desarrollo del taller.

Se recomienda utilizar este capítulo como material de consulta rápida durante la implementación y administración de la solución, manteniendo documentadas las versiones de las herramientas utilizadas y registrando los cambios relevantes en los procedimientos descritos en la colección.

---
