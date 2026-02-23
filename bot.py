import asyncio
from loguru import logger
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from config import config
from database.crud import init_db
from handlers import user, payments, referrals

# Инициализация бота и диспетчера
bot = Bot(token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()

async def main():
    logger.info("Starting bot...")
    
    # Инициализация БД
    await init_db()
    
    # Регистрация хэндлеров
    dp.include_routers(user.router, payments.router, referrals.router)
    
    # Запуск polling
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped!")
