
import socket
import array
import sys
import struct

ServerAddress = "127.0.0.1"
ServerPort = 3145 

VersionZero = 0
ConnectRequestType = 0


def create_connect_request():
    return struct.pack('BB', VersionZero, ConnectRequestType) 
    
class Server:

    def __init__(self):
        pass
        #self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        #todo timeout, exception
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((ServerAddress, ServerPort))
            sock.sendall(create_connect_request())
            print('blarg99')
            data = sock.recv(2048)
            print('blarg1000')
            return data

    def queue_request(self, request):
        pass

    def send_requests(self):
        pass

    def query_updates(self):
        pass
