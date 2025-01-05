import telebot
from googletrans import Translator

API_TOKEN = '7124792293:AAEifqC5smbCVNzbPWocfSJ2AYHGsLJqb_o'

bot = telebot.TeleBot(API_TOKEN)
translator = Translator()

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'به ربات خوش آمدید! متن و کد زبان مقصد را وارد کنید.')

@bot.message_handler(func=lambda message: True)
def translate_message(message):
    try:
        if ' ' not in message.text:
            return
        
        user_input = message.text.rsplit(' ', 1)
        text_to_translate = user_input[0]
        dest_lang = user_input[1]

        if len(dest_lang) != 2:
            return

        translated_text = translator.translate(text_to_translate, src='fa', dest=dest_lang)
        bot.send_message(message.chat.id, translated_text.text)

    except Exception:
        pass

bot.infinity_polling()