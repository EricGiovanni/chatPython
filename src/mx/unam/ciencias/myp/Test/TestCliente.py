import unittest

class TestCliente(unittest.TestCase):
    def setUp(self):
        self.cliente = Cliente()

    def test_getHola(self):
        prueba = "hola"
        self.assertEquals(prueba,"hola")

if __name__ == "__main__":
    unittest.main()
