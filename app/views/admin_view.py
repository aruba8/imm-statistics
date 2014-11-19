__author__ = 'erik'
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from app.models.user import User
from app.models.roles import Role
from app.models.userdata import UserDataDB


class UserSettingsView(ModelView):
    # Disable model creation
    def __init__(self, session):
        # Just call parent class with predefined model.
        super(UserSettingsView, self).__init__(User, session)

    can_create = False
    column_searchable_list = ['username', 'email']
    form_excluded_columns = ('password', 'roles')
    column_list = ('username', 'email', 'roles')

    def is_accessible(self):
        if hasattr(current_user, 'roles'):
            roles = [role.name for role in current_user.roles]
            if 'admin' in roles:
                return True
        return False


class RoleSettingsView(ModelView):
    # Disable model creation
    def __init__(self, session):
        # Just call parent class with predefined model.
        super(RoleSettingsView, self).__init__(Role, session)

    can_create = True

    def is_accessible(self):
        if hasattr(current_user, 'roles'):
            roles = [role.name for role in current_user.roles]
            if 'super_admin' in roles:
                return True
        return False


class UserDataSettingsView(ModelView):
    # Disable model creation
    can_create = False
    column_searchable_list = ['username']
    # form_excluded_columns = ('roles')
    column_list = ('username', 'stream', 'from_short')

    def __init__(self, session):
        # Just call parent class with predefined model.
        super(UserDataSettingsView, self).__init__(UserDataDB, session, name='UserData')

    def is_accessible(self):
        if hasattr(current_user, 'roles'):
            roles = [role.name for role in current_user.roles]
            if 'admin' in roles:
                return True
        return False
