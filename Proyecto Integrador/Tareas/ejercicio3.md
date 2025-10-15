# Ejercicio 3

## Aclaraciones 
Para garantizar que las comparaciones sean consistentes, las muestras de 5.000 y 10.000 registros deben seleccionarse de manera aleatoria pero reproducible, utilizando una semilla fija (por ejemplo, con la función random_state o la librería random de Python). De esta forma, cada vez que se ejecute el script, se obtendrán exactamente los mismos subconjuntos de datos, lo que permite comparar los resultados de tiempo, memoria y estabilidad de clusters sin que los cambios se deban a una selección diferente de observaciones.

## Pasos:

### 1) Seleccionar las muestras

* Tomar dos subconjuntos del dataset original: una muestra de 5.000 registros, y otra de 10.000 registros.

Usar la función random o el parámetro random_state para que la selección sea aleatoria pero reproducible (siempre las mismas filas en cada ejecución).

### 2) Mantener el mismo preprocesamiento

Utilizar exactamente las mismas variables y transformaciones aplicadas previamente (normalización, codificación, manejo de faltantes, etc.) para ambas muestras.

### 3) Calcular la matriz de distancias de Gower

* Generar la matriz de distancias para cada muestra.
* Registrar el tiempo de ejecución y el uso de memoria durante el proceso.

### 4) Comparar resultados entre muestras

* Analizar cómo varían los tiempos y el consumo de memoria al aumentar el tamaño de la muestra.

* Tener en cuenta que el cálculo de Gower crece de forma cuadrática (O(n²)), ya que compara cada observación con todas las demás.
Por eso, al duplicar el tamaño de la muestra, el tiempo y la memoria requeridos aumentan más del doble.

### 5) Evaluar el trade-off entre tamaño y eficiencia

* Reconocer que usar muestras grandes mejora la representatividad y la precisión de los resultados.

* En cambio, usar muestras más pequeñas reduce el tiempo de ejecución y el uso de recursos, pero puede afectar la estabilidad o calidad de los clusters.

* El objetivo es encontrar un equilibrio entre precisión y eficiencia.

### 6) Explorar técnicas de escalado para grandes volúmenes de datos

Muestreo representativo o estratificado: mantener la diversidad del dataset sin usar todos los registros.

Cálculo aproximado de distancias: aplicar métodos como MiniBatch o Approximate Nearest Neighbors.

Reducción de dimensionalidad: emplear técnicas como PCA, t-SNE o UMAP para simplificar los datos antes de calcular distancias.

Procesamiento distribuido o paralelo: usar herramientas como Dask o Spark para dividir el cálculo entre múltiples núcleos o nodos.

### 7) Conclusión

Comparar la estabilidad de los clusters entre ambas muestras (por ejemplo, cuántos grupos se repiten o qué tan similares son sus centroides).

Concluir qué tamaño de muestra ofrece un mejor equilibrio entre calidad de resultados y eficiencia computacional.