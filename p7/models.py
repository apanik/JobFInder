from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

class P7Model(models.Model):
    created_by = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(null=True)
    created_from = models.CharField(max_length=255, null=True)
    modified_by = models.CharField(max_length=255, null=True)
    modified_at = models.DateTimeField(null=True)
    modified_from = models.CharField(max_length=255, null=True)
    is_archived = models.BooleanField(default=False)
    archived_by = models.CharField(max_length=255, null=True)
    archived_at = models.DateTimeField(null=True)
    archived_from = models.CharField(max_length=255, null=True)

    class Meta:
        abstract = True



def populate_time_info(sender, instance, *args, **kwargs):
    if instance._state.adding:
        instance.created_at = timezone.now()
    else:
        instance.modified_at = timezone.now()
        if instance.is_archived and not instance.archived_at:
            instance.archived_at = timezone.now()


def populate_user_info(request, instance, is_changed, is_archived):
    if is_changed:
        instance.modified_by = request.user.id
        instance.modified_from = get_user_address(request)
        if is_archived:
            instance.archived_by = request.user.id
            instance.archived_from = get_user_address(request)
    else:
        instance.created_by = request.user.id
        instance.created_from = get_user_address(request)


def populate_user_info_request(request, is_changed, is_archived):
    if is_changed:
        request.data['modified_by'] = request.user.id
        request.data['modified_from'] = get_user_address(request)
        if is_archived:
            request.data['archived_by'] = request.user.id
            request.data['archived_from'] = get_user_address(request)
    else:
        request.data['created_by'] = request.user.id
        request.data['created_from'] = get_user_address(request)


def is_professional(user):
    return user.groups.filter(name='Professional').exists()


def is_company(user):
    return user.groups.filter(name='Company').exists()

def is_moderator(user):
    return user.groups.filter(name='Moderator').exists()

def is_professional_registered(email):
    user = User.objects.filter(email=email).first()
    if user:
        return is_professional(user)
    else:
        return False


def get_user_address(request):
    http_header = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get('HTTP_X_FORWARDED_FOR') is not None else request.META.get('REMOTE_ADDR')
    return http_header


def populate_user_info_querydict(request, data, is_changed, is_archived):
    if is_changed:
        data['modified_by'] = request.user.id
        data['modified_from'] = get_user_address(request)
        if is_archived:
            data['archived_by'] = request.user.id
            data['archived_from'] = get_user_address(request)
    else:
        data['created_by'] = request.user.id
        data['created_from'] = get_user_address(request)
