from announcement.models import Announcement
from django.core import serializers


def set_announcements(announcements):
    try:
        for a in announcements:
            #print(a)
            A = Announcement(text = a)
            A.save()
    except Exception as e:
        #print(e)
        return False
    return True

def delete_announcement(id):
    try:
        if id == "*": #delete all announcements
            Announcement.objects.all().delete()
        else:
            Announcement.objects.get(id = id).delete()
    except:
        return False
    return True

def cache_todays_announcements():
    announcements = []
    announcements = serializers.serialize("json", Announcement.objects.all())
    return announcements
