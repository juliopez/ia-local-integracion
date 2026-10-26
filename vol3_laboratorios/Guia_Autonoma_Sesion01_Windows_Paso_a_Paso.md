# Sesión 1 — Instalación y primera conversación con un LLM local
## Guía autónoma paso a paso para Windows 10/11

**Tiempo de referencia:** 120 minutos · **Público:** docentes sin experiencia previa en línea de comandos.  
**Objetivo:** reconocer qué modelos puede ejecutar su computador con **LLMFit**, instalar **Ollama**, descargar y usar un modelo desde **PowerShell**, instalar **Open WebUI** y conversar desde su interfaz.

> **Cómo utilizar esta guía:** lea un paso, realice exactamente la acción y confirme el resultado antes de continuar. No necesita abrir otro manual para completar el recorrido principal. Las explicaciones avanzadas y los métodos alternativos aparecen al final.
>
> **Importante sobre Open WebUI:** utilizaremos la **aplicación de escritorio para Windows**, sin Docker ni instalación manual mediante Python. El servidor local de la aplicación utiliza habitualmente **http://localhost:8080**; si el puerto está ocupado, puede utilizar otro. **http://localhost:3000** corresponde al ejemplo de instalación con Docker y no es la dirección de esta guía. La aplicación de escritorio se encuentra en etapa alfa: si falla, registre el mensaje y solicite apoyo.

## Antes de comenzar — Prepare el computador (5 minutos)

1. Guarde sus documentos y conecte el equipo a una red con Internet. Las descargas pueden utilizar varios gigabytes.
2. Compruebe que puede instalar programas. Si su institución administra el computador y requiere una clave de administrador, solicite apoyo a soporte TI; **no desactive controles de seguridad**.
3. Abra una carpeta de trabajo: presione simultáneamente las teclas **Windows + E**; en el Explorador de archivos vaya a **Documentos**; haga clic derecho en un espacio vacío → **Nuevo → Carpeta**; póngale el nombre **Taller-IA-Local**.
4. Mantenga esta guía abierta en otra ventana o en su teléfono para consultar los pasos.

## Parte 1 — Conocer el computador mediante LLMFit (15–20 minutos)

**¿Para qué sirve?** LLMFit estima qué modelos podrían caber y funcionar en la memoria y procesador de su equipo. No instala los modelos ni garantiza la velocidad final.

**Paso 1.** Abra Chrome, Edge o Firefox y escriba en la barra de direcciones:  
**https://github.com/AlexsJones/llmfit/releases**. Presione **Enter**.

**Paso 2.** En la versión más reciente, despliegue **Assets** si está oculto. Si utiliza un computador habitual con procesador Intel o AMD de 64 bits, descargue el archivo que contiene **`x86_64-pc-windows-msvc.zip`** en su nombre. Si utiliza Windows ARM, busque **`aarch64-pc-windows-msvc.zip`**. No descargue los archivos terminados en `.sha256` ni el código fuente.

**Paso 3.** Abra **Descargas** (Windows + E → Descargas), haga clic derecho sobre el archivo ZIP → **Extraer todo...** → **Extraer**.

**Paso 4.** Entre en la carpeta extraída y localice **`llmfit.exe`**. Haga clic en la **barra de direcciones** del Explorador (arriba de la lista de archivos), escriba **`powershell`** y presione **Enter**. Se abrirá PowerShell directamente en esa carpeta.

**Paso 5.** En la ventana de PowerShell, escriba exactamente:

```powershell
.\llmfit.exe
```

Presione **Enter**. Si Windows muestra una advertencia de confianza o seguridad, **no la ignore automáticamente**: confirme que descargó el archivo del repositorio oficial y consulte al docente o a TI si el equipo lo bloquea.

**Paso 6.** Observe la lista o interfaz de LLMFit. Busque la memoria **RAM**, la tarjeta **GPU/VRAM** si existe, y las estimaciones de **compatibilidad (fit)**, **velocidad (speed/tokens por segundo)** y **calidad (quality)**. Anote en una hoja el modelo que considera apropiado. Para practicar, este tutorial usa **`qwen2.5:1.5b`** como modelo ligero de referencia; es posible que LLMFit muestre otros modelos más recientes o más adecuados.

**Comprobación 1:** LLMFit se abrió y pudo identificar al menos un modelo viable. Si no logra ejecutarlo, registre el error, anote la RAM del equipo (Configuración → Sistema → Acerca de) y continúe con el modelo de referencia; LLMFit orienta la selección, pero no impide avanzar.

## Parte 2 — Instalar Ollama (15 minutos)

**¿Para qué sirve?** Ollama descarga y ejecuta modelos en el computador.

**Paso 7.** Abra **https://ollama.com/download/windows** en su navegador y presione **Enter**.

**Paso 8.** Seleccione **Download for Windows** o el botón equivalente. Cuando termine la descarga, haga doble clic en el instalador oficial desde **Descargas**.

**Paso 9.** Siga los mensajes de instalación. Espere a que finalice. Es posible que Ollama quede ejecutándose en segundo plano.

**Paso 10.** Abra **PowerShell**: haga clic en **Inicio** o presione la tecla **Windows**; escriba **PowerShell**; seleccione **Windows PowerShell**. **No es necesario ejecutar como administrador.**

**Paso 11.** Escriba y presione **Enter**:

```powershell
ollama --version
```

**Comprobación 2:** aparece información de versión. Si PowerShell indica que no reconoce `ollama`, cierre esa ventana, vuelva a abrirla y repita el comando. Si continúa el error, confirme que la instalación terminó y consulte al docente.

## Parte 3 — Descargar un modelo y comprobarlo (15–25 minutos)

**Paso 12.** En **la misma ventana de PowerShell**, escriba:

```powershell
ollama pull qwen2.5:1.5b
```

Presione **Enter**. Ollama comenzará la descarga. Espere a que termine; **no cierre la ventana** mientras se descarga.

**Paso 13.** Para comprobar que el modelo quedó disponible, escriba:

```powershell
ollama list
```

Presione **Enter**. Busque **`qwen2.5:1.5b`** en la lista.

**Comprobación 3:** el modelo aparece en `ollama list`. Si la descarga se interrumpió, compruebe la conexión y vuelva a ejecutar `ollama pull qwen2.5:1.5b`.

## Parte 4 — Conversar con el modelo desde PowerShell (15 minutos)

**Paso 14.** Escriba:

```powershell
ollama run qwen2.5:1.5b
```

Presione **Enter**. Tras iniciar, verá una indicación para ingresar mensajes.

**Paso 15.** Escriba esta consulta y presione **Enter**:

> ¿Qué es un modelo de inteligencia artificial local? Explícalo para un docente en tres oraciones.

**Paso 16.** Espere la respuesta. Después escriba otra pregunta:

> Indica dos ventajas y dos limitaciones de utilizar un modelo de lenguaje local en educación superior.

**Paso 17.** Para salir de la conversación, escriba:

```text
/bye
```

Presione **Enter**. Volverá al indicador habitual de PowerShell. Ollama puede continuar funcionando en segundo plano.

**Comprobación 4:** pudo hacer dos preguntas y obtener respuestas. **Guarde una captura:** presione **Windows + Shift + S**, marque la región de la pantalla y guarde la imagen dentro de **Documentos/Taller-IA-Local**.

## Parte 5 — Instalar Open WebUI mediante un instalador (20–30 minutos)

**¿Para qué sirve?** Open WebUI presenta una interfaz gráfica para conversar con modelos sin escribir cada consulta en PowerShell.

**Paso 18.** Abra **https://github.com/open-webui/desktop/releases** en el navegador. Verifique que pertenece al proyecto oficial **open-webui/desktop**.

**Paso 19.** En la última versión disponible, ubique **Assets** y descargue el **instalador para Windows x64 (`.exe`)**; en computadores Windows ARM, seleccione el correspondiente a ARM64. No descargue archivos para Linux ni macOS.

**Paso 20.** Abra **Descargas** y haga doble clic en el instalador. Complete la instalación siguiendo la ventana que aparezca. Si Windows o la institución bloquea la ejecución, no desactive protecciones ni fuerce la instalación: registre el mensaje y consulte al docente.

**Paso 21.** Presione la tecla **Windows**, escriba **Open WebUI** y abra la aplicación. En la primera ejecución se requiere conexión a Internet y la preparación del entorno puede tardar. Espere a que el servidor local termine de iniciarse; no cierre la aplicación.

**Paso 22.** Abra **Chrome o Edge**. En la barra superior de direcciones (no en el buscador), escriba **http://localhost:8080** y presione **Enter**. Debe aparecer Open WebUI. Si la página no abre, revise en la aplicación de escritorio el **estado del servidor y el puerto configurado**: puede que no haya terminado de iniciar o haya elegido otro puerto. En ese caso, utilice la dirección que muestre la aplicación. No instale Docker solo para cambiar de puerto.

**Paso 23.** Si es la primera visita, complete la creación de la cuenta administradora **local** que solicite Open WebUI. A continuación, compruebe la conexión con Ollama: su dirección habitual es **http://localhost:11434** (observe que **11434 es el puerto de Ollama**, no el de Open WebUI). En el selector de modelos, busque **`qwen2.5:1.5b`**. Si no aparece, confirme con `ollama list` que el modelo está descargado y verifique el estado de Ollama y la configuración de conexiones de Open WebUI.

**Paso 24.** Abra una conversación nueva, seleccione el modelo y escriba:

> Explica qué es la inteligencia artificial local para un docente de educación superior. Responde con una definición, una ventaja y una limitación.

Presione **Enter** o el botón de enviar.

**Comprobación 5:** la interfaz de Open WebUI abre, permite seleccionar el modelo **de Ollama** y genera una respuesta. Guarde una captura.

> **Recuerde:** en esta instalación, el acceso habitual desde el navegador es **http://localhost:8080**. **No necesita Docker** para utilizar Open WebUI ni para abrirlo en el navegador. Si el puerto 8080 está ocupado, consulte el puerto real en la aplicación de escritorio.

## Evidencias al terminar la sesión

- [ ] Abrí LLMFit y registré una recomendación o su error.
- [ ] Comprobé Ollama con `ollama --version`.
- [ ] Descargué el modelo y aparece en `ollama list`.
- [ ] Conversé con el modelo en PowerShell.
- [ ] Abrí Open WebUI y obtuve una respuesta **utilizando Ollama**.
- [ ] Guardé las capturas en **Documentos/Taller-IA-Local**.
- [ ] Accedí desde el navegador a **http://localhost:8080** (o al puerto indicado por la aplicación).

## Si aparece un problema

| Situación | Qué debe hacer |
|---|---|
| LLMFit no abre | Compruebe que extrajo el ZIP y que ejecutó `.\llmfit.exe` en la carpeta correcta. Si el sistema lo bloquea, consulte a TI; no eluda controles. |
| `ollama` no se reconoce | Reabra PowerShell y compruebe la instalación de Ollama. |
| Modelo no aparece | Repita `ollama list` y, si falta, `ollama pull qwen2.5:1.5b`. |
| La respuesta tarda | Espere; el rendimiento depende del equipo. Evite ejecutar varias descargas o modelos simultáneamente. |
| Open WebUI abre pero no ve Ollama | Compruebe la ejecución de Ollama, el proveedor configurado y la conexión local al puerto 11434. |
| Open WebUI Desktop no instala | Registre el error y consúltelo con el docente. Es una aplicación en etapa alfa. |
| `localhost:8080` no responde | Compruebe que Open WebUI Desktop esté abierto y que su servidor local esté iniciado. Consulte el puerto indicado por la aplicación; no instale Docker para resolverlo. |
| Equipo institucional bloquea la instalación | Solicite soporte TI; no desactive antivirus, restricciones ni políticas de la institución. |

## Para profundizar después de la práctica

- [Laboratorio 1 original](Lab01.md): fundamentación y actividades ampliadas.
- [Manual Técnico](../vol2_manual_tecnico/): procedimientos avanzados y alternativas de instalación.
- [Guía de Ubuntu](Guia_Ubuntu_Sesion01_Validacion_2026.md): instalación y problemas registrados en ese sistema.
- [Recursos interactivos](../RECURSOS_INTERACTIVOS.md): tokenización y visualización didáctica de modelos.
- Documentación oficial: [LLMFit](https://github.com/AlexsJones/llmfit), [Ollama](https://ollama.com/download/windows), [Open WebUI Desktop](https://github.com/open-webui/desktop) y [Open WebUI Quick Start](https://docs.openwebui.com/getting-started/quick-start/).

**Fin de la sesión 1.** La configuración de asistentes, System Prompts, Knowledge y Skills se realiza en la **sesión 2**.
