from datetime import datetime, timedelta
import typing

from .base_model import BaseModel
from .subjects import Organization
from .subscription import Subscription


class Post(BaseModel):
    id: int
    subscriptions: typing.Optional[typing.List[Subscription]]


class PostEvent(Post):
    event_datetime: datetime
    duration: typing.Optional[timedelta]
    contacts: typing.Optional[str]


class PostVacancy(Post):
    post: str
    organization: Organization
    description: str
    salary: int
    contacts: str


class PostService(Post):
    description: str
    contacts: str


class PostAd(Post):
    description: str
    contacts: str


class PostNews(Post):
    description: str
    contacts: str
