from fastapi import FastAPI
from .books.routes import router
from contextlib import asynccontextmanager
from .db.main import init_db

version='v1'

@asynccontextmanager
async def life_span(app:FastAPI):
    print('Server starting...')
    await init_db()
    yield
    print('Server stoped!')

app=FastAPI(
    version=version,
    title='Book API',
    description='A simple API to manage books',
    lifespan=life_span
)

app.include_router(router,prefix=f'/api/{version}/books',tags=['Books'])