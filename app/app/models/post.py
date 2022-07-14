from typing import TYPE_CHECKING

import enum

from sqlalchemy import (
    Column, 
    ForeignKey, 
    Integer, 
    String, 
    Table, 
    Enum, 
    DateTime, 
    UniqueConstraint
)
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .post import Post  # noqa: F401


map_post_subscription = Table(
    'map_post_subscription', 
    Base.metadata,
    Column('post', Integer, ForeignKey('post.id'), nullable=False),
    Column(
        'subscription', 
        Integer, 
        ForeignKey('subscription.id'), 
        nullable=False
    ),
    UniqueConstraint("subscription", "post")
)


class PostType(enum.Enum):
    event = 'event'
    vacancy = 'vacancy'
    service = 'service'
    ad = 'ad'
    news = 'news'


class Post(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    post_type = Column(Enum(PostType))
    subscriptions = relationship(
        "Subscription", 
        secondary=map_post_subscription, 
        backref="post")
    __mapper_args__ = {'polymorphic_on': post_type}


class PostEvent(Post):
    __mapper_args__ = {'polymorphic_identity': 'event'}
    id = Column(None, ForeignKey('post.id'), primary_key=True)
    event_datetime = Column(DateTime, nullable=True)
    duration = Column(Integer, nullable=True)
    contacts = Column(String(1024), nullable=True)


class PostVacancy(Post):
    __mapper_args__ = {'polymorphic_identity': 'vacancy'}
    id = Column(None, ForeignKey('post.id'), primary_key=True)
    job_title = Column(String(1024), nullable=True)
    organization = Column(String(1024), nullable=True)
    description = Column(String(4096), nullable=True)
    salary = Column(Integer, nullable=True)
    contacts = Column(String(1024), nullable=True)


class PostService(Post):
    __mapper_args__ = {'polymorphic_identity': 'service'}
    id = Column(None, ForeignKey('post.id'), primary_key=True)
    description = Column(String(4096), nullable=True)
    contacts = Column(String(1024), nullable=True)


class PostAd(Post):
    __mapper_args__ = {'polymorphic_identity': 'ad'}
    id = Column(None, ForeignKey('post.id'), primary_key=True)
    description = Column(String(4096), nullable=True)
    contacts = Column(String(1024), nullable=True)


class PostNews(Post):
    __mapper_args__ = {'polymorphic_identity': 'news'}
    id = Column(None, ForeignKey('post.id'), primary_key=True)
    description = Column(String(4096), nullable=True)
    contacts = Column(String(1024), nullable=True)
