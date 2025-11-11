# Pasos completos del Proyecto de Clasificación

## Fase 1: Análisis inicial de los datos

### Objetivo
Entender qué se quiere predecir, qué variables se tienen y cómo están estructurados los datos.

### Pasos a realizar:

1. **Verificar la estructura y los tipos de las variables** (son 31)
   - El dataset contiene 31 columnas en total, de las cuales 30 corresponden a las características o atributos utilizados para describir los sitios web (por ejemplo, longitud de la URL, uso de SSL, edad del dominio, etc.).
   - La última columna, denominada **Result**, es la variable objetivo que indica si el sitio es phishing (1) o legítimo (-1).
   - En el análisis exploratorio inicial, **Result** debe incluirse para revisar su distribución y balance de clases. La **debemos usar** como variable predictora en los modelos (en la fase de entrenamiento);

2. **Separar features en binarias y ordinales**
   - Las variables del dataset son discretas y codificadas con valores -1, 0 y 1, que representan niveles de sospecha o legitimidad.
   - Según su rango de valores, se dividen en dos grupos:
     - **Binarias**: cuando solo toman dos valores (-1 y 1).
     - **Ordinales**: cuando pueden tomar tres valores (-1, 0 y 1), indicando distintos grados de riesgo.

3. **Verificar que no hay valores faltantes** (hay que dejarlo demostrado).

4. **Realizar un EDA básico**
   - En este punto no se realiza un EDA estadístico profundo, ya que todas las variables son discretas y acotadas con valores predefinidos (-1, 0, 1).
   - El objetivo es únicamente verificar la estructura y consistencia de los datos.
   - Métodos a usar:
     - **df.info()**: Muestra información estructural del DataFrame: cantidad de filas y columnas, nombres de las columnas, tipo de dato (int, float, object, etc.), si hay valores nulos o faltantes. Te permite ver si los datos cargaron bien, si las columnas están con el tipo correcto y si falta algo.
     - Analizar la distribución de la variable Result para conocer la proporción de sitios phishing y legítimos.
     - Revisión de valores únicos por columna (los valores distintos que aparecen en cada columna). Sirve para confirmar que todas las variables usan la misma codificación (-1, 0, 1) que define el dataset. No se hace para analizar, sino como verificación de integridad (una especie de control de calidad de los datos).

---

## Fase 2: Carga y preparación del dataset

### Objetivo
Realizar el análisis práctico y técnico de los datos mediante la carga del archivo, la verificación de tipos y ausencia de valores nulos, la exploración de la distribución de clases y la confirmación de que todas las variables estén correctamente codificadas de forma numérica. El objetivo final es dejar el dataset listo para su uso en el modelado.

### Pasos a realizar:

1. Cargar el dataset en el entorno de trabajo (CSV o ARFF).
2. **Verificar la estructura**: cantidad de filas y columnas, nombres y tipos de datos.
3. Confirmar la variable objetivo (Result) y sus valores posibles (1 y -1).
4. Analizar la distribución de clases y comentar si hay desbalance.
5. Comprobar valores faltantes y confirmar que no existan.
6. Revisar la codificación de las variables, asegurando que todas sean numéricas (-1, 0, 1).
7. **Definir una semilla aleatoria** (random_state = 42) para mantener la reproducibilidad en las divisiones y validaciones.

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
   
   Se implementarán dos estrategias de partición para analizar su impacto en el desempeño del modelo:
   
   **Estrategia A — 70/30:**
   - 70% para entrenamiento
   - 30% para prueba
   - Dentro del conjunto de entrenamiento se aplicará validación cruzada estratificada (Stratified K-Fold) para estimar el rendimiento y ajustar hiperparámetros.
   
   **Estrategia B — 70/15/15:**
   - 70% para entrenamiento
   - 15% para validación (para ajuste de hiperparámetros y comparación de modelos)
   - 15% para prueba (para evaluación final del desempeño)
   
   Ambas divisiones serán estratificadas para mantener la proporción original de clases y utilizarán un random_state fijo para asegurar la reproducibilidad.
   
   Luego mostrar una tabla comparativa con métricas (Accuracy, Precision, Recall, F1) para ambas.

3. **Elección del método de validación**
   
   Se empleará validación cruzada estratificada (Stratified K-Fold), utilizando k = 5 o 10, según el tiempo de ejecución y la estabilidad observada en las métricas.
   
   Este método divide el conjunto de entrenamiento en k subconjuntos (folds), manteniendo la proporción original de clases en cada uno. En cada iteración, uno de los folds se usa para validar y los restantes para entrenar, repitiendo el proceso k veces.
   
   Esto permite obtener una estimación más confiable del rendimiento promedio del modelo y evitar que los resultados dependan de una única partición de datos.
   
   Se aplicará este esquema de validación dentro de ambas estrategias de división (70/30 y 70/15/15) para comparar su comportamiento.

### Observaciones
Los subconjuntos de entrenamiento, validación y prueba no se guardan como archivos físicos, sino como variables en memoria (X_train, X_val, X_test, etc.) dentro del entorno de trabajo. Esto permite utilizarlos directamente en las fases siguientes sin necesidad de exportarlos, manteniendo la consistencia en las evaluaciones.

---

## Fase 4: Modelo base (Naive Bayes)

### Observaciones
- En esta fase se utilizan los subconjuntos generados en la etapa anterior. El modelo se entrena con los datos de entrenamiento y se evalúa con los de prueba (y validación, en caso de usar la división 70–15–15). Se trabaja con las variables ya definidas en memoria.
- Esta fase se realiza dos veces: una para el esquema 70–30 y otra para el 70–15–15, con el fin de comparar los resultados.

### Pasos a realizar:

1. **Entrenar el modelo base**
   - Crear el modelo con `GaussianNB()` (sin modificar hiperparámetros).
   - Ajustarlo con `fit(X_train, y_train)` usando los datos de entrenamiento.

2. **Evaluar el modelo**

   **Caso A: División 70–30**
   - Predecir sobre el conjunto de prueba: `y_pred = model.predict(X_test)`.
   - Calcular las métricas principales:
     - **Accuracy**: porcentaje total de aciertos.
     - **Precision**: de los detectados como phishing, cuántos eran realmente phishing.
     - **Recall (Sensibilidad)**: de los phishing reales, cuántos fueron detectados.
     - **F1-score**: balance entre precisión y recall.
     - **Matriz de confusión**: para visualizar aciertos y errores (TP, FP, FN, TN).
     - (Opcional): Curva ROC y AUC para analizar la capacidad de discriminación del modelo.
   - Analizar los resultados y comentar qué tipo de error predomina (FN o FP) y su impacto en la detección de phishing.

   **Caso B: División 70-15-15**
   - Entrenarlo con el conjunto de entrenamiento (70%): `fit(X_train, y_train)`.
   - Predecir sobre el conjunto de validación (15%).
   - Calcular las métricas principales (accuracy, precision, recall, F1).
   - Analizar si el modelo mantiene buen equilibrio entre recall y precision o si tiende a sobreajustarse.
   - Usar el conjunto de prueba (15%) solo para medir desempeño final.
   - Recalcular todas las métricas y comparar con los valores obtenidos en la validación.
   - Registrar los resultados para luego comparar con el esquema 70–30.

3. **Interpretación de resultados**
   
   Analizar qué tipo de error predomina:
   - **FN (Falsos Negativos)**: phishing no detectado → riesgo alto de fraude.
   - **FP (Falsos Positivos)**: sitios legítimos marcados como phishing → molestias o falsas alarmas.
   
   Evaluar si el modelo prioriza más la precisión o el recall, y cómo eso impacta en el contexto de seguridad informática.

4. **Comparar ambos esquemas**
   - Si las métricas del 70-15-15 son más estables entre validación y prueba → mejor generalización.
   - Si el 70-30 rinde igual o mejor → el dataset es suficientemente grande y la validación extra no aporta mucho.

---

## Fase 5: Optimización de hiperparámetros (para GaussianNB)

### Observaciones
Se parte del modelo entrenado en la Fase 4 (GaussianNB() sin ajustes) como referencia para comparar métricas.

### Pasos a realizar:

1. **Identificar hiperparámetro**
   - `var_smoothing`: controla la estabilidad de la varianza.
   - Valores muy pequeños → modelo sensible.
   - Valores más grandes → modelo más estable.

2. **Definir espacio de búsqueda**
   
   El hiperparámetro `var_smoothing` controla cuánto se suaviza la varianza de cada característica para evitar divisiones por cero o valores extremos.
   
   Se define un rango de búsqueda con valores en escala logarítmica:
   ```python
   var_smoothing ∈ {1e-9, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4}
   ```
   
   Este rango es suficiente para detectar el punto donde el modelo logra un equilibrio entre estabilidad numérica y capacidad de discriminación.

3. **Estrategias de validación**
   
   **Caso A (70-30):**
   - Entrenar con 70% de datos y usar validación cruzada estratificada (k=5) sobre ese conjunto.
   - Métrica de selección: recall o F1-score (según foco en detección de phishing).
   
   **Caso B (70-15-15):**
   - Entrenar con el 70%.
   - Probar cada valor de var_smoothing sobre el 15% de validación.
   - Elegir el que logre mejor recall o F1-score.

4. **Evaluar y seleccionar el mejor valor**
   - Comparar métricas obtenidas para cada var_smoothing.
   - Seleccionar el valor que maximice el desempeño (especialmente recall de phishing).

5. **Reentrenar el modelo final**
   - Entrenar nuevamente el modelo con el mejor var_smoothing usando todo el conjunto de entrenamiento correspondiente.

6. **Evaluar en el conjunto de prueba**
   - Usar el 30% (o el 15% de test en el caso B).
   - Calcular:
     - Accuracy
     - Precision
     - Recall
     - F1-score
     - Matriz de confusión

7. **Comparar con el modelo base**
   - Mostrar tabla comparativa (Base vs Optimizado).
   - Analizar si se redujeron los falsos negativos (FN) o los falsos positivos (FP).


## Observaciones: 

- se pueden seleccionar las columnas 
- ver el smottohing que sea continuo 
