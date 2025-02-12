import asyncio
import logging
import json
from typing import Any, Callable, Dict, Awaitable

from aiogram import Bot, Dispatcher, Router, F, BaseMiddleware
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, WebAppData, TelegramObject, ContentType
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.enums.parse_mode import ParseMode

from config import TELEGRAM_BOT_TOKEN
#
#
# bot = Bot(token=TELEGRAM_BOT_TOKEN)
# dp = Dispatcher()
# router = Router()
# webapp_url = 'https://telegram-webapp-example-barbershop.onrender.com/'
# webapp_url_test = 'https://mishachza.github.io/telegram-webapp-example-barbershop/'
#
#
# @dp.message(CommandStart(), StateFilter('*'))
# async def get_start(message: Message, state: FSMContext):
#     await state.clear()
#     webapp = [[InlineKeyboardButton(text=f'Оплатить', web_app=WebAppInfo(url=webapp_url))]]
#     keyboard = InlineKeyboardMarkup(inline_keyboard=webapp)
#     print(message)
#     await message.answer('Записаться можно нажав кнопку.', reply_markup=keyboard)
#     await message.answer(
#         'Записаться можно нажав кнопку.',
#         reply_markup=InlineKeyboardMarkup(
#             inline_keyboard=[[InlineKeyboardButton(text=f'Оплатить', web_app=WebAppInfo(url=webapp_url_test))]]))
#
#
# @dp.message(F.content_type == ContentType.WEB_APP_DATA)
# async def parse_data(message: Message):
#     data = json.loads(message.web_app_data.data)
#     await message.answer(f'<b>{data["title"]}</b>\n\n<code>{data["desc"]}</code>\n\n{data["text"]}', parse_mode=ParseMode.HTML)
#
#
# class CheckUserMiddleware(BaseMiddleware):
#     async def __call__(
#             self,
#             handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
#             event: Message,
#             data: Dict[str, Any],
#     ) -> Any:
#         logging.info(f"Получено событие: {event}")
#
#
# async def main():
#     # dp.message.middleware.register(CheckUserMiddleware())
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     asyncio.run(main())

import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from config import TELEGRAM_BOT_TOKEN

logging.basicConfig(level=logging.INFO)


bot = Bot(TELEGRAM_BOT_TOKEN)
dp = Dispatcher()


@dp.message()
async def start(message: types.Message):
    webAppInfo = types.WebAppInfo(url="your-webapp-url")
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text='Отправить данные', web_app=webAppInfo))

    await message.answer(text='Привет!', reply_markup=builder.as_markup())

@dp.message(F.content_type == ContentType.WEB_APP_DATA)
async def parse_data(message: types.Message):
    data = json.loads(message.web_app_data.data)
    await message.answer(f'<b>{data["title"]}</b>\n\n<code>{data["desc"]}</code>\n\n{data["text"]}', parse_mode=ParseMode.HTML)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())