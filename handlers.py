from aiogram import types, F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
import kb


def ne():
    import datetime
    now = datetime.datetime.today()
    NY = datetime.datetime(2024, 1, 1)
    d = NY-now               
    mm, ss = divmod(d.seconds, 60)
    hh, mm = divmod(mm, 60)
    res = round((d.days * -1)*100/366)
    return f"Прошло уже {res}% 2024 года.\n<b>Хватит окладывать. Пора.</b>"

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Я способен помочь любыми средствами")


@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"EBASH RIGHT NOW BRUH", reply_markup=kb.menu)

@router.callback_query(F.data == "upm")
async def newy(call: CallbackQuery):
    ans = ne()
    await call.message.answer(ans, reply_markup=kb.menu)
    await call.answer()
@router.callback_query(F.data == "tofukk")
async def newy(call: CallbackQuery):
    ans = "<b>ЕБАШИТЬ ПОРА БРАТ, ТРАХАТЬ ВСЕ ДЕРЬМО. ИДТИ К МЕЧТЕ</b>"
    await call.message.answer(ans, reply_markup=kb.menu)
    await call.answer()
    
    
@router.callback_query(F.data == "view")
async def newy(call: CallbackQuery):
    ans = "<i>Красота есть во всем, не каждому суждено её увидеть</i>"
    await call.message.answer(ans, reply_markup=kb.menu)
    await call.answer()