from sqlalchemy import Boolean, Column, Integer, Date, ForeignKey

from sqlalchemy.orm import relationship

from app.db.base_class import Base
from .map_object import MapObject


class Favorites(Base):
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    map_object_id = Column(Integer, ForeignKey('map_object.id'), nullable=False)
    map_object = relationship(MapObject)
    date_start = Column(Date, nullable=False)
    date_end = Column(Date)
    is_active = Column(Boolean)
