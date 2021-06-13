from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from clover import book_router
from clover import user_router
from clover import record_router

app = FastAPI()

origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(book_router, prefix="/api/books", tags=["Books"])
app.include_router(user_router, prefix="/api/users", tags=["Users"])
app.include_router(record_router, prefix="/api/recs", tags=["Records"])


@app.get("/apis")
async def f():
    return "404 idhaar nahi hai"


# app.mount("/", StaticFiles(directory="./client/out", html=True), name="static")
