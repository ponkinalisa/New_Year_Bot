from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import ContentType, FSInputFile

import os
import dotenv

import random

from background import keep_alive #импорт функции для поддержки работоспособности

from body_bot.media.stickers import stickers

from body_bot.bot.init import *


dotenv.load_dotenv()


# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    photo = FSInputFile("body_bot/media/img/Satoru Gojo.jpg")
    await message.answer_photo(
        photo=photo,
        caption='Здравствуй!\nЯ могу создать для тебя предсказание на предстоящий год!'
                '\nЧтобы получить предсказание, нажми на кнопку "Получить предсказание"',
        reply_markup=keyboard
    )


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(filter_help)
async def process_help_command(message: Message):
    photo = FSInputFile("body_bot/media/img/чиби годжо с мандарином.jpg")
    await message.answer_photo(
        photo=photo,
        caption='Что-то случилось? А может что-то сломалось? Есть вопросы по работе бота или прочее?\n\nНапишите '
                'Годжо - @Oladuschek_1, он всё уладит! (наверное)\n\nМожет понадобиться некоторое время для ответа, '
                'имейте терпение ;)'
    )

# Этот хэндлер будет срабатывать на команду "/get"
@dp.message(filter_get)
async def process_get_command(message: Message):
    photo = FSInputFile("body_bot/media/img/пряник.jpg")
    await message.answer_photo(
        photo=photo,
        caption='Генерируем предсказание...'
    )
    photo = FSInputFile("body_bot/media/img/разломленный пряник.png")
    await message.answer_photo(
        photo=photo,
        caption='Готово!'
    )
    pred = random.choice(open('body_bot/media/предсказания.txt', 'r', encoding='utf-8').readlines())
    await message.answer(f"Ваше предсказание на 2026-й год: \n\n{pred}")
    await send_sticker(message)


# Этот хэндлер будет срабатывать на отправку боту фото

async def send_photo_echo(message: Message):
    print(message)
    await message.reply_photo(message.photo[0].file_id)


# Этот хэндлер будет срабатывать на отправку боту стикера
async def send_sticker(message: Message):
    await bot.send_sticker(message.from_user.id, sticker=random.choice(stickers))


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dp.message(F.text)
async def send_echo(message: Message):
    await message.reply(text=message.text)

# Регистрируем хэндлеры
dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(process_get_command, Command(commands='get'))

if __name__ == '__main__':
    keep_alive()
    dp.run_polling(bot)

'''
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
BOT_TOKEN = '7408074908:AAF95M3QeNDSnI5_pTeJoEVypvPVzJj1W2s'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)

'''

