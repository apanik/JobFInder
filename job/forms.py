from django import forms

from job.models import City
from resources import strings_job


class JobModelForm(forms.ModelForm):
    job_city = forms.ModelChoiceField(required=False, queryset=City.objects.all())
    company_city = forms.ModelChoiceField(required=False, queryset=City.objects.all())
    status = forms.ChoiceField(choices= strings_job.JOB_STATUSES)


class CompanyModelForm(forms.ModelForm):
    city = forms.ModelChoiceField(required=False, queryset=City.objects.all())


class JobApplicationModelForm(forms.ModelForm):
    def job_link(self, obj):
        """My Custom Title"""
        ...

    job_link.short_description = 'Job Link'

