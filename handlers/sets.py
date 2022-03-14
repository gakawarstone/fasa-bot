import aiogram
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove

from bot_config import bot

data = {}


async def hello(message: aiogram.types.Message):
    await message.answer('Приветсвую вас этот бот выполняет операции над множествами',
                          reply_markup=ReplyKeyboardRemove())
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
    await choose_operate(message)


async def print_result(message: aiogram.types.Message, state: FSMContext):
    await state.finish()
    a = data['set_a']
    b = data['set_b']
    operate = message.text

    if (operate == 'Пересечение'):
        await message.answer('Пересечение = ' + str(a.intersection(b)))
    elif (operate == 'Обьединение'):
        await message.answer('Обьединение = ' + str(a.union(b)))
    elif (operate == 'Разность A B'):
        await message.answer('Разность А В = ' + str(a - b))
    elif (operate == 'Разность B A'):
        await message.answer('Разность В А = ' + str(b - a))
    elif (operate == 'Cимметрическая разница'):
        await message.answer('Cимметрическая разница' + str(a.symmetric_difference(b)))
    elif (operate == 'Дополнение B до A'):
        if a.issuperset(b):
            await message.answer('Дополнение множества В до множества А:' + str(a.difference(b)))
        else:
            await message.answer('Множество B не является подмножетвом множества A')
    elif (operate == 'Разбиение B'):
        await message.answer('Разбиение' + str(b.symmetric_difference(a)))

    buttons = [['Да', 'Нет'], ['Поменять множества']]
    bot.add_keyboard('another_operate', buttons)
    await message.answer('Хотите выполните еще операцию?',
                          reply_markup=bot.keyboards['another_operate'])
    bot.add_state_handler(FSM.check_another_operate, check_another_operate)
    await FSM.check_another_operate.set()


async def check_another_operate(message: aiogram.types.Message, state: FSMContext):
    await state.finish()
    if (message.text == 'Да'):
        await choose_operate(message)
    elif (message.text == 'Поменять множества'):
        await hello(message)
    elif (message.text == 'Нет'):
        await message.answer('Спасибо за использование бота ждем вас еще\nесли захотите снова запустить бота напишите /start',
                              reply_markup=ReplyKeyboardRemove())
    

async def choose_operate(message: aiogram.types.Message):
    buttons = [['Пересечение', 'Обьединение'], 
               ['Разность A B', 'Разность B A'],
               ['Cимметрическая разница', 'Дополнение B до A'],
               ['Разбиение B']]
    bot.add_keyboard('operate_choose', buttons)
    await message.answer('Пожалуйста выберите 🛠 <b>операцию</b>',
                         reply_markup=bot.keyboards['operate_choose'])
    bot.add_state_handler(FSM.print_result, print_result)
    await FSM.print_result.set()


class FSM(StatesGroup):
    get_set_a = State()
    get_set_b = State()
    print_result = State()
    check_another_operate = State()