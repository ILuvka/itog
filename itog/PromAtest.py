from buttons import level, basmenu_markup, vipmenu_markup, premmenu_markup
import logging
from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN, PREM, VIP

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(text='НАЗАД')
async def back(msg: types.Message):
    await msg.answer('Вы вернулись в меню!', reply_markup=level)

@dp.message_handler(commands='start')
async def Create_buttons(msg: types.Message):
    await msg.answer('da', reply_markup=level)

@dp.message_handler()
async def choise(msg: types.Message):
    print(msg.text,)
    if msg.text == 'PREMIUM' and msg.from_user.id in PREM:
        await msg.answer('Вы выбрали подписку Премиум!', reply_markup=premmenu_markup)
    elif msg.text == 'PREMIUM' and not msg.from_user.id in PREM:
        await msg.answer('Вас нет в списке премиум пользователей!')

    if msg.text == 'VIP' and msg.from_user.id in VIP:
        await msg.answer('Вы выбрали подписку Вип!',reply_markup=vipmenu_markup)
    elif msg.text == 'VIP' and not msg.from_user.id in VIP:
        await msg.answer('Вас нет в списке вип пользователей!')

    if msg.text == 'BASIC':
        await msg.answer('Вы выбрали подписку Базовый',reply_markup=basmenu_markup)



if __name__ == "__main__":
   executor.start_polling(dp, skip_updates=True)
