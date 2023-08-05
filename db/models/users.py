from enum import unique
# from db.db_connector import Base
from sqlalchemy import Column,Integer, CHAR,VARCHAR
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(VARCHAR(255), unique=True,index=True)
    phone = Column(VARCHAR(255), unique=True,index=True)
    firstname =  Column(VARCHAR(255))
    lastname = Column(VARCHAR(255))
    password = Column(CHAR(64))