# AWS - Amazon Web Services
> Amazon Web Services (AWS) is a comprehensive, evolving cloud computing platform provided by Amazon. It provides a mix of infrastructure as a service (IaaS), platform as a service (PaaS) and packaged software as a service (SaaS) offerings.
- AZ = Availability Zone

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

## > DynamoDB

## > Amazon Neptune
- Banco de dados de grafo

## > SQS

## > Kinesis

## > AWS Lambda 
- Serviço **Serverless** da AWS (Functions as a service)
> AWS Lambda is an event-driven computing cloud service from Amazon Web Services that allows developers to program functions on a pay-per-use basis without having to provision storage or compute resources to support them.
- Responde a eventos como upload para AWS S3, updates no DynamoTB, Kinesis streams, requests HTTP, etc.
  - Basicamente, é possível criar um método que é executado somente quando um evento é disparado. Com isso, é possível, por exemplo, criar uma Web API que responde a chamadas HTTP, sem precisar configurar nada além do método e a lambda.
  - Você paga apenas pelo tempo de processamento das funções.
- Suporta linguagens como Node.js, Python, Java e C#.


## > S3 (Amazon Simple Storage Service)
> Amazon Simple Storage Service (Amazon S3) is a scalable, high-speed, web-based cloud storage service designed for online backup and archiving of data and applications on Amazon Web Services. Amazon S3 was designed with a minimal feature set and created to make web-scale computing easier for developers.
- Armazenamento de objetos.
- Organizado com **buckets**, que é como se fosse uma "pasta", cada bucket deve ter um **nome único** entre todos os usuários.
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

## Referências:
- https://searchaws.techtarget.com/definition/Amazon-Web-Services
- https://www.youtube.com/user/AmazonWebServices/playlists