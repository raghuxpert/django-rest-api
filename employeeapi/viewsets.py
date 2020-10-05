from rest_framework import viewsets
from . import models
from . import serializers

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer

class EmployeeViewset_fullname(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer_fullname

class CM_ACCT_Viewset(viewsets.ModelViewSet):
    queryset = models.CmAcct.objects.all()
    serializer_class = serializers.CM_ACCT_Serializer