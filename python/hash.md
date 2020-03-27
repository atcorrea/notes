# Criptografando senhas

## Passlib
- Utiliza Salt para tornar as senhas mais seguras.

## Criptografar:
```python
from passlib.hash import sha256_crypt
password = sha256_crypt.encrypt("password")
```

## Checar se bate:
```python
sha256_crypt.verify("password", password)
# retorna True se igual
```
