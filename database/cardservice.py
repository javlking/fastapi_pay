from datetime import datetime

from database import get_db
from database.models import Card

from card import RegisterCardModel


# добавить карту
def add_new_card_db(card_data: RegisterCardModel):
    db = next(get_db())

    card_info = card_data.model_dump()

    new_card = Card(reg_date=datetime.now(), **card_info)

    db.add(new_card)
    db.commit()

    return True


# удалить карты
def delete_exact_card_db(user_id: int, card_id: int):
    db = next(get_db())

    exact_card = db.query(Card).filter_by(user_id=user_id, id=card_id).first()

    if exact_card:
        db.delete(exact_card)
        db.commit()

        return 'Карта успешно удалена'

    return 'Карта не найдена'


# вывести все карты пользователя
def get_all_user_cards_db(user_id: int):
    db = next(get_db())

    user_cards = db.query(Card).filter_by(user_id=user_id).all()

    return user_cards


# вывести определенную карту пользователя
def get_exact_user_card_db(user_id: int, card_id: int):
    db = next(get_db())

    exact_card = db.query(Card).filter_by(user_id=user_id, id=card_id).first()

    return exact_card





