from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

locations = ReplyKeyboardMarkup(
    keyboard =[
       [
           KeyboardButton(text="Depo Mall"),
           KeyboardButton(text="Chilanzar")
       ],
        [
            KeyboardButton(text="Rivera"),
            KeyboardButton(text="TTZ")
        ],
        [
            KeyboardButton(text="TASHMI"),
            KeyboardButton(text="Ecopark")
        ]
    ],
    resize_keyboard=True,
)