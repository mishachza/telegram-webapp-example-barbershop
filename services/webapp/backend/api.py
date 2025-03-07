from typing import Dict
import hashlib
import hmac
import urllib.parse
import asyncio

from fastapi import FastAPI, HTTPException, Depends, Request
from pydantic import BaseModel

from config import TELEGRAM_BOT_TOKEN, ADMIN_TELEGRAM_ID
from main import bot


app = FastAPI()


class ValidationResponse(BaseModel):
    isValid: bool

def validate_telegram_data(init_data: str) -> bool:
    try:
        # Шаг 1: Декодирование URL-encoded строки
        query_params = urllib.parse.parse_qs(init_data)

        # Шаг 2: Сортировка параметров
        sorted_params = sorted([(k, v[0]) for k, v in query_params.items()])

        # Шаг 3: Исключение hash
        hash_value = None
        data_params = []
        for k, v in sorted_params:
            if k == 'hash':
                hash_value = v
            else:
                data_params.append(f"{k}={v}")

        # Шаг 4: Формирование тела
        data_string = "\n".join(data_params)

        # Шаг 5: HMAC-SHA256
        secret_key = hashlib.sha256(TELEGRAM_BOT_TOKEN.encode()).digest()
        calculated_hash = hmac.new(secret_key, data_string.encode(), hashlib.sha256).hexdigest()

        # Шаг 6: Сравнение хэшей
        return calculated_hash == hash_value

    except Exception as e:
        print(f"Ошибка валидации: {e}")
        return False

class InitDataRequest(BaseModel):
    initData: str

@app.post("/api/validate_init_data", response_model=ValidationResponse)
async def validate_init_data_endpoint(request: InitDataRequest):
    is_valid = validate_telegram_data(request.initData)
    if is_valid:
        message = "Данные валидны."
    else:
        message = "Данные не валидны."
    asyncio.create_task(bot.send_message(chat_id=int(ADMIN_TELEGRAM_ID), text=message))
    return ValidationResponse(isValid=is_valid)