import typing as t
import datetime as dt
import enum

from pydantic import BaseModel, HttpUrl


class MapObjectTag(BaseModel):
    id: t.Optional[int] = None
    name: str
    children: t.Optional[t.List['MapObjectTag']]

    class Config:
        orm_mode = True


class MapObjectEventStatus(BaseModel):
    id: t.Optional[int] = None
    name: str
    description: str


class MapObjectType(enum.Enum):
    event = 'event'
    organization = 'organization'
    attraction = 'attraction'


class MapObject(BaseModel):
    id: t.Optional[int] = None
    name: str
    description: str
    source_url: t.Optional[HttpUrl]
    address: t.Optional[str]
    latitude: float
    longitude: float
    tag_ids: t.Optional[t.List[int]]

    class Config:
        orm_mode = True


class MapObjectEvent(MapObject):
    map_object_type: MapObjectType = MapObjectType.event
    start_datetime: dt.datetime
    end_datetime: dt.datetime
    duration: t.Optional[int]
    status_name: str


class MapObjectOrganization(MapObject):
    map_object_type: MapObjectType = MapObjectType.organization
    contacts: str


class MapObjectAttraction(MapObject):
    map_object_type: MapObjectType = MapObjectType.attraction
