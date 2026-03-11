from fastapi import APIRouter,HTTPException,status,Depends
from typing import List
from .schemas import Book,BookUpdate,ReturnBook
from .book_data import books
from .service import BookService
from src.db.main import get_db
from sqlalchemy.ext.asyncio.session import AsyncSession
import uuid


router=APIRouter()

book_service=BookService()

@router.get("/",response_model=List[ReturnBook])
async def get_books(session:AsyncSession=Depends(get_db)) -> list:
    return await book_service.get_all_book(session)

@router.get("/{book_id}",response_model=ReturnBook)
async def get_book(book_id: uuid.UUID,session:AsyncSession=Depends(get_db)) ->dict:
    data=await book_service.get_book_by_id(session,book_id)
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Book not found!')
    return data

@router.post("/add_books",response_model=ReturnBook)
async def add_books(book: Book,session:AsyncSession=Depends(get_db)):
    data=await book_service.add_book(session,book)
    return data


@router.patch("/{book_id}",response_model=ReturnBook)
async def update_books(book_id: uuid.UUID, book1: BookUpdate,session:AsyncSession=Depends(get_db)):
    data=await book_service.update_book(session,book_id,book1)

    if data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found!")
    return data

@router.delete("/{book_id}")
async def delete_books(book_id: uuid.UUID,session:AsyncSession=Depends(get_db)):
    data=await book_service.delete_book(session,book_id)

    if data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Book not found!')
    
    return data








# {
#   "title": "kanchans",
#   "subtitle": "for kanchans",
#   "description": "for father"
# }



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