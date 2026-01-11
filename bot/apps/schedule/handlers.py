from aiogram import Router,F
from aiogram.types import Message,CallbackQuery,InputMediaPhoto,FSInputFile
from aiogram.filters import Command

import bot.core.keyboards as core_keyboards
router = Router()

@router.callback_query(F.data == "schedule")
async def schedule(call: CallbackQuery):
    await call.message.delete()
    await call.answer()
    paths = [
        "media/photo_5413618157500435481_y.jpg",
        "media/photo_5413618157500435482_y.jpg",
        "media/photo_5413618157500435483_y.jpg",
        "media/photo_5413618157500435484_y.jpg",
    ]
    media = [
        InputMediaPhoto(
            media=FSInputFile(path)
        ) for path in paths
    ]

    await call.message.bot.send_media_group(
        chat_id=call.message.chat.id,
        media=media,
     )
    await call.message.answer("На главную",reply_markup=core_keyboards.main_inline_keyboard)
