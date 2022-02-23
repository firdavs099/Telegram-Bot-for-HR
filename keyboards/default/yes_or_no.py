from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

yes_or_no = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✅ Да / Ha"),
            KeyboardButton(text="❌ Нет/ Yo'q")
        ]
    ],
    resize_keyboard=True,
)
