from flask_admin.contrib.sqla import ModelView
from sqlalchemy.orm import Session

from app.models import MapObjectOrganization
from app.schemas.map_object import MapObjectType


class MapObjectOrganizationView(ModelView):
    column_list = [
        "name",
        "description",
        "source_url",
        "address",
        "latitude",
        "longitude",
        "tags",
        "contacts"
    ]

    form_columns = [
        "name",
        "description",
        "source_url",
        "address",
        "latitude",
        "longitude",
        "tags",
        "contacts"
    ]

    column_labels = {
        "name": "Название",
        "description": "Описание",
        "source_url": "Ссылка",
        "address": "Адрес",
        "latitude": "Широта",
        "longitude": "Долгота",
        "tags": "Тэги",
        "contacts": "Контакты"
    }

    form_args = {
        "map_object_type": {"default": MapObjectType.organization.value},
    }

    column_searchable_list = [
        'name', 'description'
    ]

    column_sortable_list = [
        'name', 'description', 'source_url', 'address'
    ]

    column_default_sort = [
        ('name', False)
    ]

    def __init__(self, session: Session):
        super().__init__(MapObjectOrganization, session, name='Организации', category='Объекты на карте')
