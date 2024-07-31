import telebot

# Вставьте свой токен
bot = telebot.TeleBot("7295010578:AAFUpzLQ0bnzFM3CabrJAICmEcEsQ4I8QiQ")

@bot.message_handler(content_types=['text'])
def handle_message(message):
    """
    Обрабатывает текстовое сообщение от пользователя.
    Создает опрос из сообщения, если количество строк соответствует требованиям.
    """
    # Получаем количество переводов строк в сообщении
    lines_count = message.text.count("\n")
    
    # Проверяем, подходит ли количество строк для создания опроса
    if lines_count < 2 or lines_count > 10:
        bot.reply_to(message, "Неверное количество строк! Должно быть от 3 до 11 строк.")
        return

    # Разделяем сообщение на список строк
    lst = message.text.split('\n')

    # Создаем вопрос и варианты ответов
    question = lst[0]
    options = lst[1:]

    # Создаем опрос с помощью метода send_poll
    bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=options,
        is_anonymous=False  # Устанавливаем, чтобы голоса не были анонимными
    )

bot.polling()
