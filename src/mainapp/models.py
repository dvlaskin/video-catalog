from django.conf import settings
from django.db import models

from . import helpers


class Category(models.Model):
    Name = models.CharField(max_length=250)
    OrderId = models.IntegerField(default=0)
    InActive = models.BooleanField(default=False)


class VideoItem(models.Model):
    Title = models.CharField(max_length=250)
    Description = models.CharField(max_length=1500, blank=True)
    InActive = models.BooleanField(default=False)
    Thumbnail = models.CharField(max_length=150, default='', blank=True)
    VideoFile = models.FileField(upload_to=f'{settings.VIDEO_FOLDER}/', blank=True)

    Categories = models.ManyToManyField(Category)

    def save(self, *args, **kwargs):
        
        self.replace_space_with_low_dash()

        # Call your custom method before saving
        super().save(*args, **kwargs)

        try:
            if self.VideoFile != '' and self.Thumbnail == '':
                self.Thumbnail = helpers.create_thumbnail(self.VideoFile.path)
                self.save()
        except Exception as ex:
            print(f'can not create thumbnail for video {self.Title}')
            print(f'error:\r\n{ex}')

        # remove unused thumbnails
        helpers.remove_unused_thumbnails()
        helpers.remove_unused_videos()

    def replace_space_with_low_dash(self):
        if self.VideoFile != '':
            self.VideoFile.name = self.VideoFile.name.replace(' ', '_')
