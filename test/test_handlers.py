from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from app.keyboard import main
from .test_keyboard import vstroenii_kb, vstroen_test_kb, online_kb, true_false, end_test_kb
from text import text_all_online_and_vstroenii, text_vstroenii, text_online, text_handle_info_command
from .test_questions import TESTS
import logging

router = Router()

class TestState(StatesGroup):
    answering = State()

@router.callback_query(F.data == "test")
async def test_handlers(callback: CallbackQuery):
    logging.info(f"Получен callback: {callback.data}")
    try:
        markup = vstroen_test_kb()
        await callback.message.answer(
            text=text_all_online_and_vstroenii, 
            reply_markup=markup
        )
    except Exception as e:
        logging.error(f"Ошибка при обработке теста: {e}")
        await callback.message.answer(
            text=text_all_online_and_vstroenii, 
            reply_markup=markup
        )
    finally:
        await callback.answer()

@router.callback_query(F.data == "vstroenii")
async def vstroenii_handler(callback: CallbackQuery):
    markup = vstroenii_kb()
    await callback.message.edit_text(
        text=text_vstroenii, 
        reply_markup=markup
    )

@router.callback_query(F.data == "online")
async def online_handler(callback: CallbackQuery):
    markup = online_kb()
    await callback.message.edit_text(
        text=text_online,
        reply_markup=markup
    )

@router.callback_query(F.data == "back_test")
async def back_test_handler(callback: CallbackQuery):
    markup = vstroen_test_kb()
    await callback.message.edit_text(
        text=text_all_online_and_vstroenii,
        reply_markup=markup
    )

@router.callback_query(lambda c: c.data in TESTS.keys())
async def start_test(callback: CallbackQuery, state: FSMContext):
    test_id = callback.data
    test_data = TESTS[test_id]
    
    # Сохраняем данные теста в состоянии
    await state.update_data(
        test_id=test_id,
        current_question=0,
        correct_answers=0,
        total_questions=len(test_data["questions"])
    )
    
    # Показываем первый вопрос
    await show_question(callback.message, state)
    await state.set_state(TestState.answering)

async def show_question(message, state: FSMContext):
    data = await state.get_data()
    test_id = data['test_id']
    current_q = data['current_question']
    test_data = TESTS[test_id]
    question = test_data["questions"][current_q]
    
    # Формируем текст вопроса
    question_text = f"{test_data['title']}\n\n"
    question_text += f"Вопрос {current_q + 1} из {data['total_questions']}\n\n"
    question_text += f"{question['question']}\n\n"
    
    for i, option in enumerate(question['options']):
        question_text += f"{chr(65+i)}) {option}\n"
    
    markup = true_false()
    await message.edit_text(text=question_text, reply_markup=markup)

@router.callback_query(TestState.answering, lambda c: c.data in ["1", "2", "3", "4"])
async def handle_answer(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    test_id = data['test_id']
    current_q = data['current_question']
    
    # Проверяем правильность ответа
    selected_answer = int(callback.data) - 1
    correct_answer = TESTS[test_id]["questions"][current_q]["correct"]
    
    if selected_answer == correct_answer:
        data['correct_answers'] += 1
    
    data['current_question'] += 1
    await state.update_data(**data)
    
    # Если есть ещё вопросы, показываем следующий
    if data['current_question'] < data['total_questions']:
        await show_question(callback.message, state)
    else:
        result_text = f"Тест завершён!\n\n"
        result_text += f"Правильных ответов: {data['correct_answers']} из {data['total_questions']}\n"
        result_text += f"Процент правильных ответов: {(data['correct_answers']/data['total_questions'])*100:.1f}%"
        
        markup = end_test_kb()
        await callback.message.edit_text(text=result_text, reply_markup=markup)
        await state.clear()

@router.callback_query(F.data == "main_kb")
async def main_kb(callback: CallbackQuery):
    markup = main()
    await callback.message.answer(text=text_handle_info_command, reply_markup=markup)
