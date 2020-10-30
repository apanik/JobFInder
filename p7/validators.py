import re

from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
from django.utils.translation import ugettext as _

from resources.strings import DEFAULT_MIN_LENGTH_ERROR, DEFAULT_INVALID_PASSWORD_ERROR, \
    DEFAULT_INVALID_PHONE_NUMBER_ERROR


# class NumberValidator(object):
#     def validate(self, password, user=None):
#         if not re.findall('\d', password):
#             raise ValidationError(
#                 _("The password must contain at least 1 digit, 0-9."),
#                 code='password_no_number',
#             )
#
# class CharacterValidator(object):
#     def validate(self, password, user=None):
#         if not re.findall('[A-Za-z]', password):
#             raise ValidationError(
#                 _("The password must contain at least 1 character"),
#                 code='password_no_upper',
#             )

class MinLengthValidator(BaseValidator):
    def compare(self, a, b):
        if len(str(a)) < b :
            raise ValidationError(DEFAULT_MIN_LENGTH_ERROR.format(b))

def check_valid_password(value):
    # regex = re.compile('[A-Za-z0-9]')
    if not re.findall("(?=.*?[0-9])(?=.*?[A-Za-z]).+", value):
        raise ValidationError(DEFAULT_INVALID_PASSWORD_ERROR)

def check_valid_phone_number(value):
    if not re.findall('^\d{11}$', value):
        raise ValidationError(DEFAULT_INVALID_PHONE_NUMBER_ERROR)

class ResetPasswordValidator(object):
    def validate(self, password, user=None):
        if not re.findall("(?=.*?[0-9])(?=.*?[A-Za-z]).+", password):
            raise ValidationError(
                _(DEFAULT_INVALID_PASSWORD_ERROR),
                code='password_no_symbol',
            )

    def get_help_text(self):
        return _(DEFAULT_INVALID_PASSWORD_ERROR)