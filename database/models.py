from sqlalchemy import Column, BigInteger, Integer, String, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


# Таблица пользователя
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    phone_number = Column(Integer, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String)
    profile_photo = Column(String, default='None')
    city = Column(String)

    reg_date = Column(DateTime)


# Таблица пластиковых карт
class Card(Base):
    __tablename__ = 'cards'
    id = Column(Integer, primary_key=True, autoincrement=True)
    card_number = Column(Integer, unique=True)
    card_name = Column(String, default='карта')
    exp_date = Column(Integer)
    cvv = Column(Integer, unique=True)
    bank = Column(String)
    balance = Column(Float, default=0)

    reg_date = Column(DateTime)

    user_id = Column(Integer, ForeignKey('users.id'))
    user_fk = relationship(User, lazy='subquery')


# Таблица переводов
class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    card_from = Column(Integer, ForeignKey('cards.id'), nullable=False)
    amount = Column(Float, default=0)
    card_to = Column(Integer, ForeignKey('cards.id'), nullable=False)
    status = Column(Boolean, default=False)

    reg_date = Column(DateTime)

    card_from_fk = relationship(Card, lazy='subquery', foreign_keys=[card_from])
    card_to_fk = relationship(Card, lazy='subquery', foreign_keys=[card_to])

    user_id = Column(Integer, ForeignKey('users.id'))
    user_fk = relationship(User, lazy='subquery')


# Комиссия за платежи
class Commission(Base):
    __tablename__ = 'commissions'
    id = Column(Integer, autoincrement=True, primary_key=True)
    commission_amount = Column(Float, default=0.01)

    changed_date = Column(DateTime)


# Заблокированные пользователи
class BlockedUser(Base):
    __tablename__ = 'blocklist'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)

    blocked_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')

