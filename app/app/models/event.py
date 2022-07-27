from typing import TYPE_CHECKING

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .event import EventType, Event  # noqa: F401


class EventType(Base):  # noqa: F811
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(512), nullable=False, index=True, unique=True)
    description = Column(String(1024))
    events = relationship("Event", back_populates="event_type")


class Event(Base):  # noqa: F811
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(512), nullable=False, index=True, unique=True)
    description = Column(String(1024))
    read_more = Column(String(1024), nullable=True)
    address = Column(String(512), nullable=True)
    latitude = Column(Float)
    longitude = Column(Float)
    event_type_id = Column(Integer, ForeignKey("eventtype.id"))
    event_type = relationship("EventType", back_populates="events", uselist=False)
    organization_id = Column(Integer, ForeignKey("organization.id"))
    organization = relationship("Organization")
    start_datetime = Column(DateTime)
    end_datetime = Column(DateTime, nullable=True)
    vk_uri = Column(String(256), nullable=True)
