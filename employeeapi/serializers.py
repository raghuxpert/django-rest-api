from rest_framework import serializers
from .models import Employee, CmAcct

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model =Employee
        fields = '__all__'

class EmployeeSerializer_fullname(serializers.ModelSerializer):
    class Meta:
        model =Employee
        # fields = ('fullname','emp_code')
        fields = ['fullname']

class CM_ACCT_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CmAcct
        fields = '__all__'