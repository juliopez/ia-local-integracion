# Sesión 1 · Guía complementaria Ubuntu: instalación y validación de IA local

**Validación empírica:** 25 de octubre de 2026 · **Modalidad:** instructivo reproducible con observaciones del ensayo docente.  
**Alcance:** complemento para **Ubuntu** del [Laboratorio 1](Lab01.md) y del [Manual Técnico](../vol2_manual_tecnico/cap04_mt.md); **no sustituye** el itinerario principal para Windows. Los comandos de diagnóstico no deben confundirse con requisitos universales.  
**Estado:** Ollama, Qwen y Open WebUI **validados**; llmfit **por probar**; conectividad externa de Ollama **por asegurar**.

## 0. Objetivo y arquitectura

Construir una primera conversación local a través de **Navegador → Open WebUI (Docker) → Ollama (Ubuntu) → Modelo Qwen (GPU/CPU)**. Antes de elegir un modelo, examinar la capacidad del equipo. Distinguir el funcionamiento de la infraestructura de la calidad y seguimiento de instrucciones de las respuestas.

> **Importante para el estudiantado:** la sesión presencial dura **120 min**, pero esta guía registra además correcciones particulares del computador usado para el ensayo; no es necesario instalar controladores o Docker si el equipo ya está preparado. Lab01 también contempla la definición inicial del problema del Proyecto Integrador.

## 1. Diagnóstico inicial, sin modificar el computador

```bash
lsb_release -ds
uname -m
lscpu | grep -E 'Model name|CPU\(s\):'
free -h
df -h /
lspci | grep -Ei 'VGA|3D|Display'
for app in ollama docker python3 git curl; do
  command -v "$app" >/dev/null 2>&1 && echo "$app: INSTALADO" || echo "$app: NO INSTALADO"
done
command -v ollama >/dev/null 2>&1 && ollama list
```

**Ensayo docente:** Ubuntu 26.04.1 LTS, 12 procesadores lógicos, 14 GiB RAM, GeForce RTX 2050 con 4 GiB VRAM; disco inicial con ~30 GiB libres. Ollama, Docker, Python, Git y cURL ya estaban instalados. **Esos valores son del computador de prueba, no requisitos mínimos oficiales.** Registrar particularmente memoria *disponible* y espacio de disco antes de descargar imágenes y modelos.

## 2. Selección razonada de modelos: llmfit

**Antes de descargar modelos**, abrir [llmfit — repositorio y documentación oficial](https://github.com/AlexsJones/llmfit). Esta herramienta compara **hardware detectado**, memoria RAM/VRAM, tamaños/cuantizaciones y estimaciones de capacidad para modelos locales; sus resultados son orientativos y no sustituyen pruebas reales.

1. Revisar el hardware detectado en el diagnóstico anterior.
2. Instalar llmfit **solo si se necesita la CLI**, siguiendo el procedimiento vigente documentado en su repositorio para Ubuntu. **No se ha instalado ni probado llmfit todavía en este ensayo.**
3. Cuando esté instalado, ejecutar:

   ```bash
   llmfit system
   llmfit recommend
   llmfit fit --perfect -n 5
   ```

4. Registrar **modelo recomendado, formato/cuantización, memoria estimada y justificación**. Comparar luego esa predicción con `ollama ps` y el rendimiento observado.
5. Si la instalación de llmfit no es posible, consultar su documentación y justificar la selección del modelo a partir de RAM/VRAM/almacenamiento. **llmfit no sustituye a Ollama**: ayuda a elegir; Ollama ejecuta el modelo.

En el ensayo se utilizó **`qwen2.5:1.5b`**, aproximadamente 986 MB de descarga, **seleccionado manualmente antes de usar llmfit**. No presentarlo como una recomendación efectivamente calculada por llmfit.

## 3. Verificar Ollama y GPU (solo si aplica)

```bash
ollama --version
systemctl is-active ollama
curl -s http://localhost:11434/api/tags
nvidia-smi
```

Si `nvidia-smi` no existe y el equipo tiene NVIDIA, diagnosticar primero:

```bash
lspci -k -d 10de:
lsmod | grep -E 'nvidia|nouveau' || true
ubuntu-drivers devices
mokutil --sb-state
```

**Incidencia real:** Ubuntu detectaba la GPU, pero faltaba el controlador activo; Secure Boot estaba activado. Se instaló mediante `sudo apt update` y `sudo ubuntu-drivers install --recommended`; tras reiniciar, `nvidia-smi` mostró **driver 595.99.02**, RTX 2050, 4096 MiB de VRAM. **No ejecutar este paso indiscriminadamente:** las necesidades de controladores, Secure Boot y posibles pantallas MOK varían según el equipo. Evitar instalaciones a ciegas y guardar el trabajo antes de reiniciar.

## 4. Descargar y probar el primer modelo

```bash
ollama run qwen2.5:1.5b
```

En el indicador `>>>` realizar una consulta de prueba en español. Desde otra terminal:

```bash
ollama ps
```

**Ensayo docente verificado:** `qwen2.5:1.5b`, carga del modelo ~1,4 GB, contexto 4096 y **PROCESSOR: 100% GPU**. Se observó que las respuestas no siempre seguían exactamente la longitud o estructura solicitada y contenían imprecisiones; **ejecución exitosa no implica respuesta correcta**.

## 5. Revisar Docker y preservar otras cargas de trabajo

```bash
systemctl is-active docker
id -nG
docker ps
```

**Incidencia real:** Docker estaba activo, pero el usuario no pertenecía al grupo `docker`, por lo que recibió `permission denied`. Se decidió utilizar `sudo docker` **sin alterar privilegios permanentes**. Un miembro del grupo `docker` obtiene privilegios equivalentes a administrador.

```bash
sudo docker ps -a
df -h /
sudo docker system df
sudo ss -ltnp '( sport = :3000 )'
free -h
```

**Ensayo docente:** había 14 contenedores activos vinculados a Big Data (Hadoop, Spark, Kafka, NiFi, entre otros), ~28 GB libres, y el puerto 3000 libre. **No eliminar otros contenedores, imágenes ni volúmenes**; evitar `docker system prune` sin revisar el impacto.

## 6. Instalar Open WebUI sin reinstalar Ollama

Se utilizó una variante reducida de Open WebUI; su imagen puede requerir componentes adicionales para ciertas prestaciones de documentos/Knowledge. Consultar la [guía oficial de Open WebUI](https://docs.openwebui.com/getting-started/quick-start/).

```bash
sudo docker run -d \
  --name open-webui \
  --restart unless-stopped \
  -p 127.0.0.1:3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -v open-webui:/app/backend/data \
  -e OLLAMA_BASE_URL=http://host.docker.internal:11434 \
  -e WEBUI_SECRET_KEY="$(openssl rand -hex 32)" \
  ghcr.io/open-webui/open-webui:main-slim

sudo docker ps --filter name=open-webui
```

Abrir **http://localhost:3000**, registrar la primera cuenta administrativa local con contraseña privada y comprobar el selector de modelos. El volumen `open-webui` conserva los datos al reiniciar el contenedor.

> **Si ya existe un contenedor llamado `open-webui`, no repetir `docker run`**; inspeccionar primero su estado y su configuración.

## 7. Diagnóstico de conectividad Open WebUI → Ollama

**Incidencia real:** Open WebUI abrió correctamente, pero indicó «No hay modelos disponibles». Diagnóstico:

```bash
sudo ss -ltnp '( sport = :11434 )'
sudo docker inspect open-webui \
  --format '{{range .Config.Env}}{{println .}}{{end}}' | grep '^OLLAMA_BASE_URL='
ollama list
```

Ollama escuchaba en **`127.0.0.1:11434`**, mientras Open WebUI dentro de Docker llamaba a `host.docker.internal:11434`. El `localhost` del contenedor **no es** el `localhost` del anfitrión.

En el ensayo se aplicó una corrección persistente:

```bash
sudo mkdir -p /etc/systemd/system/ollama.service.d
printf '[Service]\nEnvironment="OLLAMA_HOST=0.0.0.0:11434"\n' | sudo tee /etc/systemd/system/ollama.service.d/override.conf
sudo systemctl daemon-reload
sudo systemctl restart ollama
```

**Advertencia de seguridad crucial:** esto hace que Ollama escuche en **todas las interfaces**, incluidas potencialmente las de red del equipo, y **no debe adoptarse como configuración final sin restringir el puerto 11434**. En un equipo conectado a otras redes, preferir una unión limitada a la interfaz del puente Docker o reglas de firewall explícitas y verificadas. Hasta aplicar esa protección, la seguridad de la exposición **sigue pendiente**. No reenviar ni publicar el puerto de Ollama en el enrutador.

Tras la corrección, el selector de Open WebUI mostró el modelo `qwen2.5:1.5b` sin reinstalar ni descargar nada de nuevo.

## 8. Primera conversación y validación

Desde Open WebUI, seleccionar `qwen2.5:1.5b` y enviar:

> Explica qué es la inteligencia artificial generativa local para un docente universitario. Responde en español utilizando exactamente tres viñetas: definición, ventaja y limitación.

**Resultado del ensayo:** Open WebUI devolvió una respuesta desde el modelo local. Sin embargo, **no respetó las tres viñetas** y mezcló características generales de IA generativa con las específicas de IA local. Esto será una evidencia didáctica útil para la sesión 2: la especialización requiere instrucciones verificables, contexto y evaluación crítica, no solo una conexión técnica.

## 9. Lista de comprobación y pendientes

- [x] Ubuntu diagnosticado
- [x] NVIDIA RTX 2050 y driver comprobados en este equipo
- [x] Ollama y API local operativos
- [x] Modelo `qwen2.5:1.5b` descargado
- [x] Inferencia 100 % GPU verificada con `ollama ps`
- [x] Docker operativo mediante `sudo`
- [x] Open WebUI instalado en `http://localhost:3000`
- [x] Modelo detectado en Open WebUI
- [x] Generación de respuesta desde el navegador
- [ ] **Instalar y ejecutar llmfit**: documentar recomendaciones reales en este equipo
- [ ] **Limitar y verificar el acceso de red a Ollama** en el puerto 11434
- [ ] Completar el producto de Lab01 sobre definición del problema y alcance inicial, si corresponde a la actividad del grupo
- [ ] Comprobar si `main-slim` permite las funciones de Knowledge requeridas en la sesión 2; de no ser así, planificar su habilitación

## Referencias

- [Laboratorio 1 del repositorio](Lab01.md)
- [Manual Técnico · Capítulo 4](../vol2_manual_tecnico/cap04_mt.md)
- [llmfit (oficial)](https://github.com/AlexsJones/llmfit)
- [llmfit: comandos de diagnóstico y recomendación](https://github.com/AlexsJones/llmfit/blob/main/docs/cli.md)
- [Open WebUI: instalación](https://docs.openwebui.com/getting-started/quick-start/)
- [Ollama: documentación](https://docs.ollama.com/)
