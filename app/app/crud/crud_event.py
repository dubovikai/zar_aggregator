from typing import List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.event import Event
from app.schemas.event import EventCreate, EventUpdate


class CRUDOrganization(CRUDBase[Event, EventCreate, EventUpdate]):

    def get_all_events(
        self, db: Session
    ) -> List[Event]:
        return (
            db.query(self.model).all()
        )


event = CRUDOrganization(Event)
