from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .subscription import Subscription  # noqa: F401


class Subscription(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=False, index=True, unique=True)
    friendly_name = Column(String(512))
    description = Column(String(1024))
    parent_id = Column(Integer, ForeignKey('subscription.id'))
    child_subscriptions = relationship('Subscription')
