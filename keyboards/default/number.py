from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phones = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Share Contact", request_contact=True)
        ],
    ],
    resize_keyboard=True
)
