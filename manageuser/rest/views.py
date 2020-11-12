from rest_framework.permissions import IsAuthenticated, IsAdminUser
from orlem_connect.settings import STATIC_DIR
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from user.models import CustomUser
from django.core import serializers

# Create your views here.


class ManageUsers(APIView):
    permission_classes = ()

    def get(self, request):

        U = CustomUser.objects.all()
        users = serializers.serialize("json", U, fields=('username', 'name'))

        return Response(users)
    '''
    def post(self, request, year, month, day):
        date = "%d-%d-%d"%(int(year), int(month), int(day))
        
        #if request.user.is_staff and request.user.is_authenticated:
        if True:
            reading = request.data["reading"]
            book = request.data["book"]
            content = request.data["content"]

            result = add_reading(date, reading, book, content)   
            return Response(result)
        return Response(False)
    
    def delete(self, request, year, month, day, reading="*"):
        date = "%d-%d-%d"%(int(year), int(month), int(day))

        if True:
            result = delete_reading(date, reading)
            return Response(result)
    
        return Response(False)'''
        