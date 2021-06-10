from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/apis")
async def f():
    return "404 idhaar nahi hai"

app.mount("/", StaticFiles(directory="./client/out",html = True), name="static")