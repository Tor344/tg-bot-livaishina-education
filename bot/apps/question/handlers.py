import re

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from bot.database.repository import UserRepository
from bot.apps.question.state_fms import Question
import bot.apps.question.keyboards as question_keyboards
import bot.core.keyboards as core_keyboards

router = Router()

#переход пользователя в диалог
@router.callback_query(F.data == "question")
async def question(call: CallbackQuery, state: FSMContext):
    await call.answer("")
    await state.set_state(Question.dialogue)

    await call.message.answer("""Здравствуйте! Здесь вы можете задать вопрос в службу поддержки. Алия и кураторы ответят вам в течение дня как можно скорее.
Чтобы выйти из диалога, нажмите кнопку внизу экрана.""",reply_markup=question_keyboards.dialogue_break)

#Выход из диалога
@router.message(F.text == "Выйти из диалога", StateFilter(Question.dialogue))
async def question(message: Message, state: FSMContext,session: AsyncSession):
    await message.answer("Привет, это бот-помощник по курсу, выбирай категорию 👇",reply_markup= core_keyboards.start_inline_keyboard)

    await state.clear()

#обработка сообщений пользователя 
@router.message(StateFilter(Question.dialogue))
async def question(message: Message, state: FSMContext,session: AsyncSession):
    repo = UserRepository(session)
    id_that_admin = await repo.get_that_id_admin()
    message_text = f"""ID_USER: {message.from_user.id}
NAME_USER: @{message.from_user.username}

Сообщение: {message.text}
    """

    await message.bot.send_message(str(id_that_admin.id_that), message_text)
    

@router.message(F.text)
async def question(message: Message, session:AsyncSession):
    repo = UserRepository(session)
    id_that_admin = await repo.get_that_id_admin()
    if message.chat.id != id_that_admin.id_that:
        await message.answer("Возможно вы хотели ответить аминистратора. Для этого перейдите в 'Задать вопрос / Отправить домашку'")
    if not message.reply_to_message:
        return

    id_user_match = re.search(r'ID_USER:\s*(\d+)', message.reply_to_message.text)
    id_user = int(id_user_match.group(1)) if id_user_match else None
    if id_user is None:
        return
    await message.bot.send_message(id_user, f"Ответ на ваш вопрос:\n {message.text}")
