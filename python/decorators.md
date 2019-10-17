# Decorators
- basta criar um método, que recebe uma função como argumento (como uma wrapper function), e utilizar a notação **@** em cima da função que seria o argumento para este método.

```python
def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper

@be_polite
def greet():
    print("My name is Colt.")


@be_polite
def rage():
	print("I HATE YOU!")

greet()
rage()
```

## pattern
- utilizando *args e **kwargs
```python
def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper
```

## preservando metadados (__doc__, __name__, etc.)
- o Segredo está no decorator @wraps(fn) da lib functools que preserva os metadados
```python
from functools import wraps
def log_function_data(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """I AM WRAPPER FUNCTION"""
        print(f"you are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper


@log_function_data
def add(x,y):
    """Adds two numbers together."""
    return x + y

print(add.__doc__)
print(add.__name__)
help(add)

```

## Passando argumentos
- deve-se encadear uma função que recebe os argumentos um nível acima de onde a função 'wrapper' fica (fica mais claro no exemplo)
```python
from functools import wraps

def ensure_first_arg_is(val):
	def inner(fn):
		@wraps(fn)
		def wrapper(*args, **kwargs):
			if args and args[0] != val:
				return f"First arg needs to be {val}"
			return fn(*args, **kwargs)
		return wrapper
	return inner


@ensure_first_arg_is("burrito")
def fav_foods(*foods):
    print(foods)

print(fav_foods("burrito", "ice cream")) # ('burrito', 'ice cream')
print(fav_foods("ice cream", "burrito")) # 'Invalid! First argument must be burrito'

@ensure_first_arg_is(10)
def add_to_ten(num1, num2):
    return num1 + num2

print(add_to_ten(10, 12)) # 12
print(add_to_ten(1, 2)) # 'Invalid! First argument must be 10'
```