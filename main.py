
import random
from app.link import *
from telebot import types
from app.keyboard import keyboard as k

# работа с клавиатурой
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за пользование ботом!')
    if call.data == 'education':
        text = first[0]
        bot.send_message(call.message.chat.id, text, reply_markup=k.keyboard)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    elif call.data == 'or':
        text = random.choice(first[1:5])
        bot.send_message(call.message.chat.id, text, reply_markup=k.keyboardor)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    elif call.data == 'linksplus':
        text = linki[0]
        bot.send_message(call.message.chat.id, text, reply_markup=k.keyboardlink)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    elif call.data == 'orl':
        text = random.choice(linki[1:])
        bot.send_message(call.message.chat.id, text, reply_markup=k.keyboardlinkor)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    elif call.data == 'tg':
        text = chats[0]
        bot.send_message(call.message.chat.id, text, reply_markup=k.keyboardtg)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    elif call.data == 'org':
        text = random.choice(chats[1:])
        bot.send_message(call.message.chat.id, text, reply_markup=k.keyboardtgor)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    elif call.data == 'books':
        text = books[0]
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(types.InlineKeyboardButton(text='Еще', callback_data='orb'),
                     types.InlineKeyboardButton("Назад", callback_data='back'))
        bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    elif call.data == 'orb':
        text = random.choice(books[1:])
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(types.InlineKeyboardButton(text='Еще', callback_data='orb'),
                 types.InlineKeyboardButton("Назад", callback_data='back'))
        bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    elif call.data == 'eng':
        text = engl[0]
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(types.InlineKeyboardButton(text='Еще', callback_data='ore'),
                     types.InlineKeyboardButton("Назад", callback_data='back'))
        bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    elif call.data == 'ore':
        text = random.choice(engl[1:])
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(types.InlineKeyboardButton(text='Еще', callback_data='ore'),
                 types.InlineKeyboardButton("Назад", callback_data='back'))
        bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    elif call.data == 'pyth':
        text = pyth[0]
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(types.InlineKeyboardButton(text='Еще', callback_data='orp'),
                     types.InlineKeyboardButton("Назад", callback_data='back'))
        bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    elif call.data == 'orp':
        text = random.choice(engl[1:])
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(types.InlineKeyboardButton(text='Еще', callback_data='pyth'),
                 types.InlineKeyboardButton("Назад", callback_data='back'))
        bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    elif call.data == 'back':
        bot.send_message(call.message.chat.id, "Вы вернулись на главную страницу, выберите раздел снова", reply_markup=None)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)


bot.polling(none_stop=True, interval=0)
