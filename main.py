import telebot
from telebot.types import ReplyKeyboardRemove
from фф import bc
bot = telebot.TeleBot("6498095927:AAH9yb9EtctLIVFpYcUhDH59xaE7rPAwPg8")

@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id,"Добро пожаловать!\n Давайте познокомимся,"
                             "расскажите о себе: ")
    bot.register_next_step_handler(message,help)
def help(message):
    user_id = message.from_user.id
    user_data = message.text
    bot.send_message(user_id, "Для справочной информации нажмите на help", reply_markup=bc)
    bot.register_next_step_handler(message,pp,user_data)
def pp(message,user_data):
    if message.text == "help":
        user_id = message.from_user.id
        bot.send_message(user_id,f' Вы рассказали о себе : {user_data}',reply_markup=ReplyKeyboardRemove())

    else:
        user_id = message.from_user.id
        bot.send_message(user_id, "Извините, произошла ошибка.")
bot.polling(non_stop=True)