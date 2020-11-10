from announcement.rest import views as announcement_views
from django.urls import path, include

### urls for announcement app

urlpatterns = [
    path('', announcement_views.TodayAnnouncements.as_view(), name='today_announcements'),
    path('<int:pk>/', announcement_views.TodayAnnouncements.as_view(), name='today_announcements'),
]