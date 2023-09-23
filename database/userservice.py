from datetime import datetime

from database import get_db
from database.models import User, BlockedUser
from user import UserRegisterModel


# Регистрация пользователя
def register_user_db(new_data: UserRegisterModel):
    db = next(get_db())

    # Переводим все данные из пайдентика на словарь
    user_data = new_data.model_dump()
    new_user = User(**user_data)

    db.add(new_user)
    db.commit()

    return new_user


# проверка на наличие пользователя
def check_user_db(phone_number: int, password: str = None):
    db = next(get_db())

    checker = db.query(User).filter_by(phone_number=phone_number).first()

    if checker:
        if checker.password == password:
            return checker

        elif checker.password != password:
            return 'Неверный пароль'

    return False


# добавить фото профиля
def add_profile_photo_db(user_id: int, photo_file_name: str):
    db = next(get_db())

    checker = db.query(User).filter_by(id=user_id).first()

    if checker:
        checker.profile_photo = photo_file_name
        db.commit()

        return 'Фото успешно добавлено'

    return 'Профиль не найден'


# изменить информацию о пользователе
def change_user_info_db(user_id: int, info_to_change: str, new_info: str):
    db = next(get_db())

    checker = db.query(User).filter_by(id=user_id).first()

    if checker:
        if info_to_change == 'new_password':
            checker.password = new_info

        elif info_to_change == 'new_email':
            checker.email = new_info

        elif info_to_change == 'new_city':
            checker.city = new_info

        db.commit()

        return f'{info_to_change} изменен'

    return 'Не найден'


# заблокировать пользователя
def block_user_db(user_id: int):
    db = next(get_db())

    checker = db.query(BlockedUser).filter_by(user_id=user_id).first()

    if checker:
        return True

    new_block_user = BlockedUser(user_id=user_id, blocked_date=datetime.now())
    db.add(new_block_user)
    db.commit()

    return True


# разблокировать пользователя
def unblock_user_db(user_id: int):
    db = next(get_db())

    checker = db.query(BlockedUser).filter_by(user_id=user_id).first()

    if checker:
        db.delete(checker)
        db.commit()

        return 'разблокирован'

    return 'не найден'









