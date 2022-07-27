from typing import TYPE_CHECKING

from sqlalchemy import Column, Float, Integer, String

from app.db.base_class import Base

if TYPE_CHECKING:
    from .attraction import Attraction  # noqa: F401


class Attraction(Base):  # noqa: F811
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(512), nullable=False, index=True, unique=True)
    description = Column(String(1024))
    read_more = Column(String(1024), nullable=True)
    address = Column(String(512), nullable=True)
    latitude = Column(Float)
    longitude = Column(Float)
