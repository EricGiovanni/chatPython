import socket
import threading
import sys
import pickle
import Room

class Servidor:
    def __init__(self, host, port):
        """
        Constructor que inicializa una lista de rooms, 
        una lista de clientes, el socket , el numero de 
        usuario y el numero ID que identificara a cada
        usuario
        """
        self.clientes = []
        self.rooms = []
        self.principal = Room.Room(self.clientes, "Principal")
        self.rooms.append(self.principal)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = (str(host), int(port))
        self.id = 0
        self.numUser = "User" + str(self.id)

    def aumentaID(self):
        """
        Metodo que aumenta el valor del ID para el siguiente usuario
        """
        self.id = self.id + 1

    def aumentaNumUser(self):
        """
        Metodo que cambia el nombre de usuario de acuerdo al ID
        """
        self.numUser = "User" + str(self.id)

    def setNumUser(self, numUser):
        """
        Metodo que te permite cambiar el nombre de usuario
        """
        self.numUser = numUser

    def getID(self):
        """
        Metodo que te permite obtener el ID
        """
        return self.id
    
    def getNumUser(self):
        """
        Metodo que te permite obtener el nombre de usuario
        """
        return self.numUser

    def setServer(self, server):
        """
        Metodo que te permite cambiar la tupla host y port
        """
        self.server = server

    def getServer(self):
        """
        Metodo que te permite obtener la tupla host y port
        """
        return self.server

    def cerrarSocket(self):
        """
        Metodo que cierra el socket del servidor
        """
        self.sock.close()

    def getSock(self):
        """
        Metodo que obtiene el socket del servidor
        """
        return self.sock

    def setSock(self, sock):
        """
        Metodo que te permite cambiar el socket del servidor
        """
        self.sock.close()
        self.sock = sock

    def initServer(self):
        """
        Metodo que incia el proceso del servidor
        """
        self.sock.bind(self.server)
        self.sock.listen()
        self.sock.setblocking(False)
        self.initDaemon()
        self.recibirMensaje()

    def recibirMensaje(self):
        """
        Metodo que espera mensajes de la entrada del servidor
        """
        while True:
            msg = input()
            if msg == "QUIT":
                self.sock.close()
                sys.exit()
            else:
                pass

    def initDaemon(self):
        """
        Metodo que inicia Daemons para aceptar conexiones y esperar 
        mensajes de usuarios
        """
        aceptar = threading.Thread(target=self.aceptarConexion)
        procesar = threading.Thread(target=self.esperarMensaje)
        aceptar.daemon = True
        aceptar.start()
        procesar.daemon = True
        procesar.start()
    
    #def mstToAll(self, msg, cliente):
        #if

    def msgToAll(self, msg, cliente):
        """
        Metodo que envia mensajes a todos los clientes
        """
        for c in self.clientes:
            try:
                if c[0] != cliente:
                    c[0].send(msg)
            except:
                self.clientes.remove(c)

    def privateMsg(self, msg, cliente):
        """
        Metodo que envia mensaje privado a un cliente
        """
        for c in self.clientes:
            try:
                if c[0] == cliente:
                    c[0].send(msg)
            except:
                self.clientes.remove(c)
    
    def groupMsg(self, nombre, msg, cliente):
        """
        Metodo que envia mensajes a clientes de un room
        """
        for r in self.rooms:
            if r.getNombre() == nombre:
                r.enviarMsg(msg, cliente)
    
    def aceptarConexion(self):
        """
        Metodo que acepta conexiones de nuevos clientes
        """
        print("Esperando conexiones...")
        while True:
            try:
                conn, addr = self.sock.accept()
                conn.setblocking(False)
                print("Se ha conectado" + str(addr))
                self.clientes.append((conn, self.numUser, self.id))
                for r in self.rooms:
                    if r.getNombre == "Principal":
                        r.agregarCliente((conn, self.numUser, self.id))
                self.aumentaID()
                self.aumentaNumUser()
            except:
                pass

    def esperarMensaje(self):
        """
        Metodo que espera mensajes de los clientes conectados
        """
        print("Esperando Mensajes...")
        while True:
            if len(self.clientes) > 0:
                for c in self.clientes:
                    try:
                        data = c[0].recv(1024)
                        if data:
                            if(pickle.loads(data) == "DISCONNECT"):
                                msg = "Se ha desconectado " + str(c[1])
                                print(msg)
                                msgBytes = pickle.dumps(msg)
                                self.msgToAll(msgBytes, c[0])
                            elif(pickle.loads(data).find("STATUS", 0, 6) != -1):
                                msg = pickle.loads(data)
                                if msg.find("AWAY", 7, 11) != -1:
                                    msg = pickle.dumps(str(c[1]) + " ha cambiado su status a AWAY")
                                    self.msgToAll(msg, c[0])
                                elif msg.find("BUSY", 7, 11) != -1:
                                    msg = pickle.dumps(str(c[1]) + " ha cambiado su status a BUSY")
                                    self.msgToAll(msg, c[0])
                                elif msg.find("ACTIVE", 7, 13) != -1:
                                    msg = pickle.dumps(str(c[1]) + " ha cambiado su status a ACTIVE")
                                    self.msgToAll(msg, c[0])
                                else:
                                    msg = pickle.dumps(msg)
                                    self.msgToAll(msg, c[0])
                            elif(pickle.loads(data).find("PUBLICMESSAGE", 0, 13) != -1):
                                msg = str(c[1]) + ": " + pickle.loads(data)[14:]
                                self.msgToAll(pickle.dumps(msg), c[0])
                            elif(pickle.loads(data).find("IDENTIFY", 0, 8) != -1):
                                #c[1] = str(pickle.loads(data)[9:])
                                self.privateMsg(pickle.dumps("Tu nombre ha cambiado a: " + str(c[1])), c[0])
                            else:
                                self.privateMsg(pickle.dumps("Comando incorrecto " + str(c[1])), c[0])
                    except:
                        pass

if __name__ == "__main__":
    try:
        s = Servidor("0.0.0.0", int(sys.argv[1]))
        s.initServer()
    except:
        print("use: python3 servidor.py port")
