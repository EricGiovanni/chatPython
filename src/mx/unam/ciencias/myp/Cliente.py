import socket
import threading
import sys
import pickle

class Cliente:
    
    def __init__(self, host, port):
        """
        Constructor que incializa el socket, 
        la direccion del usuario y 
        el estado en el que se encuentra el cliente
        """
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.userAddress = (str(host), int(port))
        self.estado = "ACTIVE"
    
    def setEstado(self, estado):
        """ 
        Metodo para asignar el estado del usuario, 
        recibe el estado en el cual se pondra al usuario
        """
        self.estado = estado

    def getEstado(self):
        """ Obtener estado
        Metodo para obtener el estado del usuario
        """
        return self.estado

    def cerrarSocket(self):
        """ Cerrar Socket
        Metodo que cierra la conexion del cliente
        """
        self.sock.close()

    def getSock(self):
        """ Obtener Socket
        Metodo para obtener el socket del cliente
        """
        return self.sock

    def getUserAddress(self):
        """ Obtener direccion del cliente
        Metodo para obtener la direccion del cliente
        """
        return self.userAddress

    def setSock(self, sock):
        """ Asignar Socket
        Metodo para asignar un nuevo socket al usuario
        Recibimos el socket nuevo a asignar
        """
        self.sock.close()
        self.sock = sock
    
    def setUserAddress(self, userAddress):
        """ Asignar Direccion de Usuario
        Metodo para asignar la direccion del usuario
        Recibimos la direccion que le pondremos al usuario
        """
        self.userAddress = userAddress

    def initCliente(self):
        """ Inciar cliente
        Metodo para inicializar el cliente
        """
        self.sock.connect(self.userAddress)
        self.initDaemon()
        self.esperarMensaje()

    def initDaemon(self):
        """ Iniciar Daemon
        Metodo para inciar el thread que recibira mensajes
        """
        msgRecv = threading.Thread(target=self.msgRecv)
        msgRecv.daemon = True
        msgRecv.start()

    def esperarMensaje(self):
        """ Esperar Mensaje
        Metodo que espera mensaje del usuario, 
        para posteriormente enviarlo al servidor
        """
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

    def msgRecv(self):
        """ Recibiendo Mensajes
        Metodo para esperar mensajes del servidor
        """
        while True:
            try:
                data = self.sock.recv(1024)
                if data:
                    print(pickle.loads(data))
            except:
                pass
    
    def sendMsg(self, msg):
        """ Enviar Mensajes
        Metodo para enviar mensajes al servidor
        """
        self.sock.send(pickle.dumps(msg))

if __name__ == "__main__":
    try:
        c = Cliente(sys.argv[1], sys.argv[2])
        c.initCliente()
    except:
        print(" Use: python3 cliente.py host port")