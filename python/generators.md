# Generator
- gastam menos memórias que listas
- você usa next(object) para iterar pelo gerador


## Generator method
```python
def gen(n):
    for i in range(1,n+1):
        yield n*i
```

## Infinite Generator
```python
def current_beat():
	nums = (1,2,3,4)
	i = 0
	while True:
		if i >= len(nums): i = 0
		yield nums[i]
		i += 1
```

## Generator expressions
```python
#its the same thing as a list comprehension except you are using ()
x = (for x in range(1,10))
```