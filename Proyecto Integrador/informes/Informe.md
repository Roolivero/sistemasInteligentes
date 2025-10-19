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
- Private: 75,34% (24.532 individuos)
- Self-emp-not-inc: 7,80% (2.541 individuos)
- Local-gov: 6,43% (2.093 individuos)
- State-gov: 3,99% (1.298 individuos)
- Self-emp-inc: 3,43% (1.116 individuos)
- Federal-gov: 2,95% (960 individuos)
- Without-pay: 0,04% (14 individuos)
- Never-worked: 0,02% (7 individuos)

En términos ocupacionales, la mayoría de los individuos trabaja en el sector privado (75,34%), seguido por los autoempleados (7,80%) y empleados de gobiernos locales o estatales. Esto sugiere una estructura laboral concentrada en el ámbito privado con participación limitada del sector público.

**Nivel Educativo (education):**
- HS-grad: 32,25% (10.501 individuos)
- Some-college: 22,39% (7.291 individuos)
- Bachelors: 16,45% (5.355 individuos)
- Masters: 5,29% (1.723 individuos)
- Assoc-voc: 4,24% (1.382 individuos)
- 11th: 3,61% (1.175 individuos)
- Assoc-acdm: 3,28% (1.067 individuos)
- 10th: 2,87% (933 individuos)
- 7th-8th: 1,98% (646 individuos)
- Prof-school: 1,77% (576 individuos)
- 9th: 1,58% (514 individuos)
- 12th: 1,33% (433 individuos)
- Doctorate: 1,27% (413 individuos)
- 5th-6th: 1,02% (333 individuos)
- 1st-4th: 0,52% (168 individuos)
- Preschool: 0,16% (51 individuos)

Los resultados evidencian que los niveles educativos más frecuentes corresponden a HS-grad (32,25%) y Some-college (22,39%), lo cual refleja que una gran proporción de la población completó la educación secundaria o cursó parcialmente estudios superiores.
Los niveles universitarios y de posgrado (Bachelors, Masters, Doctorate) son minoritarios, aunque, como se analizará posteriormente, estos grupos presentan una mayor proporción de ingresos altos, confirmando la relevancia de la educación como factor socioeconómico.

**Estado Civil (marital_status):**
- Married-civ-spouse: 46,00% (14.976 individuos)
- Never-married: 32,81% (10.683 individuos)
- Divorced: 13,64% (4.443 individuos)
- Separated: 3,15% (1.025 individuos)
- Widowed: 3,05% (993 individuos)
- Married-spouse-absent: 1,28% (418 individuos)
- Married-AF-spouse: 0,07% (23 individuos)

La estructura marital revela que el 46% de los individuos está casado con cónyuge presente, seguido por quienes nunca se casaron (32,81%) y los divorciados (13,64%). En conjunto, estas tres categorías agrupan más del 90% de la muestra, lo que sugiere una población predominantemente casada o soltera, con menor representación de personas separadas o viudas.

**Ocupación (occupation):**
- Prof-specialty: 18,37% (5.983 individuos)
- Craft-repair: 12,59% (4.099 individuos)
- Exec-managerial: 12,49% (4.066 individuos)
- Adm-clerical: 11,58% (3.770 individuos)
- Sales: 11,21% (3.650 individuos)
- Other-service: 10,12% (3.295 individuos)
- Machine-op-inspct: 6,15% (2.002 individuos)
- Transport-moving: 4,90% (1.597 individuos)
- Handlers-cleaners: 4,21% (1.370 individuos)
- Farming-fishing: 3,05% (994 individuos)
- Tech-support: 2,85% (928 individuos)
- Protective-serv: 1,99% (649 individuos)
- Priv-house-serv: 0,46% (149 individuos)
- Armed-Forces: 0,03% (9 individuos)

La distribución ocupacional muestra una diversificación moderada del mercado laboral. Las categorías más frecuentes son profesiones especializadas (18,37%), trabajos técnicos o de reparación (12,59%) y puestos ejecutivos o administrativos (12,49%).
Esto sugiere una estructura laboral con predominio de ocupaciones calificadas y técnicas, aunque también se observa participación de sectores de servicios y tareas manuales.


**Relación Familiar (relationship):**
- Husband: 40,51% (13.193 individuos)
- Not-in-family: 25,50% (8.305 individuos)
- Own-child: 15,56% (5.068 individuos)
- Unmarried: 10,58% (3.446 individuos)
- Wife: 4,82% (1.568 individuos)
- Other-relative: 3,01% (981 individuos)

La estructura familiar se caracteriza por una mayor proporción de jefes de hogar masculinos (Husband, 40,51%), seguida por individuos que no pertenecen a un núcleo familiar (25,50%) y por hijos dentro del hogar (15,56%).
Estos datos reflejan una muestra compuesta principalmente por adultos casados y cabezas de familia, lo cual puede relacionarse con los patrones de ingresos y empleo observados.

**Raza (race):**
- White: 85,50% (27.834 individuos)
- Black: 9,60% (3.125 individuos)
- Asian-Pac-Islander: 2,85% (927 individuos)
- Amer-Indian-Eskimo: 0,94% (305 individuos)
- Other: 1,11% (370 individuos)

La composición racial del conjunto de datos está dominada por individuos de raza blanca (85,50%), seguidos por personas de raza negra (9,60%) y asiáticas o isleñas del Pacífico (2,85%). Esta distribución es coherente con la estructura demográfica de Estados Unidos en el período de referencia (1994).

**País de Origen (native_country):**
- United-States: 89,60% (29.175 individuos)
- Mexico: 1,93% (629 individuos)
- Philippines: 0,93% (302 individuos)
- Germany: 0,50% (162 individuos)
- Canada: 0,42% (137 individuos)
- Puerto-Rico: 0,40% (129 individuos)
- El-Salvador: 0,37% (120 individuos)
- India: 0,36% (118 individuos)
- Cuba: 0,35% (115 individuos)
- England: 0,33% (108 individuos)
- Jamaica: 0,32% (103 individuos)
- South: 0,30% (98 individuos)
- China: 0,29% (95 individuos)
- Italy: 0,28% (90 individuos)
- Dominican-Republic: 0,26% (85 individuos)
- Vietnam: 0,25% (82 individuos)
- Guatemala: 0,24% (78 individuos)
- Japan: 0,24% (77 individuos)
- Poland: 0,23% (75 individuos)
- Columbia: 0,22% (72 individuos)
- Taiwan: 0,22% (71 individuos)
- Haiti: 0,21% (69 individuos)
- Iran: 0,21% (68 individuos)
- Portugal: 0,20% (66 individuos)
- Nicaragua: 0,19% (62 individuos)
- Peru: 0,19% (61 individuos)
- France: 0,18% (59 individuos)
- Greece: 0,18% (58 individuos)
- Ecuador: 0,17% (56 individuos)
- Ireland: 0,17% (55 individuos)
- Hong: 0,16% (52 individuos)
- Cambodia: 0,15% (49 individuos)
- Trinadad&Tobago: 0,15% (48 individuos)
- Laos: 0,14% (46 individuos)
- Thailand: 0,14% (45 individuos)
- Yugoslavia: 0,14% (45 individuos)
- Outlying-US(Guam-USVI-etc): 0,13% (42 individuos)
- Hungary: 0,12% (39 individuos)
- Honduras: 0,12% (38 individuos)
- Scotland: 0,11% (36 individuos)
- Holand-Netherlands: 0,10% (33 individuos)

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

Los valores faltantes tienen un impacto negativo directo en K-means porque:

1. **Incompatibilidad algorítmica:** K-means no puede operar con datos incompletos, ya que requiere calcular distancias euclidianas entre todos los puntos.

2. **Distorsión de centroides:** Los valores faltantes pueden sesgar la ubicación de los centroides, afectando la calidad del clustering.

3. **Pérdida de información:** Eliminar filas con valores faltantes reduce el tamaño de la muestra y puede introducir sesgos de selección.

4. **Estrategias de tratamiento:** Se implementó rellenado con moda para variables categóricas, preservando la integridad del dataset.

#### 1.7.3 ¿Qué limitación supone ignorar las variables categóricas?

Ignorar las variables categóricas en K-means presenta las siguientes limitaciones:

1. **Pérdida de información semántica:** Variables como marital_status, workclass y education aportan contexto socioeconómico crucial.

2. **Clusters incompletos:** Personas con perfiles socioeconómicos muy distintos pueden agruparse incorrectamente si sus valores numéricos son similares.

3. **Interpretación limitada:** Los clusters resultantes no reflejan patrones sociolaborales o educativos, que son fundamentales en el dataset Adult.

4. **Distancia no representativa:** La distancia euclidiana entre variables numéricas no captura la "realidad social" de las diferencias categóricas.

5. **Justificación metodológica:** Esta limitación justifica la implementación posterior de la distancia de Gower y AgglomerativeClustering, que pueden manejar variables mixtas.

### 1.8 Conclusiones del Análisis Descriptivo

El análisis estadístico descriptivo del dataset Adult Census revela un conjunto de datos bien estructurado con características demográficas y socioeconómicas diversas. Los principales hallazgos incluyen:

1. **Distribución desigual de ingresos:** Solo el 24.08% de la población gana más de $50K, reflejando desigualdades socioeconómicas.

2. **Desigualdades de género:** Existe una marcada brecha salarial, donde los hombres tienen 2.8 veces más probabilidades de ganar >50K que las mujeres.

3. **Importancia de la educación:** Se observa una correlación clara entre nivel educativo e ingresos, siendo los niveles superiores (Doctorate, Prof-school, Masters) los que presentan mayores probabilidades de altos ingresos.

4. **Variabilidad en variables numéricas:** Las variables capital_gain y capital_loss presentan alta variabilidad con muchos valores en cero, sugiriendo que no todos los individuos tienen inversiones de capital.

5. **Calidad de los datos:** El dataset presenta una estructura sólida con valores faltantes manejables (7.37% total), permitiendo implementar estrategias de limpieza efectivas.

Estos resultados establecen las bases metodológicas necesarias para la implementación posterior del algoritmo K-means y otras técnicas de clustering, proporcionando una comprensión profunda de las características del dataset que guiará las decisiones técnicas en las siguientes fases del proyecto.