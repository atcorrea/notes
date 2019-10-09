# Listas 

## usando range
```python
range(<de>,<até(não inclui esse número)>)
```
## Slices
[ from : to : step ]
```python
li = [1,2,3,4,5]
li[:] #all list
li[-1] #get last index
li[::-1] #reverse all list
li[:4:2] #up to index 4 always steping 2 values (2 then 2 then 2....)
```
## Usando List Comprehentions
simples
```python
[ x[0].replace('data_', '').upper() for x in tables ]
```
encadeando list comprehension
```python
[[char for char in word] for word in word_list]
```
## Métodos
- **.pop()** : remove um item da lista. Se o argumento estiver vazio, remove o último indice (como em uma stack), ou então pode receber o **índice** do item a ser removido.
- **.remove()** : remove um item recebendo o seu **valor**. EX: em uma lista ["a","b","c"], utilizariamos ***lista.remove("b")*** para remover o segundo item
- **.append()** : adiciona um item no **final** da lista (como em uma stack)
- **.insert()** : adiciona um item recebendo o indice de onde deve ser inserido. EX: em uma lista [1,2,3,4,5], podemos utilizar ***lista.insert(2,0)*** para adicionar o item 0 no indice 2.
- **.extend()** : Adiciona uma lista no final de outra
- **.index()** : retorna o indice de um item recebendo o seu valor. EX: em uma lista ['a','b','c'], podemos utilizar ***lista.index('a')*** retorna 0.