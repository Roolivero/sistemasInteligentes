# PROYECTO DE AGRUPAMIENTO 

## Tema: Implementación y evaluación de clustering con el algoritmo K-means en el dataset Adult (UCI Census Income)

---

## 1. Análisis Estadístico Descriptivo del Dataset Adult Census

### 1.1 Introducción y Contexto

El presente análisis se centra en el dataset Adult Census Income, una base de datos ampliamente utilizada en el ámbito del aprendizaje automático que contiene información demográfica y socioeconómica de 32.561 individuos. Este dataset, proveniente del UCI Machine Learning Repository, constituye un recurso fundamental para el desarrollo de técnicas de agrupamiento (clustering) y clasificación, siendo especialmente relevante para el estudio de patrones socioeconómicos y la implementación de algoritmos de machine learning.

**Propósito Principal (Tarea de Predicción):** Determinar si el ingreso anual de una persona es superior a $50,000 o igual/inferior a esta cifra (una tarea de clasificación binaria: >50K o ≤50K). Este dataset fue creado a partir de datos del censo de Estados Unidos de 1994, donde la variable objetivo `income` representa la clasificación binaria que permite identificar patrones socioeconómicos y demográficos asociados con diferentes niveles de ingresos.

El objetivo principal de esta primera fase del proyecto consiste en realizar un análisis estadístico descriptivo exhaustivo que permita comprender la estructura, calidad y características fundamentales de los datos, estableciendo así las bases metodológicas necesarias para la posterior implementación del algoritmo K-means y otras técnicas de clustering.

### 1.2 Preparación y Limpieza de Datos

#### 1.2.1 Estructura del Dataset

El dataset Adult Census presenta una estructura compuesta por 15 variables  distribuidas en 32.561 observaciones. La clasificación de las variables se realizó según su naturaleza estadística:

**Variables Numéricas:**
- `age`: Edad del individuo (cuantitativa continua)
- `education_num`: Número de años de educación (cuantitativa discreta)
- `capital_gain`: Ganancias de capital (cuantitativa continua)
- `capital_loss`: Pérdidas de capital (cuantitativa continua)
- `hours_per_week`: Horas trabajadas por semana (cuantitativa continua)
- `income_binary`: Variable objetivo codificada como binaria (0: ≤50K, 1: >50K)

**Variables Categóricas:**
- `workclass`: Clase de trabajo (cualitativa nominal)
- `education`: Nivel educativo (cualitativa ordinal)
- `marital_status`: Estado civil (cualitativa nominal)
- `occupation`: Ocupación (cualitativa nominal)
- `relationship`: Relación familiar (cualitativa nominal)
- `race`: Raza (cualitativa nominal)
- `sex`: Sexo (cualitativa nominal binaria)
- `native_country`: País de origen (cualitativa nominal)

**Decisión Metodológica:** Se excluyó la variable `fnlwgt` (final weight) del análisis, ya que representa el peso de un conjunto de muestras iguales sobre el total de los datos, no características individuales de los sujetos analizados.

#### 1.2.2 Análisis de Valores Faltantes

El análisis de integridad de los datos reveló la presencia de valores faltantes en tres variables categóricas, representados por el símbolo '?'. La evaluación sistemática de estos valores faltantes arrojó los siguientes resultados:

- **Caso 1 (3 columnas vacías):** 27 filas (0.08% del total)
- **Caso 2 (2 columnas vacías):** 1.809 filas (5.56% del total)
- **Caso 3 (1 columna vacía):** 563 filas (1.73% del total)

**Distribución por variable:**
- `workclass`: 1.836 valores faltantes (5.64%)
- `occupation`: 1.843 valores faltantes (5.66%)
- `native_country`: 583 valores faltantes (1.79%)

**Estrategia de Limpieza Implementada:** Dado que el porcentaje total de valores faltantes supera el umbral crítico del 5% por variable individual, se implementó una estrategia de rellenado con valores modales para las variables categóricas:
- `workclass`: rellenado con 'Private' (moda)
- `occupation`: rellenado con 'Prof-specialty' (moda)
- `native_country`: rellenado con 'United-States' (moda)

Esta estrategia preservó la integridad del dataset manteniendo todas las 32.561 observaciones originales, garantizando así la representatividad estadística de la muestra. 

Se tomo esta decision porque cuando menos del 5% de los datos faltan, se considera que la pérdida es pequeña y no afecta significativamente la representatividad del conjunto. En esos casos, eliminar filas o columnas con valores faltantes no distorsiona mucho los resultados. Pero en este caso al superar el 5%, eliminar datos puede sesgar el dataset, porque:

- Reducís el tamaño muestral, perdiendo información útil (especialmente si el dataset no es muy grande).
- Podés alterar la distribución de las variables, sobre todo si los valores faltantes no son aleatorios (por ejemplo, si faltan más datos en ciertos grupos).
- Los modelos pierden capacidad generalizadora, ya que entrenan con un subconjunto menos representativo.

### 1.3 Análisis Estadístico Descriptivo

#### 1.3.1 Medidas de Tendencia Central

El análisis de las medidas de tendencia central permite describir el comportamiento promedio de las principales variables numéricas del conjunto de datos.
La edad promedio de los individuos es de 38,58 años, con una mediana de 37 años, lo que sugiere una distribución relativamente simétrica con predominio de adultos en edad laboral activa.

En cuanto a la variable education_num, su valor promedio (10,08) y mediano (10) indican que la mayoría de los individuos alcanzó un nivel educativo correspondiente a la categoría “Some-college”, según la codificación del dataset Adult Census. Esto representa personas que han completado la educación secundaria y cursado parcialmente estudios terciarios o universitarios, sin haber obtenido un título formal.

Las ganancias y pérdidas de capital presentan medias de 1.077,65 y 87,30 dólares respectivamente, mientras que sus medianas son cero, evidenciando una fuerte asimetría positiva: la mayoría de los individuos no registra operaciones de capital, aunque un pequeño grupo concentra valores elevados.
El promedio de horas trabajadas por semana (40,44) y su mediana (40) indican una jornada laboral típica a tiempo completo.

Finalmente, el 24,08% de los individuos reporta ingresos superiores a 50.000 dólares anuales, lo cual evidencia una marcada desigualdad en la distribución del ingreso.

#### 1.3.2 Medidas de Dispersión

Las medidas de dispersión evidencian la variabilidad de las observaciones. La edad muestra un rango amplio (17 a 90 años) y una desviación estándar de 13,64, indicando una diversidad etaria considerable.
Los años de educación presentan menor dispersión (DE = 2,57), reflejando cierta homogeneidad educativa dentro del conjunto.

Las ganancias y pérdidas de capital exhiben alta dispersión (DE = 7.385,29 y 402,96 respectivamente), lo que refuerza la presencia de valores extremos asociados a individuos con inversiones o pérdidas significativas.
Por su parte, las horas trabajadas por semana muestran una desviación estándar de 12,35, que evidencia variabilidad en los regímenes laborales (empleos de tiempo parcial, completo o con horas extraordinarias).

#### 1.3.3 Análisis de Outliers

El análisis mediante boxplots permitió identificar valores atípicos en distintas magnitudes.
Las variables capital_gain (8,33%), capital_loss (4,67%) y especialmente hours_per_week (27,66%) concentran una proporción considerable de outliers.
La variable hours_per_week presenta la mayor proporción de valores atípicos, lo que evidencia una alta variabilidad en las horas trabajadas. Este comportamiento puede atribuirse a la existencia de diferentes modalidades laborales, tales como empleos de tiempo parcial, tiempo completo y con horas extraordinarias, reflejando la diversidad en las condiciones de empleo dentro de la muestra.
Por su parte, los outliers observados en capital_gain y capital_loss corresponden a una minoría de individuos con movimientos de capital significativamente superiores al promedio.
Finalmente, la baja proporción de valores atípicos en age (0,44%) y education_num (3,68%) indica estabilidad en las dimensiones demográficas y educativas.

### 1.4 Análisis de Variables Categóricas

#### 1.4.1 Distribución Demográfica

**Distribución por Sexo:**
- Masculino: 66,92% (21.790 individuos)
- Femenino: 33,08% (10.771 individuos)

La muestra presenta una mayor proporción de hombres que de mujeres, lo cual podría incidir en la distribución de ingresos y ocupaciones observadas, especialmente en contextos donde existen diferencias estructurales en la inserción laboral y las oportunidades económicas por género.

**Distribución por Ingresos:**
- ≤50K: 75,92% (24.720 individuos)
- \>50K: 24,08% (7.841 individuos)

La mayoría de los individuos (75,92%) percibe ingresos anuales iguales o inferiores a 50.000 dólares, mientras que solo una cuarta parte (24,08%) supera dicho umbral. Esta disparidad refleja una estructura económica desigual, donde predomina la población de ingresos bajos y medios, característica consistente con los datos censales de los Estados Unidos en 1994.

#### 1.4.2 Características Socioeconómicas

**Clase de Trabajo (workclass):**

En términos ocupacionales, la mayoría de los individuos trabaja en el sector privado (75,34%), seguido por los autoempleados (7,80%) y empleados de gobiernos locales o estatales. Esto sugiere una estructura laboral concentrada en el ámbito privado con participación limitada del sector público.

**Nivel Educativo (education):**

Los resultados evidencian que los niveles educativos más frecuentes corresponden a HS-grad (32,25%) y Some-college (22,39%), lo cual refleja que una gran proporción de la población completó la educación secundaria o cursó parcialmente estudios superiores.
Los niveles universitarios y de posgrado (Bachelors, Masters, Doctorate) son minoritarios, aunque, como se analizará posteriormente, estos grupos presentan una mayor proporción de ingresos altos, confirmando la relevancia de la educación como factor socioeconómico.

**Estado Civil (marital_status):**

La estructura marital revela que el 46% de los individuos está casado con cónyuge presente, seguido por quienes nunca se casaron (32,81%) y los divorciados (13,64%). En conjunto, estas tres categorías agrupan más del 90% de la muestra, lo que sugiere una población predominantemente casada o soltera, con menor representación de personas separadas o viudas.

**Ocupación (occupation):**

La distribución ocupacional muestra una diversificación moderada del mercado laboral. Las categorías más frecuentes son profesiones especializadas (18,37%), trabajos técnicos o de reparación (12,59%) y puestos ejecutivos o administrativos (12,49%).
Esto sugiere una estructura laboral con predominio de ocupaciones calificadas y técnicas, aunque también se observa participación de sectores de servicios y tareas manuales.


**Relación Familiar (relationship):**

La estructura familiar se caracteriza por una mayor proporción de jefes de hogar masculinos (Husband, 40,51%), seguida por individuos que no pertenecen a un núcleo familiar (25,50%) y por hijos dentro del hogar (15,56%).
Estos datos reflejan una muestra compuesta principalmente por adultos casados y cabezas de familia, lo cual puede relacionarse con los patrones de ingresos y empleo observados.

**Raza (race):**

La composición racial del conjunto de datos está dominada por individuos de raza blanca (85,50%), seguidos por personas de raza negra (9,60%) y asiáticas o isleñas del Pacífico (2,85%). Esta distribución es coherente con la estructura demográfica de Estados Unidos en el período de referencia (1994).

**País de Origen (native_country):**

La mayoría de los individuos nació en los Estados Unidos (89,60%), mientras que el resto se distribuye entre diversos países de América Latina, Asia y Europa, como México (1,93%), Filipinas (0,93%), Alemania (0,50%) y Canadá (0,42%), entre otros.
Esta diversidad geográfica pone de manifiesto el carácter multicultural de la sociedad estadounidense, aunque con predominio de población nativa.

### 1.5 Análisis de Correlaciones

#### 1.5.1 Matriz de Correlación General

La matriz de correlación de Pearson evidencia ausencia de correlaciones lineales significativas entre las variables numéricas analizadas.
Según los criterios establecidos (r ≥ 0.8 fuerte, 0.5 < r < 0.8 débil, r < 0.5 sin correlación), todos los coeficientes se encuentran por debajo de 0.5.

La mayor correlación observada (r = 0.148) corresponde a la relación entre education_num y hours_per_week, lo que sugiere una ligera tendencia a que los individuos con mayor nivel educativo trabajen más horas semanales, aunque la relación no es linealmente relevante.
Del mismo modo, las correlaciones entre age–capital_gain (r = 0.078) y education_num–capital_gain (r = 0.123) indican asociaciones muy débiles que no implican dependencia estadística entre las variables.

#### 1.5.2 Correlaciones por Grupo de Ingresos

Al segmentar la muestra según el nivel de ingresos, las correlaciones de Pearson continúan mostrando valores inferiores a 0.5, lo que indica ausencia de correlaciones lineales significativas dentro de cada grupo.

En el grupo de individuos con ingresos >50K, la relación más destacada se presenta entre education_num y capital_gain (r = 0.106), lo que sugiere una asociación leve entre mayor nivel educativo y mayores ganancias de capital, aunque sin relación lineal relevante.
Asimismo, la correlación negativa entre age y hours_per_week (r = -0.127) muestra una tendencia muy débil a que las personas de mayor edad trabajen menos horas semanales.

En el grupo de ingresos ≤50K, las correlaciones son aún menores, reflejando comportamientos más heterogéneos y una estructura interna sin relaciones lineales detectables entre las variables numéricas.

### 1.6 Análisis de Contingencia

#### 1.6.1 Relación Sexo-Ingresos

La relación entre sexo e ingresos evidencia una brecha de género significativa.
El 89,05% de las mujeres percibe ≤50K frente al 69,43% de los hombres, mientras que el 30,57% de los hombres supera los 50K, contra solo 10,95% de las mujeres.
Estos resultados confirman la existencia de desigualdades de género en los ingresos, posiblemente relacionadas con diferencias en ocupaciones, niveles educativos o tipos de jornada laboral.


#### 1.6.2 Relación Educación-Ingresos

Se observa una asociación positiva entre nivel educativo e ingresos.
Las personas con Doctorate (74,09%), Prof-school (73,44%) o Masters (55,66%) presentan las mayores proporciones de ingresos >50K, mientras que los niveles educativos básicos como Preschool (0%) o 1st-4th (3,57%) muestran escasa participación en los niveles salariales altos.
Estos resultados refuerzan el papel de la educación como factor determinante en la movilidad económica y el acceso a mejores oportunidades laborales.


### 1.7 Respuestas a las Preguntas Guías

#### 1.7.1 ¿Qué variables numéricas y categóricas consideraste para el análisis?

Se consideraron todas las variables del dataset excepto `fnlwgt`, clasificándolas en:

**Variables Numéricas (6):** age, education_num, capital_gain, capital_loss, hours_per_week, income_binary

**Variables Categóricas (8):** workclass, education, marital_status, occupation, relationship, race, sex, native_country

#### 1.7.2 ¿Qué impacto tienen los valores faltantes en K-means?

Los valores faltantes afectan negativamente el desempeño de K-means debido a que el algoritmo no puede operar con datos incompletos, ya que requiere calcular distancias euclidianas entre todos los registros. Su presencia puede distorsionar los centroides y reducir la calidad del clustering.
Eliminar observaciones con valores nulos implica una pérdida de información y potencial sesgo de selección. Por ello, se aplicó imputación mediante la moda en las variables categóricas, manteniendo la coherencia y completitud del conjunto de datos.

#### 1.7.3 ¿Qué limitación supone ignorar las variables categóricas?

Ignorar las variables categóricas en K-means implica una pérdida significativa de información semántica, especialmente en atributos socioeconómicos como marital_status, workclass o education.
Esto puede derivar en clusters incompletos o poco representativos, donde individuos con perfiles diferentes se agrupan por similitudes numéricas superficiales.
Dado que la distancia euclidiana no refleja adecuadamente las diferencias entre categorías, se justifica el uso de métodos alternativos como la distancia de Gower y Agglomerative Clustering, que permiten integrar variables mixtas en el análisis.

### 1.8 Conclusiones del Análisis Descriptivo

El análisis descriptivo del dataset Adult Census evidencia un conjunto de datos estructurado y representativo, con diversidad demográfica y socioeconómica. Se observa una marcada desigualdad de ingresos, dado que solo el 24,08% de los individuos percibe más de 50.000 dólares anuales, concentrándose la mayoría en niveles bajos y medios. Asimismo, se identifican diferencias significativas por género: los hombres tienen 2,8 veces más probabilidades que las mujeres de superar dicho umbral de ingresos. La educación surge como un factor determinante, ya que los niveles académicos más altos —Doctorate, Prof-school y Masters— presentan una mayor proporción de individuos con ingresos elevados. En términos económicos, las variables capital_gain y capital_loss muestran alta variabilidad y predominio de valores nulos, reflejando una participación desigual en actividades de inversión o pérdidas de capital. Finalmente, la calidad del dataset es adecuada, con un 7,37% de valores faltantes, lo que permite aplicar estrategias de limpieza sin comprometer la representatividad de la muestra. En conjunto, estos resultados constituyen una base sólida para la aplicación de técnicas de clustering, como K-means y aquellas basadas en la distancia de Gower, orientadas a identificar perfiles y patrones socioeconómicos dentro de la población analizada.

---

## 2. Implementación y Evaluación de la Distancia de Gower

### 2.1 Procesamiento de Variables según Tipo

Previo al cálculo de la distancia de Gower, se realizó una selección y tratamiento diferenciado de las variables del dataset.
Se excluyeron aquellas que no aportan información útil o podrían generar redundancia en el análisis:

fnlwgt: representa un peso estadístico sin relevancia interpretativa directa para el clustering.

education_num: se eliminó por duplicar la información de education, ya que esta última fue normalizada mediante label encoding y ambas variables representarían el mismo concepto educativo.

income: al ser la variable objetivo del dataset, no se incluye en un análisis no supervisado, ya que su incorporación forzaría al algoritmo a agrupar según la respuesta final, anulando la exploración de patrones naturales.

Las variables numéricas (age, capital_gain, capital_loss, hours_per_week) se normalizaron mediante el método min–max, transformando sus valores al rango [0,1]. Esto garantiza comparabilidad entre atributos de diferentes escalas y evita que una variable con magnitudes elevadas domine el cálculo de disimilitud.

La variable education, de tipo ordinal, se codificó respetando el orden natural de los niveles educativos y luego se normalizó también en el rango [0,1], asegurando una contribución proporcional a la distancia total.

En cuanto a las variables categóricas nominales (workclass, marital_status, occupation, relationship, race, native_country), no se normalizan ni se codifican numéricamente. En la distancia de Gower se comparan por igualdad o diferencia: si dos observaciones comparten el mismo valor (por ejemplo, el mismo estado civil), la distancia en esa variable es 0; si difieren, la distancia es 1.

Por último, la variable sex, considerada binaria simétrica, asigna igual peso a ambas categorías (Male/Female) dentro del cálculo.

Este procesamiento integral permitió que cada tipo de variable aportara de manera equilibrada a la medida de disimilitud, preservando el significado semántico de los datos y evitando redundancias o sesgos en el análisis.

### 2.3 Implementación y Validación

Durante la validación con un subconjunto reducido de seis registros, la matriz de distancias obtenida cumplió con las propiedades esperadas: simetría, diagonal nula y valores dentro del rango [0,1].
Los resultados reflejaron coherencia semántica: las observaciones con características similares presentaron distancias bajas, mientras que aquellas con perfiles contrastantes mostraron distancias altas.

Los valores de distancia muestran coherencia semántica: individuos con características similares presentan distancias bajas (0.1779-0.2262), mientras que perfiles muy diferentes exhiben distancias altas (0.3451-0.4357).

### 2.4 Análisis de Matrices de Distancias

Al calcular la matriz completa para una muestra de 200 observaciones, se obtuvo una distribución de distancias con media 0.341 y desviación estándar 0.12, concentrada mayormente entre 0.25 y 0.45.
Esto indica que la mayoría de los individuos presenta diferencias moderadas entre sí, con una dispersión que refleja la diversidad sociodemográfica del conjunto.
La comparación con el dataset original (que incluía valores faltantes) mostró resultados prácticamente idénticos, confirmando la estabilidad del método.

### 2.5 Comparación: Dataset Limpio vs Con Faltantes

#### 2.5.1 Análisis Estadístico Comparativo

La comparación entre ambas matrices reveló diferencias mínimas pero estadísticamente significativas:

**Diferencias en las Medidas Centrales:**
- **Diferencia en la media:** 0.0021 (0.62% de la media del dataset limpio)
- **Diferencia en la mediana:** 0.0013 (0.37% de la mediana del dataset limpio)
- **Diferencia en la desviación estándar:** -0.0031 (-2.59% de la desviación estándar del dataset limpio)

**Correlación entre Matrices:**
La correlación de Pearson entre las dos matrices fue de 0.9834, indicando una relación muy fuerte y confirmando que el manejo de valores faltantes por parte de la distancia de Gower preserva la estructura fundamental de las relaciones entre observaciones.

#### 2.5.2 Análisis de Casos Extremos

**Diferencias Significativas:**
- **Mayor diferencia absoluta:** 0.1770 (1.34% de los pares)
- **Diferencias > 0.1:** 267 de 19,900 pares (1.34%)
- **Rango de diferencias:** [-0.1065, 0.1770]

El análisis de casos extremos reveló que solo el 1.34% de los pares de observaciones presentó diferencias significativas (>0.1) entre las dos versiones del dataset. Esto confirma la robustez de la distancia de Gower ante la presencia de valores faltantes.

### 2.6 Interpretación de Resultados

La distribución de las distancias muestra que la mayoría de los individuos poseen perfiles socioeconómicos moderadamente similares, con valores medios alrededor de 0.35.
Las distancias más bajas (<0.2) representan grupos homogéneos, posiblemente asociados a perfiles laborales o educativos similares, mientras que las más altas (>0.6) reflejan subpoblaciones con diferencias marcadas, coherentes con las desigualdades observadas en el análisis descriptivo.
La comparación entre datasets confirma que la distancia de Gower preserva la coherencia estructural y semántica de los datos, incluso cuando existen ausencias parciales en algunas variables.

### 2.7 Conclusiones del Ejercicio 2

La aplicación de la distancia de Gower al dataset Adult Census demostró su eficacia y estabilidad como medida de disimilitud para datos mixtos.
El procedimiento implementado permitió incorporar todas las variables disponibles, manejando correctamente tanto la diversidad de tipos de datos como la presencia de valores faltantes.
Las matrices de distancias obtenidas fueron coherentes, simétricas y estadísticamente consistentes, evidenciando que Gower preserva la estructura relacional del conjunto.
En consecuencia, esta implementación proporciona una base metodológica sólida para el uso posterior de algoritmos de clustering como Agglomerative Clustering, posibilitando agrupaciones más representativas e interpretables de los patrones socioeconómicos presentes en la población analizada.

