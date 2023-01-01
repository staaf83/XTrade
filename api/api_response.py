class APIResponce:
    def __init__(self):
        dataFromServer = self.connection.connect().recv(4096).decode()

        