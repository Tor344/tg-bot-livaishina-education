from aiogram import Router,F
from aiogram.types import Message,CallbackQuery
from aiogram.filters import Command

import bot.core.keyboards as core_keyboards
router = Router()

@router.callback_query(F.data == "deadlines")
async def schedule(call: CallbackQuery):
    await call.message.delete()
    await call.answer()
    await call.message.answer("[ТЕКСТ КОТОРЫЙ НУЖНО ЗАПОЛНИТЬ 7]",reply_markup=core_keyboards.main_inline_keyboard)


