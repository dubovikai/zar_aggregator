import typing as t
from .user import User

from .map_object import (
    MapObjectEventStatus,
    MapObject,
    MapObjectEvent,
    MapObjectOrganization,
    MapObjectAttraction,
    MapObjectTag,
    map_object_tag_mapping
)

map_object_union_type = t.Union[
    MapObjectAttraction,
    MapObjectEvent,
    MapObjectOrganization
]

map_object_type_list = [
    MapObjectAttraction,
    MapObjectEvent,
    MapObjectOrganization
]