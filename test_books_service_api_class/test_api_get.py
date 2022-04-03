import requests


class TestApiGet:
    def __init__(self, url):
        self.url = url

    def GetLatestBookInfo(self, data):
        response = None
        try:
            response = requests.get("{}/latest?limit={}".format(self.url, data)).json()
        except Exception:
            print("{}\n{}".format(response.status_code, response.json()))
        return response

    def GetBookInfoByType(self, data):
        response = None
        try:
            response = requests.get("{}/ids?book_type={}".format(self.url, data)).json()
        except Exception:
            print("{}\n{}".format(response.status_code, response.json()))
        return response

    def GetBookInfoById(self, data):
        response = None
        try:
            response = requests.get("{}/info?id={}".format(self.url, data)).json()
        except Exception:
            print("{}\n{}".format(response.status_code, response.json()))
        return response
