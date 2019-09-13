# AWS - Amazon Web Services
> Amazon Web Services (AWS) is a comprehensive, evolving cloud computing platform provided by Amazon. It provides a mix of infrastructure as a service (IaaS), platform as a service (PaaS) and packaged software as a service (SaaS) offerings.
- AZ = Availability Zone
----

# Serviços:
## > RDS (Amazon Relational Database Service)
> AWS provides managed database services through its Amazon Relational Database Service, which includes options for Oracle, SQL Server, PostgreSQL, MySQL, MariaDB and a proprietary high-performance database called Amazon Aurora.
- **Serviço de gerenciamento e hospedagem de bancos relacionais dentro da estrutura AWS**
- Aurora foi desenvolvido para ser compatível com MySQL e Postgre
- Garante escalabilidade e disponibilidade dos banco de dados, automatizando diversas atividades de gerenciamento como:
  - Recuperação;
  - Backups;
  - Recuperação;
  - Criptografia de dados;
  - Segurança;
  - Monitoramento;

## > EMR
- Plataforma de Big Data AWS, utilizando Hadoop, Spark e integrando-os à outros serviços da AWS como S3 ou DynamoDB..
> Clientes de diversos setores usam o EMR para proteger e manipular de forma confiável grandes conjuntos de casos de uso de big data, o que inclui machine learning, transformações de dados (ETL), simulações financeiras e científicas, bioinformática, análises de registros e aprendizagem profunda.
- Serviço para hospedagem de Hadoop ou Spark
- Oferece simplificação do processo de processamento de big data, tirando a preocupação de gerenciamento de clusters físicos, e entregando uma forma escalável de rodar servidores de processamento de big data, permitindo que se adicione aramazenamento e processamento conforme demanda.

## > DynamoDB (DDB)
> O Amazon DynamoDB é um banco de dados de valor-chave e documento que oferece desempenho de milissegundos com um dígito em qualquer escala. É um banco de dados durável, que se estende por várias regiões, com vários mestres e totalmente gerenciado com segurança, backup e restauração integrados e armazenamento em cache na memória para aplicativos em escala de Internet. 
- Banco de dados NoSQL da AWS.
- Altamente Escalável e performático.
- O DDB faz a replicação de dados em diversas AZ, garantindo assim disponibilidade e integridade aos dados.
- Possui integração com diversos outros serviços da estrutura AWS.
> A user stores data in DynamoDB tables, then interacts with it via GET and PUT queries, which are read and write operations, respectively. DynamoDB supports basic CRUD operations and conditional operations. Each DynamoDB query is executed by a primary key identified by the user, which uniquely identifies each item.

## > Amazon Neptune
- Banco de dados de grafo

## > Redshift
- Serviço para armazenameto de grandes quantidades de dados (Data Warehouse)
    > Amazon Redshift is a fully managed petabyte-scale data warehouse service. Redshift is designed for analytic workloads and connects to standard SQL-based clients and business intelligence tools.

## > SQS (Amazon Simple Queue Service)
- Serviço de mensageria em fila (similar ao RabbitMQ)
    > O Amazon Simple Queue Service (SQS) é um serviço de filas de mensagens gerenciado que permite o desacoplamento e a escalabilidade de microsserviços, sistemas distribuídos e aplicativos sem servidor. 

## > Kinesis
- Processamento de streams (real time processing and analytics)
  > Amazon Kinesis is an Amazon Web Service (AWS)  for processing big data in real time. Kinesis is capable of processing hundreds of terabytes per hour from high volumes of streaming data from sources such as operating logs, financial transactions and social media feeds. 
- Serviço similar ao Kafka (Hadoop)
- É possível plugar um módulo de analytics para os dados que entram na stream.

## > AWS Lambda 
- Serviço **Serverless** da AWS (Functions as a service)
> AWS Lambda is an event-driven computing cloud service from Amazon Web Services that allows developers to program functions on a pay-per-use basis without having to provision storage or compute resources to support them.
- Responde a eventos como upload para AWS S3, updates no DynamoTB, Kinesis streams, requests HTTP, etc.
  - Basicamente, é possível criar um método que é executado somente quando um evento é disparado. Com isso, é possível, por exemplo, criar uma Web API que responde a chamadas HTTP, sem precisar configurar nada além do método e a lambda.
  - Você paga apenas pelo tempo de processamento das funções.
- Suporta linguagens como Node.js, Python, Java e C#.
- Integração com o *AWS CloudWatch* para análise de consumo e performance

## > AWS CloudWatch
- Serviço de **monitoramento**
- Simplifica o monitoramento de aplicaçõs distribuídas
- Monitora outros serviços da AWS, trazendo informações como frequência de uso, consumo, performance, etc.
  > CloudWatch enables real-time monitoring of AWS resources such as Amazon EC2 instances, Amazon EBS (Elastic Block Store) volumes, Elastic Load Balancers, and Amazon RDS database instances.  The application automatically provides metrics for CPU utilization, latency, and request counts; users can also stipulate additional metrics to be monitored, such as such as memory usage, transaction volumes or error rates. 
- É possível configurar alarmes quando algum recurso monitorado ultrapassa algum parâmetro informado.
- Tambpem monitora disponibilidade dos serviços na estrututra AWS.

## > S3 (Amazon Simple Storage Service)
> Amazon Simple Storage Service (Amazon S3) is a scalable, high-speed, web-based cloud storage service designed for online backup and archiving of data and applications on Amazon Web Services. Amazon S3 was designed with a minimal feature set and created to make web-scale computing easier for developers.
- Armazenamento de objetos.
- Organizado com **buckets**, que é como se fosse uma "pasta", cada bucket deve ter um **nome único** entre toda a AWS.
- **Amazon Glacier:** Backup de dados
- Pode ser acessado por interface web, SDK ou CLI.
  > Amazon S3 is an object storage service, which differs from block and file cloud storage. Each object is stored as a file with its metadata included and is given an ID number. Applications use this ID number to access an object. Unlike file (*Amazon Elastic File System*) and block (*Amazon Elastic Block Store*) cloud storage, a developer can access an object via a REST API.
- Os dados podem ser facilmente replicados entre regiões.
- Outras opções de armazenamendo são o Amazon Elastic Block Store e o Amazon Elastic File System.

## > EC2 (Amazon Elastic Compute Cloud)
- Oferece **servidores** virtuais (instâncias) para processamento.
  > Instances allow developers to expand computing capabilities by 'renting' virtual machines rather than purchasing hardware. An EC2 instance is used to run applications on the Amazon Web Services infrastructure. 
- AMI = Amazon Machine Image (contém os programas dentro da máquina, seu harware, seu comportamento, segurança, etc.).
  - Pode ser considerado um **template**
- Facilmente escalável: Possui ferramenta de escalablidade onde as configurações das instâncias atendem a demanda exigida pela aplicação aumentando suas configurações(CPU, memória, etc.) automaticamente.
- Possui interface web e também API para configuração.
  > To begin using EC2, developers sign up for an account at Amazon's AWS website. They can then use the AWS Management Console, the AWS Command Line Tools (CLI), or AWS Software Developer Kits (SDKs) to manage EC2.  
- Máquinas podem possuir IP fixo
- Dentro de seu marketplace, oferece uma game de diferentes soluções.
- Para acessar um servidor unix remotamente a partir do linux, existe uma ferramenta chamada **PuTTy**
- Existe um serviço: EC2 Container Service que permite que os usuários trabalhem com containers docker

## > IAM (Identity and Access Management)
- Gestão de usuários da conta AWS

## > AWS QuickSight
- Visualização de dados (DataViz)

----

## Referências:
- https://aws.amazon.com/pt
- https://searchaws.techtarget.com/definition/Amazon-Web-Services
- https://www.youtube.com/user/AmazonWebServices/playlists

## Vídeos:
1. [Launching Your First AWS Linux EC2 Instance](https://www.youtube.com/watch?v=kjrKDtxAZpE)
2. [AWS Lambda Tutorial: Lambda + Serverless = HAPPY](https://www.youtube.com/watch?v=71cd5XerKss)
3. [AWS Tutorial - AWS DynamoDB - Create Table Insert Items Scan and Query Table](https://www.youtube.com/watch?v=BdQLwSWn0Z8)