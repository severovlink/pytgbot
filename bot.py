import telebot
from telebot import apihelper
import config

bot = telebot.TeleBot(config.TG_BOT_TOKEN)
PROXY = config.TG_PROXY

apihelper.proxy = {'https': PROXY}


@bot.message_handler(commands=['start'])    # decorate for define request message after start
def start_message(message):
    bot.send_message(message.chat.id, 'Hello, my little bean!')     # message from start


@bot.message_handler(content_types=['text'])    # decorate for define type of message content
def repeat_messages(message):   # method that repeat all users message from the chat whit the bot
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop='True', timeout=123)   # launches long polling
