from flask_admin.contrib.sqla import ModelView
from sqlalchemy.orm import Session

from app.models import MapObjectEvent
from app.schemas.map_object import MapObjectType


class MapObjectEventView(ModelView):
    can_set_page_size = True

    column_list = [
        "name",
        "description",
        "source_url",
        "address",
        "latitude",
        "longitude",
        "tags",
        "start_datetime",
        "end_datetime",
        "duration",
        "status",
    ]

    column_labels = {
        "name": "Название",
        "description": "Описание",
        "source_url": "Ссылка",
        "address": "Адрес",
        "latitude": "Широта",
        "longitude": "Долгота",
        "tags": "Тэги",
        "start_datetime": "Начало",
        "end_datetime": "Конец",
        "duration": "Длительность, сек",
        "status": "Статус"
    }

    form_args = {
        "map_object_type": {"default": MapObjectType.event.value}
    }

    form_columns = [
        "name",
        "description",
        "source_url",
        "address",
        "latitude",
        "longitude",
        "tags",
        "start_datetime",
        "duration",
        "status"
    ]

    column_searchable_list = [
        'name', 'description'
    ]

    column_sortable_list = [
        'name',
        'description',
        'source_url',
        'address',
        'start_datetime',
        'end_datetime',
        'duration',
        'status'

    ]

    column_default_sort = ('start_datetime', True)

    def __init__(self, session: Session):
        super().__init__(MapObjectEvent, session, name='Мероприятия', category='Объекты на карте')
