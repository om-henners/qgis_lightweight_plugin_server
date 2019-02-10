"""
Custom URL type converters
"""
from werkzeug.routing import BaseConverter


class VersionConverter(BaseConverter):

    regex = r'\d+\.\d+'

    def to_python(self, value):
        return (int(i) for i in value.split('.'))

    def to_url(self, values):
        return '.'.join(super().to_url(value) for value in values)

