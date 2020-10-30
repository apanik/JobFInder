from ckeditor.fields import RichTextField
from django.db import models
from django.db.models.signals import pre_save

from p7.models import P7Model, populate_time_info
from resources import strings_job

class CareerAdvice(P7Model):
    title = models.CharField(max_length=50)
    short_description = models.TextField()
    description = RichTextField()
    author = models.CharField(max_length=50)
    thumbnail_image = models.ImageField(upload_to='images/', null=True)
    featured_image = models.ImageField(upload_to='images/', blank=True, null=True)
    posted_at = models.DateTimeField(blank=False,null=False)


    class Meta:
        verbose_name = strings_job.CAREER_VERBOSE_NAME
        verbose_name_plural = strings_job.CAREER_VERBOSE_NAME_PLURAL
        db_table = 'career_advices'

    def __str__(self):
        return self.title

pre_save.connect(populate_time_info, sender=CareerAdvice)
