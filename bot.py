from tarjimon import to_cyrillic, to_latin
import telebot

bot = telebot.TeleBot("7854063099:AAHJ49P5QICWdpsbSxA_v9HBiKfHNJZt0Qo", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu alaykum! Matn kiriting — bot uni avtomatik tarjima qiladi (lotin ↔ kiril).")

@bot.message_handler(func=lambda message: True)
def tarjima_qilish(message):
    msj = message.text
    if msj.isascii():
        javob = to_cyrillic(msj)
    else:
        javob =to_latin(msj)
    bot.reply_to(message,javob)
bot.infinity_polling()
