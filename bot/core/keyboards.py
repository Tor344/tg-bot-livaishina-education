from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

admin_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="admin",callback_data='admin_inline_keyboard')]])

start_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[

    [InlineKeyboardButton(text="Дедлайны",callback_data='deadlines')],
    [InlineKeyboardButton(text="Расписание",callback_data='schedule')],
    [InlineKeyboardButton(text="Задать вопрос / Отправить домашку",callback_data='question')],])

main_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="На главную",callback_data='main')]],)

admin_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,keyboard=[[KeyboardButton(text="admin",callback_data='admin_keyboard')]])