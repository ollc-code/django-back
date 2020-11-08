from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from announcement.models import Announcement
import json

# Create your views here.

''' Today's announcements cached '''
TODAY_ANNOUNCEMENTS = False


def set_announcements(announcements):
    Announcement.objects.all().delete()
    try:
        for a in announcements:
            print(a)
            A = Announcement(text = a)
            A.save()
    except Exception as e:
        print(e)
        return False
    return True


def cache_todays_announcements():
    announcements = []

    A = Announcement.objects.all()
    for a in A:
        announcements.append(a.text)
    
    print(announcements)

    return announcements


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
        
        if request.user.is_staff and request.user.is_authenticated:
            announcements = request.data["announcements"]

            result = set_announcements(announcements)
            #print(result)
            TODAY_ANNOUNCEMENTS = cache_todays_announcements()
            return Response(result)
        return Response(False)