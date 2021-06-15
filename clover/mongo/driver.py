import clover
from typing import Tuple
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase, AsyncIOMotorCollection
import os

MONGO_DETAILS = os.environ.get("mongoURI")

client: AsyncIOMotorClient = None
database: AsyncIOMotorDatabase = None
TEST: bool = False


async def connect_db():
    global client
    client = AsyncIOMotorClient(MONGO_DETAILS)


async def close_db():
    client.close()


def turnDBforTesting():
    global TEST
    TEST = True


# Can refactor later!!!!
def get_CheckOutCON():
    database = client.test if TEST else client.clover
    return database.get_collection("checkedOutBooks")


def get_recordsCON():
    database = client.test if TEST else client.clover
    return database.get_collection("records")


def get_userCON():
    print(TEST)
    database = client.test if TEST else client.clover
    return database.get_collection("user")
