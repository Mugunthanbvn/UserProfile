import os
from dotenv import load_dotenv
from pydantic import BaseModel


class Env(BaseModel):
    PG_DB_USER_NAME: str
    PG_DB_PASSWORD: str
    PG_DB_NAME: str
    PG_DB_HOST: str
    PG_DB_PORT: int

    MG_DB_USER_NAME: str
    MG_DB_PASSWORD: str
    MG_DB_NAME: str
    MG_DB_HOST: str
    MG_DB_PORT: int

    HASH_SALT:  str

envPath = '.env'
if(os.path.exists(envPath)):
    load_dotenv(envPath)

ENV: Env = Env(**{
key: os.getenv(key)  for key in Env.__fields__.keys()
})

