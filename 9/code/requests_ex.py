import requests
r = requests.get('http://yandex.ru')
print r.status_code
print r.text
