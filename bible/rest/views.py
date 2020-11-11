from rest_framework.permissions import IsAuthenticated, IsAdminUser
from bible.helpers import add_reading, cache_todays_reading, get_reading, delete_reading
from orlem_connect.settings import STATIC_DIR
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
import pandas as pd
import json

# Create your views here.

''' Today's reading cached '''
TODAY_READINGS = False

### bible api, currently, the entire bible
'''class Bible(APIView):
    permission_classes = ()

    def get(self, request):
        df = pd.read_csv(STATIC_DIR / 'res/nrsv.csv')
        # res = df.head().to_json(orient='records')
        return Response(df.to_json())'''

### gets or sets today's reading
class ReadingsToday(APIView):
    permission_classes = ()

    def get(self, request):
        global TODAY_READINGS
        if not TODAY_READINGS:
            TODAY_READINGS = cache_todays_reading()

        return Response(TODAY_READINGS)
    
    
class Readings(APIView):
    permission_classes = ()

    def get(self, request, year, month, day):
        date = "%s-%s-%s"%(year, month, day)
        result = get_reading(date)

        return Response(result)
    
    def post(self, request, year, month, day):
        date = "%s-%s-%s"%(year, month, day)
        
        #if request.user.is_staff and request.user.is_authenticated:
        if True:
            reading = request.data["reading"]
            book = request.data["book"]
            content = request.data["content"]

            result = add_reading(date, reading, book, content)   
            return Response(result)
        return Response(False)
    
    def delete(self, request, year, month, day, reading="*"):
        date = "%s-%s-%s"%(year, month, day)

        if True:
            result = delete_reading(date, reading)
            return Response(result)
    
        return Response(False)
        