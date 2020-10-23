from bible.rest import views as bible_views
from django.urls import path, include
from django.contrib import admin

### urls for bible app

urlpatterns = [
    path('all/', bible_views.Bible.as_view(), name='bible'),
    path('todays_read/', bible_views.ReadingsToday.as_view(), name='todays_read'),
]