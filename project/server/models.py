"""
User models based on standard models from Flask Security
"""
from flask_security import UserMixin, RoleMixin
from geoalchemy2 import Geography

from . import db


class RolesUsers(db.Model):
    """
    Mapping between roles and users
    """
    __tablename__ = 'roles_users'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column('user_id', db.Integer(), db.ForeignKey('user.id'))
    role_id = db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))


class Role(db.Model, RoleMixin):
    """
    Standard DB roles table
    """
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    description = db.Column(db.String)

    def __repr__(self):
        return "<Role {0}>".format(self.name)


class User(db.Model, UserMixin):
    """
    User model based on Flask-Security, but it includes:

    - screen_name - the name of the user on screen (public)
    - full_name - the full name of the user
    - preferred_address - the preferred form of address for the user
    """
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)

    # Modifyable user properties
    email = db.Column(db.Unicode, unique=True, nullable=False)
    screen_name = db.Column(db.Unicode, unique=True, nullable=False)
    full_name = db.Column(db.Unicode, nullable=False)
    preferred_address = db.Column(db.Unicode)
    password = db.Column(db.Unicode)

    # location
    geog = db.Column(Geography(geometry_type='POINT', srid=4326, spatial_index=True), nullable=True, index=True)

    # user metadata
    last_login_at = db.Column(db.DateTime)
    current_login_at = db.Column(db.DateTime)
    last_login_ip = db.Column(db.String)
    current_login_ip = db.Column(db.String)
    login_count = db.Column(db.Integer)
    active = db.Column(db.Boolean)
    confirmed_at = db.Column(db.DateTime)

    roles = db.relationship(
        'Role',
        secondary='roles_users',
        backref=db.backref('users', lazy='dynamic')
    )

    def __repr__(self):
        return "<User {0}>".format(self.email)
