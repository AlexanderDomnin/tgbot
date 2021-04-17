
import random
import telebot
from link import *
from telebot import types


# Ответ на старт
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id,'Привет! Бот покажет тебе полезныe ссылках для начинающего тестировщика!\n'+
                                          '/receive - для выбора раздела с ссылками\n /help - Для справки \n /start - Снова прочесть сообщение')
# Ответ на хелп
@bot.message_handler(commands=['help'])
def help_command(message):
    keyboard = types.InlineKeyboardMarkup()
    key_help = types.InlineKeyboardButton('Написать разработчику',url='https://vk.com/id21929322')
    keyboard.add(key_help)
    bot.send_message(message.chat.id,'В боте собраны все полезные ссылки для начинающего тестировшика\n'+
                      '1. Ссылки на курсы платные и бесплатные\n'+
                      '2. Ссылка на интересные статьи\n'+
                      '3. Ссылки на полезные каналы в телеграмм\n',reply_markup=keyboard)
# Ответ на получить
@bot.message_handler(commands=['receive'])
def link_command(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(types.InlineKeyboardButton(text='Обучение', callback_data='education'),
                 types.InlineKeyboardButton(text='Полезные ссылки', callback_data='linksplus'))
    keyboard.row(types.InlineKeyboardButton(text='Каналы в телеграмм', callback_data='tg'),
                 types.InlineKeyboardButton(text='Книги', callback_data='books'))
    bot.send_message(message.chat.id, 'Выбери по какому разделу получить ссылки', reply_markup=keyboard)

# Ответ на текст
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Привет':
        #bot.send_message(message.from_user.id,"Привет! Бот покажет и расскажет тебе о полезных ссылках для начинающего тестирвощика!")
        #keyboard = types.InlineKeyboardMarkup()
        #key_education = types.InlineKeyboardButton(text='Обучение', callback_data='education')
        #keyboard.add(key_education)
        bot.send_message(message.from_user.id, text='Выбери раздел с полезными ссылками /receive или обратись к помощи /help')
    else:
        bot.send_message(message.from_user.id,'Не понимаю тебя! Выбери раздел /help - для помощи')


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за пользование ботом!')
    if call.data == 'education':
        text = first[0]
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(types.InlineKeyboardButton(text='Еще', callback_data='or'),
                     types.InlineKeyboardButton("Назад", callback_data='back'))
        bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    elif call.data == 'or':
        text = random.choice(first[1:5])
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(types.InlineKeyboardButton(text='Еще', callback_data='or'),
                             types.InlineKeyboardButton("Назад", callback_data='back'))
        bot.send_message(call.message.chat.id, text, reply_markup=keyboard)

    elif call.data == 'back':
        bot.send_message(call.message.chat.id, "Вы вернулись на главную страницу, выберите раздел снова", reply_markup=None)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    elif call.data == 'linksplus':
        text = linki[0]
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(types.InlineKeyboardButton(text='Еще', callback_data='orl'),
                     types.InlineKeyboardButton("Назад", callback_data='back'))
        bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    elif call.data == 'orl':
        text = random.choice(linki[1:5])
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(types.InlineKeyboardButton(text='Еще', callback_data='orl'),
                 types.InlineKeyboardButton("Назад", callback_data='back'))
        bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    elif call.data == 'tg':
        text = chats[0]
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(types.InlineKeyboardButton(text='Еще', callback_data='org'),
                     types.InlineKeyboardButton("Назад", callback_data='back'))
        bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    elif call.data == 'org':
        text = random.choice(chats[1:5])
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(types.InlineKeyboardButton(text='Еще', callback_data='org'),
                 types.InlineKeyboardButton("Назад", callback_data='back'))
        bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    elif call.data == 'books':
        text = books[0]
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(types.InlineKeyboardButton(text='Еще', callback_data='orb'),
                     types.InlineKeyboardButton("Назад", callback_data='back'))
        bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    elif call.data == 'orb':
        text = random.choice(books[1:5])
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(types.InlineKeyboardButton(text='Еще', callback_data='orb'),
                 types.InlineKeyboardButton("Назад", callback_data='back'))
        bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

bot.polling(none_stop=True,interval=0)