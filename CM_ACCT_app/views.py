from rest_framework import viewsets
from . import models
from . import serializers

class CmAcctViewset(viewsets.ModelViewSet):
    queryset = models.CmAcct.objects.all()
    serializer_class = serializers.CmAcctSerializer