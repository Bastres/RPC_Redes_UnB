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
            
    def __getattr__(self, __name: str):
        def excecute(*args, **kwargs):
            self.sock.sendall(json.dumps((__name, args, kwargs)).encode())

            response = json.loads(self.sock.recv(SIZE).decode())
   
            return response
        
        return excecute
