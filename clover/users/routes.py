from typing import List, Optional
from pydantic import Field
from fastapi import APIRouter, Depends, status
from pydantic.main import BaseModel
from clover.mongo.models import User
from clover.mongo.driver import userCON

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
    id: str = Field(None, alias="_id")


class listUserRes(BaseModel):
    mess: List[userRes]


@router.get("/get_users", response_model=listUserRes)
async def get_all_users(name: Optional[str] = None):
    L = userCON.find({"name": {"$regex": f".*{name}.*"}})
    x = []
    for i in await L.to_list(length=10):
        i["_id"] = str(i["_id"])
        x.append(i)
    return {"mess": x}
