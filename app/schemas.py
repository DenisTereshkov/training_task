from pydantic import BaseModel, HttpUrl


class UrlCreate(BaseModel):
    url: HttpUrl


class UrlGet(UrlCreate):
    id: int
