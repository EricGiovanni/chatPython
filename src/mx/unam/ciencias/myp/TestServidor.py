import unittest
import threading
import Servidor
import Cliente

class TestServidor(unittest.TestCase):
    
    def testPruebaConeccion(self):
        try:
            self.assertRaises(Cliente.Cliente())
        except:
            pass
        #        accept = threading.Thread(target=self.acceptConnection())
        s = threading.Thread(target=Servidor("localhost", 50000))
        c = threading.Thread(target=Cliente("localhost", 50000))
        s.daemon = True
        s.start()
        c.daemon = True
        c.start()

    

if __name__ == "__main__":
    unittest.main()
