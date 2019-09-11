# Esse arquivo deve ser redodado dentro do container com pyspark instalado.
# não esquecer de utilizar hdfs dfs -put ./monthly_salary_brazil.csv /user/root/ para copiar o CSV!

from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, Row

conf = (SparkConf()
        .setMaster('local')
        .setAppName('app')
        .set('spark.executor.memory', '1g')
        )
sc = SparkContext(conf=conf)

sqlContext = SQLContext(sc)
sc.setLogLevel("ERROR")

data = sc.textFile('monthly_salary_brazil.csv').map(lambda x: x.split(','))

header = data.first()
rows = data.filter(lambda x: x != header).map(lambda y: Row(
    id=int(y[0]),
    job=y[1].encode('latin-1'),
    sector=y[2].encode('latin-1'),
    monthly_salary=round(float(y[3]), 2)
))
before = sqlContext.createDataFrame(rows)

raised = rows.map(lambda x: Row(
    id=x.id,
    job=x.job,
    sector=x.sector,
    monthly_salary=round(x.monthly_salary * 1.1, 2)
))
after = sqlContext.createDataFrame(raised)

print('BEFORE')
before.show()

print('AFTER')
after.show()
