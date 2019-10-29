# Input/Output
- python não precisa importar lib para manipular arquivos (nativo)
- Utiliza cursores para ler arquivos (percorre o arquivo uma vez, ao chegar ao fim, precisa ser inicializado novamente)

## open()
```python
file = open("file.txt")

#criando um novo arquivo
file = open("new.txt", "w")
```

## with()
- utilizando with() os recursos são dispensados automaticamente. (é a mesma coisa que o using do C#)
- por trás dos panos, ele utiliza os dunders __enter()__ e __exit()__ para executar as operações de abertura e fechamento

## Métodos
|Nome|Função|
|----|------|
|**file.read()**|retorna o arquivo como uma única string (\n para quebra de linhas)|
|**file.seek()**|movimenta o cursor (o argumento é um caracter)|
|**file.read()**|Traz uma única linha|
|**file.realines()**|Retorna todas as linhas como uma lista|
|**file.closed**|Retorna True se o arquivo estiver aberto|
|**file.close()**|fecha o arquivo, liberando recursos do computador|
|**file.write(<string>)**|Adiciona texto à um arquivo|

