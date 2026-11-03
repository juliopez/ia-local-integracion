"""Pruebas locales de recuperación: no requieren Ollama ni Apps Script."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import puente_local as puente


class ValidacionDocumental(unittest.TestCase):
    def validar(self, pregunta):
        return puente.validar_respuesta_documental(pregunta, "RESPUESTA INVENTADA: diez días")

    def test_plazo_documentado(self):
        respuesta = self.validar("¿Cuántos días tengo para solicitar una revisión de mi evaluación?")
        self.assertIn("cinco días hábiles", respuesta)
        self.assertNotIn("diez días", respuesta)

    def test_matricula_no_documentada(self):
        self.assertEqual(
            self.validar("¿Cuándo comienza el período de matrícula?"),
            puente.RESPUESTA_SIN_EVIDENCIA,
        )

    def test_saludo(self):
        self.assertIn("Hola", self.validar("Hola"))

    def test_asignaturas_futuras(self):
        self.assertEqual(
            self.validar("¿Qué asignaturas tendremos el próximo semestre?"),
            puente.RESPUESTA_SIN_EVIDENCIA,
        )

    def test_estado_personal(self):
        self.assertEqual(
            self.validar("¿Estoy inscrito?"),
            puente.RESPUESTA_SIN_EVIDENCIA,
        )

    def test_numero_evaluaciones(self):
        self.assertEqual(
            self.validar("¿Cuántas evaluaciones son?"),
            puente.RESPUESTA_SIN_EVIDENCIA,
        )

    def test_no_inventar_fecha_publicacion(self):
        self.assertEqual(
            self.validar("¿En qué fecha publicarán las notas?"),
            puente.RESPUESTA_SIN_EVIDENCIA,
        )

    def test_destinatario_revision(self):
        respuesta = self.validar("¿A quién dirijo la solicitud de revisión de evaluaciones?")
        self.assertIn("coordinación académica", respuesta)

    def test_publicacion_notas(self):
        respuesta = self.validar("¿Dónde se comunican las calificaciones?")
        self.assertIn("aula virtual", respuesta)

    def test_documentos_obligatorios(self):
        respuesta = self.validar("¿Necesito documentos obligatorios para pedir revisión?")
        self.assertNotIn("certificado digital obligatorio", respuesta)
        self.assertNotIn("identificación oficial obligatoria", respuesta)


if __name__ == "__main__":
    unittest.main()
