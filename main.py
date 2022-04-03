import datetime
import time
from test_books_service_api_class import *
import test_books_service_api


if __name__ == '__main__':
    ## How to use module example
    # added_bookid = test_books_service_api.addbook()
    # getinfo = test_books_service_api.getinformationaboutbook(1)
    # print("{}".format(getinfo))


    conObj = TestApiGet("http://127.0.0.1:5000/v1/books")
    getinfo = conObj.GetLatestBookInfo(1)
    print("{}".format(getinfo))




    bookObj = TestApiManipulation("http://127.0.0.1:5000/v1/books")
    date_add = datetime.date.today().strftime("%Y-%m-%d")
    add_data = {"type": "Science", "title": "#{}-Discoveries in the field of physics".format(time.time()),
                "creation_date": date_add}

    add_book = bookObj.AddBook(add_data)
    print("Book has been added:\n{}".format(add_book.json()))

    bookid = add_book.json()['id']

    rename_data = {'id': bookid, 'changes': {'id': bookid, 'type': 'Drama'}}
    rename_book = bookObj.RenameBook(rename_data)
    print("Result:\n{}".format(rename_book.json()))


