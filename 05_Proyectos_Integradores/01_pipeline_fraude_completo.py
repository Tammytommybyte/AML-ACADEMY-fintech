"""Módulo 05: pipeline end-to-end para detección de fraude."""

from pathlib import Path
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score


def cargar_dataset() -> pd.DataFrame:
    """Carga dataset integrado del módulo de proyectos."""
    ruta = Path(__file__).resolve().parent / "datos" / "dataset_completo.csv"
    return pd.read_csv(ruta)


def ejecutar_pipeline(df: pd.DataFrame) -> dict:
    """Ejecuta limpieza, reglas heurísticas, modelo y evaluación final."""
    base = df.dropna().copy()
    base["regla_monto"] = (base["amount"] > 9000).astype(int)
    base["score_reglas"] = base[["regla_monto", "velocity", "location_change"]].apply(
        lambda r: int(r.iloc[0]) + int(r.iloc[1] >= 6) + int(r.iloc[2] == 1), axis=1
    )
    X = base[["amount", "velocity", "location_change", "hour_transaction", "previous_amounts", "score_reglas"]]
    y = base["is_fraud"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    modelo = LogisticRegression(max_iter=1000)
    modelo.fit(X_train, y_train)
    pred = modelo.predict(X_test)
    return {"f1_final": round(f1_score(y_test, pred), 3), "muestras_test": len(X_test)}


if __name__ == "__main__":
    try:
        data = cargar_dataset()
        resultado = ejecutar_pipeline(data)
        print("\nResultado pipeline:", resultado)
    except Exception as error:
        print(f"Error en 01_pipeline_fraude_completo.py: {error}")
