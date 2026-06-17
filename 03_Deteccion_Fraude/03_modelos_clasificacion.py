"""Módulo 03: clasificación de fraude con Logistic Regression."""

from pathlib import Path
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


def cargar_datos() -> pd.DataFrame:
    """Carga dataset de fraude para entrenamiento."""
    ruta = Path(__file__).resolve().parent / "datos" / "fraude_ejemplo.csv"
    return pd.read_csv(ruta)


def entrenar_modelo(df: pd.DataFrame):
    """Entrena un modelo de regresión logística con features seleccionadas."""
    features = ["amount", "velocity", "location_change", "hour_transaction", "previous_amounts"]
    X = df[features]
    y = df["is_fraud"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    modelo = LogisticRegression(max_iter=1000)
    modelo.fit(X_train, y_train)
    pred = modelo.predict(X_test)
    proba = modelo.predict_proba(X_test)[:, 1]
    resultado = pd.DataFrame({"prediccion": pred, "probabilidad_fraude": proba, "real": y_test.values})
    return modelo, resultado


if __name__ == "__main__":
    try:
        datos = cargar_datos()
        _, predicciones = entrenar_modelo(datos)
        print("\nPredicciones de ejemplo:\n", predicciones.head(10))
    except Exception as error:
        print(f"Error en 03_modelos_clasificacion.py: {error}")
