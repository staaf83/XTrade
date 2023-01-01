import json

class JSONUtils:
    
    def execute(data):
        msg = json.dumps(data)
        msg = msg.encode('utf-8')
        return msg
        #"""Wczytaj dane z pliku JSON."""
        #with open(filename, "r") as f:
        #    data = json.load(f)
       # return data

    def save_json(data, filename):
        """Zapisz dane do pliku JSON."""
        with open(filename, "w") as f:
            json.dump(data, f)

    
    def save_config(self):
        pass
        """Zapisz konfigurację do pliku."""
        #save_json(self.config, "config.json")









                #self.config = load_json("config.json")
        #self.api_client = APIClient(self.config["server_url"])