import requests
import test_add_book

def delete_book(bookid):
     response = requests.delete("http://127.0.0.1:5000/v1/books/manipulation?id={}".format(bookid))
     print("{}\nRemoved {}".format(response.status_code, response.json()))
