
import socket
import array
import sys

ServerAddress = "127.0.0.1"
ServerPort = 3145 

VersionZero = 0
ConnectRequestType = 0
ListType = 1

def parse(bs):
    version = bs[0]
    if version == VersionZero:
        t = bs[1]    
        if t == ConnectRequestType:
            pass
        elif t == ListType:
            pass
        else:
            raise SystemExit(f"Unknown server response type: {t}")
    else:
        raise SystemExit(f"Unknown server response version: {t}")

def concat(items):
    ret = array.array('B') 
    for item in items:
        ret.frombytes(item)
    return ret.tobytes()

def create_connect_request():
    return concat([byte(VersionZero), byte(ConnectRequestType)])
    
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
