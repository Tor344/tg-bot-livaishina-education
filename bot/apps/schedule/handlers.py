from aiogram import Router,F
from aiogram.types import Message,CallbackQuery,InputMediaPhoto,FSInputFile
from aiogram.filters import Command

import bot.core.keyboards as core_keyboards
import bot.apps.schedule.keyboards as schedule_keyboards
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

    sent_messages = await call.message.bot.send_media_group(chat_id=call.message.chat.id, media=media)

    # Сохраняем ID только первого сообщения медиа-группы
    media_ids_str = ",".join(str(msg.message_id) for msg in sent_messages)


    await call.message.answer("Ваше расписание", reply_markup=schedule_keyboards.main_from_mediagroup(media_ids_str))

