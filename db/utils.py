from hashlib import sha256
from envloader import ENV
from db.db_connector import SessionLocal

def createHashedPassword(password: str):
    return sha256((password+'_'+ ENV.HASH_SALT ).encode()).hexdigest()

def getDb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
