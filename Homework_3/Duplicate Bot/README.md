```python
import telebot

bot = telebot.TeleBot(" ") #Токен

@bot.message_handler(content_types=['text'])
def repeat_message(message):
    repeated_text = text  *  10
    bot.send_message(message.chat.id, repeated_text)

bot.polling()
```

Зашел на  `@BotFather`

![](https://yandex.ru/images/search?pos=0&img_url=https%3A%2F%2Fcore.telegram.org%2Ffile%2F811140327%2F1%2FzlN4goPTupk%2F9ff2f2f01c4bd1b013&text=%40BotFather&rpt=simage)
Нажал на кнопку `start`

Вписал `/newbot` для создания нового бота.

Дал название боту `Duplicate Bot`

Вписал имя пользователя для бота `Duplicate Bot`

Получил API:
```txt
7295010578:AAFUpzLQ0bnzFM3CabrJAICmEcEsQ4I8QiQ
```
И получил ссылку на бота https://t.me/Duplicate_10_Bot

После запуска кода бот заработал и продублировал 10 раз мой текст.

![[./фото/Снимок экрана от 2024-07-31 20-46-19.png]]
