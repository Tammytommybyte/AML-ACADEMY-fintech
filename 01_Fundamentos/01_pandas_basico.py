"""Módulo 01: Introducción a Pandas para datos financieros."""

from pathlib import Path
import pandas as pd


def crear_dataframe_desde_diccionario() -> pd.DataFrame:
    """Crea un DataFrame financiero básico desde un diccionario."""
    data = {
        "cliente": ["C001", "C002", "C003", "C004", "C005"],
        "saldo": [1500.0, 3200.5, 980.2, 4400.8, 2100.0],
        "pais": ["MX", "CO", "AR", "MX", "PE"],
    }
    df = pd.DataFrame(data)
    print("\nDataFrame desde diccionario:\n", df)
    return df


def cargar_csv_basico() -> pd.DataFrame:
    """Carga el dataset básico del módulo desde CSV."""
    ruta = Path(__file__).resolve().parent / "datos" / "datos_basicos.csv"
    df = pd.read_csv(ruta)
    print(f"\nCSV cargado con {len(df)} registros desde: {ruta}")
    return df


def operaciones_basicas(df: pd.DataFrame) -> None:
    """Muestra operaciones básicas de inspección en Pandas."""
    print("\nHead:\n", df.head())
    print("\nTail:\n", df.tail())
    print("\nShape:", df.shape)
    print("\nInfo:")
    print(df.info())


def seleccionar_y_filtrar(df: pd.DataFrame) -> None:
    """Demuestra selección de columnas/filas y filtros simples."""
    print("\nColumnas cliente y amount:\n", df[["customer_id", "amount"]].head())
    print("\nFilas con amount > 3000:\n", df[df["amount"] > 3000].head())


def agregaciones(df: pd.DataFrame) -> None:
    """Ejecuta agregaciones y groupby para análisis financiero rápido."""
    resumen = df.groupby("country")["amount"].agg(["count", "mean", "sum"]).round(2)
    print("\nAgregaciones por país:\n", resumen)


if __name__ == "__main__":
    try:
        crear_dataframe_desde_diccionario()
        datos = cargar_csv_basico()
        operaciones_basicas(datos)
        seleccionar_y_filtrar(datos)
        agregaciones(datos)
        # Ejercicio 1: filtra solo transacciones aprobadas.
        # Ejercicio 2: calcula monto promedio por tipo de transacción.
    except Exception as error:
        print(f"Error en 01_pandas_basico.py: {error}")
