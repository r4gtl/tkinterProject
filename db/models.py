from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Utente(Base):
    __tablename__ = 'utenti'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String)

DATABASE_URL = "sqlite:///app.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
