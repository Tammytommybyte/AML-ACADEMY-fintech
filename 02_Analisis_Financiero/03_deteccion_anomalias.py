"""Módulo 02: detección de anomalías con métodos estadísticos."""

from pathlib import Path
import numpy as np
import pandas as pd


def cargar_transacciones() -> pd.DataFrame:
    """Carga transacciones para análisis de anomalías."""
    ruta = Path(__file__).resolve().parent / "datos" / "transacciones_ejemplo.csv"
    return pd.read_csv(ruta)


def detectar_anomalias(df: pd.DataFrame) -> pd.DataFrame:
    """Marca anomalías usando Z-score, IQR y desviación de media."""
    salida = df.copy()
    media = salida["amount"].mean()
    desv = salida["amount"].std(ddof=0)
    salida["z_score"] = (salida["amount"] - media) / desv
    q1, q3 = salida["amount"].quantile([0.25, 0.75])
    iqr = q3 - q1
    salida["anomalia_z"] = np.abs(salida["z_score"]) > 3
    salida["anomalia_iqr"] = (salida["amount"] < q1 - 1.5 * iqr) | (salida["amount"] > q3 + 1.5 * iqr)
    salida["anomalia_media"] = np.abs(salida["amount"] - media) > 2 * desv
    salida["alerta"] = salida[["anomalia_z", "anomalia_iqr", "anomalia_media"]].any(axis=1)
    return salida


if __name__ == "__main__":
    try:
        datos = cargar_transacciones()
        alertas = detectar_anomalias(datos)
        print("Total alertas:", int(alertas["alerta"].sum()))
        print("\nCasos anómalos:\n", alertas[alertas["alerta"]].head(10)[["transaction_id", "customer_id", "amount", "alerta"]])
    except Exception as error:
        print(f"Error en 03_deteccion_anomalias.py: {error}")
