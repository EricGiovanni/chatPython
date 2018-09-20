import socket
import threading
import sys
import pickle

class Cliente:
    """
    Constructor que incializa el socket, 
    la direccion del usuario y 
    el estado en el que se encuentra el cliente
    """
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.userAddress = (str(host), int(port))
        self.estado = "ACTIVE"

    """
    Metodo para asignar el estado del usuario, 
    recibe el estado en el cual se pondrá al usuario
    """
    def setEstado(self, estado):
        self.estado = estado

    """
    Metodo para obtener el estado del usuario
    """
    def getEstado(self):
        return self.estado

    """
    Metodo que cierra la conexion del cliente
    """
    def cerrarSocket(self):
        self.sock.close()

    """
    Metodo para obtener el socket del cliente
    """
    def getSock(self):
        return self.sock

    """
    Metodo para obtener la direccion del cliente
    """
    def getUserAddress(self):
        return self.userAddress

    """
    Metodo para asignar un nuevo socket al usuario
    Recibimos el socket nuevo a asignar
    """
    def setSock(self, sock):
        self.sock.close()
        self.sock = sock
    
    """
    Metodo para asignar la direccion del usuario
    Recibimos la direccion que le pondremos al usuario
    """
    def setUserAddress(self, userAddress):
        self.userAddress = userAddress

    """
    Metodo para inicializar el cliente
    """
    def initCliente(self):
        self.sock.connect(self.userAddress)
        self.initDaemon()
        self.esperarMensaje()

    """
    Metodo para inciar el thread que recibira mensajes
    """
    def initDaemon(self):
        msgRecv = threading.Thread(target=self.msgRecv)
        msgRecv.daemon = True
        msgRecv.start()

    """
    Metodo que espera mensaje del usuario, 
    para posteriormente enviarlo al servidor
    """
    def esperarMensaje(self):
        while True:
            msg = input()
            if msg.find("STATUS", 0, 6) != -1:
                if msg.find("AWAY", 7, 11) != -1:
                    self.sendMsg(msg)
                    self.setEstado("AWAY")
                elif msg.find("BUSY", 7, 11) != -1:
                    self.sendMsg(msg)
                    self.setEstado("BUSY")
                elif msg.find("ACTIVE", 7, 13) != -1:
                    self.sendMsg(msg)
                    self.setEstado("ACTIVE")
                else:
                    self.sendMsg(msg)
            elif msg != "DISCONNECT":
                self.sendMsg(msg)
            else:
                self.sendMsg("DISCONNECT")
                self.sock.close()
                sys.exit()

    """
    Metodo para esperar mensajes del servidor
    """
    def msgRecv(self):
        while True:
            try:
                data = self.sock.recv(1024)
                if data:
                    print(pickle.loads(data))
            except:
                pass
    
    """
    Metodo para enviar mensajes al servidor
    """
    def sendMsg(self, msg):
        self.sock.send(pickle.dumps(msg))

if __name__ == "__main__":
    try:
        c = Cliente(sys.argv[1], sys.argv[2])
        c.initCliente()
    except:
        print(" Use: python3 cliente.py host port")