from datetime import datetime

from database import get_db
from database.models import Transaction, Card
from transaction import TransactionModel


# Перевод денег (создать транзакцию)
def add_new_transaction_db(data: TransactionModel):
    db = next(get_db())

    # получаем информацию о картах
    card_from = db.query(Card).filter_by(card_number=data.card_from).first()
    card_to = db.query(Card).filter_by(card_number=data.card_to).first()

    # проверка баланса card_from
    if card_from.balance >= data.amount:
        card_from.balance -= data.amount
        card_to.balance += data.amount

        # создаем запись о сделке
        transaction = data.model_dump()
        new_transaction = Transaction(reg_date=datetime.now(), **transaction)

        db.add(new_transaction)
        db.commit()

        return True

    return False


# вывод транзакций определенной карты
def get_exact_card_db(user_id: int, card_id: int):
    db = next(get_db())

    exact_card_monitoring = db.query(Transaction).filter_by(user_id=user_id,
                                                            card_from=card_id).all()

    return exact_card_monitoring


# вывод всех транзакций по всем картам пользователя
def get_all_cards_monitor_db(user_id: int):
    db = next(get_db())

    all_cards_monitoring = db.query(Transaction).filter_by(user_id=user_id).all()

    return all_cards_monitoring


