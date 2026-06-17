"""Glosario interactivo para AML-ACADEMY-fintech."""

from __future__ import annotations

import csv
import random
from datetime import datetime
from pathlib import Path
from typing import Dict, List


class GlosarioInteractivo:
    """Gestiona búsquedas y navegación del glosario."""

    CAMPOS_REQUERIDOS = [
        "término",
        "categoría",
        "definición",
        "contexto",
        "ejemplo",
        "módulo_relacionado",
        "palabras_clave",
    ]

    def __init__(self, ruta_csv: str | Path | None = None) -> None:
        base = Path(__file__).resolve().parent
        self.ruta_csv = Path(ruta_csv) if ruta_csv else base / "datos" / "glosario_datos.csv"
        self.terminos = self._cargar_glosario()

    def _cargar_glosario(self) -> List[Dict[str, str]]:
        if not self.ruta_csv.exists():
            raise FileNotFoundError(f"No se encontró el CSV en: {self.ruta_csv}")

        with self.ruta_csv.open("r", encoding="utf-8", newline="") as archivo:
            lector = csv.DictReader(archivo)
            if not lector.fieldnames or any(campo not in lector.fieldnames for campo in self.CAMPOS_REQUERIDOS):
                raise ValueError("El CSV no tiene los encabezados esperados del glosario.")
            return [fila for fila in lector]

    def buscar_término(self, nombre: str) -> Dict[str, str] | None:
        objetivo = nombre.strip().lower()
        for fila in self.terminos:
            if fila["término"].strip().lower() == objetivo:
                return fila
        return None

    def buscar_palabras_clave(self, consulta: str) -> List[Dict[str, str]]:
        terminos = [p.strip().lower() for p in consulta.split() if p.strip()]
        resultados: List[Dict[str, str]] = []
        for fila in self.terminos:
            corpus = f"{fila['palabras_clave']} {fila['definición']} {fila['término']}".lower()
            if all(palabra in corpus for palabra in terminos):
                resultados.append(fila)
        return resultados

    def listar_por_categoría(self, categoria: str) -> List[Dict[str, str]]:
        objetivo = categoria.strip().lower()
        return [fila for fila in self.terminos if fila["categoría"].strip().lower() == objetivo]

    def termino_aleatorio(self) -> Dict[str, str]:
        if not self.terminos:
            raise ValueError("El glosario está vacío.")
        return random.choice(self.terminos)

    def similares(self, termino: str, limite: int = 5) -> List[Dict[str, str]]:
        base = self.buscar_término(termino)
        if not base:
            return []

        base_keywords = {p.strip().lower() for p in base["palabras_clave"].split(";") if p.strip()}
        candidatos = [fila for fila in self.terminos if fila["término"] != base["término"]]

        def puntaje(fila: Dict[str, str]) -> tuple[int, int]:
            fila_kw = {p.strip().lower() for p in fila["palabras_clave"].split(";") if p.strip()}
            comun = len(base_keywords & fila_kw)
            misma_categoria = int(fila["categoría"] == base["categoría"])
            return (comun, misma_categoria)

        ordenados = sorted(candidatos, key=puntaje, reverse=True)
        return [fila for fila in ordenados if puntaje(fila) != (0, 0)][:limite]

    def estadisticas(self) -> Dict[str, object]:
        categorias: Dict[str, int] = {}
        modulos: Dict[str, int] = {}

        for fila in self.terminos:
            categorias[fila["categoría"]] = categorias.get(fila["categoría"], 0) + 1
            modulos[fila["módulo_relacionado"]] = modulos.get(fila["módulo_relacionado"], 0) + 1

        return {
            "total_terminos": len(self.terminos),
            "categorias": categorias,
            "modulos": modulos,
        }

    def exportar_busqueda(self, consulta: str, resultados: List[Dict[str, str]], ruta_salida: str | Path | None = None) -> Path:
        if ruta_salida:
            destino = Path(ruta_salida)
        else:
            marca = datetime.now().strftime("%Y%m%d_%H%M%S")
            destino = Path(__file__).resolve().parent / f"busqueda_glosario_{marca}.txt"

        lineas = [f"Consulta: {consulta}", f"Resultados: {len(resultados)}", ""]
        for fila in resultados:
            lineas.append(f"- {fila['término']} ({fila['categoría']})")
            lineas.append(f"  Definición: {fila['definición']}")
            lineas.append(f"  Módulo: {fila['módulo_relacionado']}")

        destino.write_text("\n".join(lineas), encoding="utf-8")
        return destino

    def mostrar_termino(self, fila: Dict[str, str]) -> None:
        print("\n" + "=" * 72)
        print(f"📘 {fila['término']}  |  {fila['categoría']}")
        print("-" * 72)
        print(f"Definición: {fila['definición']}")
        print(f"Contexto: {fila['contexto']}")
        print(f"Ejemplo: {fila['ejemplo']}")
        print(f"Módulo relacionado: {fila['módulo_relacionado']}")
        print(f"Palabras clave: {fila['palabras_clave']}")
        print("=" * 72)

    def menu(self) -> None:
        while True:
            print("\n=== Glosario Interactivo AML-ACADEMY-fintech ===")
            print("1) Buscar término exacto")
            print("2) Buscar por palabras clave")
            print("3) Listar por categoría")
            print("4) Mostrar término aleatorio")
            print("5) Ver términos similares")
            print("6) Ver estadísticas")
            print("7) Salir")

            opcion = input("Selecciona una opción (1-7): ").strip()

            try:
                if opcion == "1":
                    nombre = input("Ingresa el término: ")
                    resultado = self.buscar_término(nombre)
                    if resultado:
                        self.mostrar_termino(resultado)
                    else:
                        print("No se encontró el término.")

                elif opcion == "2":
                    consulta = input("Ingresa palabras clave: ")
                    resultados = self.buscar_palabras_clave(consulta)
                    if not resultados:
                        print("No hubo coincidencias.")
                        continue
                    for fila in resultados[:10]:
                        self.mostrar_termino(fila)
                    exportar = input("¿Deseas exportar resultados? (s/n): ").strip().lower()
                    if exportar == "s":
                        ruta = self.exportar_busqueda(consulta, resultados)
                        print(f"Resultados exportados en: {ruta}")

                elif opcion == "3":
                    categoria = input("Ingresa la categoría exacta: ")
                    resultados = self.listar_por_categoría(categoria)
                    if not resultados:
                        print("Categoría sin resultados.")
                        continue
                    for fila in resultados:
                        print(f"- {fila['término']}")

                elif opcion == "4":
                    self.mostrar_termino(self.termino_aleatorio())

                elif opcion == "5":
                    base = input("Ingresa un término base: ")
                    relacionados = self.similares(base)
                    if not relacionados:
                        print("No se encontraron términos similares.")
                        continue
                    for fila in relacionados:
                        print(f"- {fila['término']} ({fila['categoría']})")

                elif opcion == "6":
                    stats = self.estadisticas()
                    print(f"\nTotal de términos: {stats['total_terminos']}")
                    print("Términos por categoría:")
                    for categoria, total in stats["categorias"].items():
                        print(f"- {categoria}: {total}")

                elif opcion == "7":
                    print("¡Gracias por aprender con el glosario! 👋")
                    break

                else:
                    print("Opción inválida, intenta nuevamente.")

            except Exception as error:  # pragma: no cover (flujo interactivo)
                print(f"Error: {error}")


# Alias con acento solicitado en el requerimiento
GlosarioInteractivo.buscar_término = GlosarioInteractivo.buscar_término
GlosarioInteractivo.listar_por_categoría = GlosarioInteractivo.listar_por_categoría
GlosarioInteractivo.término_aleatorio = GlosarioInteractivo.termino_aleatorio


if __name__ == "__main__":
    glosario = GlosarioInteractivo()
    print("Glosario cargado correctamente. ¡Comencemos a aprender!\n")
    glosario.menu()
