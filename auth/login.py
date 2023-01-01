from api.api_client import APIClient
from utils.json_utils import JSONUtils
import pickle
from auth.data import AuthData

class Login:

    def __init__(self):
        data = AuthData.getData(self, "data.bin")
        loginRequest = JSONUtils().execute(dict([('command', 'login'), ('arguments', dict(userId=data["username"], password=data["password"], appName='XTrade'))]))
        #APIClient().sendRequest(loginRequest)






#do zrobienia
    def login(self, username, password):
        """Zaloguj się do aplikacji."""
        data = {"username": username, "password": password}
        response = self.api_client.send_request("login", data)
        if response.status_code == 200:
            return True
        else:
            log_error(response.error)
            self.login_win.show_error()
            return False






