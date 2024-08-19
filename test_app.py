import unittest
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE" # Necesario para evitar incompatiblidades
from pysentimiento import create_analyzer

class TestSentimentAnalysisApp(unittest.TestCase):

    def setUp(self):
        # Configuración inicial para las pruebas
        self.analyzer = create_analyzer(task="sentiment", lang="es")

    def test_sentiment_analysis_positive(self):
        # Simula un comentario positivo y verifica que el análisis es correcto
        comment = "Me encanta este producto, es maravilloso"
        result = self.analyzer.predict(comment)
        self.assertEqual(result.output, "POS")
        self.assertGreater(result.probas['POS'], 0.5)

    def test_sentiment_analysis_negative(self):
        # Simula un comentario negativo y verifica que el análisis es correcto
        comment = "Este servicio es terrible, no lo recomiendo"
        result = self.analyzer.predict(comment)
        self.assertEqual(result.output, "NEG")
        self.assertGreater(result.probas['NEG'], 0.5)

    def test_sentiment_analysis_neutral(self):
        # Simula un comentario neutral y verifica que el análisis es correcto
        comment = "Es un producto más, ni bueno ni malo"
        result = self.analyzer.predict(comment)
        self.assertEqual(result.output, "NEU")
        self.assertGreater(result.probas['NEU'], 0.5)

if __name__ == "__main__":
    unittest.main()
