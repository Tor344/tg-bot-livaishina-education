from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from sqlalchemy.ext.asyncio import AsyncSession

from bot.database.repository import UserRepository

import bot.apps.start.keyboards  as start_keyboards
import bot.core.keyboards  as core_keyboards
router = Router()


@router.message(Command("start"))
async def start(message: Message, session: AsyncSession):
    repo = UserRepository(session)

    user = await repo.get_by_telegram_id(message.from_user.id)
    if not user:
        await repo.create(message.from_user.id)

    await message.answer("Привет, это бот-помощник по курсу, выбирай категорию 👇",reply_markup= core_keyboards.start_inline_keyboard)

@router.callback_query(F.data == "main")
async def start(call: CallbackQuery):
    await call.answer("")
    await call.message.delete()

    await call.message.answer("Привет, это бот-помощник по курсу, выбирай категорию 👇",reply_markup= core_keyboards.start_inline_keyboard)


@router.message(Command("chat_id"))
async def print_chat_id(message: Message):
    await message.answer(f"id чата: {message.chat.id}")