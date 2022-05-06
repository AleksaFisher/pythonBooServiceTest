import datetime
import time
import pytest

from test_books_service_api_class import api_classes
from api_classes import ApiClass


class TestApiClass:
    url = "http://127.0.0.1:5000/v1/books"
    @pytest.fixture(scope="function")
    def setup_method(self):
        try:
            check = ApiClass(self.url).check_connection()
            if not check.status_code == 200:
                raise Exception
        except Exception as error:
            print(f"{error}")




    def test_add_book(self):
        book_object = ApiClass(self.url)
        date_add = datetime.date.today().strftime("%Y-%m-%d")
        data = {"type": "Science", "title": "#{}-Discoveries in the field of physics".format(time.time()),
                "creation_date": date_add}
        result = book_object.add_book(data)
        print("{}\n{}".format(result.status_code, result.json()))
        assert result.status_code == 200

    def test_add_book_characters_name(self):
        book_object = ApiClass(self.url)
        date_add = datetime.date.today().strftime("%Y-%m-%d")
        dt_add_book = {"title": "\.,", "type": "Drama"}
        result = book_object.add_book(dt_add_book)

        assert result.status_code == 200

    def test_add_book_characters_type(self):
        book_object = ApiClass(self.url)
        date_add = datetime.date.today().strftime("%Y-%m-%d")
        dt_add_book = {"type": "\.,", "title": "Drama"}
        result = book_object.add_book(dt_add_book)

        assert result.status_code == 400

    def test_add_empty_namebook(self):
        book_object = ApiClass(self.url)
        date_add = datetime.date.today().strftime("%Y-%m-%d")
        data = {"type": "Drama", "title": "", "creation_date": date_add}
        result = book_object.add_book(data)
        assert result.status_code == 200

    def test_add_empty_typebook(self):
        book_object = ApiClass(self.url)
        date_add = datetime.date.today().strftime("%Y-%m-%d")
        data = {"type": "", "title": "Fantastic", "creation_date": date_add}
        result = book_object.add_book(data)
        assert result.status_code == 400

   # def test_delete_book(self):
    #    book_id = "6c311eaa-3166-4bb7-aa7a-55c9b2df736b"
    #    book_object = ApiClass(self.url)
    #    result = book_object.delete_book(book_id)
     #   assert result.status_code == 200

    def test_get_info_book(self):
        book_object = ApiClass(self.url)
        dict_params = "Science"
        result = book_object.get_book_info_by_type(dict_params)
        assert result.status_code == 200

    def test_get_info_book_with_id(self):
        book_object = ApiClass(self.url)
        dict_params = "ce347686-e531-4224-8a02-ab236c7babc6"
        result = book_object.get_book_info_by_id(dict_params)
        assert result.status_code == 200

    def test_get_info_book_latest(self):
        book_object = ApiClass(self.url)
        dict_params = 10000
        result = book_object.get_latest_book_info(dict_params)
        assert result.status_code == 200

    def test_rename_book(self):
        book_id = "ce347686-e531-4224-8a02-ab236c7babc6"
        rename_data = {'id': book_id, 'changes': {'id': book_id, 'type': 'Drama'}}
        book_object = ApiClass(self.url)
        result = book_object.rename_book(rename_data)
        assert result.status_code == 200




#def test_books_service():
   # b = TestApiClass("http://127.0.0.1:5000/v1/books")
   # b.t_add_book()
   # b.t_get_info_book_with_id()




# def t_selenium_case1():
#     TestCase1()
