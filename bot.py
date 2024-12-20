from telegram import Bot

# Токен вашого бота
BOT_TOKEN = "7907022002:AAESPATkMmcrOzHVVzhMMlEZKxitN8BD6J4"

# ID користувача для тестування
USER_ID = 389543078  # Замініть на ваш Telegram ID

# Створюємо об'єкт бота
bot = Bot(token=BOT_TOKEN)

# Надсилаємо тестове повідомлення з захистом контенту
bot.send_message(
    chat_id=USER_ID,
    text="Це повідомлення захищене від пересилання!",
    protect_content=True
)
