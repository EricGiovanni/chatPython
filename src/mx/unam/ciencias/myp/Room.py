import socket
import threading
import sys
import pickle

class Room:
    def __init__(self, clientes, nombre):
        """
        Constructor que inicializa la lista de clientes que 
        contendrá el room y el nombre de dicho room
        """
        self.clientes = clientes
        self.nombre = nombre


    def setNombre(self, nombre):
        """
        Metodo que te permite poner el nombre del room
        """
        self.nombre = nombre

    def getNombre(self):
        """
        Metodo que te permite obtener el nombre del room
        """
        return self.nombre

    def setClientes(self, clientes):
        """
        Metodo que te permite cambiar la lista de clientes
        """
        self.clientes = clientes
    
    def getClientes(self):
        """
        Metodo que te permite obtener la lista de clientes
        """
        return self.clientes

    def enviarMsg(self, msg, cliente):
        """
        Metodo que te permite enviar mensaje a todos los clientes 
        del room
        """
        for c in self.clientes:
            try:
                if c[0] != cliente:
                    c[0].send(msg)
            except:
                self.clientes.remove(c)
    
    def agregarCliente(self, cliente):
        """
        Metodo que te permite agregar clientes al room
        """
        self.clientes.append(cliente)

    def numClientes(self):
        """
        Metodo que te devuelve el numero de clientes
        """
        return len(self.clientes)
