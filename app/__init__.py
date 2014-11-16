__author__ = 'erik'
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from app.views.user_page_view import user_page
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_principal import Principal, Permission, RoleNeed
from flask_admin import Admin

app = Flask(__name__, static_folder='static')
app.config.from_object('config')
app.register_blueprint(user_page)

principal = Principal(app)
admin_permission = Permission(RoleNeed('admin'))


lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from views import views
from app.models.user import User
from app.models.session import Session
from app.models.userdata import UserDataDB
from app.models.roles import Role


from app.views.admin_view import UserSettingsView, RoleSettingsView

admin = Admin(app, name='Admin', base_template='my_admin.html')
admin.add_view(UserSettingsView(db.session))
admin.add_view(RoleSettingsView(db.session))


