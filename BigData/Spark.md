# Spark
### **Processamento de dados**
- Apache Spark, é uma ferramenta Big Data para o processamento de grandes conjuntos de dados. Foi desenvolvido para substituir o MapReduce, pois processa 100x mais rápido que o MapReduce.
- É um framework que contém utilidades para processamento SQL, Real Time Streaming, Machine Learning e Graph Processing.
  - **Componentes:** Spark SQL, Spark Streaming, ML Lib, GraphX
- O Mais rápido para processamento de dados em memória
- Processa dados em disco (HDFS) e memória
- Escrito em Scala
- Suporta lazy evaluation
  > "The style of only evaluating what's needed is called *lazy evaluation*, while the opposite (evaluating immediately) is called *strict evaluation*."
  > "For lazy evaluation to be efficient, it needs to use **memoization**."

----

### **RDD** (Resilient Distributed Datasets):
  - datasets imutáveis
  - Não possuem schema
  - Records are just recorded row-by-row, and are displayed similar to a lis/t.
  - Coleção de dados particionada entre nós do cluster
  > **When to use RDDs**:
  > - you want low-level transformation and actions and control on your dataset;
  > - your data is unstructured, such as media streams or streams of text;
  > - you want to manipulate your data with functional programming constructs than domain specific expressions;
  > - you don’t care about imposing a schema, such as columnar format, while processing or accessing data attributes by name or column; and
  > - you can forgo some optimization and performance benefits available with DataFrames and Datasets for structured and semi-structured data.
  - Dataframes e Datasets foram construídos em cima de RDDs.

### **Spark DataFrames**:
  - possuem schema (colunar)
  - Não tipados
  - imutável
  - A partir do spark 2.0 dataframes e datasets foram unificados em uma única API, que passou a ser apenas **Dataset**, porém para python, a biblioteca continua sendo somente dataframes, pois python não é uma linguagem tipada. 

### **Spark Datasets**
  - Fortemente Tipados
  - Não utilizado em python (pySpark) pois python não é uma linguagem tipada

### Transformação de dados
  > Transformations are one of the things you can do to an RDD in Spark. They are lazy operations that create one or more new RDDs. It’s important to note that Transformations create new RDDs because, remember, RDDs are immutable so they can’t be altered in any way once they’ve been created.
### Ações
  > An Action is any RDD operation that does not produce an RDD as an output. Some examples of common Actions are doing a count of the data, or finding the max or min, or returning the first element of an RDD, etc.
  > Actions are RDD operations that produce non-RDD values. They materialize a value in a Spark program.

### **Comandos:**
- Executar pySpark:
```
pyspark
```
- Executar um script python:
```
spark-submit <arquivo.py>
```
- Executar cluster utilizando [**YARN**](./Hadoop.md#yarn)
```
spark-submit --master yarn <arquivo>
```
- **flags spark-submit:**
  - **--num-executors**: define o número de execures para o processo
  - **--executor-cores**: número de cores para cada executor
  - **--master**: define o ip do master para execução
  - **--executor-memory**: memória alocada para o processo dentro de cada executor

#### **Comandos pySpark**
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
- particiona um RDD em n partes:
```
RDD.repartition(n)
```
-----

### **Tips:**
- Importar contexto do spark dentro de um script (para ser rodado via spark submit)
```python
    from pyspark import SparkConf, SparkContext
    conf = (SparkConf()
           .setMaster("local")
           .setAppName("My app")
           .set("spark.executor.memory", "1g"))
    sc = SparkContext(conf = conf)
```
- Ler arquivo CSV no pySpark:
```python
# Retorna um DDD com os valores separados por ','
sc.textFile("file.csv") 
    .map(lambda line: line.split(","))
```
- **Nem sempre paralelizar mais (aumentar número de executores ou particionar mais os rdds) vai reduzir o tempo de processamento!** É preciso considerar que a comunicação entre as máquinas (rede) pode aumentar o tempo de processamento, além disso, só a coordenação dos executores pode acabar aumentando o processo mais do que o necessário!

## Referências:
- [The 5-Minute Guide to Understanding the Significance of Apache Spark](https://mapr.com/blog/5-minute-guide-understanding-significance-apache-spark/)
- [A Neanderthal’s Guide to Apache Spark in Python](https://towardsdatascience.com/a-neanderthals-guide-to-apache-spark-in-python-9ef1f156d427)
- [PySpark Documentation](https://spark.apache.org/docs/0.9.0/api/pyspark/index.html)
- [Examples | Spark](https://spark.apache.org/examples.html)
- [A brief introduction to PySpark](https://towardsdatascience.com/a-brief-introduction-to-pyspark-ff4284701873)