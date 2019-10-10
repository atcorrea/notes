# Exceptions

Utilize a keyword **raise**  para lançar uma exceção

**Try Catch(except):**
```python
while True:
    try:
        num = int(input("please type a number"))
    except (ValueError, TypeError) as err:
        print("That is not a number!")
        print(err)
    else:
        print("That is a number!")
        break
    finally:
        print("always run")


def divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError as err:
        print("cannot divide by zero!")
        print(err)
    except TypeError as err:
        print("a and b must be numbers!")
        print(err)
    else:
        print(f"{a} divided by {b} is {result}" )
```