import requests
import json

class Config(object):
    add_url = "http://127.0.0.1:8000/api/add_book"
    delete_url = "http://127.0.0.1:8000/api/delete_book"
    data = {
        'money':'1000',
        'address':'潜山孙榜王塘',
        'relation':'弟兄',
        'phone':'17551017364',
        'book_name':'王文斌',
    }
    delete_data = {
        'book_name':'王小明'
    }

def post_test():
    result = requests.get(url=Config.add_url,data=json.dumps(Config.data))
    print(result.content)

def delete_test():
    result = requests.get(url=Config.delete_url,data=json.dumps(Config.delete_data))
    print(result.text)

if __name__ == '__main__':
    delete_test()