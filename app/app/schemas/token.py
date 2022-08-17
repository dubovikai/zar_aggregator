import typing as t

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str
    vk_token: t.Optional[t.Dict]


class TokenPayload(BaseModel):
    sub: t.Optional[int] = None
