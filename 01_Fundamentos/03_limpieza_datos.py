"""Módulo 01: Limpieza y validación de datos."""

from pathlib import Path
import numpy as np
import pandas as pd


def cargar_datos() -> pd.DataFrame:
    """Carga datos para limpieza."""
    ruta = Path(__file__).resolve().parent / "datos" / "datos_basicos.csv"
    return pd.read_csv(ruta)


def detectar_valores_faltantes(df: pd.DataFrame) -> None:
    """Muestra conteo de valores faltantes por columna."""
    print("\nValores faltantes:\n", df.isna().sum())


def imputar_y_deduplicar(df: pd.DataFrame) -> pd.DataFrame:
    """Imputa faltantes y elimina duplicados."""
    limpio = df.copy()
    limpio["status"] = limpio["status"].fillna("pending")
    limpio["amount"] = limpio["amount"].fillna(limpio["amount"].median())
    limpio = limpio.drop_duplicates()
    return limpio


def detectar_outliers(df: pd.DataFrame) -> pd.DataFrame:
    """Detecta outliers usando Z-score e IQR."""
    salida = df.copy()
    z_score = (salida["amount"] - salida["amount"].mean()) / salida["amount"].std(ddof=0)
    q1, q3 = salida["amount"].quantile([0.25, 0.75])
    iqr = q3 - q1
    salida["outlier_zscore"] = np.abs(z_score) > 3
    salida["outlier_iqr"] = (salida["amount"] < q1 - 1.5 * iqr) | (salida["amount"] > q3 + 1.5 * iqr)
    return salida


def normalizar(df: pd.DataFrame) -> pd.DataFrame:
    """Normaliza el monto al rango [0, 1]."""
    norm = df.copy()
    minimo, maximo = norm["amount"].min(), norm["amount"].max()
    norm["amount_normalized"] = (norm["amount"] - minimo) / (maximo - minimo)
    return norm


if __name__ == "__main__":
    try:
        datos = cargar_datos()
        detectar_valores_faltantes(datos)
        limpios = imputar_y_deduplicar(datos)
        con_outliers = detectar_outliers(limpios)
        final = normalizar(con_outliers)
        print("\nRegistros limpios:", len(final))
        print("Outliers detectados (Z-score):", int(final["outlier_zscore"].sum()))
        print("Outliers detectados (IQR):", int(final["outlier_iqr"].sum()))
    except Exception as error:
        print(f"Error en 03_limpieza_datos.py: {error}")
