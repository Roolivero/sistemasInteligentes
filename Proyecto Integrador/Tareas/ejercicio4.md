# Ejercicio 4

Este es un nuevo script, hay que resolverlo como un ejercicio aparte

## El script debe realizar un agrupamiento o clustering con K-means

1. Seleccionar las variables numéricas del dataset.
2. Escalar si es necesario (normalizar)
3. Aplicar K-means con distintos valores de k.
4. Determinar el número óptimo de clusters (Silhouette y/o Davies-Bouldin).

Preguntas guía:

- ¿Qué criterios usaste para definir el número de clusters?
- ¿Qué patrones observaste en los clusters formados?
- ¿Qué limitaciones tiene K-means al ignorar las variables categóricas

### Aclaraciones

Tenes que trabajar con estas variables:

|age|Integer|Cuantitativa continua|
|education-num|Integer|Cuantitativa discreta|
|capital-gain|Integer|Cuantitativa continua|
|capital-loss|Integer|Cuantitativa continua|
|hours-per-week|Integer|Cuantitativa continua|

- Escalar todas las variables
- Usar Silhouette y Davies-Bouldin y comparar ambos resultados para tomar una decision informada sobre que K usar en K-medias
