from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()


@app.get('/')
async def home():
    return {'message':'Hello world!'}

@app.get('/gen/{name}')
async def get_gen(name:str):
    return {'message':f'Hello {name}!'}

@app.get('/gen')
async def get_gen_age(age:int,name:Optional[str]='User'):
    return {'message':f'Hello {name}!','age':age}

class Book(BaseModel):
    titel:str
    author:str

@app.post('/add/{pass1}')
async def add_book(data:Book,pass1:str,age:int=21) -> dict:
    book_dict={}

    book_dict['titel']=data.titel
    book_dict['author']=data.author
    book_dict['age']=age
    book_dict['pass1']=pass1

    return book_dict