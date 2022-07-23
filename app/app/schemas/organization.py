import typing as t

from pydantic import BaseModel, HttpUrl


class OrganizationType(BaseModel):
    name: str
    description: str


class OrganizationTypeInDB(OrganizationType):
    id: int

    class Config:
        orm_mode = True    


# Shared properties
class Organization(BaseModel):
    name: str
    description: str
    read_more: t.Optional[HttpUrl]
    address: t.Optional[str]
    latitude: float
    longitude: float
    organization_type: OrganizationType


class OrganizationCreate(Organization):  # Заглушка
    pass


class OrganizationUpdate(Organization):  # Заглушка
    pass


class OrganizationInDB(Organization):
    id: int
    organization_type_id: int

    class Config:
        orm_mode = True
