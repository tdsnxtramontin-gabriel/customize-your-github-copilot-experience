# Starter Code for FastAPI REST APIs Assignment

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Books API")


class Book(BaseModel):
    id: int
    title: str
    author: str
    published_year: int = Field(gt=0)


# In-memory data store
books = []


@app.get("/health")
def health_check():
    # Return a small JSON response to confirm the API is running
    return {"status": "ok"}


@app.get("/books")
def list_books():
    # Return all books
    pass


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: Book):
    # Add a new book to the list
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # Return the book with matching ID or raise 404
    pass


@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    # Replace the existing book data or raise 404
    pass


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    # Remove the book by ID or raise 404
    pass


# Run locally with:
# uvicorn starter-code:app --reload
