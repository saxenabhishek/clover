from fastapi import APIRouter
import requests
from typing import Optional

FrappeBase = "https://frappe.io/api/method/frappe-library"

router = APIRouter()


@router.get("/")
async def get_books(page: Optional[int] = 0):
    data = requests.get(FrappeBase, params={"page": page})
    return data.json()

@router.get("/{isbn}")
async def get_this_book(isbn : int):
    data = requests.get(FrappeBase, params={"isbn": isbn})
    return data.json()
