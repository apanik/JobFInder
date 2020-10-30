from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase
from .models import Testimonial


#TESTIMONIAL_TEST#
class TestimonailTest(TestCase):
    def test_when_everything_required_is_given_should_pass(self):
        testimonial = Testimonial(client_name='XYZ',comment='This is a comment')
        try:
            testimonial.full_clean()
        except:
            self.fail()

    def test_when_name_is_more_than_max_length_should_raise_error(self):
        testimonial = Testimonial(client_name='Lorem Ipsum is simply dummy text of the printing and typesetting industry. '
                           'Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, '
                           'when an unknown printer took a galley of type and scrambled it to make a type '
                           'specimen book. It has survived not only five centuries, but also the leap into '
                           'electronic typesetting, remaining essentially unchanged. It was popularised in '
                           'the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, '
                           'and more recently with desktop publishing software like Aldus PageMaker '
                           'including versions of Lorem Ipsum.', comment='This is a comment')
        with self.assertRaises(ValidationError):
            testimonial.full_clean()

    def test__when_testimonial_name_duplicate__should_raise_error(self):
        t1 = Testimonial(client_name="Xyz")
        t2 = Testimonial(client_name="Xyz")
        with self.assertRaises(IntegrityError):
            t1.save()
            t2.save()

    def test_when_name_is_null_should_raise_error(self):
        testimonial = Testimonial(client_name = "This is a comment")
        with self.assertRaises(ValidationError):
            testimonial.full_clean()

    def test_when_comment_is_null_should_raise_error(self):
        testimonial = Testimonial(client_name = "name")
        with self.assertRaises(ValidationError):
            testimonial.full_clean()

    def test_when_name_and_comment_is_null_should_raise_error(self):
        testimonial = Testimonial()
        with self.assertRaises(ValidationError):
            testimonial.full_clean()

    def test_when_name_is_blank_should_raise_error(self):
        testimonial = Testimonial(client_name='', comment='This is comment')
        with self.assertRaises(ValidationError):
            testimonial.full_clean()

    def test_when_comment_is_blank_should_raise_error(self):
        testimonial = Testimonial(client_name='xyz', comment='')
        with self.assertRaises(ValidationError):
            testimonial.full_clean()

    def test_when_name_and_comment_both_is_blank_should_raise_error(self):
        testimonial = Testimonial(client_name='', comment='')
        with self.assertRaises(ValidationError):
            testimonial.full_clean()

#TESTIMONIAL_TEST#