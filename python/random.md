# Random

# Gerando número aleatório
```python
r = random.random() #0.84442185152550481
```

## Reordenando elementos em uma lista
```python
import random

up_to_ten = range(10)
random.shuffle(up_to_ten)
print(up_to_ten) #mutou a lista:: [2,5,1,9,7,2,8,6,4,0]
```

## Escolher um numero entre um range
```python
r = random.randrange(10,50) # r = 32
```

## Item aleatorio em uma lista
```python
my_best_friend = random.choice(["Alice", "Bob", "Charlie"]) # Retorna aleatoriamente um dos 3
```

## Obter varios itens aleatorios (amostra)
```python
lottery_numbers = range(60)
winning_numbs = random.sample(lottery_numbers, 6) # [16, 36, 10, 6, 25, 9]
```