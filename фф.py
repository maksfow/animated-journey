from telebot import types
bc = types.ReplyKeyboardMarkup(resize_keyboard=True)
r = types.KeyboardButton("help")
bc.add(r)