## Riak KV
+ https://riak.com/
+ Alta disponibilidade, sistema de replicação de dados avançado.
+ Scripts em **Erlang**
+ Interface HTTP para acesso e escrita de chave-valor:
```
curl http://localhost:8098/types/default/buckets/votacao/keys/davidpaniz/
curl -XPUT -d "Ciclano" http://localhost:8098/types/default/buckets/votacao/keys/adriano
  
//Recuperando todas as chaves
curl http://localhost:8098/types/default/buckets/votacao/keys?keys=true
```

### Erlang 
+ <\<valor\>> define valores binários
+ linhas terminadas em **.**
+ métodos chamados com **:**
+ Altos métodos estáticos

## **Exemplos de código**

### **Criando Conexão**

    (riak@127.0.0.1)1> Servidor = 'riak@127.0.0.1'.
    (riak@127.0.0.1)2> net_adm:ping(Servidor).
    (riak@127.0.0.1)3> {ok,Conexao} = riak:client_connect(Servidor).

### **Criando chave no BD**
    Voto = riak_object:new(<<"votacao">>, <<"davidpaniz">>, <<"Fulano">>).
    Conexao:put(Voto, 1).

### **Recuperando o valor de uma chave**
    {ok, OutroVoto} = Conexao:get(<<"votacao">>,<<"davidpaniz">>,1).
    riak_object:get_value(OutroVoto).

### **Recuperando todas as chaves em um bucket**
    Conexao:list_keys(<<"votacao">>).

