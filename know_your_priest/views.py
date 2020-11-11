from django.shortcuts import render
from .models import Priest
from .serializers import PriestSerializer

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
import json

class PriestAPIView(APIView):
    
    permission_classes = ()
    
    def get(self, request):
        priest = Priest.objects.all()
        serializer = PriestSerializer(priest, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        r = request.data
        print(r)
        if r['type'] == 'insert':
            try:
                make_priest = Priest(name = r['name'], profile_pic=r['file'],date_of_birth=r['date_of_birth'],
                    ordained=r['ordained'], about=r['about'], associations=r['associations'])
                make_priest.save()
            except Exception:
                return Response('Insert Failed')
        elif r['type'] == 'update':
            try:
                Priest.objects.filter(pk=r['id']).update(
                    name = r['name'], profile_pic=r['file'],date_of_birth=r['date_of_birth'],
                    ordained=r['ordained'], about=r['about'], associations=r['associations']
                )
            # print("Updated")
            except Exception:
                return Response('Update Failed')
        else:
            return Response('Invalid operation')
        return Response(True)
    
    def delete(self, request, pk, format=None):
        try:
            x = Priest.objects.get(pk=pk).profile_pic.delete()
            Priest.objects.get(pk=pk).delete()
        except Exception:
            return Response(False)
        return Response(True)

