from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from sqlalchemy.ext.asyncio import AsyncSession

from bot.database.repository import UserRepository

from bot.apps.start.keyboards import *
router = Router()


@router.message(Command("start"))
async def start(message: Message, session: AsyncSession):
    repo = UserRepository(session)

    user = await repo.get_by_telegram_id(message.from_user.id)
    if not user:
        await repo.create(message.from_user.id)

    await message.answer("[ТЕКСТ КОТОРЫЙ НУЖНО ЗАПОЛНИТЬ 1]",reply_markup= start_inline_keyboard)
