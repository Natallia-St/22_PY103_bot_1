import logging
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State

# Подключение модуля с токеном
import config
# Подключение модуля с кнопками
import keyboard
# Подключение модуля с эмоджи
import emoji

# Создание хранилища состояний
storage = MemoryStorage()
# Инициализация бота и установка режима парсинга для сообщений бота (для оформления текста выбирается аргументом  parse_mode)
bot = Bot(config.TOKEN, parse_mode=types.ParseMode.HTML)
# Инициализация диспетчера (Dispatcher - принимает все и обрабатывает),  указываем ему на хранилище состояний
dp = Dispatcher(bot, storage=storage)
# Подключаем логирование
logging.basicConfig(
    # Указываем название с логами
    filename='log.txt',
    # Указываем уровень логирования
    level=logging.INFO,
    # Указываем формат сохранения логов
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s '
           u'[%(asctime)s] %(message)s')


# Задаем обработчик для нашей команды start
@dp.message_handler(commands='start', state=None)
async def welcome(message: types.Message):
    # Jткрываем файл user.txt в режиме чтения
    joined_file = open('user.txt', 'r')
    # Cоздаем множество для хранения имен всех пользователей из txt
    joined_users = set()
    # Gроходим циклом по каждому пользователю в user.txt
    for line in joined_file:
        # Добавляем user_id в наше множество пользователей
        joined_users.add(line.strip())
    # Eсли пользователь, который нажал /start, не находится во множестве пользователей
    if not str(message.chat.id) in joined_users:
        # Открываем файл user.txt на дозапись
        joined_file = open('user.txt', 'a')
        # Записываем в него id нашего пользователя
        joined_file.write(str(message.chat.id) + '\n')
        # Добавляем его во множество пользователей
        joined_users.add(message.chat.id)
        # Говорим боту отправить сообщение, при этом
    await bot.send_message(
        # обращаемся к id пользователя
        message.chat.id,
        # Указываем отправляемое сообщение hello + имя пользователя
        f'✋Hello {message.from_user.first_name}',
        # Подключаем кнопки из файла keyboard, обратившись к переменной start
        reply_markup=keyboard.start)


# Задаем обработчик для кнопок клавиатуры, указываем тип контента как text
@dp.message_handler(content_types=['text'])
# Задаем асинхронную функцию-обработчик
async def info_static(message: types.Message):
    # Если переданное боту сообщение = 'Информация о проекте🌏'
    if message.text == 'Информация о проекте🌏':
        # Бот отправляет сообщение пользователю, отправившего его
        await bot.send_message(message.chat.id,
                               # с текстом
                               text='Бот \nсоздан в образовательных целях 🚀 ?',
                               # режим форматирования
                               parse_mode='Markdown')
    # Если переданное боту сообщение = 'Хочешь узнать больше?'
    elif message.text == 'Хочешь узнать больше?':
        # Бот отправляет сообщение пользователю, отправившего его
        await message.answer('Поделюсь полезной информацией' + emoji.emojize(":brain:"),
                             reply_markup=keyboard.offer_add_info)
    # Если переданное боту сообщение = 'Обучение'
    elif message.text == 'Обучение':
        # Бот отправляет сообщение пользователю, отправившего его
        await message.answer('Поделюсь полезной информацией' + emoji.emojize(":brain:"),
                             reply_markup=keyboard.offer_add_info)


# Задаем обработчик для кнопок inline - ожидаем колбэк и принимаем lambda-функцию для фильтра колбэка
@dp.callback_query_handler(lambda c: True)
# Задаем асинхронную функцию-обработчик и отлавливаем нужный нам колбэк
async def callback_inline(call):
    # Если колбэк "www" - отправляем юзеру сообщение
    if call.data == "www":
        # бот отправляет сообщение пользователю, отправившего его
        await bot.send_message(call.message.chat.id,
                               'Понятно 😇 \nEсли захочешь вернуться к обучению - пришли мне в сообщении текст "Обучение" ')


# Запускаем бота
if __name__ == '__main__':
    executor.start_polling(dp)

# Инлайн кнопки - вызов с помощью команды
# @dp.message_handler(commands=['1'])
# async def url_command(message: types.Message):
#     await bot.send_message(
#         message.chat.id,
#         text='Ссылочка',
#         reply_markup=keyboard.stats)
