from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Subscription])
def read_subscriptions(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve subscriptions.
    """
    subscriptions = crud.subscription.get_all_subscriptions()

    return subscriptions


@router.post("/", response_model=schemas.Subscription)
def create_subscription(
    *,
    db: Session = Depends(deps.get_db),
    subscription_in: schemas.SubscriptionCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new subscription.
    """
    subscription = crud.subscription.create(db=db, obj_in=subscription_in)
    return subscription


@router.put("/{id}", response_model=schemas.Subscription)
def update_subscription(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    subscription_in: schemas.SubscriptionUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an subscription.
    """
    subscription = crud.subscription.get(db=db, id=id)
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    subscription = crud.subscription.update(
        db=db, 
        db_obj=subscription, 
        obj_in=subscription_in
    )
    return subscription


@router.get("/{id}", response_model=schemas.Subscription)
def read_subscription(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get subscription by ID.
    """
    subscription = crud.subscription.get(db=db, id=id)
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return subscription


@router.delete("/{id}", response_model=schemas.Subscription)
def delete_subscription(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an subscription.
    """
    subscription = crud.subscription.get(db=db, id=id)
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    subscription = crud.subscription.remove(db=db, id=id)
    return subscription
