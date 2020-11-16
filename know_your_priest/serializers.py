from rest_framework import serializers
from .models import Priest

class PriestSerializer(serializers.ModelSerializer):
    profile_pic = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Priest
        fields = "__all__"
    

