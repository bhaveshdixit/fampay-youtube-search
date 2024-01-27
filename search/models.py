from django.db import models

class Video(models.Model):
    """
    Stores video data from YouTube API
    """
    video_id = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000)
    published_at = models.DateTimeField()
    thumbnail = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return '{}  -  {}'.format(self.title, self.published_at.strftime('%d-%m-%Y %H:%M:%S'))
