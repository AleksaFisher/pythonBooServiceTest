import requests

class TestApiGet:
    def __init__(self, url, data):
        self.url = url
        self.data = data

    def GetBookInfo(self):
        response = None
        try:
            response = requests.get("{}/latest?limit={}".format(self.url, self.data)).json()
        except Exception:
            print("{}\n{}".format(response.status_code, response.json()))
        return response
