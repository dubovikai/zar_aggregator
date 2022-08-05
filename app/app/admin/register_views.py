from sqlalchemy.orm import Session
from flask_admin import Admin

from .models.map_object_attraction import MapObjectAttractionView
from .models.map_object_event import MapObjectEventView
from .models.map_object_organization import MapObjectOrganizationView
from .models.map_object_tag import MapObjectTagView
from .models.user import UserView


def register_views(admin: Admin, session: Session):
    admin.add_views(MapObjectAttractionView(session))
    admin.add_views(MapObjectEventView(session))
    admin.add_views(MapObjectOrganizationView(session))
    admin.add_views(MapObjectTagView(session))
    admin.add_views(UserView(session))
