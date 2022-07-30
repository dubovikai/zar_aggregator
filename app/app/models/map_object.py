from datetime import timedelta, datetime

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Table,
    Enum,
    DateTime,
    Float,
    UniqueConstraint,
    Index
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from app.db.base_class import Base
from app.schemas.map_object import MapObjectType


class MapObjectTag(Base):
    name = Column(String(256), nullable=False)
    parent_id = Column(Integer, ForeignKey('map_object_tag.id'))
    children = relationship('MapObjectTag')
    UniqueConstraint('name', 'parent_id', name='uix_map_object_tag')


Index('uix_map_object_tag', MapObjectTag.name, MapObjectTag.parent_id, unique=True)

map_object_tag_mapping = Table(
    'map_object_tag_mapping',
    Base.metadata,
    Column('map_object_id', Integer, ForeignKey('map_object.id'), primary_key=True),
    Column('map_object_tag_id', Integer, ForeignKey('map_object_tag.id'), primary_key=True)
)


class MapObjectEventStatus(Base):
    name = Column(String(256), nullable=False, index=True, unique=True)


class MapObject(Base):
    map_object_type = Column('map_object_type', Enum(MapObjectType))
    __mapper_args__ = {'polymorphic_on': map_object_type}

    name = Column(String(512), nullable=False, index=True, unique=True)
    description = Column(String(1024))
    source_url = Column(String(1024), nullable=True)
    address = Column(String(512), nullable=True)
    latitude = Column(Float)
    longitude = Column(Float)

    tags = relationship(MapObjectTag, secondary=map_object_tag_mapping)

    @hybrid_property
    def tags_ids(self):
        return [tag.id for tag in self.tags]


class MapObjectEvent(MapObject):
    __mapper_args__ = {'polymorphic_identity': 'event'}
    id = Column(Integer, ForeignKey('map_object.id'), primary_key=True)
    start_datetime = Column(DateTime, nullable=True)
    duration = Column(Integer, nullable=True)
    status_id = Column(Integer, ForeignKey('map_object_event_status.id'))
    status = relationship(MapObjectEventStatus)

    @hybrid_property
    def end_datetime(self):
        return self.start_datetime + timedelta(seconds=self.duration)

    @hybrid_property
    def status_name(self):
        # TODO check timezones for property
        if datetime.now() > self.start_datetime and datetime.now() < self.end_datetime:
            return 'in_process'
        else:
            return self.status.name


class MapObjectOrganization(MapObject):
    __mapper_args__ = {'polymorphic_identity': 'organization'}
    id = Column(Integer, ForeignKey('map_object.id'), primary_key=True)
    contacts = Column(String(1024), nullable=True)


class MapObjectAttraction(MapObject):
    id = Column(Integer, ForeignKey('map_object.id'), primary_key=True)
    __mapper_args__ = {'polymorphic_identity': 'attraction'}
