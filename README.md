# AML ACADEMY Fintech

**Repositorio educativo completo para aprender Python aplicado a análisis financiero, detección de fraude, AML (Anti-Lavado de Dinero) y compliance.**

## 📚 Objetivo del Proyecto

Este repositorio proporciona una estructura modular, progresiva y práctica para aprender análisis de datos aplicado a finanzas y cumplimiento normativo. Es ideal para:

- Estudiantes de data science y finanzas
- Profesionales del sector financiero
- Analistas de compliance y AML
- Personas interesadas en seguridad financiera

## 🎓 Módulos de Aprendizaje

### 1️⃣ **Fundamentos Python para Análisis de Datos** (`01_Fundamentos/`)
- Introducción a Pandas y manipulación de datos
- Análisis Exploratorio de Datos (EDA)
- Limpieza y preparación de datos

### 2️⃣ **Análisis Financiero Básico** (`02_Analisis_Financiero/`)
- Análisis de transacciones
- Cálculo de métricas financieras
- Detección de anomalías estadísticas

### 3️⃣ **Detección de Fraude** (`03_Deteccion_Fraude/`)
- Reglas heurísticas de detección
- Análisis de comportamiento del cliente
- Modelos de clasificación (Machine Learning)
- Evaluación de modelos (precisión, recall, F1-score)

### 4️⃣ **AML y Compliance** (`04_AML_Compliance/`)
- Screening contra watchlists
- Procesos KYC (Know Your Customer)
- Identificación de actividades sospechosas (SAR)
- Generación de reportes de compliance

### 5️⃣ **Proyectos Integradores** (`05_Proyectos_Integradores/`)
- Pipeline end-to-end de detección de fraude
- Caso de estudio completo de AML
- Análisis integral de riesgo del cliente

## 🚀 Instalación

### Requisitos Previos
- Python 3.8 o superior
- pip instalado

### Pasos

1. **Clonar el repositorio:**
```bash
git clone https://github.com/Tammytommybyte/AML-ACADEMY-fintech.git
cd AML-ACADEMY-fintech
```

2. **Crear un entorno virtual (opcional pero recomendado):**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

## 📋 Estructura del Repositorio

```
AML-ACADEMY-fintech/
├── README.md
├── requirements.txt
├── .gitignore
│
├── 01_Fundamentos/
│   ├── 01_pandas_basico.py
│   ├── 02_eda_exploratorio.py
│   ├── 03_limpieza_datos.py
│   └── datos/
│       └── datos_basicos.csv
│
├── 02_Analisis_Financiero/
│   ├── 01_transacciones.py
│   ├── 02_metricas_financieras.py
│   ├── 03_deteccion_anomalias.py
│   └── datos/
│       └── transacciones_ejemplo.csv
│
├── 03_Deteccion_Fraude/
│   ├── 01_reglas_heuristicas.py
│   ├── 02_analisis_comportamiento.py
│   ├── 03_modelos_clasificacion.py
│   ├── 04_metricas_rendimiento.py
│   └── datos/
│       └── fraude_ejemplo.csv
│
├── 04_AML_Compliance/
│   ├── 01_screening_watchlist.py
│   ├── 02_kyc_due_diligence.py
│   ├── 03_sar_actividades_sospechosas.py
│   ├── 04_reportes_compliance.py
│   ├── datos/
│   │   ├── watchlist_ejemplo.csv
│   │   └── clientes_kyc.csv
│   └── templates/
│       └── reporte_sar_template.txt
│
└── 05_Proyectos_Integradores/
    ├── 01_pipeline_fraude_completo.py
    ├── 02_caso_estudio_aml.py
    ├── 03_analisis_riesgo_cliente.py
    └── datos/
        └── dataset_completo.csv
```

## 💻 Cómo Usar este Repositorio

### Opción 1: Ejecutar Scripts Directamente
```bash
# Ejemplo: ejecutar el script de pandas básico
python 01_Fundamentos/01_pandas_basico.py
```

### Opción 2: Usar Jupyter Notebooks (próximamente)
```bash
jupyter notebook
```

### Opción 3: Explorar el Código
- Lee cada archivo `.py` con comentarios explicativos
- Estudia los datos en `datos/` para entender las estructuras
- Ejecuta y modifica los ejemplos para experimentar

## 📊 Progresión de Aprendizaje

**Recomendado seguir este orden:**

1. **Semana 1:** Módulo 01 (Fundamentos)
2. **Semana 2:** Módulo 02 (Análisis Financiero)
3. **Semana 3-4:** Módulo 03 (Detección de Fraude)
4. **Semana 5:** Módulo 04 (AML y Compliance)
5. **Semana 6+:** Módulo 05 (Proyectos Integradores)

## 🔑 Conceptos Clave Cubiertos

### Python y Pandas
- DataFrames y Series
- Filtrado y agregación
- Manejo de valores faltantes
- Merge y join de datos

### Análisis de Datos
- Estadística descriptiva
- Detección de anomalías
- Visualización con Matplotlib y Seaborn

### Machine Learning
- Ingeniería de características
- Clasificación (Logistic Regression)
- Evaluación de modelos
- Matriz de confusión, Precisión, Recall, F1-score

### Finanzas y Compliance
- Análisis de transacciones
- Detección de fraude
- AML (Anti-Lavado de Dinero)
- KYC (Know Your Customer)
- Compliance y regulaciones

## 📚 Recursos Adicionales

- [Documentación Pandas](https://pandas.pydata.org/docs/)
- [Scikit-learn Docs](https://scikit-learn.org/)
- [Matplotlib Tutorial](https://matplotlib.org/stable/tutorials/index.html)
- [Guía de AML/KYC](https://www.fatf-gafi.org/) (FATF - Financial Action Task Force)

## ⚠️ Nota Importante

**Todos los datos utilizados en este repositorio son simulados y ficticios.** No contienen información real de clientes, transacciones o personas. Están diseñados únicamente con fines educativos.

## 🤝 Contribuciones

Si deseas mejorar este repositorio:
- Fork el proyecto
- Crea una rama para tu feature
- Envía un Pull Request

## 📝 Licencia

Este proyecto está disponible para uso educativo.

## 👤 Autor

**Creado por:** Tammytommybyte  
**Fecha:** 2026

---

**¡Comienza tu viaje en análisis de datos financieros hoy!** 🚀
