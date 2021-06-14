from datetime import datetime

from bson import ObjectId
from clover.books.frappeAPI import AllBookPages, TisBook
from clover.mongo.driver import CheckOutCON, recordsCON
from clover.mongo.models import CheckOut, CheckOut_arr, Record
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter()

Allpages = AllBookPages()
tis = TisBook()

secRate = 0.002


@router.get("/")
async def get_books(page: int = 1):
    if len(data := Allpages.get_page(page)) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return {"message": data}


@router.get("/ct")
async def get_money_idea(traId: str):
    if d := await recordsCON.find_one({"_id": ObjectId(traId)}):
        d = Record(**d)
        delta = datetime.now() - d.when
        print(delta.total_seconds())
        cost = secRate * delta.total_seconds()
        return {"Message": {"cost": cost}}
    else:
        print("hello")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No transaction found")


@router.get("/{isbn}")
async def get_this_book(isbn: str):
    try:
        data = tis.get(isbn)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return {"message": data}


@router.post("/issue", status_code=status.HTTP_201_CREATED)
async def give_this_book(rec: Record):
    rec.when = datetime.now()
    rec.complete = False
    rec.till = None
    item = CheckOut_arr(userId=rec.userId, when=rec.when)
    if await CheckOutCON.find_one({"isbn": rec.isbn}):
        res = await CheckOutCON.update_one({"isbn": rec.isbn}, {"$inc": {"numb": 1}, "$push": {"issues": item.dict()}})
    else:
        entry = CheckOut(isbn=rec.isbn, issues=[item], numb=1)
        res = await CheckOutCON.insert_one(entry.dict())
    res2 = await recordsCON.insert_one(rec.dict())
    return {"message": str(res2.inserted_id)}


class returnDeets(BaseModel):
    traId: str


@router.put("/return")
async def take_back_book(deets: returnDeets):
    if d := await recordsCON.find_one({"_id": ObjectId(deets.traId)}):
        d = Record(**d)
        res = await CheckOutCON.update_one(
            {"isbn": d.isbn}, {"$inc": {"numb": -1}, "$pull": {"issues": {"userId": d.userId}}}
        )
        delta = datetime.now() - d.when
        cost = secRate * delta.total_seconds()
        res2 = await recordsCON.update_one(
            {"_id": ObjectId(deets.traId)}, {"$set": {"till": datetime.now(), "complete": True, "debt": cost}}
        )
        return {"message": {"cost": cost}}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No transaction found")
