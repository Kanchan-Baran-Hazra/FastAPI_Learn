from fastapi import APIRouter,HTTPException,status
from typing import List
from .schemas import Book,BookUpdate
from .book_data import books


router=APIRouter()


@router.get("/",response_model=List[Book])
def get_books() -> list:
    return books

@router.get("/{book_id}")
def get_book(book_id: int) ->dict:
    for i in books:
        if i['id']==book_id:
            return i
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Book not found!')

@router.post("/add_books",response_model=Book)
def add_books(book: Book):
    new_book=book.model_dump()
    books.append(new_book)

    return new_book


@router.patch("/{book_id}",response_model=Book)
def update_books(book_id: int, book1: BookUpdate):
    for book in books:
        if book['id']==book_id:
            book['title']=book1.title
            book['subtitle']=book1.subtitle
            book['description']=book1.description

            return book
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found!")

@router.delete("/{book_id}",response_model=List[Book])
def delete_books(book_id: int):
    for i in books:
        if i['id']==book_id:
            books.remove(i)
            return books
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Book not found!')












# add example
# {
#    "id":10,
#    "title":"Practical python",
#    "subtitle":"Dive into ES6 and the Future of python",
#    "author":"Nicolás kanchan",
#    "published":"2017-07-16T00:00:00.000Z",
#    "publisher":"O'Reilly optics",
#    "pages":10000000,
#    "description":"To get the page very hard ",
#    "website":"https://doi.org/10.1007/978-1-4842-4221-6"
# }



# {
#   "title": "kanchans book",
#   "subtitle": "krishnapade hazra",
#   "description": "for dad"
# }