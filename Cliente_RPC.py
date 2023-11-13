import json
import socket
import inspect
from threading import Thread

class Cliente_RPC:
    def __init__(self, host:str='localhost', porta:int=8080) -> None:
        self.sock = None
        self.endereco = (host, porta)
        
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
            
    def __getattr__(self, __nome: str):
        def executar(*args, **kwargs):
            self.sock.sendall(json.dumps((__nome, args, kwargs)).encode())

            resposta = json.loads(self.sock.recv(1024).decode())
   
            return resposta
        
        return executar
        

client = Cliente_RPC()

client.conectar()

while True:
    try:
        x = int(input('\nO que deseja fazer?\n\n0. Listar funcoes cadastradas\n1. ADD\n2. SUB\n3. MULT\n4. DIV\n>'))
        
        if x == 0:
            print('\nAs seguintes funcoes estao cadastradas em Servidor_RPC:')
            print(client.listarFuncoes())
        
        elif x == 1:
            try: 
                a = int(input('\nEscolha o primeiro valor para a adicao:\n>'))
                b = int(input('\nEscolha o segundo valor para a adicao:\n>'))
            
                print(f'\nResultado: {client.add(a, b)}\n')
            except ValueError:
                 print("Por favor, insira valores inteiros válidos.")
            
        elif x == 2:
            try: 
                 a = int(input('\nEscolha o primeiro valor para a subtracao:\n>'))
                 b = int(input('\nEscolha o segundo valor para a subtracao:\n>'))
                
                 print(f'\nResultado: {client.sub(a, b)}\n')
            except ValueError:
                 print("Por favor, insira valores inteiros válidos.")

            
        elif x == 3:
            try:
                a = int(input('\nEscolha o primeiro valor para a multiplicacao:\n>'))
                b = int(input('\nEscolha o segundo valor para a multiplicacao:\n>'))
            
                print(f'\nResultado: {client.mult(a,b)}\n')
            except ValueError:
                print("Por favor, insira valores inteiros válidos.")

            
        elif x == 4:
           try:
                a = int(input('\nEscolha o primeiro valor para a divisao:\n>'))
                b = int(input('\nEscolha o segundo valor para a divisao:\n>'))
            
                print(f'\nResultado: {client.div(a,b)}\n')    
           except ValueError:
                print("Por favor, insira valores inteiros válidos.")

            
        else:
            print('\nTente novamente.\n')
        
    except KeyboardInterrupt:
        break

client.desconectar()
