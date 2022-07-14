import typing
import datetime as dt

from models.subscription import Subscription
from models.post import PostType

from pydantic import BaseModel


# Shared properties
class Post(BaseModel):
    id: int
    post_type: PostType
    subscriptions: typing.Optional[typing.List[Subscription]]

    class Config:
        orm_mode = True


class PostEvent(Post):
    event_datetime: dt.datetime
    duration: typing.Optional[int]
    contacts: typing.Optional[str]


class PostVacancy(Post):
    job_title: str
    organization: str
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
