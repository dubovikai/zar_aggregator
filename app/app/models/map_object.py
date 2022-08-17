from datetime import timedelta, datetime

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Table,
    DateTime,
    Float,
    CheckConstraint,
    Index
)
from sqlalchemy.dialects.mysql import ENUM
from sqlalchemy.orm import relationship, backref
from app.db.base_class import Base
from app.schemas.map_object import MapObjectType


class MapObjectTag(Base):
    name = Column(String(256), nullable=False)
    parent_id = Column(Integer, ForeignKey('map_object_tag.id'))
    children = relationship('MapObjectTag', backref=backref('parent', remote_side='MapObjectTag.id'))


Index('uix_map_object_tag', MapObjectTag.name, MapObjectTag.parent_id, unique=True)

map_object_tag_mapping = Table(
    'map_object_tag_mapping',
    Base.metadata,
    Column('map_object_id', Integer, ForeignKey('map_object.id', ondelete='CASCADE'), primary_key=True),
    Column('map_object_tag_id', Integer, ForeignKey('map_object_tag.id', ondelete='CASCADE'), primary_key=True)
)


class MapObjectEventStatus(Base):
    name = Column(String(256), nullable=False, index=True, unique=True)


class MapObject(Base):
    map_object_type = Column(ENUM(MapObjectType))
    __mapper_args__ = {'polymorphic_on': map_object_type}

    name = Column(String(512), nullable=False, index=True, unique=True)
    description = Column(String(1024), nullable=True)
    source_url_vk = Column(String(1024), nullable=True)
    source_id_vk = Column(Integer, nullable=True)
    post_id_vk = Column(Integer, nullable=True)
    address = Column(String(512), nullable=True)
    latitude = Column(Float, CheckConstraint('latitude >= -90 and latitude <= 90', name='chk_map_objects_latitudes'), nullable=False)
    longitude = Column(Float, CheckConstraint('longitude >= 0 and longitude <= 180', name='chk_map_objects_longitudes'), nullable=False)

    tags = relationship(MapObjectTag, secondary=map_object_tag_mapping)

    @property
    def tag_ids(self):
        return [tag.id for tag in self.tags]


class MapObjectEvent(MapObject):
    __mapper_args__ = {'polymorphic_identity': MapObjectType.event}
    id = Column(Integer, ForeignKey('map_object.id'), primary_key=True)
    start_datetime = Column(DateTime, nullable=False)
    duration = Column(Integer, nullable=True)
    status_id = Column(Integer, ForeignKey('map_object_event_status.id'), nullable=False)
    status = relationship(MapObjectEventStatus)

    @property
    def end_datetime(self):
        if self.duration:
            return self.start_datetime + timedelta(seconds=self.duration)

    @property
    def status_name(self):
        # TODO check timezones for property
        if not self.end_datetime:
            return self.status.name
        elif datetime.now() > self.start_datetime and datetime.now() < self.end_datetime:
            return 'in_process'
        else:
            return self.status.name


class MapObjectOrganization(MapObject):
    __mapper_args__ = {'polymorphic_identity': MapObjectType.organization}
    id = Column(Integer, ForeignKey('map_object.id'), primary_key=True)
    contacts = Column(String(1024), nullable=False)


class MapObjectAttraction(MapObject):
    id = Column(Integer, ForeignKey('map_object.id'), primary_key=True)
    __mapper_args__ = {'polymorphic_identity': MapObjectType.attraction}
