from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command


router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Я способен помочь любыми средствами")


@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"EBASH")