from pydantic import BaseModel

class Book(BaseModel):
    id:int
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