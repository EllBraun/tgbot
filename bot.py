from telegram import Bot
from telegram.ext import Application, CommandHandler
import asyncio

async def main():
    # Ваша токен API бота
    bot_token = "7907022002:AAESPATkMmcrOzHVVzhMMlEZKxitN8BD6J4"
    application = Application.builder().token(bot_token).build()

    # Додавання обробника команди /start
    application.add_handler(CommandHandler("start", start))

    # Запуск бота
    await application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
