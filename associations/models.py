from django.db import models

# Create your models here.

class Associations(models.Model):
    association_name = models.CharField(max_length=100)
    incharge = models.CharField(max_length=100)
    about = models.CharField(max_length=500)
    contacts = models.CharField(max_length=300)
    
    def __str__(self):
        return self.association_name
    
    
    