from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .models import CmAcct, Comment
from .serializers import CmAcctSerializer, CommentSerializer
from django.http import HttpResponse, JsonResponse

@api_view(['GET', 'POST'])
def cmacct(request, pk):
    if request.method == 'GET':
        cms = CmAcct.objects.get(pk=pk)
        serial = CmAcctSerializer(cms)
        # print(serial.data)
        # return JsonResponse(serial.data, safe=False)
        return Response(serial.data)


def cmacctwp(request):
    if request.method == 'GET':

        cms = CmAcct.objects.get(pk=pk)
        serial = CmAcctSerializer(cms)
        # print(serial.data)
        return JsonResponse(serial.data, safe=False)

@csrf_exempt
def cmacctlist(request):
    if request.method == 'GET':
        cms = CmAcct.objects.all()
        serial = CmAcctSerializer(cms, many=True)
        # print(serial.data)
        return JsonResponse(serial.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print('request : ', request)
        print('data : ', data)
        serial = CmAcctSerializer(data=data)
        if serial.is_valid():
            serial.save()
            return JsonResponse(serial.data, status=201)
        return JsonResponse(serial.errors, status=400)

def comment(request):
    comment = Comment(email='raghav@example.com', content='rag bar')
    serializer = CommentSerializer(comment)
    return JsonResponse(serializer.data, safe=False)

def commentlist(request):
    comment1 = Comment(email='raghav1@example.com', content='rag1 bar')
    comment2 = Comment(email='raghav2@example.com', content='rag2 bar')
    comment3 = Comment(email='raghav3@example.com', content='rag3 bar')
    l = [comment1, comment2, comment3]
    serializer = CommentSerializer(l, many=True)
    return JsonResponse(serializer.data, safe=False)
