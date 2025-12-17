import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Загрузка переменных окружения
load_dotenv()

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Команды бота
async def start(update: Update, context: CallbackContext):
    """Обработчик команды /start"""
    user = update.effective_user
    await update.message.reply_text(
        f"Привет, {user.first_name}! 👋\n"
        "Я твой учебный помощник!\n\n"
        "Доступные команды:\n"
        "/start - Начать работу\n"
        "/schedule - Расписание пар\n"
        "/homework - Домашние задания\n"
        "/goals - Мои цели\n"
        "/stats - Статистика\n"
        "/help - Помощь"
    )

async def schedule(update: Update, context: CallbackContext):
    """Показать расписание"""
    await update.message.reply_text(
        "📅 *Расписание на неделю:*\n\n"
        "Понедельник:\n"
        "• 9:00 - Математика\n"
        "• 11:00 - Физика\n\n"
        "Вторник:\n"
        "• 10:00 - Программирование\n"
        "• 13:00 - Алгоритмы\n\n"
        "Используйте /add_schedule чтобы добавить пару",
        parse_mode='Markdown'
    )

async def homework(update: Update, context: CallbackContext):
    """Домашние задания"""
    await update.message.reply_text(
        "📝 *Текущие задания:*\n\n"
        "1. Математика - до завтра\n"
        "2. Программирование - до пятницы\n"
        "3. Физика - на следующей неделе\n\n"
        "Используйте /add_homework чтобы добавить задание",
        parse_mode='Markdown'
    )

async def goals(update: Update, context: CallbackContext):
    """Цели и прогресс"""
    await update.message.reply_text(
        "🎯 *Мои цели:*\n\n"
        "• Сдать сессию - 75%\n"
        "• Выучить Python - 60%\n"
        "• Проект GitHub - 40%\n\n"
        "Используйте /add_goal чтобы добавить цель",
        parse_mode='Markdown'
    )

async def stats(update: Update, context: CallbackContext):
    """Статистика"""
    await update.message.reply_text(
        "📊 *Ваша статистика:*\n\n"
        "• Активных дней: 15\n"
        "• Выполнено заданий: 42\n"
        "• Прогресс по целям: 58%\n"
        "• Текущая серия: 5 дней\n\n"
        "*Молодец! Продолжай в том же духе!* 💪",
        parse_mode='Markdown'
    )

async def help_command(update: Update, context: CallbackContext):
    """Помощь"""
    await update.message.reply_text(
        "❓ *Помощь по командам:*\n\n"
        "/start - Начать диалог\n"
        "/schedule - Расписание пар\n"
        "/homework - Домашние задания\n"
        "/goals - Цели и прогресс\n"
        "/stats - Статистика обучения\n"
        "/help - Эта справка\n\n"
        "📌 Бот автоматически присылает уведомления утром и вечером!",
        parse_mode='Markdown'
    )

async def echo(update: Update, context: CallbackContext):
    """Эхо-ответ на текстовые сообщения"""
    await update.message.reply_text(f"Вы сказали: {update.message.text}")

def main():
    """Запуск бота"""
    # Получаем токен из переменных окружения
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not token:
        logger.error("TELEGRAM_BOT_TOKEN не найден в .env файле!")
        return
    
    # Создаем приложение
    app = Application.builder().token(token).build()
    
    # Регистрируем обработчики команд
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("schedule", schedule))
    app.add_handler(CommandHandler("homework", homework))
    app.add_handler(CommandHandler("goals", goals))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("help", help_command))
    
    # Обработчик текстовых сообщений
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    # Запускаем бота
    logger.info("Бот запущен...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
