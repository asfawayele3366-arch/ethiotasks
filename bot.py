import os
import telebot
from flask import Flask, request

server = Flask(__name__)
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = "👋 Welcome to EthioTask Platform Bot!\n\nWebsite: https://onrender.com"
    bot.reply_to(message, welcome_text)

@bot.message_handler(content_types=['text'])
def handle_ads(message):
    bot.reply_to(message, "📩 Ad request received. It will be live after admin approval!")

@server.route('/' + BOT_TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://onrender.com/' + BOT_TOKEN)
    return "EthioTask Bot is Active!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
