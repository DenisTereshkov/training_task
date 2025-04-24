from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column

from config import DATABASE_URL


engine = create_async_engine(
    DATABASE_URL
)

SessionLocal = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    """Base class for all ORM models."""
    pass


class UrlOrm(Base):
    __tablename__ = 'urls'
    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(unique=True)
    abbreviated_url: Mapped[str]


async def create_tables():
    """Creates all tables in the database defined in the models."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
