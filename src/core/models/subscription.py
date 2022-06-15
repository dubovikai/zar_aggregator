import typing

from .base_model import BaseModel


class Subscription(BaseModel):
    id: int
    name: str
    friendly_name: str
    description: str
    child_subscriptions: typing.Optional[typing.List['Subscription']]
