import re

from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator

from resources.strings import DEFAULT_MIN_LENGTH_ERROR, DEFAULT_INVALID_CHARACTER_ERROR


def check_valid_chars(value):
    regex = re.compile('[@\\\_!#$%^&*()<>?/\|}{~:, \[\]+.=\'"]')
    if not regex.search(value) == None:
        raise ValidationError(DEFAULT_INVALID_CHARACTER_ERROR)


class MinLengthValidator(BaseValidator):
    def compare(self, a, b):
        if len(str(a)) < b:
            raise ValidationError(DEFAULT_MIN_LENGTH_ERROR.format(b))


