import typing

from pydantic import BaseModel


# Shared properties
class SubscriptionBase(BaseModel):
    title: typing.Optional[str] = None
    description: typing.Optional[str] = None
    child_subscriptions: typing.Optional[typing.List['Subscription']]


# Properties to receive on item creation``
class SubscriptionCreate(SubscriptionBase):
    title: str
    parent_id: int


# Properties to receive on item update
class SubscriptionUpdate(SubscriptionBase):
    pass


# Properties shared by models stored in DB
class SubscriptionInDBBase(SubscriptionBase):
    id: int
    title: str
    parent_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Subscription(SubscriptionInDBBase):
    pass


# Properties properties stored in DB
class SubscriptionInDB(SubscriptionInDBBase):
    pass
