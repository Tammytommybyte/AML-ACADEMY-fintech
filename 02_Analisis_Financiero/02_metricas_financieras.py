"""Módulo 02: métricas financieras clave por cliente."""

from pathlib import Path
import pandas as pd


def cargar_transacciones() -> pd.DataFrame:
    """Carga transacciones para métricas financieras."""
    ruta = Path(__file__).resolve().parent / "datos" / "transacciones_ejemplo.csv"
    return pd.read_csv(ruta)


def calcular_metricas(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula saldo promedio, frecuencia y volatilidad por cliente."""
    metricas = df.groupby("customer_id").agg(
        saldo_promedio=("amount", "mean"),
        volumen=("amount", "sum"),
        frecuencia=("transaction_id", "count"),
        volatilidad=("amount", "std"),
    ).fillna(0)
    metricas["riesgo"] = pd.cut(
        metricas["volatilidad"],
        bins=[-1, 800, 1600, float("inf")],
        labels=["Low", "Medium", "High"],
    )
    return metricas.sort_values("volumen", ascending=False)


if __name__ == "__main__":
    try:
        datos = cargar_transacciones()
        resultado = calcular_metricas(datos)
        print("\nMétricas financieras por cliente:\n", resultado.head(10).round(2))
    except Exception as error:
        print(f"Error en 02_metricas_financieras.py: {error}")
