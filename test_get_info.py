import requests


def getinfobook():
    dict_params = "Science"
    response = requests.get("http://127.0.0.1:5000/v1/books/ids?book_type={}".format(dict_params))
    print("{}\n{}".format(response.status_code, response.json()))
    if response.status_code == 200:
        print("Resp {}".format(response.url))
        for resp in response.json():
            print("{}".format(resp['title']))
        #print("Я кодер")
    else:
        #print("Я Г-кодер")
        print(response.status_code)

def getinfobookwithid():

    params = "55297037-e455-4be5-b131-55d4b25df6e0"
    response = requests.get("http://127.0.0.1:5000/v1/books/info?id={}".format(params))
    print("{}\n{}".format(response.status_code, response.json()))
    if response.status_code == 200:
        print("Resp {}".format(response.url))
        print("{}".format(response.json()['type']))
        #print("Я кодер")
    else:
        #print("Я Г-кодер")
        print(response.status_code)

if __name__ == '__main__':
        print('PyCharm')
        getinfobookwithid()