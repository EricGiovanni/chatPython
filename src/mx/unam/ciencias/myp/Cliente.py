import socket
import threading
import sys
import pickle

class Cliente:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.userAddress = (str(host), int(port))

    def cerrarSocket(self):
        self.sock.close()

    def getSock(self):
        return self.sock

    def getUserAddress(self):
        return self.userAddress

    def setSock(self, sock):
        self.sock.close()
        self.sock = sock
    
    def setUserAddress(self, userAddress):
        self.userAddress = userAddress

if __name__ == "__main__":
    try:
        c = Cliente(sys.argv[1], sys.argv[2])
        c.initCliente()
    except:
        print(" Use: python3 cliente.py host port")