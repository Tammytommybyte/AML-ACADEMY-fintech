"""Módulo 03: reglas heurísticas para detección de fraude."""

from pathlib import Path
import pandas as pd


def cargar_datos() -> pd.DataFrame:
    """Carga dataset de fraude para reglas."""
    ruta = Path(__file__).resolve().parent / "datos" / "fraude_ejemplo.csv"
    return pd.read_csv(ruta)


def aplicar_reglas(df: pd.DataFrame) -> pd.DataFrame:
    """Aplica reglas de monto, velocidad, ubicación y horario."""
    salida = df.copy()
    salida["regla_monto"] = salida["amount"] > 9000
    salida["regla_velocidad"] = salida["velocity"] >= 6
    salida["regla_ubicacion"] = salida["location_change"] == 1
    salida["regla_horario"] = salida["hour_transaction"].isin([0, 1, 2, 3, 4])
    reglas = ["regla_monto", "regla_velocidad", "regla_ubicacion", "regla_horario"]
    salida["score_reglas"] = salida[reglas].sum(axis=1)
    salida["alerta_heuristica"] = salida["score_reglas"] >= 2
    return salida


if __name__ == "__main__":
    try:
        datos = cargar_datos()
        alertas = aplicar_reglas(datos)
        print("\nAlertas heurísticas:", int(alertas["alerta_heuristica"].sum()))
        print(alertas[alertas["alerta_heuristica"]].head(10)[["transaction_id", "score_reglas", "alerta_heuristica"]])
    except Exception as error:
        print(f"Error en 01_reglas_heuristicas.py: {error}")
