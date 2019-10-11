# Object Oriented Programming

## defining classes
- Convention: CamelCase
```python
class Food():
```

## Constructor
```python
class Food():
    def __init__(self, name):
        self.name = name

food1 = Food("pizza")
print(food.name) # pizza
```

## Métodos da instância
```python
class Food:
    def __init__(self, name):
        self.name = name

    def taste(self):
        print(print(f"{self.name} is good"))
```

## Atributos estáticos
```python
class Food:
    #attributes
    menu = [] ## anything without self is static

    def __init__(self, name):
        self.name = name
        Food.menu.append(name) # reference the class...
```
## Métodos estáticos
```python
class Food:
    
    @classmethod
    def how_many_foods(cls):
        print(f"there are {len(cls.menu)} foods on the menu")

    menu = []

    def __init__(self, name):
        self.name = name
        Food.menu.append(name)
```

## __repr__ (representation)
- é o .toString() do python
ex:
```python
class Food:
    def __init__(self, name):
        self.name = name

    def __repr(self):
        print(f"this is a {self.name}")

# usage:
f1 = Food('pizza')
print(f1) # prints: this is a pizza
```

## Dunder methods (convenção + ou -)
- envoltos por __ no começo e no final.
- são métodos para o python (compilador) utilizar (como é o exemplo do init) não para serem chamados diretamente.

## Membros privados (convention)
- prepostos por um _ (python não suporta private)
- EX: _counter

