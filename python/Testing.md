# TESTS
- Assertions e doctests tem vários contras, logo não são a melhor opção para testes automatizados

## Unittest
- Lib de testes (framework)
- Basicamente a classe de testes herda de uma classe (unittest.TestCase) e utiliza os métodos herdados, como por exemplo: assertEqual(v1,v2)
- rodar com:
```
python <file> -v
```
- Exemplo #1
```python
import unittest
from activities import eat, nap, is_funny, laugh

class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
    	"""eat should have a positive message for healthy eating"""
    	self.assertEqual(
			eat("broccoli", is_healthy=True),
			"I'm eating broccoli, because my body is a temple"
    	)
    def test_eat_healthy_boolean(self):
    	"""is_healthy must be a bool"""
    	with self.assertRaises(ValueError):
    		eat("pizza", is_healthy="who cares?")

    def test_is_funny_anyone_else(self):
    	"""anyone else but tim should be funny"""
    	self.assertTrue(is_funny("blue"), "blue should be funny")
    	self.assertTrue(is_funny("tammy"), "tammy should be funny")
    	self.assertTrue(is_funny("sven"), "sven should be funny")
    
    def test_laugh(self):
    	"""laugh returns a laughing string"""
    	self.assertIn(laugh(), ('lol', 'haha', 'tehehe'))

if __name__ == "__main__":
    unittest.main()
```
- Exemplo #2
```python
import unittest
from robot import Robot


class RobotTests(unittest.TestCase):
    #RUN BEFORE EACH TEST
    def setUp(self):
        self.mega_man = Robot("Mega Man", battery=50)

    def test_charge(self):
        self.mega_man.charge()
        self.assertEqual(self.mega_man.battery, 100)

    def test_say_name(self):
        self.assertEqual(
            self.mega_man.say_name(),
            "BEEP BOOP BEEP BOOP.  I AM MEGA MAN")
        self.assertEqual(self.mega_man.battery, 49)

    #RUN AFTER EACH TEST
    def tearDown(self):
        self.mega_man.terminate()

if __name__ == "__main__":
    unittest.main()
```

## DocTests
- permite a escrita de testes na doc do método
- para rodar no terminal utilize: 
```
python -m doctest -v <arquivo>
```
- **Incrivelmente chato com sua sintaxe**:
  - respostas em string devem ser em ' não "
  - número de espaços deve ser exatamente o mesmo (mesmo na exibição de listas)
  - Ao esperar um erro, o texto deve ser exatamente o mesmo que o que o console exibiria
  - considera ordem dos itens de dicionários
```python
def add(a, b):
	"""
	>>> add(2, 3)
	5
	>>> add(100,200)
	300
	"""
	return a + b

def double(values):
	""" double the values in a list

	>>> double([1,2,3,4])
	[2, 4, 6, 8]

	>>> double([])
	[]

	>>> double(['a', 'b', 'c'])
	['aa', 'bb', 'cc']

	>>> double([True, None])
	Traceback (most recent call last):
		...
	TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
	"""
	return [2 * element for element in values]

# Doctests can only compare to single quoted strings
def say_hi():
	"""
	>>> say_hi()
	"hi"
	"""
	return "hi"

# Order of keys in dicts matters in doctests
def make_dict(keys):
	"""
	>>> make_dict(['a','b'])
	{'b': True, 'a': True}
	"""
	return {key: True for key in keys}
```

## Assert
- Caso a condição seja avaliada como falsa, ele dispara um AssertionError
- Se você rodar o arquivo python com a flag -O, ele ignora todas as assertions
- **Não** é muito recomendada a utilização
```python
# Example 1
def add_positive_numbers(x, y):
    assert x > 0 and y > 0, "Both numbers must be positive!"
    return x + y

print(add_positive_numbers(1, 1)) # 2
add_positive_numbers(1, -1) # AssertionError: Both numbers must be positive!

# Example 2
def eat_junk(food):
	assert food in [
		"pizza", 
		"ice cream", 
		"candy", 
		"fried butter"
	], "food must be a junk food!"
	return f"NOM NOM NOM I am eating {food}"

food = input("ENTER A FOOD PLEASE: ")
print(eat_junk(food))
```