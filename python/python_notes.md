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

## Exibindo os membros de um tipo
```python
print(dir(<type>))
```
## Exibindo informações sobre uma função ou classe
```python
help(<func>)
```
## Trabalhando com datas:
```python
import datetime
datetimeObj = datetime.datetime.strptime(dateStr, '%d-%m-%Y')

year = datetimeObj.year
month = datetimeObj.month
day = datetimeObj.day
```

## Variados:
- Divisão com resultado inteiro (arredondado para baixo)
```python
 a // b
```

## Falsy objects:
Os objetos 
- 0
- None
- ""
- []
