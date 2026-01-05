from rest_framework import serializers
from .models import Activity, ActivityType


class ActivityTypeSerializer(serializers.ModelSerializer):
    total = serializers.IntegerField(read_only=True)

    class Meta:
        model = ActivityType
        fields = ['id', 'name', 'total']


class ActivitySerializer(serializers.ModelSerializer):
    activity_type = ActivityTypeSerializer(read_only=True)
    activity_type_id = serializers.PrimaryKeyRelatedField(
        queryset=ActivityType.objects.all(),
        source='activity_type',
        write_only=True
    )

    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Activity
        fields = [
            'id',
            'activity_type',
            'activity_type_id',
            'created_by',
            'description',
            'photo',
            'created_at',
        ]
