from rest_framework import serializers
from .models import Devotional


class DevotionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devotional
        fields = '__all__'
