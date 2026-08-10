from __future__ import annotations

import time
from pathlib import Path
from typing import Any

import requests


# ---------------------------------------------------------
# Configuración
# ---------------------------------------------------------

URL_APPS_SCRIPT = "https://script.google.com/macros/s/AKfycbxSXsR4wmgah3ONEl1uvV4KJ5hjQ1LU62GhmzCE1t8oUh5I-K103-S7-ue8CFJUDgmHQg/exec"

URL_OLLAMA = "http://localhost:11434/api/chat"
MODELO_OLLAMA = "nombre-del-modelo"

INTERVALO_SEGUNDOS = 10
RUTA_SYSTEM_PROMPT = Path("system_prompt.txt")


# ---------------------------------------------------------
# Cargar instrucciones permanentes
# ---------------------------------------------------------

def cargar_system_prompt() -> str:
    if not RUTA_SYSTEM_PROMPT.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo: {RUTA_SYSTEM_PROMPT}"
        )

    contenido = RUTA_SYSTEM_PROMPT.read_text(
        encoding="utf-8"
    ).strip()

    if not contenido:
        raise ValueError(
            "El archivo system_prompt.txt está vacío."
        )

    return contenido


# ---------------------------------------------------------
# Obtener una solicitud pendiente
# ---------------------------------------------------------

def obtener_solicitud() -> dict[str, Any] | None:
    respuesta = requests.get(
        URL_APPS_SCRIPT,
        timeout=30,
    )

    respuesta.raise_for_status()

    solicitud = respuesta.json()

    if not solicitud.get("disponible"):
        return None

    return solicitud


# ---------------------------------------------------------
# Construir mensaje del usuario
# ---------------------------------------------------------

def construir_mensaje(
    solicitud: dict[str, Any]
) -> str:
    nombre = str(solicitud.get("nombre", "")).strip()
    tipo = str(solicitud.get("tipo", "")).strip()
    consulta = str(
        solicitud.get("consulta", "")
    ).strip()

    if not consulta:
        raise ValueError(
            "La solicitud no contiene una consulta."
        )

    return (
        f"Nombre del usuario: {nombre}\n\n"
        f"Tipo de consulta: {tipo}\n\n"
        f"Consulta:\n{consulta}\n\n"
        "Responde en español, de manera clara, "
        "precisa y dentro del alcance del "
        "asistente académico."
    )


# ---------------------------------------------------------
# Consultar la API local de Ollama
# ---------------------------------------------------------

def consultar_ollama(
    system_prompt: str,
    mensaje_usuario: str,
) -> str:
    carga = {
        "model": MODELO_OLLAMA,
        "stream": False,
        "messages": [
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": mensaje_usuario,
            },
        ],
    }

    respuesta = requests.post(
        URL_OLLAMA,
        json=carga,
        timeout=300,
    )

    respuesta.raise_for_status()

    contenido = respuesta.json()

    texto = (
        contenido
        .get("message", {})
        .get("content", "")
        .strip()
    )

    if not texto:
        raise RuntimeError(
            "Ollama devolvió una respuesta vacía."
        )

    return texto


# ---------------------------------------------------------
# Registrar la respuesta en Apps Script
# ---------------------------------------------------------

def registrar_respuesta(
    fila: int,
    respuesta_ia: str,
    estado: str = "RESPONDIDA",
) -> None:
    carga = {
        "fila": fila,
        "respuesta": respuesta_ia,
        "estado": estado,
    }

    respuesta = requests.post(
        URL_APPS_SCRIPT,
        json=carga,
        timeout=30,
    )

    respuesta.raise_for_status()

    contenido = respuesta.json()

    if not contenido.get("correcto"):
        raise RuntimeError(
            contenido.get(
                "error",
                "No fue posible registrar la respuesta."
            )
        )


# ---------------------------------------------------------
# Procesar una solicitud
# ---------------------------------------------------------

def procesar_una_solicitud(
    system_prompt: str
) -> bool:
    solicitud = obtener_solicitud()

    if solicitud is None:
        print("No existen solicitudes pendientes.")
        return False

    fila = int(solicitud["fila"])

    print(f"Procesando la fila {fila}...")

    mensaje = construir_mensaje(solicitud)

    respuesta_ia = consultar_ollama(
        system_prompt,
        mensaje,
    )

    registrar_respuesta(
        fila=fila,
        respuesta_ia=respuesta_ia,
    )

    print(f"Fila {fila} procesada correctamente.")

    return True


# ---------------------------------------------------------
# Ejecución continua
# ---------------------------------------------------------

def main() -> None:
    system_prompt = cargar_system_prompt()

    print("Puente local iniciado.")
    print("Presione CTRL+C para detenerlo.")

    while True:
        try:
            procesar_una_solicitud(system_prompt)

        except requests.RequestException as error:
            print(f"Error de comunicación: {error}")

        except (
            FileNotFoundError,
            ValueError,
            RuntimeError,
            KeyError,
        ) as error:
            print(f"Error de procesamiento: {error}")

        except Exception as error:
            print(f"Error no previsto: {error}")

        time.sleep(INTERVALO_SEGUNDOS)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPuente local detenido.")
