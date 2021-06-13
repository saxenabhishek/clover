from typing import List, Optional
from bson import ObjectId
from clover.mongo.driver import userCON
from clover.mongo.models import PyObjectId, User
from fastapi import APIRouter, Depends, status
from pydantic import Field

router = APIRouter()


async def hashpass(deets: User):
    # will make a proper hash in prod
    hashedpass = deets.passw + "HASH"
    deets.passw = hashedpass
    return deets


@router.post("/make_user", status_code=status.HTTP_201_CREATED)
async def make_user(deets: User = Depends(hashpass)):
    user = await userCON.insert_one(deets.dict())
    return {"inserted_id": str(user.inserted_id)}


class userRes(User):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


@router.get("/get_users", response_model=List[userRes])
async def get_all_users(name: Optional[str] = ""):
    L = userCON.find({"name": {"$regex": f".*{name}.*"}})
    res = [userRes(**i) for i in await L.to_list(length=10)]
    return res
