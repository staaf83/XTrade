from api.api_connection import APIConnection

class APIClient:

    def sendRequest(self, msg):
        sent = 0
        while sent < len(msg):
            sent += APIConnection().connect().send(msg[0:])
            print('Sent: ' + str(msg))
            
   


        