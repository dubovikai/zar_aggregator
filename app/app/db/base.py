# Import all the models, so that Base has them before being
# imported by Alembic
# flake8: noqa: F401

from app.db.base_class import Base, meta
from app.models.user import User

from app.models.map_object import (
    MapObject,
    MapObjectType,
    MapObjectAttraction,
    MapObjectEvent,
    MapObjectEventStatus,
    MapObjectOrganization,
    map_object_tag_mapping,
    MapObjectTag
)
from app.models.favorites import Favorites
