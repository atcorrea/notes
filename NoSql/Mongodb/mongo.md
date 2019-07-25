# **MONGO**
```js
> db.[COLECTION_NAME].[COMMAND]
```

# **notas:**
+ Ideal para armazenamento de dados não estruturados.
+ Dentro do MongoDB, os arquivos são armazenados em formato BSON.
+ Utilizando **.pretty()** no final da query, o JSON vem identado no console.

------
## **commands:**
|Comando                         |  Função   |
|--------------------------------|-----------|
| .insert({json})                | incluir novo registro |
| [.find({json})](#find)      | encontrar registro(s) |
| .findOne({json})               | traz o primeiro registro que satisfaz a condição |
| .remove({json})                | remove um registro |
| [.update({json}, [new values])](#update)  | atualiza um registro |
| .count({})                     | contagem de todos os registros que satisfazem uma condição |

-----
## **operadores find:**
```js
> db.[COLLECTION_NAME].find({"[CAMPO]":"[operador]":[valor]})
```

|Operador|Sinal matemático|Significado|
|----|----|---|
| $gt |  > |  (greater than) |
| $gte | >= | (greater than equal) |
| $lt |  < |  (lower than) |
| $lte | <= | (lower than equal) |
| $ne |  != | (not equal) |
| $in |  |(range ) |

## **operadores lógicos:**
+ $and
+ $or
+ $nor
+ $not
```js
db.[COLLECTION_NAME].find(
{ 
    [operador lógico] :
        [ 
            {"[CAMPO]": {[operador] : [valor]}}, 
            {"[CAMPO]": {[operador] : [valor]}} 
        ]
}
);
```
------
## **.find()**

### **Busca aninhada:**

```js
db.[COLLECTION_NAME].find({"[CAMPO]": {["CAMPO_INTERNO"] : [valor]}})
```

Em objetos aninhados (embedded documents), é preciso utilizar uma busca aninhanda (obj dentro de obj), para obter o resultado desejado.

**Exemplos**
```js
//busca por ID
db.albuns.find({"_id": new ObjectId("5d3712041383fd82610359d3")})

//busca com duas condições (and)
db.albuns.find({$and: [
{"dataLancamento": {$gte: new Date(1986, 0 , 1)}},
{"dataLancamento": {$lt: new Date(1987, 0, 1)}}
]})

//busca aninhada
db.albuns.find({"artista":{"nome":"Blind Guardian"}}).pretty()

```
-----
## .update()
update **modifica o objeto completo** (troca um objeto json por outro, mantendo apenas o ID) isso pode resultar em perda de informações (sintaxe pura não atualiza campos).

para atualizar apenas o campo, utilizar o operador **$set**

o operador **$unset** serve para **remover** campos.

Por default, **update sempre atualiza apenas 1 registro**, para atualizar mais de um doc, deve-se passar um terceiro argumento, um booleano, ex: 

    db.colecao.update({BUSCA}, {ATUALIZACAO},{multi : true}).

**Exemplos**
```js
//update de valor de um campo
db.albuns.update({"nome":"Among the Living"},{$set : {"produtor":"Tony Ganza"}}) 

//removendo campos do documento
db.albuns.update({},{$unset : {"nome_artista":true, "artista_id":true}}) 
```
----
## **Bons Exemplos**
```js
1.
artistas.forEach(x => {
  print("atualizando albuns de " + x["nome"]);
  var result = db.albuns.update(
    { "artista.nome": x["nome"] },
    {
      $unset: { artista: true },
      $set: { artista_id: x["_id"], nome_artista: x["nome"] }
    },
    { multi: true }
  );
  print(result);
});

```

## **referências:**
+ [**NoSQL:** Como armazenar os dados de uma aplicação moderna - Casa do código](https://www.casadocodigo.com.br/products/livro-nosql)
