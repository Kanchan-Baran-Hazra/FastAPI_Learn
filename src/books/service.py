from .models import Book
from sqlalchemy import select
from .schemas import BookUpdate
import uuid



class BookService:
    async def get_all_book(self,session):
        result=await session.execute(select(Book))
        return result.scalars().all()
    
    async def get_book_by_id(self,session,book_id:uuid.UUID):
        result=await session.execute(select(Book).where(Book.uid==book_id))
        return result.scalars().first()
    
    async def add_book(self,session,book_data):
        book_dict=book_data.model_dump()
        new_book=Book(
            **book_dict
        )
        session.add(new_book)
        await session.commit()
        await session.refresh(new_book)

        return new_book
    
    async def update_book(self,session,book_id:uuid.UUID,book_data:BookUpdate):
        book_data=book_data.model_dump()
        result=await session.execute(select(Book).where(Book.uid==book_id))
        data=result.scalar_one_or_none()

        if data is not None:
            for key,val in book_data.items():
                setattr(data,key,val)

            await session.commit()
            await session.refresh(data)

            return data
        return None
    
    async def delete_book(self, session, book_id: uuid.UUID):

        result = await session.execute(
            select(Book).where(Book.uid == book_id)
        )
    
        book = result.scalars().first()
        print(book)
    
        if book is not None:
            await session.delete(book)
            await session.commit()
            return {"message": "Book deleted"}
    
        return None
        