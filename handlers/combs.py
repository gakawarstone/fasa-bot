import math
import random

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

    d = a.union(b.intersection(c))
    await message.answer('D = ' + str(d))

    e = (c - b).intersection(a)
    await message.answer('E = ' + str(e))

    if (a.union(b).union(c) == range(1, 11)):
        await message.answer('Множества содержат все арабские числа')
    else:
        await message.answer('Множество не сожержить все арабские числа')

    k = 10
    m = 20
    n = 2

    await message.answer('Генерирую множество А')
    a = set([random.randint(0, m) for i in range(k)])

    await message.answer('Задаю случайный элемент')
    el = random.randint(0, m + n)

    if el in a:
        await message.answer('Элемент входит в множество А')
    else:
        await message.answer('Элемент не входин в множетсво А')

    await message.answer('Кординальное число множетсва А = ' + str(len(a)))

    await message.answer('Кординальное число булеана множетсва А = ' + str(math.factorial(len(a))))

    name = set([i for i in 'ИВАН'])
    surname = set([i for i in 'ПИННЕКЕР'])
    dad_name = set([i for i in 'ИВАНОВИЧ'])

    await message.answer('Обьединение = ' + str(name.union(surname).union(dad_name)))
    await message.answer('Пересечение = ' + str(name.intersection(surname).intersection(dad_name)))
    await message.answer('А\B = ' + str(name - surname))
    await message.answer('B\A = ' + str(name - surname))
    await message.answer('Симметрическая разница = ' + str(name.symmetric_difference(surname)))

    k = 10
    m = 20

    a = set([random.randint(0, m) for i in range(k)])
    b = set([random.randint(0, m) for i in range(k)])

    if (a.issuperset(b)):
        await message.answer('А принадлежит В')
    else:
        await message.answer('А не принадлежит В')

    if b.issuperset(a):
        await message.answer('B принадлежит A')
    else:
        await message.answer('B не принадлежит A')
    
    if (a.intersection(b) != set()):
        await message.answer('А пересекает B')
    else:
        await message.answer('A не пересекает В')


class FSM(StatesGroup):
    get_set_a = State()
    get_set_b = State()
    print_result = State()
    check_another_operate = State()
