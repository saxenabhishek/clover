from typing import List, Optional

from bson import ObjectId
import requests
from clover.mongo.driver import get_recordsCON, get_userCON
from clover.mongo.models import PyObjectId, Record
from fastapi import APIRouter, HTTPException, status
from pydantic import Field

router = APIRouter()
FrappeBase = "https://frappe.io/api/method/frappe-library"


class recRes(Record):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    bookTitle: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


@router.get("", response_model=List[recRes])
async def get_records(completed: Optional[bool] = None, page: int = 0):
    find_args = {}

    if completed != None:
        find_args["complete"] = completed

    L = get_recordsCON().find(find_args).sort("_id", 1).skip(page * 10)
    res = []
    for i in await L.to_list(length=10):
        tempName = await get_userCON().find_one({"_id": ObjectId(i["userId"])})
        tempName = tempName["name"]
        tempTitle = requests.get(FrappeBase, {"isbn": i["isbn"]}).json()
        tempTitle = tempTitle["message"][0]["title"]
        res.append(recRes(**i, name=tempName, bookTitle=tempTitle))
    if len(res) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This page doesn't exist")
    return res
