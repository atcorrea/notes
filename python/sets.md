# Sets

- Não tem ordem
- Não possuem itens duplicados
- Não é possui acessar os itens pelo índice
- **Normalmente utilizado para remover itens duplicados de uma lista** (converte lista pra set, depois converte novamente para lista)

## Criando um set:
```python
s = {1,2,3,4,5}
# ou
s = set({1,2,3,4,5})
```

## métodos:
- **.add(item)** : adiciona um item
- **.remove(item)** : remove um item (dá erro quando não existe)
- **.discard(item)** : remove um item (não dá erro quando não existe)
- **.clear()** : remove todos os itens
- **Matemáticos**:
  - Utilizando **union** entre dois sets:
  ```python
  set1 | set2
  ```
  - Utilizando **intersect** entre dois sets:
  ```python
  set1 & set2
  ```

## Set comprehensions:
- A sintaxe é quase a mesma que a do dictionary comprehension, **a única diferença é que não há o ":"** para separar chave valor
```python
{ x**2 for x in range(10)}
```