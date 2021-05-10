from telebot import types
class keyboard():
    keyboard_education = types.InlineKeyboardMarkup()
    keyboard_education.row(types.InlineKeyboardButton(text='Еще', callback_data='or'),
                           types.InlineKeyboardButton("Назад", callback_data='back'))

    keyboard_or = types.InlineKeyboardMarkup()
    keyboard_or.row(types.InlineKeyboardButton(text='Еще', callback_data='or'),
                    types.InlineKeyboardButton("Назад", callback_data='back'))

    keyboard_link = types.InlineKeyboardMarkup()
    keyboard_link.row(types.InlineKeyboardButton(text='Еще', callback_data='orl'),
                      types.InlineKeyboardButton("Назад", callback_data='back'))

    keyboard_linkor = types.InlineKeyboardMarkup()
    keyboard_linkor.row(types.InlineKeyboardButton(text='Еще', callback_data='orl'),
                        types.InlineKeyboardButton("Назад", callback_data='back'))

    keyboardtg = types.InlineKeyboardMarkup()
    keyboardtg.row(types.InlineKeyboardButton(text='Еще', callback_data='org'),
                   types.InlineKeyboardButton("Назад", callback_data='back'))

    keyboard_org = types.InlineKeyboardMarkup()
    keyboard_org.row(types.InlineKeyboardButton(text='Еще', callback_data='org'),
                     types.InlineKeyboardButton("Назад", callback_data='back'))

    keyboard_books = types.InlineKeyboardMarkup()
    keyboard_books.row(types.InlineKeyboardButton(text='Еще', callback_data='orb'),
                       types.InlineKeyboardButton("Назад", callback_data='back'))

    keyboard_orb = types.InlineKeyboardMarkup()
    keyboard_orb.row(types.InlineKeyboardButton(text='Еще', callback_data='orb'),
                     types.InlineKeyboardButton("Назад", callback_data='back'))

    keyboard_eng = types.InlineKeyboardMarkup()
    keyboard_eng.row(types.InlineKeyboardButton(text='Еще', callback_data='ore'),
                     types.InlineKeyboardButton("Назад", callback_data='back'))

    keyboard_ore = types.InlineKeyboardMarkup()
    keyboard_ore.row(types.InlineKeyboardButton(text='Еще', callback_data='ore'),
                     types.InlineKeyboardButton("Назад", callback_data='back'))

    keyboard_pyth = types.InlineKeyboardMarkup()
    keyboard_pyth.row(types.InlineKeyboardButton(text='Еще', callback_data='orp'),
                      types.InlineKeyboardButton("Назад", callback_data='back'))

    keyboard_orp = types.InlineKeyboardMarkup()
    keyboard_orp.row(types.InlineKeyboardButton(text='Еще', callback_data='pyth'),
                     types.InlineKeyboardButton("Назад", callback_data='back'))
