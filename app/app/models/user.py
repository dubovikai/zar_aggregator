from sqlalchemy import Boolean, Column, String

from app.db.base_class import Base


class User(Base):  # noqa: F811
    full_name = Column(String(512), index=True)
    email = Column(String(256), unique=True, index=True, nullable=False)
    hashed_password = Column(String(1024), nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
