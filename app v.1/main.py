import asyncio as asy

from aiogram import Bot, Dispatcher, executor
from config import API_KEY

loop = asy.get_event_loop() #Не онял что это такое
bot = Bot(API_KEY, parse_mode = 'HTML') #переменная с токеном и форматированием по правилам аштиэмель
dp = Dispatcher(bot, loop=loop)

if __name__ == '__main__':
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup = send_to_admin)