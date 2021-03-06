import random
import tokens
from app.link import *
from telebot import types
from app.keyboard import keyboard as k
import telebot

bot = telebot.TeleBot(tokens.token_bot)

# Response to start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, 'Привет! Бот покажет тебе полезныe ссылках для начинающего тестировщика!\n' +
                     '/receive - для выбора раздела с ссылками\n /help - Для справки \n /start - Снова прочесть сообщение')


# Response to help
@bot.message_handler(commands=['help'])
def help_command(message):
    keyboard = types.InlineKeyboardMarkup()
    key_help = types.InlineKeyboardButton('Написать разработчику',
                                          url='https://docs.google.com/forms/d/e/1FAIpQLSeIBw7ZnQNQXDuV2AaJo9WCIDZP0klz7Y39OWapXZYpdD9HlA/viewform?usp=sf_link')
    keyboard.add(key_help)
    bot.send_message(message.chat.id, 'В боте собраны все полезные ссылки для начинающего тестировшика\n' +
                     '1. Ссылки на курсы платные и бесплатные\n' +
                     '2. Ссылка на интересные статьи\n' +
                     '3. Ссылки на полезные каналы в телеграмм\n', reply_markup=keyboard)


# response to receive
@bot.message_handler(commands=['receive'])
def link_command(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(types.InlineKeyboardButton(text='Обучение', callback_data='education'),
                 types.InlineKeyboardButton(text='Полезные ссылки', callback_data='linksplus'))
    keyboard.row(types.InlineKeyboardButton(text='Блоги, каналы', callback_data='tg'),
                 types.InlineKeyboardButton(text='Книги', callback_data='books'))
    keyboard.row(types.InlineKeyboardButton(text='Учить английский', callback_data='eng'),
                 types.InlineKeyboardButton(text='Питон', callback_data='pyth'))
    bot.send_message(message.chat.id, 'Выбери по какому разделу получить ссылки', reply_markup=keyboard)


# Response to text
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    message.text.lower()
    if message.text == 'Привет':
        bot.send_message(message.from_user.id,
                         text='Выбери раздел с полезными ссылками /receive или обратись к помощи /help')
    else:
        bot.send_message(message.from_user.id,
                         'Не понимаю тебя! Выбери раздел с полезными ссылками /receive или обратись к помощи /help')


# Response to the photo, sticker, audio, document
@bot.message_handler(content_types=['photo', 'sticker', 'audio', 'document'])
def get_other_messages(message):
    bot.send_message(message.chat.id, 'Спасибо за старание, но бот знает только команды:(. Обратись к /help.')

# Calling call functions
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за пользование ботом!')
    if call.data == 'education':
        text = first[0]
        bot.send_message(call.message.chat.id, text, reply_markup=k.keyboard_education)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    elif call.data == 'or':
        text = random.choice(first[1:5])
        bot.send_message(call.message.chat.id, text, reply_markup=k.keyboard_or)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    elif call.data == 'linksplus':
        text = linki[0]
        bot.send_message(call.message.chat.id, text, reply_markup=k.keyboard_link)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    elif call.data == 'orl':
        text = random.choice(linki[1:])
        bot.send_message(call.message.chat.id, text, reply_markup=k.keyboard_linkor)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    elif call.data == 'tg':
        text = chats[0]
        bot.send_message(call.message.chat.id, text, reply_markup=k.keyboardtg)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    elif call.data == 'org':
        text = random.choice(chats[1:])
        bot.send_message(call.message.chat.id, text, reply_markup=k.keyboard_org)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    elif call.data == 'books':
        text = books[0]
        bot.send_message(call.message.chat.id, text, reply_markup=k.keyboard_books)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    elif call.data == 'orb':
        text = random.choice(books[1:])
        bot.send_message(call.message.chat.id, text, reply_markup=k.keyboard_orb)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    elif call.data == 'eng':
        text = engl[0]
        bot.send_message(call.message.chat.id, text, reply_markup=k.keyboard_eng)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    elif call.data == 'ore':
        text = random.choice(engl[1:])
        bot.send_message(call.message.chat.id, text, reply_markup=k.keyboard_ore)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    elif call.data == 'pyth':
        text = pyth[0]
        bot.send_message(call.message.chat.id, text, reply_markup=k.keyboard_pyth)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    elif call.data == 'orp':
        text = random.choice(engl[1:])
        bot.send_message(call.message.chat.id, text, reply_markup=k.keyboard_orp)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    elif call.data == 'back':
        bot.send_message(call.message.chat.id, "Вы вернулись на главную страницу, выберите раздел снова", reply_markup=None)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)


bot.polling(none_stop=True, interval=0) #starting the survey
