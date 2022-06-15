from .base_model import BaseModel
import typing


class Organization(BaseModel):
    id: int
    name: str
    address: str
    coordinates: typing.Tuple[float, float]
    contacts: str


class Person(BaseModel):
    id: int
    name: str
    address: str
    contacts: str
