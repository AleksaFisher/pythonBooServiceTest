import requests


class TestApiDelete:
    def __init__(self, url, data):
        self.url = url
        self.data = data

    def DeleteBook(self):
        response = None
        try:
            response = requests.delete("{}/manipulation?id={}".format(self.url, self.data))
            print("{}\nRemoved {}".format(response.status_code, response.json()))
        except Exception:
            print("{}\n{}".format(response.status_code, response.json()))
        return response
