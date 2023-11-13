import json
import socket
import inspect
from threading import Thread

class Servidor_RPC:
    def __init__(self, host:str='0.0.0.0', porta:int=8080) -> None:
        self.host = host
        self.porta = porta
        self.endereco = (host, porta)
        self._metodos = {}
        
    def registrarMetodo(self, funcao) -> None:
        try:
            self._metodos.update({funcao.__name__ : funcao})
        except:
            raise Exception('Um objeto diferente de uma funcao foi repassado ao metodo Servidor_RPC.registrarMetodo(self, funcao)')

    def __gerenciador__(self, cliente:socket.socket, endereco:tuple) -> None:
        print(f'Gerenciando requests do cliente {endereco[0]}:{endereco[1]}...\n')
        print(f'> Cliente {endereco[0]}:{endereco[1]} conectou.')
        while True:
            try:
                nomeFuncao, args, kwargs = json.loads(cliente.recv(1024).decode())
            except: 
                print(f'> Cliente {endereco[0]}:{endereco[1]} desconectou.\n')
                break
            print(f'> Cliente {endereco[0]}:{endereco[1]} solicitou {nomeFuncao}({args})')

            try:
                response = self._metodos[nomeFuncao](*args, **kwargs)
            except Exception as e:
                cliente.sendall(json.dumps(str(e)).encode())
            else:
                cliente.sendall(json.dumps(response).encode())

        print(f'\nOs requests do cliente {endereco[0]}:{endereco[1]} terminaram.\n')
        cliente.close()
        
    def iniciarServidor(self) -> None:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind(self.endereco)
            sock.listen()

            print(f'\nIniciando servidor no host "{self.endereco[0]}" e porta "{self.endereco[1]}"...\n')
            while True:
                try:
                    cliente, endereco = sock.accept()

                    Thread(target=self.__gerenciador__, args=[cliente, endereco]).start()

                except KeyboardInterrupt:
                    print(f'\n\nServidor no host "{self.endereco[0]}" e porta "{self.endereco[1]}" interrompido.\n')
                    break

def listarFuncoes():
    return list(server._metodos)

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b
    
server = Servidor_RPC()

server.registrarMetodo(listarFuncoes)
server.registrarMetodo(add)
server.registrarMetodo(sub)
server.registrarMetodo(mult)
server.registrarMetodo(div)

server.iniciarServidor()
