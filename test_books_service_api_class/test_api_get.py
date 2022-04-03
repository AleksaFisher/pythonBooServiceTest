import requests


class TestApiGet:
    def __init__(self, url, data):
        self.url = url
        self.data = data

    def GetLatestBookInfo(self):
        response = None
        try:
            response = requests.get("{}/latest?limit={}".format(self.url, self.data)).json()
        except Exception:
            print("{}\n{}".format(response.status_code, response.json()))
        return response

    def GetBookInfoByType(self):
        response = None
        try:
            response = requests.get("{}/ids?book_type={}".format(self.url, self.data)).json()
        except Exception:
            print("{}\n{}".format(response.status_code, response.json()))
        return response

    def GetBookInfoById(self):
        response = None
        try:
            response = requests.get("{}/info?id={}".format(self.url, self.data)).json()
        except Exception:
            print("{}\n{}".format(response.status_code, response.json()))
        return response
