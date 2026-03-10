from fastapi import FastAPI
from .books.routes import router

version='v1'

app=FastAPI(
    version=version,
    title='Book API',
    description='A simple API to manage books'
    )

app.include_router(router,prefix=f'/api/{version}/books',tags=['Books'])