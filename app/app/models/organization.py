from typing import TYPE_CHECKING

from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .organization import OrganizationType, Organization  # noqa: F401


class OrganizationType(Base):  # noqa: F811
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(512), nullable=False, index=True, unique=True)
    description = Column(String(1024))
    organizations = relationship("Organization", back_populates="organization_type")


class Organization(Base):  # noqa: F811
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(512), nullable=False, index=True, unique=True)
    description = Column(String(1024))
    read_more = Column(String(1024), nullable=True)
    address = Column(String(512), nullable=True)
    latitude = Column(Float)
    longitude = Column(Float)
    organization_type_id = Column(Integer, ForeignKey("organizationtype.id"))
    organization_type = relationship(
        "OrganizationType", back_populates="organizations", uselist=False
    )
