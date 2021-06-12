from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from clover import book_router
from clover import user_router

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

app.include_router(book_router, prefix="/api/books", tags=["books"])
app.include_router(user_router, prefix="/api/users", tags=["Users"])


@app.get("/apis")
async def f():
    return "404 idhaar nah hai"


# app.mount("/", StaticFiles(directory="./client/out", html=True), name="static")
