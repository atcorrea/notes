# Comandos UNIX:

## **time**: 
exibe o tempo que demorou para executar uma linha de comando.
#### Exemplo:
```
time spark-submit --master yarn --num-executors 3 --executor-cores 1 raise.py
```
## **wget**:
faz o download de um arquio (solicitação get)
#### Exemplo:
```
wget <url>
```

## **SSH**
inicia uma conexão remota por protocolo SSH
#### Exemplo:
```
ssh -i <caminho do arquivo .pem> <url do servidor>
```