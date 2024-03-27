from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self,id,title,author,description,rating) -> None:
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating

class BookRequest(BaseModel):
    id: Optional[int]
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0,lt=6)


BOOKS = [
    Book(1, "Computer Science Pro", "PyAuthor", "Highly Informative", 5),
    Book(2, "Advanced Data Structures", "DataGuru", "In-depth Guide", 4),
    Book(3, "The Art of Programming", "CodeMaster", "Comprehensive Insights", 5),
    Book(4, "Machine Learning Essentials", "AIWizard", "Cutting-edge Techniques", 4),
    Book(5, "Network Security Handbook", "CyberGuard", "Essential Guidelines", 5),
    Book(6, "Artificial Intelligence Fundamentals", "AIExplorer", "Insightful Exploration", 4),
    Book(7, "Web Development Mastery", "WebWizard", "Practical Techniques", 5),
    Book(8, "Data Science Essentials", "DataGenius", "Comprehensive Overview", 4),
    Book(9, "Mobile App Development Guide", "AppGenie", "Step-by-Step Instructions", 4),
    Book(10, "Cybersecurity Handbook", "SecuritySavvy", "Critical Strategies", 5),
    Book(11, "Cloud Computing Explained", "CloudExpert", "Clear Explanations", 4),
    Book(12, "Game Development Essentials", "GameMaster", "Creative Insights", 4),
    Book(13, "Blockchain Basics", "CryptoScribe", "Foundational Knowledge", 5),
    Book(14, "Python Programming Guide", "PyWizard", "Hands-on Learning", 5),
    Book(15, "Big Data Analytics Handbook", "DataInsight", "In-depth Analysis", 4)
]


@app.get("/books")
async def get_books():
    return BOOKS

@app.post("/books/create_book")
async def create_book(new_book:BookRequest):
    new_book1 = Book(**new_book.dict())
    #new_book = Book(**new_book.model_dump())
    BOOKS.append(find_book_id(new_book1))

def find_book_id(Book):
    Book.id = 1 if len(BOOKS)==0 else BOOKS[-1].id+1
    return Book