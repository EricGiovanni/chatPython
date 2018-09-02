import socket
import threading
import sys

class Servidor:
    #Constructor que recibe el host y el puerto en el que se conectará
    def __init__(self, host, port):
        self.clientes = []
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverAddress = (str(host), (port))
        self.serverSocket.bind(serverAddress)
        self.serverSocket.listen(10000)
        self.serverSocket.setblocking(False)

        accept = threading.Thread(target=self.acceptConnection())
        process = threading.Thread(target=self.processConnection())
        accept.daemon = True
        accept.start()
        process.daemon = True
        process.start()

    def acceptConnection(self):
        print("Aceptando conección")
        while True:
            try:
                conn, addr = self.serverSocket.accept()
                conn.setblocking(False)
                print("conectado " + str(addr))
                self.clientes.append(conn)
            except:
                pass
        
    def processConnection(self):
        print("Procesando conección")
        while True:
            if len(self.clientes) > 0:
                for c in self.clientes:
                    try:
                        data = c.recv(1024)
                        if data:
                            self.sendMsg(data, c)
                    except:
                        pass
            
    def sendMsg(self, msg, cliente):
    		for c in self.clientes:
			    try:
				    if c != cliente:
					    c.send(msg)
			    except:
				    self.clientes.remove(c)

try:
    s = Servidor(str(sys.argv[1]), int(sys.argv[2]))
except:
    print("use: python3 servidor.py host port")