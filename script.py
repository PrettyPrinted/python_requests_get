import requests

res = requests.get('https://scotch.io/')

print(res)

if res:
    print('Response OK')
else:
    print('Response Failed')

print(res.status_code)

print(res.headers)
print(res.text)

API_KEY = 'YOUR API KEY'

url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

params = dict(key=API_KEY, text='Goodbye', lang='en-es')

res = requests.get(url, params=params)

json = res.json()
print(json['text'][0])

print(res.status_code)