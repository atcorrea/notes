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