from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker


def set_up_db(url, *, autocommit: bool = False, autoflush: bool = False) -> tuple[sessionmaker, Engine]:
  engine = create_engine(url)
  return sessionmaker(autocommit=autocommit, autoflush=autoflush, bind=engine), engine
