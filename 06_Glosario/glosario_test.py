"""Pruebas del módulo de glosario."""

from __future__ import annotations

import csv
import unittest
from pathlib import Path

from glosario_interactivo import GlosarioInteractivo


class TestGlosario(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.base = Path(__file__).resolve().parent
        cls.csv_path = cls.base / "datos" / "glosario_datos.csv"
        cls.glosario = GlosarioInteractivo(cls.csv_path)

    def test_csv_bien_formado(self) -> None:
        self.assertTrue(self.csv_path.exists(), "El archivo CSV no existe")
        with self.csv_path.open("r", encoding="utf-8", newline="") as archivo:
            lector = csv.DictReader(archivo)
            esperados = {
                "término",
                "categoría",
                "definición",
                "contexto",
                "ejemplo",
                "módulo_relacionado",
                "palabras_clave",
            }
            self.assertEqual(set(lector.fieldnames or []), esperados)
            filas = list(lector)
            self.assertGreaterEqual(len(filas), 50)

    def test_no_hay_terminos_duplicados(self) -> None:
        vistos = set()
        for fila in self.glosario.terminos:
            termino = fila["término"].strip().lower()
            self.assertNotIn(termino, vistos, f"Término duplicado: {termino}")
            vistos.add(termino)

    def test_referencias_modulos_validas(self) -> None:
        modulos_validos = {
            "01_Fundamentos",
            "02_Analisis_Financiero",
            "03_Deteccion_Fraude",
            "04_AML_Compliance",
            "05_Proyectos_Integradores",
            "06_Glosario",
        }
        for fila in self.glosario.terminos:
            self.assertIn(fila["módulo_relacionado"], modulos_validos)

    def test_estadisticas_cobertura(self) -> None:
        stats = self.glosario.estadisticas()
        self.assertGreaterEqual(stats["total_terminos"], 50)
        categorias = stats["categorias"]
        self.assertGreaterEqual(categorias.get("Términos Financieros Básicos", 0), 15)
        self.assertGreaterEqual(
            categorias.get("Términos de Fraude", 0)
            + categorias.get("Términos AML/Compliance", 0),
            15,
        )
        self.assertGreaterEqual(categorias.get("Términos de Data Science", 0), 10)
        self.assertGreaterEqual(categorias.get("Términos de Análisis", 0), 10)

    def test_busquedas(self) -> None:
        resultado = self.glosario.buscar_término("KYC (Know Your Customer)")
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado["categoría"], "Términos AML/Compliance")

        por_keyword = self.glosario.buscar_palabras_clave("riesgo")
        self.assertGreater(len(por_keyword), 0)

        por_categoria = self.glosario.listar_por_categoría("Términos de Data Science")
        self.assertGreaterEqual(len(por_categoria), 10)

        aleatorio = self.glosario.termino_aleatorio()
        self.assertIn("término", aleatorio)

        similares = self.glosario.similares("Fraude")
        self.assertIsInstance(similares, list)


if __name__ == "__main__":
    unittest.main(verbosity=2)
