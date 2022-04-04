import requests


class TestApiManipulation:
    def __init__(self, url):
        self.url = url

    def AddBook(self, data):
        # date_add = datetime.date.today().strftime("%Y-%m-%d")
        # dt_add_book = {"type": "Science", "title": "#{}-Discoveries in the field of physics".format(time.time()),
        #            "creation_date": date_add}

        try:
            response = requests.post("{}/manipulation".format(self.url), json=data)

        except Exception:
            print("{}\n{}".format(response.status_code, response.json()))
        return response

    def RenameBook(self, data):
        bookid = data['id']
        new_book_data = data['changes']
        try:
            response = requests.put("{}/manipulation?id={}".format(self.url, bookid), json=new_book_data)

        except Exception:
            print("{}\n{}".format(response.status_code, response.json()))
        return response
