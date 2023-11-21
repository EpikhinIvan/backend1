import telebot
from myapp.models import Application

from django.core.management.base import BaseCommand



bot_token = '6950562270:AAEsZfsJdg7P2KNbYDGAHrFz5aLjYYq-h-g' 
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = ("Доступные команды:\n"
                 "/start - Начало работы с ботом\n"
                 "/add - Добавить новую заявку \n"
                 "/applications - Просмотреть все заявки\n"
                 "/help - Показать это сообщение с информацией о командах")
    bot.send_message(message.chat.id, help_text)


@bot.message_handler(commands=['start',])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я бот для создания заявок.")

@bot.message_handler(commands=['applications'])
def applications(message):
    applications = Application.objects.all()  
    for application in applications:
        response = f"Заявка: {application.title}\nОписание: {application.description}"
        bot.send_message(message.chat.id, response)

@bot.message_handler(commands=['add'])
def add_application(message):
    try:
        content = message.text.split(maxsplit=1)[1]  
        title, description = content.split(';') 
        title = title.strip()
        description = description.strip()

        Application.objects.create(
            title=title, 
            description=description
        )
        bot.reply_to(message, "Заявка успешно создана!")
    except (IndexError, ValueError):
        bot.reply_to(message, "Пожалуйста, следуйте формату: /add Заголовок заявки; Описание заявки")


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(message, "Сообщение получено.")





bot.polling()
