from typing import List, Optional
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
