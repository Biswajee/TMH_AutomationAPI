from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import appointments

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ApiVersionV1_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = appointments
        fields = ['userid', 'token', 'name', 'department', 'date']
