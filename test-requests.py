import requests

params = dict(key='trnsl.1.1.20200524T070332Z.e331af92244e01d9.4bbf0e51a86adc223bc3d1594c020c24e146fd39', text='Hello', lang='en-es')
url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
res = requests.get(url, params)
print(res.text)

'''

res = requests.get('https://scotch.io')
if res.status_code == 200:
    print('Response OK')
else:
    print('Response Failed')
print(res.headers)'''
