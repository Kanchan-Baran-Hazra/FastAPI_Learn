from sqlmodel import create_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

engine=AsyncEngine(
    create_engine(
    url=Config.DATABASE_URL,
    echo=True
))



async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)