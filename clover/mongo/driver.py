from typing import Tuple
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase, AsyncIOMotorCollection
import os

MONGO_DETAILS = os.environ.get("mongoURI")

client: AsyncIOMotorClient = None
database: AsyncIOMotorDatabase = None

CheckOutCON: AsyncIOMotorCollection = None
recordsCON: AsyncIOMotorCollection = None
userCON: AsyncIOMotorCollection = None

async def connect_db():
    global client
    global database
    client = AsyncIOMotorClient(MONGO_DETAILS)
    database = client.clover
    set_tables()


async def close_db():
    client.close()


# Can refactor later
def get_CheckOutCON():
    return CheckOutCON


def get_recordsCON():
    return recordsCON


def get_userCON():
    return userCON


def set_tables():
    if database:
        global CheckOutCON
        global recordsCON
        global userCON
        CheckOutCON = database.get_collection("checkedOutBooks")
        recordsCON = database.get_collection("records")
        userCON = database.get_collection("user")
    else:
        raise ValueError("database object is not set")
