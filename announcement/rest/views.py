from announcement.helpers import set_announcements, cache_todays_announcements, delete_announcement
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
import json

# Create your views here.

''' Today's announcements cached '''
TODAY_ANNOUNCEMENTS = False


### gets or sets today's announcements
class TodayAnnouncements(APIView):
    permission_classes = ()

    def get(self, request):
        global TODAY_ANNOUNCEMENTS
        if not TODAY_ANNOUNCEMENTS:
            TODAY_ANNOUNCEMENTS = cache_todays_announcements()

        return Response(TODAY_ANNOUNCEMENTS)
    
    def post(self, request):
        global TODAY_ANNOUNCEMENTS
        
        #if request.user.is_staff and request.user.is_authenticated:
        if True:
            announcements = request.data["announcements"]

            result = set_announcements(announcements)
            #print(result)
            TODAY_ANNOUNCEMENTS = cache_todays_announcements()
            return Response(result)
        return Response(False)

    def delete(self, request, pk, format = None):
        global TODAY_ANNOUNCEMENTS
        #if request.user.is_staff and request.user.is_authenticated:
        try:
            result = delete_announcement(pk)
            #print(result)
            TODAY_ANNOUNCEMENTS = cache_todays_announcements()
            return Response(result)
        except:
            return Response(False)