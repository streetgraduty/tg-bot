from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message, InlineKeyboardButton, InlineKeyboardMarkup, FSInputFile, BufferedInputFile
from app.keyboard import laws, laws_2, main, help_kb
from app.keyboard import optica, otnosit, termodinamica, quantum, mechanica, electro, fluctuations, otrajenie, svet, save_impulse, sharlya, nuton
from app.keyboard import arhimed, amper, avogadro, boilya, tyagotenia, guka, oma, paskal, dalton, gey_lussaka
from test.test_keyboard import vstroen_test_kb
from test import test_router

from text import text_optica, text_handle_info_command, text_electro, text_quantum_physics, text_oma
from text import text_nuton, text_otnosit, text_termodinamica, text_mechanica, text_fluctuations
from text import text_ampera, text_tygoteniya, text_avogadro, text_arhimeda, text_daltona, text_guka, text_boilya, text_sharlya
from text import text_svet, text_save_impulse, text_otrajenie, text_gey_lussaka, text_paskal, text_laws

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from chatgpt_handler import get_gpt_response
from app.keyboard import generate_payment_qr

router = Router()
router.include_router(test_router)

@router.message(Command("start", prefix="!/"))
async def handle_info_command(message: types.Message):
    markup = main()
    await message.answer(
        text=text_handle_info_command, 
            reply_markup=markup)
    

@router.callback_query(F.data == 'optica')
async def optica_handler(callback: CallbackQuery):
    markup = optica()
    await callback.message.edit_text(
        text=text_optica, reply_markup=markup
    )


@router.callback_query(F.data == 'back')
async def back_handler(callback: CallbackQuery):
    markup = laws()
    await callback.message.edit_text(
        text=text_laws, reply_markup=markup
    )


@router.callback_query(F.data == 'back2')
async def back2(callback: CallbackQuery):
    markup = laws_2()
    await callback.message.edit_text(
        text=text_laws, reply_markup=markup
    )


@router.callback_query(F.data == 'nuton')
async def nuton_handler(callback: CallbackQuery):
    markup = nuton()
    await callback.message.edit_text(
        text=text_nuton, reply_markup=markup
    )


@router.callback_query(F.data == 'otnosit')
async def otnosit_handler(callback: CallbackQuery):
    markup = otnosit()
    await callback.message.edit_text(
        text=text_otnosit, reply_markup=markup
    )


@router.callback_query(F.data == 'termodinamica')
async def termodinamica_handler(callback: CallbackQuery):
    markup = termodinamica()
    await callback.message.edit_text(
        text=text_termodinamica, reply_markup=markup
    )


@router.callback_query(F.data == 'electro')
async def electro_handler(callback: CallbackQuery):
    markup = electro()
    await callback.message.edit_text(
        text=text_electro, reply_markup=markup
    )


@router.callback_query(F.data == 'mechanica')
async def electro_handler(callback: CallbackQuery):
    markup = mechanica()
    await callback.message.edit_text(
        text=text_mechanica, reply_markup=markup
    )


@router.callback_query(F.data == 'quantum_physics')
async def guantum_physics_handler(callback: CallbackQuery):
    markup = quantum()
    await callback.message.edit_text(
        text=text_quantum_physics, reply_markup=markup
    )


@router.callback_query(F.data == 'fluctuations')
async def fluctuations_handler(callback: CallbackQuery):
    markup = fluctuations()
    await callback.message.edit_text(
        text=text_fluctuations, reply_markup=markup
    )


@router.callback_query(F.data == 'next')
async def next_handler(callback: CallbackQuery):
    markup = laws_2()
    await callback.message.edit_text(
        text=text_laws, reply_markup=markup
    )


@router.callback_query(F.data == 'sharlya')
async def sharlya_handler(callback: CallbackQuery):
    markup = sharlya()
    await callback.message.edit_text(
        text=text_sharlya, reply_markup=markup
    )


@router.callback_query(F.data == 'dalton')
async def sharlya_handler(callback: CallbackQuery):
    markup = dalton()
    await callback.message.edit_text(
        text=text_daltona, reply_markup=markup
    )


@router.callback_query(F.data == 'boilya')
async def sharlya_handler(callback: CallbackQuery):
    markup = boilya()
    await callback.message.edit_text(
        text=text_boilya, reply_markup=markup
    )


@router.callback_query(F.data == 'guka')
async def sharlya_handler(callback: CallbackQuery):
    markup = guka()
    await callback.message.edit_text(
        text=text_guka,reply_markup=markup
    )


@router.callback_query(F.data == 'oma')
async def sharlya_handler(callback: CallbackQuery):
    markup = oma()
    await callback.message.edit_text(
        text=text_oma, reply_markup=markup
    )


@router.callback_query(F.data == 'avagadro')
async def sharlya_handler(callback: CallbackQuery):
    markup = avogadro()
    await callback.message.edit_text(
        text=text_avogadro, reply_markup=markup
    )


@router.callback_query(F.data == 'tyagoteniya')
async def sharlya_handler(callback: CallbackQuery):
    markup = tyagotenia()
    await callback.message.edit_text(
        text=text_tygoteniya, reply_markup=markup
    )


@router.callback_query(F.data == 'amper')
async def sharlya_handler(callback: CallbackQuery):
    markup = amper()
    await callback.message.edit_text(
        text=text_ampera, reply_markup=markup
    )


@router.callback_query(F.data == 'arhimed')
async def sharlya_handler(callback: CallbackQuery):
    markup = arhimed()
    await callback.message.edit_text(
        text=text_arhimeda, reply_markup=markup
    )


@router.callback_query(F.data == 'otrajenie')
async def sharlya_handler(callback: CallbackQuery):
    markup = otrajenie()
    await callback.message.edit_text(
        text=text_otrajenie, reply_markup=markup
    )


@router.callback_query(F.data == 'svet')
async def sharlya_handler(callback: CallbackQuery):
    markup = svet()
    await callback.message.edit_text(
        text=text_svet, reply_markup=markup
    )


@router.callback_query(F.data == 'save_impulse')
async def sharlya_handler(callback: CallbackQuery):
    markup = save_impulse()
    await callback.message.edit_text(
        text=text_save_impulse, reply_markup=markup
    )


@router.callback_query(F.data == 'gey_lussaka')
async def sharlya_handler(callback: CallbackQuery):
    markup = gey_lussaka()
    await callback.message.edit_text(
        text=text_gey_lussaka, reply_markup=markup
    )

@router.callback_query(F.data == 'paskal')
async def sharlya_handler(callback: CallbackQuery):
    markup = paskal()
    await callback.message.edit_text(
        text=text_paskal, reply_markup=markup
    )

class QuestionState(StatesGroup):
    waiting_for_question = State()


@router.callback_query(F.data == "ask_gpt")
async def ask_gpt_handler(callback: CallbackQuery, state:  FSMContext):
    await callback.message.answer(
        "Задайте свой вопрос или опишите задачу по физике. Я постараюсь помочь! 🤓\n"
        "Вы можете задавать вопросы несколько раз подряд."
    )
    await state.set_state(QuestionState.waiting_for_question)

@router.message(QuestionState.waiting_for_question)
async def handle_question(message: Message, state: FSMContext):
    loading_message = await message.answer("⏳ Генерирую ответ...")
    
    try:
        response = await get_gpt_response(message.text)
        
        # Создаем клавиатуру с двумя кнопками
        back_button = InlineKeyboardButton(text="Назад🔙", callback_data="back3")
        ask_again_button = InlineKeyboardButton(text="Задать ещё вопрос 🤔", callback_data="ask_gpt")
        markup = InlineKeyboardMarkup(inline_keyboard=[[back_button, ask_again_button]])
        
        await loading_message.delete()
        await message.answer(response, reply_markup=markup)
        
        # Не очищаем состояние, чтобы можно было продолжать диалог
        await state.set_state(QuestionState.waiting_for_question)
    except Exception as e:
        await loading_message.edit_text(f"Произошла ошибка: {str(e)}")


@router.callback_query(F.data == "about")
async def about_handler(callback: CallbackQuery):
    markup = help_kb()
    await callback.message.answer(
        """Я бот, который помогает освоить непонятную тему по физике, а также сразу закрепить ее. Я могу помочь с вопросами и задачами. 🤓

        Этот бот совершенно бесплатный, но вы можете поддержать разработчика, оплатив небольшую сумму qr-кодом. 💸""",
        reply_markup=markup
    )


@router.callback_query(F.data == "laws")
async def laws_handler(callback: CallbackQuery):
    markup = laws()
    await callback.message.answer(
        text=text_laws, reply_markup=markup
    )


@router.callback_query(F.data == "back3")
async def back_handler(callback: CallbackQuery):
    try:
        markup = main()
        await callback.message.edit_text(
            text=text_handle_info_command,
            reply_markup=markup
        )
    except Exception as e:
        # Если сообщение слишком старое, отправим новое
        await callback.message.answer(
            text=text_handle_info_command,
            reply_markup=markup
        )
    finally:
        # Закрываем состояние ожидания callback
        await callback.answer()


@router.callback_query(F.data == "back4")
async def back_handler(callback: CallbackQuery, state: FSMContext):
        markup = main()
        # Пробуем удалить сообщение
        await callback.message.delete()

        # Очищаем состояние и закрываем callback
        await state.clear()
        await callback.answer()


@router.callback_query(F.data == "help_kb")
async def help_handler(callback: CallbackQuery):
    # Генерируем QR код
    qr_image = generate_payment_qr()
    
    # Создаем кнопку для возврата
    back_button = InlineKeyboardButton(text="Назад🔙", callback_data="back4")
    markup = InlineKeyboardMarkup(inline_keyboard=[[back_button]])
    
    # Конвертируем BytesIO в BufferedInputFile
    photo = BufferedInputFile(
        qr_image.getvalue(),
        filename="payment_qr.png"
    )
    
    # Отправляем фото с QR кодом
    await callback.message.answer_photo(
        photo,
        caption="Спасибо за поддержку! 🙏\nОтсканируйте QR-код для перевода.\n Или вы можете перейти по ссылку(вас перенаправит в банк):\nhttps://www.tbank.ru/rm/r_HDqEjRjbms.hfgFLcoatX/TROVs3203/",
        reply_markup=markup
    )
    
    # Удаляем предыдущее сообщение
    await callback.message.delete()