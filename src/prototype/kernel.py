from dal import BotDataBase
import lib
import datetime

bdb = BotDataBase("base.db")

new_user = lib.User()
new_object = lib.Object


def show_object(cur_object):
    return bdb.get_object_all(cur_object[1], cur_object[2])


def check_free_time(object_id, dt_begin, dt_end):
    status = True
    arr_begin = bdb.get_status_object_begin(object_id)
    arr_end = bdb.get_status_object_end(object_id)
    if len(arr_begin):
        for i in range(len(arr_begin)):
            if (str(dt_end) > str(arr_begin[i])
                and str(dt_end) <= str(arr_end[i])) \
                    or (str(dt_begin) >= str(arr_begin[i])
                        and str(dt_begin) < str(arr_end[i])) \
                    or (str(dt_end) <= str(arr_end[i])
                        and str(dt_begin) >= str(arr_begin[i])):
                status = False
    else:
        status = True
    return status


def add_booking(cur_object, cur_user, dt_begin, dt_end):
    print(f'ADD_BOOKING INP - {cur_object} {cur_user} {dt_begin} {dt_end}')
    res = (0, 'Error')
    if check_free_time(cur_object[0], dt_begin, dt_end):
        if not bdb.book_object(cur_user.ID_user,
                               cur_object[1], dt_begin, dt_end):
            res = (1, 'Success')
    print(f'ADD_BOOKING RES - {res}')
    return res


def pop_booking(cur_booking):
    print(f'POP_BOOKING INP - {cur_booking}')
    res = (0, 'Error')
    print(cur_booking[0])
    if not bdb.cancel_booking(cur_booking[0]):
        res = (1, 'Success')
    print(f'POP_BOOKING RES - {res}')
    return res


def show_user_bookings(cur_user):
    print(f'SHOW_USER_BOOKINGS INP - {cur_user}')
    res = (0, 'Error')
    if bdb.get_user_booking(cur_user.ID_user):
        res = (1, 'Success')
    print(f'SHOW_USER_BOOKINGS RES - {res}')
    return res


def take_objects_list(cur_object):
    print(f'TAKE_OBJECTS_LIST INP - {cur_object}')
    res = bdb.get_object_all(cur_object.campus, cur_object.type)
    if not res[0]:
        res = (0, 'Invalid data')  # 0 - error
    print(f'TAKE_OBJECTS_LIST RES - {res}')
    return res


def add_user(cur_user):
    print(f'ADD_USER INP - {cur_user}')
    res = (0, 'Error')
    if not bdb.user_exists(cur_user.mail):
        if bdb.add_user(cur_user.mail, cur_user.role, cur_user.campus):
            res = (1, 'Success')
    print(f'ADD_USER RES - {res}')
    return res


def add_object(cur_object):
    print(f'ADD_OBJECT INP - {cur_object}')
    res = (0, 'Error')
    if not bdb.object_exist(cur_object.campus, cur_object.type):
        if bdb.add_object(cur_object.type, cur_object.name, cur_object.note,
                          cur_object.campus, cur_object.floor,
                          cur_object.room_name):
            res = (1, 'Success')
    print(f'ADD_OBJECT RES - {res}')
    return res


def del_user(cur_user):
    print(f'DEL_USER INP - {cur_user}')
    res = (0, 'Error')
    if bdb.user_exists(cur_user.ID_user):
        if bdb.pop_user(cur_user.email):
            res = (1, 'Success')
    print(f'DEL_USER RES - {res}')
    return res


def del_object(cur_object):
    print(f'DEL_OBJECT INP - {cur_object}')
    res = (0, 'Error')
    if bdb.object_exist(cur_object.campus, cur_object.type):
        if bdb.pop_object(cur_object.ID_object):
            res = (1, 'Success')
    print(f'DEL_OBJECT RES - {res}')
    return res


def validate_date(date):
    res = 1
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d %H')
    except ValueError:
        res = 0
    return res


def verify_auth_code(code_orig, code_input):
    res = (1, 'Success')
    if code_orig != code_input:
        res = (0, 'Auth code incorrect')
    return res


def get_day(n):
    first_date = datetime.date.today()
    for i in range(n):
        first_date = first_date + datetime.timedelta(days=1)
    return first_date


def take_user_role(email):
    return bdb.get_mail_return_role(email)


def take_user_id(email):
    return bdb.get_mail_return_user_id(email)


def write_tg_id(email, ID_tg_user):
    bdb.put_id_and_return_role(email, ID_tg_user)


def get_booking(user):
    return bdb.get_user_booking(user.ID_user)


def get_objekt(id):
    return bdb.get_object_with_id(id)


def get_objekt_book(id):
    return bdb.get_object_booking(id)


def check_text_adm(tmp):

    if "add_user_email" in tmp:
        new_user.mail = tmp[16:]
    elif "add_user_role" in tmp:
        new_user.role = tmp[15:]
    elif "add_user_campus" in tmp:
        new_user.campus = tmp[17:]
    elif "add_user" in tmp:
        bdb.add_user(new_user.mail, new_user.role, new_user.campus)

    if "pop_user" in tmp:
        bdb.pop_user(tmp[10:])

    if "add_object_campus" in tmp:
        new_object.campus = tmp[len("add_object_campus")+2:]
    elif "add_object_type" in tmp:
        new_object.type = tmp[len("add_object_type")+2:]
    elif "add_object_name" in tmp:
        new_object.name = tmp[len("add_object_name")+2:]
    elif "add_object_note" in tmp:
        new_object.note = tmp[len("add_object_note")+2:]
    elif "add_object_floor" in tmp:
        new_object.floor = int(tmp[len("add_object_floor")+2:])
    elif "add_object_room_name" in tmp:
        new_object.room_name = tmp[len("add_object_room_name")+2:]
    elif "add_object" in tmp:
        bdb.add_object(new_object)

    if "pop_object" in tmp:
        bdb.pop_object(int(tmp[len("pop_object")+2:]))
