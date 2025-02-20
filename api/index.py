from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Book(BaseModel):
    id: Optional[int] = None
    title: str
    author: str
    description: str
    price: float

books = []
book_id_counter = 1

@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Manager API"}

@app.get("/books", response_model=List[Book])
def get_books():
    return books

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    book = next((book for book in books if book.id == book_id), None)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.post("/books", response_model=Book)
def create_book(book: Book):
    global book_id_counter
    book.id = book_id_counter
    book_id_counter += 1
    books.append(book)
    return book

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
    book_index = next((index for index, book in enumerate(books) if book.id == book_id), None)
    if book_index is None:
        raise HTTPException(status_code=404, detail="Book not found")
    updated_book.id = book_id
    books[book_index] = updated_book
    return updated_book

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    book_index = next((index for index, book in enumerate(books) if book.id == book_id), None)
    if book_index is None:
        raise HTTPException(status_code=404, detail="Book not found")
    deleted_book = books.pop(book_index)
    return {"message": f"Book '{deleted_book.title}' has been deleted"}

from mangum import Adapter
handler = Adapter(app)
