# Redis

## Start Redis Server
```
$ redis-server
```
## Start CLI
```
$ redis-cli
$ redis-cli -h host -p port -a password
127.0.0.1:6379> PING  
PONG
```

# Strings
## GET/SET String/number value
- definir valor: **SET {key} {value}**
- recuperar valor: **GET {key}**
```
127.0.0.1:6379> SET test "i am testing"
OK
...
127.0.0.1:6379> GET test
"i am testing"
```

## List of string commands
|Comando                         |  Função   |
|--------------------------------|-----------|
|GETRANGE key start end | Gets a substring of the string stored at a key. |
|GETSET key value| Sets the string value of a key and return its old value.|
|GETBIT key offset| Returns the bit value at the offset in the string value stored at the key.|
|MGET key1 \[key2..\]| Gets the values of all the given keys|
|SETBIT key offset value| Sets or clears the bit at the offset in the string value stored at the key|
|SETEX key seconds value| Sets the value with the expiry of a key|
|SETNX key value| Sets the value of a key, only if the key does not exist|
|SETRANGE key offset value| Overwrites the part of a string at the key starting at the specified offset|
|STRLEN key| Gets the length of the value stored in a key|
|MSET key value [key value ...]| Sets multiple keys to multiple values|
|MSETNX key value [key value ...]| Sets multiple keys to multiple values, only if none of the keys exist|
|PSETEX key milliseconds value| Sets the value and expiration in milliseconds of a key|
|INCR key| Increments the integer value of a key by one|
|INCRBY key increment| Increments the integer value of a key by the given amount|
|INCRBYFLOAT key increment| Increments the float value of a key by the given amount|
|DECR key| Decrements the integer value of a key by one
|DECRBY key decrement| Decrements the integer value of a key by the given number
|APPEND key value| Appends a value to a key

## DELETE VALUES
- formato: **DEL KEY_NAME**
```
127.0.0.1:6379> DEL test
```

## CHECK IF VALUE EXISTS
- formato: **EXISTS KEY_NAME**
- returns
    - 1, if the key exists.
    - 0, if the key does not exist.
```
127.0.0.1:6379> EXISTS test
(integer) 1
```

## FIND KEYS
- formato: **KEYS pattern**
- aceita **\*** como operador para todos
```
127.0.0.1:6379> KEYS t*
```

## GET KEY TYPE
- formato: **TYPE key**
```
127.0.0.1:6379> TYPE test 
string
```

# HashMaps
## SET Hashmap values 
    A Redis hash is a collection of key value pairs. Redis Hashes are maps between string fields and string values. Hence, they are used to represent objects.
- pode ser json
- HM = hashmap (set)
- H = hash (get)
```
127.0.0.1:6379> HMSET test a 1 b 2
OK
```

## GET Hashmap values
- um registro: **HGET {key} {field}**
- lista de chaves e registros(?): **HGETALL {key}**
```
127.0.0.1:6379> HGET test a
"1"
...
127.0.0.1:6379> HGETALL test
1) "a" 
2) "1" 
3) "b" 
4) "2"
```

## DELETE Hashmaps
- formato: **HDEL KEY_NAME FIELD1.. FIELDN**
```
127.0.0.1:6379> HSET myhash field1 "foo" 
(integer) 1 
127.0.0.1:6379> HDEL myhash field1 
(integer) 1 
127.0.0.1:6379> HDEL myhash field2 
(integer) 1
```
- Nao é possivel apagar varios registros com pattern, para isso, consegui utilizar um comando no unix que utiliza XARGS para tal finalidade
- **redis-cli --scan --pattern {pattern}** : faz uma busca pelas chaves que atendem determinado padrão
- **xargs -t -I** : xargs é um comando do unix que executa um comando para cada registro encontrado no primeiro pipe
    - -t -> exibe o comando ao executa-lo
    - -I -> permite que você escreva um script e use % como placeholder para os argumentos do xargs
- **sh -c 'redis-cli del  "%" '**:
    - % sh -c -> é o início do script
    - redis-cli del % -> é o comando de fato a ser executado multiplas vezes, (% é o caracter placeholder)
```
$ redis-cli --scan --pattern mte:ptbr:* | xargs -t -I % sh -c 'redis-cli del  "%" '
```

## List of HMAP commands:
|Comando                         |  Função   |
|--------------------------------|-----------|
|HDEL key field2 \[field2\]|Deletes one or more hash fields.|
|HEXISTS key field|Determines whether a hash field exists or not.|
|HGET key field|Gets the value of a hash field stored at the specified key.
|HGETALL key|Gets all the fields and values stored in a hash at the specified key|
|HINCRBY key field increment|Increments the integer value of a hash field by the given number|
|HINCRBYFLOAT key field increment|Increments the float value of a hash field by the given amount|
|HKEYS key|Gets all the fields in a hash|
|HLEN key|Gets the number of fields in a hash|
|HMGET key field1 \[field2\]|Gets the values of all the given hash fields|
|HMSET key field1 value1 \[field2 value2 \]|Sets multiple hash fields to multiple values|
|HSET key field value|Sets the string value of a hash field|
|HSETNX key field value|Sets the value of a hash field, only if the field does not exist|
|HVALS key|Gets all the values in a hash|
|HSCAN key cursor \[MATCH pattern\] \[COUNT count\]|Incrementally iterates hash fields and associated values|

# Lists
## Set list
- formato: **lpush {key} {value}**
```
127.0.0.1:6379> lpush li 0
127.0.0.1:6379> lpush li 1
127.0.0.1:6379> lpush li 2
...
127.0.0.1:6379> lrange li 0 -1
1) 2
2) 1
3) 0
```

## Get list
- o indice 0 sempre é o ultimo item incluido (como uma pilha(?))
- formato: **lrange {key} {indexStart} {indexEnd}**
- do primeiro ao ultimo item:
```
127.0.0.1:6379> lrange li 0 -1
```
- somente o primeiro item
```
127.0.0.1:6379> lrange li 0 0
```

## Sets
- Redis Sets are an unordered collection of strings. In Redis, you can add, remove, and test for the existence of members in O(1) time complexity.
- permite a criação de listas com distinct (itens nao se repetem)
- fora isso  é muito parecida com lista
- GET: **smembers** (set members)
- SET: **sadd** (set add)
```
127.0.0.1:6379> sadd tutoriallist redis
127.0.0.1:6379> sadd tutoriallist rabitmq
127.0.0.1:6379> smembers tutoriallist
2) "rabitmq" 
1) "redis"
```

## sorted sets
- Redis Sorted Sets are similar to Redis Sets, non-repeating collections of Strings. The difference is, every member of a Sorted Set is associated with a score, that is used in order to take the sorted set ordered, from the smallest to the greatest score. While members are unique, the scores may be repeated.
```
127.0.0.1:6379> zadd tutoriallist 0 redis
127.0.0.1:6379> ZRANGEBYSCORE tutoriallist 0 1000
```

# Transaction
## MULTI
- voce consegue enfileirar uma serie de comandos a serem executados em uma transação
- basta começar com o comando MULTI, inserir uma serie de comandos e finalizar com EXEC
- ex:
```
127.0.0.1:6379> MULTI 
OK 
127.0.0.1:6379> SET tutorial redis 
QUEUED 
127.0.0.1:6379> GET tutorial 
QUEUED 
127.0.0.1:6379> INCR visitors 
QUEUED 
127.0.0.1:6379> EXEC  
1) OK 
2) "redis" 
3) (integer) 1
```

# Referencias:
[TutorialsPoint](https://www.tutorialspoint.com/redis/redis_overview.htm)