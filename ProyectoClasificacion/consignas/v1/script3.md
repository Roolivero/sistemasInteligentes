# Pasos - parte 3 División y validación

## Objetivo:

Dividir el conjunto de datos en tres subconjuntos —entrenamiento, validación y prueba— para entrenar, ajustar y evaluar el modelo de manera controlada y reproducible, manteniendo la proporción original de clases.

1) **Separar variables predictoras y la variable objetivo**

```bash 
X = datos.drop("Result", axis=1)
y = datos["Result"]
```
Confirmar que Result sea binaria: 1 (phishing) y -1 (legítimo).

2) **División en tres subconjuntos**

Se implementarán dos estrategias de partición para analizar su impacto en el desempeño del modelo:

* **Estrategia A — 70/30:**

- 70 % para entrenamiento
- 30 % para prueba

Dentro del conjunto de entrenamiento se aplicará validación cruzada estratificada (Stratified K-Fold) para estimar el rendimiento y ajustar hiperparámetros.

* **Estrategia B — 70/15/15:**

- 70 % para entrenamiento
- 15 % para validación (para ajuste de hiperparámetros y comparación de modelos)
- 15 % para prueba (para evaluación final del desempeño)

Ambas divisiones serán estratificadas para mantener la proporción original de clases y utilizarán un random_state fijo para asegurar la reproducibilidad.

* Luego mostrar una tabla comparativa con métricas (Accuracy, Precision, Recall, F1) para ambas.

3) **Elección del método de validación**

Se empleará validación cruzada estratificada (Stratified K-Fold), utilizando k = 5 o 10, según el tiempo de ejecución y la estabilidad observada en las métricas.

Este método divide el conjunto de entrenamiento en k subconjuntos (folds), manteniendo la proporción original de clases en cada uno.

En cada iteración, uno de los folds se usa para validar y los restantes para entrenar, repitiendo el proceso k veces.

Esto permite obtener una estimación más confiable del rendimiento promedio del modelo y evitar que los resultados dependan de una única partición de datos.

Se aplicará este esquema de validación dentro de ambas estrategias de división (70/30 y 70/15/15) para comparar su comportamiento.

## Observaciones: 

Los subconjuntos de entrenamiento, validación y prueba no se guardan como archivos físicos, sino como variables en memoria (X_train, X_val, X_test, etc.) dentro del entorno de trabajo. Esto permite utilizarlos directamente en las fases siguientes sin necesidad de exportarlos, manteniendo la consistencia en las evaluaciones.