import socket
import threading
import sys
import pickle

class Room:
    def __init__(self, clientes, nombre):
        self.clientes = clientes
        self.nombre = nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setClientes(self, clientes):
        self.clientes = clientes
    
    def getClientes(self):
        return self.clientes

    def enviarMsg(self, msg, cliente):
        for c in self.clientes:
            try:
                if c[0] != cliente:
                    c[0].send(msg)
            except:
                self.clientes.remove(c)

    def recibirMsg(self, clientes):
        self.clientes = clientes
    
    def agregarCliente(self, cliente):
        self.clientes.append(cliente)

    def numClientes(self):
        return len(self.clientes)
