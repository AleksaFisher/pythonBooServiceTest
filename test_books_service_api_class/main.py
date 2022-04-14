import datetime
import time
import pytest
from test_books_service_api_class import ApiClass
# from Case_with_Selenium import TestCase1




class TestApiClass:
    def __init__(self, url):
        self.url = url


    def setup_method(self, method):
        try:
            check = ApiClass(self.url).check_connection()
            if not check.status_code == 200:
                raise Exception
        except Exception as error:
            print(f"{error}")
        # assert check is not None
        # assert check.status_code == 200



    def t_add_book(self):
        book_object = ApiClass(self.url)
        date_add = datetime.date.today().strftime("%Y-%m-%d")
        data = {"type": "Science", "title": "#{}-Discoveries in the field of physics".format(time.time()),
                "creation_date": date_add}
        result = book_object.add_book(data)
        assert result.status_code == 200

    def t_add_book_characters_name(self):
        book_object = ApiClass(self.url)
        date_add = datetime.date.today().strftime("%Y-%m-%d")
        dt_add_book = {"title": "\.,"}
        result = book_object.add_book(dt_add_book)

        assert result.status_code == 200

    def t_add_book_characters_type(self):
        book_object = ApiClass(self.url)
        date_add = datetime.date.today().strftime("%Y-%m-%d")
        dt_add_book = {"type": "\.,"}
        result = book_object.add_book(dt_add_book)

        assert result.status_code == 200

    def t_add_empty_book(self):
        book_object = ApiClass(self.url)
        date_add = datetime.date.today().strftime("%Y-%m-%d")
        data = {"type": "", "title": "", "creation_date": date_add}
        result = book_object.add_book(data)
        assert result.status_code == 200

    def t_delete_book(self):
        book_id = "d87f4b4a-908d-48e7-bc0d-7da2850d3f1a"
        book_object = ApiClass(self.url)
        result = book_object.delete_book(book_id)
        assert result.status_code == 200

    def t_get_info_book(self):
        book_object = ApiClass(self.url)
        dict_params = "Science"
        result = book_object.get_book_info_by_type(dict_params)
        assert result.status_code == 200

    def t_get_info_book_with_id(self):
        book_object = ApiClass(self.url)
        dict_params = "6bfc01c4-7100-4a06-b02b-7305a3f44949"
        result = book_object.get_book_info_by_id(dict_params)
        assert result.status_code == 200

    def t_get_info_book_latest(self):
        book_object = ApiClass(self.url)
        dict_params = 10000
        result = book_object.get_lat_book_info(dict_params)
        assert result.status_code == 200

    def t_rename_book(self,setup):
        book_id = "6bfc01c4-7100-4a06-b02b-7305a3f44949"
        rename_data = {'id': book_id, 'changes': {'id': book_id, 'type': 'Drama'}}
        book_object = ApiClass(self.url)
        result = book_object.rename_book(rename_data)
        assert result.status_code == 200




def test_books_service():
    b = TestApiClass("http://127.0.0.1:5000/v1/books")
    b.t_get_info_book_with_id()




# def t_selenium_case1():
#     TestCase1()
