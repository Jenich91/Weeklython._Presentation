import dal
dal.BotDataBase = dal.BotDataBase("base.db")


def test_user_exists_1():
    login = "chaniska"
    email = login + "@21-school.ru"
    tempBool = dal.BotDataBase.user_exists(email)
    assert tempBool is True


def test_user_exists_2():
    login = "aboba"
    tempBool = dal.BotDataBase.user_exists(login)
    assert tempBool is False
