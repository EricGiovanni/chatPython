#!/usr/bin/env/python3
import unittest
import threading
import socket
import sys
import Usuario

class TestCliente(unittest.TestCase):

    def testGetConn(self):
        """
        Prueba unitaria para getConn
        """
        self.u = Usuario.Usuario("pruebaConexion", "User0", 0)
        self.assertEqual("pruebaConexion", self.u.getConn())
        self.u.setConn("cambioConexion")
        self.assertEqual("cambioConexion", self.u.getConn())
    
    def testGetNomUser(self):
        """
        Prueba unitaria para getNomUser
        """
        self.u = Usuario.Usuario("pruebaConexion", "User1", 1)
        self.assertEqual("User1", self.u.getNomUser())
        self.u.setNomUser("Usuario1")
        self.assertEqual("Usuario1", self.u.getNomUser())

    def testGetNumId(self):
        """
        Prueba unitaria para getNumId
        """
        self.u = Usuario.Usuario("pruebaConexion", "User2", 2)
        self.assertEqual(2, self.u.getNumId())
        self.u.setNumId(3)
        self.assertEqual(3, self.u.getNumId())

    def testSetConn(self):
        """
        Prueba unitaria para setConn
        """
        self.u = Usuario.Usuario("pruebaConexion", "User3", 3)
        self.assertEqual("pruebaConexion", self.u.getConn())
        self.u.setConn("cambioConexion2")
        self.assertEqual("cambioConexion2", self.u.getConn())
    
    def testSetNomUser(self):
        """
        Prueba unitaria para setNomUser
        """
        self.u = Usuario.Usuario("pruebaConexion", "User4", 4)
        self.assertEqual("User4", self.u.getNomUser())
        self.u.setNomUser("Usuario4")
        self.assertEqual("Usuario4", self.u.getNomUser())

    def testSetNumId(self):
        """
        Prueba unitaria para setNumId
        """
        self.u = Usuario.Usuario("pruebaConexion", "User5", 5)
        self.assertEqual(5, self.u.getNumId())
        self.u.setNumId(6)
        self.assertEqual(6, self.u.getNumId())
    
if __name__ == "__main__":
    unittest.main()