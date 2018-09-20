#!/usr/bin/env/python3
import unittest
import threading
import socket
import sys
import Room

class TestCliente(unittest.TestCase):

    def testSetNombre(self):
        self.r = Room.Room([], "Principal")
        self.assertEqual("Principal", self.r.getNombre())
        self.r.setNombre("Prueba")
        self.assertEqual("Prueba", self.r.getNombre())

    def testGetNombre(self):
        self.r = Room.Room([], "Principal2")
        self.assertEqual("Principal2", self.r.getNombre())
        self.r.setNombre("Prueba2")
        self.assertEqual("Prueba2", self.r.getNombre())

    def testSetClientes(self):
        self.r = Room.Room([], "Principal")
        self.assertEqual([], self.r.getClientes())
        self.lista =[("pruebaSocket", "Prueba3", 1)]
        self.r.setClientes(self.lista)
        self.assertEqual(self.lista, self.r.getClientes())
    
    def testGetClientes(self):
        self.r = Room.Room([], "Principal2")
        self.assertEqual([], self.r.getClientes())
        self.lista =[("pruebaSocket2", "Prueba4", 1)]
        self.r.setClientes(self.lista)
        self.assertEqual(self.lista, self.r.getClientes())
    
if __name__ == "__main__":
    unittest.main()