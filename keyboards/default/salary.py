from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

expected_salary = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1.000.000")
        ],
        [
            KeyboardButton(text="1.500.000")
        ],
        [
            KeyboardButton(text="2.000.000")
        ],
        [
            KeyboardButton(text="3.000.000>")
        ],
    ]
)