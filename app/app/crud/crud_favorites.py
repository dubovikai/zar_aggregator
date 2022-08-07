# * `model`: A SQLAlchemy model class
# * `schema`: A Pydantic model (schema) class
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase

from app.models.favorites import Favorites as FavoritesModel

from app.schemas.favorites import Favorites as FavoritesSchema


class CRUDFavorites(CRUDBase[FavoritesModel, FavoritesSchema]):
    def get_user_favorites(self, db: Session, user_id: int, offset: int, limit: int):
        models = db.query(FavoritesModel) \
            .filter(FavoritesModel.user_id == user_id) \
            .offset(offset=offset).limit(limit=limit) \
            .all()
        return models


favorites = CRUDFavorites(FavoritesModel)
