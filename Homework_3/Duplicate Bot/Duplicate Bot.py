import telebot

bot = telebot.TeleBot("") #API

@bot.message_handler(content_types=['text'])
def repeat_message(message):
    text = message.text
    repeated_text = text  *  10
    bot.send_message(message.chat.id, repeated_text)

bot.polling()
