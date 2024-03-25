from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
menu = [
    [InlineKeyboardButton(text="СОЗИДАТЬ", callback_data="view")],
    [InlineKeyboardButton(text="ТРАХАТЬ", callback_data="tofukk")],
    [InlineKeyboardButton(text="НЕ УПУСТИ", callback_data="upm")], 
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="get it")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="get out", callback_data="menu")]])