from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

locations = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Qatortol"),
            KeyboardButton(text="Chilanzar")
        ],
        [
            KeyboardButton(text="Rivera"),
            KeyboardButton(text="TTZ")
        ],
    ],
    resize_keyboard=True,
)
