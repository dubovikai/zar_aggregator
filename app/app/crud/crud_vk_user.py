# * `model`: A SQLAlchemy model class
# * `schema`: A Pydantic model (schema) class
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import VKUser as VKUserModel, User
from app.schemas import VKUser as VKUserSchema


class CRUDVKUser(CRUDBase[VKUserModel, VKUserSchema]):
    def get_user_by_uid(self, db: Session, uid: int) -> User:
        return db.query(VKUserModel).filter(VKUserModel.uid == uid).one_or_none()

    def get_or_create_user(self, db: Session, vk_user: VKUserSchema) -> VKUserModel:
        # TODO Check if vk user account is not banned and deleted
        new_vk_user = self.get_user_by_uid(db, vk_user.uid)
        if not new_vk_user:
            new_vk_user = self.create(db, obj_in=vk_user)
        if not new_vk_user.user:
            new_user = User(
                full_name=f"{new_vk_user.first_name} {new_vk_user.last_name}",
                email=f"vk_{new_vk_user.uid}@vk.com",
                vk_uid=new_vk_user.uid,
                hashed_password=None
            )
            db.add(new_user)
            db.commit()
        db.refresh(new_user)
        db.refresh(new_vk_user)
        return new_vk_user


vk_user = CRUDVKUser(VKUserModel)
