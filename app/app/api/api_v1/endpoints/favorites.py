import typing as t

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, models
from app.api import deps
from app.schemas.favorites import Favorites

router = APIRouter()


@router.get("/{user_id}", response_model=t.List[Favorites])
def read_user_favorites(
    user_id: int,
    offset: int = 0,
    limit: int = 10,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> t.Any:
    """
    Retrieve favorites.
    """
    user_favorites = crud.favorites.get_user_favorites(db, user_id=user_id, offset=offset, limit=limit)

    return user_favorites


@router.post("/", response_model=Favorites)
def create_favorites(
    *,
    db: Session = Depends(deps.get_db),
    favorites_in: Favorites,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> t.Any:
    """
    Create new Favorites.
    """
    create_favorites = crud.favorites.create(db=db, obj_in=favorites_in)
    return create_favorites


@router.delete("/{id}", response_model=Favorites)
def delete_favorites(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> t.Any:
    """
    Delete an Favorites.
    """
    del_favorites = crud.favorites.remove(db=db, id=id)
    return del_favorites
