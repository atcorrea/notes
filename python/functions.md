# Functions
## default Parameters
Definindo valores default para parâmetros:
```python
def exponent(base, power=2):
    return base ** power
```

## Ordem dos parâmetros recebidos:
1. parâmetro
2. *args
3. parâmetros opcionais
4. **kwargs

## *Args
pega uma coleção (infita) de **parâmetros como uma tupla**
```python
def sum(*nums):
    soma = 0
    for n in nums: #nums = tupla com todos os argumentos recebidos.
        soma += n
    return soma
```

## **kwargs (key-word args)
- recebe uma coleção (infinita) de **parâmetros como um dicionário.**
- os argumentos entram nomeados na chamada da função.
```python
'''
combine_words("child") = child
combine_words("child", prefix="man") = childman
combine_words("child", suffix="ish") = childish
combine_words("work", "suffix="ing) = working
'''
def combine_words(word,**kwargs):
    if 'prefix' in kwargs: # kwargs = dicionário com os argumentos recebidos
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word
``` 

## parameter unpacking
Transforma uma lista (ou tupla) em uma série de parâmetros para uma função que recebe *args
```python
data = [1,2,3,4,5]
def sum_all(*args):
    total = 0
    for n in args:
        total += n
    return total

# USING uncpacking to pass a list of numbers: (the * is the secret)
sum_all(*data)
```

## utilizando um dicionário de parâmetros
- é possivel passar um dicionário com todos os parâmetros necessários para uma função
- Também chamado de **dictionary unpacking**
- O dicionário precisa que as **chaves tenham o mesmo nome dos parâmetros**, e os **valores sejam os argumentos a serem passados** para a função.
```python
info = {"first":"andre", "last":"torres"}

def print_name(first, last):
    print(f"{first} {last}")

# utilizando:
print_name(**info)
```