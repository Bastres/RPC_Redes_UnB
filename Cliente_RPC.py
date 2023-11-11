import json
import socket
import inspect
from threading import Thread

class RPC_Cliente:
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
            
    def __getattr__(self nome: str):
        def excecutar(*args, **kwargs):
            self.sock.sendall(json.dumps((nome, args, kwargs)).encode())

            resposta = json.loads(self.sock.recv(SIZE).decode())
   
            return resposta
        
        return excecutar
