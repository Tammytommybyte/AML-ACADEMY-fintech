"""Módulo 01: EDA exploratorio con datos financieros."""

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def cargar_datos() -> pd.DataFrame:
    """Carga datos del módulo para EDA."""
    ruta = Path(__file__).resolve().parent / "datos" / "datos_basicos.csv"
    return pd.read_csv(ruta)


def estadisticas_descriptivas(df: pd.DataFrame) -> None:
    """Imprime estadísticas descriptivas y cuantiles."""
    print("\nDescribe amount:\n", df["amount"].describe())
    print("\nCuantiles amount:\n", df["amount"].quantile([0.25, 0.5, 0.75, 0.95]))


def correlaciones(df: pd.DataFrame) -> None:
    """Calcula correlaciones entre columnas numéricas."""
    numericas = df.select_dtypes(include="number")
    print("\nCorrelaciones:\n", numericas.corr().round(2))


def visualizar(df: pd.DataFrame) -> None:
    """Genera histogramas y boxplots educativos."""
    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    sns.histplot(df["amount"], bins=20, kde=True, ax=axes[0])
    axes[0].set_title("Distribución de montos")
    sns.boxplot(data=df, x="type", y="amount", ax=axes[1])
    axes[1].set_title("Montos por tipo")
    fig.tight_layout()
    plt.close(fig)
    print("\nVisualizaciones generadas correctamente (histograma y boxplot).")


if __name__ == "__main__":
    try:
        datos = cargar_datos()
        estadisticas_descriptivas(datos)
        correlaciones(datos)
        visualizar(datos)
        print("\nResumen: se observan diferencias de montos por tipo y cola alta en la distribución.")
    except Exception as error:
        print(f"Error en 02_eda_exploratorio.py: {error}")
