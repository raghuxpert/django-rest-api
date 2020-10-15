from rest_framework import viewsets
from django.db.models import Q, Subquery, F
from rest_framework.decorators import api_view
from rest_framework.response import Response
from CM_DVCE_DSGN_app.models import CmDvceDsgn


from . import serializers
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import CmDvceInvtr
from .serializers import CmDvceInvtrSerializer, CmDvceInvtrSerializerlist

'''To fetch list of cards for given account number'''
'''Here we are using JsonResponse'''
def cmdvceinvtrlist(request, acct):
    cms = CmDvceInvtr.objects.filter(account__exact=acct)
    print(str(cms.query)) # To display SQL query
    serial = CmDvceInvtrSerializerlist(cms, many=True)
    return JsonResponse(serial.data, safe=False)

'''To fetch one unique record matching given criteria'''
'''Here we are using Response'''
@api_view(['GET', 'POST'])
def cmdvceinvtronerequest(request, acct, seq):
    cm = CmDvceInvtr.objects.get(account__exact=acct, seq_nbr__exact=seq) # AND condition
    # cm = CmDvceInvtr.objects.filter(Q(account__exact=acct)|Q(seq_nbr__exact=seq)) # OR condition
    serial = CmDvceInvtrSerializer(cm)
    return Response(serial.data)

'''To fetch all entries available in inventory table'''
@api_view(['GET', 'POST'])
def CmDvceInvtrViewset(request):
    qs = CmDvceInvtr.objects.all()
    serial = CmDvceInvtrSerializerlist(qs, many=True)
    return Response(serial.data)

'''To perform subquery'''
'''Fetch all cards having metal design'''
@api_view(['GET', 'POST'])
def CmMetalViewset(request):
    design = CmDvceDsgn.objects.filter(material_type__exact = 'M')
    # print(design.values('dsgn_cde'))
    qs = CmDvceInvtr.objects.filter(design_cde__in = Subquery(design.values('dsgn_cde')))
    print(str(qs.query))
    serial = CmDvceInvtrSerializerlist(qs, many=True)
    return Response(serial.data)

'''compare queryset field values'''
@api_view(['GET', 'POST'])
def CmFilterViewset(request):
    qs = CmDvceInvtr.objects.filter(emer_ind = F('cm_rrc'))
    print(str(qs.query))
    serial = CmDvceInvtrSerializerlist(qs, many=True)
    return Response(serial.data)