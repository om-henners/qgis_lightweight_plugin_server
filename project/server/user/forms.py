"""
Custom form for user registration parameters
"""
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_security.forms import RegisterForm


class ExtendedRegisterForm(RegisterForm):
    """
    Add the extra fields for the user object
    """
    screen_name = StringField('Screen name', [DataRequired()])
    full_name = StringField('Full name', [DataRequired()])
    preferred_address = StringField('Preferred form of address')
