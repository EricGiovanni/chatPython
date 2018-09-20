class Usuario: 
    def __init__(self, conn, nomUser, numId):
        """
        Constructor que inicializa la conexion del usuario, 
        el nombre de usuario y el numero de ID
        """
        self.conn = conn
        self.nomUser = nomUser
        self.numId = numId
    
    def getConn(self):
        """
        Metodo que obtiene la conexion (host, port)
        """
        return self.conn
    
    def getNomUser(self):
        """
        Metodo que obtiene el nombre de usuario
        """
        return self.nomUser

    def getNumId(self):
        """
        Metodo que obtiene el numero de ID
        """
        return self.numId

    def setConn(self, conn):
        """
        Metodo que te permite cambiar la conexion (host, port)
        """
        self.conn = conn
    
    def setNomUser(self, nomUser):
        """
        Metoodo que te permite cambiar el nombre de usuario
        """
        self.nomUser = nomUser

    def setNumId(self, numId):
        """
        Metodo que te permite cambiar el ID
        """
        self.numId = numId
