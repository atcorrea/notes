# ISTIO
É uma implementação de service mesh. Utiliza CRD (custom kubernetes component)
É possivel instalr o istio de maneira facil no cluster utilizando istioctl.

## Service mesh
Gerencia comunicação entre microsserviços. Sobe em um side-car dentro dos pods de serviços. Cada container é um proxy para comunicação entre os pods.
É possivel fazer deploy canário com um service mesh.

Istio utiliza proxys Envoy dentro dos pods. Esse é chamado de data pane.

O Istio também roda um Control Pane chamado Istiod. A configuração do istio é separada das aplicações.

Ele tem um discovery de novos serviços publicados no cluster. Ele Permite comunicação TLS entre os microsserviços (mTLS). Também coleta métricas de telemetria dos serviços.

## Istio Ingress Gateway
Um ponto de entrada para o seu cluster. Para o ingress gateway funcionar, é necessário um Gateway configurado no cluster e também é necessário configurar um VirtualService para cada pod que será exposto via gateway.


