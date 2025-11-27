# Proyecto de detección de objetos

## Introducción

En contextos de obra y construcción, el uso adecuado de cascos de seguridad constituye una de las principales barreras de protección frente a accidentes laborales. La detección automática de cascos y personas en imágenes de vigilancia se presenta como una herramienta potencialmente útil para asistir a los responsables de seguridad, siempre que el sistema exhiba niveles adecuados de precisión y, especialmente, de sensibilidad ante situaciones de riesgo.

En este trabajo se estudia el comportamiento de un modelo de detección de objetos basado en la arquitectura MobileNetV2 con una cabeza de detección tipo RetinaNet, aplicado al problema de detección de cascos de seguridad. Se analiza tanto la versión en punto flotante (float) como una variante cuantizada entrenada mediante Quantization Aware Training (QAT), orientada a su despliegue en dispositivos móviles.

El foco del análisis se sitúa en dos aspectos complementarios. Por un lado, se estudian las métricas estándar de detección (AP y AR en el estilo COCO, para distintos umbrales de IoU y escalas de objeto). Por otro lado, se discuten dichas métricas en relación con el objetivo de seguridad: minimizar la cantidad de trabajadores sin casco que el sistema deja sin detectar (falsos negativos), incluso a costa de tolerar cierta imprecisión en la localización o un número moderado de falsos positivos.

## Metodología

El modelo se entrena con un conjunto de imágenes anotadas de entornos de obra, que incluye cascos, personas y cabezas como clases de interés. Para cada configuración de hiperparámetros, el script produce dos modelos: uno float en precisión de punto flotante y otro cuantizado mediante QAT, exportado en formato TFLite y representativo de un posible despliegue en dispositivos móviles. La evaluación se realiza sobre un conjunto de validación con las métricas COCO habituales: AP@[0.50:0.95] (mAP promedio entre IoU 0.50 y 0.95), AP50 y AP75, AP por escala (APs, APm, APl) y AR tanto por número máximo de detecciones (ARmax1, ARmax10, ARmax100) como por escala (ARs, ARm, ARl).

Con el objetivo de analizar el impacto de las decisiones de entrenamiento sobre la capacidad del modelo para detectar cascos en un escenario de seguridad, se exploran distintas combinaciones de hiperparámetros. Para el análisis final se seleccionan tres configuraciones representativas, que permiten estudiar el compromiso entre precisión, sensibilidad y cuantización. Estas configuraciones se resumen en la Tabla 1.

**Tabla 1 – Configuraciones de entrenamiento analizadas**

| Configuración          | EPOCHS | LEARNING_RATE | BATCH_SIZE | DECAY_STEPS | DECAY_RATE |
| ---------------------- | :----: | :-----------: | :--------: | :---------: | :--------: |
| Base (M_base)          |   30   |      0.15     |      4     |      8      |    0.96    |
| Comparación 1 (M_lr)   |   20   |      0.08     |      4     |      8      |    0.96    |
| Comparación 2 (M_ap75) |   50   |      0.05     |      4     |      16     |    0.98    |

La configuración base (M_base) presenta el mejor compromiso entre precisión global y recall, con el mayor ARmax100 entre las corridas realizadas. La configuración M_lr reduce la tasa de aprendizaje manteniendo el resto de parámetros fijos, para observar el efecto de un entrenamiento menos agresivo. La configuración M_ap75 incrementa el número de épocas, reduce la tasa de aprendizaje y modifica el schedule de decrecimiento del learning rate, buscando mejorar la precisión fina de las cajas (AP75) aun a costa de posibles pérdidas de recall. En todos los casos, el script entrena primero el modelo float y luego aplica QAT sobre la misma configuración, produciendo un par de modelos (float y cuantizado) por cada conjunto de hiperparámetros.

## Resultados

La Tabla 2 sintetiza las métricas principales obtenidas para las tres configuraciones seleccionadas, tanto en su versión float como cuantizada. Los valores corresponden al conjunto de validación y se muestran redondeados a tres decimales.

**Tabla 2 – Métricas COCO para las configuraciones analizadas (float vs cuantizado)**

| Configuración | Modelo     |    AP |  AP50 |  AP75 |   APs |   APm |   APl | ARmax100 |
| :------------ | :--------- | ----: | ----: | ----: | ----: | ----: | ----: | -------: |
| M_base        | Float      | 0.315 | 0.633 | 0.252 | 0.242 | 0.373 | 0.734 |    0.551 |
| M_base        | Cuantizado | 0.137 | 0.346 | 0.075 | 0.115 | 0.137 | 0.608 |    0.346 |
| M_lr          | Float      | 0.280 | 0.609 | 0.258 | 0.214 | 0.295 | 0.695 |    0.463 |
| M_lr          | Cuantizado | 0.126 | 0.363 | 0.057 | 0.053 | 0.136 | 0.489 |    0.301 |
| M_ap75        | Float      | 0.326 | 0.614 | 0.323 | 0.291 | 0.341 | 0.725 |    0.372 |
| M_ap75        | Cuantizado | 0.138 | 0.347 | 0.056 | 0.120 | 0.144 | 0.441 |    0.367 |

En la configuración base (M_base), el modelo float alcanza AP@[0.50:0.95] ≈ 0.315, con AP50 ≈ 0.633 y AP75 ≈ 0.252. El ARmax100 ≈ 0.551 indica que, permitiendo hasta 100 detecciones por imagen, el modelo recupera algo más de la mitad de los objetos relevantes. La precisión por escala revela un desempeño claramente superior en objetos grandes (APl ≈ 0.734) que en objetos pequeños (APs ≈ 0.242. En esta misma configuración, el modelo cuantizado muestra una degradación importante (AP ≈ 0.137, AP50 ≈ 0.346, AP75 ≈ 0.075, ARmax100 ≈ 0.346), lo que refleja una caída notable de precisión y recall pese a las ventajas de tamaño y despliegue en móvil.

La configuración M_lr, con learning rate más bajo y 20 épocas, produce un modelo float con AP ≈ 0.280, AP50 ≈ 0.609, AP75 ≈ 0.258 y ARmax100 ≈ 0.463. En comparación con M_base, se observa una ligera disminución del mAP y de AP50, una mejora marginal en AP75 y una reducción apreciable del recall, sin un beneficio claro en el equilibrio precisión–sensibilidad. La configuración M_ap75, con 50 épocas, learning rate 0.05 y un decay más suave, obtiene el mayor mAP (AP ≈ 0.326) y el AP75 más alto (≈ 0.323), pero reduce ARmax100 a ≈ 0.372, lo que implica que detecta menos objetos en total. En conjunto, las tres configuraciones cuantizadas siguen el mismo patrón: mAP y recall sistemáticamente inferiores a sus respectivas versiones float, con especial degradación en las escalas pequeñas, lo que confirma que la cuantización introduce una penalización relevante que debe valorarse en función de los riesgos aceptables en la aplicación.

### Costos computacionales: tamaño del modelo y tiempos de entrenamiento

Además de las métricas de detección, se compararon los modelos en términos de tiempo de entrenamiento y tamaño aproximado de los pesos. La Tabla 3 resume estos resultados para las tres configuraciones analizadas.

**Tabla 3 – Tiempos de entrenamiento y tamaño aproximado de los pesos**
| Configuración | Modelo | Épocas | Tiempo de entrenamiento | Total params | Tamaño estimado de pesos (MB) |
| :------------ | :----- | :----: | :---------------------- | :----------: | :---------------------------: |
| M_base        | Float  |   30   | 18 min 17 s             |   2 580 424  |             ≈ 9.84            |
| M_base        | QAT    |   30   | 18 min 17 s             |   2 580 424  |             ≈ 9.84            |
| M_lr          | Float  |   20   | 14 min 20 s             |   2 580 424  |             ≈ 9.84            |
| M_lr          | QAT    |   20   | 14 min 20 s             |   2 580 424  |             ≈ 9.84            |
| M_ap75        | Float  |   50   | 23 min 15 s             |   2 580 424  |             ≈ 9.84            |
| M_ap75        | QAT    |   50   | 23 min 15 s             |   2 580 424  |             ≈ 9.84            |

En todos los casos, el número total de parámetros del modelo es el mismo (≈2.58 millones), lo que se refleja en un tamaño estimado de los pesos en torno a 9.84 MB. Esto es coherente con el hecho de que las tres configuraciones comparten arquitectura y difieren únicamente en los hiperparámetros de entrenamiento. La variante QAT introduce una simulación de cuantización durante el entrenamiento, pero no modifica el número de parámetros del modelo; en términos de almacenamiento, la reducción de tamaño se manifiesta principalmente en el modelo TFLite final, que no se midió de manera separada en este trabajo.

En cuanto al tiempo de entrenamiento, se observa una relación aproximadamente proporcional con la cantidad de épocas: la configuración M_lr (20 épocas) requiere alrededor de 14 minutos y 20 segundos, la configuración M_base (30 épocas) unos 18 minutos y 17 segundos, y la configuración M_ap75 (50 épocas) aproximadamente 23 minutos y 15 segundos. Dado que en cada caso el entrenamiento float y el QAT se realizan secuencialmente dentro del mismo script, ambos comparten el mismo tiempo total reportado. Estas diferencias de tiempo son relevantes a la hora de decidir si resulta conveniente entrenar configuraciones más largas orientadas a mejorar marginalmente ciertas métricas, teniendo en cuenta que no siempre se traducen en mejoras significativas desde el punto de vista de la seguridad.

## Discusión

Los resultados permiten extraer una serie de conclusiones sobre el comportamiento del modelo y su adecuación al problema de detectar cascos de seguridad.

En la configuración base, el valor de AP@[0.50:0.95] ≈ 0.315 refleja un desempeño global moderado: el detector identifica una fracción relevante de cascos y personas, pero aún lejos de un escenario de alta confiabilidad. Este comportamiento se aclara al analizar AP50 y AP75. Que AP50 supere 0.6 indica que el modelo ubica correctamente muchos objetos con un criterio de solapamiento relativamente laxo, mientras que AP75, en torno a 0.25 en M_base y ~0.32 en M_ap75, muestra que son muchas menos las detecciones que alcanzan una coincidencia precisa con la anotación.

La diferencia marcada entre AP50 y AP75 sugiere que el modelo captura adecuadamente la presencia de cascos y personas, pero no siempre ajusta con precisión el tamaño y la posición de las bounding boxes. Desde el punto de vista de seguridad, esta limitación es menos grave que la ausencia total de detección, aunque puede afectar tareas posteriores que requieran localización muy exacta (por ejemplo, distinguir con certeza si una persona lleva casco cuando ambos aparecen muy próximos en la imagen).

Un aspecto crítico es la dependencia del desempeño respecto de la escala del objeto. Los valores de APs, APm y APl muestran consistentemente que la detección de objetos grandes es sustancialmente mejor que la de objetos pequeños. En la configuración base, APl ≈ 0.73 mientras que APs ≈ 0.24. Esto sugiere que el sistema es relativamente competente para identificar cascos y personas cercanos a la cámara y de gran tamaño en la imagen, pero falla con mayor frecuencia cuando los trabajadores aparecen lejos o en el fondo de la escena. En un entorno de obra, donde es habitual tener múltiples personas distribuidas en profundidad, esta limitación se traduce en un riesgo concreto: los trabajadores más alejados tienen una probabilidad considerable de no ser detectados.

El análisis del recall por número máximo de detecciones refuerza este diagnóstico. El salto entre ARmax1 y ARmax10 es pronunciado, lo que indica que permitir varias detecciones por imagen mejora sustancialmente la capacidad de recuperar objetos. Sin embargo, de ARmax10 a ARmax100 la mejora es muy modesta, lo que sugiere que, más allá de cierto punto, las detecciones adicionales aportan poco recall útil y tienden a ser redundantes o de peor calidad. La relación entre AR y AP muestra además que, aunque existen falsos positivos, el principal problema del modelo reside en los falsos negativos: un porcentaje importante de cascos y personas no son detectados en absoluto, en particular en la escala small.

Las configuraciones de comparación ayudan a entender mejor el impacto de las decisiones de entrenamiento. La configuración M_lr, con learning rate reducido y menos épocas, conduce a un descenso del recall y a cambios modestos en AP50 y AP75, sin aportar un beneficio claro que justifique abandonar la configuración base desde la perspectiva de seguridad. La configuración M_ap75, en cambio, mejora de manera visible AP75 y el mAP global, pero reduce ARmax100 a valores cercanos a 0.37. En otros términos, se obtiene un detector capaz de localizar con mayor precisión un subconjunto de cascos y personas, al precio de dejar sin detectar un número mayor de ellos. En un sistema destinado a monitorear el uso de elementos de protección personal, este compromiso no resulta favorable; es preferible aceptar cajas moderadamente imprecisas, pero con mayor probabilidad de que cada trabajador presente en la escena sea detectado.

La comparación entre modelos float y cuantizados añade una dimensión adicional. En todas las configuraciones, la cuantización implica una caída de mAP y de AR, con impacto particularmente notable en objetos pequeños. Su ventaja principal es la reducción del tamaño del modelo y la posibilidad de ejecución en dispositivos con recursos limitados, como teléfonos o cámaras inteligentes. No obstante, los resultados muestran que, en su estado actual, la versión cuantizada amplifica precisamente la debilidad más crítica del sistema: la incapacidad de detectar con suficiente fiabilidad a los trabajadores más alejados o con cascos de tamaño pequeño en la imagen.

Los patrones observados sugieren varias líneas de mejora. Sería deseable reforzar la representación de objetos pequeños mediante ajustes en la resolución de entrada, en los parámetros de la cabeza de detección (por ejemplo, anchors) y en las estrategias de augmentación de datos. Asimismo, una colección de datos más amplia y equilibrada, con mayor cantidad de ejemplos de cascos pequeños y escenas densas, podría ayudar a reducir la brecha de desempeño entre escalas. En términos de entrenamiento, resultaría razonable seguir explorando schedules de learning rate y criterios de parada temprana que prioricen el aumento del recall sin degradar en exceso la precisión.

## Conclusiones

El estudio realizado muestra que un detector basado en MobileNetV2 y entrenado sobre un conjunto de imágenes de obra alcanza un desempeño moderado en la detección de cascos y personas. En la mejor configuración identificada (M_base, 30 épocas, learning rate 0.15), el modelo float obtiene un mAP cercano a 0.31, un AP50 superior a 0.6 y un ARmax100 en torno a 0.55, lo que indica que el sistema identifica una fracción relevante de cascos y trabajadores, especialmente cuando los objetos son de gran tamaño y se encuentran próximos a la cámara. Sin embargo, el rendimiento se degrada de forma sensible en objetos pequeños, y la versión cuantizada, necesaria para el despliegue en dispositivos móviles, reduce tanto la precisión como el recall, con un impacto particularmente marcado en la detección de cascos lejanos. Además, las configuraciones que mejoran la precisión de las cajas (AP75) lo hacen a costa de disminuir el recall, incrementando el número de trabajadores que pasan desapercibidos para el sistema.

Desde la perspectiva de la seguridad laboral, el tipo de error más preocupante es el falso negativo, es decir, la ausencia de detección de una persona sin casco. Los resultados evidencian que, en su estado actual, el sistema deja de detectar una proporción significativa de cascos y personas, en particular en las escalas pequeñas, por lo que no puede considerarse un mecanismo autónomo de vigilancia confiable. Su papel más adecuado, en esta etapa, es el de herramienta de apoyo que complemente la supervisión humana, proporcionando alertas sobre muchas situaciones evidentes, pero sin reemplazar el criterio de los responsables de seguridad.

En síntesis, el trabajo demuestra la viabilidad técnica de aplicar técnicas de detección de objetos y cuantización para asistir en el monitoreo del uso de cascos de seguridad, pero también pone de manifiesto las limitaciones actuales del modelo y las líneas de trabajo necesarias para su mejora. Incrementar la capacidad de detección en objetos pequeños, reducir la brecha entre los modelos float y cuantizados y diseñar estrategias de entrenamiento orientadas explícitamente a maximizar el recall en contextos de riesgo aparecen como pasos imprescindibles para avanzar hacia un sistema de vigilancia automatizada que pueda considerarse robusto desde el punto de vista de la seguridad en obra.