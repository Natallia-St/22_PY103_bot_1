from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton


# Добавляем разметку  кнопок для клавиатуры
start = types.ReplyKeyboardMarkup(resize_keyboard=True)
# Создаем кнопки для клавиатуры
info = types.KeyboardButton('Информация о проекте🌏')
stats = types.KeyboardButton('Хочешь узнать больше?')
# Добавляем кнопки в клавиатуру
start.add(stats, info)


# Создаем клавиатуру типа инлайн и добавляем разметку  кнопок для инлайн - клавиатуры
offer_add_info = InlineKeyboardMarkup(row_width=1)
# Создаем кнопки-ссфлки  для инлайн клавиатуры
url_button1= InlineKeyboardButton(text = "Информация о Python", url="https://surik00.gitbooks.io/aiogram-lessons/content/chapter5.html")
url_button2= InlineKeyboardButton(text = "Список полезной литературы", url="https://surik00.gitbooks.io/aiogram-lessons/content/chapter5.html")
# Создаем кнопку с колбэком для инлайн- клавиатуры
simpl_button= InlineKeyboardButton(text="Спасибо, пока не интересно", callback_data="www")
# Добавляем кнопки в инлайн -клавиатуру
offer_add_info.add(url_button1, url_button2, simpl_button)

