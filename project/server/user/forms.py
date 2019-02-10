"""
Custom form for user registration parameters
"""
from wtforms import StringField, Field, widgets
from wtforms.validators import DataRequired
from flask_security.forms import RegisterForm


class PointFieldRenderer(Field):
    widget = widgets.HiddenInput()

    def _value(self):
        """
        Assuming there is data, it'll be in the form:

            POINT(x y)

        Strip off the outside of the data, and display to the user.

        :rtype: str
        """
        if self.data:
            return self.data[len('POINT('): -len(')')]
        else:
            return self.data

    def process_formdata(self, valuelist):
        """
        Cheat to make this into a WKT point for easy db insertion
        """
        if valuelist and valuelist[0] not in (None, 'None'):
            self.data = f'POINT({valuelist[0]})'
        else:
            self.data = None


class ExtendedRegisterForm(RegisterForm):
    """
    Add the extra fields for the user object
    """
    screen_name = StringField('Screen name', [DataRequired()])
    full_name = StringField('Full name', [DataRequired()])
    preferred_address = StringField('Preferred form of address')
    geog = PointFieldRenderer('geog')
