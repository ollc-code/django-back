from user.models import CustomUser
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core import serializers
from manageuser.helpers import change_password


class ManageUsers(APIView):
    permission_classes = ()

    def get(self, request):
        if request.user.is_staff and request.user.is_authenticated:
            U = CustomUser.objects.get(id = request.user.id)
            user = serializers.serialize("json", [U], fields=('username', 'name', 'email'))

            return Response(user)
        else:
            return Response(False)

    def post(self, request):
        if request.user.is_staff and request.user.is_authenticated:
            action = request.data["action"]
            U = CustomUser.objects.get(id = request.user.id)

            if action == "edit_basic":
                name = request.data["name"]
                username = request.data["username"]
                email = request.data["email"]

                U.name = name
                U.email = email
                U.username = username
                try:
                    U.save()
                    return Response(True)
                except Exception as e:
                    print(e)
                    return Response(False)

            elif action == "change_pwd":
                current_password = request.data["current_password"]
                new_password = request.data["new_password"]

                result = change_password(request.user.username, current_password, new_password)

                return Response(result)

        return Response(False)
    
    '''
    def delete(self, request, year, month, day, reading="*"):
        date = "%d-%d-%d"%(int(year), int(month), int(day))

        if True:
            result = delete_reading(date, reading)
            return Response(result)
    
        return Response(False)'''
        