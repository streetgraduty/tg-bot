from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
import logging
from test.test_keyboard import true_false
router = Router()

@router.callback_query(F.data == "nuton")
async def nuton_test(callback: CallbackQuery):
    markup = true_false()
    await callback.message.edit_text(
        text="""1. Какой из следующих законов описывает инерцию?

   • A) Первый закон Ньютона (правильный)

   • B) Второй закон Ньютона

   • C) Третий закон Ньютона

   • D) Закон всемирного тяготения
""",reply_markup=markup
    )