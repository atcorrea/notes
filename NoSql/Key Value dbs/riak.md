## Riak KV
+ https://riak.com/
+ Alta disponibilidade, sistema de replicação de dados avançado.
+ Scripts em **Erlang**
+ Interface [HTTP](#manipula%c3%a7%c3%a3o-por-http) para acesso e escrita de chave-valor:
+ Possui tipos de dados especiais:
  + **Flag**, para armazenar valores booleanos / binários;
  + **Set**, para armazenar os já citado conjuntos;
  + **Map**, para armazenar mapas, possibilitando atualizar
    apenas parte do valor, parecido com um banco orientado a
    documento;
  + **Counter**, que armazena números inteiros, mas com a
    vantagem de utilizar operação de incremento, que resolve o
    problema dos votos. Este tipo de dado é muito útil para
    armazenar números de visualização, números de
    compartilhamentos, total de cliques ou qualquer outra
    informação que seja um contador inteiro.

### Erlang 
+ <\<valor\>> define valores binários
+ linhas terminadas em **.**
+ métodos chamados com **:**
+ Altos métodos estáticos

----
## **Manipulação por HTTP**
### **Recuperando Chave (GET)**
    curl http://localhost:8098/types/default/buckets/votacao/keys/davidpaniz/
### **Inserindo chave(PUT/POST)**
    curl -XPUT -d "Ciclano" http://localhost:8098/types/default/buckets/votacao/keys/adriano
### **Listando todas as chaves**
    curl http://localhost:8098/types/default/buckets/votacao/keys?keys=true
### **Removendo uma chave**
    curl -XDELETE http://localhost:8098/types/default/buckets/votacao/keys/adriano

----
## **Manipulação via Console**
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

### **Deletando uma chave**
    Conexao:delete(<<"votacao">>,<<"davidpaniz">>).
----
