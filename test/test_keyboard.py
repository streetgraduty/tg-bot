from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def vstroen_test_kb() -> InlineKeyboardMarkup:
    vstroenii = InlineKeyboardButton(
        text="Встроенные тесты📔",
        callback_data="vstroenii"
    )
    online = InlineKeyboardButton(
        text="Онлайн тесты в Интернете🛜",
        callback_data="online"
    )
    back = InlineKeyboardButton(
        text="Назад🔙",
        callback_data="back4"
    )
    rows = [
        [vstroenii, online], [back]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup

def online_kb() -> InlineKeyboardMarkup:
    test5 = InlineKeyboardButton(
        text="Закон преломления света",
        url="https://onlinetestpad.com/ru/test/287236-zakony-otrazheniya-i-prelomleniya-sveta"
    )
    test6 = InlineKeyboardButton(
        text="Закон Паскаля",
        url="https://solncesvet.ru/tests/test-na-temu-zakon-paskalya/"
    )
    test7 = InlineKeyboardButton(
        text="Закон Архимеда",
        url="https://onlinetestpad.com/ru/test/289513-test-po-teme-sila-arkhimeda-7-klass"
    )
    test8 = InlineKeyboardButton(
        text="Закон всемирного тяготения",
        url="https://solncesvet.ru/tests/test-zakon-vsemirnogo-tyagoteniya-9-klass/"
    )
    test9 = InlineKeyboardButton(
        text="Давление газов, жидкостей и твердых тел",
        url="https://onlinetestpad.com/ru/test/4794-test-po-teme-davlenie-gazov-zhidkostej-i-tverdykh-tel"
    )
    test10 = InlineKeyboardButton(
        text="Механическая работа",
        url="https://obrazovaka.ru/test/po-fizike-mehanicheskaya-rabota-7-klass.html"
    )
    test11 = InlineKeyboardButton(
        text="Геометричекая оптика",
        url="https://onlinetestpad.com/ru/test/1270396-geometricheskaya-optika"
    )
    test12 = InlineKeyboardButton(
        text="Магнитное поле",
        url="https://onlinetestpad.com/ru/test/256859-magnitnoe-pole"
    )
    back = InlineKeyboardButton(
        text="Назад🔙",
        callback_data="back_test"
    )
    
    # Исправляем форматирование кнопок
    rows = [
        [test5],
        [test6],
        [test7],
        [test8],
        [test9],
        [test10],
        [test11],
        [test12],
        [back]
    ]
    
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup 

def vstroenii_kb():
    test1 = InlineKeyboardButton(
        text="Законы Ньютона",
        callback_data="nuton_test_kb"
    )
    test2 = InlineKeyboardButton(
        text="Механика",
        callback_data="mechanika_test_kb"
    )
    test3 = InlineKeyboardButton(
        text="Колебания и волны",
        callback_data="Kolebaniya_test_kb"
    )
    test4 = InlineKeyboardButton(
        text="Ома",
        callback_data="Oma_test_kb"
    )
    back = InlineKeyboardButton(
        text="Назад🔙",
        callback_data="back_test"
    )
    rows = [
        [test1], [test2], [test3], [test4], [back]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup


def true_false() -> InlineKeyboardMarkup:
    buttons = [
        InlineKeyboardButton(text=letter, callback_data=str(i+1))
        for i, letter in enumerate(['A', 'B', 'C', 'D'])
    ]
    back = InlineKeyboardButton(text="Выйти из теста", callback_data="back_test")
    markup = InlineKeyboardMarkup(inline_keyboard=[buttons, [back]])
    return markup

def end_test_kb() -> InlineKeyboardMarkup:
    vstroenii = InlineKeyboardButton(
        text="Пройти другой тест📔",
        callback_data="back4"
    )
    main = InlineKeyboardButton(
        text="На главную🔙",
        callback_data="main_kb"
    )
    rows = [
        [vstroenii], [main]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup