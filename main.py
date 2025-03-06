import random
import string
import uuid
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello, {name}!"}


@app.get("/random")
def random_book(isbn: str):
    # generate a random book with isbn
    random.seed(isbn)
    # genera a uuid for the book
    r_uuid = uuid.uuid4()
    return {
        "title": ''.join(random.choices(string.ascii_letters + string.digits, k=10)),
        "author":   ''.join(random.choices(string.ascii_letters + string.digits, k=5)),
        "coverUrl": "https://via.placeholder.com/150",
        "language": "English",
        "publisher": "HarperCollins",
        "published_date": "1988-01-01",
        "isbn": isbn,
        "description": r_uuid,
        "available": 1
    }
