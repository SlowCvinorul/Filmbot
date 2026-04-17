import os
import telebot
from django.core.management.base import BaseCommand
from django.conf import settings
from films.models import Film

# Создаем бота
bot = telebot.TeleBot(settings.BOT_TOKEN)
class Command(BaseCommand):
    help = 'Запуск Telegram бота для поиска фильмов'
    
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('🤖 Бот запущен...'))
        bot.infinity_polling()

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = """
    🎬 Добро пожаловать в FilmBot! 🎭

    Я помогу вам найти информацию о фильмах.

    📋 Доступные команды:
    /start - Начать работу
    /help - Помощь
    /search - Поиск фильмов

    🔍 Просто напишите название фильма, актера или режиссера!
    """
    bot.reply_to(message, welcome_text)

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """
    🆘 Помощь по использованию бота:

    🔍 Поиск фильмов:
    • Напишите название фильма
    • Имя актера
    • Фамилию режиссера
    • Жанр фильма

    Примеры запросов:
    • "Криминальное чтиво"
    • "Тарантино"
    • "Том Хэнкс"
    • "комедия"
    """
    bot.reply_to(message, help_text)

# Обработчик команды /search
@bot.message_handler(commands=['search'])
def send_search_help(message):
    search_help = """
    🔍 Поиск фильмов

    Напишите что искать:
    • Название фильма
    • Имя актера
    • Режиссера
    • Жанр

    Пример: "Назад в будущее"
    """
    bot.reply_to(message, search_help)

# Обработчик текстовых сообщений (поиск)
@bot.message_handler(func=lambda message: True)
def search_films(message):
    search_text = message.text.strip()
    
    # Ищем фильмы в базе данных
    films = Film.objects.filter(
        title__icontains=search_text
    ) | Film.objects.filter(
        director__icontains=search_text
    ) | Film.objects.filter(
        actors__icontains=search_text
    ) | Film.objects.filter(
        genre__icontains=search_text
    )
    
    if films:
        response = f"🎭 Найдено {films.count()} фильмов:\n\n"
        
        for film in films[:5]:  # Ограничиваем вывод
            response += f"🎬 {film.title} ({film.year})\n"
            response += f"📽 Режиссер: {film.director}\n"
            response += f"⭐ Актеры: {film.actors}\n"
            response += f"🎭 Жанр: {film.genre}\n"
            if film.description:
                response += f"📖 {film.description[:100]}...\n"
            response += "\n"
        
        if films.count() > 5:
            response += f"🔍 Показано 5 из {films.count()} фильмов. Уточните запрос."
    else:
        response = "😔 Фильмы не найдены. Попробуйте другой запрос."
    
    bot.reply_to(message, response)