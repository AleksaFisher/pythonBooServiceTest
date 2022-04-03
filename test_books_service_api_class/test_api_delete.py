import requests


class TestApiGet:
    def __init__(self, url, data):
        self.url = url
        self.data = data

    def BookDelete(self):
        response = None
        try:
            response = requests.delete("{}/manipulation?id={}".format(self.url, self.data))
            print("{}\nRemoved {}".format(response.status_code, response.json()))
        except Exception:
            print("{}\n{}".format(response.status_code, response.json()))
        return response
