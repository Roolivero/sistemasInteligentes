# Borrador

## 1. El script debe contener una sección de preparación de los datos
      A).¿Qué variables numéricas y categóricas consideraste para el análisis?
      B).¿Qué impacto tienen los valores faltantes en K-means?
      C).¿Qué limitación supone ignorar las variables categóricas?​

Identificar y separar las variables en numericas y categoricas 

|Variables|Tipo|Clasificacion|
|----------|----|-------------------|
|age|Integer|Cuantitativa continua|
|workclass|Categorical|Cualitativa nominal|
|fnlwgt (final weight)|Integer|Cuantitativa continua| 
|education|Categorical|Cualitativa ordinal|
|education-num|Integer|Cuantitativa discreta|
|marital-status|Categorical|Cualitativa nominal|
|occupation|Categorical|Cualitativa nominal|
|relationship|Categorical|Cualitativa nominal|
|race|Categorical|Cualitativa nominal|
|sex |Binario|Cualitativa nominal |
|capital-gain|Integer|Cuantitativa continua|
|capital-loss|Integer|Cuantitativa continua|
|hours-per-week|Integer|Cuantitativa continua|
|native-country|Categorical|Cualitativa nominal|
|income|Binario|Cualitativa nominal|


### OBS: Los valores ceros en las variables numericas no indican que sean valores faltantes.


### A).
Consideramos todas las variables menos fnlwgt ya que esta varibale representa el peso de un conjunto de muestras iguales sobre el total de los datos y nosotros estamos analizando las muestras individuales. 

### B). 
Los valores faltantes (missing values) tienen un impacto negativo y directo en el funcionamiento del algoritmo K-means, porque este no puede operar con datos incompletos.

Por eso, antes de entrenar el modelo, hay que:
* Detectar los valores faltantes,
* Analizar su proporción,
* Decidir un tratamiento adecuado:
      * Si son pocos: eliminar filas con NaN
      * Si son moderados: imputar con media, mediana o moda
      * Si afectan columnas enteras: eliminar esa variable

### C).
El algoritmo K-means está diseñado para trabajar solo con variables numéricas continuas.
Esto se debe a que utiliza la distancia euclidiana para medir similitud entre los puntos.

Cuando tenés variables categóricas (como ocupación, estado civil, nivel educativo, etc.), no podés medir una distancia euclidiana válida entre categorías como “Married-civ-spouse” y “Divorced”.

Por eso, si las ignorás o las eliminás del análisis:

Limitaciones principales

Pérdida de información semántica.

Variables como marital-status, workclass o education aportan mucho contexto socioeconómico.

Al quitarlas, los clusters se basan solo en variables numéricas (edad, horas trabajadas, capital-gain/loss), lo que genera agrupamientos menos representativos.

Clusters incompletos o sesgados.

Personas con perfiles muy distintos (por ejemplo, un estudiante y un jubilado) pueden caer en el mismo cluster si sus valores numéricos son parecidos.

Interpretación menos rica.

No podés identificar patrones sociolaborales o educativos, que son justamente los más interesantes en el dataset Adult.

Distancia no representativa de la “realidad social”.

Dos individuos pueden tener distancias numéricas similares pero pertenecer a contextos totalmente distintos (por su ocupación, país o estado civil).

Por eso, la consigna pide que más adelante implementes la distancia de Gower y el AgglomerativeClustering,
porque Gower sí puede manejar variables mixtas (numéricas, ordinales y categóricas), corrigiendo esta limitación de K-means.


## 2. Gower

### Obs
Cuanto menor sea la distancia, más probable es que ambos individuos pertenezcan al mismo cluster o grupo de características similares.



## 3. Kmedias

```bash
# Decidir tipo de normalización basado en distribución
if abs(skewness) < 1.0 and abs(kurtosis) < 3.0:
    scaler_type = "StandardScaler (distribución normal)"
else:
    scaler_type = "MinMaxScaler (distribución sesgada)"
```

Variables y su Escalado:
StandardScaler (para age y hours_per_week):
¿Por qué? Estas variables tienen distribuciones más cercanas a la normal
Criterio: Asimetría < 1.0 y Curtosis < 3.0
Ventaja: Mantiene la forma de la distribución original
Resultado: Media ≈ 0, Desviación estándar ≈ 1
MinMaxScaler (para education_num, capital_gain, capital_loss):
¿Por qué? Estas variables tienen distribuciones sesgadas o con outliers
Criterio: Asimetría ≥ 1.0 o Curtosis ≥ 3.0
Ventaja: Es más robusto a outliers y comprime todos los valores al rango [0,1]
Resultado: Mínimo = 0, Máximo = 1
Razones Técnicas:
capital_gain y capital_loss: Típicamente tienen muchos ceros y pocos valores altos (distribución muy sesgada)
education_num: Puede tener distribución no normal
age y hours_per_week: Distribuciones más simétricas y normales
¿Por qué esta estrategia?
K-means es sensible a la escala de las variables
StandardScaler preserva mejor las relaciones cuando la distribución es normal
MinMaxScaler es más robusto con outliers y distribuciones sesgadas
Esta estrategia híbrida optimiza el rendimiento del clustering

1. Fundamentos Estadísticos
Asimetría (Skewness):
Valor 0: Distribución perfectamente simétrica (normal)
Valor < 1.0: Distribución aproximadamente normal
Valor > 1.0: Distribución claramente sesgada
Curtosis (Kurtosis):
Valor 3: Distribución normal (mesocúrtica)
Valor < 3: Distribución platicúrtica (más plana)
Valor > 3: Distribución leptocúrtica (más puntiaguda)
2. Criterios Establecidos en la Literatura
Los umbrales que usas (skewness < 1.0 y kurtosis < 3.0) son estándares reconocidos:
George & Mallery (2010): Skewness entre -1 y +1 indica distribución aproximadamente normal
Bulmer (1979): Curtosis entre 2 y 4 es aceptable para normalidad
Tabachnick & Fidell (2013): Skewness > 2 o < -2 indica severa no-normalidad
3. Justificación para K-means
StandardScaler (distribuciones normales):
K-means asume que las variables tienen varianzas similares
Funciona mejor con datos centrados y con desviación estándar unitaria
Preserva las distancias euclidianas de manera óptima
MinMaxScaler (distribuciones sesgadas):
Más robusto a outliers que pueden distorsionar los centroides
Evita que variables con rangos amplios dominen el clustering
Preserva la forma de la distribución original






## OBSERVACIONES DE CLASE 

* Considerar el final weigth a ver que pasa, cada registro tiene un peso 
* Ordena los pesos de menor a mayor y usar los 5.000 y 10.000 de mayor a menor para ver la mayor representacion de los datos (la mayoria de las personas que caen en esa categoria)

* EL income hay que dejarlo, no era parte de la consigna 
* Decidir si balancear los datos o no.(caulquier opcion es valido, depende de nosotros, mientras justifiquemos)
* Analizar la cohesion por ejemplo, los parametreos de Davies Boulding y Silluete

* feature engenieering -> Tenia dos variables que separadas no te dicen nada pero juntas puede ser que si (analizar esto)

* Una de als cosas que pdoriamos hacer es ordenas las variables o caracteristicas por variablidad
* Seria valido no considerar el peso pero si lo justificamos igual con un objetivo a analizar.

* Que dice un centroide del otro 
* Se puede analizar cada variable y en funcion a los resultados tomafr desiciones de si tomalas o no

* que pasa si haces las variables categoricas con aglomerative clustering y las numericas con kmedias

