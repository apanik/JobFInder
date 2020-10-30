from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import Settings


# from helpers.validators import ONE_INSTANCE_ONLY


# TestCase_SETTINGS#
class SettingsTest(TestCase):
    def test_when_everything_required_is_given_should_pass(self):
        settings = Settings(facebook_url='https://www.facebook.com', appstore_url='https://www.apple.com/store',
                            playstore_url='https://www.google.com/play')
        try:
            settings.full_clean()
        except:
            self.fail()

    def test_when_facebook_url_is_null_should_raise_error(self):
        settings = Settings(appstore_url='https://www.apple.com/store',
                            playstore_url='https://www.google.com/play')
        with self.assertRaises(ValidationError):
            settings.full_clean()

    def test_when_facebook_url_is_blank_should_raise_error(self):
        settings = Settings(facebook_url='', appstore_url='https://www.apple.com/store',
                            playstore_url='https://www.google.com/play')
        with self.assertRaises(ValidationError):
            settings.full_clean()

    def test_when_appstore_url_is_null_should_raise_error(self):
        settings = Settings(facebook_url='https://www.facebook.com',
                            playstore_url='https://www.google.com/play')
        with self.assertRaises(ValidationError):
            settings.full_clean()

    def test_when_appstore_url_is_blank_should_raise_error(self):
        settings = Settings(facebook_url='https://www.facebook.com', appstore_url='',
                            playstore_url='https://www.google.com/play')
        with self.assertRaises(ValidationError):
            settings.full_clean()

    def test_when_playstore_url_is_null_should_raise_error(self):
        settings = Settings(facebook_url='https://www.facebook.com',
                            appstore_url='https://www.apple.com/store')
        with self.assertRaises(ValidationError):
            settings.full_clean()

    def test_when_playstore_url_is_blank_should_raise_error(self):
        settings = Settings(facebook_url='https://www.facebook.com', appstore_url='https://www.apple.com/store',
                            playstore_url='')
        with self.assertRaises(ValidationError):
            settings.full_clean()

    def test_when_not_provide_valid_url_for_facebook_should_raise_error(self):
        settings = Settings(facebook_url='dgddjah', appstore_url='https://www.apple.com/store',
                            playstore_url='https://www.google.com/play')
        with self.assertRaises(ValidationError):
            settings.full_clean()

    def test_when_not_provide_valid_url_for_linkedin_should_raise_error(self):
        settings = Settings(facebook_url='https://www.facebook.com', appstore_url='https://www.apple.com/store',
                            playstore_url='https://www.google.com/play', linkedin_url='dgddjah')
        with self.assertRaises(ValidationError):
            settings.full_clean()

    def test_when_not_provide_valid_url_for_twitter_should_raise_error(self):
        settings = Settings(facebook_url='https://www.facebook.com', appstore_url='https://www.apple.com/store',
                            playstore_url='https://www.google.com/play', twitter_url='dgddjah')
        with self.assertRaises(ValidationError):
            settings.full_clean()

    def test_when_not_provide_valid_url_for_appstore_url_should_raise_error(self):
        settings = Settings(facebook_url='https://www.facebook.com', appstore_url='gghgjf',
                            playstore_url='https://www.google.com/play')
        with self.assertRaises(ValidationError):
            settings.full_clean()

    def test_when_not_provide_valid_url_for_playstore_url_should_raise_error(self):
        settings = Settings(facebook_url='https://www.facebook.com', appstore_url='https://www.apple.com/store',
                            playstore_url='fhsjhfjdh')
        with self.assertRaises(ValidationError):
            settings.full_clean()

# TestCase_SETTINGS#
