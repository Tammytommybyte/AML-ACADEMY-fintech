# Glosario — AML ACADEMY Fintech

Este glosario reúne términos clave usados en el repositorio y en el dominio de AML, fraude y análisis de datos. Definiciones en español e inglés (cuando aplica), concisas y orientadas a estudiantes.

- AML (Anti-Money Laundering / Anti-Lavado de Dinero): Conjunto de políticas, procedimientos y controles destinados a prevenir y detectar el lavado de dinero y financiamiento del terrorismo.
- KYC (Know Your Customer / Conoce a tu Cliente): Proceso para verificar la identidad de clientes, recopilar información y evaluar riesgo antes de establecer una relación comercial.
- SAR (Suspicious Activity Report / Reporte de Actividad Sospechosa): Documento que se remite a autoridades cuando se identifica actividad financiera sospechosa.
- CDD (Customer Due Diligence / Diligencia Debida del Cliente): Evaluación básica del cliente para identificar riesgos, verificar identidad y recopilar información relevante.
- EDD (Enhanced Due Diligence / Diligencia Debida Aumentada): Procedimientos adicionales aplicados a clientes o transacciones de alto riesgo.
- Due Diligence (Diligencia Debida): Proceso general de investigación y verificación de información sobre un cliente, contraparte o transacción para evaluar riesgos legales, financieros o de cumplimiento.
- PEP (Politically Exposed Person / Persona Políticamente Expuesta): Individuo con funciones públicas prominentes que puede implicar mayor riesgo de corrupción u lavado.
- TF (Terrorist Financing / Financiamiento del Terrorismo): Actos de financiamiento que facilitan actividades terroristas; forma parte del foco de AML.
- Watchlist / Lista de vigilancia: Listado de personas, entidades o países sancionados o de riesgo que se usan para screening.
- Screening: Proceso automatizado o manual para comparar clientes/transacciones contra listas de watchlists o sanciones.
- Transacción (Transaction): Movimiento financiero (pago, retiro, transferencia) que se analiza en detección de fraude y monitoreo AML.
- Anomalía / Anomaly: Observación o patrón que difiere significativamente del comportamiento esperado o histórico.
- Detección de anomalías (Anomaly Detection): Técnicas (estadísticas o ML) para identificar eventos atípicos en los datos.
- False positive (Falso positivo): Resultado donde el sistema marca una actividad como sospechosa cuando en realidad es legítima.
- False negative (Falso negativo): Resultado donde el sistema no detecta una actividad sospechosa real.
- Precisión (Precision): En clasificación, proporción de positivos predichos que son realmente positivos (evita falsos positivos).
- Recall (Sensibilidad): Proporción de positivos reales que fueron detectados por el modelo (evita falsos negativos).
- F1-score: Media armónica de precisión y recall; métrica balanceada para evaluar clasificadores.
- ROC AUC: Área bajo la curva ROC; métrica que mide la capacidad de un modelo para distinguir clases.
- Matriz de confusión (Confusion Matrix): Tabla que muestra TP, FP, FN, TN para evaluar rendimiento del clasificador.
- Ingeniería de características (Feature engineering): Proceso de crear variables predictivas relevantes a partir de datos crudos.
- EDA (Exploratory Data Analysis / Análisis Exploratorio): Conjunto de técnicas para entender la estructura, calidad y patrones en los datos.
- Umbral (Threshold): Valor usado para convertir probabilidades del modelo en etiquetas (ej., sospechoso/no sospechoso).
- Scoring / Puntuación de riesgo (Risk Scoring): Valor numérico asignado a clientes/transacciones que refleja el nivel de riesgo.
- Monitoreo de transacciones (Transaction Monitoring): Supervisión continua de transacciones para detectar actividades inusuales.
- Beneficial owner (Propietario beneficiario): Persona física que, en última instancia, posee o controla a un cliente/jurídica.
- Due diligence documental (Documentary due diligence): Verificación de documentos (identidad, prueba de domicilio, etc.) como parte de KYC.
- SAR template / Plantilla de SAR: Formato estándar para documentar y reportar actividades sospechosas.
- Compliance (Cumplimiento): Conjunto de procesos para asegurar que la organización cumple con leyes, regulaciones y políticas internas.
- Geolocalización (Geolocation): Técnica para determinar la ubicación geográfica aproximada de un dispositivo, usuario o transacción, útil para detectar transacciones desde ubicaciones inusuales o de alto riesgo.
- IP reputation (Reputación de IP): Evaluación de si una dirección IP está asociada con actividad maliciosa, fraudulenta o de alto riesgo.
- Device fingerprinting (Huella del dispositivo): Conjunto de atributos técnicos que identifican un dispositivo para detectar fraudes o comportamientos anómalos.
- Time-series analysis (Análisis de series temporales): Técnicas para modelar y detectar patrones en datos ordenados por tiempo — importante para monitoreo de transacciones.
- Feature importance (Importancia de características): Medida de qué variables contribuyen más a las predicciones de un modelo.
- Model drift (Deriva del modelo): Cambio en el rendimiento del modelo a lo largo del tiempo debido a cambios en el comportamiento o los datos.

Entidades regulatorias y de inteligencia financiera (México):
- UIF (Unidad de Inteligencia Financiera) — México: Unidad adscrita a la Secretaría de Hacienda y Crédito Público (SHCP) encargada de recibir, analizar y difundir reportes de operaciones sospechosas y prevenir el lavado de dinero.
- CNBV (Comisión Nacional Bancaria y de Valores) — México: Autoridad supervisora del sistema financiero que supervisa instituciones bancarias, casas de bolsa y su cumplimiento de normas AML.
- SAT (Servicio de Administración Tributaria) — México: Autoridad fiscal que participa en la prevención y detección de delitos financieros relacionados con evasión y lavado.
- Banco de México (Banxico): Banco central de México; regula aspectos del sistema de pagos y puede emitir disposiciones relacionadas con riesgos financieros.

Entidades regulatorias e internacionales relevantes:
- FATF / GAFI (Financial Action Task Force / Grupo de Acción Financiera Internacional): Organismo internacional que establece estándares y promueve la implementación efectiva de medidas legales, regulatorias y operativas para combatir el lavado de dinero y financiamiento del terrorismo.
- FinCEN (Financial Crimes Enforcement Network) — EE. UU.: Unidad de inteligencia financiera de Estados Unidos que recibe y analiza reportes de actividad sospechosa y coordina investigaciones transnacionales.
- Egmont Group: Red internacional de Unidades de Inteligencia Financiera (FIUs) que facilita el intercambio de información y cooperación entre países.
- UNODC (United Nations Office on Drugs and Crime): Oficina de la ONU que trabaja en prevención del crimen, incluyendo lavado de dinero y crimen organizado.
- IMF (International Monetary Fund / Fondo Monetario Internacional): Proporciona asistencia técnica y evalúa vulnerabilidades financieras y cumplimiento AML en países.
- World Bank (Banco Mundial): Provee asistencia técnica y apoyo para fortalecer marcos regulatorios y lucha contra delitos financieros.
- European Banking Authority (EBA) — Unión Europea: Regula y supervisa el sector bancario en UE, incluye directrices sobre prevención de lavado de dinero.
- Europol: Agencia de la UE para la cooperación policial que facilita la lucha contra el crimen organizado y delitos financieros.

Buenas prácticas relacionadas al glosario:
- Indicar el acrónimo y la forma expandida en ambos idiomas cuando aplique (ej.: KYC — Know Your Customer / Conoce a tu Cliente).
- Mantener definiciones concisas y actualizarlas cuando cambien regulaciones o prácticas.

Si quieres, puedo:
- Añadir referencias (enlaces) oficiales para cada entidad regulatoria.
- Traducir todo el glosario a un archivo separado GLOSSARY_EN.md con solo inglés.
- Insertar el glosario en el README y añadir el enlace automático.

