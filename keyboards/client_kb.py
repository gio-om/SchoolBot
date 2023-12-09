from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button_algebra = KeyboardButton('/Алгебра')
button_geometry = KeyboardButton('/Геометрия')
button_specmat = KeyboardButton('/Спецмат')
button_back = KeyboardButton('/Назад')

#kb for start
kb_client_start = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_start.row(button_algebra, button_geometry, button_specmat)


#kb for back
kb_client_back = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_back.row(button_algebra, button_geometry, button_specmat)


#kb for subject
kb_client_subject = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_subject.add(button_back)


#kb for new request
kb_client_new_request = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_new_request.add(button_back)