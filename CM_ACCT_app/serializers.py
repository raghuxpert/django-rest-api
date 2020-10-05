from rest_framework import serializers
from .models import CmAcct

class CmAcctSerializer(serializers.ModelSerializer):
    class Meta:
        model =CmAcct
        fields = '__all__'

