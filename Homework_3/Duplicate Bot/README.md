```python
import telebot

bot = telebot.TeleBot("") #API

@bot.message_handler(content_types=['text'])
def repeat_message(message):
    repeated_text = text  *  10
    bot.send_message(message.chat.id, repeated_text)

bot.polling()
```

Зашел на  `@BotFather`

![фото](фото/фото_3.png)

Нажал на кнопку `start`

Вписал `/newbot` для создания нового бота.

Дал название боту `Duplicate Bot`

Вписал имя пользователя для бота `Duplicate Bot`

Получил API:

И получил ссылку на бота https://t.me/Duplicate_10_Bot

![фото](фото/фото_2.png)

После запуска кода бот заработал и продублировал 10 раз мой текст.

![фото](фото/фото_1.png)