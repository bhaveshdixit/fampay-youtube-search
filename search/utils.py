import requests

from django.conf import settings

def get_videos_from_youtube(publishedAfter):
    """
    Utility to fetch videos from YouTube API given a publishedAfter date
    """
    
    url = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        'part': 'snippet',
        'q': settings.SEARCH_KEY,
        'type': 'video',
        'key': settings.SEARCH_API_KEY,
        'maxResults': 5,
        'publishedAfter': publishedAfter.strftime("%Y-%m-%dT%H:%M:%SZ"), # format: 2021-09-25T00:00:00Z RFC 3339 
    }
    print("🐍 File: search/utils.py | Line: 19 | get_videos_from_youtube ~ publishedAfter.isoformat()+Z",publishedAfter.isoformat()+"Z")
    response = requests.get(url, params=params)

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

