from aiogram import Router,F
from aiogram.types import Message,CallbackQuery
from aiogram.filters import Command

import bot.core.keyboards as core_keyboards
router = Router()

@router.callback_query(F.data == "deadlines")
async def schedule(call: CallbackQuery):
    await call.message.delete()
    await call.answer()
    await call.message.answer("""
22 января - дедлайн рекламного ролика
8 февраля - дедлайн по отчетному ролику
23 февраля - дедлайн «говорящей головы»
10 марта - дедлайн тизера
29 марта - дедлайн по корпоративному фильму
17 апреля - дедлайн по комбо""",reply_markup=core_keyboards.main_inline_keyboard)


