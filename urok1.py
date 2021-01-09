import requests
import aiogram

API_KEY = '1543692297:AAHRVsPV6qb3xD_GEyMKCdKKsMSwK7Rpuak'
api_link = 'https://api.telegram.org/bot' + API_KEY
updates = requests.get(api_link + '/getUpdates?offset=-1').json() # превращаем запрос в словарь
print(updates)

message = updates['result'][0]['message']
chat_id = message['from']['id'] #вытягиваем id пользователя
name = message['from']['first_name'] #вытягиваем имя пользователя
send_message = requests.get(api_link + f'/sendMessage?chat_id={chat_id}&text=Привет, {name}')
#используя запрос передаем параметры в get запросе(id пользователя, тест + используем переменную из словаря)