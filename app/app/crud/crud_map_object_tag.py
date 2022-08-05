# * `model`: A SQLAlchemy model class
# * `schema`: A Pydantic model (schema) class
import typing as t
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.map_object import MapObjectTag as MapObjectTagModel
from app.schemas.map_object import MapObjectTag as MapObjectTagSchema


class CRUDTag(CRUDBase[MapObjectTagModel, MapObjectTagSchema]):
    def get_all_tags(self, db: Session) -> t.List[MapObjectTagModel]:
        return db.query(MapObjectTagModel).filter(MapObjectTagModel.parent_id.is_(None)).all()

    def get_all_tags_ids_by_id(self, db: Session, id: int) -> t.List[int]:
        models = db.query(MapObjectTagModel).filter(MapObjectTagModel.id == id).all()
        ids_list = []

        def recursive_list_builder(models_: t.List[MapObjectTagModel]) -> t.List[int]:
            nonlocal ids_list
            for model in models_:
                ids_list.append(model.id)
                recursive_list_builder(model.children)

        recursive_list_builder(models)
        return ids_list


tag = CRUDTag(MapObjectTagModel)
