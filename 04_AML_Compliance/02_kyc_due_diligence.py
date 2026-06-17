"""Módulo 04: proceso KYC y due diligence básico."""

from pathlib import Path
import pandas as pd


def cargar_clientes() -> pd.DataFrame:
    """Carga clientes KYC del módulo AML."""
    ruta = Path(__file__).resolve().parent / "datos" / "clientes_kyc.csv"
    return pd.read_csv(ruta)


def evaluar_kyc(df: pd.DataFrame) -> pd.DataFrame:
    """Asigna estado de revisión según riesgo y documentos."""
    salida = df.copy()
    salida["riesgo_recomendado"] = salida["risk_level"].map({"Low": "Anual", "Medium": "Semestral", "High": "Trimestral"})
    salida["du_diligence"] = salida.apply(
        lambda r: "Aprobado" if r["documents_verified"] == 1 and r["kyc_status"] == "Completed" else "Pendiente",
        axis=1,
    )
    return salida


if __name__ == "__main__":
    try:
        clientes = cargar_clientes()
        evaluados = evaluar_kyc(clientes)
        print("\nEstado KYC:\n", evaluados[["customer_id", "risk_level", "kyc_status", "du_diligence", "riesgo_recomendado"]].head(10))
    except Exception as error:
        print(f"Error en 02_kyc_due_diligence.py: {error}")
