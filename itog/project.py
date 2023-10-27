from buttons import categories
import logging
from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN
from towari import towars_list, towars_list_str
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

button_back = KeyboardButton('НАЗАД')
towar = None

@dp.message_handler(commands='start')
async def start_button(msg: types.Message):
    await msg.answer('Вас приветствует бот-компьютерщик! Подбери себе детали для пк мечты!', reply_markup=categories)

@dp.message_handler(text='ВИДЕОКАРТЫ')
async def VD(msg: types.Message):
    button_gtx_1650 = KeyboardButton('GTX_1650')
    button_rtx_4060 = KeyboardButton('RTX_4060')
    videocards = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    videocards.row(button_gtx_1650, button_rtx_4060)
    videocards.add(button_back)

    await msg.answer('Видеокарты!', reply_markup=videocards)
    return videocards
@dp.message_handler(text='ПРОЦЕССОРЫ')
async def CP(msg: types.Message):
    button_11400f = KeyboardButton('I5_11400f')
    #\/\/\/\/\/\/ ВЫДАЕТ ОШИБКУ!!!!!!!!!!!!!!!!!!!!!!!!!!!!\/\/\/\/\/\/
    button_12700f = KeyboardButton('I7_12700f')
    #/\/\/\/\/\/\ ВЫДАЕТ ОШИБКУ!!!!!!!!!!!!!!!!!!!!!!!!!!!!/\/\/\/\/\/\
    processors = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    processors.row(button_12700f, button_11400f)
    processors.add(button_back)
    await msg.answer('Процессоры!', reply_markup=processors)

@dp.message_handler(text='НАЗАД')
async def back(msg: types.Message):
    await msg.answer('Вы вернулись в меню!', reply_markup=categories)

POST_REGULAR_SHIPPING = types.ShippingOption(
   id='post_reg',
   title='Почтой',
   prices=[
       types.LabeledPrice(
           'Обычная коробка', 0
       ),
       types.LabeledPrice(
           'Почтой', 500_00
       ),
   ]
)

POST_FAST_SHIPPING = types.ShippingOption(
   id='post_fast',
   title='Почтой ускоренная',
   prices=[
       types.LabeledPrice(
           'Прочная упаковка', 200_00
       ),
       types.LabeledPrice(
           'Срочной почтой', 1000_00
       ),
   ]
)

PICKUP_SHIPPING = types.ShippingOption(
   id='pickup',
   title='Самовывоз',
   prices=[
       types.LabeledPrice(
           'Самовывоз из магазина', -100_00
       ),
   ]
)

@dp.message_handler(text=towars_list_str)
async def check_towar(msg: types.Message):

    twr = msg.text

    for i in towars_list:
        print(str((i.title).split('Видеокарта ')))

        if twr in str(i.title).split('Видеокарта ') or twr in str(i.title).split('Процессор Intel core '):
            towar = i

            await bot.send_invoice(msg.from_user.id, **towar.generate_invoices(), payload='12345')
            await msg.answer("Вы выбрали следующий товар:", reply_markup=categories)

@dp.shipping_query_handler()
async def choose_shipping(query: types.ShippingQuery):
   if query.shipping_address.country_code == 'RU':
       await bot.answer_shipping_query(shipping_query_id=query.id, shipping_options=[
           POST_REGULAR_SHIPPING,
           POST_FAST_SHIPPING,
           PICKUP_SHIPPING
       ],
                                       ok=True)
   elif query.shipping_address.country_code == 'US':
       await bot.answer_shipping_query(shipping_query_id=query.id,
                                       ok=False, error_message='Сюда не доставляем')

   else:
       await bot.answer_shipping_query(shipping_query_id=query.id,
                                       shipping_options=[POST_REGULAR_SHIPPING],
                                       ok=True)

@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(query: types.PreCheckoutQuery):
   await bot.answer_pre_checkout_query(pre_checkout_query_id=query.id, ok=True)
   await bot.send_message(chat_id=query.from_user.id, text='Спасибо за покупку')


if __name__ == "__main__":
   executor.start_polling(dp, skip_updates=True)
