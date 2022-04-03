import requests


class TestApiManipulation:
    def __init__(self, url, data):
        self.url = url
        self.data = data

    def AddBook(self):
        # date_add = datetime.date.today().strftime("%Y-%m-%d")
        # dt_add_book = {"type": "Science", "title": "#{}-Discoveries in the field of physics".format(time.time()),
        #            "creation_date": date_add}
        bookid = None
        try:
            response = requests.post("{}/manipulation".format(self.url), json=self.data)
            bookid = response.json()['id']

        except Exception:
            print("{}\n{}".format(response.status_code, response.json()))
        return bookid, response


# def addbookemptyname():
#     date_add = datetime.date.today().strftime("%Y-%m-%d")
#     dt_add_book = {"type": "", "title": "", "creation_date": ""}
#     getid = None
#     try:
#         response = requests.post("http://127.0.0.1:5000/v1/books/manipulation", json=dt_add_book)
#         print("{}\n{}".format(response.status_code, response.json()))
#         getid = response.json()['id']
#         print("{}".format(getid))
#     except:
#         print("{}\n{}".format(response.status_code, response.json()))
#     return (getid)


# def addbookcharactersname():
#     date_add = datetime.date.today().strftime("%Y-%m-%d")
#     dt_add_book = {"type": "\.,", "title": "\.,", "creation_date": "\.,"}
#     getid = None
#     try:
#         response = requests.post("http://127.0.0.1:5000/v1/books/manipulation", json=dt_add_book)
#         print("{}\n{}".format(response.status_code, response.json()))
#         getid = response.json()['id']
#         print("{}".format(getid))
#     except:
#         print("{}\n{}".format(response.status_code, response.json()))
#     return (getid)
