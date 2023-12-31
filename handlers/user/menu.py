from aiogram.types import Message, ReplyKeyboardMarkup
from loader import dp
from filters import IsAdmin, IsUser

catalog = '🛍️ Каталог'
balance = '💰 Баланс'
cart = '🛒 Корзина'
delivery_status = '🚚 Статус заказа'

settings = '⚙️ Настройка каталога'
orders = '🚚 Заказы'
questions = '❓ Вопросы'

@dp.message_handler(IsAdmin(), text='Меню')
async def admin_menu(message: Message):

    markup = ReplyKeyboardMarkup(selective=True)
    markup.add(settings)
    markup.add(questions, orders)

    await message.answer('Меню ', reply_markup=markup)

@dp.message_handler(IsUser(), text='Меню')
async def user_menu(message: Message):
    markup = ReplyKeyboardMarkup(selective=True)
    markup.add(catalog)
    markup.add(balance, cart)
    markup.add(delivery_status)

    await message.answer('Меню ', reply_markup=markup)