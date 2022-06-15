import typing

from .base_model import BaseModel
from .subjects import Person


class User(BaseModel):
    id: int
    login: str
    password_hash: str
    email: str
    is_deleted: bool
    is_active: bool
    person: typing.Optional[Person]
