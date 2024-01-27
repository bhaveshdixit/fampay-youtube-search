from django.urls import path

from search import views as search_views

app_name = 'search'


urlpatterns = [ 
    path('videos/', search_views.VideoListView.as_view(), name='video-list'),
    path('videos/search/', search_views.VideoSearchView.as_view(), name='video-search'),
]
