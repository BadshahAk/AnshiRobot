

from async_pymongo import AsyncClient

from AnshiRobot import MONGO_DB_URI

DBNAME = "AnshiRobot"

mongo = AsyncClient(MONGO_DB_URI)
dbname = mongo[DBNAME]
