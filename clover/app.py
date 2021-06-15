from clover.mongo.driver import close_db, connect_db
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from clover import book_router
from clover import user_router
from clover import record_router

app = FastAPI(title="backend for clover")

app.add_event_handler("startup",connect_db)
app.add_event_handler("shutdown",close_db)

origins = [
    "*",
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


@app.get("/api")
async def test_Alive():
    return "Backend API is up"


# app.mount("/", StaticFiles(directory="./client/out", html=True), name="static")
