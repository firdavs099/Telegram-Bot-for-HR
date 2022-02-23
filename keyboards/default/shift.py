from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

shift = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="10:00 - 17:00"),
            KeyboardButton(text="15:00 - 22:00")
        ],
    ],
    resize_keyboard=True
)
