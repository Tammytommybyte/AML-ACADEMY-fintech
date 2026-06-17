# Módulo 06: Glosario Educativo

Este glosario reúne términos clave de finanzas, fraude, AML/compliance y data science usados en el repositorio.

## Cómo leer cada término

- **Definición:** explicación clara y breve.
- **Contexto de uso en el proyecto:** dónde aparece.
- **Ejemplo práctico:** caso aplicable.
- **Relación con otros términos:** conexiones útiles para estudiar.
- **Módulos donde se usa:** referencia a carpetas del repositorio.

## Términos Financieros Básicos

### Transacción
- **Definición:** Movimiento de dinero entre cuentas o actores financieros.
- **Contexto de uso en el proyecto:** Se usa para analizar operaciones en los módulos de fraude y riesgo.
- **Ejemplo práctico:** Transferencia de 500 USD entre dos cuentas.
- **Relación con otros términos:** Se relaciona con movimiento, dinero y con términos de la categoría términos financieros básicos.
- **Módulos donde se usa:** `02_Analisis_Financiero`

### Saldo
- **Definición:** Cantidad disponible en una cuenta en un momento dado.
- **Contexto de uso en el proyecto:** Permite validar capacidad financiera y detectar inconsistencias.
- **Ejemplo práctico:** Cuenta con saldo inicial de 1200 USD.
- **Relación con otros términos:** Se relaciona con cuenta, balance y con términos de la categoría términos financieros básicos.
- **Módulos donde se usa:** `02_Analisis_Financiero`

### Monto
- **Definición:** Valor monetario de una transacción específica.
- **Contexto de uso en el proyecto:** Es variable clave para reglas de alertamiento y métricas.
- **Ejemplo práctico:** Compra por 89.90 USD en comercio digital.
- **Relación con otros términos:** Se relaciona con valor, importe y con términos de la categoría términos financieros básicos.
- **Módulos donde se usa:** `02_Analisis_Financiero`

### Depósito
- **Definición:** Ingreso de fondos en una cuenta bancaria o billetera.
- **Contexto de uso en el proyecto:** Se monitorea para identificar patrones atípicos de entrada de dinero.
- **Ejemplo práctico:** Depósito en efectivo de 3000 USD.
- **Relación con otros términos:** Se relaciona con abono, ingreso y con términos de la categoría términos financieros básicos.
- **Módulos donde se usa:** `02_Analisis_Financiero`

### Retiro
- **Definición:** Salida de dinero desde una cuenta.
- **Contexto de uso en el proyecto:** Ayuda a medir fuga de liquidez y comportamiento de riesgo.
- **Ejemplo práctico:** Retiro en cajero por 250 USD.
- **Relación con otros términos:** Se relaciona con extracción, egreso y con términos de la categoría términos financieros básicos.
- **Módulos donde se usa:** `02_Analisis_Financiero`

### Cuenta bancaria
- **Definición:** Producto financiero donde se registran movimientos y saldos de un cliente.
- **Contexto de uso en el proyecto:** Es la entidad central para relacionar eventos y transacciones.
- **Ejemplo práctico:** Cuenta corriente usada para pagos diarios.
- **Relación con otros términos:** Se relaciona con cuenta, cliente y con términos de la categoría términos financieros básicos.
- **Módulos donde se usa:** `02_Analisis_Financiero`

### Cliente
- **Definición:** Persona o empresa titular de productos financieros.
- **Contexto de uso en el proyecto:** Su perfil se usa en KYC y en detección de comportamiento.
- **Ejemplo práctico:** Cliente con historial de pagos puntuales.
- **Relación con otros términos:** Se relaciona con usuario, titular y con términos de la categoría términos financieros básicos.
- **Módulos donde se usa:** `04_AML_Compliance`

### Volatilidad
- **Definición:** Grado de variación de un valor en el tiempo.
- **Contexto de uso en el proyecto:** Permite identificar inestabilidad en montos o frecuencias.
- **Ejemplo práctico:** Montos diarios con cambios bruscos en una semana.
- **Relación con otros términos:** Se relaciona con variación, riesgo y con términos de la categoría términos financieros básicos.
- **Módulos donde se usa:** `02_Analisis_Financiero`

### Flujo de efectivo
- **Definición:** Entradas y salidas de dinero de una cuenta o negocio.
- **Contexto de uso en el proyecto:** Se usa para evaluar sostenibilidad y posibles desbalances.
- **Ejemplo práctico:** Más retiros que depósitos durante un mes.
- **Relación con otros términos:** Se relaciona con cashflow, entradas y con términos de la categoría términos financieros básicos.
- **Módulos donde se usa:** `02_Analisis_Financiero`

### Indicador financiero
- **Definición:** Métrica que resume desempeño o riesgo financiero.
- **Contexto de uso en el proyecto:** Se calcula en análisis para apoyar decisiones.
- **Ejemplo práctico:** Índice de transacciones rechazadas por semana.
- **Relación con otros términos:** Se relaciona con métrica, ratio y con términos de la categoría términos financieros básicos.
- **Módulos donde se usa:** `02_Analisis_Financiero`

### Activo
- **Definición:** Recurso con valor económico que posee una persona o entidad.
- **Contexto de uso en el proyecto:** Ayuda a contextualizar capacidad económica del cliente.
- **Ejemplo práctico:** Saldo en inversiones de bajo riesgo.
- **Relación con otros términos:** Se relaciona con bien, recurso y con términos de la categoría términos financieros básicos.
- **Módulos donde se usa:** `02_Analisis_Financiero`

### Pasivo
- **Definición:** Obligación financiera pendiente de pago.
- **Contexto de uso en el proyecto:** Se considera en perfilamiento de riesgo financiero.
- **Ejemplo práctico:** Préstamo personal con cuotas mensuales.
- **Relación con otros términos:** Se relaciona con deuda, obligación y con términos de la categoría términos financieros básicos.
- **Módulos donde se usa:** `02_Analisis_Financiero`

### Liquidez
- **Definición:** Facilidad para convertir activos en efectivo.
- **Contexto de uso en el proyecto:** Importa para evaluar respuesta ante movimientos inusuales.
- **Ejemplo práctico:** Fondo disponible para cubrir pagos inmediatos.
- **Relación con otros términos:** Se relaciona con efectivo, disponibilidad y con términos de la categoría términos financieros básicos.
- **Módulos donde se usa:** `02_Analisis_Financiero`

### Rentabilidad
- **Definición:** Capacidad de generar ganancias sobre una inversión.
- **Contexto de uso en el proyecto:** Se usa para medir desempeño en casos de estudio.
- **Ejemplo práctico:** Retorno anual de 8% en cartera simulada.
- **Relación con otros términos:** Se relaciona con retorno, ganancia y con términos de la categoría términos financieros básicos.
- **Módulos donde se usa:** `05_Proyectos_Integradores`

### Riesgo crediticio
- **Definición:** Probabilidad de incumplimiento en obligaciones de crédito.
- **Contexto de uso en el proyecto:** Se cruza con señales de fraude y AML en análisis integral.
- **Ejemplo práctico:** Cliente con mora repetida en pagos.
- **Relación con otros términos:** Se relaciona con crédito, incumplimiento y con términos de la categoría términos financieros básicos.
- **Módulos donde se usa:** `05_Proyectos_Integradores`

## Términos de Fraude

### Fraude
- **Definición:** Acción deliberada para obtener beneficio financiero ilícito.
- **Contexto de uso en el proyecto:** Es el objetivo principal de detección en el módulo 03.
- **Ejemplo práctico:** Uso de cuenta comprometida para compras no autorizadas.
- **Relación con otros términos:** Se relaciona con engaño, delito y con términos de la categoría términos de fraude.
- **Módulos donde se usa:** `03_Deteccion_Fraude`

### Heurística
- **Definición:** Regla práctica basada en experiencia para detectar eventos sospechosos.
- **Contexto de uso en el proyecto:** Se usa cuando no hay modelo complejo disponible.
- **Ejemplo práctico:** Marcar transacciones nocturnas de alto monto.
- **Relación con otros términos:** Se relaciona con regla, criterio y con términos de la categoría términos de fraude.
- **Módulos donde se usa:** `03_Deteccion_Fraude`

### Anomalía
- **Definición:** Dato o comportamiento que se desvía del patrón esperado.
- **Contexto de uso en el proyecto:** Permite priorizar revisiones en monitoreo continuo.
- **Ejemplo práctico:** Compra internacional atípica para el cliente.
- **Relación con otros términos:** Se relaciona con outlier, desviación y con términos de la categoría términos de fraude.
- **Módulos donde se usa:** `03_Deteccion_Fraude`

### Patrón sospechoso
- **Definición:** Secuencia de eventos con señales de posible fraude.
- **Contexto de uso en el proyecto:** Se construye combinando reglas y contexto histórico.
- **Ejemplo práctico:** Múltiples intentos fallidos y luego transacción exitosa alta.
- **Relación con otros términos:** Se relaciona con secuencia, señal y con términos de la categoría términos de fraude.
- **Módulos donde se usa:** `03_Deteccion_Fraude`

### Regla de detección
- **Definición:** Condición lógica que activa una alerta de riesgo.
- **Contexto de uso en el proyecto:** Base de sistemas de monitoreo transaccional iniciales.
- **Ejemplo práctico:** Si monto > 5000 y país nuevo, generar alerta.
- **Relación con otros términos:** Se relaciona con if, umbral y con términos de la categoría términos de fraude.
- **Módulos donde se usa:** `03_Deteccion_Fraude`

### Velocidad de transacciones
- **Definición:** Número de transacciones en una ventana de tiempo definida.
- **Contexto de uso en el proyecto:** Detecta automatización o actividad no habitual.
- **Ejemplo práctico:** 10 transferencias en 2 minutos.
- **Relación con otros términos:** Se relaciona con frecuencia, ventana y con términos de la categoría términos de fraude.
- **Módulos donde se usa:** `03_Deteccion_Fraude`

### Cambio de ubicación geográfica
- **Definición:** Variación abrupta de ubicación entre transacciones consecutivas.
- **Contexto de uso en el proyecto:** Se usa para identificar imposibilidad física de actividad legítima.
- **Ejemplo práctico:** Pago en México y minutos después en Japón.
- **Relación con otros términos:** Se relaciona con geolocalización, ubicación y con términos de la categoría términos de fraude.
- **Módulos donde se usa:** `03_Deteccion_Fraude`

### Perfil de comportamiento
- **Definición:** Resumen de hábitos normales de un cliente.
- **Contexto de uso en el proyecto:** Sirve como referencia para hallar desviaciones.
- **Ejemplo práctico:** Cliente suele operar solo en horario laboral.
- **Relación con otros términos:** Se relaciona con histórico, hábitos y con términos de la categoría términos de fraude.
- **Módulos donde se usa:** `03_Deteccion_Fraude`

### Desviación estándar
- **Definición:** Medida de dispersión respecto a la media.
- **Contexto de uso en el proyecto:** Ayuda a definir umbrales estadísticos de alerta.
- **Ejemplo práctico:** Montos fuera de 2 desviaciones estándar.
- **Relación con otros términos:** Se relaciona con dispersión, estadística y con términos de la categoría términos de fraude.
- **Módulos donde se usa:** `03_Deteccion_Fraude`

### Baseline
- **Definición:** Nivel base esperado de comportamiento para comparación.
- **Contexto de uso en el proyecto:** Es referencia para marcar eventos anómalos.
- **Ejemplo práctico:** Promedio semanal de 3 transacciones por día.
- **Relación con otros términos:** Se relaciona con línea base, referencia y con términos de la categoría términos de fraude.
- **Módulos donde se usa:** `03_Deteccion_Fraude`

## Términos AML/Compliance

### AML (Anti-Lavado de Dinero)
- **Definición:** Conjunto de prácticas para prevenir lavado de activos y financiamiento ilícito.
- **Contexto de uso en el proyecto:** Marco central del módulo de cumplimiento normativo.
- **Ejemplo práctico:** Monitoreo de operaciones para reportar actividad sospechosa.
- **Relación con otros términos:** Se relaciona con lavado, dinero y con términos de la categoría términos aml/compliance.
- **Módulos donde se usa:** `04_AML_Compliance`

### KYC (Know Your Customer)
- **Definición:** Proceso para verificar identidad y perfil de riesgo del cliente.
- **Contexto de uso en el proyecto:** Se aplica al alta y actualización de clientes.
- **Ejemplo práctico:** Validación de documento, dirección y actividad económica.
- **Relación con otros términos:** Se relaciona con identidad, onboarding y con términos de la categoría términos aml/compliance.
- **Módulos donde se usa:** `04_AML_Compliance`

### Due Diligence
- **Definición:** Evaluación de riesgo con revisión documental y contextual.
- **Contexto de uso en el proyecto:** Se usa en clientes de riesgo medio o alto.
- **Ejemplo práctico:** Análisis reforzado para cliente con operaciones internacionales.
- **Relación con otros términos:** Se relaciona con diligencia, revisión y con términos de la categoría términos aml/compliance.
- **Módulos donde se usa:** `04_AML_Compliance`

### SAR (Suspicious Activity Report)
- **Definición:** Reporte formal de actividad sospechosa a autoridad competente.
- **Contexto de uso en el proyecto:** Resultado de investigación interna de alertas AML.
- **Ejemplo práctico:** Emisión de SAR tras detectar estructuración de depósitos.
- **Relación con otros términos:** Se relaciona con reporte, sospecha y con términos de la categoría términos aml/compliance.
- **Módulos donde se usa:** `04_AML_Compliance`

### PEP (Persona Políticamente Expuesta)
- **Definición:** Persona con función pública relevante y mayor riesgo inherente.
- **Contexto de uso en el proyecto:** Requiere controles reforzados y seguimiento continuo.
- **Ejemplo práctico:** Cliente identificado como ex funcionario de alto nivel.
- **Relación con otros términos:** Se relaciona con pep, riesgo alto y con términos de la categoría términos aml/compliance.
- **Módulos donde se usa:** `04_AML_Compliance`

### Watchlist
- **Definición:** Lista de personas o entidades sujetas a vigilancia o sanción.
- **Contexto de uso en el proyecto:** Se consulta en procesos de screening automático.
- **Ejemplo práctico:** Coincidencia parcial de nombre con lista OFAC.
- **Relación con otros términos:** Se relaciona con lista, sanciones y con términos de la categoría términos aml/compliance.
- **Módulos donde se usa:** `04_AML_Compliance`

### Screening
- **Definición:** Comparación de clientes y transacciones contra listas de riesgo.
- **Contexto de uso en el proyecto:** Paso crítico previo a aprobación de operaciones.
- **Ejemplo práctico:** Evaluar beneficiario contra listas internacionales.
- **Relación con otros términos:** Se relaciona con filtro, coincidencia y con términos de la categoría términos aml/compliance.
- **Módulos donde se usa:** `04_AML_Compliance`

### FATF (Financial Action Task Force)
- **Definición:** Organismo internacional que emite estándares AML/CFT.
- **Contexto de uso en el proyecto:** Guía recomendaciones aplicadas en políticas de compliance.
- **Ejemplo práctico:** Alinear controles internos con recomendaciones FATF.
- **Relación con otros términos:** Se relaciona con fatf, gafi y con términos de la categoría términos aml/compliance.
- **Módulos donde se usa:** `04_AML_Compliance`

### Compliance
- **Definición:** Cumplimiento de normativas internas y externas aplicables.
- **Contexto de uso en el proyecto:** Marco transversal para procesos y reportes regulatorios.
- **Ejemplo práctico:** Revisión periódica de políticas y controles.
- **Relación con otros términos:** Se relaciona con cumplimiento, normativa y con términos de la categoría términos aml/compliance.
- **Módulos donde se usa:** `04_AML_Compliance`

### Reporte regulatorio
- **Definición:** Documento requerido por reguladores sobre actividad y controles.
- **Contexto de uso en el proyecto:** Se genera con base en indicadores y eventos monitoreados.
- **Ejemplo práctico:** Envío mensual de alertas analizadas al supervisor.
- **Relación con otros términos:** Se relaciona con regulador, informe y con términos de la categoría términos aml/compliance.
- **Módulos donde se usa:** `04_AML_Compliance`

## Términos de Data Science

### DataFrame
- **Definición:** Estructura tabular de datos con filas y columnas.
- **Contexto de uso en el proyecto:** Es la base de manipulación en ejercicios de pandas.
- **Ejemplo práctico:** Cargar CSV de transacciones en un DataFrame.
- **Relación con otros términos:** Se relaciona con pandas, tabla y con términos de la categoría términos de data science.
- **Módulos donde se usa:** `01_Fundamentos`

### Series
- **Definición:** Estructura unidimensional etiquetada en pandas.
- **Contexto de uso en el proyecto:** Se usa para columnas individuales y operaciones vectorizadas.
- **Ejemplo práctico:** Extraer columna monto como Series.
- **Relación con otros términos:** Se relaciona con pandas, vector y con términos de la categoría términos de data science.
- **Módulos donde se usa:** `01_Fundamentos`

### Feature Engineering
- **Definición:** Creación y transformación de variables para mejorar modelos.
- **Contexto de uso en el proyecto:** Clave en clasificación de fraude y scoring de riesgo.
- **Ejemplo práctico:** Crear variable monto_promedio_7d por cliente.
- **Relación con otros términos:** Se relaciona con variables, atributos y con términos de la categoría términos de data science.
- **Módulos donde se usa:** `03_Deteccion_Fraude`

### Matriz de Confusión
- **Definición:** Tabla que compara predicciones contra valores reales.
- **Contexto de uso en el proyecto:** Permite evaluar aciertos y errores del modelo.
- **Ejemplo práctico:** Mostrar verdaderos positivos y falsos negativos.
- **Relación con otros términos:** Se relaciona con evaluación, tp y con términos de la categoría términos de data science.
- **Módulos donde se usa:** `03_Deteccion_Fraude`

### Precisión
- **Definición:** Proporción de positivos predichos que son correctos.
- **Contexto de uso en el proyecto:** Útil cuando el costo de falsas alertas es relevante.
- **Ejemplo práctico:** De 100 alertas, 80 fueron fraude real.
- **Relación con otros términos:** Se relaciona con precision, exactitud y con términos de la categoría términos de data science.
- **Módulos donde se usa:** `03_Deteccion_Fraude`

### Recall
- **Definición:** Proporción de casos positivos reales detectados.
- **Contexto de uso en el proyecto:** Prioritario cuando perder fraudes es costoso.
- **Ejemplo práctico:** Se detectó 90% de fraudes existentes.
- **Relación con otros términos:** Se relaciona con sensibilidad, cobertura y con términos de la categoría términos de data science.
- **Módulos donde se usa:** `03_Deteccion_Fraude`

### F1-Score
- **Definición:** Media armónica entre precisión y recall.
- **Contexto de uso en el proyecto:** Resume desempeño balanceado en clases desiguales.
- **Ejemplo práctico:** F1 de 0.82 en validación del clasificador.
- **Relación con otros términos:** Se relaciona con f1, balance y con términos de la categoría términos de data science.
- **Módulos donde se usa:** `03_Deteccion_Fraude`

### ROC Curve
- **Definición:** Curva que compara tasa de verdaderos positivos frente a falsos positivos.
- **Contexto de uso en el proyecto:** Ayuda a elegir umbral de clasificación.
- **Ejemplo práctico:** Comparar dos modelos con sus curvas ROC.
- **Relación con otros términos:** Se relaciona con roc, umbral y con términos de la categoría términos de data science.
- **Módulos donde se usa:** `03_Deteccion_Fraude`

### AUC (Area Under Curve)
- **Definición:** Área bajo la curva ROC, mide capacidad de discriminación.
- **Contexto de uso en el proyecto:** Se usa para comparar clasificadores de fraude.
- **Ejemplo práctico:** Modelo AUC 0.91 supera al de 0.84.
- **Relación con otros términos:** Se relaciona con auc, roc y con términos de la categoría términos de data science.
- **Módulos donde se usa:** `03_Deteccion_Fraude`

### Machine Learning
- **Definición:** Métodos que aprenden patrones desde datos para predecir.
- **Contexto de uso en el proyecto:** Aplicado en módulos de fraude y proyectos integradores.
- **Ejemplo práctico:** Entrenar modelo para clasificar transacciones riesgosas.
- **Relación con otros términos:** Se relaciona con ml, modelo y con términos de la categoría términos de data science.
- **Módulos donde se usa:** `03_Deteccion_Fraude`

### Clasificación
- **Definición:** Tarea supervisada para asignar una clase discreta.
- **Contexto de uso en el proyecto:** Se usa para decidir fraude/no fraude.
- **Ejemplo práctico:** Etiqueta binaria: 1 fraude, 0 legítima.
- **Relación con otros términos:** Se relaciona con clase, binario y con términos de la categoría términos de data science.
- **Módulos donde se usa:** `03_Deteccion_Fraude`

### Regresión Logística
- **Definición:** Modelo lineal probabilístico para clasificación binaria.
- **Contexto de uso en el proyecto:** Primer modelo base recomendado por su interpretabilidad.
- **Ejemplo práctico:** Estimar probabilidad de fraude por transacción.
- **Relación con otros términos:** Se relaciona con logistic regression, probabilidad y con términos de la categoría términos de data science.
- **Módulos donde se usa:** `03_Deteccion_Fraude`

### Train/Test Split
- **Definición:** Separación de datos en entrenamiento y prueba.
- **Contexto de uso en el proyecto:** Evita evaluar el modelo en datos vistos.
- **Ejemplo práctico:** Usar 80% para entrenar y 20% para probar.
- **Relación con otros términos:** Se relaciona con partición, validación y con términos de la categoría términos de data science.
- **Módulos donde se usa:** `03_Deteccion_Fraude`

### Overfitting
- **Definición:** Cuando el modelo aprende ruido y pierde generalización.
- **Contexto de uso en el proyecto:** Riesgo típico con demasiadas variables o poca regularización.
- **Ejemplo práctico:** Excelente en train pero pobre en test.
- **Relación con otros términos:** Se relaciona con sobreajuste, generalización y con términos de la categoría términos de data science.
- **Módulos donde se usa:** `03_Deteccion_Fraude`

### Underfitting
- **Definición:** Cuando el modelo es demasiado simple para capturar el patrón.
- **Contexto de uso en el proyecto:** Indica necesidad de mejores features o mayor complejidad.
- **Ejemplo práctico:** Bajo desempeño tanto en train como en test.
- **Relación con otros términos:** Se relaciona con subajuste, sesgo y con términos de la categoría términos de data science.
- **Módulos donde se usa:** `03_Deteccion_Fraude`

## Términos de Análisis

### EDA (Exploratory Data Analysis)
- **Definición:** Análisis inicial para entender estructura y calidad de datos.
- **Contexto de uso en el proyecto:** Primer paso antes de modelar o definir reglas.
- **Ejemplo práctico:** Revisar distribuciones y valores atípicos.
- **Relación con otros términos:** Se relaciona con eda, exploración y con términos de la categoría términos de análisis.
- **Módulos donde se usa:** `01_Fundamentos`

### Outlier
- **Definición:** Observación extrema que difiere notablemente del resto.
- **Contexto de uso en el proyecto:** Puede indicar fraude, error o caso especial.
- **Ejemplo práctico:** Monto diez veces mayor al promedio del cliente.
- **Relación con otros términos:** Se relaciona con atípico, anomalía y con términos de la categoría términos de análisis.
- **Módulos donde se usa:** `02_Analisis_Financiero`

### Valor Faltante (Missing Value)
- **Definición:** Dato ausente en un registro o variable.
- **Contexto de uso en el proyecto:** Debe tratarse antes de entrenar modelos.
- **Ejemplo práctico:** Edad del cliente vacía en formulario KYC.
- **Relación con otros términos:** Se relaciona con missing, null y con términos de la categoría términos de análisis.
- **Módulos donde se usa:** `01_Fundamentos`

### Imputación
- **Definición:** Técnica para reemplazar valores faltantes con un criterio definido.
- **Contexto de uso en el proyecto:** Mantiene volumen de datos para análisis y modelado.
- **Ejemplo práctico:** Completar ingresos faltantes con mediana del segmento.
- **Relación con otros términos:** Se relaciona con relleno, faltantes y con términos de la categoría términos de análisis.
- **Módulos donde se usa:** `01_Fundamentos`

### Normalización
- **Definición:** Escalado de variables a un rango común, usualmente 0 a 1.
- **Contexto de uso en el proyecto:** Facilita comparación y entrenamiento de algunos modelos.
- **Ejemplo práctico:** Escalar monto para redes neuronales.
- **Relación con otros términos:** Se relaciona con escala, minmax y con términos de la categoría términos de análisis.
- **Módulos donde se usa:** `03_Deteccion_Fraude`

### Estandarización
- **Definición:** Transformación para media 0 y desviación estándar 1.
- **Contexto de uso en el proyecto:** Útil en modelos sensibles a escala.
- **Ejemplo práctico:** Aplicar z-score a variables numéricas.
- **Relación con otros términos:** Se relaciona con zscore, media y con términos de la categoría términos de análisis.
- **Módulos donde se usa:** `03_Deteccion_Fraude`

### Correlación
- **Definición:** Medida de relación lineal entre dos variables.
- **Contexto de uso en el proyecto:** Ayuda a seleccionar features y detectar redundancias.
- **Ejemplo práctico:** Alta correlación entre frecuencia y monto total.
- **Relación con otros términos:** Se relaciona con relación, pearson y con términos de la categoría términos de análisis.
- **Módulos donde se usa:** `01_Fundamentos`

### Distribución
- **Definición:** Forma en que se reparten los valores de una variable.
- **Contexto de uso en el proyecto:** Permite elegir métricas y transformaciones adecuadas.
- **Ejemplo práctico:** Montos con distribución sesgada a la derecha.
- **Relación con otros términos:** Se relaciona con histograma, densidad y con términos de la categoría términos de análisis.
- **Módulos donde se usa:** `01_Fundamentos`

### Z-Score
- **Definición:** Número de desviaciones estándar de un valor respecto a la media.
- **Contexto de uso en el proyecto:** Se usa para detectar outliers de forma simple.
- **Ejemplo práctico:** Transacción con z-score de 3.2 marcada para revisión.
- **Relación con otros términos:** Se relaciona con z, outlier y con términos de la categoría términos de análisis.
- **Módulos donde se usa:** `02_Analisis_Financiero`

### IQR (Interquartile Range)
- **Definición:** Rango entre el percentil 75 y 25 de una variable.
- **Contexto de uso en el proyecto:** Método robusto para detección de valores extremos.
- **Ejemplo práctico:** Regla 1.5*IQR para detectar montos anómalos.
- **Relación con otros términos:** Se relaciona con iqr, cuartiles y con términos de la categoría términos de análisis.
- **Módulos donde se usa:** `02_Analisis_Financiero`

### Percentil
- **Definición:** Valor bajo el cual cae un porcentaje de observaciones.
- **Contexto de uso en el proyecto:** Permite definir umbrales por segmentación de riesgo.
- **Ejemplo práctico:** Monto en percentil 95 se considera alto.
- **Relación con otros términos:** Se relaciona con cuantil, ranking y con términos de la categoría términos de análisis.
- **Módulos donde se usa:** `02_Analisis_Financiero`

### Desviación típica
- **Definición:** Sinónimo de desviación estándar, mide dispersión de datos.
- **Contexto de uso en el proyecto:** Se usa para construir alertas y métricas de variabilidad.
- **Ejemplo práctico:** Aumenta la desviación típica de montos nocturnos.
- **Relación con otros términos:** Se relaciona con desviación, sigma y con términos de la categoría términos de análisis.
- **Módulos donde se usa:** `02_Analisis_Financiero`
