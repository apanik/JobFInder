import unittest

from .validators import check_valid_password, check_valid_phone_number


class ValidatorTest(unittest.TestCase):
    def test__check_valid_password__when_alphabet_and_number_only__should_pass(self):
        try:
            check_valid_password('111a2111')
        except:
            self.fail()

    def test__check_valid_phone_number__when_number_only__should_pass(self):
        try:
            check_valid_phone_number('01626296800')
        except:
            self.fail()

