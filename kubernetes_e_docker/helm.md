# HELM
Gerenciador de pacotes para um cluster k8s

Aplicação dentro do k8s pode precisar de vários arquivos:
    - Uma definição de POD (app)
    - Uma definição de service para expor o app dentro ou fora do cluster
    - Uma definição de configmap para obter configurações para nossa app (variáveis de ambiente)
    - Uma definiçao de secret (config maps com arquivos escondidos)
    - Uma definição de Ingress para expor rotas de entrada para o cluster
    - Uma definição de deployment para o número de pods
    - definiçao de HPA, e outros...

O Helm tem um componente que é o CHART, que seria um **pacote** com **todos os arquivos** yaml necessários para uma aplicação dentro do k8s.

Um chart pode conter uma versão, assim como um pacote, e publicado em um registry. Desta forma podemos baixar todas os recursos necessários e executar e versionar facilmente uma aplicação dentro de um cluster kubernetes.

É possível criar nossos próprios charts helm, definindo uma estrutura de template dos nossos arquivos yaml do kubernetes, desta forma conseguimos também construir charts para publicação de uma aplicação em diferentes ambientes por exemplo.