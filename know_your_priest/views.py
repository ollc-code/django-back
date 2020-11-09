from django.shortcuts import render
from .models import Priest
from .serializers import PriestSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

class PriestAPIView(APIView):
    def get(self, request):
        priest = Priest.objects.first()
        serializer = PriestSerializer(priest)
        return Response(serializer.data)

