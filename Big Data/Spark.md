## Spark
### Processamento de dados
- Apache Spark, é uma ferramenta Big Data para o processamento de grandes conjuntos de dados. Foi desenvolvido para substituir o MapReduce, pois processa 100x mais rápido que o MapReduce.
- É um framework que contém utilidades para processamento SQL, Real Time Streaming, Machine Learning e Graph Processing.
  - Componentes: Spark SQL, Spark Streaming, ML Lib, GraphX
- O Mais rápido para processamento de dados em memória
- Processa dados em disco (HDFS) e memória
- Escrito em Scala
- Executa queries em lazy evaluation

**Comandos:**
- Executar Spark:
```
pyspark --master local
```
- Cria um RDD:
```
variavel = sc.parallelize(list)
```
- Exibe dados:
```
variavel.collect()
```
- Cria um DataFrame:
```
variavel = sqlContext.createDataFrame(collection)
```
-----