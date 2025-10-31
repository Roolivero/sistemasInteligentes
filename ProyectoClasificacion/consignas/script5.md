# Pasos - Parte 5 - Optimización de hiperparámetros (para GaussianNB)
## Observación: Se parte del modelo entrenado en la Fase 4 (GaussianNB() sin ajustes) como referencia para comparar métricas.

1) **Identificar hiperparámetro**

- var_smoothing: controla la estabilidad de la varianza.
- Valores muy pequeños → modelo sensible.
- Valores más grandes → modelo más estable.

2) **Definir espacio de búsqueda**

El hiperparámetro var_smoothing controla cuánto se suaviza la varianza de cada característica para evitar divisiones por cero o valores extremos.
Se define un rango de búsqueda con valores en escala logarítmica, que permiten explorar desde ajustes muy pequeños hasta moderados

```bash
    var_smoothing ∈ {1e-9, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4}
```
Este rango es suficiente para detectar el punto donde el modelo logra un equilibrio entre estabilidad numérica y capacidad de discriminación.

3) **Estrategias de validación**

* *Caso A (70-30):*
    - Entrenar con 70 % de datos y usar validación cruzada estratificada (k=5) sobre ese conjunto.
    - Métrica de selección: recall o F1-score (según foco en detección de phishing).

* *Caso B (70-15-15):*
    - Entrenar con el 70 %.
    - Probar cada valor de var_smoothing sobre el 15 % de validación.
    - Elegir el que logre mejor recall o F1-score.

4) **Evaluar y seleccionar el mejor valor**

- Comparar métricas obtenidas para cada var_smoothing.
- Seleccionar el valor que maximice el desempeño (especialmente recall de phishing).

5) **Reentrenar el modelo final**

- Entrenar nuevamente el modelo con el mejor var_smoothing usando todo el conjunto de entrenamiento correspondiente.

6) **Evaluar en el conjunto de prueba**
-Usar el 30 % (o el 15 % de test en el caso B).
- Calcular:
    - Accuracy
    - Precision    
    - Recall
    - F1-score
    - Matriz de confusión

7) **Comparar con el modelo base**    
- Mostrar tabla comparativa (Base vs Optimizado).    
- Analizar si se redujeron los falsos negativos (FN) o los falsos positivos (FP).