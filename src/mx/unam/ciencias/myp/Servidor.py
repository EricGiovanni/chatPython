import socket
import threading
import sys
import pickle

class Servidor:
    def __init__(self, host, port):
        self.clientes = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = (str(host), int(port))
        self.numUser = 0
        self.id = 0

    def aumentaID(self):
        self.id = self.id + 1

    def aumentaNumUser(self):
        self.numUser = self.numUser + 1

    def getID(self):
        return self.id
    
    def getNumUser(self):
        return self.numUser

    def setServer(self, server):
        self.server = server

    def getServer(self):
        return self.server

    def cerrarSocket(self):
        self.sock.close()

    def getSock(self):
        return self.sock

    def setSock(self, sock):
        self.sock.close()
        self.sock = sock

    def initServer(self):
        self.sock.bind(self.server)
        self.sock.listen()
        self.sock.setblocking(False)
        self.initDaemon()
        self.recibirMensaje()

    def recibirMensaje(self):
        while True:
            msg = input()
            if msg == "QUIT":
                self.sock.close()
                sys.exit()
            else:
                pass

    def initDaemon(self):
        aceptar = threading.Thread(target=self.aceptarConexion)
        procesar = threading.Thread(target=self.esperarMensaje)
        aceptar.daemon = True
        aceptar.start()
        procesar.daemon = True
        procesar.start()
    
    def msgToAll(self, msg, cliente):
        for c in self.clientes:
            try:
                if c[0] != cliente:
                    c[0].send(msg)
            except:
                self.clientes.remove(c)

    def privateMsg(self, msg, cliente):
        for c in self.clientes:
            try:
                if c[0] in cliente:
                    c[0].send(msg)
            except:
                self.clientes.remove(c)
    
    def aceptarConexion(self):
        print("Esperando conexiones...")
        while True:
            try:
                conn, addr = self.sock.accept()
                conn.setblocking(False)
                print(addr)
                self.clientes.append((conn, self.numUser, self.id))
                self.aumentaNumUser()
                self.aumentaID()
            except:
                pass

    def esperarMensaje(self):
        print("Esperando Mensajes...")
        while True:
            if len(self.clientes) > 0:
                for c in self.clientes:
                    try:
                        data = c[0].recv(1024)
                        if data:
                            if(pickle.loads(data) == "DISCONNECT"):
                                msg = "Se ha desconectado " + str(c[1])
                                msgBytes = pickle.dumps(msg)
                                print(msgBytes)
                                self.msgToAll(msgBytes, c[0])
                            else:
                                self.msgToAll(data,c[0])
                    except:
                        pass

if __name__ == "__main__":
    try:
        s = Servidor(str(sys.argv[1]), int(sys.argv[2]))
        s.initServer()
    except:
        print("use: python3 servidor.py host port")
