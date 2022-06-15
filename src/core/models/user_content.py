import typing

from .user import User
from .post import Post
from .subscription import Subscription


class UserContent(User):
    subscriptions: typing.Optional[typing.List[Subscription]]
    unwatched: typing.Optional[typing.List[Post]]
    watched: typing.Optional[typing.List[Post]]
    liked: typing.Optional[typing.List[Post]]
    deleted: typing.Optional[typing.List[Post]]
    favorite: typing.Optional[typing.List[Post]]
