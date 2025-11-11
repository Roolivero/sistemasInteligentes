### Plan de reescritura: dos scripts comparativos y conclusiones

Este documento define, en limpio, los pasos para reescribir el flujo de clasificación en dos scripts complementarios y comparables. El objetivo es obtener evidencia sólida para un informe final que justifique la elección del camino con mejor desempeño y mejor equilibrio entre precisión y recall para la clase phishing (-1).

### Objetivo general

Construir dos pipelines evaluados bajo el mismo esquema de datos y validación:
- Script A: usa las 30 features originales y optimiza hiperparámetros del clasificador (modelo “sin selección de features”).
- Script B: reproduce la lógica de `script3` con selección de features basada en Información Mutua integrada al pipeline, optimización de hiperparámetros y ajuste de umbral por F1 de la clase -1.

Ambos se comparan en un marco justo (misma semilla, misma partición 70/15/15 estratificada, mismas métricas, mismo protocolo de evaluación).

### División de datos (común a ambos scripts)

Primero se fija la semilla y se hace una sola partición estratificada del dataset completo en 70% entrenamiento, 15% validación y 15% prueba. Esta partición debe ser idéntica para Script A y Script B, garantizando comparabilidad. Se reporta la distribución de `Result` en cada split para verificar que las proporciones se preservan.

### Script A: 30 features + optimización de hiperparámetros (baseline robusto)

Este script entrena un clasificador sobre todas las columnas predictoras originales (30 features) sin reducción de dimensionalidad previa. La optimización de hiperparámetros se hace con validación cruzada estratificada en entrenamiento y se evalúa con umbral por defecto (0.5).

Fases propuestas:
- **Fase A1 – Carga y auditoría de datos**: importar el `.arff`, convertir tipos, verificar nulos y distribución de `Result`.  
- **Fase A2 – División estratificada 70/15/15**: reproducir el split común, documentar tamaños y proporciones.  
- **Fase A3 – Definición del modelo base**: instanciar `GaussianNB` (o el clasificador histórico) junto con la semilla.  
- **Fase A4 – Búsqueda de hiperparámetros**: ejecutar `GridSearchCV` (CV=5, estratificada, `n_jobs=-1`) sobre `var_smoothing = logspace(-10, -2, 9)`; métrica objetivo F1 con `pos_label=-1`.  
- **Fase A5 – Evaluación y registro**: evaluar el mejor modelo en `val` y `test` con umbral 0.5 (Accuracy, Precision(-1), Recall(-1), F1(-1), matriz de confusión, curva PR opcional) y guardar hiperparámetros + métricas finales.

Resultado esperado: un baseline optimizado exclusivamente a nivel de hiperparámetros, usando las 30 features, con umbral estándar 0.5.

### Script B: selección de features + optimización + ajuste de umbral (pipeline completo)

Este script replica el enfoque de `script3` con selección de features basada en Información Mutua y posterior ajuste de umbral para maximizar F1 en la clase -1.

Fases propuestas:
- **Fase B1 – Carga y auditoría de datos** (idéntica a Fase A1).  
- **Fase B2 – División estratificada 70/15/15** (idéntica a Fase A2, compartir splits).  
- **Fase B3 – Diagnóstico de Información Mutua**: calcular MI en `train` para conocer el ranking de features (sin tocar `val`/`test`).  
- **Fase B4 – Definición del pipeline**: `Pipeline([('selector', SelectKBest(MI)), ('clf', GaussianNB)])`.  
- **Fase B5 – GridSearchCV del pipeline**: optimizar `selector__k ∈ {10,15,20,25,30}` y `clf__var_smoothing = logspace(-10, -2, 9)` con F1 (`pos_label=-1`).  
- **Fase B6 – Evaluación base (umbral 0.5)**: métricas en `val` y `test`, matriz de confusión, curva PR opcional.  
- **Fase B7 – Ajuste de umbral óptimo**: explorar umbrales con `predict_proba` en `val` para maximizar F1(-1).  
- **Fase B8 – Evaluación con umbral óptimo**: aplicar el umbral en `test`, reportar métricas y matriz, comparar contra umbral 0.5.  
- **Fase B9 – Registro de resultados**: documentar k final, features seleccionadas, hiperparámetros, umbral óptimo, métricas finales, matrices y curvas.

Resultado esperado: un pipeline que reduce dimensionalidad de forma informada, ajusta hiperparámetros y además “mueve” el umbral para optimizar F1 en la clase de interés.

### Comparación justa y reporte de resultados

Para que la comparación sea válida, ambos scripts deben:  
- Usar la misma semilla y la misma partición 70/15/15.  
- Medir con las mismas métricas y criterios (F1 con `pos_label=-1` como objetivo primario).  
- Reportar matrices de confusión en prueba.  
- Documentar claramente los hiperparámetros elegidos y, en el caso del Script B, el valor del umbral óptimo.

Elementos a incluir en el informe final:
- Tabla de métricas en `test`: Accuracy, Precision(-1), Recall(-1), F1(-1) para Script A (0.5), Script B (0.5) y Script B (umbral óptimo).  
- Matrices de confusión de `test` para cada caso reportado.  
- Curva Precision–Recall del Script B en validación y la justificación del umbral elegido.  
- Lista de features seleccionadas por el Script B (con k óptimo).  
- Hiperparámetros óptimos de cada enfoque.

### Criterios de decisión y conclusiones

La decisión debe priorizar el equilibrio que ofrezca mejor F1 en phishing (-1), considerando el costo de errores:  
- Si el Script B con umbral óptimo ofrece F1 superior y reduce sustancialmente falsas alarmas sin disparar falsos negativos de forma inaceptable, se recomienda este camino.  
- Si el negocio penaliza mucho los falsos negativos, se puede fijar un umbral más bajo (mayor recall), pero siempre mostrando explícitamente el impacto en precision y F1.  
- La lista de features seleccionadas aporta interpretabilidad y puede simplificar futuros despliegues.

### Estructura sugerida de archivos

- `scripts/v2/scriptA_baseline_full.py` (o notebook): 30 features, tuning de hiperparámetros, evaluación.  
- `scripts/v2/scriptB_pipeline_mi_tuning_threshold.py` (o notebook): selección de features + tuning + ajuste de umbral, evaluación.  
- `reportes/` con tablas de comparación, matrices de confusión, curvas y un breve informe de conclusiones.

### Reproducibilidad

Fijar `RANDOM_STATE`, registrar versiones (Python, scikit-learn, numpy, pandas), mantener el mismo orden de columnas y documentar la partición. Guardar resultados clave (JSON/CSV) para no depender de re-ejecuciones al armar el informe.


