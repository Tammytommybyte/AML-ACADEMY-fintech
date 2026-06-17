"""Módulo 03: análisis de comportamiento transaccional."""

from pathlib import Path
import pandas as pd


def cargar_datos() -> pd.DataFrame:
    """Carga datos de fraude para análisis comportamental."""
    ruta = Path(__file__).resolve().parent / "datos" / "fraude_ejemplo.csv"
    return pd.read_csv(ruta)


def matriz_comportamiento(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula desviación entre monto actual y promedio histórico."""
    salida = df.copy()
    salida["desviacion_monto"] = (salida["amount"] - salida["previous_amounts"]).abs()
    salida["cambio_patron"] = salida["desviacion_monto"] > salida["previous_amounts"] * 1.5
    salida["alerta_comportamiento"] = salida[["cambio_patron"]].any(axis=1)
    return salida


if __name__ == "__main__":
    try:
        datos = cargar_datos()
        matriz = matriz_comportamiento(datos)
        print("\nAlertas comportamentales:", int(matriz["alerta_comportamiento"].sum()))
        print(matriz[["amount", "previous_amounts", "desviacion_monto", "cambio_patron"]].head(10))
    except Exception as error:
        print(f"Error en 02_analisis_comportamiento.py: {error}")
