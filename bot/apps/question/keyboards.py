from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

start_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="question",callback_data='question_inline_keyboard')]])



start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,keyboard=[[KeyboardButton(text="question",callback_data='question_keyboard')]])

remove_keyboard = ReplyKeyboardRemove()

dialogue_break = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[KeyboardButton(text="Выйти из диалога")]])