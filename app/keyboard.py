from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import qrcode
from io import BytesIO

def main():
    chat_gpt = InlineKeyboardButton(
        text='Спросить ChatGPT 🤓',
        callback_data='ask_gpt'
    )
    laws = InlineKeyboardButton(
        text='Законы👨🏼‍🎓',
        callback_data='laws'
    )
    about = InlineKeyboardButton(
        text='О боте🤖',
        callback_data='about'
    )
    test = InlineKeyboardButton(
        text='Тесты📝',
        callback_data='test'
    )
    rows = [laws, about], [chat_gpt], [test]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup


def laws():
    Nuton = InlineKeyboardButton(
        text='Законы Ньютона',
        callback_data='nuton'
    )
    Termodinamica = InlineKeyboardButton(
        text='Термодинамика',
        callback_data='termodinamica'
    )
    Electro = InlineKeyboardButton(
        text='Электромагнетизм',
        callback_data='electro'
    )
    Optica = InlineKeyboardButton(
        text='Оптика',
        callback_data='optica'
    )
    Otnos = InlineKeyboardButton(
        text='Общая т. относительности',
        callback_data='otnosit'
    )
    Mechanica = InlineKeyboardButton(
        text='Механика',
        callback_data='mechanica'
    )
    Fluctuations = InlineKeyboardButton(
        text='Колебания и волны',
        callback_data='fluctuations'
    )
    Quantum_physics = InlineKeyboardButton(
        text="Квантовая физика",
        callback_data='quantum_physics'
    )
    Sharlya = InlineKeyboardButton(
        text='Закон Шарля',
        callback_data='sharlya'
    )
    Otrajenie = InlineKeyboardButton(
        text='Закон отражения волн',
        callback_data='otrajenie'
    )
    Save_impulse = InlineKeyboardButton(
        text='Закон сохранения импульса',
        callback_data = 'save_impulse'
    )
    Svet = InlineKeyboardButton(
        text='Закон преломления света',
        callback_data='svet'
    )
    Next = InlineKeyboardButton(
        text='Следующая страница⏭️',
        callback_data='next'
    )
    back = InlineKeyboardButton(
        text='Назад🔙',
        callback_data='back4'
    )


    rows = [Nuton, Termodinamica], [Electro, Optica], [Otnos, Mechanica], [Fluctuations, Quantum_physics], [Sharlya, Otrajenie], [Save_impulse, Svet], [back, Next] 
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup

def back():
    back = InlineKeyboardButton(
        text='Назад🔙',
        callback_data='back'
    )
    rows = [back],
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup


def laws_2():
    Arhimeda = InlineKeyboardButton(
        text='Закон Архимеда',
        callback_data='arhimed'
    )
    Ampera = InlineKeyboardButton(
        text='Закон Ампера',
        callback_data='amper'
    )
    Avogadro = InlineKeyboardButton(
        text='Закон Авогадро',
        callback_data='avagadro'
    )
    Boilya_Mariotta = InlineKeyboardButton(
        text='Закон Бойля - Мариотта',
        callback_data='boilya'
    )
    Tyagotenia = InlineKeyboardButton(
        text='Закон всемирного Тяготения',
        callback_data='tyagotenia'
    )
    Guka = InlineKeyboardButton(
        text='Закон Гука',
        callback_data='guka'
    )
    Oma = InlineKeyboardButton(
        text='Закон Ома',
        callback_data='oma'
    )
    Paskal = InlineKeyboardButton(
        text='Закон Паскаля',
        callback_data='paskal'
    )
    back = InlineKeyboardButton(
        text='Предыдущая страница🔙',
        callback_data='back'
    )
    Daltona = InlineKeyboardButton(
        text='Законы Дальтона',
        callback_data='daltona'
    )
    Geya_Lussaka = InlineKeyboardButton(
        text='Закон Гей-Люссака',
        callback_data='gey_lussaka'
    )
    rows = [Arhimeda, Ampera], [Avogadro, Boilya_Mariotta], [Tyagotenia, Guka], [Oma, Paskal], [Daltona, Geya_Lussaka],[back]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup

def back_2():
    back2 = InlineKeyboardButton(
        text='Назад🔙',
        callback_data='back2'
    )
    rows = [back2]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup


def nuton():
    rutube = InlineKeyboardButton(
        text='Видеоурок',
        url='https://rutube.ru/video/d6f9613c63089ea023a692f54c9180e9/'
    )
    back = InlineKeyboardButton(
        text='Назад🔙',
        callback_data='back'
    )
    rows = [rutube], [back]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup


def optica():
    rutube = InlineKeyboardButton(
        text='Видеоурок',
        url='https://rutube.ru/video/4245044af176f6d6ee59b5301d3b16ca/'
    )
    back = InlineKeyboardButton(
        text='Назад🔙',
        callback_data='back'
    )
    rows = [rutube], [back]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup


def otnosit():
    rutube = InlineKeyboardButton(
        text='Видеоурок',
        url='https://rutube.ru/video/2c4d72cf18408700cbd234d7dceb885c/'
    )
    back = InlineKeyboardButton(
        text='Назад🔙',
        callback_data='back'
    )
    rows = [rutube], [back]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup


def termodinamica():
    rutube = InlineKeyboardButton(
        text='Видеоурок',
        url='https://rutube.ru/video/8cee87fec1015f9c82d74eb276e8f7c6/'
    )
    back = InlineKeyboardButton(
        text='Назад🔙',
        callback_data='back'
    )
    rows = [rutube], [back]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup


def electro():
    rutube = InlineKeyboardButton(
        text='Видеоурок',
        url='https://rutube.ru/video/72affb565f5d5a4965cd0992fa9be078/'
    )
    back = InlineKeyboardButton(
        text='Назад🔙',
        callback_data='back'
    )
    rows = [rutube], [back]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup


def mechanica():
    rutube = InlineKeyboardButton(
        text='Видеоурок',
        url='https://rutube.ru/video/92f7dbbc14ae4c434b60f94c3127cdd6/'
    )
    back = InlineKeyboardButton(
        text='Назад🔙',
        callback_data='back'
    )
    rows = [rutube], [back]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup


def quantum():
    rutube = InlineKeyboardButton(
        text='Видеоурок',
        url='https://rutube.ru/video/76184beb89627bbbd0dcaf47f8bfdbc8/'
    )
    back = InlineKeyboardButton(
        text='Назад🔙',
        callback_data='back'
    )
    rows = [rutube], [back]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup


def fluctuations():
    rutube = InlineKeyboardButton(
        text='Видеоурок',
        url='https://rutube.ru/video/728c097b19f0df4b71463c31a9f9603b/'
    )
    back = InlineKeyboardButton(
        text='Назад🔙',
        callback_data='back'
    )
    rows = [rutube], [back]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup


def sharlya():
    rutube = InlineKeyboardButton(
        text='Видеоурок',
        url='https://rutube.ru/video/c1c50a5e408a55317118510360ab8809/'
    )
    back = InlineKeyboardButton(
        text='Назад🔙',
        callback_data='back'
    )
    rows = [rutube], [back]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup


def dalton():
    rutube = InlineKeyboardButton(
        text='Видеоурок',
        url='https://rutube.ru/video/f1769d39ebe63c3102a0aa7a8ad17d23/'
    )
    back = InlineKeyboardButton(
        text='Назад🔙',
        callback_data='back'
    )
    rows = [rutube], [back]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup


def otrajenie():
    rutube = InlineKeyboardButton(
        text='Видеоурок',
        url='https://rutube.ru/video/cd5897ffed3fe038d8f83115ecb58cfb/'
    )
    back = InlineKeyboardButton(
        text='Назад🔙',
        callback_data='back'
    )
    rows = [rutube], [back]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup


def save_impulse():
    rutube = InlineKeyboardButton(
        text='Видеоурок',
        url='https://rutube.ru/video/3014ac88e424f9d742190aac28b2ec98/'
    )
    back = InlineKeyboardButton(
        text='Назад🔙',
        callback_data='back'
    )
    rows = [rutube], [back]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup


def svet():
    rutube = InlineKeyboardButton(
        text='Видеоурок',
        url='https://rutube.ru/video/cd5897ffed3fe038d8f83115ecb58cfb/'
    )
    back = InlineKeyboardButton(
        text='Назад🔙',
        callback_data='back'
    )
    rows = [rutube], [back]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup


def arhimed():
    rutube = InlineKeyboardButton(
        text='Видеоурок',
        url='https://rutube.ru/video/6c7626fbc1133bf7127b8915d098bebb/'
    )
    back = InlineKeyboardButton(
        text='Назад🔙',
        callback_data='back2'
    )
    rows = [rutube], [back]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup


def amper():
    rutube = InlineKeyboardButton(
        text='Видеоурок',
        url='https://rutube.ru/video/b24359edfbeb4cc62d8d2b881d5723ea/'
    )
    back = InlineKeyboardButton(
        text='Назад🔙',
        callback_data='back2'
    )
    rows = [rutube], [back]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup


def avogadro():
    rutube = InlineKeyboardButton(
        text='Видеоурок',
        url='https://rutube.ru/video/f787e8d7940238dcfb6cab73434dbf1c/'
    )
    back = InlineKeyboardButton(
        text='Назад🔙',
        callback_data='back2'
    )
    rows = [rutube], [back]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup


def boilya():
    rutube = InlineKeyboardButton(
        text='Видеоурок',
        url='https://rutube.ru/video/c1c50a5e408a55317118510360ab8809/'
    )
    back = InlineKeyboardButton(
        text='Назад🔙',
        callback_data='back2'
    )
    rows = [rutube], [back]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup


def tyagotenia():
    rutube = InlineKeyboardButton(
        text='Видеоурок',
        url='https://rutube.ru/video/e9482e580b4cc7b5b34cfe558362034f/'
    )
    back = InlineKeyboardButton(
        text='Назад🔙',
        callback_data='back2'
    )
    rows = [rutube], [back]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup


def guka():
    rutube = InlineKeyboardButton(
        text='Видеоурок',
        url='https://rutube.ru/video/3e3daf574d467e06960b74e1c3f7e184/'
    )
    back = InlineKeyboardButton(
        text='Назад🔙',
        callback_data='back2'
    )
    rows = [rutube], [back]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup


def oma():
    rutube = InlineKeyboardButton(
        text='Видеоурок',
        url='https://rutube.ru/video/a9e3ce9cccd4a4e3dab044bd404f4a22/'
    )
    back = InlineKeyboardButton(
        text='Назад🔙',
        callback_data='back2'
    )
    rows = [rutube], [back]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup


def paskal():
    rutube = InlineKeyboardButton(
        text='Видеоурок',
        url='https://rutube.ru/video/5fbf9ac5bd76fd62315def5f33a4c8ed/'
    )
    back = InlineKeyboardButton(
        text='Назад🔙',
        callback_data='back2'
    )
    rows = [rutube], [back]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup


def gey_lussaka():
    rutube = InlineKeyboardButton(
        text='Видеоурок',
        url='https://rutube.ru/video/9cd8c25ea993b2d86f394da609210d44/'
    )
    back = InlineKeyboardButton(
        text='Назад🔙',
        callback_data='back2'
    )
    rows = [rutube], [back]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup


def gpt():
    gpt_kb = InlineKeyboardButton(
        text='Задать вопрос или решить задачу🤖',
        callback_data='gpt_question'
    )
    rows = [gpt_kb]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup


def generate_payment_qr() -> BytesIO:
    """Генерирует QR код для оплаты"""
    # Создаем объект QR кода
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Добавляем данные для оплаты (замените на свои реквизиты)
    payment_data = "https://www.tinkoff.ru/rm/r_HDqEjRjbms.hfgFLcoatX/TROVs3203" # Ваша платежная ссылка
    qr.add_data(payment_data)
    qr.make(fit=True)
    
    # Создаем изображение
    qr_image = qr.make_image(fill_color="black", back_color="white")
    
    # Сохраняем в байтовый объект
    bio = BytesIO()
    qr_image.save(bio, 'PNG')
    bio.seek(0)
    
    return bio


def help_kb() -> InlineKeyboardMarkup:
    # Создаем кнопки
    help_kb = InlineKeyboardButton(
        text="Поддержать разработчика💸",
        callback_data="help_kb"
    )
    back = InlineKeyboardButton(
        text="Назад🔙",
        callback_data="back4"
    )
    rows = [help_kb], [back]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup
