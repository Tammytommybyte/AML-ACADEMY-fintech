"""Módulo 04: generación de SAR para actividad sospechosa."""

from pathlib import Path
import pandas as pd


def cargar_transacciones() -> pd.DataFrame:
    """Carga transacciones para análisis SAR."""
    ruta = Path(__file__).resolve().parents[1] / "02_Analisis_Financiero" / "datos" / "transacciones_ejemplo.csv"
    return pd.read_csv(ruta)


def detectar_sospechas(df: pd.DataFrame) -> pd.DataFrame:
    """Marca transacciones inusuales y patrones raros para SAR."""
    salida = df.copy()
    umbral_alto = salida["amount"].quantile(0.98)
    salida["monto_inusual"] = salida["amount"] >= umbral_alto
    salida["pais_riesgo"] = salida["country"].isin(["NG", "RU", "IR"])
    salida["sar_flag"] = salida[["monto_inusual", "pais_riesgo"]].any(axis=1)
    return salida


def generar_sar(df: pd.DataFrame) -> pd.DataFrame:
    """Genera un resumen SAR para escalamiento a compliance."""
    sospechosas = df[df["sar_flag"]].copy()
    sospechosas["comentario"] = "Escalar a equipo de compliance"
    return sospechosas[["transaction_id", "customer_id", "amount", "country", "sar_flag", "comentario"]]


if __name__ == "__main__":
    try:
        datos = cargar_transacciones()
        analizadas = detectar_sospechas(datos)
        sar = generar_sar(analizadas)
        print("\nReportes SAR sugeridos:", len(sar))
        print(sar.head(10))
    except Exception as error:
        print(f"Error en 03_sar_actividades_sospechosas.py: {error}")
