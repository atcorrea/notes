## Abrindo um arquivo csv:
```python
import csv

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)
        print(row[0])
        print(row[0],row[1],row[2],)
```

## Exibindo os métodos de um módulo (?)
```python
print(dir(<type>))
```

## Trabalhando com datas:
```python
import datetime
datetimeObj = datetime.datetime.strptime(dateStr, '%d-%m-%Y')

year = datetimeObj.year
month = datetimeObj.month
day = datetimeObj.day
```

## Usando List Comprehentions
```python
[ x[0].replace('data_', '').upper() for x in tables ]
```