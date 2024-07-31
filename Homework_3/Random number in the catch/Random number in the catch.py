# импортируем библиотеку telebot
import telebot
import random

# вставляем токен 
bot = telebot.TeleBot("7295010578:AAFUpzLQ0bnzFM3CabrJAICmEcEsQ4I8QiQ") # Вставить свой API

# хэндлер для сообщений с "рандом"
@bot.message_handler(func=lambda message: 'рандом' in message.text.lower())
def handle_random(message):
    """Обрабатывает сообщение, содержащее слово 'рандом'."""
    # генерируем случайное число от 0 до 100
    random_number = random.randint(0, 100)
    # отправляем случайное число пользователю
    bot.reply_to(message, f"Случайное число: {random_number}")

# хэндлер для всех остальных сообщений
@bot.message_handler(func=lambda message: True)
def handle_other(message):
    """Обрабатывает все остальные сообщения."""
    # дублируем сообщение пользователя
    bot.reply_to(message, message.text)

# запускаем бота
bot.polling()
