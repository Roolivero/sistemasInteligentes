# Pasos completos del Proyecto de Clasificación

## Fase 1: Análisis inicial de los datos

### Objetivo
Entender qué se quiere predecir, qué variables se tienen y cómo están estructurados los datos.

### Pasos a realizar:

1. **Verificar la estructura y los tipos de las variables** (son 31)
   - El dataset contiene 31 columnas en total, de las cuales 30 corresponden a las características o atributos utilizados para describir los sitios web (por ejemplo, longitud de la URL, uso de SSL, edad del dominio, etc.).
   - La última columna, denominada **Result**, es la variable objetivo que indica si el sitio es phishing (1) o legítimo (-1).
   - **Result** se utilizará como variable objetivo (y) en el entrenamiento de los modelos, donde 1 representa phishing y -1 representa legítimo.

2. **Verificar que no hay valores faltantes** (hay que dejarlo demostrado).

3. **Verificar tipos de datos numéricos**
   - Asegurar que todas las variables sean de tipo numérico (int o float).
   - Confirmar que todas las columnas (features y Result) sean numéricas antes de proceder con el modelado.

4. **Evaluación inicial con F-score**
   - En lugar de realizar un EDA estadístico tradicional, se realizará una evaluación inicial entrenando un modelo base y calculando el F-score como métrica principal.
   - Esto permite obtener una línea base de rendimiento y verificar que los datos están correctamente preparados para el modelado.
   - El objetivo es verificar la estructura y consistencia de los datos mediante el entrenamiento de un modelo inicial, en lugar de análisis exploratorio estadístico.

---

## Fase 2: Carga y preparación del dataset

### Objetivo
Realizar el análisis práctico y técnico de los datos mediante la carga del archivo, la verificación de tipos y ausencia de valores nulos, la exploración de la distribución de clases y la confirmación de que todas las variables estén correctamente codificadas de forma numérica. El objetivo final es dejar el dataset listo para su uso en el modelado.

### Pasos a realizar:

1. Cargar el dataset en el entorno de trabajo (CSV o ARFF).
2. **Verificar la estructura**: cantidad de filas y columnas, nombres y tipos de datos.
3. **Convertir todos los datos a numéricos**
   - Asegurar que Result sea de tipo int con valores 1 (phishing) y -1 (legítimo).
   - Verificar que todas las features sean numéricas (int o float).
4. Confirmar la variable objetivo (Result) y sus valores posibles: 1 (phishing) y -1 (legítimo).
5. Analizar la distribución de clases y comentar si hay desbalance. (Sabemos que las clases no estan desbalanceadas pero lo evaluamos para dejarlo por escrito)
6. Comprobar valores faltantes y confirmar que no existan.
7. Revisar la codificación de las variables, asegurando que todas sean numéricas (-1, 0, 1).
8. **Definir una semilla aleatoria** (random_state = 42) para mantener la reproducibilidad en las divisiones y validaciones.

---

## Fase 3: División y validación de datos

### Objetivo
Dividir el conjunto de datos en subconjuntos para entrenar, ajustar y evaluar el modelo de manera controlada y reproducible, manteniendo la proporción original de clases.

### Pasos a realizar:

1. **Separar variables predictoras y la variable objetivo**
   ```python
   X = datos.drop("Result", axis=1)
   y = datos["Result"]
   ```
   Confirmar que Result sea binaria: 1 (phishing) y -1 (legítimo). 

2. **División en subconjuntos**
   
   Se utilizará la **Estrategia 70/15/15** como método principal:
   
   **Estrategia 70/15/15:**
   - 70% para entrenamiento (X_train, y_train)
   - 15% para validación (X_val, y_val) - se usará más adelante para ajuste de hiperparámetros y comparación de modelos
   - 15% para prueba (X_test, y_test) - se usará solo para evaluación final del desempeño
   
   Esta división será estratificada para mantener la proporción original de clases y utilizará un random_state fijo para asegurar la reproducibilidad.
   
   La estrategia 70/15/15 es preferible porque permite tener un conjunto de validación dedicado para ajustar hiperparámetros sin tocar el conjunto de prueba, lo que proporciona una evaluación más robusta del desempeño final.
   
   **Nota**: El conjunto de validación (15%) se usará en la Fase 5 para optimizar hiperparámetros. La explicación detallada de cómo se realizará esa optimización (usando GridSearchCV) se encuentra en la Fase 5.

### Observaciones
Los subconjuntos de entrenamiento, validación y prueba no se guardan como archivos físicos, sino como variables en memoria (X_train, X_val, X_test, etc.) dentro del entorno de trabajo. Esto permite utilizarlos directamente en las fases siguientes sin necesidad de exportarlos, manteniendo la consistencia en las evaluaciones.

---

## Fase 4: Modelo base (Naive Bayes)

### Observaciones
- En esta fase se utilizan los subconjuntos generados en la etapa anterior. El modelo se entrena con los datos de entrenamiento (70%) usando **Result** como variable objetivo (y), donde Result = 1 representa phishing y Result = -1 representa legítimo.
- El modelo se evalúa primero con el conjunto de validación (15%) y luego con el de prueba (15%).
- Se trabaja con las variables ya definidas en memoria (X_train, X_val, X_test, y_train, y_val, y_test).

### Pasos a realizar:

1. **Entrenar el modelo base**
   - Crear el modelo con `GaussianNB()` (sin modificar hiperparámetros).
   - Ajustarlo con `fit(X_train, y_train)` usando los datos de entrenamiento (70%).
   - **Importante**: y_train corresponde a la columna Result del conjunto de entrenamiento.

2. **Evaluar el modelo en el conjunto de validación**
   - Predecir sobre el conjunto de validación (15%): `y_pred_val = model.predict(X_val)`.
   - Calcular las métricas principales:
     - **Accuracy**: porcentaje total de aciertos.
     - **Precision**: de los detectados como phishing, cuántos eran realmente phishing.
     - **Recall (Sensibilidad)**: de los phishing reales, cuántos fueron detectados.
     - **F1-score**: balance entre precisión y recall (métrica principal de evaluación).
     - **Matriz de confusión**: para visualizar aciertos y errores (TP, FP, FN, TN).
   - Analizar si el modelo mantiene buen equilibrio entre recall y precision o si tiende a sobreajustarse.

3. **Evaluar el modelo en el conjunto de prueba**
   - Predecir sobre el conjunto de prueba (15%): `y_pred_test = model.predict(X_test)`.
   - Recalcular todas las métricas (accuracy, precision, recall, F1-score).
   - Comparar con los valores obtenidos en la validación para verificar la consistencia del modelo.
   - Registrar los resultados para comparar con el modelo optimizado.

4. **Interpretación de resultados**
   
   Analizar qué tipo de error predomina:
   - **FN (Falsos Negativos)**: phishing no detectado → riesgo alto de fraude.
   - **FP (Falsos Positivos)**: sitios legítimos marcados como phishing → molestias o falsas alarmas.
   
   Evaluar si el modelo prioriza más la precisión o el recall, y cómo eso impacta en el contexto de seguridad informática.
   
   Comparar las métricas entre validación y prueba:
   - Si las métricas son similares → buen equilibrio y generalización.
   - Si hay diferencias significativas → posible sobreajuste o necesidad de ajustar hiperparámetros.

---

## Fase 5: Optimización de hiperparámetros (para GaussianNB)

### Observaciones
- **Orden del proceso**: Primero se entrena el modelo base en la Fase 4 (sin optimizar hiperparámetros), y luego en esta Fase 5 se optimiza usando GridSearchCV.
- Se parte del modelo entrenado en la Fase 4 (GaussianNB() sin ajustes) como referencia para comparar métricas.
- **¿Qué hace GridSearchCV?**: 
  - GridSearchCV SÍ entrena modelos, pero lo hace internamente como parte de su proceso de búsqueda.
  - Cuando ejecutas `grid_search.fit(X_train, y_train)`, GridSearchCV:
    1. Entrena múltiples modelos (uno por cada valor de `var_smoothing` que le indiques).
    2. Para cada modelo, usa validación cruzada para evaluarlo (entrena en algunos folds, evalúa en otros).
    3. Selecciona el mejor modelo según la métrica que definas (F1-score en este caso).
    4. Al final, el modelo en `best_estimator_` ya está entrenado con el mejor hiperparámetro.
- GridSearchCV solo necesita el conjunto de entrenamiento (70%) y automáticamente realiza la validación cruzada para seleccionar los mejores hiperparámetros.

### Pasos a realizar:

1. **Identificar hiperparámetro**
   - `var_smoothing`: controla la estabilidad de la varianza.
   - Valores muy pequeños → modelo sensible.
   - Valores más grandes → modelo más estable.

2. **Definir espacio de búsqueda**
   
   El hiperparámetro `var_smoothing` controla cuánto se suaviza la varianza de cada característica para evitar divisiones por cero o valores extremos.
   
   Se define un rango de búsqueda con valores en escala logarítmica usando `np.logspace()`:
   ```python
   param_grid = {"var_smoothing": np.logspace(-12, -6, 7)}
   # Equivale a: {1e-12, 1e-11, 1e-10, 1e-9, 1e-8, 1e-7, 1e-6}
   ```
   
   Este rango es suficiente para detectar el punto donde el modelo logra un equilibrio entre estabilidad numérica y capacidad de discriminación.

3. **Configurar GridSearchCV**
   
   Utilizar GridSearchCV de scikit-learn con las siguientes configuraciones:
   ```python
   from sklearn.model_selection import GridSearchCV, StratifiedKFold
   
   cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
   grid_search = GridSearchCV(
       GaussianNB(), 
       param_grid,
       scoring="f1",  # Métrica de selección: F1-score
       cv=cv, 
       n_jobs=-1
   )
   ```
   
   **Nota importante - Cómo funciona GridSearchCV**:
   
   GridSearchCV hace lo siguiente cuando ejecutas `grid_search.fit(X_train, y_train)`:
   
   1. **Toma el conjunto de entrenamiento** (70% de los datos).
   
   2. **Para cada valor de `var_smoothing`** (por ejemplo, 1e-12, 1e-11, ... 1e-6):
      - Divide el conjunto de entrenamiento en k=5 folds usando validación cruzada.
      - Para cada fold:
        - Entrena un modelo GaussianNB con ese valor de `var_smoothing` en 4 folds.
        - Evalúa el modelo en el fold restante y calcula el F1-score.
      - Calcula el F1-score promedio de los 5 folds para ese valor de `var_smoothing`.
   
   3. **Selecciona el mejor**: Elige el valor de `var_smoothing` que obtuvo el mejor F1-score promedio.
   
   4. **Entrena el modelo final**: Con el mejor `var_smoothing` encontrado, entrena un modelo usando TODO el conjunto de entrenamiento (70%).
   
   5. **Resultado**: El modelo en `best_estimator_` ya está entrenado y listo para usar.
   
   **Resumen**: GridSearchCV entrena múltiples modelos internamente para encontrar el mejor hiperparámetro, y te devuelve el modelo ya entrenado con los mejores parámetros.

4. **Entrenar y seleccionar el mejor modelo**
   - Ejecutar `grid_search.fit(X_train, y_train)`.
   - Esto ejecuta todo el proceso descrito arriba: GridSearchCV entrena múltiples modelos, evalúa cada uno con validación cruzada, selecciona el mejor según F1-score, y entrena el modelo final con el mejor hiperparámetro.
   - Obtener el mejor modelo: `best_model = grid_search.best_estimator_`.
   - El modelo `best_model` ya está entrenado y listo para hacer predicciones.

5. **Evaluar en el conjunto de validación (opcional)**
   - Predecir sobre el conjunto de validación (15%): `y_pred_val = best_model.predict(X_val)`.
   - Calcular métricas (accuracy, precision, recall, F1-score) para verificar el comportamiento.

6. **Evaluar en el conjunto de prueba**
   - Predecir sobre el conjunto de prueba (15%): `y_pred_test = best_model.predict(X_test)`.
   - Calcular todas las métricas:
     - Accuracy
     - Precision
     - Recall
     - F1-score
     - Matriz de confusión

7. **Comparar con el modelo base**
   - Mostrar tabla comparativa (Base vs Optimizado) con todas las métricas.
   - Analizar si se redujeron los falsos negativos (FN) o los falsos positivos (FP).
   - Verificar si el F1-score mejoró con la optimización de hiperparámetros.
