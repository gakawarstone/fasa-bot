from multiprocessing.connection import answer_challenge
import aiogram
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from bot_config import bot

data = {}


async def hello(message: aiogram.types.Message):
    await message.answer('Приветсвую вас этот бот выполняет операции над множествами')
    await message.answer('Введите множество А через запятую [1, 2, 3]')
    bot.add_state_handler(FSM.get_set_a, get_set_a)
    await FSM.get_set_a.set()


async def get_set_a(message: aiogram.types.Message, state: FSMContext):
    await state.finish()
    data['set_a'] = set(message.text.split(', '))
    await message.answer('Введите множество B через запятую [1, 2, 3]')
    bot.add_state_handler(FSM.get_set_b, get_set_b)
    await FSM.get_set_b.set()


async def get_set_b(message: aiogram.types.Message, state: FSMContext):
    await state.finish()
    data['set_b'] = set(message.text.split(', '))
    await message.answer('Если хотите получить ответ то напишите да')
    bot.add_state_handler(FSM.print_result, print_result)
    await FSM.print_result.set()


async def print_result(message: aiogram.types.Message, state: FSMContext):
    await state.finish()
    a = data['set_a']
    b = data['set_b']
    await message.answer('Пересечение = ' + str(a.intersection(b)))
    await message.answer('Обьединение = ' + str(a.union(b)))
    await message.answer('Разность А В = ' + str(a - b))
    await message.answer('Разность В А = ' + str(b - a))


class FSM(StatesGroup):
    get_set_a = State()
    get_set_b = State()
    print_result = State()