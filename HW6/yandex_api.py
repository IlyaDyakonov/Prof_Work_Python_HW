import requests
from TOKEN import TOKEN

name_papka_unittest = 'папка_для_unittests'
name_papka_pytest = 'папка_для_pytest'

def header(TOKEN):
    headers = {'Content-Type': 'application/json',
            'Authorization': f'OAuth {TOKEN}'
            }
    return headers

def create(name_papka):
    headers = header(TOKEN)
    url = 'https://cloud-api.yandex.net/v1/disk/resources/'
    params = {'path': name_papka}
    response1 = requests.put(url, headers=headers, params = params)
    return response1.status_code

# create(name_papka)