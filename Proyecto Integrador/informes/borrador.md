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
