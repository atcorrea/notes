# Built in Functions

## All
**all(list)** : verifica se todos os itens da lista são True para uma condição passada
todos os números são pares:
```python
all(num % 2 for num in [1,2,3,4,5])
```

## Any
**any(list)** : verifica se um dos itens da lista é verdadeiro para uma condição passada
algum número par:
```python
any(num % 2 for num in [1,2,3,4,5])
```

## Filter
**filter(predicate, list)** : retorna uma lista de itens que atendem a uma função (lambda) que retorna True ou False

## Sorted
**sorted(li)** : organiza itens de uma lista ou tupla em ordem. (sempre retorna uma lista). pode receber um parâmento ***reverse=True*** para ir ao contrário.
```python
sorted([5,2,3,1,4]) # [1,2,3,4,5]
sorted([5,2,3,1,4], reverse=True) # [5,4,3,2,1]

#ordenar por artista alfabeticamente em ordem descendente
songs = [
    {"title" : "one", "artist":"metallica"}
    {"title" : "Crazy", "artist":"aerosmith"}
    {"title" : "winds of change", "artist":"scorpions"}
]

sorted(songs, key=lambda s: s["artist"], reverse=True)

```

## Min, Max
**min(list)** : retorna o menor item da lista
```python
min(len(x) for x in [1,2,3,4,5] )
```
**max(list)** : retorna o maior item da lista
```python
max(key=lambda n: len(n))
```

## Reversed
**reversed(iterator)** : inverte a ordem dos elementos em um iterável
```python
reversed(range(0,10))
```

## Len
**len(it)** : Retorna a quantidade de elementos em um iterável

## Mathematical functions
**abs(num)** : retorna o número absoluto (remove o sinal)
```python
def max_magnitude(nums):
    return max(abs(num) for num in nums)
```
**sum(it)** : soma os itens de um iterável. possui um parâmetro opcional que diz o indice para começar a soma.
```python
def sum_floats(*args):
    return sum(arg for arg in args if type(arg) == float)
```
**round(float, decimals)** : arredonda um decimal para o número informado de casas decimais

## ZIP
**zip(list1, list2)** : junta varias listas em uma lista de duplas, com cada tupla sendo os valores de cada lista para um mesmo indice.
```python
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

l = list(zip(list1, list2)) # returns [(1,6), (2,7), (3,8), (4,9), (5,10)]

def interleave(str1,str2):
    return ''.join(''.join(x) for x in (zip(str1,str2)))

interleave('hi', 'ha') # returns 'hhia'
interleave('aaa', 'zzz') # returns 'azazaz'
interleave('lzr', 'iad') # returns 'lizard'
```