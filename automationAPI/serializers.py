from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import appointments, emergency

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ApiVersionV1_Appointments(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = appointments
        fields = ['userid', 'token', 'name', 'department', 'date']

class ApiVersionV1_Emergency(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = emergency
        fields = ['userid', 'etoken', 'name', 'department', 'edate']
