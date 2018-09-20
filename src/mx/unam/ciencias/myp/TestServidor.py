#!/usr/bin/env/python3
import unittest
import threading
import socket
import sys
import Cliente
import Servidor

class TestServidor(unittest.TestCase):

    def testSetSock(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servidor = Servidor.Servidor("0.0.0.0", 1)
        self.servidor.setSock(self.sock)
        self.assertEqual(self.sock, self.servidor.getSock())
        self.sock.close()
        self.servidor.cerrarSocket()
    
    def testGetSock(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servidor = Servidor.Servidor("0.0.0.0", 2)
        self.servidor.setSock(self.sock)
        self.assertEqual(self.sock, self.servidor.getSock())
        self.sock.close()
        self.servidor.cerrarSocket()

    def testSetServer(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servidor = Servidor.Servidor("0.0.0.0", 3)
        self.serv = (("0.0.0.0"), 12345)
        self.servidor.setServer((str("0.0.0.0"), 12345))
        self.assertEqual(self.serv, self.servidor.getServer())
        self.sock.close()
        self.servidor.cerrarSocket()

    def testGetServer(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servidor = Servidor.Servidor("0.0.0.0", 4)
        self.serv = (("0.0.0.0"), 123456)
        self.servidor.setServer((str("0.0.0.0"), 123456))
        self.assertEqual(self.serv, self.servidor.getServer())
        self.sock.close()
        self.servidor.cerrarSocket()

    def testAumentaID(self):
        self.servidor = Servidor.Servidor("0.0.0.0", 5)
        self.assertEqual(0, self.servidor.getID())
        self.servidor.aumentaID()
        self.assertEqual(1, self.servidor.getID())
        self.servidor.cerrarSocket()
    
    def testAumentaNumUser(self):
        self.servidor = Servidor.Servidor("0.0.0.0", 6)
        self.assertEqual("User0", self.servidor.getNumUser())
        self.servidor.aumentaID()
        self.servidor.aumentaNumUser()
        self.assertEqual("User1", self.servidor.getNumUser())
        self.servidor.cerrarSocket()

    def testGetID(self):
        self.servidor = Servidor.Servidor("0.0.0.0", 7)
        self.assertEqual(0, self.servidor.getID())
        self.servidor.aumentaID()
        self.assertEqual(1, self.servidor.getID())
        self.servidor.cerrarSocket()

    def testGetNumUser(self):
        self.servidor = Servidor.Servidor("0.0.0.0", 8)
        self.assertEqual("User0", self.servidor.getNumUser())
        self.servidor.aumentaID()
        self.servidor.aumentaNumUser()
        self.assertEqual("User1", self.servidor.getNumUser())
        self.servidor.cerrarSocket()

    def testSetNumUser(self):
        self.servidor = Servidor.Servidor("0.0.0.0", 9)
        self.assertEqual("User0", self.servidor.getNumUser())
        self.servidor.setNumUser("Hola")
        self.assertEqual("Hola", self.servidor.getNumUser())
        self.servidor.cerrarSocket()

if __name__ == "__main__":
    unittest.main()