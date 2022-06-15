# coding: utf-8
from core.models.user import User

from fastapi import HTTPException, status, Depends, Security
from fastapi.security.api_key import APIKeyHeader

_user_id_header = APIKeyHeader(name='X-CURRENT-USER', auto_error=False)


def upsert_user(user_id):
    try:
        user = User(id=user_id, login='user_login', password_hash=321, email='d@d.d', is_deleted=False, is_active=True)
        return user
    except (ValueError, AttributeError, KeyError):
        return None


async def get_user(
    user_id: int = Security(_user_id_header)
):
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User id not specified"
        )

    user = upsert_user(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Can't decode user id"
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User is not active"
        )

    if user.is_deleted:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User is deleted"
        )

    return user

app_user = Depends(get_user)
