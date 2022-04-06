import requests


class TestApiDelete:
    def __init__(self, url):
        self.url = url

    def DeleteBook(self, data):
        response = None
        try:
            response = requests.delete("{}/manipulation?id={}".format(self.url, data))
            #print("{format(response.status_code}\nRemoved {response.json()}"))
            print("{}\nRemoved {}".format(response.status_code, response.json()))
        except Exception:
            print("{}\n{}".format(response.status_code, response.json()))
        return response
