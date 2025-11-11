# Pasos - Parte 1

*En esta fase se evalua la probabilidad inicial*

## Analisis de los datos

### Objetivo de esta fase:
Entender qué se quiere predecir, qué variables se tienen y cómo están estructurados los datos.

1) Verificar la estructura y los tipos de las variables. (son 31) 

**Observacion sobre las variables:** 
    El dataset contiene 31 columnas en total, de las cuales 30 corresponden a las características o atributos utilizados para describir los sitios web (por ejemplo, longitud de la URL, uso de SSL, edad del dominio, etc.). La última columna, denominada Result, es la variable objetivo que indica si el sitio es phishing (1) o legítimo (-1).
    En el análisis exploratorio inicial, **Result** debe incluirse para revisar su distribución y balance de clases, pero **no debe usarse** como variable predictora en los modelos; se emplea únicamente como etiqueta o variable de salida durante el entrenamiento y evaluación.

2) Separar features en binarias y ordinales.

**Observacion sobre las variables binarias y ordinales**: 
    Las variables del dataset son discretas y codificadas con valores -1, 0 y 1, que representan niveles de sospecha o legitimidad. Según su rango de valores, se dividen en dos grupos: binarias, cuando solo toman dos valores (-1 y 1), y ordinales, cuando pueden tomar tres valores (-1, 0 y 1), indicando distintos grados de riesgo.

3) Verificar que no hay valores faltantes (hay que dejarlo demostrado)

4)**Realizar un EDA básico:** En este punto no se realiza un EDA estadístico profundo, ya que todas las variables son discretas y acotadas con valores predefinidos (-1, 0, 1).
El objetivo es únicamente verificar la estructura y consistencia de los datos.

* **df.info()** Muestra información estructural del DataFrame: cantidad de filas y columnas,nombres de las columnas, tipo de dato (int, float, object, etc.), si hay valores nulos o faltantes.
*OBS:* Te permite ver si los datos cargaron bien, si las columnas están con el tipo correcto y si falta algo.

- Analizar la distribución de la variable Result para conocer la proporción de sitios phishing y legítimos.

- revisión de valores únicos por columna (los valores distintos que aparecen en cada columna.
Sirve para confirmar que todas las variables usan la misma codificación (-1, 0, 1) que define el dataset. No se hace para analizar, sino como verificación de integridad (una especie de control de calidad de los datos).)

