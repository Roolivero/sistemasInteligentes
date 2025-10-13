# Tareas para completar el script del ejercicio 1

## Aclaraciones: 
* Usamos el archivo adult.data
* Tenes que hacerlo en scripts -> scriptBorrador.ipybn
* En el archivo que esta en informes -> borrador.md hay mas informacion sobre las variables

## Pasos:

### Para obtener estas metricas hay que tener en cuenta que hay que hacerlo por columna.

### 1) Sacar la media (para las variables numericas)
variables: age, final weight, education_num, capital_gain, capital-loss, income y hours_per_week.

#### Obs sobre la variable Income: 
Tene en cuenta que estamos caluclando el porcentaje de ingresos (1 ganan > 50 y "0" ganan <= 50).
Esta variable hay que codificarla a binario y luego calcluar la media (pasa a ser una variable cuantitativa discreta binaria).

### 2) Sacar la mediana
Usamos las mismas variables que en 1) 

### 3) Sacar la moda de todas las variables 

### 4) Sacar máximo, mínimo y rango intercuartílico de las mismas variables que en 1) 

### 5) Sacar desviación estádar, varianza y cuartiles de las mismas varibales que en 1) 

### 6) Sacar la frecuencia absoluta y relativa de las varibales cualitativas

Variables: workclass, education, marital_status, ocupation, relationship, race, sex y native_country

### 7) Diagramar los box Plot

Variables: age, final weight, education_num, capital_gain, capital-loss y hours_per_week.

* El *objetivo* de este punto es ver la distribucion de las variables y sus outliers o puntos extremos.

### 8) Hacer un gráfico de barras o de proporción 

Varibales: sex e income
* El *objetivo* es ver los porcentajes de cada una

### 9) Hacer un gráfico de barras o de torta 

Variables: workclass, education, marital_status, ocupation, relationship, race y native_country
* El *objetivo* es ver las frecuencias

### 10) Hacer la matriz de correlación (hacerla con la formula de pearson)

Varibales: age, final weight, education_num, capital_gain, capital-loss y hours_per_week.

* Observacion: usar la variable income, hacer una matriz cuando income = 0 y otra cuando income =1. 

### 11) Hacer la tabla de contingencias para variables categóricas 

Con los siguientes conjuntos: 

* sex vs income
* education vs income
* workclass vs income
* marital_status vs income
* race vs income 


