from typing import TYPE_CHECKING

import enum

from sqlalchemy import Column, ForeignKey, Integer, String, Table, Enum, DateTime, Index
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .post import Post  # noqa: F401


map_user_subscription = Table(
    'user_subscription', 
    Base.metadata,
    Column('user', Integer, ForeignKey('user.id'), nullable=False),
    Column(
        'subscription', 
        Integer, 
        ForeignKey('subscription.id'), 
        nullable=False
    ),
    __table_args__=(Index(
        'idx_map_post_subscription', 
        "subscription", 
        "post", 
        unique=True
    ),)
)

map_user_post_unwatched = Table(
    'map_user_post_unwatched', 
    Base.metadata,
    Column('user', Integer, ForeignKey('user.id'), nullable=False),
    Column(
        'post', 
        Integer, 
        ForeignKey('post.id'), 
        nullable=False
    ),
    __table_args__=(Index(
        'idx_map_user_post_unwatched', 
        "subscription", 
        "post", 
        unique=True
    ),)
)

map_user_post_watched = Table(
    'map_user_post_unwatched', 
    Base.metadata,
    Column('user', Integer, ForeignKey('user.id'), nullable=False),
    Column(
        'post', 
        Integer, 
        ForeignKey('post.id'), 
        nullable=False
    ),
    __table_args__=(Index(
        'idx_map_user_post_unwatched', 
        "user", 
        "post", 
        unique=True
    ),)
)

map_user_post_liked = Table(
    'map_user_post_liked', 
    Base.metadata,
    Column('user', Integer, ForeignKey('user.id'), nullable=False),
    Column(
        'post', 
        Integer, 
        ForeignKey('post.id'), 
        nullable=False
    ),
    __table_args__=(Index(
        'idx_map_user_post_liked', 
        "user", 
        "post", 
        unique=True
    ),)
)

map_user_post_deleted = Table(
    'map_user_post_deleted', 
    Base.metadata,
    Column('user', Integer, ForeignKey('user.id'), nullable=False),
    Column(
        'post', 
        Integer, 
        ForeignKey('post.id'), 
        nullable=False
    ),
    __table_args__=(Index(
        'idx_map_user_post_deleted', 
        "user", 
        "post", 
        unique=True
    ),)
)


class UserContent(Base):
    user = Column(Integer, ForeignKey('user.id'))
    subscriptions = relationship(
        "Subscription", 
        secondary=map_user_subscription, 
        backref="post")
    watched = relationship(
        "Post", 
        secondary=map_user_post_watched, 
        backref="post")
    liked = relationship(
        "Post", 
        secondary=map_user_post_liked, 
        backref="post")
    deleted = relationship(
        "Post", 
        secondary=map_user_post_deleted, 
        backref="post")
