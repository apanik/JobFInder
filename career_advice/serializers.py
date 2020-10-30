from rest_framework import serializers
from career_advice.models import *

class CareerAdviceSerializer(serializers.ModelSerializer):
    thumbnail_image = serializers.CharField(source='thumbnail_image.url')
    featured_image = serializers.CharField(source='featured_image.url')
    class Meta:
        model = CareerAdvice
        fields = '__all__'