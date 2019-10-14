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

## Herança
```python
# Inheritance Example Using Super()
class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def make_sound(self, sound):
		print(f"this animal says {sound}")


class Cat(Animal):
	def __init__(self, name, breed, toy):
		super().__init__(name, species="Cat") # Call init on parent class
		self.breed = breed
		self.toy = toy

	def play(self):
		print(f"{self.name} plays with {self.toy}")

blue = Cat()
blue.make_sound("Meow")
```

## Propriedades
```python
@property #getter decorator
def age(self):
    return self._age

@age.setter
def age(self, value):
    if value >= 0:
        self._age = value
    else:
        raise ValueError("Age cannot be negative!")
```

## Herança Múltipla
- python suporta herança multipla
- Não é muito recomendado que seja utilizado
- Ele utiliza um conceito chamado **MRO (method resolution order)** para decidir qual método executar em uma herança multipla caso as assinaturas sejam iguais
- pode ser visto com ***classe.mro()*** ou help(class) que mostra o mro em um texto formatado.
```python
# Define your classes below:
class Mother():
    def __init__(self):
        self.eye_color = "brown"
        self.hair_color = "dark brown"
        self.hair_type = "curly"

class Father():
    def __init__(self):
        self.eye_color = "blue"
        self.hair_color = "blond"
        self.hair_type = "straight"
    
class Child(Mother, Father):
    def __init__(self):
        super().__init__()

print(Child.mro())
```

## sobreescrevendo operadores (+, -, etc...)
- Basicamente você sobrescreve dunder methods das classes, isso altera o comportamento do compilador em algumas situações exemplos: \_\_init\_\_ para criação de novas instâncias \_\_len\_\_ para utilização com o método len(), entre outros.

|method|usage|desc|
|---|----|----|
|\_\_init\_\_()|variavel =  Classe()|construtor da classe|
|\_\_repr\_\_()|print(Classe)|é basicamente a mesma coisa que o método .toString() do C#|
|\_\_len\_\_()|len(Objeto)|diz a quantidade de elementos em um iterável|
|\_\_add\_\_()|Objeto + Objeto|sobreescreve o operador +|
|\_\_mul\_\_()|Objeto * Objeto|sobreescreve o operador *|