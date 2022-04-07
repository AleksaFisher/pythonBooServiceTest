import datetime
import time
from test_books_service_api_class import test_book_service_api_classes
#import test_books_service_api


def test_add_book():
    book_object = test_book_service_api_classes("http://127.0.0.1:5000/v1/books")
    date_add = datetime.date.today().strftime("%Y-%m-%d")
    data = {"type": "Science", "title": "#{}-Discoveries in the field of physics".format(time.time()),
            "creation_date": date_add}
    result = book_object.add_book(data)
    assert result.status_code == 200


def test_add_book_characters_name():
    book_object = test_book_service_api_classes("http://127.0.0.1:5000/v1/books")
    date_add = datetime.date.today().strftime("%Y-%m-%d")
    dt_add_book = {"title": "\.,"}
    result = book_object.add_book(dt_add_book)

    assert result.status_code == 200


def test_add_book_characters_type():
    book_object = test_book_service_api_classes("http://127.0.0.1:5000/v1/books")
    date_add = datetime.date.today().strftime("%Y-%m-%d")
    dt_add_book = {"type": "\.,"}
    result = book_object.add_book(dt_add_book)

    assert result.status_code == 200


def test_add_empty_book():
    book_object = test_book_service_api_classes("http://127.0.0.1:5000/v1/books")
    date_add = datetime.date.today().strftime("%Y-%m-%d")
    data = {"type": "", "title": "", "creation_date": date_add}
    result = book_object.add_book(data)

    assert result.status_code == 200


def test_delete_book():
    book_id = "d87f4b4a-908d-48e7-bc0d-7da2850d3f1a"
    book_object = test_book_service_api_classes("http://127.0.0.1:5000/v1/books")
    result = book_object.delete_book(book_id)
    assert result.status_code == 200


def test_get_info_book():
    book_object = test_book_service_api_classes("http://127.0.0.1:5000/v1/books")
    dict_params = "Scidence"
    result = book_object.get_book_info_by_type(dict_params)
    assert result.status_code == 200


def test_get_info_book_with_id():
    book_object = test_book_service_api_classes("http://127.0.0.1:5000/v1/books")
    dict_params = "6bfc01c4-7100-4a06-b02b-7305a3f44949"
    result = book_object.get_book_info_by_id(dict_params)
    assert result.status_code == 200


def test_get_info_book_latest():
    book_object = test_book_service_api_classes("http://127.0.0.1:5000/v1/books")
    dict_params = 10000
    result = book_object.get_latest_book_info(dict_params)
    assert result.status_code == 200


def test_rename_book():
    book_id = "6bfc01c4-7100-4a06-b02b-7305a3f44949"
    rename_data = {'id': book_id, 'changes': {'id': book_id, 'type': 'Drama'}}
    book_object = test_book_service_api_classes("http://127.0.0.1:5000/v1/books")
    result = book_object.rename_book(rename_data)
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
    added_bookid = test_book_service_api_classes.add_book()
    get_info = test_book_service_api_classes.get_information_about_book(1)
    print("{}".format(get_info))

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
