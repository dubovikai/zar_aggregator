from flask_admin.contrib.sqla import ModelView
from sqlalchemy.orm import Session

from app.models import MapObjectAttraction
from app.schemas.map_object import MapObjectType


class MapObjectAttractionView(ModelView):

    can_set_page_size = True

    column_list = [
        "name",
        "description",
        "source_url_vk",
        "source_id_vk",
        "address",
        "latitude",
        "longitude",
        "tags"
    ]

    column_labels = {
        "name": "Название",
        "description": "Описание",
        "source_url_vk": "Ссылка",
        "source_id_vk": "source_id",
        "address": "Адрес",
        "latitude": "Широта",
        "longitude": "Долгота",
        "tags": "Тэги"
    }

    form_args = {
        "map_object_type": {"default": MapObjectType.attraction.value}
    }

    form_columns = [
        "name",
        "description",
        "source_url_vk",
        "source_id_vk",
        "address",
        "latitude",
        "longitude",
        "tags"
    ]

    column_searchable_list = [
        'name', 'description'
    ]

    column_sortable_list = [
        'name', 'description', 'source_id_vk', 'source_url_vk', 'address'
    ]

    column_default_sort = 'name'

    def __init__(self, session: Session):
        super().__init__(MapObjectAttraction, session, name='Достопримечательности', category='Объекты на карте', endpoint='events')
