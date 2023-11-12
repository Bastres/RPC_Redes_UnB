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
        

server = Cliente_RPC()

server.conectar()

while True:
    try:
        x = int(input('O que deseja fazer?\n\n1. ADD\n2. SUB\n3. MULT\n4. DIV\n\n'))
        
        if x == 1:
            
            a = int(input('\nEscolha o primeiro valor para a adicao:\n>'))
            b = int(input('\nEscolha o segundo valor para a adicao:\n>'))
            
            print(f'\nResultado: {server.add(a, b)}\n')
            
        elif x == 2:
        
            a = int(input('\nEscolha o primeiro valor para a subtracao:\n>'))
            b = int(input('\nEscolha o segundo valor para a subtracao:\n>'))
                
            print(f'\nResultado: {server.sub(a, b)}\n')
            
        elif x == 3:
        
            a = int(input('\nEscolha o primeiro valor para a multiplicacao:\n>'))
            b = int(input('\nEscolha o segundo valor para a multiplicacao:\n>'))
            
            print(f'\nResultado: {server.mult(a,b)}\n')
            
        elif x == 4:
        
            a = int(input('\nEscolha o primeiro valor para a divisao:\n>'))
            b = int(input('\nEscolha o segundo valor para a divisao:\n>'))
            
            print(f'\nResultado: {server.div(a,b)}\n')    
            
        else:
            print('\nTente novamente.\n')
        
    except KeyboardInterrupt:
        break

server.desconectar()
