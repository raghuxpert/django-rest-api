from rest_framework import serializers
from .models import CmDvceInvtr

class CmDvceInvtrSerializer(serializers.ModelSerializer):
    class Meta:
        model =CmDvceInvtr
        fields = '__all__'
        # fields = 'account', 'seq_nbr', 'cm_name'

class CmDvceInvtrSerializerlist(serializers.ModelSerializer):
    class Meta:
        model =CmDvceInvtr
        fields = '__all__'
        # fields = 'account', 'seq_nbr', 'cm_name'