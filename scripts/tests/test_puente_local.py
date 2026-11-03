"""Pruebas aisladas: no contactan Google Workspace ni Ollama."""
import importlib.util
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

ARCHIVO = Path(__file__).resolve().parents[1] / "puente_local.py"
spec = importlib.util.spec_from_file_location("puente_local", ARCHIVO)
puente = importlib.util.module_from_spec(spec)
spec.loader.exec_module(puente)


def respuesta_json(datos):
    objeto = Mock()
    objeto.json.return_value = datos
    objeto.raise_for_status.return_value = None
    return objeto


class PuenteLocalTest(unittest.TestCase):
    @patch.object(puente.requests, "post")
    @patch.object(puente.requests, "get")
    def test_lectura_no_reserva_ni_envia(self, get, post):
        get.return_value = respuesta_json({
            "disponible": True, "fila": 2,
            "tipo": "consulta", "consulta": "Ejemplo ficticio",
        })
        puente.modo_lectura()
        get.assert_called_once()
        post.assert_not_called()

    @patch.object(puente, "consultar_ollama", return_value="Respuesta simulada")
    @patch.object(puente.requests, "get")
    @patch.object(puente.requests, "post")
    def test_prueba_no_contacta_google(self, post, get, ollama):
        with patch.object(puente, "cargar_system_prompt", return_value="Rol ficticio"):
            puente.modo_prueba()
        get.assert_not_called()
        post.assert_not_called()
        ollama.assert_called_once()

    @patch.object(puente, "registrar_respuesta")
    @patch.object(puente, "consultar_ollama", return_value="Respuesta simulada")
    @patch.object(puente, "reclamar_solicitud")
    def test_completo_procesa_y_registra(self, reclamar, ollama, registrar):
        reclamar.return_value = {
            "disponible": True, "fila": 2,
            "nombre": "Ficticio", "tipo": "consulta",
            "consulta": "Prueba local",
        }
        self.assertTrue(puente.procesar_una_solicitud("Reglas"))
        registrar.assert_called_once_with(2, "Respuesta simulada")

    @patch.object(puente, "registrar_respuesta")
    @patch.object(puente, "consultar_ollama")
    @patch.object(puente, "reclamar_solicitud", return_value=None)
    def test_completo_sin_pendientes(self, reclamar, ollama, registrar):
        self.assertFalse(puente.procesar_una_solicitud("Reglas"))
        ollama.assert_not_called()
        registrar.assert_not_called()

    @patch.object(puente.requests, "post")
    def test_reclamar_rechazado(self, post):
        post.return_value = respuesta_json({"correcto": False, "error": "Acceso denegado"})
        with self.assertRaisesRegex(RuntimeError, "Acceso denegado"):
            puente.reclamar_solicitud()

    @patch.object(puente.requests, "get")
    def test_error_en_lectura(self, get):
        get.return_value = respuesta_json({"disponible": False, "error": "Hoja no encontrada"})
        with self.assertRaisesRegex(RuntimeError, "Hoja no encontrada"):
            puente.obtener_solicitud()


if __name__ == "__main__":
    unittest.main()
