import json

from sqlalchemy import Column, Integer, Float, String, BigInteger
from sqlalchemy.orm import declarative_base

from pydantic import BaseModel

Base = declarative_base()


class RequestWallet(BaseModel):
  name: str = "BTC"
  icon_link: str = "https://s2.coinmarketcap.com/static/img/coins/128x128/1.png"
  amount: int = 0
  price_bought: float = 0.0
  date_bought: int = 1696194539753


class RequestCryptoInfo(BaseModel):
  wallet_id: int = 1
  name: str = "Bitcoin"
  icon_link: str = "https://s2.coinmarketcap.com/static/img/coins/128x128/1.png"
  description: str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt"
  link: str = "https://bitcoin.org/en"
  exchanges: str = str([{"name":"binance","link":"www.binance.com/en"},{"name":"kucoin","link":"www.kucoin.com"}])


class Wallet(Base):
  __tablename__ = 'wallet'

  id = Column(Integer(), primary_key=True)
  name = Column(String(255), nullable=False, unique=True)
  icon_link = Column(String(255), nullable=False)
  amount = Column(Integer(), nullable=False, default=0)
  price_bought = Column(Float(), nullable=False, default=0.0)
  date_bought = Column(BigInteger(), nullable=False, default=1696194539753)


  @staticmethod
  def serialized_items(items):
    json_array = []
    for item in items:
      json_array.append({
        "name": item.name,
        "icon_link": item.icon_link,
        "amount": item.amount,
        "price_bought": item.price_bought,
        "date_bought": item.date_bought,
      })
    return json.dumps(json_array)


class CryptoInfo(Base):
  __tablename__ = 'crypto_info'

  id = Column(Integer(), primary_key=True)
  wallet_id = Column(Integer(), nullable=False)
  name = Column(String(255), nullable=False, unique=True)
  icon_link = Column(String(255), nullable=False)
  description = Column(String(255), nullable=False)
  link = Column(String(255), nullable=False)
  exchanges = Column(String(255), nullable=False)


  @staticmethod
  def serialized_items(items):
    json_array = []
    for item in items:
      json_array.append({
        "wallet_id": item.wallet_id,
        "name": item.name,
        "icon_link": item.icon_link,
        "description": item.description,
        "link": item.link,
        "exchanges": item.exchanges,
      })
    return json.dumps(json_array)