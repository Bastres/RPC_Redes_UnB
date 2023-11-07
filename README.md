# RPC_Redes_UnB
## descrição do projeto 19/11
<p align="center">• Serviço de chamada de procedimento remoto (RPC)
– O cliente deve ser capaz de listar os servi¸cos (fun¸c˜oes) oferecidas pelo servidor
1
– O cliente deve implementar fun¸c˜oes stub locais, reproduzindo a assinatura da fun¸c˜ao (nome da fun¸c˜ao,
tipos de parˆametros e de retorno)
– A fun¸c˜ao de stub do cliente deve encapsular os parˆametros passados em uma mensagem de RPC,
que ser´a enviada ao servidor quando a fun¸c˜ao stub ´e chamada no programa
– O servidor deve escutar por mensagens de RPC, executˆando-as localmente e enviando de volta o
resultado da fun¸c˜ao executada
– O cliente deve receber o resultado do RPC e retomar a execu¸c˜ao do programa local, de maneira
transparente (sem realizar nenhuma opera¸c˜ao de rede ou captura de exce¸c˜oes fora da fun¸c˜ao stub)
– Caso o servidor de RPC n˜ao responda em um intervalo especificado, o cliente deve retransmitir a
requisi¸c˜ao de RPC e aguardar pela resposta
– Caso o cliente receba duas respostas para uma mesma requisi¸c˜ao de RPC, dever´a escolher o primeiro
valor recebido</p>
