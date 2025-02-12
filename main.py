import asyncio
from typing import Any, Callable, Dict, Awaitable

from aiogram import Bot, Dispatcher, Router, F, BaseMiddleware
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, WebAppData, TelegramObject
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext

from config import TELEGRAM_BOT_TOKEN


bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()
router = Router()
webapp_url = 'https://telegram-webapp-example-barbershop.onrender.com/'


@dp.message(CommandStart(), StateFilter('*'))
async def get_start(message: Message, state: FSMContext):
    await state.clear()
    webapp = [[InlineKeyboardButton(text=f'Оплатить', web_app=WebAppInfo(url=webapp_url))]]
    keyboard = InlineKeyboardMarkup(inline_keyboard=webapp)
    print(message)
    await message.answer('Записаться можно нажав кнопку.', reply_markup=keyboard)

@dp.message()
async def web_app2(message: Message):
    print(message)


class CheckUserMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any],
    ) -> Any:
        print(event)


async def main():
    dp.message.middleware.register(CheckUserMiddleware())
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())