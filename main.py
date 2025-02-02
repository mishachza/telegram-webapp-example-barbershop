import asyncio

from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext

from config import TELEGRAM_BOT_TOKEN


bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()
router = Router()


@router.message(CommandStart(), StateFilter('*'))
async def get_start(message: Message, state: FSMContext):
    await state.clear()

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())