# Pasos - parte 4 - Modelo base (Naive Bayes)

## Observaciones:

* En esta fase se utilizan los subconjuntos generados en la etapa anterior. El modelo se entrena con los datos de entrenamiento y se evalúa con los de prueba (y validación, en caso de usar la división 70–15–15). Se trabaja con las variables ya definidas en memoria.

* Esta fase se realiza dos veces: una para el esquema 70–30 y otra para el 70–15–15, con el fin de comparar los resultados.

1) **Entrenar el modelo base**

- Crear el modelo con GaussianNB() (sin modificar hiperparámetros).
- Ajustarlo con fit(X_train, y_train) usando los datos de entrenamiento.

2) **Evaluar el modelo**

* *Caso A: División 70 – 30*
    - Predecir sobre el conjunto de prueba: y_pred = model.predict(X_test).
    - *Calcular las métricas principales:*
        - **Accuracy:** porcentaje total de aciertos.
        - **Precision:** de los detectados como phishing, cuántos eran realmente phishing.
        - **Recall (Sensibilidad):** de los phishing reales, cuántos fueron detectados.
        - **F1-score:** balance entre precisión y recall.
        - **Matriz de confusión:** para visualizar aciertos y errores (TP, FP, FN, TN).
        - (Opcional): Curva ROC y AUC para analizar la capacidad de discriminación del modelo.
    - Analizar los resultados y comentar qué tipo de error predomina (FN o FP) y su impacto en la detección de phishing.

* *Caso B: División 70-15-15*
    - Entrenarlo con el conjunto de entrenamiento (70 %): fit(X_train, y_train).
    - Predecir sobre el conjunto de validación (15 %).
    - Calcular las métricas principales (accuracy, precision, recall, F1).
    - Analizar si el modelo mantiene buen equilibrio entre recall y precision o si tiende a sobreajustarse.
    - Usar el conjunto de prueba (15 %) solo para medir desempeño final.
    - Recalcular todas las métricas y comparar con los valores obtenidos en la validación
    - Registrar los resultados para luego comparar con el esquema 70 – 30.


3) **Interpretación de resultados**

Analizar qué tipo de error predomina:
- FN (Falsos Negativos) → phishing no detectado → riesgo alto de fraude.
- FP (Falsos Positivos) → sitios legítimos marcados como phishing → molestias o falsas alarmas.

Evaluar si el modelo prioriza más la precisión o el recall, y cómo eso impacta en el contexto de seguridad informática.

4) *Comparar ambos esquemas:*

- Si las métricas del 70-15-15 son más estables entre validación y prueba → mejor generalización.
- Si el 70-30 rinde igual o mejor → el dataset es suficientemente grande y la validación extra no aporta mucho.