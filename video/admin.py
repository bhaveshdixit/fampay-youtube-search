from django.contrib import admin

from video import models as video_models

admin.site.register(video_models.Video)
admin.site.register(video_models.APIKey)
