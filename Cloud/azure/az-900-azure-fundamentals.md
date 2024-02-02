# AZ-900 (Azure Fundamentals)

## Intro
Uma certificação da Microsoft prova que você passou na prova, comprovando, de maneira confiável, as habilidades em determinado tema.

### Azure Portal
Interface em uma página web que permite que você consiga interagir com a Azure.
- Permite personalizar dashboards
- Acompanhamento de custos
- Controle de acessos
- Acesso a todos os recursos da Azure
- Atualizado constantemente (PaaS)
- Multi Plataforma

### Azure CLI
Interface de linha de comando para interação com a Azure. Comunicação utilizando comandos via texto.
- É estavel
- Comandos estruturados de maneira lógica
- Multi Plataforma
- Possibilita automação

### Azure Powershell
Conjunto de scripts (cmdlets) powershell para interação com a Azure. Assim como a CLI, é uma interface de comunicação via comandos de texto.
- Utiliza o Azure Resource Manager para manipular os recursos.
- Existe comandos especificos para tarefas na Azure.

### Azure Cloud Shell
Shell disponibilizado no navegador para utilizar a azure CLI ou Powershell para comunicar com a Azure.
- Permite acessar a CLI ou Powershell no navegador ou no celular.
- Persite dados através de sessões

### Azure Mobile Apps
Disponível para Android e IoS. Acesso à Azure através de aplicativo. Utiliza o ARM por baixo dos panos. É possivel rodar a Azure Cloud Shell nesse APP.

### ARM Templates
Linguagem comum para descrever a utilização de recursos da Azure. 
- Possibilita automação com idempotência da manipulação dos recursos.
- Utiliza JSON para descrever os recursos.
- Ao executar comandos na Azure CLI, por padrão é retornada a descrição do recurso alterado neste formato.
- Permite versionamento dos arquivos
- Linguagem declarativa

### Azure Advisor
Oferece recomendação sobre serviços, gerenciamento de custos, alertas, segurança, performance, etc.

-------------------------------------------------------------

## Cloud Concepts



3 categorias:
Compute, Networking and Storage

Grande número de datacenters divididos pelo mundo. Baixo custo, alta disponibilidade.

### Language

- **High Availability**: Se algum dos servidores (ou serviços) falharem, você pode subsitui-lo por um idêntico quase imediatamente.
	> Systems are always available - even automatically!
- **Reliability (Fault Tolerance/ Disaster Recovery)**: Resiliência. Habilidade do sistema de se recuperar de falhas e continuar a funcionar. Através do deploy em multiplas locations a aplicação pode se proteger contra disastres locais e regionais. Não há um único ponto de falha, ou seja sempre que um servidor cair, haverá outro para assumir a carga.
	> Reliability describes how Azure can tolerate failures or even disasters.
- **Scalability**: Aumentar ou diminuir automaticamente o tamanho/quantidade dos recursos sob demanda. É possivel escalar para cima horizontalmente (scale out) em horários quando há mais trafego e escalar para baixo horizontamente em horários com menos trafego. Também é possivel escalar verticalmente (scale up), adicionar mais memória, cpu, etc. - no caso de uma vm - tanto para cima quanto para baixo.
	> Ability to scaling out or scaling up while automatically providing resources as needed.
- **Predictability**: 
	- previsibilidade de perfomance -> Uma aplicação pode ter uma experiência consistente independente do tráfego recebido, isso é possivel devido a característica autoscalling de um serviço.
	- previsibilidade de custos -> Evitar surpresas com custos. Ofere acompanhamento de custos e previsões para acompanhamento de custos em tempo real. Também analisa os serviços para sugerir padrões que otimizam o custo no longo prazo.
	> Knowing your application will always perform as expected an knowing what it will cost.
- **Security**: Controle total da segurança das aplicações. Podendo controlar desde infraestrutura, redes, versionamento, etc.
	> Is Having full control of your cloud security posture.
- **Governance**: Governança. Capacidade de padronizar ambientes para atender demandas  corporativas, governamentais, de auditoria, etc. Controle de acessos, monitoramento de usuários, autorização, autenticação, entre outras possibilidades.
	> Standardizing cloud deployments to meet requirements/company standards.
- **Manageability**: 
	- Managemente of the cloud: Autoscalling, monitoring, template-based deployments.
	- Management in the cloud: Várias formas de interagir com a nuvem - portal, cli, apis;
	> Management of cloud resources and how we interect with them.

### Economy
**CAPEX**: Captital Expediture -> Dinheiro gasto por uma organização para adquirir ou manter recursos fixos, como terras, prédios ou equipamentos. Neste contexto, uma empresa poderia estar gastando comprando mais servidores.
	> Buying hardware outight, paid upfront as a one time purchase.
**OPEX**: Operational Expediture -> Custo contínuo para rodar um produto, negócio ou sistema no dia-a-dia, incluindo custos anuais. Nesse contexto pode ser a energia para os servidores funcionarem.
	> Ongoing costs needed to run your business.

Em um modelo sem cloud, um produto digital precisa de muito mais capital de investimento inicial pois seria necessário comprar vários servidores e equipamentos para o negócio funcionar.Alto CAPEX.

Em um modelo cloud você pode pagar apenas o que consumir, logo, pode começar pequeno, sem necessidade de alto investimento no inicio. Assim se diminui o CAPEX (empresa possui menos ativos e menos necessidade de manutenção). No exemplo de um produto digital, um modelo cloud pode diminuir o CAPEX e ter mais controle sobre o OPEX, pois não precisaria investir na compra de equipamentos e manutenção de servidores, nem com energia para eles. Precisaria gastar com os serviços de nuvem, que podem variar os custos conforme a demanda.

Existem alguns modelos de pricing em serviços de nuvem. Alguns deles são:
- Hourly (por hora - VMs, App Services)
- Consumption (pague conforme o uso) => baixa utilização, baixo custo.

Alguns serviços misturam mais de um modelo de pricing (por exemplo serverless Azure Functions)

### Cloud Service Models
- **IaaS Infrastructure-as-a-Service**: Infraestrutura. VMs e Servidores, Redes, Storage, etc.
	> Organization has complete control of the infrastructure.
	> Cost varies depending on consumption.
	> Highly scalable
	> Multiple users share a single piece of hardware.
- **PaaS Platform-as-a-Service**: Plataforma. Abstrai a infraestrutura (que passa a ser gerenciada pela Azure). Middlewares, Ferramentas de desenvolvimento, App Service, Azure CDN, Cosmos DB, etc.
	> Resources are virtualized and can easily be scaled up or down as needed.
	> Services often assist with the development, testing and deployment of apps.
	> Multi-user access via the same development application.
	> Integrates web services and databases.
- **SaaS Software-as-a-Service**: Software. Abstrai a infraestrutura e a plataforma, entrega um software pronto para utilização. Microsoft Entra (active directory) é um Saas na Azure.  Normalmente as pessoas constroem seus SaaS em cima dos serviços oferecidos na Azure. Não há muitos serviços deste tipo na azure.
	> Managed from a central location.
	> Hosted on a remote server.
	> Users not resopnsible for hardware or software updates.

**Serverless** => Não há nenhuma necessidade de gerenciar servidores. Azure Functions. Leva o Paas ao extremo.

### Marketplace
Tipo a app store na azure, com vários serviços oferecidos pela microsoft ou por parceiros. Há serviços gratuitos e pagos.
Todos os produtos oferecidos são certificados pela Microsoft.
Canal de oferta: Caso você seja um parceiro, pode oferecer seus produtos aqui.

### Cloud Architecture Models

- **Private (on premises) **: Total controle sobre a infraestrutura. Oferece vários benefícios da cloud pública e possui mais segurança e privacidade por ser acessivel apenas pela rede interna da empresa. Exige que a empresa tenha a mesma estrutura de pessoas, equipamentos que um datacenter e ela é responsável por sua manutenção.
	> Private cloud is azure on your own hardware in a location of your choice. All the benefits of public cloud, but you can lock it down. A lot of staff required.
- **Public**: Azure, AWS, GCP. Não há necessidade de compra de hardware. Custos variáveis. Não há nenhum acesso físico, pois não há como saber em qual servidor está a aplicação, apenas em qual location está.
	> No upfront costs but monthly usage. Little control over services and infraestructure.
- **Hybrid**: Mistura de privado e publico. Normalmente para empresas em transição ou para atender demandas regulatórias. Há uso dos dois modelos. Alta complexidade de infraestrutura.
	> Best of private and public, but could be complex.

-------------------------------------------------------------

## Azure Architecture

-------------------------------------------------------------

## Compute

-------------------------------------------------------------

## Networking

-------------------------------------------------------------

## Storage

-------------------------------------------------------------

## Database

-------------------------------------------------------------

## Authentication and Authorization

-------------------------------------------------------------

## Solution

-------------------------------------------------------------

## Security

-------------------------------------------------------------

## Privacy Compliancy and Trust

-------------------------------------------------------------

## Pricing

-------------------------------------------------------------

## Support

-------------------------------------------------------------

## Exam

-------------------------------------------------------------
