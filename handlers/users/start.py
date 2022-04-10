from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from loader import bot
from loader import dp
from data.config import GROUP
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from datetime import datetime
from keyboards.default import yes_or_no,  locations, shift, expected_salary
from states import get_data


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, <b>{message.from_user.full_name}!</b>\n"
                         "👤 Введите Ф.И.О.(пример: Иван Иванов Иванович)")
    await get_data.name.set()


@dp.message_handler(state=get_data.name)
async def get_name(message: types.Message, state: FSMContext):
    answer_name = message.text
    await state.update_data(name=answer_name)

    await message.answer("📅 Укажите дату своего рождения (пример, 18.03.1995):")
    await get_data.next()


@dp.message_handler(state=get_data.db)
async def get_name(message: types.Message, state: FSMContext):
    answer_db = message.text
    await state.update_data(db=answer_db)

    await message.answer("📱 Укажите Ваш контактный номер телефона (пример: +998931234567):")
    await get_data.next()


@dp.message_handler(state=get_data.phone)
async def get_number(message: types.Message, state: FSMContext):
    answer_num = message.text
    await state.update_data(number=answer_num)

    await message.answer("📱 Дополнительный номер для связи")
    await get_data.next()


@dp.message_handler(state=get_data.extra_phone)
async def ext_phn(message: types.Message, state: FSMContext):
    answer_extra_num = message.text
    await state.update_data(extra_num=answer_extra_num)

    await message.answer("👨‍🎓 Вы студент?", reply_markup=yes_or_no)
    await get_data.next()


@dp.message_handler(state=get_data.is_student)
async def is_std(message: types.Message, state: FSMContext):
    answer_std = message.text
    await state.update_data(student=answer_std)

    await message.answer("📍 В каком филиале хотите работать? \n", reply_markup=locations)
    await get_data.next()


@dp.message_handler(state=get_data.loc)
async def get_loc(message: types.Message, state: FSMContext):
    locc = message.text
    await state.update_data(location=locc)

    await message.answer("🕙 Смена: \n\n", reply_markup=shift)
    await get_data.next()


@dp.message_handler(state=get_data.shiftt)
async def get_shift(message: types.Message, state: FSMContext):
    work_time = message.text
    await state.update_data(shift=work_time)

    await message.answer("* Опыт: \n\n", reply_markup=yes_or_no)
    await get_data.next()


@dp.message_handler(state=get_data.exp)
async def get_exp(message: types.Message, state: FSMContext):
    exp = message.text
    await state.update_data(experince=exp)

    await message.answer("Введите названия двух последних  мест работы (название организации, должность, период работы). \n\nПример: 'MobiUz', оператор Call-центра, 2015-2018", reply_markup=ReplyKeyboardRemove())
    await get_data.next()


@dp.message_handler(state=get_data.work_place)
async def get_work_plc(message: types.Message, state: FSMContext):
    work_plc = message.text
    await state.update_data(work_place=work_plc)

    await message.answer("💵  Укажите ожидаемый уровень заработной платы.", reply_markup=expected_salary)
    await get_data.next()


@dp.message_handler(state=get_data.salary)
async def get_sal(message: types.Message, state: FSMContext):
    data = await state.get_data()
    name = data.get("name")
    db = data.get("db")
    phone = data.get("number")
    ext_phone = data.get("extra_num")
    student = data.get("student")
    location = data.get("location")
    shiftt = data.get("shift")
    experience = data.get("experience")
    work_place = data.get("work_place")
    salary = message.text
    dates = datetime.now().strftime("%d/%m/%Y %H:%M")
    details = (
        "<b>Candidate</b>:\n\n"
        f"* <i><b>Name</b></i>: {name}\n"
        f"* <i><b>Date of birth</b></i>: {db}\n"
        f"* <i><b>Is student</b></i>: {student}\n"
        f"* <i><b>Phone</b></i>: {phone}\n"
        f"* <i><b>extra phone</b></i>: {ext_phone}\n"
        f"* <i><b>Location</b></i>: {location}\n"
        f"* <i><b>Time</b></i>: {shiftt}\n"
        f"* <i><b>Experience</b></i>: {experience}\n"
        f"* <i><b>Work place</b></i>: {work_place}\n"
        f"* <i><b>Salary</b></i>: {salary}\n\n"
        f"Registered time:   {str(dates)}"
    )

    await message.answer("Благодарим Вас. \nВы включены в список кандидатов на рассмотрение.", reply_markup=ReplyKeyboardRemove())
    await bot.send_message(chat_id=GROUP, text=details)
    await state.finish()
