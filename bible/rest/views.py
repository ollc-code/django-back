from rest_framework.permissions import IsAuthenticated, IsAdminUser
from bible.helpers import add_reading, cache_todays_reading
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
    
    def post(self, request):
        global TODAY_READINGS
        
        if request.user.is_staff and request.user.is_authenticated:
            date = request.data["date"] ### YEAR-MONTH-DAY
            reading = request.data["reading"]
            book = request.data["book"]
            content = request.data["content"]

            result = add_reading(date, reading, book, content) 
                
        return Response(result)