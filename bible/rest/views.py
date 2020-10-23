from rest_framework.permissions import IsAuthenticated, IsAdminUser
from bible.reading_getter import runner, today_reading_setter
from orlem_connect.settings import STATIC_DIR
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from bible.models import Reading
from datetime import date
import pandas as pd
import json

# Create your views here.

TODAY_READINGS = False

### bible api, currently, the entire bible
class Bible(APIView):
    permission_classes = ()

    def get(self, request):
        df = pd.read_csv(STATIC_DIR / 'res/nrsv.csv')
        # res = df.head().to_json(orient='records')
        return Response(df.to_json())

### gets or sets today's reading
class ReadingsToday(APIView):
    permission_classes = ()

    def get(self, request):
        global TODAY_READINGS
        if not TODAY_READINGS:
            TODAY_READINGS = today_reading_setter()
        
        return Response(TODAY_READINGS)
    
    def post(self, request):
        global TODAY_READINGS
        
        if request.user.is_staff and request.user.is_authenticated:
            date = request.data["date"] ### YEAR-MONTH-DAY
            reading = request.data["reading"]
            book = request.data["book"]
            content = request.data["content"]
            #print(date)

            ### get today's readings
            R = Reading.objects.filter(date = date, reading = reading).first()
            #print(date); print(book); print(content)
            if R:
                R.book = book
                R.content = content
                R.save()
                return Response(True)
            else:
                R = Reading(date = date, reading = reading, book = book, content = content)
                R.save()                
                return Response(True)
        else:
            return Response(False)