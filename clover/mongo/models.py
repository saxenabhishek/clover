from typing import List
from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    name: str
    passw: str
    debt: int = 0
    admin: bool = False

    class Config:
        schema_extra = {"example": {"name": "Abhishek", "passw": "SuperSecret", "debt": 45, "admin": False}}


class CheckOut_arr(BaseModel):
    UserID: str
    time: datetime


class CheckOut(BaseModel):
    isbn: str
    issues: List[CheckOut_arr]
    numb: int


class Record(BaseModel):
    isbn: str
    userID: str
    when: datetime
    till: datetime
    debt: int = 0
