from fastapi import APIRouter, Body
from transaction import TransactionModel


transaction_router = APIRouter(prefix='/transfer', tags=['Переводы денег и мониторинг'])


# Перевод денег с карты на карту
@transaction_router.post('/transfer-money')
async def transfer_money(data: TransactionModel):
    pass


# Вывести все переводы определенного пользователя
@transaction_router.get('/all-payments')
async def get_all_payments(user_id: int):
    pass


# Вывести переводы определенной карты
@transaction_router.get('/card-payments')
async def get_exact_card_payments(user_id: int, card_id: int):
    pass
