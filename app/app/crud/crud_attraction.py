from typing import List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.attraction import Attraction
from app.schemas.attraction import AttractionCreate, AttractionUpdate


class CRUDAttraction(CRUDBase[Attraction, AttractionCreate, AttractionUpdate]):
    def get_all_attractions(self, db: Session) -> List[Attraction]:
        return db.query(self.model).all()


attraction = CRUDAttraction(Attraction)
