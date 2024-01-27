from django.contrib import admin

from video import models as video_models


class VideoAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at", "published_at"]


class APIKeyAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at", "next_available_on"]


admin.site.register(video_models.Video, VideoAdmin)
admin.site.register(video_models.APIKey, APIKeyAdmin)
