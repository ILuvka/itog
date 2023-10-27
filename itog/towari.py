from dataclasses import dataclass
from aiogram.types import LabeledPrice

PROVIDER_TOKEN = "1744374395:TEST:4a71b1e6e882ac6208c2"
towars_list_str = ['GTX_1650','RTX_4060','I5_11400f','I7_12700f']

@dataclass
class Item:
   title: str
   description: str
   start_parameter: str
   currency: str
   prices: [LabeledPrice]
   provider_data: dict = None # провайдер платежа
   photo_url: str = None
   photo_size: int = None
   photo_width: int = None
   photo_height: int = None

   need_name: bool = False
   need_phone_number: bool = False
   need_email: bool = False
   need_shipping_address: bool = False

   send_phone_number_to_provider: bool = False
   send_email_to_provider: bool = False
   is_flexible: bool = False
   provider_token: str = PROVIDER_TOKEN
   def generate_invoices(self):
       return self.__dict__

GTX_1650 = Item(
   title='Видеокарта GTX_1650',
   description='Достаточно мощная ИГРОВАЯ видеокарта в малом бюджете!',
   currency='RUB',
   prices=[
       LabeledPrice(
           label='Видеокарта GTX_1650',
           amount=17_999_00
       ),
       LabeledPrice(
           label='Доставка',
           amount=500_00
       ),
       LabeledPrice(
           label='Скидка',
           amount=-2_000_00
       )

   ],
   start_parameter='create_invoice_gtx_1650',
   photo_url="https://c.dns-shop.ru/thumb/st1/fit/200/200/88afaa75aaf253e2bcf30961757f648e/75ca1fca4dd7ecfed85669b1379ea023b3ebeabcd59f3a9d9ca76e1b4e7bfb1d.jpg",
   photo_size=600,
   need_shipping_address=True,
   is_flexible=True
)

RTX_4060 = Item(
   title='Видеокарта RTX_4060',
   description='МОЩНАЯ и ИГРОВАЯ видеокарта в среднем бюджете!',
   currency='RUB',
   prices=[
       LabeledPrice(
           label='Видеокарта RTX_4060',
           amount=39_799_00
       ),
       LabeledPrice(
           label='Доставка',
           amount=500_00
       ),
       LabeledPrice(
           label='Скидка',
           amount=-2_000_00
       )

   ],
   start_parameter='create_invoice_rtx_4060',
   photo_url="https://c.dns-shop.ru/thumb/st1/fit/320/250/6f870593a36fe11ef1eee92ae6b4d36e/f1b6ba1dfa062a28dc3e77f10042664c4bd0981fd39cfc8f9599eda6b0e1741d.jpg",
   photo_size=600,
   need_shipping_address=True,
   is_flexible=True

)

I5_11400f = Item(
   title='Процессор Intel core I5_11400f',
   description='Отличный процессор для игр! Отлично подойдет для дешевой сборки ПК!',
   currency='RUB',
   prices=[
       LabeledPrice(
           label='Процессор Intel core I5_11400f',
           amount=14_999_00
       ),
       LabeledPrice(
           label='Доставка',
           amount=500_00
       ),
       LabeledPrice(
           label='Скидка',
           amount=-2_000_00
       )

   ],
   start_parameter='create_invoice_intel_11400',
   photo_url="https://c.dns-shop.ru/thumb/st1/fit/200/200/61353ae935c91fa9b54c543cd8008161/265f413b3a925b4fb9aa486275e27a5c4d1c215e9729de0cc574b86a41c21e1b.jpg",
   photo_size=600,
   need_shipping_address=True,
   is_flexible=True

)

I7_12700f = Item(
   title='Процессор Intel core I7_12700f',
   description='ОТЛИЧНЫЙ процессор для МОЩНЫХ игр! Подойдет для СРЕДНИХ и ТОПОВЫХ сборок ПК!',
   currency='RUB',
   prices=[
       LabeledPrice(
           label='Процессор Intel core I7 12700f',
           amount=30_799_00
       ),
       LabeledPrice(
           label='Доставка',
           amount=500_00
       ),
       LabeledPrice(
           label='Скидка',
           amount=-2_000_00
       )

   ],
   start_parameter='create_invoice_intel_12700',
   photo_url="https://c.dns-shop.ru/thumb/st1/fit/200/200/2b15be6f3d04c9ceb16b8bc9e2fbbd18/66f830bccaf933d9e40b749d00c780910cb927ca81f573186d1a1466e02a02bb.jpg.webp",
   photo_size=600,
   need_shipping_address=True,
   is_flexible=True
)
towars_list = [GTX_1650, RTX_4060, I5_11400f, I7_12700f]