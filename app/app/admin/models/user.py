from flask_admin.contrib.sqla import ModelView
from sqlalchemy.orm import Session

from app.models import User


class UserView(ModelView):
    can_create = False
    column_list = [
        "full_name",
        "email",
        "vk_uid",
        "is_active",
        "is_superuser"
    ]

    form_columns = [
        "full_name",
        "email",
        "is_active",
        "is_superuser"
    ]

    column_labels = {
        "full_name": "Имя",
        "vk_uid": "VK ID",
        "is_active": "Активный",
        "is_superuser": "Админ"
    }
    column_searchable_list = [
        'full_name', 'vk_uid', 'email'
    ]

    column_sortable_list = column_list

    def __init__(self, session: Session):
        super().__init__(User, session, name='Пользователи')
