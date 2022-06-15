from fastapi import APIRouter, Request, Response
import typing

from core.database.database import DBSubscription

from ..dependencies import app_token, app_user
from core.models.subscription import Subscription

from main import session

router = APIRouter()


@router.get(
    "/subscriptions",
    status_code=200,
    dependencies=[app_token, app_user]
)
async def get_all_subscriptions(request: Request, response: Response) -> typing.List[Subscription]:
    response = []

    subscriptions = session.query(DBSubscription).filter_by(parent_id=None).all()
    response = [Subscription.from_orm(subscription) for subscription in subscriptions]

    return response

