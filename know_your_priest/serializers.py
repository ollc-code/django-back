from rest_framework import serializers
from .models import Priest

class PriestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Priest
        fields = ['name', 'date', 'ordained', 'about', 'associations']
    

