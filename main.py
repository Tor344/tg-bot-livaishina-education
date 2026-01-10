import asyncio
import sys
import logging

from bot.apps.schedule.handlers import router as schedule_router
from bot.apps.deadlines.handlers import router as deadlines_router
from bot.apps.homework.handlers import router as homework_router
from bot.apps.materials.handlers import router as materials_router
from bot.apps.question.handlers import router as question_router
from aiogram import Bot, Dispatcher

import config.settings as set


from bot.apps.start.handlers import router as start_router
from bot.apps.user.handlers import router as user_router
from bot.apps.admin.handlers import router as admin_router
from bot.database.session import engine, Base
import bot.database.models
from bot.middlewares.db import DbSessionMiddleware

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout  # Рекомендуется для aiogram/Docker
)

logger = logging.getLogger(__name__)

bot = Bot(token=set.API_TOKEN)

dp = Dispatcher()

dp.update.middleware(DbSessionMiddleware())


dp.include_router(user_router)
dp.include_router(admin_router)
dp.include_router(start_router)
dp.include_router(question_router)
dp.include_router(schedule_router)
dp.include_router(deadlines_router)
dp.include_router(homework_router)
dp.include_router(materials_router)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def main():
    try:
        await init_db()
        logger.info("Бот запущен")
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Ошибка при запуске: {e}")


if __name__ == "__main__":
    asyncio.run(main())