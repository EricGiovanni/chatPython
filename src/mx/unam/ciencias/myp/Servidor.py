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

    def initServer(self):
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
                if c != cliente:
                    c.send(msg)
            except:
                self.clientes.remove(c)
    
    def aceptarConexion(self):
        print("Esperando conexiones...")
        while True:
            try:
                conn, addr = self.sock.accept()
                conn.setblocking(False)
                print(addr)
                self.clientes.append(conn)
            except:
                pass

    def esperarMensaje(self):
        print("Esperando Mensajes...")
        while True:
            if len(self.clientes) > 0:
                for c in self.clientes:
                    try:
                        data = c.recv(1024)
                        if data:
                            self.msgToAll(data,c)
                    except:
                        pass

if __name__ == "__main__":
    try:
        s = Servidor(str(sys.argv[1]), int(sys.argv[2]))
    except:
        print("use: python3 servidor.py host port")
