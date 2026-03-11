from pydantic import BaseModel
import uuid

class Book(BaseModel):
    title:str
    subtitle:str
    author:str
    published:str
    publisher:str
    pages:int
    description:str
    website:str

class ReturnBook(BaseModel):
    uid:uuid.UUID
    title:str
    subtitle:str
    author:str
    published:str
    publisher:str
    pages:int
    description:str
    website:str

class BookUpdate(BaseModel):
    title:str
    subtitle:str
    description:str