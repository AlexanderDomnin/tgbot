from telebot import types

keyboard = types.InlineKeyboardMarkup()
        keyboard.row(types.InlineKeyboardButton(text='Еще', callback_data='or'),
                     types.InlineKeyboardButton("Назад", callback_data='back'))

keyboardor = types.InlineKeyboardMarkup()
        keyboardor.row(types.InlineKeyboardButton(text='Еще', callback_data='or'),
                             types.InlineKeyboardButton("Назад", callback_data='back'))

keyboardlink = types.InlineKeyboardMarkup()
keyboardlink.row(types.InlineKeyboardButton(text='Еще', callback_data='orl'),
             types.InlineKeyboardButton("Назад", callback_data='back'))

keyboardlinkor = types.InlineKeyboardMarkup()
keyboardlinkor.row(types.InlineKeyboardButton(text='Еще', callback_data='orl'),
             types.InlineKeyboardButton("Назад", callback_data='back'))

keyboardtg = types.InlineKeyboardMarkup()
keyboardtg.row(types.InlineKeyboardButton(text='Еще', callback_data='org'),
             types.InlineKeyboardButton("Назад", callback_data='back'))

keyboardtgor = types.InlineKeyboardMarkup()
keyboardtgor.row(types.InlineKeyboardButton(text='Еще', callback_data='org'),
             types.InlineKeyboardButton("Назад", callback_data='back'))