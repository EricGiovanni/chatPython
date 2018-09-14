import unittest
import threading
import socket
import sys
import Cliente
import Servidor

class TestCliente(unittest.TestCase):

    def testSetUserAddress(self):
        self.cliente = Cliente.Cliente("localhost", 1)
        self.cliente.setUserAddress(("localhost",1))
        self.assertEqual(("localhost",1), self.cliente.getUserAddress())
        self.cliente.cerrarSocket()

    def testGetUserAddress(self):
        self.cliente = Cliente.Cliente("localhost", 2)
        self.cliente.setUserAddress(("localhost",2))
        self.assertEqual(("localhost",2), self.cliente.getUserAddress())
        self.cliente.cerrarSocket()
    
if __name__ == "__main__":
    unittest.main()