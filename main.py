from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello, {name}!"}
