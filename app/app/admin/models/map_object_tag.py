from flask_admin.contrib.sqla import ModelView
from sqlalchemy.orm import Session

from app.models import MapObjectTag


class MapObjectTagView(ModelView):
    can_set_page_size = True

    column_list = [
        "name",
        'parent',
        "children",
        "id",
        "parent_id"
    ]
    column_labels = {
        "name": "Название",
        "parent": "Родитель",
        "children": "Дети",
    }

    form_columns = [
        "name",
        "parent"
    ]

    column_default_sort = [('parent_id', False), ('id', False)]

    def __init__(self, session: Session):
        super().__init__(MapObjectTag, session, name='Тэги', category='Система', endpoint='tags')
