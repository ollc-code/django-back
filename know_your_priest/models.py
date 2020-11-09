from django.db import models

# Create your models here.

class Priest(models.Model):
    name = models.CharField(max_length = 100)
    date = models.DateField()
    ordained = models.DateField()
    about = models.CharField(max_length=1000)
    associations = models.CharField(max_length=500)

    def __str__(self):
        return self.name