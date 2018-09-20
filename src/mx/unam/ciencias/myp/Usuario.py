class Usuario: 
    def __init__(self, conn, nomUser, numId):
        self.conn = conn
        self.nomUser = nomUser
        self.numId = numId
    
    def getConn(self):
        return self.conn
    
    def getNomUser(self):
        return self.nomUser

    def getNumId(self):
        return self.numId

    def setConn(self, conn):
        self.conn = conn
    
    def setNomUser(self, nomUser):
        self.nomUser = nomUser

    def setNumId(self, numId):
        self.numId = numId
