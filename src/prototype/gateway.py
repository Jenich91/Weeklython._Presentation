import telebot
from telebot import types
import lib
import config
import kernel
import random
import authorization
import sys

if len(sys.argv) > 1:
    sys.exit(0)

bot = telebot.TeleBot(config.token)
current_path = lib.Way()
user = lib.User()
code = random.randint(1000000, 9999999)


@bot.message_handler(commands=["start"])
def start_menu(message):
    key = types.InlineKeyboardMarkup()
    but = types.InlineKeyboardButton(text="Авторизация",
                                     callback_data="avtorizacia")
    key.add(but)
    bot.send_message(message.chat.id,
                     "Привет! Я создан, чтобы ты мог забронировать "
                     "что-нибудь полезное в Школе21",
                     reply_markup=key)


@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    global temp
    global start_time
    global end_time
    global day_time
    if c.data == 'avtorizacia':
        bot.send_message(c.message.chat.id,
                         "Напиши мне свой логин на платформе")
        key = types.InlineKeyboardMarkup()
        but = types.InlineKeyboardButton(text="Отправил тебе код доступа, "
                                              "проверяй почту",
                                         callback_data='cod dostypa')
        key.add(but)
        bot.send_message(c.message.chat.id, 'Теперь нажми сюда',
                         reply_markup=key)

    elif c.data == 'cod dostypa' and current_path.status == 1:
        bot.send_message(c.message.chat.id,
                         "Отправил тебе на почту код доступа, "
                         "вводи его сюда и жми на кнопку")
        key = types.InlineKeyboardMarkup()
        but = types.InlineKeyboardButton(text="Я ввел код",
                                         callback_data="main_menu")
        key.add(but)
        bot.send_message(c.message.chat.id, 'После введения кода нажми сюда',
                         reply_markup=key)
        kernel.write_tg_id(user.mail, c.message.from_user.id)

    elif c.data == 'main_menu':
        tmp = kernel.take_user_role(user.mail)
        user.ID_user = kernel.take_user_id(user.mail)
        if tmp == 1:
            user.role = "ab"
        elif tmp == 2:
            user.role = "stu"
        elif tmp == 3:
            user.role = "sta"
        elif tmp == 4:
            user.role = "adm"

        if user.role == "ab":
            key = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(text="Забронировать",
                                               callback_data="bron_ab")
            but_2 = types.InlineKeyboardButton(text="Отменить бронь",
                                               callback_data="pop")
            but_3 = types.InlineKeyboardButton(text="Список бронирования",
                                               callback_data="show_ob")
            key.add(but_1, but_2, but_3)
            bot.send_message(c.message.chat.id, 'Eto glavnoe menu',
                             reply_markup=key)
        elif user.role == "stu":
            key = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(text="Забронировать",
                                               callback_data="bron_stu")
            but_2 = types.InlineKeyboardButton(text="Отменить бронь",
                                               callback_data="pop")
            but_3 = types.InlineKeyboardButton(text="Список бронирования",
                                               callback_data="show_ob")
            key.add(but_1, but_2, but_3)
            bot.send_message(c.message.chat.id, 'Главное меню',
                             reply_markup=key)
        elif user.role == "sta":
            key = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(text="Бронь",
                                               callback_data="bron_sta")
            but_2 = types.InlineKeyboardButton(text="Отменить бронь",
                                               callback_data="pop")
            but_3 = types.InlineKeyboardButton(text="Список бронирования",
                                               callback_data="show_ob")
            key.add(but_1, but_2, but_3)
            bot.send_message(c.message.chat.id, 'Главное меню',
                             reply_markup=key)

    elif c.data == 'bron_ab':
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Новосибирск",
                                           callback_data="Novosibirsk_ab")
        but_2 = types.InlineKeyboardButton(text="Москва",
                                           callback_data="Moscow_ab")
        but_3 = types.InlineKeyboardButton(text="Казань",
                                           callback_data="Kazan_ab")
        but_4 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2, but_3, but_4)
        bot.send_message(c.message.chat.id, 'Выбери кампус',
                         reply_markup=key)
        current_path.staus = 1

    elif c.data == 'bron_stu':
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Новосибирск",
                                           callback_data="Novosibirsk_stu")
        but_2 = types.InlineKeyboardButton(text="Москва",
                                           callback_data="Moscow_stu")
        but_3 = types.InlineKeyboardButton(text="Казань",
                                           callback_data="Kazan_stu")
        but_4 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2, but_3, but_4)
        bot.send_message(c.message.chat.id, 'Выбери кампус',
                         reply_markup=key)
        current_path.staus = 1

    elif c.data == 'bron_sta':
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Новосибирск",
                                           callback_data="Novosibirsk_sta")
        but_2 = types.InlineKeyboardButton(text="Москва",
                                           callback_data="Moscow_sta")
        but_3 = types.InlineKeyboardButton(text="Казань",
                                           callback_data="Kazan_sta")
        but_4 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2, but_3, but_4)
        bot.send_message(c.message.chat.id, 'Выбери в кампус',
                         reply_markup=key)
        current_path.staus = 1

    elif c.data == 'show_ob':
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Новосибирск",
                                           callback_data="Novosibirsk_sta")
        but_2 = types.InlineKeyboardButton(text="Москва",
                                           callback_data="Moscow_sta")
        but_3 = types.InlineKeyboardButton(text="Казань",
                                           callback_data="Kazan_sta")
        but_4 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2, but_3, but_4)
        bot.send_message(c.message.chat.id, 'Выбери в кампус',
                         reply_markup=key)
        current_path.status = 0

    elif c.data == 'Novosibirsk_ab':
        bot.send_message(c.message.chat.id,
                         'Новосибирск - отличный выбор')
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Переговорка",
                                           callback_data="peregovorka")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'Что нужно забронировать?',
                         reply_markup=key)
        current_path.campus = 3

    elif c.data == 'Moscow_ab':
        bot.send_message(c.message.chat.id,
                         'Москва - отличный выбор')
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Переговорка",
                                           callback_data="peregovorka")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'Что нужно забронировать?',
                         reply_markup=key)
        current_path.campus = 1

    elif c.data == 'Kazan_ab':
        bot.send_message(c.message.chat.id,
                         'Казань - отличный выбор')
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Переговорка",
                                           callback_data="peregovorka")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'Что нужно забронировать?',
                         reply_markup=key)
        current_path.campus = 2

    elif c.data == 'Novosibirsk_stu':
        bot.send_message(c.message.chat.id,
                         'Новосибирск - отличный выбор')
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Спорт инвентарь",
                                           callback_data="sport")
        but_2 = types.InlineKeyboardButton(text="Переговорка",
                                           callback_data="peregovorka")
        but_3 = types.InlineKeyboardButton(text="Настольные игры",
                                           callback_data="GAME")
        but_4 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2, but_3, but_4)
        bot.send_message(c.message.chat.id, 'Что нужно забронировать?',
                         reply_markup=key)
        current_path.campus = 3

    elif c.data == 'Moscow_stu':
        bot.send_message(c.message.chat.id,
                         'Москва - отличный выбор')
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Спорт инвентарь",
                                           callback_data="sport")
        but_2 = types.InlineKeyboardButton(text="Переговорка",
                                           callback_data="peregovorka")
        but_3 = types.InlineKeyboardButton(text="Настольные игры",
                                           callback_data="GAME")
        but_4 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2, but_3, but_4)
        bot.send_message(c.message.chat.id, 'Что нужно забронировать?',
                         reply_markup=key)
        current_path.campus = 1

    elif c.data == 'Kazan_stu':
        bot.send_message(c.message.chat.id,
                         'Казань - отличный выбор')
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Спорт инвентарь",
                                           callback_data="sport")
        but_2 = types.InlineKeyboardButton(text="Переговорка",
                                           callback_data="peregovorka")
        but_3 = types.InlineKeyboardButton(text="Настольные игры",
                                           callback_data="GAME")
        but_4 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2, but_3, but_4)
        bot.send_message(c.message.chat.id, 'Что нужно забронировать?',
                         reply_markup=key)
        current_path.campus = 2

    elif c.data == 'Novosibirsk_sta':
        bot.send_message(c.message.chat.id,
                         'Новосибирск - отличный выбор')
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Кухня",
                                           callback_data="kitchen")
        but_2 = types.InlineKeyboardButton(text="Спорт инвентарь",
                                           callback_data="sport")
        but_3 = types.InlineKeyboardButton(text="Переговорка",
                                           callback_data="peregovorka")
        but_4 = types.InlineKeyboardButton(text="Настольные игры",
                                           callback_data="GAME")
        but_5 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2, but_3, but_4, but_5)
        bot.send_message(c.message.chat.id, 'Что нужно забронировать?',
                         reply_markup=key)
        current_path.campus = 3

    elif c.data == 'Moscow_sta':
        bot.send_message(c.message.chat.id,
                         'Москва - отличный выбор')
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Кухня",
                                           callback_data="kitchen")
        but_2 = types.InlineKeyboardButton(text="Спорт инвентарь",
                                           callback_data="sport")
        but_3 = types.InlineKeyboardButton(text="Переговорка",
                                           callback_data="peregovorka")
        but_4 = types.InlineKeyboardButton(text="Настольные игры",
                                           callback_data="GAME")
        but_5 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2, but_3, but_4, but_5)
        bot.send_message(c.message.chat.id, 'Что нужно забронировать?',
                         reply_markup=key)
        current_path.campus = 1

    elif c.data == 'Kazan_sta':
        bot.send_message(c.message.chat.id,
                         'Казань - отличный выбор')
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Кухня",
                                           callback_data="kitchen")
        but_2 = types.InlineKeyboardButton(text="Спорт инвентарь",
                                           callback_data="sport")
        but_3 = types.InlineKeyboardButton(text="Переговорка",
                                           callback_data="peregovorka")
        but_4 = types.InlineKeyboardButton(text="Настольные игры",
                                           callback_data="GAME")
        but_5 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2, but_3, but_4, but_5)
        bot.send_message(c.message.chat.id, 'Что нужно забронировать?',
                         reply_markup=key)
        current_path.campus = 2

    elif c.data == 'kitchen':
        bot.send_message(c.message.chat.id,
                         'Хмм.. Кухню могут бронировать только сотрудники')
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Перейти к выбору",
                                           callback_data="vibor")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'knopka dla vozrashenia v menu',
                         reply_markup=key)
        current_path.type = 4
        temp = kernel.take_objects_list(current_path)

    elif c.data == 'sport':
        bot.send_message(c.message.chat.id, 'Прекрасный выбор')
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Перейти к выбору",
                                           callback_data="vibor")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'knopka dla vozrashenia v menu',
                         reply_markup=key)
        current_path.type = 2
        temp = kernel.take_objects_list(current_path)

    elif c.data == 'peregovorka':
        bot.send_message(c.message.chat.id, 'Ooo, секретики?')
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Перейти к выбору",
                                           callback_data="vibor")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'knopka dla vozrashenia v menu',
                         reply_markup=key)
        current_path.type = 1
        temp = kernel.take_objects_list(current_path)

    elif c.data == 'GAME':
        bot.send_message(c.message.chat.id, 'Обожаю играть!')
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Перейти к выбору",
                                           callback_data="vibor")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'knopka dla vozrashenia v menu',
                         reply_markup=key)
        current_path.type = 3
        temp = kernel.take_objects_list(current_path)

    elif c.data == 'vibor':
        i = 0
        for tmp in temp:
            key = types.InlineKeyboardMarkup()
            but = types.InlineKeyboardButton(text=str(i+1),
                                             callback_data=str(i))
            key.add(but)
            bot.send_message(c.message.chat.id,
                             str(temp[i][2]) + ' ' +
                             str(temp[i][3]) + ' ' +
                             str(temp[i][6]) + ' etag',
                             reply_markup=key)
            i += 1

    elif c.data == '0':
        temp = temp[0]
        if current_path.status == 0:
            key = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(text="Выбери obekt",
                                               callback_data="show")
            but_2 = types.InlineKeyboardButton(text="Вернуться назад",
                                               callback_data="main_menu")
            key.add(but_1, but_2)
            bot.send_message(c.message.chat.id, 'Меню', reply_markup=key)
        else:
            key = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(text="Выбери день",
                                               callback_data="day")
            but_2 = types.InlineKeyboardButton(text="Вернуться назад",
                                               callback_data="main_menu")
            key.add(but_1, but_2)
            bot.send_message(c.message.chat.id, 'Меню', reply_markup=key)

    elif c.data == '1':
        temp = temp[1]
        if current_path.staus == 0:
            key = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(text="Выбери obekt",
                                               callback_data="show")
            but_2 = types.InlineKeyboardButton(text="Вернуться назад",
                                               callback_data="main_menu")
            key.add(but_1, but_2)
            bot.send_message(c.message.chat.id, 'Меню', reply_markup=key)
        else:
            key = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(text="Выбери день",
                                               callback_data="day")
            but_2 = types.InlineKeyboardButton(text="Вернуться назад",
                                               callback_data="main_menu")
            key.add(but_1, but_2)
            bot.send_message(c.message.chat.id, 'Меню', reply_markup=key)

    elif c.data == '2':
        temp = temp[2]
        if current_path.staus == 0:
            key = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(text="Выбери obekt",
                                               callback_data="show")
            but_2 = types.InlineKeyboardButton(text="Вернуться назад",
                                               callback_data="main_menu")
            key.add(but_1, but_2)
            bot.send_message(c.message.chat.id, 'Меню', reply_markup=key)
        else:
            key = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(text="Выбери день",
                                               callback_data="day")
            but_2 = types.InlineKeyboardButton(text="Вернуться назад",
                                               callback_data="main_menu")
            key.add(but_1, but_2)
            bot.send_message(c.message.chat.id, 'Меню', reply_markup=key)

    elif c.data == '3':
        temp = temp[3]
        if current_path.staus == 0:
            key = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(text="Выбери obekt",
                                               callback_data="show")
            but_2 = types.InlineKeyboardButton(text="Вернуться назад",
                                               callback_data="main_menu")
            key.add(but_1, but_2)
            bot.send_message(c.message.chat.id, 'Меню', reply_markup=key)
        else:
            key = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(text="Выбери день",
                                               callback_data="day")
            but_2 = types.InlineKeyboardButton(text="Вернуться назад",
                                               callback_data="main_menu")
            key.add(but_1, but_2)
            bot.send_message(c.message.chat.id, 'Меню', reply_markup=key)

    elif c.data == '4':
        temp = temp[4]
        if current_path.staus == 0:
            key = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(text="Выбери obekt",
                                               callback_data="show")
            but_2 = types.InlineKeyboardButton(text="Вернуться назад",
                                               callback_data="main_menu")
            key.add(but_1, but_2)
            bot.send_message(c.message.chat.id, 'Меню', reply_markup=key)
        else:
            key = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(text="Выбери день",
                                               callback_data="day")
            but_2 = types.InlineKeyboardButton(text="Вернуться назад",
                                               callback_data="main_menu")
            key.add(but_1, but_2)
            bot.send_message(c.message.chat.id, 'Меню',
                             reply_markup=key)

    elif c.data == 'day':
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text=str(kernel.get_day(0)),
                                           callback_data="day_1")
        but_2 = types.InlineKeyboardButton(text=str(kernel.get_day(1)),
                                           callback_data="day_2")
        but_3 = types.InlineKeyboardButton(text=str(kernel.get_day(2)),
                                           callback_data="day_3")
        but_4 = types.InlineKeyboardButton(text=str(kernel.get_day(3)),
                                           callback_data="day_4")
        but_5 = types.InlineKeyboardButton(text=str(kernel.get_day(4)),
                                           callback_data="day_5")
        but_6 = types.InlineKeyboardButton(text=str(kernel.get_day(5)),
                                           callback_data="day_6")
        but_7 = types.InlineKeyboardButton(text=str(kernel.get_day(6)),
                                           callback_data="day_7")
        but_8 = types.InlineKeyboardButton(text="Вернуться назад",
                                           callback_data="main_menu")
        key.add(but_1, but_2, but_3, but_4,
                but_5, but_6, but_7, but_8)
        bot.send_message(c.message.chat.id, 'Какой день?',
                         reply_markup=key)

    elif c.data == 'day_1':
        day_time = kernel.get_day(0)
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Выбор времени",
                                           callback_data="vibor_time_start")
        but_2 = types.InlineKeyboardButton(text="Вернуться назад",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'Перейдем к выбору времени',
                         reply_markup=key)

    elif c.data == 'day_2':
        day_time = kernel.get_day(1)
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Выбор времени",
                                           callback_data="vibor_time_start")
        but_2 = types.InlineKeyboardButton(text="Вернуться назад",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'pereidem k vibory vremeni?',
                         reply_markup=key)

    elif c.data == 'day_3':
        day_time = kernel.get_day(2)
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Выбор времени",
                                           callback_data="vibor_time_start")
        but_2 = types.InlineKeyboardButton(text="Вернуться назад",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'Перейдем к выбору времени',
                         reply_markup=key)

    elif c.data == 'day_4':
        day_time = kernel.get_day(3)
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Выбор времени",
                                           callback_data="vibor_time_start")
        but_2 = types.InlineKeyboardButton(text="Вернуться назад",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'Перейдем к выбору времени',
                         reply_markup=key)

    elif c.data == 'day_5':
        day_time = kernel.get_day(4)
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Выбор времени",
                                           callback_data="vibor_time_start")
        but_2 = types.InlineKeyboardButton(text="Вернуться назад",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'Перейдем к выбору времени',
                         reply_markup=key)

    elif c.data == 'day_6':
        day_time = kernel.get_day(5)
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Выбор времени",
                                           callback_data="vibor_time_start")
        but_2 = types.InlineKeyboardButton(text="Вернуться назад",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'Перейдем к выбору времени',
                         reply_markup=key)

    elif c.data == 'day_7':
        day_time = kernel.get_day(6)
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Выбор времени",
                                           callback_data="vibor_time_start")
        but_2 = types.InlineKeyboardButton(text="Вернуться назад",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id,
                         'Перейдем к выбору времени', reply_markup=key)

    elif c.data == 'vibor_time_start':
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="0:00",
                                           callback_data="time_0_start")
        but_2 = types.InlineKeyboardButton(text="1:00",
                                           callback_data="time_1_start")
        but_3 = types.InlineKeyboardButton(text="2:00",
                                           callback_data="time_2_start")
        but_4 = types.InlineKeyboardButton(text="3:00",
                                           callback_data="time_3_start")
        but_5 = types.InlineKeyboardButton(text="4:00",
                                           callback_data="time_4_start")
        but_6 = types.InlineKeyboardButton(text="5:00",
                                           callback_data="time_5_start")
        but_7 = types.InlineKeyboardButton(text="6:00",
                                           callback_data="time_6_start")
        but_8 = types.InlineKeyboardButton(text="7:00",
                                           callback_data="time_7_start")
        but_9 = types.InlineKeyboardButton(text="8:00",
                                           callback_data="time_8_start")
        but_10 = types.InlineKeyboardButton(text="9:00",
                                            callback_data="time_9_start")
        but_11 = types.InlineKeyboardButton(text="10:00",
                                            callback_data="time_10_start")
        but_12 = types.InlineKeyboardButton(text="11:00",
                                            callback_data="time_11_start")
        but_13 = types.InlineKeyboardButton(text="12:00",
                                            callback_data="time_12_start")
        but_14 = types.InlineKeyboardButton(text="13:00",
                                            callback_data="time_13_start")
        but_15 = types.InlineKeyboardButton(text="14:00",
                                            callback_data="time_14_start")
        but_16 = types.InlineKeyboardButton(text="15:00",
                                            callback_data="time_15_start")
        but_17 = types.InlineKeyboardButton(text="16:00",
                                            callback_data="time_16_start")
        but_18 = types.InlineKeyboardButton(text="17:00",
                                            callback_data="time_17_start")
        but_19 = types.InlineKeyboardButton(text="18:00",
                                            callback_data="time_18_start")
        but_20 = types.InlineKeyboardButton(text="19:00",
                                            callback_data="time_19_start")
        but_21 = types.InlineKeyboardButton(text="20:00",
                                            callback_data="time_20_start")
        but_22 = types.InlineKeyboardButton(text="21:00",
                                            callback_data="time_21_start")
        but_23 = types.InlineKeyboardButton(text="22:00",
                                            callback_data="time_22_start")
        but_24 = types.InlineKeyboardButton(text="23:00",
                                            callback_data="time_23_start")
        key.add(but_1, but_2, but_3, but_4, but_5, but_6,
                but_7, but_8, but_9, but_10, but_11,
                but_12, but_13, but_14, but_15, but_16,
                but_17, but_18, but_19, but_20,
                but_21, but_22, but_23, but_24)
        bot.send_message(c.message.chat.id, "Укажи время начала брони",
                         reply_markup=key)

    elif c.data == 'vibor_time_end':
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="1:00",
                                           callback_data="time_1_end")
        but_2 = types.InlineKeyboardButton(text="2:00",
                                           callback_data="time_2_end")
        but_3 = types.InlineKeyboardButton(text="3:00",
                                           callback_data="time_3_end")
        but_4 = types.InlineKeyboardButton(text="4:00",
                                           callback_data="time_4_end")
        but_5 = types.InlineKeyboardButton(text="5:00",
                                           callback_data="time_5_end")
        but_6 = types.InlineKeyboardButton(text="6:00",
                                           callback_data="time_6_end")
        but_7 = types.InlineKeyboardButton(text="7:00",
                                           callback_data="time_7_end")
        but_8 = types.InlineKeyboardButton(text="8:00",
                                           callback_data="time_8_end")
        but_9 = types.InlineKeyboardButton(text="9:00",
                                           callback_data="time_9_end")
        but_10 = types.InlineKeyboardButton(text="10:00",
                                            callback_data="time_10_end")
        but_11 = types.InlineKeyboardButton(text="11:00",
                                            callback_data="time_11_end")
        but_12 = types.InlineKeyboardButton(text="12:00",
                                            callback_data="time_12_end")
        but_13 = types.InlineKeyboardButton(text="13:00",
                                            callback_data="time_13_end")
        but_14 = types.InlineKeyboardButton(text="14:00",
                                            callback_data="time_14_end")
        but_15 = types.InlineKeyboardButton(text="15:00",
                                            callback_data="time_15_end")
        but_16 = types.InlineKeyboardButton(text="16:00",
                                            callback_data="time_16_end")
        but_17 = types.InlineKeyboardButton(text="17:00",
                                            callback_data="time_17_end")
        but_18 = types.InlineKeyboardButton(text="18:00",
                                            callback_data="time_18_end")
        but_19 = types.InlineKeyboardButton(text="19:00",
                                            callback_data="time_19_end")
        but_20 = types.InlineKeyboardButton(text="20:00",
                                            callback_data="time_20_end")
        but_21 = types.InlineKeyboardButton(text="21:00",
                                            callback_data="time_21_end")
        but_22 = types.InlineKeyboardButton(text="22:00",
                                            callback_data="time_22_end")
        but_23 = types.InlineKeyboardButton(text="23:00",
                                            callback_data="time_23_end")
        but_24 = types.InlineKeyboardButton(text="00:00",
                                            callback_data="time_0_end")
        key.add(but_1, but_2, but_3, but_4,
                but_5, but_6, but_7, but_8, but_9, but_10, but_11,
                but_12, but_13, but_14, but_15, but_16, but_17,
                but_18, but_19, but_20, but_21, but_22, but_23, but_24)
        bot.send_message(c.message.chat.id, "Укажи время завершения брони",
                         reply_markup=key)

    elif c.data == "time_0_start":
        start_time = "0:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Выбрать время завершения",
                                           callback_data="vibor_time_end")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_1_start":
        start_time = "0:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Выбрать время завершения",
                                           callback_data="vibor_time_end")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_2_start":
        start_time = "2:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Выбрать время завершения",
                                           callback_data="vibor_time_end")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_3_start":
        start_time = "3:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Выбрать время завершения",
                                           callback_data="vibor_time_end")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_4_start":
        start_time = "4:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Выбрать время завершения ",
                                           callback_data="vibor_time_end")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_5_start":
        start_time = "5:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Выбрать время завершения",
                                           callback_data="vibor_time_end")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_6_start":
        start_time = "6:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Выбрать время завершения",
                                           callback_data="vibor_time_end")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_7_start":
        start_time = "7:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Выбрать время завершения",
                                           callback_data="vibor_time_end")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_8_start":
        start_time = "8:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Выбрать время завершения",
                                           callback_data="vibor_time_end")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_9_start":
        start_time = "9:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Выбрать время завершения",
                                           callback_data="vibor_time_end")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_10_start":
        start_time = "10:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Выбрать время завершения",
                                           callback_data="vibor_time_end")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_11_start":
        start_time = "11:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Выбрать время завершения",
                                           callback_data="vibor_time_end")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_12_start":
        start_time = "12:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Выбрать время завершения",
                                           callback_data="vibor_time_end")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_13_start":
        start_time = "13:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Выбрать время завершения",
                                           callback_data="vibor_time_end")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_14_start":
        start_time = "14:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Выбрать время завершения",
                                           callback_data="vibor_time_end")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_15_start":
        start_time = "15:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Выбрать время завершения",
                                           callback_data="vibor_time_end")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_16_start":
        start_time = "16:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Выбрать время завершения",
                                           callback_data="vibor_time_end")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_17_start":
        start_time = "17:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Выбрать время завершения",
                                           callback_data="vibor_time_end")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_18_start":
        start_time = "18:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Выбрать время завершения",
                                           callback_data="vibor_time_end")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_19_start":
        start_time = "19:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Выбрать время завершения",
                                           callback_data="vibor_time_end")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_20_start":
        start_time = "20:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Выбрать время завершения",
                                           callback_data="vibor_time_end")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_21_start":
        start_time = "21:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Выбрать время завершения",
                                           callback_data="vibor_time_end")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_22_start":
        start_time = "22:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Выбрать время завершения",
                                           callback_data="vibor_time_end")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_23_start":
        start_time = "23:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Выбрать время завершения",
                                           callback_data="vibor_time_end")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_0_end":
        end_time = "0:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Все верно",
                                           callback_data="confirmation")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_1_end":
        end_time = "1:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Все верно",
                                           callback_data="confirmation")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_2_end":
        end_time = "2:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Все верно",
                                           callback_data="confirmation")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_3_end":
        end_time = "3:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Все верно",
                                           callback_data="confirmation")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_4_end":
        end_time = "4:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Все верно",
                                           callback_data="confirmation")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_5_end":
        end_time = "5:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Все верно",
                                           callback_data="confirmation")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_6_end":
        end_time = "6:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Все верно",
                                           callback_data="confirmation")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_7_end":
        end_time = "7:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Все верно",
                                           callback_data="confirmation")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_8_end":
        end_time = "8:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Все верно",
                                           callback_data="confirmation")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_9_end":
        end_time = "9:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Все верно",
                                           callback_data="confirmation")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_10_end":
        end_time = "10:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Все верно",
                                           callback_data="confirmation")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_11_end":
        end_time = "11:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Все верно",
                                           callback_data="confirmation")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_12_end":
        end_time = "12:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Все верно",
                                           callback_data="confirmation")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_13_end":
        end_time = "13:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Все верно",
                                           callback_data="confirmation")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_14_end":
        end_time = "14:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Все верно",
                                           callback_data="confirmation")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_15_end":
        end_time = "15:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Все верно",
                                           callback_data="confirmation")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_16_end":
        end_time = "16:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Все верно",
                                           callback_data="confirmation")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_17_end":
        end_time = "17:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Все верно",
                                           callback_data="confirmation")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_18_end":
        end_time = "18:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Все верно",
                                           callback_data="confirmation")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_19_end":
        end_time = "19:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Все верно",
                                           callback_data="confirmation")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_20_end":
        end_time = "20:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Все верно",
                                           callback_data="confirmation")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_21_end":
        end_time = "21:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Все верно",
                                           callback_data="confirmation")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_22_end":
        end_time = "22:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Все верно",
                                           callback_data="confirmation")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "time_23_end":
        end_time = "23:00"
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="Все верно",
                                           callback_data="confirmation")
        but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                           callback_data="main_menu")
        key.add(but_1, but_2)
        bot.send_message(c.message.chat.id, 'kogda zakonshitsa?',
                         reply_markup=key)

    elif c.data == "confirmation":
        if temp[1] == 1:
            campus = "Moscow"
        elif temp[1] == 2:
            campus = "Kazan"
        else:
            campus = "NSK"
        if current_path.staus == 0:
            key = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(text="Все верно",
                                               callback_data="show")
            but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                               callback_data="main_menu")
            key.add(but_1, but_2)
            bot.send_message(c.message.chat.id, (str(day_time) +
                                                 'chisla  s ' +
                                                 str(start_time) + ' do ' +
                                                 str(end_time) + '/n' +
                                                 'V ' + campus + ' na ' +
                                                 str(temp[6]) + ' etasge '
                                                 + str(temp[4]) + '?'),
                             reply_markup=key)

        elif current_path.staus == 1:
            key = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(text="Все верно",
                                               callback_data="add")
            but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                               callback_data="main_menu")
            key.add(but_1, but_2)
            bot.send_message(c.message.chat.id, (str(day_time) + 'chisla  s ' +
                                                 str(start_time) + ' do ' +
                                                 str(end_time) + '/n' + 'V ' +
                                                 campus + ' na ' +
                                                 str(temp[6]) +
                                                 ' etasge ' +
                                                 str(temp[4]) + '?'),
                             reply_markup=key)

        elif current_path.staus == -1:
            key = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(text="Все верно",
                                               callback_data="pop")
            but_2 = types.InlineKeyboardButton(text="Вернуться в меню",
                                               callback_data="main_menu")
            key.add(but_1, but_2)
            bot.send_message(c.message.chat.id, (str(day_time) + 'chisla  s ' +
                                                 str(start_time) + ' do ' +
                                                 str(end_time) + '/n' + 'V ' +
                                                 campus + ' na ' +
                                                 str(temp[6]) + ' etasge ' +
                                                 str(temp[4]) + '?'),
                             reply_markup=key)

    elif c.data == "show":
        print(temp)
        temp_str = kernel.get_objekt_book(temp[0])
        for i in range(len(temp_str)):
            bot.send_message(c.message.chat.id,
                             temp_str[i][3] + '  -  ' + temp_str[i][4])
        key = types.InlineKeyboardMarkup()
        but = types.InlineKeyboardButton(text="Вернуться в меню",
                                         callback_data="main_menu")
        key.add(but)
        bot.send_message(c.message.chat.id,
                         "Вернуться в меню?", reply_markup=key)

    elif c.data == "pop":
        temp_1 = kernel.get_booking(user)
        print(temp_1)
        print(len(temp_1))
        for i in range(len(temp_1)):
            temp_2 = kernel.get_objekt(temp_1[i][2])
            print(temp_2)
            key = types.InlineKeyboardMarkup()
            but = types.InlineKeyboardButton(text=str(i+1),
                                             callback_data=str(i)+'_book')
            key.add(but)
            bot.send_message(c.message.chat.id, str(temp_2[0][3])
                             + ' ' + str(temp_2[0][4]) + ' ' +
                             str(temp_1[i][3]) + ' ' + str(temp_1[i][4]),
                             reply_markup=key)

    elif c.data == "0_book":
        kernel.pop_booking(kernel.get_booking(user)[0])
        key = types.InlineKeyboardMarkup()
        but = types.InlineKeyboardButton(text="Вернуться в меню",
                                         callback_data="main_menu")
        key.add(but)
        bot.send_message(c.message.chat.id, "Отмена брони", reply_markup=key)

    elif c.data == "1_book":
        kernel.pop_booking(kernel.get_booking(user)[1])
        key = types.InlineKeyboardMarkup()
        but = types.InlineKeyboardButton(text="Вернуться в меню",
                                         callback_data="main_menu")
        key.add(but)
        bot.send_message(c.message.chat.id, "Отмена брони", reply_markup=key)

    elif c.data == "2_book":
        kernel.pop_booking(kernel.get_booking(user)[2])
        key = types.InlineKeyboardMarkup()
        but = types.InlineKeyboardButton(text="Вернуться в меню",
                                         callback_data="main_menu")
        key.add(but)
        bot.send_message(c.message.chat.id, "Отмена брони", reply_markup=key)

    elif c.data == "3_book":
        kernel.pop_booking(kernel.get_booking(user)[3])
        key = types.InlineKeyboardMarkup()
        but = types.InlineKeyboardButton(text="Вернуться в меню",
                                         callback_data="main_menu")
        key.add(but)
        bot.send_message(c.message.chat.id, "Отмена брони", reply_markup=key)

    elif c.data == "4_book":
        kernel.pop_booking(kernel.get_booking(user)[4])
        key = types.InlineKeyboardMarkup()
        but = types.InlineKeyboardButton(text="Вернуться в меню",
                                         callback_data="main_menu")
        key.add(but)
        bot.send_message(c.message.chat.id, "Отмена брони", reply_markup=key)

    elif c.data == "5_book":
        kernel.pop_booking(kernel.get_booking(user)[5])
        key = types.InlineKeyboardMarkup()
        but = types.InlineKeyboardButton(text="Вернуться в меню",
                                         callback_data="main_menu")
        key.add(but)
        bot.send_message(c.message.chat.id, "Отмена брони", reply_markup=key)

    elif c.data == "add":
        end_time = str(day_time) + ' ' + end_time
        start_time = str(day_time) + ' ' + start_time
        kernel.add_booking(temp, user, start_time, end_time)
        key = types.InlineKeyboardMarkup()
        but = types.InlineKeyboardButton(text="Вернуться в меню",
                                         callback_data="main_menu")
        key.add(but)
        bot.send_message(c.message.chat.id, "Бронь создана", reply_markup=key)

    else:
        bot.send_message(c.message.chat.id, "Повторите ввод почты")
        key = types.InlineKeyboardMarkup()
        but = types.InlineKeyboardButton(text="Логин введен",
                                         callback_data='avtorizacia')
        key.add(but)
        bot.send_message(c.message.chat.id,
                         'После введения логина, нажми сюда', reply_markup=key)


def check_text(tmp, code):
    status = False
    if "@21-school.ru" in tmp or "@student.21-school.ru" in tmp:
        user.mail = tmp
        authorization.send_email(tmp, code)
    elif tmp == str(code):
        status = True
    return status


@bot.message_handler(content_types=['text'])
def error(message):
    if check_text(message.text, code):
        current_path.status = 1

    if user.role == "adm":
        kernel.check_text_adm(message.text)


if __name__ == '__main__':
    bot.infinity_polling()
