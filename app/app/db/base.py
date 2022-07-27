# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.attraction import Attraction  # noqa
from app.models.event import Event, EventType  # noqa
from app.models.organization import Organization, OrganizationType  # noqa
from app.models.user import User  # noqa
