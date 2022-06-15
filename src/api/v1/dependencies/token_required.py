# coding: utf-8
from fastapi import HTTPException, Security, status, Depends
from fastapi.security.api_key import APIKeyQuery, APIKeyCookie

from main import settings


_api_key_query = APIKeyQuery(name='token', auto_error=False)
_api_key_cookie = APIKeyCookie(name='token', auto_error=False)


async def get_api_key(
        api_key_query: str = Security(_api_key_query),
        api_key_cookie: str = Security(_api_key_cookie),
):
    token = settings.api_token

    if api_key_query == token:
        return api_key_query
    elif api_key_cookie == token:
        return api_key_cookie
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )


app_token = Depends(get_api_key)
