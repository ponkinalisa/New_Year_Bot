from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Создаем объекты кнопок
button_1 = KeyboardButton(text='🎄 Получить предсказание! 🎄')
button_3 = KeyboardButton(text='❓ Помощь ❓')

# Создаем объект клавиатуры, добавляя в него кнопки
keyboard = ReplyKeyboardMarkup(
    keyboard=[[button_1], [button_3]],
    resize_keyboard=True
)