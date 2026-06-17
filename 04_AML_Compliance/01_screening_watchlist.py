"""Módulo 04: screening AML contra watchlists."""

from pathlib import Path
from difflib import SequenceMatcher
import pandas as pd


def cargar_datos():
    """Carga watchlist y clientes KYC para screening."""
    base = Path(__file__).resolve().parent
    watchlist = pd.read_csv(base / "datos" / "watchlist_ejemplo.csv")
    clientes = pd.read_csv(base / "datos" / "clientes_kyc.csv")
    return watchlist, clientes


def fuzzy_ratio(a: str, b: str) -> float:
    """Calcula similitud básica entre dos nombres."""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def screening(watchlist: pd.DataFrame, clientes: pd.DataFrame) -> pd.DataFrame:
    """Aplica exact match y fuzzy match para detectar coincidencias."""
    resultados = []
    for _, cliente in clientes.iterrows():
        for _, alerta in watchlist.iterrows():
            similitud = fuzzy_ratio(cliente["name"], alerta["name"])
            exacto = cliente["name"].lower() == alerta["name"].lower()
            if exacto or similitud >= 0.85:
                resultados.append(
                    {
                        "customer_id": cliente["customer_id"],
                        "cliente": cliente["name"],
                        "watch_name": alerta["name"],
                        "match_exacto": exacto,
                        "score_similitud": round(similitud, 2),
                        "accion": "Bloquear transacción",
                    }
                )
    return pd.DataFrame(resultados)


if __name__ == "__main__":
    try:
        watch, clientes = cargar_datos()
        matches = screening(watch, clientes)
        print("\nMatches detectados:", len(matches))
        print(matches.head(10))
    except Exception as error:
        print(f"Error en 01_screening_watchlist.py: {error}")
