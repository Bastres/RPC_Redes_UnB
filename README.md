# RPC_Redes_UnB
## descrição do projeto 19/11
<p align="center">
• Serviço de chamada de procedimento remoto (RPC)<br>
– O cliente deve ser capaz de listar os servi¸cos (funções) oferecidas pelo servidor
 <br>
– O cliente deve implementar funções stub locais, reproduzindo a assinatura da funções (nome da função,
tipos de parâmetros e de retorno)
<br>
– A função de stub do cliente deve encapsular os parâmetros passados em uma mensagem de RPC,
que ser´a enviada ao servidor quando a função stub ´e chamada no programa
<br>
– O servidor deve escutar por mensagens de RPC, executˆando-as localmente e enviando de volta o
resultado da função executada
<br>
– O cliente deve receber o resultado do RPC e retomar a execução do programa local, de maneira
transparente (sem realizar nenhuma opera¸c˜ao de rede ou captura de exce¸c˜oes fora da função stub)
<br>
– Caso o servidor de RPC n˜ao responda em um intervalo especificado, o cliente deve retransmitir a
requisição de RPC e aguardar pela resposta
<br>
– Caso o cliente receba duas respostas para uma mesma requisição de RPC, deverá escolher o primeiro
valor recebido</p>
