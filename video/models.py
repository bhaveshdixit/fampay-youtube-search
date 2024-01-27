from django.db import models
from django.utils import timezone

from common import models as common_models

class Video(common_models.DatesTimeModel):
    """
    Stores video data from YouTube API
    """
    video_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000)
    published_at = models.DateTimeField()
    thumbnail_url = models.CharField(max_length=100)

    def __str__(self) -> str:
        return '{}  -  {}'.format(self.title, self.published_at.strftime('%d-%m-%Y %H:%M:%S'))
    

class APIKey(common_models.DatesTimeModel):
    """ 
    Stores API Key for YouTube API 
    """

    key = models.CharField(max_length=100, unique=True)
    next_available_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.key
