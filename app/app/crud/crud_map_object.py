# * `model`: A SQLAlchemy model class
# * `schema`: A Pydantic model (schema) class
import typing as t
from sqlalchemy.orm import Session

from app.models import MapObject as MapObjectModel, MapObjectTag
from app.schemas import MapObject as MapObjectSchema
from .crud_map_object_tag import tag


class CRUDMapObject():
    def _from_orm(self, model):
        if not model:
            return None
        for sub_cls in MapObjectSchema.__subclasses__():
            if sub_cls.__name__ == model.__class__.__name__:
                return sub_cls.from_orm(model)

    def get(self, db: Session, id: int) -> t.Any:
        model = db.query(MapObjectModel).with_polymorphic('*').filter(MapObjectModel.id == id).one_or_none()
        return self._from_orm(model)

    def get_map_objects_by_tag_id(self, db: Session, id: int, offset: int, limit: int) -> t.Any:
        tag_ids = tag.get_all_tags_ids_by_id(db, id)
        models = db.query(MapObjectModel).with_polymorphic('*') \
            .join(MapObjectModel.tags) \
            .filter(MapObjectTag.id.in_(tag_ids)) \
            .offset(offset=offset).limit(limit=limit) \
            .all()
        return [self._from_orm(model) for model in models]

    def get_multi(self, db: Session, *, offset: int = 0, limit: int = 100) -> t.Any:
        models = db.query(MapObjectModel).with_polymorphic('*').offset(offset).limit(limit).all()
        return [self._from_orm(model) for model in models]


map_object = CRUDMapObject()
