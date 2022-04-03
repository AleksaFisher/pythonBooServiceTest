from test_books_service_api import TestApi


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    conObj = TestApi("http://127.0.0.1:5000/v1/books")
    getinfo = conObj.checkconnection()

    # added_bookid = test_books_service_api.addbook()
    # getinfo = test_books_service_api.getinformationaboutbook(10)

    print("{}".format(getinfo))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
