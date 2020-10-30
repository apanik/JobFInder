from django.db import models
from django.db.models.signals import pre_save

from p7.models import populate_time_info, P7Model
from resources import strings_settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Settings(P7Model):
    facebook_url = models.URLField(verbose_name='Facebook URL')
    linkedin_url = models.URLField(verbose_name='Linkedin URL', blank=True, null=True)
    twitter_url = models.URLField(verbose_name='Twitter URL', blank=True, null=True)
    appstore_url = models.URLField(verbose_name='App Store URL', blank=True, null=True)
    playstore_url = models.URLField(verbose_name='Play Store URL', blank=True, null=True)
    logo_url = models.ImageField(upload_to='logo/', blank=True)
    admin_email = models.CharField(max_length=50)
    support_email = models.CharField(max_length=50)
    sender_email_host = models.CharField(max_length=50)
    sender_email_port = models.CharField(max_length=10)
    email_use_tls = models.BooleanField(default=True)
    no_reply_sender_host_user = models.CharField(max_length=50)
    no_reply_sender_host_password = models.CharField(max_length=50)
    address = models.TextField()
    phone = models.CharField(max_length=50)
    zoom = models.IntegerField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    minimum_profile_completeness = models.IntegerField(blank=True,null=True,default=0)

    class Meta:
        verbose_name = strings_settings.SETTINGS_VERBOSE_NAME
        verbose_name_plural = strings_settings.SETTINGS_VERBOSE_NAME_PLURAL
        db_table = 'settings'

    def __str__(self):
        return self.facebook_url


pre_save.connect(populate_time_info, sender=Settings)
