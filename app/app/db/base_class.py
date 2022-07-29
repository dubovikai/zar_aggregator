import re

from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import Column, Integer


@as_declarative()
class Base:
    id = Column(Integer, primary_key=True, autoincrement=True)
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        name = re.sub(r'(?<!^)(?=[A-Z])', '_', cls.__name__).lower()
        return name

    def __repr__(self) -> str:
        return(f'table={self.__tablename__}, id={self.id}')
