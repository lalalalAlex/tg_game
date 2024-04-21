from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


def main():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = KeyboardButton(text='Играть')
    btn2 = KeyboardButton(text='Создатели')
    btn.add(btn1, btn2)
    return btn


def main2():
    btn = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton(text='Играть', callback_data='play')
    btn2 = InlineKeyboardButton(text='Создатели', callback_data='creators')
    btn.add(btn1, btn2)
    return btn


def characters():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = KeyboardButton(text='Слава')
    btn2 = KeyboardButton(text='Анжела')
    btn.add(btn1, btn2)
    return btn


def creators():
    btn = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton(text='Альберт', url='https://t.me/xD_DxD_Dx')
    btn2 = InlineKeyboardButton(text='Александр', url='https://t.me/Shawnn_ref')
    back = InlineKeyboardButton(text='Назад', callback_data='back')
    btn.add(btn1, btn2)
    btn.add(back)
    return btn


def variants():
    btn = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton(text='Первый вариант', callback_data='first')
    btn2 = InlineKeyboardButton(text='Второй вариант', callback_data='second')
    btn.add(btn1, btn2)
    return btn
