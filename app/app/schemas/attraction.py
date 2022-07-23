import typing as t

from pydantic import BaseModel, HttpUrl


# Shared properties
class Attraction(BaseModel):
    name: str
    description: str
    read_more: t.Optional[HttpUrl]
    address: t.Optional[str]
    latitude: float
    longitude: float


class AttractionCreate(Attraction):  # Заглушка
    pass


class AttractionUpdate(Attraction):  # Заглушка
    pass


class AttractionInDB(Attraction):
    id: int

    class Config:
        orm_mode = True
