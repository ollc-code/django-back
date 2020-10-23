from django.db import models

# Create your models here.

class Reading(models.Model):
    date = models.DateField(null = False)
    reading = models.CharField(max_length = 50, null = False)
    book = models.CharField(max_length = 100, null = False)
    content = models.CharField(max_length = 500, null = False)