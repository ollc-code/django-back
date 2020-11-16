from manageuser.rest import views as manageuser_views
from django.urls import path, include, re_path

### urls for bible app

urlpatterns = [
    path(
        '', manageuser_views.ManageUsers.as_view(), name='manage_users'
         ),
]