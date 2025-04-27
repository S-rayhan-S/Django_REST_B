from rest_framework import serializers
from status.models import Status
from django.contrib.auth.models import User

# to nest user info & then send through Status serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id', 'username', 'email']

class StatusSerializer(serializers.ModelSerializer):
    # user=UserSerializer(many=False)
    class Meta:
        model = Status
        fields = ['id', 'text', 'created_at', 'image_link', 'user']