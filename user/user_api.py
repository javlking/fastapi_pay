from fastapi import APIRouter, Body, UploadFile

from user import UserRegisterModel
from database.userservice import register_user_db, block_user_db, unblock_user_db, \
                                change_user_info_db, check_user_db, add_profile_photo_db


user_router = APIRouter(prefix='/user', tags=['Работа с пользователями'])


# Запрос на регистрацию
@user_router.post('/register')
async def register_user(data: UserRegisterModel):
    checker = check_user_db(data.phone_number)

    if not checker:  # Если пользователя нет в базе
        result = register_user_db(data)

        return {'status': 1, 'data': result}

    return {'status': 0, 'data': checker}


# Запрос на вход в аккаунт
@user_router.post('/login')
async def login_user(phone_number: int = Body(...), password: str = Body(...)):
    result = check_user_db(phone_number, password)

    return {'status': 1, 'data': result}


# Добавить фото профиля
@user_router.post('/upload-photo')
async def upload_photo(user_id: int = Body(...),
                       photo_file: UploadFile = None):

    photo_path = f'media/{photo_file.filename}'
    # сохранение пути к файлу
    result = add_profile_photo_db(user_id, photo_path)

    # Сохранение файла в папку
    with open(photo_path, 'wb') as photo:
        file = await photo_file.read()
        photo.write(file)

    return {'status': 1, 'data': result}


# Изменить данные пользователя
@user_router.put('/change-info')
async def change_user_info(user_id: int = Body(...),
                           info_to_change: str = Body(...),
                           new_info: str = Body(...)):
    result = change_user_info_db(user_id, info_to_change, new_info)

    return {'status': 1, 'data': result}


# Заблокировать пользователя
@user_router.post('/block-user')
async def block_user(user_id: int):
    result = block_user_db(user_id)

    return {'status': 1, 'data': result}


# Разблокировать пользователя
@user_router.delete('/unblock-user')
async def unblock_user(user_id: int):
    result = unblock_user_db(user_id)

    return {'status': 1, 'data': result}
