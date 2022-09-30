"""
Created on Thu Sep 29 19:51:57 2022

@author: MrZafarov

"""

from transliterate import to_latin, to_cyrillic
import telebot

TOKEN = '5625979981:AAFDzGPAuNKSTAl9n9aattLxxN16woZ7qec'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = f"👋Assalomu alaykum {message.from_user.first_name}\n"
    javob += "\n♻️Bot krill alifbosidagi so'z va matnlarni lotin alifbosiga va aksincha lotin alifbosidagi so'z va matnlarni krill alifbosiga o'tkazib beradi✅\n"
    javob += "\n⚡️Botdan foydalanish uchun istalgan so'z yoki matn kiriting✍️\n"
    javob += "\n📜Botdan to'g'ri foydalanish bo'yicha qo'llanma: /help\n"
    javob += "\n🧑🏻‍💻Dasturchi: @MoviyDev"
    bot.reply_to(message, javob)
    
@bot.message_handler(commands=['help'])
def send_suppose(message):
    javob = "❗️Botdan to'g'ri foydalanish uchun quyidagi qoidalarga amal qiling:\n"
    javob += "\n❌Noto'g'ri: Oʻzbekiston\n"
    javob += "✅To'g'ri: O'zbekiston\n"
    javob += "\n❌Noto'g'ri: 🇺🇿O'zbekiston\n"
    javob += "✅To'g'ri: O'zbekiston\n"
    bot.reply_to(message, javob)
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))

bot.infinity_polling()

