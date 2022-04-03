import requests

def getlatestlimit():
    limit = "2"
    response = requests.get("http://127.0.0.1:5000/v1/books/latest?limit={}".format(limit))
    print("{}\n{}".format(response.status_code, response.json()))
    if response.status_code == 200:
        print("Resp {}".format(response.url))
        for resp in response.json():
            print("{}".format(resp['title']))
        # print("Я кодер")
    else:
        # print("Я Г-кодер")
        print(response.status_code)

if __name__ == '__main__':
        print('PyCharm')
        getlatestlimit()