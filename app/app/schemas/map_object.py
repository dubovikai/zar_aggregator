import typing as t
import datetime as dt
import enum

from pydantic import BaseModel


class MapObjectTag(BaseModel):
    id: t.Optional[int] = None
    name: str
    children: t.Optional[t.List['MapObjectTag']]

    class Config:
        orm_mode = True


class MapObjectEventStatus(BaseModel):
    id: t.Optional[int] = None
    name: str


class MapObjectType(enum.Enum):
    event = 'event'
    organization = 'organization'
    attraction = 'attraction'


class MapObject(BaseModel):
    id: t.Optional[int] = None
    name: str
    description: t.Optional[str]
    source_url_vk: t.Optional[str]
    source_id_vk: t.Optional[int]
    address: t.Optional[str]
    latitude: float
    longitude: float
    tag_ids: t.Optional[t.List[int]]

    class Config:
        orm_mode = True


class MapObjectEvent(MapObject):
    event: bool = True
    map_object_type: MapObjectType = MapObjectType.event
    start_datetime: dt.datetime
    end_datetime: t.Optional[dt.datetime]
    duration: t.Optional[int]
    status_name: str


class MapObjectAttraction(MapObject):
    attraction: bool = True
    map_object_type: MapObjectType = MapObjectType.attraction


class MapObjectOrganization(MapObject):
    organization: bool = True
    map_object_type: MapObjectType = MapObjectType.organization
    contacts: str


class AnyMapObject(BaseModel):
    __root__: t.Union[MapObjectEvent, MapObjectOrganization, MapObjectAttraction]
