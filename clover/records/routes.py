from typing import List, Optional

from bson import ObjectId
from clover.mongo.driver import recordsCON
from clover.mongo.models import PyObjectId, Record
from fastapi import APIRouter, HTTPException, status
from pydantic import Field

router = APIRouter()


class recRes(Record):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


@router.get("/", response_model=List[recRes])
async def get_records(completed: Optional[bool] = None, page: int = 0):
    find_args = {}
    
    if completed != None:
        find_args["complete"] = completed

    L = recordsCON.find(find_args).sort("_id", 1).skip(page * 10)
    res = [recRes(**i) for i in await L.to_list(length=10)]
    if len(res) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This page doesn't exist")
    return res
