from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from bson import ObjectId


class User(BaseModel):
    name: str
    passw: str
    debt: Optional[int] = 0
    admin: Optional[bool] = False

    class Config:
        schema_extra = {"example": {"name": "Abhishek", "passw": "SuperSecret", "admin": False}}


class CheckOut_arr(BaseModel):
    userId: str
    when: datetime


class CheckOut(BaseModel):
    isbn: str
    issues: List[CheckOut_arr]
    numb: int


class Record(BaseModel):
    isbn: str
    userId: str
    when: Optional[datetime] = None
    till: Optional[datetime] = None
    debt: int = 0
    complete: bool = False

    class Config:
        schema_extra = {
            "example": {
                "isbn": "0226731510",
                "userId": "60c52cd30536c26314ddf528",
                "when": "2021-06-12T23:52:27.351Z",
                "till": "2021-06-12T23:52:27.351Z",
                "debt": 0,
                "complete": False,
            }
        }


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")
