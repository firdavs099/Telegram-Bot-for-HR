from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from loader import bot
from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from data.config import GROUP, ADMINS
from datetime import datetime
from keyboards.default import yes_or_no, phones, locations, shift
from states import get_data


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"🇷🇺 Привет, <b>{message.from_user.full_name}!</b>\n"
                         "Введите свое имя: \n\n"
                         f"🇺🇿 Salom, <b>{message.from_user.full_name}!</b>\n"
                         "Ismingizni kiriting: ")
    await get_data.name.set()


@dp.message_handler(state=get_data.name)
async def get_name(message: types.Message, state: FSMContext):
    answer_name = message.text
    await state.update_data(name=answer_name)

    await message.answer("* Дата рождения: \n\n"
                         "* Tug'ilgan kun:")
    await get_data.next()


@dp.message_handler(state=get_data.db)
async def get_name(message: types.Message, state: FSMContext):
    answer_db = message.text
    await state.update_data(db=answer_db)

    await message.answer("* Phone: \n\n"
                         "* Phone:\n"
                         "(<i>+998990001122</i>)\n\n")
    await get_data.next()


@dp.message_handler(state=get_data.phone)
async def get_number(message: types.Message, state: FSMContext):
    answer_num = message.text
    await state.update_data(number=answer_num)

    await message.answer("* А вы студент?\n\n"
                         "* Siz talabamisiz?", reply_markup=yes_or_no)
    await get_data.next()


@dp.message_handler(state=get_data.is_student)
async def is_std(message: types.Message, state: FSMContext):
    answer_std = message.text
    await state.update_data(student=answer_std)

    await message.answer("* В каком филиале вы хотите работать? \n\n"
                         "* Qaysi filialda ishlamoqchisiz?", reply_markup=locations)
    await get_data.next()


@dp.message_handler(state=get_data.loc)
async def get_loc(message: types.Message, state: FSMContext):
    locc = message.text
    await state.update_data(location=locc)

    await message.answer("* Cмена: ", reply_markup=shift)
    await get_data.next()


@dp.message_handler(state=get_data.shiftt)
async def get_shift(message: types.Message, state: FSMContext):
    shift_time = message.text
    await state.update_data(shift=shift_time)

    await message.answer("* Отпыт работы: \n\n"
                         "* Ish tajribasi:", reply_markup=yes_or_no)
    await get_data.next()


@dp.message_handler(state=get_data.exp)
async def get_exp(message: types.Message, state: FSMContext):
    data = await state.get_data()
    name = data.get("name")
    db = data.get("db")
    phone = data.get("number")
    student = data.get("student")
    location = data.get("location")
    shiftt = data.get("shift")
    exp = message.text
    dates = datetime.now().strftime("%d/%m/%Y %H:%M")
    prof_detail = ("<b>Candidate</b>:\n\n"
                   f"* <i><b>Name</b></i>: {name}\n"
                   f"* <i><b>Date of birth</b></i>: {db}\n"
                   f"* <i><b>Is student</b></i>: {student}\n"
                   f"* <i><b>Phone</b></i>: {phone}\n"
                   f"* <i><b>Location</b></i>: {location}\n"
                   f"* <i>Time</i>: {shiftt}\n"
                   f"* <i><b>experience</b></i>: {exp}\n\n"
                   f"Registered time:   {str(dates)}")
    await message.answer("Thanks", reply_markup=ReplyKeyboardRemove())
    await bot.send_message(chat_id=GROUP, text=prof_detail)
    await state.finish()


