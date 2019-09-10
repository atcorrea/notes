# Hadoop

Família de projetos realcionados a uma infraestrutura de computação distribuída para processamento de dados em larga escala.

**Rodar imagem docker:**
**without docker img:**
```
docker run --hostname=quickstart.cloudera --privileged=true -t -i -p 8888:8888 -p 80:80 -p 50070 cloudera/quickstart usr/bin/docker-quickstart
```
**with docker img:**
```
docker run --hostname=quickstart.cloudera --privileged=true -t -i -p 8888:8888 -p 80:80 -p 50070 atcorrea/hadooptests
```

## HDFS
### Sistema distribuído de arquivos do hadoop
- Baseado no Google File System
- Lida apenas com arquivos, dividindo os em blocos
- Coordenação dos Nós do cluster (main node e job tracker)
- comandos __hadoop fs__ podem substituídos por __hdfs dfs__
  
- Comandos:
  - **Criar diretório:**
  ```
  hdfs dfs -mkdir <diretorio> 
  ``` 
  - **Criar arquivo:**
  ```
  hdfs dfs -touchz <nomedoarquivo> 
  ``` 
  - **Copiar arquivo: (hdfs para local)**
  ```
  hdfs fds -get <diretorio hdfs> <diretorio local>
  ```
  - **Copiar arquivo: (local para hdfs)**
  ```
  hdfs fds -put <diretorio local> <diretorio hdfs>
  (a opção -f ativa sobreescrita de arquivos)
  ```

## Map Reduce
### Framework distribuído de processamento
- Map reduce é um processo que é disparado (map reduce job)
- Transforma dados maiores em dados menores
- Executa scripts escritos em diversas linguagens: python, java, etc.
- Processamento de dados em disco
- O Hive abstrai o map reduce, permitindo a escrita de scripts Hql que, internamente, são convertidos em Map Reduce.

# CDH (Cloudera Data Hub)

## YARN
### Gerenciamento do cluster (nível de recursos)
- Permite o gerenciamento de um cluster e seus nós, oferecendo recursos como limitação de processamento, memória, entre outros.
-----

## Impala
### Processamento de dados (?)
- Similar ao spark (?)
-----

## Hbase
### Banco de Dados (não relacional)
- Apache Hbase, é um banco de Dados não relacionais (noSQL), projetado para trabalhar com grande conjunto de dados (Big Data). É o banco de dados oficial do hadoop.
- Chave-Valor (?)
-----

## Kafka
### Processamento Stream / Dados em tempo real
- Apache Kafka, é foi desenvolvido pelo Linkedin e liberado como projeto Open-source em 2011. O Apache Kafka é um sistema para gerenciamento de fluxo de dados em tempo real, gerados a partir de websites, aplicações e sensores.
- Ferramenta Similar: Storm
-----

## Ambari
### Gerenciamento do Hadoop
- Apache Ambari tem como objetivo tornar o gerenciamento do Hadoop mais simples. O Ambari fornece uma interface de usuário da Web de gerenciamento do Hadoop intuitiva e fácil de usar.
-----

## Mahout
### Machine Learning
- Contém alguns algorítmos prontos de machine learning para aplicação nos dados do cluster
-----

## Hive
### Camada de abstração
- Permite consultas em cluster de dados hadoop utilizando SQL (HiveQL).
-----

## Hue
### Hadoop UI
- Interface gráfica
    
# Pesquisar:
- Big O Complexity
- (Spark) DAG, RDD, DataFrame, DS;

# Missão:
- Iniciar conexão com spark diretamente no python
- Ler os dados do arquivo monthly_salary_brazil.csv
- Dar um aumento de 10% (coluna monthly_salary) para os funcionários
- exibir os dados (.show())