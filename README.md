# RPC_Redes_UnB
## Lista de requisitos funcionais do Projeto Chamada de Procedimento Remoto (RPC)

– O cliente deve ser capaz de listar os serviços (funções) oferecidas pelo servidor; ✓
 <br>
 
– O cliente deve implementar funções stub locais, reproduzindo a assinatura da funções (nome da função,
tipos de parâmetros e de retorno);
<br>

– A função de stub do cliente deve encapsular os parâmetros passados em uma mensagem de RPC,
que será enviada ao servidor quando a função stub é chamada no programa;
<br>

– O servidor deve escutar por mensagens de RPC, executando-as localmente e enviando de volta o
resultado da função executada; ✓
<br>

– O cliente deve receber o resultado do RPC e retomar a execução do programa local, de maneira
transparente (sem realizar nenhuma operação de rede ou captura de exceções fora da função stub);
<br>

– Caso o servidor de RPC não responda em um intervalo especificado, o cliente deve retransmitir a
requisição de RPC e aguardar pela resposta;
<br>

– Caso o cliente receba duas respostas para uma mesma requisição de RPC, deverá escolher o primeiro
valor recebido;</p>

## Data de entrega: 23/11/2023

Integrantes do Grupo:

- Caio Silva Batista - 211020820
- Mateus Pereira da Silva - 190035145
- Tiago Leão Buson - 200034162
