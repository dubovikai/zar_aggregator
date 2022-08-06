import typing as t

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=t.List[schemas.AnyMapObject])
def read_map_objects(
    offset: int = 0,
    limit: int = 10,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> t.Any:
    """
    Retrieve map objects.
    """
    map_objects = crud.map_object.get_multi(db, offset=offset, limit=limit)

    return [schemas.AnyMapObject.parse_obj(map_object) for map_object in map_objects]


@router.get("/{id}", response_model=schemas.AnyMapObject)
def read_map_object(
    id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> t.Any:
    """
    Retrieve map object.
    """
    map_object = crud.map_object.get(db, id=id)

    return schemas.AnyMapObject.parse_obj(map_object)


@router.get("/by_tag/{tag_id}", response_model=t.List[schemas.AnyMapObject])
def read_map_objects_by_tag_id(
    tag_id: int,
    offset: int = 0,
    limit: int = 10,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> t.Any:
    """
    Retrieve map object by tag.
    """
    map_objects = crud.map_object.get_map_objects_by_tag_id(db, id=tag_id, offset=offset, limit=limit)

    return [schemas.AnyMapObject.parse_obj(map_object) for map_object in map_objects]


@router.get("/tags/", response_model=t.List[schemas.MapObjectTag])
def read_categories(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> t.Any:
    """
    Retrieve tags.
    """
    tags = crud.tag.get_all_tags(db)

    return tags


@router.get("/tags/{id}", response_model=schemas.MapObjectTag)
def read_tag(
    id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> t.Any:
    """
    Retrieve tag.
    """
    tag = crud.tag.get(db, id)

    return tag
