import typing as t
import datetime as dt

from pydantic import BaseModel


class Favorites(BaseModel):
    id: t.Optional[int] = None
    user_id: int
    map_object_id: int
    date_start: dt.date = dt.datetime.now()
    date_end: t.Optional[dt.date] = None
    is_active: bool = True

    class Config:
        orm_mode = True
