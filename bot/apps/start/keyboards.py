from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

start_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Материалы",callback_data='materials')],
    [InlineKeyboardButton(text="Домашки",callback_data='homework')],
    [InlineKeyboardButton(text="Дедлайны",callback_data='deadlines')],
    [InlineKeyboardButton(text="Расписание",callback_data='schedule')],
    [InlineKeyboardButton(text="Задать вопрос",callback_data='question')],])

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,keyboard=[[KeyboardButton(text="start",callback_data='start_keyboard')]])