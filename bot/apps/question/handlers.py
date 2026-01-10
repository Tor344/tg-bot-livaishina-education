import re

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from bot.database.repository import UserRepository
from bot.apps.question.state_fms import Question
import bot.core.keyboards as core_keyboards

router = Router()


@router.callback_query(F.data == "question")
async def question(call: CallbackQuery, state: FSMContext, session: AsyncSession):
    repo = UserRepository(session)
    await call.answer("")
    await state.set_state(Question.dialogue)

    await call.message.answer("Здравствуйте. Здесь вы можете написать вопрос поддежке, которая вам оперативно ответит")


@router.message(StateFilter(Question.dialogue))
async def question(message: Message, state: FSMContext):
    message_text = f"""ID_USER: {message.from_user.id}
NAME_USER: @{message.from_user.username}

Сообщение: {message.text}
    """

    await message.bot.send_message(-5263441534, message_text)

    await message.answer("[Сообщение отправлено модериции. Вам скоро придет ответ ТЕКСТ КОТОРЫЙ НУЖНО ЗАПОЛНИТЬ 2]",
                         reply_markup=core_keyboards.main_inline_keyboard)
    await state.clear()


@router.message(F.text)
async def question(message: Message):
    if message.chat.id != -5263441534:
        return
    if not message.reply_to_message:
        return

    id_user_match = re.search(r'ID_USER:\s*(\d+)', message.reply_to_message.text)
    id_user = int(id_user_match.group(1)) if id_user_match else None

    await message.bot.send_message(id_user, f"[Ответ модерации ТЕКСТ КОТОРЫЙ НУЖНО ЗАПОЛНИТЬ 2]:\n {message.text}")



