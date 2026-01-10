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

    # Здесь будет перессылка сообщений в чат модеров
    print(message.chat.id)
    await message.bot.send_message(8097357981, message.text)
    await message.answer("[Сообщение отправлено модериции. Вам скоро придет ответ ТЕКСТ КОТОРЫЙ НУЖНО ЗАПОЛНИТЬ 2]",reply_markup=core_keyboards.main_inline_keyboard)
    await state.clear()