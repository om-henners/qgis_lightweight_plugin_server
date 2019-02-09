"""
Views for plugins
"""
from flask import Blueprint

from .models import Plugin, PluginVersion


plugin_blueprint = Blueprint("plugin", __name__)
