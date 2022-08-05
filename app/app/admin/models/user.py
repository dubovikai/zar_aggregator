from flask_admin.contrib.sqla import ModelView
from sqlalchemy.orm import Session

from app.models import User


class UserView(ModelView):
    can_create = False
    column_exclude_list = ['hashed_password']
    form_excluded_columns = ['hashed_password']

    def __init__(self, session: Session):
        super().__init__(User, session, name='Пользователи')
