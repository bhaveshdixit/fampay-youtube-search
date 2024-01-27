from rest_framework import serializers as rest_serializers

from video import models as video_models


class VideoSerializer(rest_serializers.ModelSerializer):
    """
    Serializer to serilaizer Videos Instance
    """
    created_at = rest_serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    updated_at = rest_serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    published_at = rest_serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = video_models.Video
        fields = '__all__'

class APIKeySerializer(rest_serializers.ModelSerializer):
    """
    Serializer to serilaizer APIKey Instance
    """
    created_at = rest_serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    updated_at = rest_serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    next_available_on = rest_serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = video_models.APIKey
        fields = '__all__'
