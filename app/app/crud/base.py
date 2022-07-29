import typing as t

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.base_class import Base

ModelType = t.TypeVar("ModelType", bound=Base)
SchemaType = t.TypeVar("SchemaType", bound=BaseModel)


class CRUDBase(t.Generic[ModelType, SchemaType]):
    def __init__(self, model: t.Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update!!, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def get(self, db: Session, id: int) -> t.Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).one_or_none()

    def get_multi(
        self, db: Session, *, offset: int = 0, limit: int = 100
    ) -> t.List[ModelType]:
        return db.query(self.model).offset(offset).limit(limit).all()

    def create(self, db: Session, *, obj_in: SchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: ModelType,
        obj_in: t.Union[SchemaType, t.Dict[str, t.Any]]
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, id: int) -> ModelType:
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj
