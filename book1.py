from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get("/books")
async def read_all_books(category : str = None):
    books_to_return = []

    if category:
        books_to_return = [book for book in BOOKS if book.get('category').casefold()==category.casefold()]
        
        if not books_to_return:
            return f'{{"message": "Could not find the book with category {category}"}}'
        else:
            return books_to_return
    else:
        return BOOKS

@app.get("/books/{book_title}")
async def read_book(book_title:str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
    return f'{{"message": "Could not find the book named {book_title}"}}'

"""
@app.get("/books/{book_author}/")
async def read_book_by_author_category(book_author:str, category: str = None):
    books_to_return = []
    if category:
        books_to_return = [book for book in BOOKS if book.get('author').casefold()==book_author.casefold() and book.get('category').casefold()==category.casefold()]
    else:
        books_to_return = [book for book in BOOKS if book.get('author').casefold()==book_author.casefold()]
    
    if books_to_return:
        return books_to_return
    else:
        return {"message":"Could not find books matching your criteria"}
"""
@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

@app.put("/books/update_book/")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold()==updated_book.get("title").casefold():
            BOOKS[i]=updated_book

@app.delete("/books/delete/")
async def delete_book(book_title:str):
    for i in range(len(BOOKS)):
        print("for >>> ", BOOKS[i].get("title"))
        if BOOKS[i].get("title").casefold()==book_title.casefold():
            print("if >>> ", BOOKS[i].get("title"))
            BOOKS.pop(i)
            break  

@app.get("/books/author/{author_name}/")
async def get_books_by_author(author_name : str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold()==author_name.casefold():
            books_to_return.append(book)

    if books_to_return:
        return books_to_return
    else:
        print(author_name.casefold())
        return f'{{"message":"Could not find any book from author {author_name}"}}'