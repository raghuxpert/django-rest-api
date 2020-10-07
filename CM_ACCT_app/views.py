from rest_framework import viewsets
from .models import CmAcct
from .serializers import CmAcctSerializer
from django.http import HttpResponse, JsonResponse

def cmacctlist(request):
    cms = CmAcct.objects.all()
    serial = CmAcctSerializer(cms, many=True)
    return JsonResponse(serial.data, safe=False)