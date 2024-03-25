from aiogram import types, F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
import kb

a = "CgACAgQAAxkBAAOvZcH1VyLVHLxbp13bUYE09TOTMhwAAvcCAAKvXQ1T2t9JcNUxm0E0BA"
b = "CgACAgQAAxkBAAOxZcH1Y71flGQs7P0zoRe3B5-xXdcAAscCAAKiaxxTr4L2eS0mCnY0BA"
c = "CgACAgQAAxkBAAOzZcH1c9jVP_qgr9gBXssUOhF1YhgAAk4FAAKLbJxSyoXXsvHYnwM0BA"
chmp = "CgACAgQAAxkBAAO5ZcH2pU0pMc9XijziRGvUEqNmJegAAgkDAAKszA1TuooR-V3Jc340BA"


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
    await msg.answer_animation(chmp, caption=f"EBASH RIGHT NOW BRUH", reply_markup=kb.menu)

@router.callback_query(F.data == "upm")
async def newy(call: CallbackQuery):
    ans = ne()
    await call.message.answer_animation(c, caption=ans, reply_markup=kb.menu)
    await call.answer()
@router.callback_query(F.data == "tofukk")
async def newy(call: CallbackQuery):
    ans = "<b>ЕБАШИТЬ ПОРА БРАТ, ТРАХАТЬ ВСЕ ДЕРЬМО. ИДТИ К МЕЧТЕ</b>"
    await call.message.answer_animation(a, caption=ans, reply_markup=kb.menu)
    await call.answer()
    
    
@router.callback_query(F.data == "view")
async def newy(call: CallbackQuery):
    ans = "<i>Красота есть во всём, не каждый в состоянии её увидеть</i>"
    await call.message.answer_animation(b, caption=ans, reply_markup=kb.menu)
    await call.answer()
