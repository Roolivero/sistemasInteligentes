# Ejercicio 5

## El script debe realizar un agrupamiento o Clustering con AgglomerativeClustering y distancia de Gower 

1.  Usar la matriz de distancias de Gower calculada en Fase 3. 
2.  Aplicar AgglomerativeClustering1 con affinity="precomputed" y  linkage="average". 
3.  Determinar un número adecuado de clusters (Silhouette y/o Davies-Bouldin). 

Preguntas guía: 
●  ¿Qué diferencia hay entre un dendrograma jerárquico y los centroides de K-means? 
●  ¿Qué criterio usaste para elegir el número de clusters finales? 
●  ¿Qué ventajas observaste al usar variables categóricas con Gower? 


### Aclaracion: 
* Es una continuacion del "scriptBorrador3"
* Fijate si podes hacerlo en "scriptBorrador5" o tenes que hacerlo en "scriptBorrador3" porque vas a necesitar los resultados obtenidos de Gower.
* Para calcular *AgglomerativeClustering1* podes usar librerias. Tenes que aplicarlo con *affinity="precomputed"* y  *linkage="average"*. 
* Para determinar el numero adecuado de Clusters usar Silhouette y Davies-Bouldin. 
* Hacer los dendrograma