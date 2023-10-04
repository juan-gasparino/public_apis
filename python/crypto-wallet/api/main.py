import uvicorn

from database import set_up_db
from models import Wallet, RequestWallet, CryptoInfo, RequestCryptoInfo
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
  return {
    "message": "Crypto API 💰"
  }


@app.get("/get_all_cryptos")
async def get_crypto():
  session_maker, _ = set_up_db('postgresql+psycopg://admin:admin@postgres:5432/database')
  session = session_maker()
  result = session.query(Wallet).all()
  result = Wallet.serialized_items(result)
  return {result}


@app.get("/get_crypto/{name_crypto}")
async def get_crypto(name_crypto: str):
  session_maker, _ = set_up_db('postgresql+psycopg://admin:admin@postgres:5432/database')
  session = session_maker()
  item = session.query(Wallet).filter(Wallet.name == name_crypto.upper()).first()
  return {
    "name": item.name,
    "icon_link": item.icon_link,
    "amount": item.amount,
    "price_bought": item.price_bought,
    "date_bought": item.date_bought,
  }


@app.post("/add_crypto")
async def add_crypto(params: RequestWallet):
  session_maker, _ = set_up_db('postgresql+psycopg://admin:admin@postgres:5432/database')
  session = session_maker()
  item = Wallet(
    name=params.name.upper(),
    icon_link=params.icon_link,
    amount=params.amount,
    price_bought=params.price_bought,
    date_bought=params.date_bought
  )
  session.add(item)
  session.commit()
  return "Item added"


@app.post("/update_crypto")
async def add_crypto(params: RequestWallet):
  session_maker, _ = set_up_db('postgresql+psycopg://admin:admin@postgres:5432/database')
  session = session_maker()
  wallet_query = session.query(Wallet)
  item = wallet_query.filter(Wallet.name == params.name.upper())
  item.update({
    Wallet.name: params.name.upper(),
    Wallet.icon_link: params.icon_link,
    Wallet.amount: params.amount,
    Wallet.price_bought: params.price_bought,
    Wallet.date_bought: params.date_bought
  })
  session.commit()
  return "Item updated"


@app.get("/delete_crypto/{name_crypto}")
async def delete_crypto(name_crypto: str):
  session_maker, _ = set_up_db('postgresql+psycopg://admin:admin@postgres:5432/database')
  session = session_maker()
  wallet_query = session.query(Wallet)
  item = wallet_query.filter(Wallet.name == name_crypto.upper()).first()
  session.delete(item)
  session.commit()
  return "Item deleted"


@app.get("/get_crypto_info_all")
async def get_crypto_info_all():
  session_maker, _ = set_up_db('postgresql+psycopg://admin:admin@postgres:5432/database')
  session = session_maker()
  result = session.query(CryptoInfo).all()
  result = CryptoInfo.serialized_items(result)
  return {result}


@app.get("/get_crypto_info/{id}")
async def get_crypto_info(id: int):
  session_maker, _ = set_up_db('postgresql+psycopg://admin:admin@postgres:5432/database')
  session = session_maker()
  crypto_info_query = session.query(CryptoInfo)
  item = crypto_info_query.filter(CryptoInfo.wallet_id == id).first()
  return {
    "wallet_id": item.wallet_id,
    "name": item.name,
    "icon_link": item.icon_link,
    "description": item.description,
    "link": item.link,
    "exchanges": item.exchanges
  }


if __name__ == "__main__":
  uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)