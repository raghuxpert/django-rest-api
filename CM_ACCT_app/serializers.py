from rest_framework import serializers
from .models import CmAcct

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

class CmAcctSerializer(serializers.ModelSerializer):
    class Meta:
        model =CmAcct
        fields = '__all__'

