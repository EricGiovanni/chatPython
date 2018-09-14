import unittest
import threading
import socket
import sys
import Cliente
import Servidor

class TestServidor(unittest.TestCase):

    def testSetSock(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servidor = Servidor.Servidor("localhost", 1)
        self.servidor.setSock(self.sock)
        self.assertEqual(self.sock, self.servidor.getSock())
        self.sock.close()
        self.servidor.cerrarSocket()
    
    def testGetSock(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servidor = Servidor.Servidor("localhost", 2)
        self.servidor.setSock(self.sock)
        self.assertEqual(self.sock, self.servidor.getSock())
        self.sock.close()
        self.servidor.cerrarSocket()

    def testSetServer(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servidor = Servidor.Servidor("localhost", 3)
        self.serv = (("localhost"), 12345)
        self.servidor.setServer((str("localhost"), 12345))
        self.assertEqual(self.serv, self.servidor.getServer())
        self.sock.close()
        self.servidor.cerrarSocket()

    def testGetServer(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servidor = Servidor.Servidor("localhost", 4)
        self.serv = (("localhost"), 123456)
        self.servidor.setServer((str("localhost"), 123456))
        self.assertEqual(self.serv, self.servidor.getServer())
        self.sock.close()
        self.servidor.cerrarSocket()

if __name__ == "__main__":
    unittest.main()