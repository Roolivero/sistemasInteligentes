# PROYECTO DE AGRUPAMIENTO 

## Tema: Implementación y evaluación de clustering con el algoritmo K-means en el dataset Adult (UCI Census Income)

---

## 1. Análisis Estadístico Descriptivo del Dataset Adult Census

### 1.1 Introducción y Contexto
El presente trabajo se enmarca en el análisis de datos socioeconómicos del dataset Adult Income, con el objetivo de explorar las posibles desigualdades laborales y de ingresos en función de características demográficas. En particular, se busca identificar patrones de agrupamiento entre individuos según su raza y género, considerando su ocupación y nivel de ingresos. Este enfoque permite examinar si ciertos grupos poblacionales presentan una mayor concentración en determinadas categorías ocupacionales o rangos salariales, lo cual podría reflejar diferencias estructurales en el mercado laboral. Para garantizar la validez poblacional de los resultados, se incorpora la variable fnlwgt únicamente en la fase interpretativa del análisis, utilizándola como ponderador muestral que refleja la representatividad real de cada registro dentro de la población total, sin intervenir en el proceso de agrupamiento ni en los cálculos descriptivos principales.

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
- `fnlwgt`: Peso muestral para análisis ponderado (cuantitativa continua)

**Variables Categóricas:**
- `workclass`: Clase de trabajo (cualitativa nominal)
- `education`: Nivel educativo (cualitativa ordinal)
- `marital_status`: Estado civil (cualitativa nominal)
- `occupation`: Ocupación (cualitativa nominal)
- `relationship`: Relación familiar (cualitativa nominal)
- `race`: Raza (cualitativa nominal)
- `sex`: Sexo (cualitativa nominal binaria)
- `native_country`: País de origen (cualitativa nominal)

**Decisión Metodológica:** Se incluyo la variable `fnlwgt` (final weight) del análisis, ya que representa el peso muestral asignado a cada registro, indicando cuántas personas reales de la población están representadas por ese individuo en la muestra.
Aunque no describe una característica personal, su presencia es necesaria porque permite ajustar los resultados del análisis a la estructura poblacional real. Sin esta variable, las proporciones y medias calculadas reflejarían solo la composición de la muestra, no la de la población de referencia.
Por ello, fnlwgt se mantiene en el dataset para ponderar resultados en etapas de interpretación, asegurando que los análisis reflejen correctamente la representatividad poblacional, aun cuando no se use en el EDA ni en los modelos predictivos.

- **Análisis no ponderado**: Proporciones basadas en la muestra original (32,561 observaciones)
- **Análisis ponderado**: Proporciones ajustadas por `fnlwgt` para reflejar la representatividad poblacional

### 1.2.2 Análisis de Valores Faltantes

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

En cuanto a la variable education_num, su valor promedio (10,08) y mediano (10) indican que la mayoría de los individuos alcanzó un nivel educativo correspondiente a la categoría "Some-college", según la codificación del dataset Adult Census. Esto representa personas que han completado la educación secundaria y cursado parcialmente estudios terciarios o universitarios, sin haber obtenido un título formal.

Las ganancias y pérdidas de capital presentan medias de 1.077,65 y 87,30 dólares respectivamente, mientras que sus medianas son cero, evidenciando una fuerte asimetría positiva: la mayoría de los individuos no registra operaciones de capital, aunque un pequeño grupo concentra valores elevados.

El promedio de horas trabajadas por semana (40,44) y su mediana (40) indican una jornada laboral típica a tiempo completo.

En cuanto a la variable fnlwgt, su media (189.778,37) y mediana (178.356,00) indican la distribución de los pesos muestrales asignados a cada observación, con una moda de 123.011, reflejando la representatividad poblacional de cada registro en la muestra.

Finalmente, el 24,08% de los individuos reporta ingresos superiores a 50.000 dólares anuales, lo cual evidencia una marcada desigualdad en la distribución del ingreso.

#### 1.3.2 Medidas de Dispersión

Las medidas de dispersión evidencian la variabilidad de las observaciones. La edad muestra un rango amplio (17 a 90 años) y una desviación estándar de 13,64, indicando una diversidad etaria considerable.

Los años de educación presentan menor dispersión (DE = 2,57), reflejando cierta homogeneidad educativa dentro del conjunto.

Las ganancias y pérdidas de capital exhiben alta dispersión (DE = 7.385,29 y 402,96 respectivamente), lo que refuerza la presencia de valores extremos asociados a individuos con inversiones o pérdidas significativas.

Por su parte, las horas trabajadas por semana muestran una desviación estándar de 12,35, que evidencia variabilidad en los regímenes laborales (empleos de tiempo parcial, completo o con horas extraordinarias).

La variable fnlwgt presenta una desviación estándar de 105.549,98, con un coeficiente de variación del 55,62%, indicando una alta variabilidad en los pesos muestrales que refleja la diversidad en la representatividad poblacional de las observaciones.

#### 1.3.3 Análisis de Outliers

El análisis mediante boxplots permitió identificar valores atípicos en distintas magnitudes.

Las variables capital_gain (8,33%), capital_loss (4,67%) y especialmente hours_per_week (27,66%) concentran una proporción considerable de outliers.

La variable hours_per_week presenta la mayor proporción de valores atípicos, lo que evidencia una alta variabilidad en las horas trabajadas. Este comportamiento puede atribuirse a la existencia de diferentes modalidades laborales, tales como empleos de tiempo parcial, tiempo completo y con horas extraordinarias, reflejando la diversidad en las condiciones de empleo dentro de la muestra.

Por su parte, los outliers observados en capital_gain y capital_loss corresponden a una minoría de individuos con movimientos de capital significativamente superiores al promedio.

Finalmente, la baja proporción de valores atípicos en age (0,44%) y education_num (3,68%) indica estabilidad en las dimensiones demográficas y educativas.

La variable fnlwgt presenta 992 outliers (3,05%), concentrados en el rango superior de los pesos muestrales, lo que indica la presencia de observaciones con mayor representatividad poblacional que el promedio.

### 1.4 Análisis de Variables Categóricas

#### 1.4.1 Distribución Demográfica

**Distribución por Sexo:**
- Masculino: 66,92% (21.790 individuos)
- Femenino: 33,08% (10.771 individuos)

La muestra presenta una mayor proporción de hombres que de mujeres, lo cual podría incidir en la distribución de ingresos y ocupaciones observadas, especialmente en contextos donde existen diferencias estructurales en la inserción laboral y las oportunidades económicas por género.

**Distribución por Ingresos:**
- ≤50K: 75,92% (24.720 individuos)
- >50K: 24,08% (7.841 individuos)

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

### 1.7 Análisis de Ponderaciones y Representatividad Poblacional

#### 1.7.1 Metodología de Análisis Ponderado

Para garantizar la validez poblacional de los resultados, se implementó un análisis comparativo entre proporciones calculadas con y sin ponderación por `fnlwgt`. La ponderación permite ajustar los resultados para reflejar la representatividad real de cada grupo en la población, identificando sesgos de muestreo que pueden distorsionar las interpretaciones sobre las desigualdades estructurales.

#### 1.7.2 Impacto de la Ponderación en las Desigualdades por Género

El análisis ponderado revela diferencias significativas entre las proporciones calculadas con y sin ponderación por `fnlwgt`:

**Resultados por Sexo:**
- **Mujeres**: 10.95% (no ponderado) → 10.82% (ponderado) = -1.11% de diferencia
- **Hombres**: 30.57% (no ponderado) → 30.10% (ponderado) = -1.57% de diferencia

**Interpretación:** Ambos géneros están ligeramente sub-representados en la muestra, con los hombres mostrando mayor sub-representación. La brecha de género en ingresos altos se mantiene prácticamente igual (19.62% vs 19.28%), indicando una desigualdad estructural consistente independientemente del método de cálculo.

#### 1.7.3 Desigualdades Raciales y Representatividad Muestral

Los resultados por raza muestran patrones más complejos de representatividad:

**Resultados (ordenados por magnitud de diferencia):**
1. **Amer-Indian-Eskimo**: 11.58% → 12.44% = +7.44% (sobre-representados en muestra)
2. **Asian-Pac-Islander**: 26.56% → 27.62% = +3.97% (sobre-representados en muestra)
3. **Black**: 12.39% → 12.83% = +3.58% (sobre-representados en muestra)
4. **Other**: 9.23% → 9.07% = -1.63% (sub-representados en muestra)
5. **White**: 25.59% → 25.48% = -0.43% (sub-representados en muestra)

**Interpretación:** Los grupos raciales minoritarios (Amer-Indian-Eskimo, Asian-Pac-Islander, Black) están sobre-representados en la muestra, mientras que White y Other están sub-representados. Esto sugiere que la muestra incluye desproporcionadamente a miembros de minorías raciales con mayor probabilidad de tener ingresos altos.

#### 1.7.4 Segregación Ocupacional y Patrones de Concentración

El análisis ponderado revela patrones de segregación ocupacional significativos:

**Concentración Ocupacional por Género:**
- **Mujeres**: Índice de concentración = 0.1590 (mayor concentración)
- **Hombres**: Índice de concentración = 0.1117 (mayor diversidad)

**Patrones de Segregación:**
- Las mujeres muestran mayor concentración en ocupaciones de servicios y administrativas
- Los hombres están más distribuidos pero dominan ocupaciones de manufactura, construcción y gerenciales
- Esta segregación horizontal contribuye a las diferencias salariales observadas

#### 1.7.5 Análisis Trivariado: Intersección de Desigualdades

El análisis de la intersección entre género, raza e ingresos revela patrones complejos de desigualdad:

**Combinaciones con Mayor Proporción de Ingresos Altos:**
- **Hombres Asian-Pac-Islander**: 34.5% de ingresos altos
- **Hombres White**: 31.4% de ingresos altos

**Combinaciones con Menor Proporción de Ingresos Altos:**
- **Mujeres Other**: 5.1% de ingresos altos
- **Mujeres Black**: 5.6% de ingresos altos

**Diferencia Máxima:** 29.4 puntos porcentuales entre la combinación con mayor y menor proporción de ingresos altos.

#### 1.7.6 Implicaciones Metodológicas y Estructurales

**Sesgos de Muestreo Identificados:**
- **Sobre-representación**: Grupos raciales minoritarios, niveles educativos bajos, ocupaciones militares
- **Sub-representación**: Población blanca, ocupaciones agrícolas y de manufactura, servicio doméstico privado

**Impacto en la Interpretación:**
- Las desigualdades estructurales persisten independientemente del método de cálculo
- La ponderación revela que ciertos grupos están desproporcionadamente representados en la muestra
- Los patrones de desigualdad observados pueden ser aún más pronunciados a nivel poblacional real

**Validación de Patrones de Agrupamiento:**
- Los análisis ponderados confirman la existencia de patrones sistemáticos de agrupamiento por género, raza y ocupación
- Las desigualdades identificadas reflejan verdaderas diferencias estructurales en el acceso a oportunidades económicas
- La segregación ocupacional horizontal contribuye significativamente a las brechas salariales observadas

#### 1.7.7 Conclusiones del Análisis Ponderado

El análisis ponderado revela que las desigualdades estructurales en el mercado laboral estadounidense de 1994 persisten independientemente del método de cálculo, pero con magnitudes ajustadas que reflejan la realidad poblacional. La implementación de la ponderación no solo corrige sesgos de muestreo, sino que proporciona una base más sólida para identificar patrones de agrupamiento y concentración ocupacional que reflejan verdaderas diferencias estructurales en el acceso a oportunidades económicas.

Los hallazgos confirman la existencia de brechas significativas por género, raza y nivel educativo, mientras que la ponderación revela que ciertos grupos están desproporcionadamente representados en la muestra, sugiriendo que los patrones de desigualdad observados pueden ser aún más pronunciados a nivel poblacional real.

### 1.8 Respuestas a las Preguntas Guías

#### 1.8.1 ¿Qué variables numéricas y categóricas consideraste para el análisis?

Se consideraron todas las variables del dataset Adult Census, clasificándolas en:

**Variables Numéricas (7):** age, education_num, capital_gain, capital_loss, hours_per_week, income_binary, fnlwgt

**Variables Categóricas (8):** workclass, education, marital_status, occupation, relationship, race, sex, native_country

**Decisión Metodológica:** En este estudio se decidió incluir la variable `fnlwgt` en el análisis descriptivo completo, ya que representa información valiosa sobre la representatividad poblacional de cada observación. Aunque no describe características individuales, su inclusión permite comprender la estructura muestral y realizar análisis ponderados que garantizan la validez poblacional de los resultados. Esta decisión se fundamenta en la necesidad de identificar patrones de agrupamiento demográfico que reflejen tanto la composición de la muestra como la estructura poblacional real.

#### 1.8.2 ¿Qué impacto tienen los valores faltantes en K-means?

Los valores faltantes afectan negativamente el desempeño de K-means debido a que el algoritmo no puede operar con datos incompletos, ya que requiere calcular distancias euclidianas entre todos los registros. Su presencia puede distorsionar los centroides y reducir la calidad del clustering.

Eliminar observaciones con valores nulos implica una pérdida de información y potencial sesgo de selección. Por ello, se aplicó imputación mediante la moda en las variables categóricas, manteniendo la coherencia y completitud del conjunto de datos.

#### 1.8.3 ¿Qué limitación supone ignorar las variables categóricas?

Ignorar las variables categóricas en K-means implica una pérdida significativa de información semántica, especialmente en atributos socioeconómicos como marital_status, workclass o education.

Esto puede derivar en clusters incompletos o poco representativos, donde individuos con perfiles diferentes se agrupan por similitudes numéricas superficiales.

Dado que la distancia euclidiana no refleja adecuadamente las diferencias entre categorías, se justifica el uso de métodos alternativos como la distancia de Gower y Agglomerative Clustering, que permiten integrar variables mixtas en el análisis.

### 1.9 Conclusiones del Análisis Descriptivo

El análisis descriptivo del dataset Adult Census evidencia un conjunto de datos estructurado y representativo que permite explorar las desigualdades laborales y de ingresos en función de características demográficas. Se observa una marcada desigualdad de ingresos, dado que solo el 24,08% de los individuos percibe más de 50.000 dólares anuales, concentrándose la mayoría en niveles bajos y medios.

Los análisis revelan patrones de agrupamiento demográfico significativos que reflejan diferencias estructurales en el mercado laboral. Se identifican diferencias pronunciadas por género: los hombres tienen 2,8 veces más probabilidades que las mujeres de superar el umbral de ingresos altos. Asimismo, la educación emerge como un factor determinante en la movilidad económica, donde los niveles académicos más altos —Doctorate, Prof-school y Masters— presentan una mayor proporción de individuos con ingresos elevados.

Los análisis de ponderación por `fnlwgt` confirman la existencia de patrones de segregación ocupacional que contribuyen a las desigualdades observadas. Las mujeres muestran mayor concentración en ocupaciones de servicios y administrativas, mientras que los hombres dominan ocupaciones de manufactura, construcción y gerenciales. Esta segregación horizontal evidencia que ciertos grupos poblacionales presentan una mayor concentración en determinadas categorías ocupacionales, lo cual refleja diferencias estructurales en el acceso a oportunidades laborales.

En términos económicos, las variables capital_gain y capital_loss muestran alta variabilidad y predominio de valores nulos, reflejando una participación desigual en actividades de inversión. La variable `fnlwgt` presenta una alta variabilidad (CV: 55,62%), indicando la diversidad en la representatividad poblacional de las observaciones, lo cual es fundamental para garantizar la validez de los análisis interpretativos.

Los análisis trivariados revelan que la intersección entre género, raza e ingresos amplifica las desigualdades observadas, con diferencias de hasta 29,4 puntos porcentuales entre las combinaciones demográficas con mayor y menor proporción de ingresos altos. Esto confirma que las características demográficas interactúan de manera compleja para determinar los patrones de agrupamiento en el mercado laboral.

Finalmente, la calidad del dataset es adecuada, con un 7,37% de valores faltantes, lo que permite aplicar estrategias de limpieza sin comprometer la representatividad de la muestra. Los análisis ponderados confirman que las desigualdades estructurales persisten independientemente del método de cálculo, proporcionando una base sólida para identificar patrones de agrupamiento entre individuos según su raza y género, considerando su ocupación y nivel de ingresos, lo cual constituye el fundamento para el desarrollo de técnicas de clustering que permitan examinar las diferencias estructurales en el mercado laboral estadounidense de 1994.

