from fastapi import APIRouter

from card import RegisterCardModel
from database.cardservice import get_all_user_cards_db, get_exact_user_card_db, \
                                 add_new_card_db, delete_exact_card_db


card_router = APIRouter(prefix='/card', tags=['работа с пластиковыми картами'])


# добавить карту пользователя
@card_router.post('/add-card')
async def add_new_card(data: RegisterCardModel):
    try:
        result = add_new_card_db(data)

        return {'status': 1, 'data': result}

    except Exception as error:
        return {'status': 0, 'data': str(error)}


# Удалить карту пользователя
@card_router.delete('/delete-card')
async def delete_exact_card(user_id: int, card_id: int):
    result = delete_exact_card_db(user_id, card_id)

    return {'status': 1, 'data': result}


# Вывод всех карт пользователя
@card_router.get('/get-all-user-card')
async def get_all_cards(user_id: int):
    result = get_all_user_cards_db(user_id)

    return {'status': 1, 'data': result}


# Вывод определенной карты пользователя
@card_router.get('/get-exact-card')
async def get_exact_card(user_id: int, card_id: int):
    result = get_exact_user_card_db(user_id, card_id)

    return {'status': 1, 'data': result}






