from associations.rest import views as associations_views
from django.urls import path, include

### urls for announcement app

urlpatterns = [
    path('', associations_views.AssociationDetails.as_view(), name='associations'),
]