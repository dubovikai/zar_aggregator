import typing as t
from pydantic import BaseModel, EmailStr


# Shared properties
class UserBase(BaseModel):
    email: t.Optional[EmailStr] = None
    vk_uid: t.Optional[int]
    is_active: t.Optional[bool] = True
    is_superuser: bool = False
    full_name: t.Optional[str] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: t.Optional[str] = None


class UserInDBBase(UserBase):
    id: t.Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str


class VKUser(BaseModel):
    uid: int
    user: t.Optional[UserBase]
    first_name: str
    last_name: str
