from aiogram.types import Message


def filter_help(message: Message):
    return message.text and ('/help' in message.text or 'помощь' == message.text.lower() or
                             '❓ Помощь ❓' == message.text)


def filter_rules(message: Message):
    return message.text and (message.text == '/rules' or 'правила' == message.text.lower() or
                             '📋 Правила 📋' == message.text)

def filter_get(message: Message):
    return message.text and ('/get' in message.text or 'получить предсказание' == message.text.lower() or
                             '🎄 Получить предсказание! 🎄' == message.text)