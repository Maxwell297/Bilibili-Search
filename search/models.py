from django.db import models
from django.urls import reverse
# Create your models here.

class Video(models.Model):
    video_title = models.CharField(max_length=200)
    video_description = models.TextField
    video_img = models.URLField()
    video_view = models.FloatField()
    video_dm = models.FloatField()
    video_share = models.FloatField()
    video_like = models.FloatField()
    video_collect = models.FloatField()
    video_coin = models.FloatField()
    video_pub_time = models.DateTimeField()

    up_img = models.URLField()
    up_fans = models.FloatField()
    up_name = models.CharField(max_length=200)
    up_desciption = models.TextField()

    def __str__(self):
        return self.video_title

    def get_absolute_url(self):
        return reverse('video_detail', args=[str(self.id)])
