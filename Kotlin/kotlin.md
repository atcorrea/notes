# Kotlin

## Funções
- Identificadas pela keyword **fun**
- Tipos: precedidos por **:** (dois pontos)
- Tipos começam com letra maiúscula (?)
-  **Exemplo:**
```
fun sum(a: Int, b: Int): Int {
    return a + b
}
``` 
- Suporte a valores default para parâmetros:
```java
fun foo(a: Int = 0, b: String = "") { ... }
```

## Strings
- Utilizando **"""** (tres aspas duplas) você pode escrever uma string com várias linhas.

## String templates (interpolation)
- identifica variáveis pelo carácter **$**
```java
var a = 3
println("number is $a")
```

## Variáveis
- Keyword **var** infere o tipo do dado e podem ser redefinidas. Funciona exatamente como no C#.
- Keyword **val** são read-only, podem ou não receber o tipo de dados.
- **Exemplo:**
```java
val a: Int = 1  // immediate assignment
val b = 2   // `Int` type is inferred
val c: Int  // Type required when no initializer is provided
c = 3       // deferred assignment
```

## Nullable Types
- Tipos nullable funcionam igual o C#
- Sucedidos por **?**
```
fun parseInt(str: String): Int? {
    // ...
}
```

## Type checks
- utiliza o operador **is**
```java
fun getStringLength(obj: Any): Int? {
    if (obj is String) {
        // `obj` is automatically cast to `String` in this branch
        return obj.length
    }

    // `obj` is still of type `Any` outside of the type-checked branch
    return null
}
```

## When
- Como se fosse um switch case
```java
fun describe(obj: Any): String =
    when (obj) {
        1          -> "One"
        "Hello"    -> "Greeting"
        is Long    -> "Long"
        !is String -> "Not a string"
        else       -> "Unknown"
    }
```
- Com coleções:
```java
when {
    "orange" in items -> println("juicy")
    "apple" in items -> println("apple is fine too")
}
```
## Enums
- a convenção para enums é que todos os valores devem estar em **up case**
```java
enum class Weapons{
    SWORD, AXE, SPEAR
}
```

## Coleções:
- Listas podem ser representadas como ArrayList<> (entre outros tipos) assim como no Java
```java
val inventory = ArrayList<String>()
```

## Loops
- Sintaxe de loops parecida com python, possui apenas **for**
- para um for com números, utilizar ranges
- existem palavras chave que representam a forma de andar nos ranges, (until, downTo, step)
- **until** não inclui o último número
- **step** só aceita valores positivos, para contagem negativa usar **downTo**
- **Exemplos:**
```java
for(val in values) {
    println(val)
}

//Incremental - NÃO INCLUI O ULTIMO NUMERO!!
for(x in 0 until 10) {
    print(x)
}

//Decrescente
for(x in 10 downTo 0) {
    print(x)
}

//de 2 em 2 (VALOR DEVE SEMPRE SER POSITIVO!)
for(x in 0 until 10 step 2) {
    print(x)
}
```

## Ranges
- identificados por numeros separados por **..**
- diferente de python, INCLUI o ultimo número
```java
for (x in 1..5) {
    print(x)
}
```
- O operador **in** pode ser utilizado para verificar se um valor está contido dentro de um range
```java
val list = listOf("a", "b", "c")

if (-1 !in 0..list.lastIndex) {
    println("-1 is out of range")
}
if (list.size !in list.indices) {
    println("list size is out of valid list indices range, too")
}
```

## Construtores
- O construtor é declarado junto com a classe, recebendo as propriedades
- para executar código no momento da criação do objeto, utiliza-se a keyword **init**
```java
class Player(val name:String, var level: Int = 1){
    init {
        level += 4
    }
}

var player = Player("l1nk")
```
- **Não é necessário o uso de new** para declarar objetos

## Herança
- Por padrão classes e metodos não podem ser herdados
- Utiliza a keyword **open** para tornar as classes herdáveis
- mesmo se a classe for **open** os métodos ainda precisam da notação **open** para serem sobrescritos.
- Métodos precisam da notação **override** para sobrescrever a implementação herdada
```java
open class Animal(val name: String, val numberOfLegs: Int) {
    open fun move(distance: Int){
        //...
    }
}
```
- Notação para herança:
```java
class Bird(val name: String, val numberOfLegs: Int = 2) : Animal(name, numberOfLegs) {
    override fun move(distance: Int) {
        this.fly(distance)
    }

    fun fly(distance: Int) {
        //...
    }
}
```

## Mais
- Todas as classes herdam de **Any**
- Não precisa de ; no final das linhas
- Puxa conceitos da programação funcional e pode ser usado com sintaxe similar ao LINQ
```java
val fruits = listOf("banana", "avocado", "apple", "kiwifruit")
fruits
  .filter { it.startsWith("a") }
  .sortedBy { it }
  .map { it.toUpperCase() }
  .forEach { println(it) }
```
- Equivalente ao null coalescing operator (**?:** ):
```java
val email = values["email"] ?: throw IllegalStateException("Email is missing!")
```
- Utilizando o método **TODO()** automaticamente dispara uma exceção **NotImplementedError**

## Referências:
- https://kotlinlang.org/docs/
- [Dicas](https://kotlinlang.org/docs/reference/idioms.html)