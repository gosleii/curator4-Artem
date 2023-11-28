import telebot
bot = telebot.TeleBot('6640562245:AAGp7wrB3X4X6LMaD8AaDsySOB4wC7MztMI')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, '*Телеграмм* \n Телеграмм', parse_mode='Markdown')

@bot.message_handler(commands=['jump'])
def main(message):
    bot.send_message(message.chat.id, 'прыгни')

@bot.message_handler(commands=['work'])
def main(message):
    bot.send_message(message.chat.id, 'робот')

@bot.message_handler(commands=['translate'])
def main(message):
    bot.send_message(message.chat.id, 'это [ссылка](https://yandex.ru/search/?text=%D0%BF%D0%B5%D1%80%D0%B5%D0%B2%D0%BE%D0%B4%D1%87%D0%B8%D0%BA&clid=2411726&lr=75)', parse_mode='Markdown')

@bot.message_handler(commands=['translate_google'])
def main(message):
    bot.send_message(message.chat.id, 'это [ссылка](https://translate.google.com.co/?hl=ru)', parse_mode='Markdown')

bot.infinity_polling()