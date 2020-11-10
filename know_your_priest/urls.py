from django.urls import path
from .views import PriestAPIView

urlpatterns = [
    path('priest/', PriestAPIView.as_view()),
    path('priest/<int:pk>/', PriestAPIView.as_view()),
]