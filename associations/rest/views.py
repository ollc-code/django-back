from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from associations.models import Associations
from associations.serializers import AssocSerializer

# Create your views here.
class AssociationDetails(APIView):
    
    permission_classes = ()
    
    def get(self, request):
        assoc_get = Associations.objects.all()
        serializer = AssocSerializer(assoc_get)
        return Response(serializer.data)
    

# @api_view(['GET'])
# def get(self, request):
#     assoc_get = Associations.objects.all()
#     serializer = AssocSerializer(assoc_get)
#     return Response(serializer.data)
    
        
         