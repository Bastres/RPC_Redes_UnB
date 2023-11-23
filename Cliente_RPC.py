import json
import socket
import time

class Cliente_RPC:
    def __init__(self, host:str='localhost', porta:int=8080,timeout=5) -> None:
        self.sock = None
        self.endereco = (host, porta)
        self.timeout = timeout
        self.next_request_id = 0
        self.respostas = {}
        
    def conectar(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect(self.endereco)
        except EOFError as e:
            print(e)
    
    def desconectar(self):
        try:
            self.sock.close()
        except:
            pass

    def gerarId(self):
        # Gera um id unico para cada requisição
        requestId = self.next_request_id
        self.next_request_id += 1
        return requestId
            
    
    def __getattr__(self, nome):
        def executar(*args, **kwargs):
            requestId = self.gerarId()
            for i in range(3):
                # REQUISITO 5
                try:
                    
                    # Envia a chamada RPC para o servidor
                    self.sock.sendall(json.dumps((nome, args, kwargs, requestId)).encode())
                    self.sock.settimeout(self.timeout)
                    # Recebe a resposta do servidor
                    while True:
                        resposta, respostaId = json.loads(self.sock.recv(1024).decode())
                        self.respostas[respostaId] = resposta

                        while respostaId != requestId:
                            print(f"ID errado! ReqId: {requestId} ResId: {respostaId} Tentando novamente...")
                            respostaRepetida, respostaRepetidaId = json.loads(self.sock.recv(1024).decode())
                            respostaId += 1
                            # self.respostas.append(respostaRepetida)
                            self.respostas[respostaRepetidaId] = respostaRepetida
                        break
                    
                    return self.respostas[requestId]
                except socket.timeout:
                    # REQUISITO 6
                    # Manipula o caso em que o tempo de espera excede
                    print(f"Tempo de espera excedido para a chamada {nome}. Tentando novamente...")
                    self.sock.settimeout(self.timeout)

        return executar
        

#funcoes stub (REQUISITO 2 e 3)

# REQUISITO 1
def listarFuncoes():
    return client.listarFuncoes()

def add(a,b):
    return client.add(a,b)

def sub(a,b):
    return client.sub(a,b)

def mult(a,b):
    return client.mult(a,b)

def div(a,b):
    return client.div(a,b)      

client = Cliente_RPC()

client.conectar()

while True:
    try:
        x = input('\nO que deseja fazer?\n\n0. Listar funcoes cadastradas\n1. ADD\n2. SUB\n3. MULT\n4. DIV\n\n>')
        
        if x == '0':
            print('\nAs seguintes funcoes estao cadastradas no Servidor_RPC:')
            print(listarFuncoes())
        
        elif x == '1':
            try: 
                a = int(input('\nEscolha o primeiro valor para a adicao:\n>'))
                b = int(input('\nEscolha o segundo valor para a adicao:\n>'))
            
                print(f'\nResultado: {add(a, b)}\n')
            except ValueError:
                 print("Por favor, insira valores inteiros válidos.")
            
        elif x == '2':
            try: 
                 a = int(input('\nEscolha o primeiro valor para a subtracao:\n>'))
                 b = int(input('\nEscolha o segundo valor para a subtracao:\n>'))
                
                 print(f'\nResultado: {sub(a, b)}\n')
            except ValueError:
                 print("Por favor, insira valores inteiros válidos.")

            
        elif x == '3':
            try:
                a = int(input('\nEscolha o primeiro valor para a multiplicacao:\n>'))
                b = int(input('\nEscolha o segundo valor para a multiplicacao:\n>'))
            
                print(f'\nResultado: {mult(a,b)}\n')
            except ValueError:
                print("Por favor, insira valores inteiros válidos.")

            
        elif x == '4':
           try:
                a = int(input('\nEscolha o primeiro valor para a divisao:\n>'))
                b = int(input('\nEscolha o segundo valor para a divisao:\n>'))
            
                print(f'\nResultado: {div(a,b)}\n')    
           except ValueError:
                print("Por favor, insira valores inteiros válidos.")

            
        else:
            print('\nTente novamente.\n')
        
    except KeyboardInterrupt:
        break

client.desconectar()
