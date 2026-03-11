from sqlmodel import create_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config
from sqlalchemy.orm import DeclarativeBase,sessionmaker
from sqlalchemy.ext.asyncio.session import AsyncSession

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

async_session= sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db():
    async with async_session() as session:
        yield session