
import socket

ServerAddress = "0.0.0.0"
ServerPort = 80

ConnectRequest = 0



    
class Server:

    def __init__(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        #self._socket.connect((ServerAddress, ServerPort))
        pass
    
    def queue_request(self, request):
        pass

    def send_requests(self):
        pass

    def query_updates(self):
        pass