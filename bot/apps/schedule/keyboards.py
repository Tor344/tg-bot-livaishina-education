from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

start_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="schedule",callback_data='schedule_inline_keyboard')]])

def main_from_mediagroup(first_media_id):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="На главную", callback_data=f"main_from_mediagroup:{first_media_id}")]
    ])
    return keyboard

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,keyboard=[[KeyboardButton(text="schedule",callback_data='schedule_keyboard')]])
