from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pydantic import BaseModel

# 👇 Create FastAPI app
app = FastAPI()

# 👇 Enable CORS (lets your React frontend call this backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 📘 Define Book model
class Book(BaseModel):
    id: int
    title: str
    author: str
    genre: str

# 📚 Sample book data
books = [
    {"id": 1, "title": "1984", "author": "George Orwell", "genre": "Dystopian"},
    {"id": 2, "title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Romance"},
    {"id": 3, "title": "The Hobbit", "author": "J.R.R. Tolkien", "genre": "Fantasy"},
    {"id": 4, "title": "Brave New World", "author": "Aldous Huxley", "genre": "Dystopian"},
]

# 🔹 Route to get all books
@app.get("/books", response_model=List[Book])
def get_books():
    return books

# 🔹 Route to get recommendations by genre
@app.get("/recommend/{genre}", response_model=List[Book])
def recommend_books(genre: str):
    return [b for b in books if b["genre"].lower() == genre.lower()]
