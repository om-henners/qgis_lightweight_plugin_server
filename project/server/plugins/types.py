"""
Custom data types
"""
import re

from sqlalchemy.types import TypeDecorator, Unicode


VERSION_RE = re.compile(r'(^|(?<=\.))0+(?!(\.|$|-))|\.#+')


class Version(TypeDecorator):
    """
    Custom data type for version types so they can be stored in the DB

    From `vjust` in qgis-app/plugins/models.py, in
    https://github.com/qgis/QGIS-Django

    Normalize a dotted version string.

    1.12 becomes : 1.    12
    1.1  becomes : 1.     1


    if force_zero=True and level=2:

    1.12 becomes : 1.    12.     0
    1.1  becomes : 1.     1.     0
    """

    impl = Unicode

    def __init__(self, *args, level=3, delim='.', bitsize=3, fillchar=' ', force_zero=False, **kwargs):
        """
        Parameters for the function to transform the version number
        """
        self._level = level
        self._delim = delim
        self._bitsize = bitsize
        self._fillchar = fillchar
        self._force_zero = force_zero

        super().__init__(*args, **kwargs)

    def process_bind_param(self, value, dialect):
        """
        Process the incoming version into a normalised string

        This is essentially the `vjust` function from the original.
        """
        if not value:
            return value
        nb = value.count(self._delim)
        if nb < self._level:
            if self._force_zero:
                value += (self._level - nb) * (self._delim + '0')
            else:
                value += (self._level - nb) * self._delim
        parts = []
        for v in value.split(self._delim)[:self._level + 1]:
            if not v:
                parts.append(v.rjust(self._bitsize, '#'))
            else:
                parts.append(v.rjust(self._bitsize, self._fillchar))
        return self._delim.join(parts)

    def process_result_value(self, value, dialect):
        """
        Get rid of the delimited spaces
        """
        if not value:
            return value
        return VERSION_RE.sub('', value)
