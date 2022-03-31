import requests

def test_change_name_book(bookid):
    dt_change_book = {"id":bookid,"type": "Drama"}
    getid = None
    try:
        response = requests.put("http://127.0.0.1:5000/v1/books/manipulation?id={}".format(bookid), json=dt_change_book)
        print("{}\n{}".format(response.status_code, response.json()))
        getid = response.json()['id']
        print("{}".format(getid))
    except:
        print("{}\n{}".format(response.status_code, response.json()))
    return(getid)

if __name__ == '__main__':
        print('PyCharm')
        test_change_name_book("bf7da2c6-40e3-47ec-bb20-c81077f123ef")