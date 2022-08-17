import datetime as dt
from typing import Any
# import requests

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from vk_api.vk_api import VkApi

from app import crud, models, schemas
from app.api import deps
from app.core import security
from app.core.config import settings
from app.core.security import get_password_hash
from app.utils import (
    generate_password_reset_token,
    send_reset_password_email,
    verify_password_reset_token
)

router = APIRouter()


@router.post("/login/access-token", response_model=schemas.Token)
def login_access_token(
    db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = crud.user.authenticate(
        db, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not crud.user.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = dt.timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }


@router.post("/login/test-token", response_model=schemas.User)
def test_token(current_user: models.User = Depends(deps.get_current_user)) -> Any:
    """
    Test access token
    """
    return current_user


@router.post("/password-recovery/{email}", response_model=schemas.Msg)
def recover_password(email: str, db: Session = Depends(deps.get_db)) -> Any:
    """
    Password Recovery
    """
    user = crud.user.get_by_email(db, email=email)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system.",
        )
    password_reset_token = generate_password_reset_token(email=email)
    send_reset_password_email(
        email_to=user.email, email=email, token=password_reset_token
    )
    return {"msg": "Password recovery email sent"}


@router.post("/reset-password/", response_model=schemas.Msg)
def reset_password(
    token: str = Body(...),
    new_password: str = Body(...),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Reset password
    """
    email = verify_password_reset_token(token)
    if not email:
        raise HTTPException(status_code=400, detail="Invalid token")
    user = crud.user.get_by_email(db, email=email)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system.",
        )
    elif not crud.user.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    hashed_password = get_password_hash(new_password)
    user.hashed_password = hashed_password
    db.add(user)
    db.commit()
    return {"msg": "Password updated successfully"}


@router.get("/vk_auth/redirect")
def get_redirect() -> Any:
    """
    Редирект на https://oauth.vk.com/authorize для авторизации в ВК.
    """
    return RedirectResponse(
        'https://oauth.vk.com/authorize?client_id=51402004&display=page&redirect_uri=http://localhost:8000/api/v1/vk_auth/callback&response_type=code&v=5.131'
    )


@router.get("/vk_auth/callback", response_model=schemas.Token)
def get_vk_access_token(
    code: str = '',
    error: str = '',
    error_description: str = '',
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Callback метод для авторизации в ВК. Вернет access token апи и ВК после успешной авторизации на странице redirect.
    """
    if error:
        raise HTTPException(status_code=400, detail=f"VK Error {error}: {error_description}")

    if code:
        redirect_url = "http://localhost:8000/api/v1/vk_auth/callback"
        app_id = 51402004
        secret = 'AaHczuSNu2amEIw0GUhf'

        vk_session = VkApi(app_id=app_id, client_secret=secret)
        vk_session.code_auth(code, redirect_url)
        vk_api = vk_session.get_api()
        data = vk_api.users.get(ids=vk_session.token['user_id'])[0]

        new_vk_user = models.VKUser(
            uid=vk_session.token['user_id'],
            first_name=data['first_name'],
            last_name=data['last_name']
        )

        vk_user = crud.vk_user.get_or_create_user(db, new_vk_user)

        access_token_expires = dt.timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        return {
            "access_token": security.create_access_token(
                vk_user.user.id, expires_delta=access_token_expires
            ),
            "token_type": "bearer",
            "vk_token": vk_session.token
        }
