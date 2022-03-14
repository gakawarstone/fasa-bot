import aiogram
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove

from bot_config import bot

async def hello(message: aiogram.types.Message):
    await message.answer('Вы включили лабораторную работу номер 5')
    a = {1, 2, 3, 5}
    b = {1, 5, 8}
    c = {1, 3, 5, 8}

    d = a.intersection(b.union(c))
    await message.answer('D = ' + str(d))

    e = (c - b).union(a)
    await message.answer('E =' + str(e))

    if (a + b + c == range(1, 11)):
        await message.answer('Множества содержат все арабские числа')
    else:
        await message.answer('Множество не сожержить все арабские числа')
    

class FSM(StatesGroup):
    get_set_a = State()
    get_set_b = State()
    print_result = State()
    check_another_operate = State()