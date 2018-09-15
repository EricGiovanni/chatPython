import socket
import threading
import sys
import pickle

class Cliente:
    
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.userAddress = (str(host), int(port))
        self.estado = "ACTIVE"

    def setEstado(self, estado):
        self.estado = estado

    def getEstado(self):
        return self.estado

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

    
    def initCliente(self):
        self.sock.connect(self.userAddress)
        self.initDaemon()
        self.esperarMensaje()

    def initDaemon(self):
        msgRecv = threading.Thread(target=self.msgRecv)
        msgRecv.daemon = True
        msgRecv.start()

    def esperarMensaje(self):
        while True:
            msg = input()
            if msg != "DISCONNECT":
                self.sendMsg(msg)
            else:
                self.sendMsg("DISCONNECT")
                self.sock.close()
                sys.exit()

    def msgRecv(self):
        while True:
            try:
                data = self.sock.recv(1024)
                if data:
                    print(pickle.loads(data))
            except:
                pass
    
    def sendMsg(self, msg):
        self.sock.send(pickle.dumps(msg))

if __name__ == "__main__":
    try:
        c = Cliente(sys.argv[1], sys.argv[2])
        c.initCliente()
    except:
        print(" Use: python3 cliente.py host port")