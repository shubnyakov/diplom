from telebot.types import Message

from loader import bot


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    bot.send_message(message.chat.id, f"Привет, {message.from_user.full_name}!\nОткройте меню и выберите команду")
