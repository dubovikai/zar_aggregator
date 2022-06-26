import sqlalchemy as sa
from sqlalchemy.orm import declarative_base

from sqlalchemy.orm import relationship, backref

from main import engine

metadata_obj = sa.MetaData()
Base = declarative_base(metadata=metadata_obj)


class DBSubscription(Base):
    __tablename__ = 'subscription'
    id = sa.Column(sa.INTEGER, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String(256), nullable=False, index=True, unique=True)
    friendly_name = sa.Column(sa.String(512))
    description = sa.Column(sa.String(1024))
    parent_id = sa.Column(sa.INTEGER, sa.ForeignKey('subscription.id'))
    child_subscriptions = relationship('DBSubscription')


metadata_obj.create_all(engine)
