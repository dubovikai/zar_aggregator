from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.subscription import Subscription
from app.schemas.subscription import SubscriptionCreate, SubscriptionUpdate


class CRUDSubscription(CRUDBase[Subscription, SubscriptionCreate, SubscriptionUpdate]):
    def create(
        self, db: Session, *, obj_in: SubscriptionCreate
    ) -> Subscription:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_all_subscriptions(
        self, db: Session
    ) -> List[Subscription]:
        return (
            db.query(self.model)
            .filter(Subscription.parent_id == None)
            .all()
        )


subscription = CRUDSubscription(Subscription)
