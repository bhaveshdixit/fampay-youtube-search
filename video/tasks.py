from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.utils.log import get_task_logger
from datetime import datetime

from video import models as video_models, utils as video_utils

logger = get_task_logger(__name__)


@shared_task(name="fetch_latest_videos")
def fetch_latest_video_from_youtube():
    """
    Our task to fetch latest videos from YouTube API and store them in our database
    """

    current_latest_video = video_models.Video.objects.order_by("-published_at").first()
    current_latest_video_published_at = None

    if current_latest_video:
        current_latest_video_published_at = current_latest_video.published_at
    else:
        # We will be using a fallback value if no videos are stored in our database
        current_latest_video_published_at = datetime(2000, 1, 1)

    try:
        latest_videos = video_utils.get_videos_from_youtube(
            current_latest_video_published_at
        )
    except Exception as e:
        logger.error(e)
        return

    video_objects = [video_models.Video(**video) for video in latest_videos]

    # We will be using bulk_create to create multiple objects in a single query
    video_models.Video.objects.bulk_create(video_objects)

    return "Success"
