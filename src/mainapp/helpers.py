import os

from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site

from . import database_queries, openCV_helpers


def get_current_site_name(request) -> str:
    current_site = get_current_site(request)
    site_domain = current_site.domain

    return f"http://{site_domain}"


def create_thumbnail(video_link: str) -> str:
    thumbnail_file_path = ''
    folder_path = os.path.join(settings.BASE_DIR, settings.THUMBNAILS_FOLDER) 
    create_folder_if_not_exists(folder_path)

    thumbnail_file_path = openCV_helpers.create_thumbnail(video_link, folder_path)

    return thumbnail_file_path


def create_folder_if_not_exists(folder_path: str) -> str:
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' created.")
    else:
        print(f"Folder '{folder_path}' already exists.")
    return folder_path


def remove_unused_thumbnails():
    # Set the path to the media folder
    folder_path = os.path.join(settings.BASE_DIR, settings.THUMBNAILS_FOLDER)

    # Create the media folder if it does not exist
    create_folder_if_not_exists(folder_path)

    # Get a list of all files in the media folder
    thumbnail_files = os.listdir(folder_path)

    # Get a list of all thumbnail files from database
    thumbnail_records = database_queries.get_all_video_items()

    # Get list file name from thumbnail records
    thumbnail_file_names = [record.Thumbnail for record in thumbnail_records]

    for thumbnail_file in thumbnail_files:
        file_path = os.path.join(settings.MEDIA_ROOT, thumbnail_file)

        if os.path.isfile(file_path) and os.path.join(settings.THUMBNAILS_FOLDER, thumbnail_file) not in thumbnail_file_names:
            try:
                print(f"Removing unused thumbnail file: {thumbnail_file}")
                os.remove(file_path)
            except:
                print(f"Error: Could not remove file: {file_path}")
    return

def remove_unused_videos():
    # Set the path to the media folder
    folder_path = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT, settings.VIDEO_FOLDER)

    # Create the video folder if it does not exist
    create_folder_if_not_exists(folder_path)

    # Get a list of all files in the media folder
    video_files = os.listdir(folder_path)

    # Get a list of all video files from database
    video_records = database_queries.get_all_video_items()

    # Get list file name from thumbnail records
    video_file_names = [record.VideoFile.name for record in video_records]

    for video_file in video_files:
        file_path = os.path.join(settings.MEDIA_ROOT, settings.VIDEO_FOLDER, video_file)

        if os.path.isfile(file_path) and os.path.join(settings.VIDEO_FOLDER, video_file) not in video_file_names:
            try:
                print(f"Removing unused video file: {video_file}")
                os.remove(file_path)
            except:
                print(f"Error: Could not remove file: {file_path}")
    return