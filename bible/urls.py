from bible.rest import views as bible_views
from django.urls import path, include, re_path
from django.contrib import admin

### urls for bible app

urlpatterns = [
    #path('all/', bible_views.Bible.as_view(), name='bible'),
    path(
        'readings/today/', bible_views.ReadingsToday.as_view(), name='todays_read'
         ),
    re_path(
        r'readings/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/(?P<reading>\w*)/' ,
        bible_views.Readings.as_view(), name="readings"
        ),
    re_path(
        r'readings/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/',
        bible_views.Readings.as_view(), name="readings"
        ),
]