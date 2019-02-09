"""
QGIS Plugin models.

Adapted from qgis-app/plugins/models.py in https://github.com/qgis/QGIS-Django
"""
from datetime import datetime

from sqlalchemy_utils import EmailType, URLType

from .. import db
from ..models import User
from .types import Version


class PluginsOwners(db.Model):
    """
    Join table between plugins and owners
    """
    __tablename__ = 'plugins_owners'

    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    plugin_id = db.Column('plugin_id', db.Integer, db.ForeignKey('plugin.id'))


# TODO: Query mixins to match the queries from the Django plugin

class Plugin(db.Model):
    """
    QGIS Plugin
    """
    __tablename__ = 'plugin'

    id = db.Column(db.Integer, primary_key=True)

    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    modified_on = db.Column(db.DateTime, default=datetime.utcnow)

    # owners
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    creator = db.relationship(User, backref=db.backref('plugins'))

    author = db.Column(db.Unicode)  # This is the plugin's original author, if different from the uploader, this field will appear in the XML and in the web GUI
    email = db.Column(EmailType)
    homepage = db.Column(URLType)

    # Support
    repository = db.Column(URLType)
    tracker = db.Column(URLType)

    owners = db.relationship(
        'Role',
        secondary='plugins_owners',
        backref=db.backref('plugins', lazy='dynamic')
    )

    # name, desc etc.
    package_name = db.Column(db.String(256), unique=True, nullable=False)
    name = db.Column(db.String(256), unique=True, nullable=False)
    description = db.Column(db.UnicodeText)
    about= db.Column(db.UnicodeText)

    icon = db.Column(URLType)  # the URL will depend on the upload method - flask upload or s3

    # downloads (soft trigger from versions)
    downloads = db.Column(db.Integer, default=0)

    # Flags
    featured = db.Column(db.Boolean, default=True, index=True)
    deprecated = db.Column(db.Boolean, default=True, index=True)

    # True if the plugin has a server interface
    server = db.Column(db.Boolean, default=True, index=True)


    def __repr__(self):
        return f'<Plugin "{self.name}">'


class PluginVersion(db.Model):
    """
    Plugin versions
    """
    __tablename__ = 'plugin_version'

    id = db.Column(db.Integer, primary_key=True)

    # link to parent
    plugin_id = db.Column(db.Integer, db.ForeignKey('plugin.id'), nullable=False)
    plugin = db.relationship(Plugin, backref=db.backref('plugin_versions'))

    # dates
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    # download counter
    downloads = db.Column(db.Integer, default=0)
    # owners
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    creator = db.relationship(User, backref=db.backref('plugin_versions'))

    # version info, the first should be read from plugin
    min_qg_version = db.Column(Version(length=32, fillchar='0', level=2, force_zero=True), index=True)
    max_qg_version = db.Column(Version(length=32, fillchar='0', level=2, force_zero=True), nullable=True, index=True)
    version = db.Column(Version(length=32, fillchar='0'), index=True)
    changelog = db.Column(db.UnicodeText)

    # the file!
    package = db.Column(URLType)  # the URL will depend on the upload method

    # Flags: checks on unique current/experimental are done in save() and possibly in the views
    experimental = db.Column(db.Boolean, default=False, index=True, nullable=False)
    approved = db.Column(db.Boolean, default=True, index=True, nullable=False)
    external_deps = db.Column(db.String(512), nullable=True)


    def __repr__(self):
        return f'<PluginVersion "{self.plugin.name}" "{self.version}">'
