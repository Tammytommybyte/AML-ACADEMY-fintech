"""Módulo 04: reportes regulatorios de compliance."""

from pathlib import Path
import pandas as pd


def cargar_fuentes() -> tuple[pd.DataFrame, pd.DataFrame]:
    """Carga transacciones y clientes para reporte consolidado."""
    base = Path(__file__).resolve().parents[1]
    trans = pd.read_csv(base / "02_Analisis_Financiero" / "datos" / "transacciones_ejemplo.csv")
    clientes = pd.read_csv(Path(__file__).resolve().parent / "datos" / "clientes_kyc.csv")
    return trans, clientes


def generar_reporte(trans: pd.DataFrame, clientes: pd.DataFrame) -> dict:
    """Resume actividad, alertas y estado de investigaciones."""
    merged = trans.merge(clientes[["customer_id", "risk_level"]], on="customer_id", how="left")
    resumen = {
        "total_transacciones": int(len(merged)),
        "monto_total": float(round(merged["amount"].sum(), 2)),
        "clientes_high_risk": int((merged["risk_level"] == "High").sum()),
        "alertas_monto_alto": int((merged["amount"] > 9000).sum()),
    }
    return resumen


if __name__ == "__main__":
    try:
        transacciones, clientes = cargar_fuentes()
        reporte = generar_reporte(transacciones, clientes)
        print("\nDashboard compliance:")
        for clave, valor in reporte.items():
            print(f"- {clave}: {valor}")
    except Exception as error:
        print(f"Error en 04_reportes_compliance.py: {error}")
