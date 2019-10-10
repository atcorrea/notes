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
- para alterar uma variável global dentro de uma função, utilize o modificador **global**
- para acessar uma variável num bloco acima do que você está agora (parent) use o modificador **nonlocal**
- Para documentar um método utilize 
```python
def add(num1, num2):
    """ adiciona dois números """
    return num1 + num2
```

## Falsy objects:
Os objetos que são interpretados como **False** pelo compilador
- 0
- None
- ""
- []

## Debugging
debugando na linha de comando
**comandos**
- **l** : mostra aonde você está no código
- **variavel** : exibe o valor da variável
- **n** : próxima linha
- **c** : despausa o programa
- **q** : para a execução

```python
import pdb
first = "First"
second = "Second"
pdb.set_trace()
result = first + second
```
