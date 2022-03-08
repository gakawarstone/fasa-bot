import aiogram
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from bot_config import bot


async def hello(message: aiogram.types.Message):
    await message.answer('Приветсвую вас этот бот выполняет операции над множествами')
    bot.add_state_handler(FSM.get_data, get_data)
    await FSM.get_data.set()


async def get_data(message: aiogram.types.Message, state: FSMContext):
    await state.finish()


class FSM(StatesGroup):
    get_data = State()