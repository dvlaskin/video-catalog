from . import models


def get_all_video_items():
    """
    Retrieves all video items from the database.

    Returns:
        QuerySet: A QuerySet containing all video items.
    """
    return models.VideoItem.objects.all()