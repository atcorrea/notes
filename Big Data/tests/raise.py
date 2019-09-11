# Esse arquivo deve ser redodado dentro do container com pyspark instalado.

from pyspark import SparkConf, SparkContext
conf = (SparkConf().setMaster('local').setAppName('app').set('spark.executor.memory', '1g'))
sc = SparkContext(conf = conf)
sc.setLogLevel("ERROR")

data = sc.textFile('monthly_salary_brazil.csv').map(lambda x: x.split(','))

header = data.first()
rows = data.filter(lambda x: x != header).map(lambda y: [int(y[0]), y[1].encode('latin-1'), y[2].encode('latin-1'), round(float(y[3]), 2)])

raised = rows.map(lambda x: [x[0], x[1], x[2], round(x[3] * 1.1, 2)])


before = rows.take(10)
after = raised.take(10)

print('before')
print(before)

print('after')
print(after)