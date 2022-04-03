import requests


def getinformationaboutbook(limit = 1):
    response = requests.get("http://127.0.0.1:5000/v1/books/latest?limit={}".format(limit))
    # print("{}\n{}".format(response.status_code, response.json()))
    # if response.status_code == 200:
    #     print("Я кодер")
    # else:
    #     print("Я Г-кодер")
    return response.json()
