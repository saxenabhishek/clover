from clover.books.frappeAPI import AllBookPages
from fastapi import APIRouter
import requests
from typing import Optional

FrappeBase = "https://frappe.io/api/method/frappe-library"

router = APIRouter()

Allpages = AllBookPages()

@router.get("/")
async def get_books(page: int = 1):
    return {"message":Allpages.get_page(page)}

@router.get("/{isbn}")
async def get_this_book(isbn : int):
    data = requests.get(FrappeBase, params={"isbn": isbn})
    return data.json()
