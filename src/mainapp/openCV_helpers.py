import os
import uuid

import cv2
from django.conf import settings


def create_thumbnail(video_file_path: str, folder_path: str) -> str:
    
    thumbnail_file_path = ''
    cap = cv2.VideoCapture(video_file_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return thumbnail_file_path
    
    # Set the desired time in seconds (e.g., 15 seconds) for frame screenshot
    target_time_seconds = 15

    # Calculate the target frame number based on the frame rate
    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    target_frame_number = int(target_time_seconds * frame_rate)

    # Move to the desired frame in the video
    cap.set(cv2.CAP_PROP_POS_FRAMES, target_frame_number)

    ret, frame = cap.read()

    if ret:
        # Customize the filename
        thumbnail_file = f'thumbnail_{uuid.uuid4()}.png'
        cv2.imwrite(os.path.join(folder_path, thumbnail_file), frame)

        thumbnail_file_path = os.path.join(settings.THUMBNAILS_FOLDER, thumbnail_file)
        
        print(f"Frame saved at {thumbnail_file_path}.")
    else:
        print(f"Error: Could not capture frame at {target_time_seconds} seconds.")

    cap.release()
    cv2.destroyAllWindows()
    return thumbnail_file_path