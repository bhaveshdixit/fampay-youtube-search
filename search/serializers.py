from rest_framework import serializers as rest_serializers

from search import models as search_models


class VideoSerializer(rest_serializers.ModelSerializer):

    created_at = rest_serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    updated_at = rest_serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = search_models.Video
        fields = '__all__'
