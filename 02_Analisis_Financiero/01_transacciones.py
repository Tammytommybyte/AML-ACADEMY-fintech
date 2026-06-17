"""Módulo 02: análisis de transacciones financieras."""

from pathlib import Path
import pandas as pd


def cargar_transacciones() -> pd.DataFrame:
    """Carga transacciones del dataset del módulo."""
    ruta = Path(__file__).resolve().parent / "datos" / "transacciones_ejemplo.csv"
    return pd.read_csv(ruta, parse_dates=["date"])


def analizar(df: pd.DataFrame) -> None:
    """Ejecuta métricas por cliente/tipo y tendencias."""
    print("\nEstadísticas generales:\n", df["amount"].describe())
    print("\nTop 5 clientes por volumen:\n", df.groupby("customer_id")["amount"].sum().nlargest(5).round(2))
    print("\nTransacciones más grandes:\n", df.nlargest(5, "amount")[["transaction_id", "customer_id", "amount", "country"]])
    tendencias = df.set_index("date").resample("M")["amount"].sum()
    print("\nTendencia mensual (suma):\n", tendencias)


if __name__ == "__main__":
    try:
        datos = cargar_transacciones()
        print("Total de transacciones:", len(datos))
        analizar(datos)
    except Exception as error:
        print(f"Error en 01_transacciones.py: {error}")
