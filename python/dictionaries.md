## Métodos
- **.pop(key)** : remove um item baseado na sua chave. Retorna o **valor** removido.
- **.popitem()** : remove um item aleatoriamente do dicionário.
- **.update()** : adiciona os items de um dicionário no final do outro. Se houverem chaves iguais, irá atualizar os valores.

## criando um dict com valores default:
```python
{}.fromkeys(['item1','item2','item3'], 'valor padrão')
'''
irá gerar:
{
    'item1': 'valor padrão', 
    'item2': 'valor padrão', 
    'item3': 'valor padrão'
}
'''
```
## melhor forma de checar se dict contém um valor:
```python
from random import choice
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"])

bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}
```
- Utilizando {}.get(valor), que retorna **None** caso a chave não exista no dicionário.
```python
items = bakery_stock.get(food)
if items:
    print("{} left".format(items))
else:
    print("We don't make that")
```

- Utilizando **in**
```python
if food in bakery_stock:
    print("{} left".format(bakery_stock[food]))
else:
    print("We don't make that")
```

## Dictionary comprehensions

### **Exemplos:**
- a partir de outro dicionário:
```python
numbs = {'one':1, 'two':2,'three':3}
squared = {k:v**2 for k, v in numbs.items()}
```

- a partir de uma lista de chaves e uma lista de valores
```python
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
answer = {list1[i] : list2[i] for i in range(0,3)}
'''
{
   'CA': 'California', 
   'NJ': 'New Jersey', 
   'RI': 'Rhode Island'
}
'''
```
- Lista de pares:
```python
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = dict(person)
'''
{
    'name': 'Jared', 
    'job': 'Musician', 
    'city': 'Bern'
}
'''
```

- Dicionário de valores ASCII
```python
answer = {n: chr(n) for n in range(65,91)}
```