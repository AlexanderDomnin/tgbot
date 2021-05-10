from app.link import *
from telebot import types

class messages_answer():
    # Ответ на старт
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.from_user.id, 'Привет! Бот покажет тебе полезныe ссылках для начинающего тестировщика!\n' +
                                              '/receive - для выбора раздела с ссылками\n /help - Для справки \n /start - Снова прочесть сообщение')
    # Ответ на хелп
    @bot.message_handler(commands=['help'])
    def help_command(message):
        keyboard = types.InlineKeyboardMarkup()
        key_help = types.InlineKeyboardButton('Написать разработчику', url='https://docs.google.com/forms/d/e/1FAIpQLSeIBw7ZnQNQXDuV2AaJo9WCIDZP0klz7Y39OWapXZYpdD9HlA/viewform?usp=sf_link')
        keyboard.add(key_help)
        bot.send_message(message.chat.id, 'В боте собраны все полезные ссылки для начинающего тестировшика\n' +
                          '1. Ссылки на курсы платные и бесплатные\n' +
                          '2. Ссылка на интересные статьи\n' +
                          '3. Ссылки на полезные каналы в телеграмм\n', reply_markup=keyboard)


    # Ответ на получить
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

    # Ответ на текст
    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        message.text.lower()
        if message.text == 'Привет':
            bot.send_message(message.from_user.id, text='Выбери раздел с полезными ссылками /receive или обратись к помощи /help')
        else:
            bot.send_message(message.from_user.id,'Не понимаю тебя! Выбери раздел с полезными ссылками /receive или обратись к помощи /help')

    #Ответ на фото, стикер, аудио, документы
    @bot.message_handler(content_types=['photo','sticker','audio','document'])
    def get_other_messages(message):
        bot.send_message(message.chat.id,'Спасибо за старание, но бот знает только команды:(. Обратись к /help.')

