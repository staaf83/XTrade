import pickle


class AuthData:
    def __init__(self):
        pass

    def setData(self, file, data):
        dataFile = self.getData(file)
        dataFile.update(data)
        with open(file, "wb") as f:
            pickle.dump(dataFile, f)

    def getData(self, file):
        try:
            with open(file, "rb") as f:
                data = pickle.load(f)
                return data
        except FileNotFoundError:
            return False
        except EOFError:
            return {"logged": False}

    def createFile(self):
        with open("data.bin", "wb") as f:
            pickle.dump({"logged": False}, f)

    def confirm_login(self, username, password):
        data = {
            "username": username,
            "password": password,
            "host": 'xapi.xtb.com',
            "port": 5124
        }
        open("data.bin", "wb").write(pickle.dumps(data))
        if True:
            # Login()
            pass
