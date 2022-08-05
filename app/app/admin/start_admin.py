from app.core.config import settings
from app.api.deps import get_db
from flask import Flask
from flask_admin import Admin
from flask_babelex import Babel

from .register_views import register_views

app = Flask(__name__)
# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.secret_key = settings.SECRET_KEY
app.env = settings.FLASK_ENV

babel = Babel(app)


@babel.localeselector
def get_locale():
    return settings.BABEL_LOCALE


db_generator = get_db()
db = db_generator.__next__()

admin = Admin(app, name=settings.PROJECT_NAME, template_mode='bootstrap3')

register_views(admin, db)


if __name__ == "__main__":
    app.run()
