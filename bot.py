# bot.py

import telebot
from tarjimon import lotin_to_kirill, kirill_to_lotin

TOKEN = '7854063099:AAHJ49P5QICWdpsbSxA_v9HBiKfHNJZt0Qo'  # o'z tokeningizni yozing
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu alaykum! Matn kiriting — bot uni avtomatik tarjima qiladi (lotin ↔ kiril).")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text
    if any(harf in text.lower() for harf in ['қ', 'ў', 'ғ', 'ҳ', 'ё', 'ш', 'ч', 'ж']):
        natija = kirill_to_lotin(text)
        bot.send_message(message.chat.id, f"Lotincha:\n{natija}")
    else:
        natija = lotin_to_kirill(text)
        bot.send_message(message.chat.id, f"Kirilcha:\n{natija}")

bot.polling()
