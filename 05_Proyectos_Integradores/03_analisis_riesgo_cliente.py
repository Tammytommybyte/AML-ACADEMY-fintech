"""Módulo 05: scoring integral de riesgo cliente."""

from pathlib import Path
import pandas as pd


def cargar_dataset() -> pd.DataFrame:
    """Carga dataset consolidado para scoring."""
    ruta = Path(__file__).resolve().parent / "datos" / "dataset_completo.csv"
    return pd.read_csv(ruta)


def calcular_riesgo(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula score de riesgo y acciones recomendadas."""
    salida = df.copy()
    salida["riesgo_score"] = (
        (salida["amount"] > 8000).astype(int) * 2
        + (salida["velocity"] > 5).astype(int)
        + (salida["location_change"] == 1).astype(int)
        + (salida["is_fraud"] == 1).astype(int) * 3
    )
    salida["categoria"] = pd.cut(salida["riesgo_score"], bins=[-1, 2, 4, 10], labels=["Low", "Medium", "High"])
    salida["accion_recomendada"] = salida["categoria"].map(
        {"Low": "Monitoreo estándar", "Medium": "Revisión manual", "High": "Escalar a compliance"}
    )
    return salida


if __name__ == "__main__":
    try:
        datos = cargar_dataset()
        riesgos = calcular_riesgo(datos)
        print("\nMatriz de riesgo (top 10):\n", riesgos[["transaction_id", "riesgo_score", "categoria", "accion_recomendada"]].head(10))
    except Exception as error:
        print(f"Error en 03_analisis_riesgo_cliente.py: {error}")
