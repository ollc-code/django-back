from django.urls import path
from .views import PriestAPIView

urlpatterns = [
    path('priests/', PriestAPIView.as_view()),
    path('priests/<int:pk>/', PriestAPIView.as_view()),
]