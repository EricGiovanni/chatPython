import socket
import threading
import sys
import pickle

class Cliente:

    def __init__(self, host, port):

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        userAddress = (str(host), int(port))
        try:
            self.sock.connect(userAddress)
        except:
            print("Error de conexión")
            sys.exit()

        msgRecv = threading.Thread(target=self.msgRecv)
        msgRecv.daemon = True
        msgRecv.start()

        while True:
            msg = input("Mensaje: ")
            if msg != "salir":
                self.sendMsg(msg)
            else:
                self.sock.close()
                sys.exit()


    def sendMsg(self, msg):
        self.sock.send(pickle.dumps(msg))

    def msgRecv(self):
        while True:
            try:
                data = self.sock.recv(1024)
                if data:
                    print("Mensaje: " + pickle.loads(data))
            except:
                pass

try:
    c = Cliente(sys.argv[1], sys.argv[2])
except:
    print(" Use: python3 cliente.py host port")