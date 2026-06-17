"""Módulo 05: caso de estudio AML de extremo a extremo."""

from pathlib import Path
import pandas as pd


def cargar_datasets() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Carga datasets de transacciones, clientes y watchlist."""
    raiz = Path(__file__).resolve().parents[1]
    trans = pd.read_csv(raiz / "02_Analisis_Financiero" / "datos" / "transacciones_ejemplo.csv")
    clientes = pd.read_csv(raiz / "04_AML_Compliance" / "datos" / "clientes_kyc.csv")
    watch = pd.read_csv(raiz / "04_AML_Compliance" / "datos" / "watchlist_ejemplo.csv")
    return trans, clientes, watch


def ejecutar_caso(trans: pd.DataFrame, clientes: pd.DataFrame, watch: pd.DataFrame) -> dict:
    """Resume screening, KYC y potenciales casos SAR."""
    screening_hits = clientes["name"].str.lower().isin(watch["name"].str.lower()).sum()
    pendientes_kyc = (clientes["kyc_status"] != "Completed").sum()
    sar = ((trans["amount"] > trans["amount"].quantile(0.98)) | trans["country"].isin(["NG", "RU", "IR"]))
    return {
        "screening_hits": int(screening_hits),
        "pendientes_kyc": int(pendientes_kyc),
        "casos_sar": int(sar.sum()),
    }


if __name__ == "__main__":
    try:
        transacciones, clientes, watchlist = cargar_datasets()
        resumen = ejecutar_caso(transacciones, clientes, watchlist)
        print("\nReporte final AML:", resumen)
    except Exception as error:
        print(f"Error en 02_caso_estudio_aml.py: {error}")
