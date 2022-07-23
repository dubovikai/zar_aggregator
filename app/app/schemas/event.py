import typing as t
from datetime import datetime
from pydantic import BaseModel, HttpUrl

from .organization import Organization


class EventType(BaseModel):
    name: str
    description: str


class EventTypeInDB(EventType):
    id: int

    class Config:
        orm_mode = True    


# Shared properties
class Event(BaseModel):
    name: str
    description: str
    read_more: t.Optional[HttpUrl]
    address: t.Optional[str]
    latitude: float
    longitude: float
    event_type: EventType
    organization: Organization
    start_datetime: datetime
    end_datetime: t.Optional[datetime]
    vk_uri: t.Optional[str]


class EventCreate(Event):  # Заглушка
    pass


class EventUpdate(Event):  # Заглушка
    pass


class EventInDB(Event):
    id: int
    event_type_id: int
    organization_id: int

    class Config:
        orm_mode = True
