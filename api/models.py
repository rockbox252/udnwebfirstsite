from django.db import models
from accounts.models import *
from django.utils import timezone

# Create your models here.
class Information(models.Model):
    android_id = models.CharField(max_length=200)
    advertiser_name = models.CharField(max_length=200)
    video_count = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200) 
    time = models.DateTimeField(default=timezone.now)
    
 