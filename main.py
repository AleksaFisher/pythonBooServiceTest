from test_books_service_api_class import *
import test_books_service_api

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # added_bookid = test_books_service_api.addbook()
    # getinfo = test_books_service_api.getinformationaboutbook(1)
    # print("{}".format(getinfo))


    conObj = TestApiGet("http://127.0.0.1:5000/v1/books")
    getinfo = conObj.GetLatestBookInfo(1)
    print("{}".format(getinfo))

