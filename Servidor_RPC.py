import json
import socket
import inspect
from threading import Thread

class Servidor_RPC:
    def __init__(self, host:str='0.0.0.0', porta:int=8080) -> None:
        self.host = host
        self.porta = porta
        self.endereco = (host, porta)
        self.metodos = {}
        
    def registrarMetodo(self, funcao) -> None:
        try:
            self.metodos.update({funcao.__name__ : funcao})
        except:
            raise Exception('A non funcao object has been passed into RPCServidor.registrarMetodo(self, funcao)')    

    def registrarInstancia(self, instancia=None) -> None:
        try:
            # Regestring the instancia's methods
            for nomeFuncao, funcao in inspect.getmembers(instancia, predicate=inspect.ismethod):
                if not nomeFuncao.startswith('__'):
                    self.metodos.update({nomeFuncao: funcao})
        except:
            raise Exception('A non class object has been passed into RPCServidor.registrarInstancia(self, instancia)')
        
    def __handle__(self, cliente:socket.socket, endereco:tuple) -> None:
        print(f'Managing requests from {endereco}.')
        while True:
            try:
                nomeFuncao, args, kwargs = json.loads(cliente.recv(SIZE).decode())
            except: 
                print(f'! clientee {endereco} desconectou.')
                break
            # Showing request Type
            print(f'> {endereco} : {nomeFuncao}({args})')

            try:
                response = self.metodos[nomeFuncao](*args, **kwargs)
            except Exception as e:
                # Send back exeption if funcao called by cliente is not registred 
                cliente.sendall(json.dumps(str(e)).encode())
            else:
                cliente.sendall(json.dumps(response).encode())

        print(f'Completed requests from {endereco}.')
        cliente.close()
        
    def iniciarServidor(self) -> None:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind(self.endereco)
            sock.listen()

            print(f'Servidor {self.endereco} iniciando...')
            while True:
                try:
                    cliente, endereco = sock.accept()

                    Thread(target=self.__handle__, args=[cliente, endereco]).start()

                except KeyboardInterrupt:
                    print(f'- Servidor {self.endereco} interrompido')
                    break
