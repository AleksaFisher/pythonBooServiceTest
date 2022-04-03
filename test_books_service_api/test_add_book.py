import datetime
import time
import json
import requests


def addbook():

    date_add = datetime.date.today().strftime("%Y-%m-%d")
    dt_add_book = {"type": "Science", "title": "#{}-Discoveries in the field of physics".format(time.time()),
                   "creation_date":date_add}
    response = requests.post("http://127.0.0.1:5000/v1/books/manipulation",json=dt_add_book)
    # print("{}\n{}".format(response.status_code, response.json()))
    getid = response.json()['id']
    # print("{}".format(getid))
    return(getid)


def addbookemptyname():
    date_add = datetime.date.today().strftime("%Y-%m-%d")
    dt_add_book = {"type": "", "title": "", "creation_date": ""}
    getid=None
    try:
        response = requests.post("http://127.0.0.1:5000/v1/books/manipulation", json=dt_add_book)
        print("{}\n{}".format(response.status_code, response.json()))
        getid = response.json()['id']
        print("{}".format(getid))
    except:
        print("{}\n{}".format(response.status_code, response.json()))
    return (getid)

def addbookcharactersname():
    date_add = datetime.date.today().strftime("%Y-%m-%d")
    dt_add_book = {"type": "\.,", "title": "\.,", "creation_date": "\.,"}
    getid=None
    try:
        response = requests.post("http://127.0.0.1:5000/v1/books/manipulation", json=dt_add_book)
        print("{}\n{}".format(response.status_code, response.json()))
        getid = response.json()['id']
        print("{}".format(getid))
    except:
        print("{}\n{}".format(response.status_code, response.json()))
    return (getid)

#
#
# if __name__ == '__main__':
#     print('PyCharm')
#     bookid=addbook()
#     # delete_book(bookid)
#     #print("{}".format(bookid))
#
#     # bookid = addbookcharactersname()
