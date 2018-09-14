import socket
import threading
import sys
import pickle

class Servidor:
    def __init__(self, host, port):
        self.clientes = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server = (str(host), int(port))
        self.sock.bind(server)
        self.sock.listen()
        self.sock.setblocking(False)

    def cerrarSocket(self):
        self.sock.close()

    def getSock(self):
        return self.sock

    def setSock(self, sock):
        self.sock.close()
        self.sock = sock

if __name__ == "__main__":
    try:
        s = Servidor(str(sys.argv[1]), int(sys.argv[2]))
    except:
        print("use: python3 servidor.py host port")
