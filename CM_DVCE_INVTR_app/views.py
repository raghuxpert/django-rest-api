from rest_framework import viewsets
# from django.db.models import Max
from . import serializers
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import CmDvceInvtr
from .serializers import CmDvceInvtrSerializer, CmDvceInvtrSerializerlist

def cmdvceinvtrlist(request):
    cms = CmDvceInvtr.objects.all()
    serial = CmDvceInvtrSerializerlist(cms, many=True)
    return JsonResponse(serial.data, safe=False)

def cmdvceinvtronerequest(request):
    cm = CmDvceInvtr.objects.get(pk=1)
    serial = CmDvceInvtrSerializer(cm)
    return JsonResponse(serial.data)

class CmDvceInvtrViewset(viewsets.ModelViewSet):
    queryset = CmDvceInvtr.objects.all()
    serializer_class = serializers.CmDvceInvtrSerializer
