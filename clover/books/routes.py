from clover.books.frappeAPI import AllBookPages
from fastapi import APIRouter, HTTPException
import requests

FrappeBase = "https://frappe.io/api/method/frappe-library"

router = APIRouter()

Allpages = AllBookPages()

@router.get("/")
async def get_books(page: int = 1):
    if len(data := Allpages.get_page(page)) == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message":data}

@router.get("/{isbn}")
async def get_this_book(isbn : int):
    data = requests.get(FrappeBase, params={"isbn": isbn})
    return data.json()
