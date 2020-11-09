from .models import Associations
from rest_framework import serializers


class AssocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Associations
        fields = '__all__'
        