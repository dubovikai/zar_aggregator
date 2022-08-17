import sqlalchemy as sa
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class User(Base):  # noqa: F811
    full_name = sa.Column(sa.String(512), index=True, nullable=True)
    email = sa.Column(sa.String(256), unique=True, index=True, nullable=False)
    vk_uid = sa.Column(sa.Integer, sa.ForeignKey("v_k_user.uid"), index=True, unique=True, nullable=True)
    hashed_password = sa.Column(sa.String(1024), nullable=True)
    is_active = sa.Column(sa.Boolean(), default=True)
    is_superuser = sa.Column(sa.Boolean(), default=False)


class VKUser(Base):
    uid = sa.Column(sa.Integer, index=True, unique=True, nullable=False)
    user = relationship(User, uselist=False)
    first_name = sa.Column(sa.String(512), nullable=False)
    last_name = sa.Column(sa.String(512), nullable=False)
