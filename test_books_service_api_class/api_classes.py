import requests


class ApiClass:
    def __init__(self, url):
        self.url = url

    def delete_book(self, data):
        """
        uses requests.delete method to call BooksService API to delete particular book
        data: string - id of book to delete
        return
        response: object - object returned by requests.delete, including api json response & satus code
        """
        response = None
        try:
            response = requests.delete(f"{self.url}/manipulation?id={data}")
            # print("{format(response.status_code}\nRemoved {response.json()}"))
            print("{}\nRemoved {}".format(response.status_code, response.json()))
        except Exception:
            print(f"{response.status_code}\n{response.json()}")
        #  print("{}\n{}".format(response.status_code, response.json()))
        return response

    # class test_api_get:
    # def __init__(self, url):
    #   self.url = url

    def get_latest_book_info(self, data):
        """
        uses requests.get method to call BooksService API to get info latest book
        data: string - id of book to latest
        return
        response: object - object returned by requests.get, including api json response & satus code
        """

        response = None
        try:
            response = requests.get("{}/latest?limit={}".format(self.url, data))
        except Exception:
            print(f"{response.status_code}\n{response.json()}")
        #  print("{}\n{}".format(response.status_code, response.json()))
        return response

    def get_book_info_by_type(self, data):
        """
        uses requests.get method to call BooksService API to get info by type book
        data: string - id of book to type
        return
        response: object - object returned by requests.get, including api json response & satus code
        """
        response = None
        try:
            response = requests.get("{}/ids?book_type={}".format(self.url, data))

        except Exception:
            print(f"{response.status_code}\n{response.json()}")
            # print("{}\n{}".format(response.status_code, response.json()))
        return response

    def get_book_info_by_id(self, data):
        """
        uses requests.get method to call BooksService API to get info by id book
        data: string - id of book
        return
        response: object - object returned by requests.get, including api json response & satus code
        """

        response = None
        try:
            response = requests.get("{}/info?id={}".format(self.url, data))
        except Exception:
            print(f"{response.status_code}\n{response.json()}")
            # print("{}\n{}".format(response.status_code, response.json()))
        return response

    # class test_api_manipulation:
    #  def __init__(self, url):
    #     self.url = url

    def add_book(self, data):
        # date_add = datetime.date.today().strftime("%Y-%m-%d")
        # dt_add_book = {"type": "Science", "title": "#{}-Discoveries in the field of physics".format(time.time()),
        #            "creation_date": date_add}
        """
        uses requests.post method to call BooksService API to post manipulation about add book
        data: string - id add of book
        return
        response: object - object returned by requests.post, including api json response & satus code
        """
        try:
            response = requests.post("{}/manipulation".format(self.url), json=data)

        except Exception:
            print(f"{response.status_code}\n{response.json()}")
            # print("{}\n{}".format(response.status_code, response.json()))
        return response

    def rename_book(self, data):

        """
        uses requests.post method to call BooksService API to post manipulation rename book
        data: string - id rename of book
        return
        response: object - object returned by requests.post, including api json response & satus code
        """
        book_id = data['id']
        new_book_data = data['changes']
        try:
            response = requests.put("{}/manipulation?id={}".format(self.url, book_id), json=new_book_data)

        except Exception:
            print(f"{response.status_code}\n{response.json()}")
            # print("{}\n{}".format(response.status_code, response.json()))
        return response

    def check_connection(self):
        response = None
        try:
            response = requests.get("{}/latest?limit=1".format(self.url)).json()

        except Exception as error:
            print(f"ERROR:\n{error}")

        return response
