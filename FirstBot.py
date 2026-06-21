import telebot
import random
from datetime import datetime

TOKEN = '8621180554:AAEBXtxiIISB5T4cUjMQ81cQNaMqwDW6e4Y'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    text = """
Привет! 👋 Я многофункциональный бот!

Команды:
/time - текущее время
/coin - флип монеты(орёл/решка)
/random - случайное число (от 1 до 10)
/help - помощь (это меню)
/secret - поделюсь секретом)

Или просто напиши выражение (2+2, 10*5)
"""
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['coin'])
def coinflip(message):
    flip_result = "Орёл" if random.random() > 0.5 else 'Решка'
    bot.send_message(message.chat.id, flip_result)

@bot.message_handler(commands=['time'])
def current_time(message):
    cur_time = datetime.now().strftime('%H:%M')
    bot.send_message(message.chat.id, f"Сейчас: {cur_time}⌚")

@bot.message_handler(commands=['random'])
def random_number(message):
    random_num = random.randint(1, 10)
    bot.send_message(message.chat.id, f"Случайное число: {random_num}")

@bot.message_handler(commands=['secret'])
def send_secret(message):
    secret = "Не скажу" if random.random() > 0.5 else "Твоя матуха шлюха"
    bot.send_message(message.chat.id, secret)

@bot.message_handler(func=lambda message: True)
def send_result(message):
    try:
        result = eval(message.text)
        bot.send_message(message.chat.id, f"Результат: {result}")
    except:
        errors = ['Ошибка', 'Не выражение', 'Не верное выражение']
        bot.send_message(message.chat.id, random.choice(errors))




bot.infinity_polling()