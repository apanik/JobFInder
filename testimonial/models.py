from django.db import models
from django.db.models.signals import pre_save

from p7.models import P7Model, populate_time_info
from resources import strings_testimonial


class Testimonial(P7Model):
    client_name = models.CharField(max_length=255,unique=True)
    comment = models.TextField()
    profile_picture = models.ImageField(upload_to='testimonials/',verbose_name='Profile Picture',blank=True)

    class Meta:
        verbose_name = strings_testimonial.TESTIMONIAL_VERBOSE_NAME
        verbose_name_plural = strings_testimonial.TESTIMONIAL_VERBOSE_NAME_PLURAL
        db_table = 'testimonials'

    def __str__(self):
        return self.client_name

pre_save.connect(populate_time_info, sender=Testimonial)
