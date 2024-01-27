import requests
from datetime import datetime, timedelta

from django.conf import settings

from search import models as search_models

def get_active_api_keys():
    """
    Utility to fetch active API keys from database
    """
    return search_models.APIKey.objects.filter(next_available_on__lte=datetime.now())

def get_params(key, publishedAfter):
    """
    Utility to fetch params for YouTube API
    """
    return {
        'part': 'snippet',
        'q': settings.SEARCH_KEY,
        'type': 'video',
        'key': key,
        'maxResults': 5,
        'publishedAfter': publishedAfter.strftime("%Y-%m-%dT%H:%M:%SZ"), # format: 2021-09-25T00:00:00Z RFC 3339 
    }

def get_videos_from_youtube(publishedAfter):
    """
    Utility to fetch videos from YouTube API given a publishedAfter date
    """
    
    url = 'https://www.googleapis.com/youtube/v3/search'
    response = None
    active_keys = get_active_api_keys()

    for key in active_keys:
        params = get_params(key, publishedAfter)
        response = requests.get(url, params=params)
        if response and response.ok:
            break
        else:
            key.next_available_on = datetime.now() + timedelta(days=1)
            key.save()

    
    if not response or not response.ok:
        # If all keys are exhausted, we will return empty list
        raise Exception('No active API keys found')

    # for key in get_active_api_keys():
    #     params = get_params(key.key, publishedAfter)
    #     response = requests.get(url, params=params)
    #     if response.status_code == 200:
    #         break
    # print("🐍 File: search/utils.py | Line: 19 | get_videos_from_youtube ~ publishedAfter.isoformat()+Z",publishedAfter.isoformat()+"Z")

    print("🐍 File: search/utils.py | Line: 22 | get_videos_from_youtube ~ response.json()",response.json())
    items = response.json()['items']
    return [
        {
            'video_id': item['id']['videoId'],
            'title': item['snippet']['title'],
            'description': item['snippet']['description'],
            'published_at': item['snippet']['publishedAt'],
            'thumbnail': item['snippet']['thumbnails']['default']['url'],
        } for item in items
    ]

