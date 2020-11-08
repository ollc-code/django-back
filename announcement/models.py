from django.db import models

# Create your models here.

class Announcement(models.Model):
    text = models.CharField(max_length = 1000)