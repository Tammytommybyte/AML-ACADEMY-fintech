"""Módulo 03: evaluación de rendimiento del modelo de fraude."""

from pathlib import Path
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
    roc_curve,
)
from sklearn.model_selection import train_test_split


def cargar_datos() -> pd.DataFrame:
    """Carga dataset para evaluación."""
    ruta = Path(__file__).resolve().parent / "datos" / "fraude_ejemplo.csv"
    return pd.read_csv(ruta)


def evaluar(df: pd.DataFrame, threshold: float = 0.5) -> dict:
    """Calcula métricas: matriz, precisión, recall, F1, ROC AUC."""
    X = df[["amount", "velocity", "location_change", "hour_transaction", "previous_amounts"]]
    y = df["is_fraud"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    modelo = LogisticRegression(max_iter=1000)
    modelo.fit(X_train, y_train)
    y_prob = modelo.predict_proba(X_test)[:, 1]
    y_pred = (y_prob >= threshold).astype(int)
    tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
    _fpr, _tpr, _thr = roc_curve(y_test, y_prob)
    return {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred, zero_division=0),
        "recall": recall_score(y_test, y_pred, zero_division=0),
        "f1": f1_score(y_test, y_pred, zero_division=0),
        "specificity": tn / (tn + fp) if (tn + fp) else 0.0,
        "sensitivity": tp / (tp + fn) if (tp + fn) else 0.0,
        "roc_auc": roc_auc_score(y_test, y_prob),
    }


if __name__ == "__main__":
    try:
        datos = cargar_datos()
        for thr in [0.4, 0.5, 0.6]:
            metricas = evaluar(datos, threshold=thr)
            print(f"\nMétricas con threshold={thr}:\n", {k: round(v, 3) for k, v in metricas.items()})
    except Exception as error:
        print(f"Error en 04_metricas_rendimiento.py: {error}")
