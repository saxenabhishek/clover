import motor.motor_asyncio
import os

MONGO_DETAILS = os.environ.get("monogoURI")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.clover

CheckOutCON = database.get_collection("checkedOutBooks")
recordsCON = database.get_collection("records")
userCON = database.get_collection("user")
