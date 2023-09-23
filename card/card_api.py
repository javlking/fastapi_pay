from fastapi import APIRouter, Body

from card import RegisterCardModel


card_router = APIRouter(prefix='/card', tags=['работа с пластиковыми картами'])


# добавить карту пользователя
@card_router.post('/add-card')
async def add_new_card(data: RegisterCardModel):
    pass


# Удалить карту пользователя
@card_router.delete('/delete-card')
async def delete_exact_card(user_id: int, card_id: int):
    pass


# Вывод всех карт пользователя
@card_router.get('/get-all-user-card')
async def get_all_cards(user_id: int):
    pass


# Вывод определенной карты пользователя
@card_router.get('/get-exact-card')
async def get_exact_card(user_id: int, card_id: int):
    pass






