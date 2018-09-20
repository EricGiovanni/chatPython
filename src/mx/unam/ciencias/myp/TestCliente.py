#!/usr/bin/env/python3
import unittest
import threading
import socket
import sys
import Cliente
import Servidor

class TestCliente(unittest.TestCase):

    def testSetUserAddress(self):
        """
        Prueba unitaria para setUserAddress
        """
        self.cliente = Cliente.Cliente("localhost", 1)
        self.cliente.setUserAddress(("localhost",1))
        self.assertEqual(("localhost",1), self.cliente.getUserAddress())
        self.cliente.cerrarSocket()

    def testGetUserAddress(self):
        """
        Prueba unitaria para getUserAddress
        """
        self.cliente = Cliente.Cliente("localhost", 2)
        self.cliente.setUserAddress(("localhost",2))
        self.assertEqual(("localhost",2), self.cliente.getUserAddress())
        self.cliente.cerrarSocket()

    def testSetSock(self):
        """
        Prueba unitaria para setSock
        """
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cliente = Cliente.Cliente("localhost", 3)
        self.cliente.setSock(self.sock)
        self.assertEqual(self.sock, self.cliente.getSock())
        self.sock.close()
        self.cliente.cerrarSocket()

    def testGetEstado(self):
        """
        Prueba unitaria para getEstado
        """
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cliente = Cliente.Cliente("localhost", 4)
        self.cliente.setSock(self.sock)
        self.assertEqual(self.sock, self.cliente.getSock())
        self.sock.close()
        self.cliente.cerrarSocket()

    def testSetEstado(self):
        """
        Prueba unitaria para setEstado
        """
        self.cliente = Cliente.Cliente("localhost", 5)
        self.cliente.setEstado("AWAY")
        self.assertEqual("AWAY", self.cliente.getEstado())
        self.cliente.cerrarSocket()

    def testGetSock(self):
        """
        Prueba unitaria para getSock
        """
        self.cliente = Cliente.Cliente("localhost", 6)
        self.cliente.setEstado("BUSY")
        self.assertEqual("BUSY", self.cliente.getEstado())
        self.cliente.cerrarSocket()
    
if __name__ == "__main__":
    unittest.main()