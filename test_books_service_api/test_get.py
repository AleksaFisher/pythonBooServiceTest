import requests


def getinformationaboutbook():
    response = requests.get("http://127.0.0.1:5000/v1/books/latest?limit=1")
    # print("{}\n{}".format(response.status_code, response.json()))
    # if response.status_code == 200:
    #     print("Я кодер")
    # else:
    #     print("Я Г-кодер")
    return response.json()
