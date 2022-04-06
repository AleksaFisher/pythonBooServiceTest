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
    bookid = "d87f4b4a-908d-48e7-bc0d-7da2850d3f1a"
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


#
#     params = "55297037-e455-4be5-b131-55d4b25df6e0"
#     #response = requests.get("http://127.0.0.1:5000/v1/books/info?id={}".format(params))
#    # print("{}\n{}".format(response.status_code, response.json()))
#    # if response.status_code == 200:
#     #    print("Resp {}".format(response.url))
#      #   print("{}".format(response.json()['type']))
#         #print("Я кодер")
#     #else:
#         #print("Я Г-кодер")
#      #   print(response.status_code)

if __name__ == '__main__':
    # test_add_book()
    # test_add_empty_book()

    ## How to use module example
    added_bookid = test_books_service_api.addbook()
    getinfo = test_books_service_api.getinformationaboutbook(1)
    print("{}".format(getinfo))

    # conObj = TestApiGet("http://127.0.0.1:5000/v1/books")
    # getinfo = conObj.GetLatestBookInfo(1)
    # print("{}".format(getinfo))
    #
    #
    #
    #
    # bookObj = TestApiManipulation("http://127.0.0.1:5000/v1/books")
    # #test adding normal book
    # date_add = datetime.date.today().strftime("%Y-%m-%d")
    # add_data = {"type": "Science", "title": "#{}-Discoveries in the field of physics".format(time.time()),
    #             "creation_date": date_add}
    #
    # add_book = bookObj.AddBook(add_data)
    # print("Book has been added:\n{}".format(add_book.json()))
    #
    # #test_addming empy book
    # add_data_epmty = {"type": "", "title": "#{}-Discoveries in the field of physics".format(time.time()),
    #             "creation_date": date_add}
    # add_book_empty = bookObj.AddBook(add_data_epmty)
    # print("Book has been added:\n{}".format(add_book_empty.json()))
    #
    # #test adding  wrong book
    # add_data_wrong = {"type": "", "title": "#{}-Discoveries in the field of physics".format(time.time()),
    #             "creation_date": date_add}
    # add_book_wrong = bookObj.AddBook(add_data_wrong)
    # print("Book has been added:\n{}".format(add_book_wrong.json()))
    #
    #
    # # test renaming book
    # bookid = add_book.json()['id']
    #
    # rename_data = {'id': bookid, 'changes': {'id': bookid, 'type': 'Drama'}}
    # rename_book = bookObj.RenameBook(rename_data)
    # print("Result:\n{}".format(rename_book.json()))
    #
