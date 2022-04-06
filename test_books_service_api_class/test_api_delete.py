import requests


class TestApiDelete:
    def __init__(self, url):
        self.url = url

    def DeleteBook(self, data):
        """
        uses requests.delete method to call BooksService API to delete particular book
        data: string - id of book to delete
        return
        response: object - object returned by requests.delete, including api json response & satus code
        """
        response = None
        try:
            response = requests.delete(f"{self.url}/manipulation?id={data}")
            #print("{format(response.status_code}\nRemoved {response.json()}"))
            print("{}\nRemoved {}".format(response.status_code, response.json()))
        except Exception:
            print("{}\n{}".format(response.status_code, response.json()))
        return response
