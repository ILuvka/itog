from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

button_back = KeyboardButton('НАЗАД')

button_VD = KeyboardButton('ВИДЕОКАРТЫ')
button_CP = KeyboardButton('ПРОЦЕССОРЫ')
categories = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
categories.row(button_CP, button_VD)

button_gtx_1650 = KeyboardButton('GTX_1650')
button_rtx_4060 = KeyboardButton('RTX_4060')
videocards = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
videocards.row(button_gtx_1650, button_rtx_4060)
videocards.add(button_back)

# promejutochnaya atest:
button_vipmenu = KeyboardButton('МЕНЮ ДЛЯ ВИП ПОЛЬЗОВАТЕЛЕЙ')
button_basicmenu = KeyboardButton('МЕНЮ ДЛЯ ОБЫЧНЫХ ПОЛЬЗОВАТЕЛЕЙ')
button_premmenu = KeyboardButton('МЕНЮ ДЛЯ ПРЕМ ПОЛЬЗОВАТЕЛЕЙ')

PREM_button = KeyboardButton('PREMIUM')
VIP_button = KeyboardButton('VIP')
BASIC_button = KeyboardButton('BASIC')
level = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
level.row(PREM_button,VIP_button,BASIC_button)

basmenu_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
basmenu_markup.add(button_basicmenu)
basmenu_markup.add(button_back)

premmenu_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
premmenu_markup.add(button_premmenu)
premmenu_markup.add(button_back)

vipmenu_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
vipmenu_markup.add(button_vipmenu)
vipmenu_markup.add(button_back)