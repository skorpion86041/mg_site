import requests

HEADERS = {
    'Host': 'api.content.market.yandex.ru',
    'Accept': '*/*',
    'Authorization': 'ea2d0a82-8377-45a4-9dd4-20aa3130635c'}
info = requests.get('https://api.content.market.yandex.ru/v2/models/14211947/opinions', headers=HEADERS)
print(info.text)