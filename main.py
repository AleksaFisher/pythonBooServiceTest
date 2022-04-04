import datetime
import time
from test_books_service_api_class import *
import test_books_service_api


def test_add_book():

    bookObject = TestApiManipulation("http://127.0.0.1:5000/v1/books")
    date_add = datetime.date.today().strftime("%Y-%m-%d")
    data = {"type": "Science", "title": "#{}-Discoveries in the field of physics".format(time.time()),
            "creation_date": date_add}
    result = bookObject.AddBook(data)
    assert result.status_code == 200


def test_addbookcharactersname():
    bookObject = TestApiManipulation("http://127.0.0.1:5000/v1/books")
    date_add = datetime.date.today().strftime("%Y-%m-%d")
    dt_add_book = {"title": "\.,"}
    result = bookObject.AddBook(dt_add_book)

    assert result.status_code == 200

def test_addbookcharacterstype():
    bookObject = TestApiManipulation("http://127.0.0.1:5000/v1/books")
    date_add = datetime.date.today().strftime("%Y-%m-%d")
    dt_add_book = {"type": "\.,"}
    result = bookObject.AddBook(dt_add_book)

    assert result.status_code == 200

def test_add_empty_book():

    bookObject = TestApiManipulation("http://127.0.0.1:5000/v1/books")
    date_add = datetime.date.today().strftime("%Y-%m-%d")
    data = {"type": "", "title": "", "creation_date": date_add}
    result = bookObject.AddBook(data)

    assert result.status_code == 200


def test_delete_book():
    bookid="d87f4b4a-908d-48e7-bc0d-7da2850d3f1a"
    bookObject = TestApiDelete("http://127.0.0.1:5000/v1/books")
    result = bookObject.DeleteBook(bookid)
    assert result.status_code == 200

def test_getinfobook():

    bookObject = TestApiGet("http://127.0.0.1:5000/v1/books")
    dict_params = "Scidence"
    result = bookObject.GetBookInfoByType(dict_params)
    assert result.status_code == 200

def test_getinfobookwithid():
    bookObject = TestApiGet("http://127.0.0.1:5000/v1/books")
    dict_params = "6bfc01c4-7100-4a06-b02b-7305a3f44949"
    result = bookObject.GetBookInfoById(dict_params)
    assert result.status_code == 200

def test_getinfobooklatest():
    bookObject = TestApiGet("http://127.0.0.1:5000/v1/books")
    dict_params = 10000
    result = bookObject.GetLatestBookInfo(dict_params)
    assert result.status_code == 200

def test_renamebook():
    bookid = "6bfc01c4-7100-4a06-b02b-7305a3f44949"
    rename_data = {'id': bookid, 'changes': {'id': bookid, 'type': 'Drama'}}
    bookObject = TestApiManipulation("http://127.0.0.1:5000/v1/books")
    result = bookObject.RenameBook(rename_data)
    assert result.status_code == 200


if __name__ == '__main__':

 ## How to use module example
    added_bookid = test_books_service_api.addbook()
    getinfo = test_books_service_api.getinformationaboutbook(1)
    print("{}".format(getinfo))



