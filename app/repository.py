from database import SessionLocal, UrlOrm
from sqlalchemy import select
from pydantic import HttpUrl

from .schemas import UrlCreate


class UrlRepository:
    @classmethod
    async def add_url(cls, data: UrlCreate):
        """
        Adds a new URL to the database.
        """
        async with SessionLocal() as session:
            url_dict = data.model_dump()
            if isinstance(url_dict.get("url"), HttpUrl):
                url_dict["url"] = str(url_dict["url"])
            url = UrlOrm(**url_dict)
            session.add(url)
            await session.flush()
            await session.commit()
            return url

    @classmethod
    async def get_url(cls, url_id: int):
        """
        Retrieves a URL from the database by its ID.
        """
        async with SessionLocal() as session:
            query = select(UrlOrm).where(UrlOrm.id == url_id)
            result = await session.execute(query)
            url_model = result.scalar_one_or_none()
            return url_model
