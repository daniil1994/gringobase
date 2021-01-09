import telebot

bot= telebot.TeleBot('1543692297:AAHRVsPV6qb3xD_GEyMKCdKKsMSwK7Rpuak')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Введите имя: ")

if __name__ == '__main__':
    bot.polling(none_stop = True)