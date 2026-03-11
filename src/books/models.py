from src.db.main import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import Integer,String,DateTime
import uuid
from datetime import datetime

class Book(Base):
    __tablename__='books'
    uid:Mapped[uuid.UUID]=mapped_column(primary_key=True,default=uuid.uuid4)
    title:Mapped[str]=mapped_column(String)
    subtitle:Mapped[str]=mapped_column(String)
    author:Mapped[str]=mapped_column(String)
    published:Mapped[str]=mapped_column(String)
    publisher:Mapped[str]=mapped_column(String)
    pages:Mapped[int]=mapped_column(Integer)
    description:Mapped[str]=mapped_column(String)
    website:Mapped[str]=mapped_column(String)
    created_at:Mapped[datetime]=mapped_column(DateTime,default=datetime.now())
    updated_at:Mapped[datetime]=mapped_column(DateTime,default=datetime.now(),onupdate=datetime.now())

    def __repr__(self):
        return f'<Book {self.title}> '