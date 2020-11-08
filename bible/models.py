from django.db import models

# Create your models here.

class Reading(models.Model):
    date = models.DateField(null = False)
    reading = models.CharField(max_length = 50, null = False)
    book = models.CharField(max_length = 100, null = False)


class ReadingVerse(models.Model):
    reading = models.ForeignKey(Reading, on_delete = models.CASCADE)
    chapter = models.IntegerField()
    start_verse = models.IntegerField()
    end_verse = models.IntegerField()