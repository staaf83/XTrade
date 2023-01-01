import socket
import ssl

from auth.data import AuthData

class APIConnection:
    def __init__(self):
        data = AuthData.getData(self, "data.bin")
        self.conn = ssl.create_default_context().wrap_socket(socket.create_connection((data["host"], data["port"])),server_hostname=data["host"])
    
  
    def connect(self):
        return self.conn

    def disconnect(self):
        self.conn.close
