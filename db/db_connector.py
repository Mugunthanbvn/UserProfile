from envloader import ENV
import pymongo
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from db.models.users import Base

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{ENV.PG_DB_USER_NAME}:{ENV.PG_DB_PASSWORD}@{ENV.PG_DB_HOST}:{ENV.PG_DB_PORT}/{ENV.PG_DB_NAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()
Base.metadata.create_all(engine)

mongoClient = pymongo.MongoClient(f"mongodb://{ENV.MG_DB_USER_NAME}:{ENV.MG_DB_PASSWORD}@{ENV.MG_DB_HOST}:{ENV.MG_DB_PORT}/{ENV.MG_DB_NAME}")
mongoDb = mongoClient[ENV.MG_DB_NAME]

