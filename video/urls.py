from django.urls import path

from video import views as video_views

app_name = 'video'


urlpatterns = [
    path('', video_views.VideoListView.as_view(), name='video-list'),
    path('search/', video_views.VideoSearchView.as_view(), name='video-search'),
    path('api-key/', video_views.APIKeyView.as_view(), name='api-key'),
]
