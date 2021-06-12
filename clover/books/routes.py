from clover.books.frappeAPI import AllBookPages, TisBook
from fastapi import APIRouter, HTTPException
import requests

FrappeBase = "https://frappe.io/api/method/frappe-library"

router = APIRouter()

Allpages = AllBookPages()
tis = TisBook()


@router.get("/")
async def get_books(page: int = 1):
    if len(data := Allpages.get_page(page)) == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": data}


@router.get("/{isbn}")
async def get_this_book(isbn: str):
    try:
        data = tis.get(isbn)
    except ValueError:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": data}
