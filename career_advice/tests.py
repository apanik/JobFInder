from django.core.exceptions import ValidationError
from career_advice.models import CareerAdvice
from django.test import TestCase

# Create your tests here.

#CAREER_ADVICE_TEST#


class CareerAdviceTest(TestCase):
    def test_when_everything_is_given_should_pass(self):
        career_advice = CareerAdvice(title='Lorem Ipsum is simply dummy text of the printing and typesetting industry.',
                                      description='Lorem Ipsum is simply dummy text of the printing and typesetting industry. '
                             'Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, '
                             'when an unknown printer took a galley of type and scrambled it to make a type '
                             'specimen book. It has survived not only five centuries, but also the leap into '
                             'electronic typesetting, remaining essentially unchanged. It was popularised in '
                             'the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, '
                             'and more recently with desktop publishing software like Aldus PageMaker '
                             'including versions of Lorem Ipsum. Lorem Ipsum is simply dummy text of the printing and typesetting industry. '
                             'Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, '
                             'when an unknown printer took a galley of type and scrambled it to make a type '
                             'specimen book. It has survived not only five centuries, but also the leap into '
                             'electronic typesetting, remaining essentially unchanged. It was popularised in '
                             'the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, '
                             'and more recently with desktop publishing software like Aldus PageMaker '
                             'including versions of Lorem Ipsum. ', author= 'Abc Hossian')
        try:
            career_advice.full_clean()
        except:
            self.fail()

    def test_when_title_is_null_should_raise_error(self):
        career_advice = CareerAdvice()
        with self.assertRaises(ValidationError):
            career_advice.full_clean()

    def test_when_title_is_blank_should_raise_error(self):
        career_advice = CareerAdvice(title=' ')
        with self.assertRaises(ValidationError):
            career_advice.full_clean()

    def test_when_title_is_more_than_max_length_should_raise_error(self):
        career_advice = CareerAdvice(title='Lorem Ipsum is simply dummy text of the printing and typesetting industry. '
                             'Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, '
                             'when an unknown printer took a galley of type and scrambled it to make a type '
                             'specimen book. It has survived not only five centuries, but also the leap into '
                             'electronic typesetting, remaining essentially unchanged. It was popularised in '
                             'the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, '
                             'and more recently with desktop publishing software like Aldus PageMaker '
                             'including versions of Lorem Ipsum. ')
        with self.assertRaises(ValidationError):
            career_advice.full_clean()

    def test_when_description_is_null_should_raise_error(self):
        career_advice = CareerAdvice()
        with self.assertRaises(ValidationError):
            career_advice.full_clean()

    def test_when_description_is_blank_should_raise_error(self):
        career_advice = CareerAdvice(description=' ')
        with self.assertRaises(ValidationError):
            career_advice.full_clean()

    def test_when_author_is_null_should_raise_error(self):
        career_advice = CareerAdvice()
        with self.assertRaises(ValidationError):
            career_advice.full_clean()

    def test_when_author_is_blank_should_raise_error(self):
        career_advice = CareerAdvice(author=' ')
        with self.assertRaises(ValidationError):
            career_advice.full_clean()

    def test_when_author_is_more_than_max_length_should_raise_error(self):
        career_advice = CareerAdvice(author='Lorem Ipsum is simply dummy text of the printing and typesetting industry. '
                             'Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, '
                             'when an unknown printer took a galley of type and scrambled it to make a type '
                             'specimen book. It has survived not only five centuries, but also the leap into '
                             'electronic typesetting, remaining essentially unchanged. It was popularised in '
                             'the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, '
                             'and more recently with desktop publishing software like Aldus PageMaker '
                             'including versions of Lorem Ipsum. ')
        with self.assertRaises(ValidationError):
            career_advice.full_clean()


#CAREER_ADVICE_TEST#